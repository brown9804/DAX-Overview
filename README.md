# DAX Overview

Atlanta, USA

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/Cloud2BR-MSFTLearningHub)
[Cloud2BR OSS - Learning Hub](https://github.com/Cloud2BR-MSFTLearningHub)
[![Validation](https://github.com/brown9804/DAX-Overview/actions/workflows/validate-and-deploy.yml/badge.svg)](https://github.com/brown9804/DAX-Overview/actions/workflows/validate-and-deploy.yml)
[![License: GPL-3.0](https://img.shields.io/badge/license-GPL--3.0-12365b)](https://github.com/brown9804/DAX-Overview/blob/main/LICENSE)

A beginner-friendly introduction to **Data Analysis Expressions (DAX)** for
Power BI, Power Pivot, and Analysis Services. Learn how calculations depend
on the model and context, not just the function you choose.

**[Open the learning website](https://brown9804.github.io/DAX-Overview/)**

## Two complementary resources

| Resource | Use it for |
| --- | --- |
| **DAX Overview** | Understand the language, reason about results, and complete a compact first analysis |
| **[DAX for Everyone](https://github.com/Cloud2BR-MSFTLearningHub/DAX-For-Everyone)** | Import the full practice model, explore 18 reusable measures/eight queries, and build report projects |

Start here for the conceptual overview, then continue to the
[DAX for Everyone website](https://cloud2br-msftlearninghub.github.io/DAX-For-Everyone/).
The larger hub is referenced rather than duplicated.

## Learning route

1. [Choose your route](https://brown9804.github.io/DAX-Overview/learning-path.html).
2. [Run the first analysis](https://brown9804.github.io/DAX-Overview/getting-started.html).
3. [Understand calculation objects and context](https://brown9804.github.io/DAX-Overview/core-concepts.html).
4. [Explore essential functions and patterns](https://brown9804.github.io/DAX-Overview/functions-patterns.html).
5. [Connect time intelligence to model design](https://brown9804.github.io/DAX-Overview/time-and-modeling.html).
6. [Practice and explain your answers](https://brown9804.github.io/DAX-Overview/practice.html).

## Included resources

- Original lessons, worked examples, a cheat sheet, and troubleshooting.
- A synthetic three-line dataset with independent expected results.
- A downloadable standalone query with three result sets; no retail model import required.
- Explicit links to the companion hub's model, measure library, security, and projects.
- A responsive, searchable MkDocs Material website with navy styling and light/dark themes.
- Automated data/package/documentation validation and GitHub Pages publication.

| Folder | Contents |
| --- | --- |
| [examples](https://github.com/brown9804/DAX-Overview/tree/main/examples) | Synthetic CSV, canonical query body, expected results, and usage instructions |
| [docs](https://github.com/brown9804/DAX-Overview/tree/main/docs) | Overview lessons and companion-hub references |
| [scripts](https://github.com/brown9804/DAX-Overview/tree/main/scripts) | Independent arithmetic checks, synchronized downloads, and site-link checks |
| [.github](https://github.com/brown9804/DAX-Overview/tree/main/.github) | Validation/deployment workflow and community templates |

> **Validation boundary:** CI checks synthetic data, independent arithmetic,
> download synchronization, and the strict website build. It does **not**
> execute DAX in Power BI or Analysis Services. Record actual engine results
> when following the query exercises; Python passing is not DAX execution evidence.

Read [CONTRIBUTING.md](https://github.com/brown9804/DAX-Overview/blob/main/CONTRIBUTING.md)
and the [code of conduct](https://github.com/brown9804/DAX-Overview/blob/main/CODE_OF_CONDUCT.md).
The original GPL-3.0 license is preserved. No paid resources or Power BI
semantic models are deployed by CI. This is community learning material,
not official Microsoft training.
