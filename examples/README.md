# Overview example sources

`items.csv` contains three artificial transaction lines. Amounts share one
unspecified demonstration currency. `analysis-body.dax` contains three
EVALUATE sections referencing a query-scoped Items variable.

**Do not run the body alone.** From a checkout run:

```shell
python scripts/build_downloads.py
```

Open `docs/downloads/first-analysis.dax`, including its generated DEFINE VAR
Items declaration. Run all statements in DAX query view or DAX Studio connected
to a real engine. The table is query-scoped, not a persisted model update.

Alternatively use the [website download](https://brown9804.github.io/DAX-Overview/getting-started.html).
The ZIP includes the complete query, original sources, CSV, expectations, and
original GPL-3.0 license.

Expected totals: Revenue 1250, Cost 840, Profit 410, Units 9, Lines 3.
North Revenue 1150, North Lines 2. Aggregate margin 32.8%, unweighted row
margin 40%. Default zero division is BLANK; explicit alternate returns 0.

Changing Keyboard quantity from 3 to 4 yields Revenue 1300, Cost 870,
Profit 430, Units 10, and North Revenue 1200. Restore the fixture afterward.
CI checks independent data arithmetic and packaging, **not DAX execution**.
