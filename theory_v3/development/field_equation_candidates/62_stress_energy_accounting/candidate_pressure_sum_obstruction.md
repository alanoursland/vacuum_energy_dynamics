# candidate_pressure_sum_obstruction — Result Note

## Result

The script tests whether:

```text
P = p_r + 2p_t
```

is identically zero for the closure-supported layer.

It finds a nonzero reduced expression:

```text
P =
p0*(y-1)^3*(y+1)^3*(7R^2*y - 2Rell + ell^2*y)
*
(70R^3*y^2 - 14R^3 + 91R^2ell*y^3 - 51R^2ell*y
 - 12Rell^2*y^2 + 4Rell^2 + 13ell^3*y^3 - 5ell^3*y)
/
(ell*(7R^2+ell^2)^2)
```

and interior witnesses:

```text
P(0) = -4R^2*p0*(7R^2-2ell^2)/(7R^2+ell^2)^2

P(1/2) =
-27*p0*(7R^2-4Rell+ell^2)*(28R^3-113R^2ell+8Rell^2-7ell^3)
/
(1024*ell*(7R^2+ell^2)^2)
```

## Main Findings

The pressure sum is not generically zero.

That means the simultaneous closure condition:

```text
P=0
```

is not available for the nontrivial closure-supported transition response.

So the route cannot claim both:

```text
trace-free;
active-mass-neutral.
```

without a new derived stress principle or a special/trivial relation.

The script also rejects the shortcut:

```text
set p0=0
```

because that kills the transition response rather than licensing it.

## Boundary

This is a reduced obstruction witness, not a covariant theorem.

## Steering Consequence

The next step is integrated accounting. Local nonzero `P` should be connected to the layer energy/pressure burden.
