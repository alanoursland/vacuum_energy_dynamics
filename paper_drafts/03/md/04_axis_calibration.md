# 4. Axis Calibration

PDF drawing coordinates are page coordinates. To recover data coordinates, one
must infer the transform used by the plotting software. The simplest case is a
linear axis:

```text
x_data = a_x x_pdf + b_x
y_data = a_y y_pdf + b_y
```

The constants can be obtained from two known tick positions on each axis. PDF
coordinates often increase downward in the displayed page coordinate system, so
the sign of `a_y` must be inferred rather than assumed.

For logarithmic axes, the affine map applies to the logarithm:

```text
log10(x_data) = a_x x_pdf + b_x
log10(y_data) = a_y y_pdf + b_y
```

Equivalently,

```text
x_data = 10^(a_x x_pdf + b_x)
y_data = 10^(a_y y_pdf + b_y)
```

Major tick marks determine the decade spacing. Minor ticks at `2, 3, ..., 9`
within a decade provide an internal consistency check because their PDF
positions should match `log10(k)` spacing. This makes log-axis calibration
possible even before optical character recognition of tick labels, provided
the decade identity is known from the figure labels or context.

Let `Delta x_pdf` be the uncertainty in the PDF coordinate of a point on a log
axis. The propagated fractional data uncertainty is approximately

```text
Delta x_data / x_data = ln(10) |a_x| Delta x_pdf .
```

This estimate separates coordinate precision from semantic uncertainty.
Coordinate precision may be very high for vector paths, but the extracted path
still might not represent the intended scientific boundary. That semantic
question is handled by path selection and anchor validation.
