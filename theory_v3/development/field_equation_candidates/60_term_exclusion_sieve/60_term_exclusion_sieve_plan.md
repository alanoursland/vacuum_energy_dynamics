# 60_term_exclusion_sieve — Plan

## Purpose

Group 60 applies a stricter exclusion sieve to the surviving Group 59 candidate family before any covariant lift, insertion, source-safety theorem, or parent-equation work.

Group 59 left one narrow survivor:

```text
localized weighted-neutral closure-supported transition response
```

It survived reduced filters for:

```text
endpoint locality;
weighted scalar neutrality;
source/trace incidence;
reduced divergence closure.
```

But this is still only a reduced candidate surface. Group 60 should now try to kill it.

The point is not to make the candidate prettier. The point is to apply stronger kill tests so that future development does not build on a repair term, hidden source, hidden trace entry, derivative leak, arbitrary tuning, or parent-equation shortcut.

## Group Name

```text
60_term_exclusion_sieve
```

Short Windows-safe name chosen instead of the longer `60_candidate_term_exclusion_sieve`.

## Central Question

```text
Can the localized weighted-neutral closure-supported transition response survive
a stricter exclusion sieve without becoming a repair term, source carrier,
trace double-count, derivative leak, arbitrary tuning artifact, divergence failure,
or hidden insertion?
```

## Starting State

Group 60 imports Group 59 status:

```text
transition-term candidate surface opened;
R1/R2 residues inventoried as clues;
weighted-neutralizer N_w[f] derived;
localized bases survived;
constant/nonlocal terms rejected;
source-carrying and trace-double-counting terms rejected;
radial-only stress rejected;
closure-supported response survives conditionally;
physical use blocked.
```

## Desired Outcome

Best useful result:

```text
Raw residue insertion is rejected.
Repair/counterterm forms are rejected.
Nonlocal constant/background terms remain rejected.
Scalar eta is value/slope-localized but has a second-derivative endpoint burden.
Stress basis eta^2 has stronger endpoint derivative silence.
eta remains weighted-neutral as scalar response.
eta^2 is rejected as scalar-charge-neutral response, but retained only as stress-like basis.
Arbitrary constant admixture is rejected unless its coefficient is forced to zero.
Source-carrying and trace-carrying incidence routes remain rejected.
Radial-only stress remains rejected; closure-supported stress survives conditionally.
The surviving candidate is narrowed to:
  stress-only / closure-supported / weighted-neutral-generated / localized transition response.
Physical use remains blocked.
```

Possible negative result:

```text
The surviving Group 59 family fails the stricter sieve and must be rejected or returned to diagnostic-only status.
```

Either result is progress.

## What This Group May Do

Group 60 may:

```text
reject raw residue repair;
test derivative locality under first/second derivatives;
test scalar weighted charge of eta and eta^2;
test arbitrary constant admixture and coefficient tuning;
apply source/trace incidence kill tests;
apply reduced divergence and energy burden filters;
classify the narrowed survivor.
```

## What This Group Must Not Do

Group 60 must not:

```text
insert B_s/F_zeta;
insert R1/R2 as repair tensors;
promote N_w to active O;
treat eta or eta^2 as ordinary source;
treat eta^2 scalar charge as acceptable if interpreted as scalar response;
claim covariant lift;
claim source safety theorem;
claim Bianchi identity;
open recombination;
open parent closure.
```

## Recommended Script Batch

```text
candidate_sieve_problem.py
candidate_repair_sieve.py
candidate_derivative_sieve.py
candidate_neutrality_sieve.py
candidate_tuning_sieve.py
candidate_source_trace_sieve.py
candidate_div_energy_sieve.py
candidate_sieve_classifier.py
candidate_sieve_reconcile.py
order.txt
```

## Script Intent

### 1. candidate_sieve_problem.py

Open Group 60 as a stricter exclusion sieve for the Group 59 survivor.

### 2. candidate_repair_sieve.py

Reject:

```text
R1 as direct equation term;
R2 as direct equation term;
arbitrary counterterm C=-R;
```

Residues remain clues only.

### 3. candidate_derivative_sieve.py

Test endpoint derivative locality for:

```text
w=(1-y^2)^2
eta=w*(y-c*)
eta^2
```

Expected useful result:

```text
w and eta vanish with first derivative at endpoints,
but second derivatives are nonzero;
eta^2 has stronger endpoint silence through second derivative.
```

This narrows the stress-like route.

### 4. candidate_neutrality_sieve.py

Test weighted scalar charge of candidate bases:

```text
Q[eta]=0
Q[eta^2] != 0
```

Interpretation:

```text
eta can be scalar-neutral;
eta^2 cannot be used as scalar charge response;
eta^2 may survive only as stress-like basis, not scalar source.
```

### 5. candidate_tuning_sieve.py

Test whether adding bad basis terms requires arbitrary tuning:

```text
candidate = a*eta + b*constant
Q = b * Q_constant
```

Weighted neutrality forces:

```text
b=0
```

So constant admixture is not a real degree of freedom.

### 6. candidate_source_trace_sieve.py

Reapply source and trace incidence to narrowed candidate classes.

Reject:

```text
ordinary-source-carrying transition response;
extra trace-count transition response;
residual reentry.
```

### 7. candidate_div_energy_sieve.py

Reapply divergence and energy burden tests.

Reject:

```text
radial-only stress;
free-energy transition response.
```

Retain only:

```text
closure-supported stress with explicit energy/stress burden.
```

### 8. candidate_sieve_classifier.py

Classify the survivor after the stronger sieve.

Expected survivor:

```text
localized weighted-neutral-generated closure-supported transition response,
stress-only interpretation,
not scalar source,
not trace entry,
not insertable.
```

### 9. candidate_sieve_reconcile.py

Prepare result notes and summary.

## Expected Summary Shape

Likely result:

```text
Group 60 applied a stricter exclusion sieve.
Raw residues remain clues and repair insertion is rejected.
Derivative locality narrows the route: eta is not enough for strong curvature-endpoint silence, eta^2 is better as stress-like basis.
eta is weighted scalar-neutral; eta^2 is not scalar-neutral and cannot be used as scalar source.
Constant admixtures are rejected because neutrality forces their coefficients to zero.
Source/trace-carrying and radial-only divergence-failing routes remain rejected.
A narrower stress-only closure-supported transition response survives conditionally.
Physical use remains blocked.
```

## Safe Handoff Options

Depending on outputs, Group 61 could be:

```text
61_source_safety_audit
61_covariant_layer_lift
61_layer_energy_stress_accounting
61_candidate_confidence_ledger
```
