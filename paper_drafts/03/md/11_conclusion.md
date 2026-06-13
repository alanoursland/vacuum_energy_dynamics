# 11. Conclusion

Many published physics figures contain numerical structure in two forms: the
visible image seen by readers and the vector drawing paths stored inside the
PDF. When the relevant path can be identified, calibrated from tick geometry,
and validated against an external anchor, the PDF itself can provide a
reproducible route to plotted data.

The Lee et al. 2020 case study demonstrates the workflow. A vector path from
the filled exclusion region reproduces the text-stated `|alpha| = 1` crossing
at `38.6 um` to `0.03%` and yields the `alpha = 1/3` crossing at `54.05 um`.
The result is not a replacement for official data release, but it is a
provenance-graded, anchor-validated extraction from the published figure.

The broader lesson is methodological. Data extraction from figures should move
from manual clicks toward auditable scripts, explicit coordinate transforms,
and refusal criteria. The best outcome remains routine publication of
machine-readable data. Until that norm is universal, vector-path extraction can
make unavoidable figure reuse more accurate and more reproducible.
