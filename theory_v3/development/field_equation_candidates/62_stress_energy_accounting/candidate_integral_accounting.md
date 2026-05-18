# candidate_integral_accounting — Result Note

## Result

The script computes reduced integrated accounting for the stress-only transition response.

It obtains:

```text
E_pr =
256*ell*p0*(49R^4 + 58R^2*ell^2 + ell^4)
/
(3465*(7R^2 + ell^2)^2)
```

and:

```text
I_P =
512*ell*p0*(49R^4 + 58R^2*ell^2 + ell^4)
/
(3465*(7R^2 + ell^2)^2)
```

with:

```text
I_P / E_pr = 2
```

It also finds the integrated burden left by the two simple closure choices:

```text
u=P:
  integrated active diagnostic = 2*I_P

u=-P:
  integrated trace diagnostic = 2*I_P
```

## Main Findings

This is a strong accounting result.

The pressure-sum burden is not separate from the layer stress energy. It is tied directly to it:

```text
I_P = 2*E_pr
```

Therefore the nonzero pressure sum is not just a local algebraic nuisance. It integrates to a nonzero layer burden.

The two one-sided closures each fail the other diagnostic:

```text
trace-free u=P:
  active-mass burden remains

active-mass-neutral u=-P:
  trace burden remains
```

## Boundary

This is reduced integrated accounting. It does not provide a covariant stress theorem.

## Steering Consequence

The next check should test simple closure choices and sign/positivity burden. The accounting is explicit, but admissibility is still not derived.
