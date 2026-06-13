# 8. Workflow Component 5: Data Provenance Grades

Empirical confrontations require data provenance. A number remembered from a
paper, copied from a plot, extracted from a vector path, or received from an
author should not have the same status.

A practical grading vocabulary is:

| grade | meaning |
|---|---|
| `FROM_MEMORY` | forbidden for empirical confrontation |
| `TEXT_STATED` | stated explicitly in the source text |
| `VERIFIED_FROM_ABSTRACT` | independently checked against an abstract or summary claim |
| `VECTOR_EXTRACTED` | recovered from a vector figure with calibration and validation |
| `AUTHOR_PROVIDED` | obtained from original authors or official supplement |

For extracted plots, the workflow requires anchor validation. A curve extracted
from a PDF should reproduce an external text-stated number before derived
read-offs are trusted.

Paper 3 develops this data-gate component in detail. In the present case
study, the Lee 2020 short-range gravity curve was extracted from vector PDF
paths and validated against the text-stated `|alpha| = 1` crossing at
`38.6 um`. The extracted crossing was `38.61 um`; the `alpha = 1/3` read-off
was `54.05 um`.

The methodology point is broader than that one curve. AI-assisted theory work
should not let a model cite vague numbers. Every empirical number used to kill
or support a candidate needs a provenance grade.
