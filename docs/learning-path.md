# Choose a learning route

## New to DAX: learn to explain an answer

1. Run [getting started](getting-started.md). Predict revenue before executing.
2. Read [core concepts](core-concepts.md). Identify whether a calculation needs
   a stored row value, a reusable measure, or a query result.
3. Study [functions and patterns](functions-patterns.md). Explain the difference
   between a stored amount and an iterator's expression.
4. Complete exercises 1-4 in [practice](practice.md). Check your reasoning,
   not just whether a number matches.

**Exit criteria:** explain why North revenue differs from total revenue, why
total margin is 32.8% instead of 40%, and why a zero denominator may be blank.

## Report author: make comparisons deliberate

Continue with [time and modeling](time-and-modeling.md), then import the
[DAX for Everyone practice model](https://cloud2br-msftlearninghub.github.io/DAX-For-Everyone/model-setup.html).
Create measures in its catalog order. Build visuals using dimension fields;
compare replacement/intersection and selected/all-product denominators.

**Exit criteria:** describe which filters a denominator retains and which
date relationship a measure uses. A slicer is not an access-control policy.

## Experienced analyst: investigate before optimizing

Use the companion hub's
[performance investigation](https://cloud2br-msftlearninghub.github.io/DAX-For-Everyone/performance.html)
and [projects](https://cloud2br-msftlearninghub.github.io/DAX-For-Everyone/projects.html).
Capture engine/client versions, storage mode, model size, filters, timings,
and output correctness. The tiny Overview fixture cannot prove production speed.

## Keep an evidence log

For each exercise record:

- Question/business definition and expected output.
- Calculation object and exact model relationships.
- Query or visual filters, including hidden page filters.
- Actual engine/client version and observed output.
- Explanation of blanks, totals, and any discrepancy.

Do not substitute a passing website build for this execution evidence.
