# Maintenance and verification

## Run repository checks

From a repository checkout using Python 3.12:

```shell
python -m unittest discover -s scripts -p "test_*.py"
python scripts/build_downloads.py
python -m pip install -r requirements.txt
mkdocs build --strict
python scripts/check_site.py
```

Python checks independently compute fixture totals and ratios, reject invalid
rows, and verify that generated query/ZIP data remain synchronized with CSV
and source changes. They **do not execute DAX** or establish model-measure
correctness. The website checker verifies local HTML links, fragments, and assets.

## Canonical sources

- `examples/items.csv`: the three invented transaction lines.
- `examples/analysis-body.dax`: three EVALUATE result sections.
- `examples/expected-results.json`: independent baseline expectations.
- `scripts/build_downloads.py`: assembles the DATATABLE declaration and source
  body into a complete downloadable query and portable package.

Do not manually edit generated `docs/downloads/` files. Update the fixture,
source, affected expected results, and lessons together. Keep the raw source
body clearly distinguished from the directly executable assembled download.

## Actual DAX execution

Run the complete query against a real available engine. Record client/engine
versions, the three result sets, the controlled quantity-change results, and
whether BLANK differs from explicit zero. For model-dependent snippets, import
the companion fixture and record relationships/filter context.

No DAX engine is provisioned by CI. Do not describe Python tests or a
Markdown build as DAX compilation/runtime validation.

## Publishing

Pull requests validate without Pages write permissions. Main pushes and
manual main runs build/check the website and then deploy to GitHub Pages.
No Power BI models, paid cloud resources, or production credentials are created.

Keep the root README GitHub-compatible; MkDocs-only snippet/button syntax
belongs under `docs/`. Preserve the original GPL-3.0 license and continue
linking to the companion library instead of copying it wholesale.
