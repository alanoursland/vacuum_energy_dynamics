# 59_transition_term_audit — Plan

## Purpose

Group 59 begins the candidate transition-term audit.

Groups 57 and 58 made the finite boundary layer mathematically useful:

```text
Group 57:
  finite transition layer modeled;
  smoothstep endpoint behavior verified;
  blend residues made explicit;
  layer energy is finite but nonfree;
  reduced divergence closure exists;
  weighted neutrality required.

Group 58:
  nontrivial weighted-neutral layer profile constructed;
  flat odd cancellation rejected;
  geometry-aware skew derived;
  Q-driven tail/mass diagnostics controlled;
  weighted shape supports reduced D=0 closure.
```

Group 59 should now ask whether the finite-layer residues and weighted-neutral layer shape can generate candidate transition-response terms.

This is **not** an insertion group. It is an audit/classification group. It may generate candidate term surfaces, but it must not insert them into the field equation.

## Group Name

```text
59_transition_term_audit
```

Short enough for Windows/archive paths.

## Central Question

```text
Can Group 57 blend residues and Group 58 weighted-neutral layer shape be organized into admissible candidate transition-response terms without becoming hidden source, charge, mass, divergence failure, or repair insertion?
```

## Starting State

Group 59 imports Group 58 status:

```text
weighted-neutral finite-layer route survives conditionally;
weighted-neutral profile exists;
flat neutrality rejected;
layer energy finite for finite ell;
Q-driven tail/mass diagnostics controlled;
reduced D=0 closure exists;
source safety, candidate transition-term audit, covariant lift, and physical-use block remain.
```

## Desired Outcome

Best useful result:

```text
A candidate transition-term surface opens.
Raw blend residues are classified as clues, not inserted terms.
A weighted-neutralization operator for layer profiles is derived:
  N_w[f] = w(y)*(f(y)-mu_w[f])
  mu_w[f] = integral r^2 w f dy / integral r^2 w dy
and for f=y it reproduces the Group 58 skew:
  mu_w[y] = 2Rell/(7R^2+ell^2).
Layer-locality filters reject nonlocalized terms.
Weighted-neutrality filters reject scalar-charge-carrying raw terms.
Source/trace filters reject ordinary-source-carrying or trace-double-counting terms.
Reduced divergence filters retain only closure-supported stress routes.
One narrow candidate class survives conditionally:
  localized weighted-neutral transition response + closure-supported stress interpretation.
```

Negative result:

```text
All transition term families either carry charge/source/mass, fail locality, fail divergence,
or act as repair terms. The finite-layer route remains only a diagnostic, not a candidate-equation ingredient.
```

Either result is progress.

## What This Group May Do

Group 59 may:

```text
inventory candidate term families from R1/R2 residues and weighted-neutral shapes;
construct a weighted-neutralization operator for layer profiles;
test endpoint locality;
test weighted scalar charge;
test source and trace incidence;
test reduced divergence closure;
classify candidate term families as rejected, conditional, or audit-only.
```

## What This Group Must Not Do

Group 59 must not:

```text
insert B_s/F_zeta;
insert blend residues as repair tensors;
treat weighted neutrality as source safety;
treat reduced D=0 as covariant Bianchi proof;
claim a parent equation;
construct active O;
open recombination;
open parent closure.
```

## Recommended Script Batch

```text
candidate_transition_problem.py
candidate_residue_inventory.py
candidate_locality_filter.py
candidate_weighted_neutralizer.py
candidate_source_trace_filter.py
candidate_divergence_filter.py
candidate_transition_route_classifier.py
candidate_transition_batch_reconcile.py
order.txt
```

## Script Intent

### 1. candidate_transition_problem.py

Open Group 59 as a transition-term audit, not insertion.

### 2. candidate_residue_inventory.py

Inventory candidate ingredients:

```text
R1=(F_out-F_in)s'
R2=(F_out-F_in)s''+2(F_out'-F_in')s'
weighted shape eta=w(y)*(y-c*)
window w=(1-y^2)^2
stress basis eta^2
```

Classify them as candidate clues.

### 3. candidate_locality_filter.py

Verify endpoint locality of layer basis terms:

```text
w(-1)=w(1)=0
eta(-1)=eta(1)=0
s' endpoints vanish
s'' endpoints vanish
eta^2 endpoints vanish
```

Reject nonlocalized constant terms.

### 4. candidate_weighted_neutralizer.py

Derive a weighted-neutralization operator:

```text
N_w[f] = w*(f - mu_w[f])
mu_w[f] = integral r^2*w*f dy / integral r^2*w dy
```

Verify:

```text
integral r^2 N_w[f] dy = 0
```

For:

```text
f=y
```

recover:

```text
mu_w[y]=2Rell/(7R^2+ell^2)
```

This generalizes the Group 58 profile.

### 5. candidate_source_trace_filter.py

Reject candidate terms that carry ordinary source or double-count trace:

```text
source residual S_M*(i_A+i_layer-1)
trace residual T_zeta*(i_Bs+i_layer+i_res-1)
```

A layer term may survive only if it is interpreted as source-neutral transition response, not ordinary source and not extra trace count.

### 6. candidate_divergence_filter.py

Test reduced divergence status:

```text
D=p_r'+2(p_r-p_t)/r
```

Reject scalar/radial stress without closure. Retain closure route:

```text
p_t=p_r+r*p_r'/2
```

### 7. candidate_transition_route_classifier.py

Classify term families.

Expected survivor:

```text
localized weighted-neutral transition response;
stress-only / closure-supported;
source-neutral;
trace-neutral;
conditional;
not insertable.
```

### 8. candidate_transition_batch_reconcile.py

Prepare result notes and summary.

## Expected Summary Shape

Likely result:

```text
Group 59 opened a candidate transition-term surface.
Raw residues are clues, not insertions.
A weighted-neutralization operator was derived and reproduced Group 58 skew.
Nonlocalized, scalar-charge-carrying, source-carrying, trace-double-counting, and divergence-failing term families were rejected.
A narrow localized weighted-neutral closure-supported transition response survives conditionally.
Physical use remains blocked.
```

## Safe Handoff Options

Depending on outputs, Group 60 could be:

```text
60_covariant_layer_lift
60_weighted_source_safety
60_layer_energy_minimizer
60_candidate_term_exclusion_sieve
```
