"""Assemble a portable query from CSV and source; this does not execute DAX."""

import csv
from dataclasses import dataclass
from decimal import Decimal
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Line:
    product: str
    region: str
    quantity: int
    price: Decimal
    cost: Decimal


def read_fixture(path: Path) -> list[Line]:
    with path.open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != ["Product", "Region", "Quantity", "UnitPrice", "UnitCost"]:
            raise ValueError("Unexpected fixture CSV schema")
        rows = []
        for record in reader:
            if None in record or any(value is None for value in record.values()):
                raise ValueError("Fixture CSV row contains extra or missing values")
            row = Line(
                record["Product"], record["Region"], int(record["Quantity"]),
                Decimal(record["UnitPrice"]), Decimal(record["UnitCost"]),
            )
            if not row.product.strip() or not row.region.strip() or not 0 < row.quantity <= 9223372036854775807:
                raise ValueError("Fixture labels must be nonblank and quantity a positive whole number")
            for amount in (row.price, row.cost):
                if not amount.is_finite() or not 0 <= amount <= Decimal("922337203685477.5807"):
                    raise ValueError("Fixture amounts must be finite, nonnegative CURRENCY values")
                if amount.normalize().as_tuple().exponent < -4:
                    raise ValueError("CURRENCY amounts support at most four decimal places")
            if row.price == 0:
                raise ValueError("This row-margin exercise requires positive unit prices")
            rows.append(row)
    if not rows or len({row.product for row in rows}) != len(rows):
        raise ValueError("The practice fixture requires nonempty, distinct product lines")
    return rows


def reference(rows: list[Line]) -> dict[str, Decimal | int]:
    revenue = sum((row.quantity * row.price for row in rows), Decimal(0))
    cost = sum((row.quantity * row.cost for row in rows), Decimal(0))
    north = [row for row in rows if row.region == "North"]
    return {
        "revenue": revenue,
        "cost": cost,
        "profit": revenue - cost,
        "units": sum(row.quantity for row in rows),
        "lines": len(rows),
        "north_revenue": sum((row.quantity * row.price for row in north), Decimal(0)),
        "north_lines": len(north),
        "gross_margin": (revenue - cost) / revenue,
        "unweighted_row_margin": sum(((row.price - row.cost) / row.price for row in rows), Decimal(0)) / len(rows),
    }


def dax_string(value: str) -> str:
    return '"' + value.replace('"', '""') + '"'


def build(root: Path = ROOT) -> Path:
    rows = read_fixture(root / "examples/items.csv")
    literals = ",\n".join(
        f"        {{ {dax_string(row.product)}, {dax_string(row.region)}, {row.quantity}, {row.price:f}, {row.cost:f} }}"
        for row in rows
    )
    declaration = (
        "// Generated from examples/items.csv and examples/analysis-body.dax.\n"
        "DEFINE\nVAR Items =\nDATATABLE (\n"
        '    "Product", STRING,\n    "Region", STRING,\n    "Quantity", INTEGER,\n'
        '    "UnitPrice", CURRENCY,\n    "UnitCost", CURRENCY,\n'
        "    {\n" + literals + "\n    }\n)\n\n"
    )
    body = (root / "examples/analysis-body.dax").read_text(encoding="utf-8").strip()
    if not body:
        raise ValueError("The analysis query body is empty")
    destination = root / "docs/downloads"
    destination.mkdir(parents=True, exist_ok=True)
    query = destination / "first-analysis.dax"
    query.write_text(declaration + body + "\n", encoding="utf-8")
    with ZipFile(destination / "dax-overview-examples.zip", "w", compression=ZIP_DEFLATED) as archive:
        archive.write(query, "first-analysis.dax")
        for filename in ("items.csv", "analysis-body.dax", "expected-results.json", "README.md"):
            archive.write(root / "examples" / filename, "source/" + filename)
        archive.write(root / "LICENSE", "LICENSE")
        archive.writestr(
            "README.txt",
            "DAX Overview\nRun the complete first-analysis.dax against a real DAX engine.\n"
            "It contains a query-scoped DATATABLE and three EVALUATE result sets.\n"
            "https://brown9804.github.io/DAX-Overview/getting-started.html\n"
            "CI checks data arithmetic and packaging, not DAX engine execution.\n",
        )
    return query


if __name__ == "__main__":
    query = build()
    print(f"Generated complete query and ZIP: {query.name}")
    print("Packaging/data checks do not execute DAX.")
