# candidate_layer_charge_mass — Result Note

## Result

The script computes reduced layer charge and mass-shift diagnostics for an odd layer charge density:

```text
rho_layer(y)=rho1*y
```

The unweighted charge cancels:

```text
flat charge integral = 0
```

but the spherical weighted charge does not:

```text
Q_weighted = 4*R*ell^2*rho1/3
```

The mass-shift diagnostic is:

```text
Delta_M_layer = 4*R*alpha*ell^2*rho1/3
```

and it vanishes only under the tested solve:

```text
rho1=0
```

## Main Findings

This is the most important warning in Group 57.

A layer profile that is odd and charge-neutral in a flat/unweighted sense is not necessarily neutral in the spherical problem. The `r^2` weighting spoils the naive cancellation.

That means the finite layer cannot hide scalar charge by symmetry alone. It needs a weighted neutrality theorem or a deliberately weighted-neutral profile.

This is real restriction progress. It kills a tempting shortcut:

```text
odd layer profile -> zero layer charge
```

No. The correct condition is:

```text
integral r^2*rho_layer dr = 0
```

## Boundary

The script does not prove neutrality. It shows that neutrality is more demanding than flat odd cancellation.

## Steering Consequence

Future work should probably construct a weighted-neutral finite-layer profile. This is a natural next-group target, because the layer route survives only if weighted charge and mass shift can be controlled.
