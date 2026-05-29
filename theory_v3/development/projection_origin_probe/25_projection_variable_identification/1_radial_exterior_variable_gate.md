# Radial Exterior Variable Gate

The weak-field scalar exterior is represented by a finite-flux monopole potential.  The physical exterior datum is the falloff class `Phi ~ A/r`, not a unique compactified projection variable.

## SymPy check

Set `q=1/r`.  Then `Phi=A/r` becomes `Phi=A*q`.  The compactified boundary at infinity is `q=0`; the exterior solution has first-order contact in `q`.

```text
Phi(r)=A/r -> Phi(q)=A q
```

This closes only the physical exterior falloff, not the projection chart.
