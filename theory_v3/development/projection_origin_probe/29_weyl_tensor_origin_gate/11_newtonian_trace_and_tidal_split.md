# 11. Newtonian trace and tidal split

A Hessian-like matrix can be split as

```text
H = (rho/3) I + Tidal_TF.
```

For the witness matrix, the trace is

```text
tr(H) = rho.
```

and the trace-free tidal part is

```text
Matrix([
[a,  0, 0],
[0, -a, 0],
[0,  0, 0]]).
```

The source/Poisson trace and free tidal data are distinct channels.
