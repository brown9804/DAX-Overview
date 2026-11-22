# Practice: predict, execute, explain

Use a local practice environment, not a production model. Attempt each
question before opening its answer. First-query exercises use Overview data;
model exercises explicitly use DAX for Everyone.

## 1. Change the grain-level input

In the Overview query, change Keyboard quantity to 4. What happens to Revenue,
Cost, Profit, Units, and North Revenue?

<details markdown="1">
<summary>Answer and reasoning</summary>

Revenue 1300, Cost 870, Profit 430, Units 10, North Revenue 1200.
One extra Keyboard adds 50 revenue and 30 cost to the North subset.
The number of transaction lines stays 3. Increasing quantity does not add
a new transaction line or establish a different order count.

</details>

## 2. Explain a total ratio

Why is Overview total margin 32.8%, while the simple average of row margins
is 40%? Which result belongs in an aggregate gross-margin measure?

<details markdown="1">
<summary>Answer and reasoning</summary>

Aggregate margin divides total profit 410 by total revenue 1250: 32.8%.
AVERAGEX of row percentages gives each transaction line equal weight:
(30% + 50% + 40%)/3 = 40%. The Laptop's 1000 revenue dominates the aggregate,
so the definitions answer different questions. Aggregate gross margin
requires a ratio of sums, not the unweighted row average.

</details>

## 3. Distinguish blank from zero

In the first query, how do `DIVIDE(10,0)` and `DIVIDE(10,0,0)` differ?
Why might replacing every blank with zero mislead a report reader?

<details markdown="1">
<summary>Answer and reasoning</summary>

Default DIVIDE returns BLANK; the explicit alternate returns numeric 0.
An undefined denominator is not an observed zero-valued ratio. Replacing it
can make missing comparisons look like measured performance. Decide and
document the business meaning instead of changing it to hide errors.

</details>

## 4. A variable that does not recalculate

In the companion model under Laptop/North selection, evaluate:

```dax
Unexpected Denominator =
VAR CurrentRevenue = [Revenue]
RETURN
    CALCULATE ( CurrentRevenue, REMOVEFILTERS ( DimProduct ) )
```

Does it return 3000 or the all-product North revenue 4100?

<details markdown="1">
<summary>Answer and reasoning</summary>

3000. CurrentRevenue is evaluated before CALCULATE changes product filters.
Its stored scalar value is not a delayed measure expression. Put `[Revenue]`
inside CALCULATE to recalculate under the all-product context, yielding 4100.
The retained North region filter explains why the denominator is not 9500.

</details>

## 5. Replacement versus intersection

With South selected in the companion model, predict base Revenue, North
Revenue, and North Within Selection. Then run its
[filter-intersection query](https://cloud2br-msftlearninghub.github.io/DAX-For-Everyone/downloads/queries/06-filter-intersection.dax).

<details markdown="1">
<summary>Answer and reasoning</summary>

Base Revenue is 5400. North Revenue replaces the Region-column filter and
returns 4100. North Within Selection uses KEEPFILTERS, so South intersect North
has no rows and returns BLANK. Region filtering is not equivalent to removing
all model filters, and these are companion-model values.

</details>

## 6. Dates determine the question

In the companion model, why can February order revenue be 3700 while February
shipping revenue is 3300, without either measure being incorrect?

<details markdown="1">
<summary>Answer and reasoning</summary>

They group the same transaction amounts by different dates. Two February
transactions totaling 400 ship in March. The shipment measure activates the
existing ShipDate relationship. Removing date filters reconciles the totals;
monthly results need not match. Check relationships before changing arithmetic.

</details>

## 7. A security misconception

Someone filters a report to North and says South data is protected.
What needs to be tested instead?

<details markdown="1">
<summary>Answer and reasoning</summary>

A report filter is not an access-control boundary. Define appropriate RLS
and service permissions, then test allowed and disallowed identities under
their actual workspace/semantic-model permissions. Higher-privilege roles can
behave differently. Desktop "View as" is useful but does not prove service
permission enforcement. Use only synthetic mappings during this exercise.

</details>

## Continue with a complete project

Build the companion hub's
[Revenue and margin report](https://cloud2br-msftlearninghub.github.io/DAX-For-Everyone/projects.html).
Include Region/Product slicers, revenue/profit cards, and a margin visual.
Record the exact context of each result and explain non-additive totals.
Use its data rather than mixing Overview values with the larger fixture.
