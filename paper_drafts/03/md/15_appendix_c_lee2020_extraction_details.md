# Appendix C. Lee 2020 Extraction Details

The current implementation is
`src_exp/dataexp/tools/extract_lee2020_fig5.py`.

Source:

```text
arXiv:2002.11761
Lee et al., PRL 124, 101101 (2020)
Figure 5 bottom panel, PDF page 4
```

The script loads the PDF with PyMuPDF and inspects drawing paths on page index
`3`. The target object is a green filled polygon with fill color
`(0.0, 1.0, 0.0)`. Its line-segment vertices are transformed from PDF
coordinates to `(lambda_m, alpha_95cl)` using hard-coded tick geometry derived
from the figure.

Calibration constants:

```text
x decade ticks: 421.22, 483.21, 545.20
x tick values:  1e-5, 1e-4, 1e-3 m
y top:          434.72 -> alpha = 1e6
y bottom:       585.48 -> alpha = 1e-3
```

Validation:

```text
anchor:                |alpha| = 1 excluded for lambda >= 38.6 um
extracted crossing:    38.61 um
relative deviation:    0.03%
tolerance:             2%
result:                PASS
```

Derived readout:

```text
alpha = 1/3 crossing:  54.05 um
```

The output CSV path is:

```text
src_exp/dataexp/.data/alpha_lambda/lee2020_alpha_lambda_95cl.csv
```

The CSV should be accompanied by the extraction script and these notes. The
CSV alone is not sufficient provenance.
