# 6. Additional Case Studies

The final paper should include additional examples before submission. The
purpose is not to maximize the number of extracted plots, but to show that the
method is not a single-figure trick and to document where it fails.

Case studies should be selected to cover different plotting toolchains and
figure structures:

- a line plot encoded as stroked paths;
- a filled exclusion or confidence region encoded as a polygon;
- a multi-curve plot where path selection is nontrivial;
- at least one refusal case where validation fails or the path identity is
  ambiguous.

Candidate domains include short-range gravity limit curves, high-energy
physics exclusion contours, and condensed-matter or materials plots generated
by Origin-style workflows. A useful case study set should include one example
from a ROOT-generated figure if possible, because ROOT output has different PDF
path conventions from matplotlib.

For each case, the paper should report:

- source paper and figure;
- whether the page is vector-rich or raster-only;
- path-selection rule;
- axis-calibration rule;
- external anchor;
- validation result;
- extracted data product or refusal reason.

The refusal cases are important. A tool that always emits a CSV invites false
precision. A tool that sometimes refuses demonstrates that validation is part
of the method rather than a decorative check.
