# 5. Exterior Scalaron Solution

Outside matter, the trace equation is homogeneous:

```text
(1 - ell^2 Lap) R = 0,
ell = sqrt(6a).
```

For a static spherical exterior, the asymptotically regular solution is

```text
R_ext(r) = C exp(-r/ell) / r .
```

The coefficient `C` is set by matching to the interior solution. A hairless
exterior is the special case `C = 0`.

The metric potentials inherit the same Yukawa scale:

```text
phi(r) = -(GM/r) [1 + (1/3) exp(-r/ell)],
psi(r) = -(GM/r) [1 - (1/3) exp(-r/ell)]
```

for the point-source weak-field solution. Extended sources change the
amplitude through matching and form factors, but not the central fact: a
nonzero exterior scalar curvature profile is a Yukawa tail and violates
`AB = 1`.

The remaining question is whether a sourced static body can choose `C = 0`.
The next section gives the matching obstruction.
