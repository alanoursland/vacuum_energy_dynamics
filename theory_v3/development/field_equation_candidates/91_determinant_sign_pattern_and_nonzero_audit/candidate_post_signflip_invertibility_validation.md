# candidate_post_signflip_invertibility_validation — Analysis Note

## Result

`candidate_post_signflip_invertibility_validation.py` solves the hierarchy systems at `N=11` and `N=12`.

The results are:

```text
N=11:
  det_sign = -1
  residuals_zero = True

N=12:
  det_sign = +1
  residuals_zero = True
```

The script also reports representative coefficients:

```text
N=11:
  first coefficient = -12163353/1783
  last coefficient  = -2262354131583/1783

N=12:
  first coefficient = -550230732/2500481
  last coefficient  = 367758232722881/2500481
```

Governance records:

```text
post-signflip generation:
  N=11 and N=12 profile systems solve exactly

invertibility versus positivity:
  negative determinant does not block coefficient generation
```

## Interpretation

This is the hierarchy-survival result.

The determinant sign flip at `N=11` does not break profile generation. The linear systems still solve exactly, and the target residuals vanish.

This confirms the main conceptual correction:

```text
positivity is optional;
invertibility is essential.
```

The hierarchy does not care whether the determinant is positive or negative. It cares whether the determinant is zero.

## What Changed

The sign flip is now proven harmless for finite profile generation at the first post-flip orders.

That strengthens the retargeted route:

```text
nonzero determinant theorem remains alive.
```

## What Did Not Change

Large coefficients and sign changes may still matter for limit behavior, conditioning, or physical interpretation. This script only checks exact finite solvability.

## Steering Consequence

The next theorem work should not try to restore positivity. It should explain why determinant signs follow the observed pattern while staying nonzero.
