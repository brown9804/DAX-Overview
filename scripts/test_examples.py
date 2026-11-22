import json
import shutil
import tempfile
import unittest
from dataclasses import replace
from decimal import Decimal
from pathlib import Path
from zipfile import ZipFile

from build_downloads import ROOT, build, read_fixture, reference


class ExampleTests(unittest.TestCase):
    def test_independent_baseline_arithmetic(self):
        rows = read_fixture(ROOT / "examples/items.csv")
        observed = reference(rows)
        expected = json.loads((ROOT / "examples/expected-results.json").read_text(encoding="utf-8"))
        numeric = {key: Decimal(expected[key]) if isinstance(expected[key], str) else expected[key] for key in observed}
        self.assertEqual(observed, numeric)
        self.assertNotEqual(observed["gross_margin"], observed["unweighted_row_margin"])

    def test_quantity_change_matches_documented_exercise(self):
        rows = read_fixture(ROOT / "examples/items.csv")
        changed = [replace(row, quantity=4) if row.product == "Keyboard" else row for row in rows]
        result = reference(changed)
        self.assertEqual(
            {key: result[key] for key in ("revenue", "cost", "profit", "units", "north_revenue")},
            {"revenue": 1300, "cost": 870, "profit": 430, "units": 10, "north_revenue": 1200},
        )

    def test_rejects_invalid_quantity(self):
        with tempfile.TemporaryDirectory(prefix="dax-overview-") as directory:
            path = Path(directory) / "items.csv"
            text = (ROOT / "examples/items.csv").read_text(encoding="utf-8")
            path.write_text(text.replace("North,1,1000", "North,0,1000"), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "quantity"):
                read_fixture(path)

    def test_rejects_unrepresentable_currency_precision(self):
        with tempfile.TemporaryDirectory(prefix="dax-overview-") as directory:
            path = Path(directory) / "items.csv"
            text = (ROOT / "examples/items.csv").read_text(encoding="utf-8")
            path.write_text(text.replace("South,5,20,10", "South,5,20.00001,10"), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "four decimal"):
                read_fixture(path)

    def test_generated_query_tracks_source_and_escapes_csv_strings(self):
        with tempfile.TemporaryDirectory(prefix="dax-overview-") as directory:
            root = Path(directory)
            shutil.copytree(ROOT / "examples", root / "examples")
            shutil.copy2(ROOT / "LICENSE", root / "LICENSE")
            fixture = root / "examples/items.csv"
            fixture.write_text(
                fixture.read_text(encoding="utf-8").replace("Keyboard", '"Keyboard""Plus"""'),
                encoding="utf-8",
            )
            body = root / "examples/analysis-body.dax"
            body.write_text(body.read_text(encoding="utf-8") + "\n// Source synchronization check\n", encoding="utf-8")
            query = build(root)
            text = query.read_text(encoding="utf-8")
            self.assertIn('"Keyboard""Plus"""', text)
            self.assertTrue(text.startswith("// Generated"))
            self.assertIn("DEFINE\nVAR Items", text)
            self.assertIn("// Source synchronization check", text)
            with ZipFile(root / "docs/downloads/dax-overview-examples.zip") as archive:
                self.assertEqual(archive.read("first-analysis.dax"), query.read_bytes())
                self.assertEqual(archive.read("source/items.csv"), fixture.read_bytes())
                self.assertIn("LICENSE", archive.namelist())


if __name__ == "__main__":
    unittest.main()
