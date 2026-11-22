# Essential functions and calculation patterns

The snippets here are **model measures** using the companion hub's Sales,
DimProduct, and DimRegion tables. Import its model and use its canonical
measure library for report practice. They are not declarations for the
temporary Items table in the Overview query.

## Aggregations versus iterators

SUM adds a stored numeric column. SUMX evaluates a row expression then adds
results. COUNTROWS counts rows; DISTINCTCOUNT counts distinct column values.
An ID representing transaction lines does not automatically count orders.

| Need | Function/pattern | Main question |
| --- | --- | --- |
| Add amounts | SUM | Is the stored amount already correct at this grain? |
| Compute row arithmetic | SUMX | Is the expression truly row-dependent? |
| Count rows | COUNTROWS | What does one row represent? |
| Count unique IDs | DISTINCTCOUNT | Are blank IDs possible? |
| Divide safely | DIVIDE | Should an undefined ratio be blank or an explicit alternative? |

For Import mode, storing amounts can simplify measures, but do not assume
SUMX is always slower. Compare actual engine timings under equivalent results.

## CALCULATE: replacement versus intersection

```dax
North Revenue =
CALCULATE ( [Revenue], DimRegion[Region] = "North" )
```

The Boolean filter replaces an existing filter on that same Region column.
It does not remove every filter in the model. In the companion dataset,
under South selection this returns North Revenue **4100**, not South 5400.

```dax
North Within Selection =
CALCULATE (
    [Revenue],
    KEEPFILTERS ( DimRegion[Region] = "North" )
)
```

KEEPFILTERS intersects Region conditions. South intersect North has no rows;
the companion measure is BLANK. These **4100/5400** values belong to the larger
companion dataset, not the Overview fixture's **1150/100** split.

## Denominators communicate business intent

```dax
All Products Revenue =
CALCULATE ( [Revenue], REMOVEFILTERS ( DimProduct ) )
```

This clears Product and Category filters on DimProduct while retaining other
dimensions such as Region and Date. Clearing only ProductName is a different
business definition when Category is filtered.

ALLSELECTED can retain outside selections while removing visual grouping
context. It is not interchangeable with ALL or REMOVEFILTERS. Compare query
and visual results only under equivalent external filters.

## Variables are evaluated values

```dax
Gross Profit =
VAR CurrentRevenue = [Revenue]
VAR CurrentCost = [Cost]
RETURN
    CurrentRevenue - CurrentCost
```

Variables improve readability and can avoid repeated evaluation. But a scalar
variable is not a delayed formula:

```dax
Unexpected Denominator =
VAR CurrentRevenue = [Revenue]
RETURN
    CALCULATE ( CurrentRevenue, REMOVEFILTERS ( DimProduct ) )
```

This does not recalculate Revenue after removing product filters. Use the
measure expression inside CALCULATE when a new context evaluation is intended.

## Blanks and ratios

Use `DIVIDE([Gross Profit], [Revenue])` for margin. Its default result when
the denominator is zero/blank is BLANK; an explicit alternate such as 0 has
different reporting meaning. Avoid changing undefined results to zero merely
to hide a modeling error.

Continue with the companion
[CALCULATE lesson](https://cloud2br-msftlearninghub.github.io/DAX-For-Everyone/calculate.html)
and [ratio/ranking patterns](https://cloud2br-msftlearninghub.github.io/DAX-For-Everyone/ratios-rankings.html).
