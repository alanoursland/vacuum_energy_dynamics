# candidate_group_87_status_summary — Analysis Note

## Result

`candidate_group_87_status_summary.py` closes Group 87 with this stable result:

```text
general even compact-support operator tested;
odd moments vanish by parity;
finite moment hierarchy supported for N=1..4;
unique normalized even profile per order through N=4;
quadratic-measure weighted block inheritance derived;
next even moment M(2N+2) remains nonzero in tested cases;
local rho remains nonzero;
all-order closure not proven;
physical/covariant origin remains open;
parent divergence identity remains unproven;
recombination remains blocked.
```

## Interpretation

Group 87 makes real progress.

It shows that the Group 86 quartic profile is not a one-off. It is part of a finite moment-suppression hierarchy, at least through `N=4`.

The hierarchy has a clean structure:

```text
even profile -> odd moments vanish by parity;
degree 2N profile -> unique suppression of M2..M(2N);
quadratic measure -> W0..W(2N-1) inherited from flat block;
next moment M(2N+2) remains nonzero.
```

That is a real technical pattern.

## What Changed

The route status should update from:

```text
quartic profile structurally derived
```

to:

```text
finite hierarchy supported through N=4
```

This is a meaningful strengthening of the reduced exactness/payload-suppression program.

## What Did Not Change

The hierarchy is not full local inertness.

The group explicitly leaves open:

```text
all-order closure;
general coefficient recurrence;
all-order limit behavior;
covariant/physical origin;
parent divergence;
recombination.
```

## Steering Consequence

The best next group is:

```text
88_hierarchy_formula_derivation
```

because the current result is pattern evidence. The next real progress would be deriving the rule behind the pattern.
