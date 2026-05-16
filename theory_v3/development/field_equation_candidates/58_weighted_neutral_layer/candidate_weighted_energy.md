# candidate_weighted_energy — Result Note

## Result

The script computes the reduced gradient-energy scaling for the weighted-neutral profile.

It finds:

```text
Integral (drho/dy)^2 dy =
256*rho0^2*(49*R^4 + 26*R^2*ell^2 + ell^4)
/
(315*(7*R^2 + ell^2)^2)
```

and therefore:

```text
E_r =
256*rho0^2*(49*R^4 + 26*R^2*ell^2 + ell^4)
/
(315*ell*(7*R^2 + ell^2)^2)
```

The thin-layer scaling coefficient is:

```text
lim_{ell -> 0} ell*E/rho0^2 = 256/315
```

## Main Findings

The weighted-neutral profile has finite explicit reduced gradient energy for finite `ell`.

This is important because Group 58 did not create a free neutral layer. Neutrality still has a cost. The profile is reduced-charge neutral, but it has gradient structure and therefore reduced layer energy.

The hard-shell warning remains:

```text
E_r ~ 1/ell
```

as `ell -> 0`.

So the weighted-neutral route supports the finite-layer picture. The layer should not be collapsed into a zero-thickness shell without paying a growing energy cost.

## Boundary

This is reduced gradient energy, not a covariant stress tensor or mass theorem.

## Steering Consequence

The next check should connect `Q_weighted=0` to the reduced exterior tail and mass-shift diagnostics. Energy finiteness is not the same as mass neutrality.
