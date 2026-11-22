# Calculation objects and context

DAX is an expression language for tabular models, not a replacement for SQL
or Power Query. SQL retrieves/transforms data in databases; Power Query
prepares data for a model; DAX defines analytical calculations over that model.
The tools can be complementary rather than competing choices.

## Choose the correct object

| Object | Evaluation/use | Example |
| --- | --- | --- |
| Measure | Calculated when requested under filter context | Revenue in a region visual |
| Calculated column | One value per row; in Import models stored and refreshed with the model | Row-level sales amount |
| Calculated table | A model table calculated during processing/refresh where supported | Calendar table |
| Query | Returns one or more tables through EVALUATE | Our first-analysis download |
| RLS rule | Boolean expression restricting visible rows for a role | Allowed regions |

Do not paste EVALUATE into New measure, or treat a slicer-sensitive measure
as a stored column. Storage mode/product restrictions differ: review function
documentation before adapting examples to DirectQuery or RLS.

## Filter context: which rows are eligible?

Using the Overview fixture, unrestricted revenue is 1250. A Region=North
filter leaves Laptop and Keyboard, so revenue is 1150. Report visual groups,
slicers, page/report filters, relationships, and DAX filter modifications all
contribute to context.

On a properly related model, the reusable measure could be:

```dax
Revenue = SUM ( Sales[SalesAmount] )
```

This example needs a **Sales** model table with a stored SalesAmount column.
It is not directly runnable against the temporary Items variable.

## Row context: which row is being visited?

SUMX visits eligible rows and evaluates an expression for each:

```dax
Revenue Iterator =
SUMX ( Sales, Sales[Quantity] * Sales[UnitPrice] )
```

Filter context first determines eligible rows; the iterator then supplies
row context. Row context alone does not automatically filter unrelated
aggregations or traverse every model relationship.

## Context transition

CALCULATE converts an existing row context into filter context. A model
measure invoked within an iterator performs automatic context transition:

```dax
Sum Of Product Revenue =
SUMX ( VALUES ( DimProduct[ProductKey] ), [Revenue] )
```

With an active dimension-to-fact relationship, each product row becomes a
filter for Revenue. Replacing `[Revenue]` with a naked `SUM(Sales[SalesAmount])`
does not automatically perform the same transition; it may repeat the
broader total for every product.

This model-dependent snippet assumes unique product keys and an active
one-to-many DimProduct-to-Sales relationship. Adapt names to your model.
For a reproducible setup, follow
[DAX for Everyone context lessons](https://cloud2br-msftlearninghub.github.io/DAX-For-Everyone/context.html).

## A total is another evaluation

The total row of a visual re-evaluates a measure in total context. Ratios,
distinct counts, and rankings are not generally additive. Ask what the total
should mean before deciding that a differing total is wrong.
