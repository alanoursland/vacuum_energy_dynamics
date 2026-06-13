# Appendix B. Log-Axis Calibration

Suppose a log-axis has two identified major ticks:

```text
(u_1, X_1), (u_2, X_2)
```

where `u` is the PDF coordinate and `X` is the data value. For a base-10 log
axis,

```text
log10(X) = a u + b .
```

The calibration constants are:

```text
a = (log10(X_2) - log10(X_1)) / (u_2 - u_1)
b = log10(X_1) - a u_1 .
```

For an inverted visual axis, the sign of `a` is negative. The recovered data
coordinate is:

```text
X = 10^(a u + b) .
```

Minor ticks provide an internal residual check. If `u_1` and `u_2` are adjacent
decade ticks, the expected PDF coordinate of the minor tick `k X_1`, with
`k = 2, ..., 9`, is:

```text
u_k = u_1 + (log10(k) / (log10(X_2) - log10(X_1))) (u_2 - u_1) .
```

The residuals between observed and predicted minor-tick positions measure the
quality of the geometric calibration independent of the curve extraction.
