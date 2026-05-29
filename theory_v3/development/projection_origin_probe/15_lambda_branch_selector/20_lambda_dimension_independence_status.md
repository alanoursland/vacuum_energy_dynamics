# 20. Lambda Dimension Independence Status

The dimension selector and Lambda selector interact but are not identical.
The TT count depends on `D`, while the constant-curvature scale depends on
`Lambda` once `D` is fixed:

```text
N_TT = D(D-3)/2,
H^2 = 2 Lambda / ((D-1)(D-2)).
```

The script checks these dependencies exactly.
