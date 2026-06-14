# 5. Case Study: Lee et al. 2020 Yukawa Exclusion Curve

The first case study is the short-range gravity Yukawa exclusion curve in
Lee et al. 2020 [Lee et al., 2020], Figure 5. The figure reports a `95%` confidence-level
exclusion boundary in the `alpha(lambda)` plane. The relevant public PDF page
contains vector drawings and no raster images for the plotted figure.

The target object is the green newly excluded region in the bottom panel. The
region is encoded as a filled polygon. Because the previously excluded region
is painted over it, one boundary chain of the green polygon carries the limit
curve. This is the useful painter's-algorithm observation: the visual fill
object contains the numerical boundary.

The implemented extraction script identifies the green fill polygon, takes its
line-segment vertices, calibrates the log-log axes from vector tick marks, and
transforms the vertices into `(lambda_m, alpha_95cl)` coordinates. The x-axis
major ticks at PDF x positions `421.22`, `483.21`, and `545.20` correspond to
`1e-5`, `1e-4`, and `1e-3 m`. The y-axis calibration uses evenly spaced decade
ticks from `alpha = 1e6` to `alpha = 1e-3`.

The validation anchor is the text-stated result that `|alpha| = 1` is excluded
for `lambda >= 38.6 um`. The extracted curve crosses `alpha = 1` at
`lambda = 38.61 um`, a relative deviation of `0.03%`. This passes the
validation gate.

The same extracted curve gives the `alpha = 1/3` crossing as
`lambda = 54.05 um`. This number is not claimed to be author-provided raw data.
It is a read-off from the author-generated plotted path, with provenance
`VECTOR_EXTRACTED_FROM_ARXIV_PDF`.

After this extraction was written, the project also obtained a text extraction
of the Lee supplemental `chi^2` table, validated by the project owner. That
table [Lee et al., 2020] gives `|alpha| = 1` at `38.63 um` and
`alpha = 1/3` at `54.03 um`.
The agreement is a useful independent check: the path-level figure extraction
and the supplemental-table extraction differ by about `0.02 um` at the
scalaron crossing.

| quantity | value |
|---|---:|
| source figure | Lee et al. 2020, Figure 5 bottom panel |
| extraction object | green filled exclusion polygon |
| anchor | `|alpha| = 1` at `38.6 um` |
| extracted anchor crossing | `38.61 um` |
| relative anchor deviation | `0.03%` |
| scalaron crossing | `alpha = 1/3` at `54.05 um` |
| supplemental-table cross-check | `alpha = 1/3` at `54.03 um` |

Figure 3 shows the recovered curve and the two crossings used in the present
program.
