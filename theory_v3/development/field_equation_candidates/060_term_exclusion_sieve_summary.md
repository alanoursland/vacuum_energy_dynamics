# 60_term_exclusion_sieve_summary.md

## Result

Group 60 applied a stricter exclusion sieve to the Group 59 transition-response survivor.

The result is a sharpened candidate, not insertion:

```text
raw residue repair rejected;
arbitrary counterterm repair rejected;
eta derivative burden found;
eta^2 stronger endpoint silence found;
eta^2 rejected as scalar response;
constant admixture rejected;
source repair/carrying rejected;
trace double-counting rejected;
radial-only stress rejected;
closure-supported stress survives conditionally;
energy/stress burden preserved;
physical use remains blocked.
```

The retained trace-normalization candidate remains:

```text
audit-only;
not adopted;
not branch-selected;
not insertable;
not parent-facing.
```

## What Changed

Group 59 left a surviving reduced candidate family:

```text
localized weighted-neutral closure-supported transition response
```

Group 60 tried to kill that survivor with stricter filters.

It did not kill the route completely, but it narrowed it to:

```text
stress-only localized weighted-neutral-generated closure-supported transition response
```

That narrower wording matters.

The candidate is no longer allowed to behave like a scalar source, raw residue, counterterm, constant admixture, radial-only stress, source replacement, trace entry, or active `O`.

## Repair and Counterterm Rejection

Group 60 rejected raw residue insertion:

```text
R1 as direct field-equation term
R2 as direct field-equation term
```

It also rejected arbitrary repair:

```text
H + aR1 + bR2
```

because the formal repair route works only by choosing coefficients to cancel the defect.

The correct status is:

```text
R1/R2 remain clues;
R1/R2 are not inserted terms.
```

## Derivative Locality

Group 60 tested endpoint derivatives through second order.

For:

```text
w=(1-y^2)^2
eta=w*(y-c*)
eta^2
```

the result was:

```text
w:
  value and first derivative vanish at endpoints;
  second derivative does not vanish.

eta:
  value and first derivative vanish at endpoints;
  second derivative does not vanish.

eta^2:
  value, first derivative, and second derivative vanish at endpoints.
```

This narrows the route.

`eta` has a scalar/curvature endpoint burden. `eta^2` has stronger endpoint silence and is more suitable as a stress-like basis.

This is reduced endpoint behavior, not covariant compact support.

## Weighted Scalar-Charge Sieve

Group 60 found:

```text
Q[eta]=0
```

but:

```text
Q[eta^2] != 0
Q[constant] != 0
```

Therefore:

```text
eta survives as weighted-neutral scalar basis;
eta^2 is rejected as scalar response;
constant is rejected as scalar response.
```

This is the key goblin trap exposed by Group 60:

```text
eta^2 looks better under derivatives,
but it is not scalar-neutral.
```

So `eta^2` may survive only as:

```text
stress-like basis;
closure-supported;
not scalar source;
not scalar charge profile.
```

## Tuning Rejection

Group 60 tested:

```text
candidate=a*eta+b
```

It found:

```text
Q = 2*b*(3R^2+ell^2)/3
endpoint left = b
endpoint right = b
```

So:

```text
weighted neutrality forces b=0;
endpoint locality forces b=0.
```

Therefore the constant admixture is not a real surviving degree of freedom.

A bad basis cannot be kept by saying its coefficient can be set to zero. If the coefficient must be zero, the basis is rejected.

The amplitude `a` remains deferred and needs a physical origin before use.

## Source and Trace Sieve

Group 60 reapplied the incidence filters.

Source residual:

```text
S_M*(i_A+i_trans_src-1)
```

Safe source condition:

```text
i_A=1
i_trans_src=0
```

Rejected source routes:

```text
transition carries ordinary source load;
transition repairs or replaces A-sector source.
```

Trace residual:

```text
T_zeta*(i_Bs+i_res+i_trans_trace-1)
```

Safe trace condition:

```text
i_Bs=1
i_trans_trace=0
i_res=0
```

Rejected trace routes:

```text
transition carries trace;
residual reentry occurs with B_s.
```

The source-repair route is rejected by role-purity even where the incidence residual can vanish algebraically.

## Divergence and Energy

Group 60 tested:

```text
p_r=p0*eta^2
```

The radial-only route:

```text
p_t=0
```

is rejected because reduced divergence fails.

The closure route:

```text
p_t=p_r+r*p_r'/2
```

survives with:

```text
D=0
```

The layer stress/energy burden is:

```text
E_layer =
256*ell*p0*(49R^4+58R^2ell^2+ell^4)
/
(3465*(7R^2+ell^2)^2)
```

and:

```text
E_layer/ell -> 256*p0/3465
```

So the candidate is nonfree. It requires energy/stress accounting.

This is not a covariant Bianchi proof.

## Narrow Survivor

The only survivor is:

```text
stress-only localized weighted-neutral-generated closure-supported transition response
```

It survives only as audit material.

It is not:

```text
a scalar source;
a scalar charge profile;
a raw residue;
a counterterm;
a constant admixture;
a source repair;
a trace entry;
a radial-only stress;
active O;
an inserted field-equation term.
```

## Rejected Families

Group 60 rejects:

```text
raw residue repair;
arbitrary counterterm repair;
eta as unrestricted scalar insertion;
eta^2 as scalar response;
constant admixture;
source repair;
source carrying;
trace double-counting;
radial-only stress;
active O by disguise;
reduced D=0 as Bianchi proof.
```

These rejections are important. They make the surviving candidate much harder to fake.

## Conceptual Meaning

Group 60 made real progress by narrowing the transition-response route.

The surviving object is now specific enough to test seriously:

```text
stress-only;
localized;
weighted-neutral-generated;
closure-supported;
nonfree;
audit-only.
```

This increases confidence in the route by removing several tempting bad interpretations.

But it also exposes the next hard work:

```text
source safety;
covariant lift;
covariant divergence identity;
energy/stress accounting.
```

## Boundary

Group 60 does not adopt Package B. It does not choose a trace-normalization branch. It does not collapse the paired trace candidate. It does not insert `B_s/F_zeta`. It does not prove source safety. It does not prove a covariant theorem. It does not prove a Bianchi identity. It does not construct active `O`. It does not open recombination or parent closure.

## Safe Handoff

The safe next moves are:

```text
source safety audit:
  test whether the narrowed stress-only transition response duplicates ordinary source load;

covariant layer lift:
  lift derivative locality, weighted neutralizer, and closure to geometric layer objects;

energy/stress accounting:
  derive or reject the energy/stress role of the narrowed survivor.
```

Immediate insertion, residue insertion, active `O` construction, recombination, and parent closure remain forbidden.
