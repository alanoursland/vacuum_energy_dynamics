# candidate_quadratic_scalar_origin — Result Note

## Result

The script tests whether `eta` can arise from a simple constant-coefficient quadratic scalar functional with Euler-Lagrange form:

```text
f'' = k f
```

The necessary test is whether:

```text
f''/f
```

is constant.

It finds:

```text
(f''/f)(0) = -4
```

and:

```text
(f''/f)(1/2) =
-16*(49R^2 - 4Rell + 7ell^2)
/
(9*(7R^2 - 4Rell + ell^2))
```

with nonzero difference:

```text
4*(133R^2 + 20Rell + 19ell^2)
/
(9*(7R^2 - 4Rell + ell^2))
```

## Main Findings

The simple constant-coefficient scalar origin fails.

`eta` does not satisfy a global constant-`k` equation of the form:

```text
f'' = k f
```

This rejects a plausible easy variational origin. It also blocks the shortcut of choosing `k` locally at one point.

This is negative progress, not total no-go. The script correctly does **not** reject all possible variational origins. Variable-coefficient, nonlinear, higher-derivative, constrained, or tensor origins are still not ruled out.

## Boundary

This is only a reduced constant-coefficient scalar test. It is not a proof that all variational origins are impossible.

## Steering Consequence

Proceed to stress closure. If the profile is not derived by the simplest scalar origin, the next possible origin route is a stress-energy closure relation.
