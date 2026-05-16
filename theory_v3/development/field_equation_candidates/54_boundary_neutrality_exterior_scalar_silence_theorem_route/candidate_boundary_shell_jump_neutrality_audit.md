# candidate_boundary_shell_jump_neutrality_audit — Result Note

## Result

This script derives a reduced matching-surface derivative-jump diagnostic.

It defines:

```text
phi_ext'(R) = -C1/R^2
phi_int'(R) = a_int
J = R^2*(phi_ext'(R)-phi_int'(R))
```

and obtains:

```text
J = -C1 - R^2*a_int
```

The explicit zero-charge / zero-interior-derivative case gives:

```text
C1=0 and a_int=0 -> J=0
```

## Main Findings

The shell-jump condition is now explicit. A nonzero `J` is the reduced diagnostic for a boundary shell scalar source. Exterior silence is therefore not just about the far-zone scalar tail; it also requires matching neutrality.

There is an important technical wrinkle: the script reports

```text
No-shell matching condition solved for a_int: []
```

Given the printed assumptions, this likely reflects sign/positivity restrictions on `a_int`, `C1`, and `R`. Algebraically, from:

```text
-C1 - R^2*a_int = 0
```

the unconstrained matching relation would be:

```text
a_int = -C1/R^2
```

If both `C1` and `a_int` are constrained positive, that relation is incompatible except for special zero cases. The explicit zero case `C1=0, a_int=0` remains valid and is the clean no-shell condition tested here.

This is useful: matching neutrality is sign-sensitive and cannot be hidden by a boundary term.

## Boundary

This is not a full junction theorem. It does not derive the interior behavior. It gives a reduced shell-source diagnostic and a clean zero-charge / zero-derivative no-shell case.

## Steering Consequence

The summary should preserve the no-shell burden as a real condition:

```text
J=0
```

and should avoid claiming a generic matched interior solution unless the sign assumptions are removed or the matching relation is analyzed separately.
