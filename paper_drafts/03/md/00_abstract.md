# Abstract

Published physics plots often contain more numerical information than their
captions, tables, or supplementary files expose. When a figure is embedded in a
PDF as vector graphics, the plotted curves are stored as drawing paths rather
than pixels. We describe a reproducible method for recovering numerical data
from such figures: extract PDF drawing paths, identify the path carrying the
curve or boundary of interest, calibrate the plot frame from vector tick
geometry, transform path coordinates into data coordinates, and validate the
result against an independently stated anchor value before releasing data for
scientific use. In a case study on the Lee et al. 2020 short-range gravity
[Lee et al., 2020]
Yukawa exclusion figure, the method recovers the published `|alpha| = 1`
crossing at `lambda = 38.6 um` to within `0.03%` and reads the `alpha = 1/3`
crossing as `lambda = 54.05 um` from the same author-generated path. A later
supplemental-table extraction gives `54.03 um`, providing an independent
cross-check of the path-level result. We compare
path-level extraction with pixel digitization, describe failure modes, and
propose a validation-or-refuse norm for provenance-graded reuse of data
extracted from published vector figures.
