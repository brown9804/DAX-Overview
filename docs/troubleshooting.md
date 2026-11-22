# Troubleshooting and safe adaptation

| Symptom | First investigation | Avoid |
| --- | --- | --- |
| EVALUATE rejected | Use DAX query view/DAX Studio, not New measure | Removing keywords randomly |
| Items not found | Run the complete generated DEFINE block with the query | Running the raw source body alone |
| Sales/DimDate missing | Import the companion model for model-dependent snippets | Assuming temporary Items is the retail model |
| Same value for every product | Relationship path, visual fields, context transition | Enabling bidirectional filtering as a guess |
| Total percentage differs from row average | Business definition and aggregate denominator | Summing or averaging row percentages blindly |
| North value ignores South selection | Replacement versus KEEPFILTERS | Treating deliberate replacement as a SUM error |
| PY/YTD blank or unexpected | Calendar coverage, marked table, date relationship | Inventing 2024 values absent from the fixture |
| Shipping months differ | Active OrderDate and inactive ShipDate relationship | Changing stored transaction amounts |
| Variable ignores new filters | Scalar variable evaluation context | Expecting a variable to re-run a measure |

## Types and locales

The complete query uses commas as argument separators and decimal dots.
Some authoring surfaces/locales use different separators. Confirm the client's
syntax rather than changing CSV delimiter/type assumptions blindly.

Import dates as Date and quantities/IDs as whole numbers. Use fixed decimal
amounts for the practice model. Display formatting such as currency or percentage
does not change the underlying value. The query fixture contains no currency
conversion, taxes, returns, or multiple-line order logic.

## Performance is a separate investigation

Capture a representative model, identical filters, output correctness,
engine version, repeated cold/warm timings, and server timings where available.
Do not claim a general improvement from the three-row query. Before optimizing
functions, investigate model cardinality, unused columns, relationships,
visual count, and storage mode.

## Security and deployment boundaries

RLS is distinct from report filters and workspace permissions. Check current
product restrictions and test actual service roles when adapting USERELATIONSHIP
or calculated expressions. Never publish confidential semantic models, actual
user mappings, customer data, or credentials in issues.

CI here deploys documentation only; it does not create cloud resources or
publish/secure a Power BI semantic model. See the companion
[security lesson](https://cloud2br-msftlearninghub.github.io/DAX-For-Everyone/security.html)
and [troubleshooting](https://cloud2br-msftlearninghub.github.io/DAX-For-Everyone/troubleshooting.html).
