# 4. Plus/cross polarization basis gate

The two standard TT basis tensors for propagation in the `z` direction are

```text
e_+ = diag(1,-1,0)
e_x = [[0,1,0],[1,0,0],[0,0,0]].
```

Validated checks:

```text
tr(e_+) = tr(e_x) = 0
<e_+, e_x> = 0
<e_+, e_+> = <e_x, e_x> = 2
```

Result: the free radiative tensor sector contains two independent TT polarizations, not one scalar mode.
