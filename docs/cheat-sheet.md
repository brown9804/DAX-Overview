# DAX quick reference

| Question | Starting point | Watch for |
| --- | --- | --- |
| Add a stored amount? | SUM | Correct column and transaction grain |
| Calculate per-row values? | SUMX | Row expression and eligible rows |
| Return a table? | EVALUATE | Query surface, not New measure |
| Change measure filters? | CALCULATE | Same-column replacement and context transition |
| Intersect a filter? | KEEPFILTERS | Empty intersections may return BLANK |
| Clear product filters? | REMOVEFILTERS(DimProduct) | Entire dimension includes Category |
| Compare selected products? | ALLSELECTED | Outside selection versus visual grouping |
| Divide with zero/blank guard? | DIVIDE | Default BLANK versus explicit alternate |
| Calculate classic YTD? | TOTALYTD | Proper date table/relationship and calendar assumptions |
| Use shipment dates? | USERELATIONSHIP | Existing inactive relationship and RLS restrictions |
| Count transaction lines? | COUNTROWS / DISTINCTCOUNT | Row grain and duplicate/blank IDs |

## Before changing a formula

1. Identify the calculation object and exact input columns.
2. Confirm relationships and filter direction.
3. Explain the business definition and total behavior.
4. Capture the current filters, including page/report filters.
5. Reduce to a small query with independent expected values.
6. Measure performance only after correctness is established.

## Do not mix fixtures

| Metric | Overview three-line example | DAX for Everyone retail model |
| --- | ---: | ---: |
| Revenue | 1250 | 9500 |
| Cost | 840 | 6420 |
| Profit | 410 | 3080 |
| North Revenue | 1150 | 4100 |
| Transaction lines | 3 | 12 |

Keep this distinction in your evidence log. The larger model is required for
the referenced time/relationship/RLS lessons.
