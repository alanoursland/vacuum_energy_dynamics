# candidate_suppressed_profile_validation — Analysis Note

## Result

`candidate_suppressed_profile_validation.py` validates the derived profile:

```text
P = 51y^4 - 12y^2 + 1
```

The corresponding flux and remainder are:

```text
J = -30y(y - 1)^4(y + 1)^4(17y^4 - 10y^2 + 1)

rho = -30(y - 1)^3(y + 1)^3
      (221y^6 - 195y^4 + 39y^2 - 1)
```

Endpoint flux is retained:

```text
J(-1) = 0
J(1) = 0
```

The local field is still nonzero:

```text
rho(0) = -30
```

Flat moments:

```text
M0 = M1 = M2 = M3 = M4 = M5 = 0
M6 = 65536/323323
M7 = 0
```

## Interpretation

This is the strongest positive result of Group 85.

The even quartic profile does more than merely fix the `M2` problem found in Group 84. It suppresses all flat moments through `M5`.

That is a substantial finite-mode payload suppression result. It means the local exactness profile can be shaped so that the first several low-order probes do not see it.

However, the script also proves the crucial caution:

```text
rho(0) = -30
```

so the field is not pointwise zero. The profile achieves moment invisibility through structured oscillation/cancellation, not local disappearance.

The next obstruction appears at:

```text
M6 = 65536/323323
```

So the result is finite-order suppression, not all-order inertness.

## What Changed

The status of the exactness route improves again:

```text
the current family can suppress low-order local payload moments much better than linear skew.
```

Group 84 said the local goblin still bites low-order probes. Group 85 finds a profile that hides it from probes through fifth order.

## What Did Not Change

The local goblin is still there.

The result does not imply:

```text
rho(y)=0;
all moments vanish;
full inertness;
physical payload absence.
```

It says:

```text
low-order flat payload moments through M5 vanish.
```

## Steering Consequence

This result should push the next work toward either:

```text
shape-origin derivation;
moment hierarchy closure;
or covariant interpretation of finite-mode suppression.
```

It should not be treated as full local inertness.
