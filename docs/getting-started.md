# Your first DAX analysis

## Choose a tool

Use Power BI Desktop's **DAX query view** with a local practice file, or DAX
Studio connected to an available Power BI/Analysis Services model. DAX Studio
is a client, not a standalone DAX engine. Power Pivot supports DAX calculations
but does not provide the same query-view interface.

Our first query creates an in-query table. It does not require importing
the companion retail model or saving any measures.

## Inspect the synthetic data

| Product | Region | Quantity | Unit price | Unit cost |
| --- | --- | ---: | ---: | ---: |
| Laptop | North | 1 | 1000 | 700 |
| Mouse | South | 5 | 20 | 10 |
| Keyboard | North | 3 | 50 | 30 |

The grain is one invented transaction line. All amounts use one unspecified
demonstration currency. These are not customer records or complete orders.

## Download and run the complete query

[Download first-analysis.dax](downloads/first-analysis.dax){ .md-button .md-button--primary }
[Download query, CSV, expectations, and license](downloads/dax-overview-examples.zip){ .md-button }

Paste the **entire** query, including `DEFINE VAR Items`, into query view.
Run all three EVALUATE statements. A client may show separate results/tabs
or a result-set selector. If your client runs only a selection, retain the
DEFINE block and run one EVALUATE section at a time.

Website builds derive the DATATABLE declaration from the canonical CSV.
The source body below intentionally does not repeat the table declaration;
use the complete download for direct execution.

```dax
--8<-- "examples/analysis-body.dax"
```

## Expected results

| Result set | Expected values |
| --- | --- |
| 1: Totals | Revenue 1250; Cost 840; Profit 410; Units 9; Lines 3 |
| 2: North subset | North Revenue 1150; North Lines 2 |
| 3: Ratios | Gross Margin 0.328; Unweighted Row Margin 0.4; Default Zero Division BLANK; Explicit Zero 0 |

Query results are numeric decimals, not necessarily formatted percentages.
0.328 represents **32.8%**. A blank cell is not the text `"BLANK"` or zero.

Revenue is `1*1000 + 5*20 + 3*50`. North includes Laptop and Keyboard. Aggregate
profit is `1250-840`; aggregate margin is `410/1250`, not the average of
30%, 50%, and 40% row margins.

## Try a controlled change

In the downloaded table declaration, change Keyboard quantity from 3 to 4.
Predict Revenue **1300**, Cost **870**, Profit **430**, Units **10**, and
North Revenue **1200**. Run it and compare. Restore the original before using
the baseline expectations.

This query demonstrates iterators and table filtering, not model relationship
propagation or CALCULATE context transition. Those require the next lessons
and an actual semantic model.

**Cleanup:** close/delete your local practice file if unwanted. The query
does not persist tables or deploy cloud resources.

References: [DAX queries](https://learn.microsoft.com/en-us/dax/dax-queries)
and [DAX query view](https://learn.microsoft.com/en-us/power-bi/transform-model/dax-query-view).
