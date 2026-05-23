# Smooth Support And Matching Laws Plan

## Canonical Filename

```text
smooth_support_and_matching_laws_plan.md
```

## Group Name

```text
23_smooth_support_and_matching_laws
```

## Why This Group Comes Next

Group 22 closed as a requirements / diagnostic audit for boundary neutrality and exterior scalar silence.

It made the target ledger explicit:

```text
delta F_A|boundary,non-A = 0
C_i = 0 sector-wise
I_nonA = 0
no shell source
no recovery-tuned smoothing
no active O
no H insertion
```

It also showed that:

```text
C1 value matching can still carry boundary flux.

C2 and smooth compact toy profiles have zero toy boundary flux,
but remain diagnostics, not support theorems.

Repair routes remain rejected.

Diagnostic residuals must remain inert and non-reentering.

Boundary neutrality and scalar silence remain theorem-targeted.

Parent equation remains not ready.
```

So Group 23 should not attempt a parent equation.

It should not open H insertion.

It should not use O as an eraser.

It should not choose compact support from Schwarzschild, PPN, gamma_like, AB, or \(B=1/A\) recovery.

It should attack the next narrow locked door:

```text
What matching/support conditions are actually required to prevent shell sources,
boundary flux, scalar tails, and recovery-tuned seams?
```

Tiny goblin reason:

```text
The seam is where the ghost hides.
Inspect the seam.
```

---

## Central Question

```text
Can smooth support and boundary matching be stated strongly enough to avoid shell sources,
boundary scalar flux, A-tail mass shifts, and recovery-tuned boundary behavior?
```

Equivalently:

Given an interior residual or non-A boundary profile \(\phi(r)\), identify what must be true at a matching surface \(r=R\) so that:

```text
no value jump,
no derivative jump,
no distributional shell source,
no boundary scalar flux,
no induced A-tail,
no far-zone scalar tail,
no recovery-selected support radius,
no repair route.
```

---

## What Group 23 Is

Group 23 is a support/matching law requirements group.

It should turn the Group 22 diagnostics into a sharper matching ledger:

```text
C0 matching is not enough.
C1 value matching is not enough.
C2 value/slope matching is safer but still diagnostic.
Distributional terms must be explicitly audited.
Compact support must be structural, not imposed after failure.
Smoothing must be recovery-independent.
No-shell behavior must be shown, not named.
```

---

## What Group 23 Is Not

Group 23 is not:

```text
a parent field equation group,
a final boundary neutrality theorem,
a final scalar silence theorem,
a metric insertion group,
a recovery construction group,
a correction tensor group,
a no-overlap O group,
a dark-sector patch group,
a curvature rescue group,
a vacuum-current definition group,
an observational prediction group.
```

It may produce stronger prerequisites for boundary/scalar silence.

It should not claim boundary/scalar silence is solved unless it actually derives the relevant matching/support laws.

---

## Starting Status Imported From Group 22

```text
Boundary/scalar silence targets:
  explicit but not derived.

C1 value matching:
  risky because boundary flux can survive.

C2 / smooth compact toy profiles:
  safer diagnostics but not support laws.

Scalar-tail sector coefficients:
  must vanish or remain inert / theorem-targeted.

Current flux coefficients:
  must vanish or remain role-level / theorem-targeted.

Repair routes:
  rejected.

Diagnostic residuals:
  must be inert and non-reentering.

Parent equation:
  not ready.
```

Group 23 must preserve all of this.

---

## Core Reduced Witnesses

Group 23 should continue using the reduced witnesses:

### Scalar tail

\[
\phi_i=\frac{C_i}{r}
\]

\[
F_i=-4\pi C_i
\]

### Boundary A-tail

\[
\delta A_{\rm boundary}=\frac{q}{r}
\]

\[
\delta M_A=-\frac{c^2q}{2G}
\]

### Far-zone current

\[
j_i^r=\frac{I_i}{4\pi r^2}
\]

\[
\Phi_i=I_i
\]

### Boundary profile flux

\[
F_{\phi,R}=4\pi R^2\phi'(R)
\]

These are diagnostics, not parent equations.

---

## Core Discipline Rules

```text
Do not claim compact support from exterior zero alone.

Do not claim no-shell behavior from value matching alone.

Do not claim scalar silence from total cancellation.

Do not choose support radius or smoothing from recovery targets.

Do not use O to erase boundary leakage.

Do not use H to counterterm boundary leakage.

Do not use dark labels to absorb ordinary leakage.

Do not use exchange, curvature, or current roles as boundary repair.

Do not let diagnostic residuals re-enter through support/matching language.

Do not treat toy smooth profiles as derived support laws.
```

Tiny goblin guardrail:

```text
No seam coin.
No tail ghost.
No smoothing theft.
```

---

## Group Success Criterion

A useful success would produce:

```text
a matching regularity ladder,
a distributional shell audit,
a compact-support admissibility ledger,
a recovery-independence test,
a no-repair support law obligation,
and a clear statement of which profiles are safe only diagnostically.
```

A stronger success would derive a theorem target like:

```text
If support is structural, value and slope match at the boundary,
distributional terms vanish, and no recovery-tuned parameters enter,
then the residual profile contributes no boundary scalar flux and no shell source
in the reduced diagnostic audit.
```

A good negative success would say:

```text
Group 23 still does not derive compact support,
but it identifies the exact matching and distributional failures that must be controlled.
```

---

## Group Failure Criterion

The group fails if it allows:

```text
compact support by declaration,
C0 matching as no-shell proof,
C1 value matching as no-flux proof,
C2 toy profile as a support theorem,
smooth bump chosen after leakage appears,
support radius chosen from recovery,
derivative jump hidden as harmless,
distributional shell ignored,
O boundary eraser,
H boundary counterterm,
dark boundary patch,
exchange/curvature/current boundary repair,
residual-kill treated as derived support,
parent equation opened from matching diagnostics alone.
```

---

# Recommended Script Chain

A likely chain is eight scripts.

---

# 1. `candidate_matching_regularization_ladder.py`

## Locked-Door Question

```text
What matching regularity is required at the boundary?
```

## Purpose

Build the matching ladder:

```text
C0 value match,
C1 value+slope match,
C2 value+slope+curvature diagnostic,
smooth bump,
derived support law.
```

## Core Diagnostics

For boundary \(r=R\):

```text
phi(R)
phi'(R)
phi''(R)
F_R = 4*pi*R^2*phi'(R)
```

## Branches

```text
value jump,
value match only,
slope match,
curvature/second-derivative match,
smooth compact bump,
derived matching law.
```

## Expected Result

```text
Value matching alone is insufficient.
Slope matching is a necessary diagnostic condition.
Derived support law remains theorem-targeted.
```

Possible next script:

```text
candidate_distributional_shell_source_audit.py
```

---

# 2. `candidate_distributional_shell_source_audit.py`

## Locked-Door Question

```text
What distributional shell terms appear when boundary profiles are cut off?
```

## Purpose

Audit Heaviside and smoothed cutoff profiles.

## Core Tests

For a cutoff profile:

\[
\phi(r)=f(r)\Theta(R-r)
\]

distributional derivatives can include:

```text
delta(R-r) terms from value mismatch,
delta'(R-r) or derivative-jump terms depending on operator,
boundary flux terms from f'(R),
shell-source-like terms in reduced radial operators.
```

## Expected Result

```text
Sharp support is not neutral by declaration.
No-shell requires controlling value and derivative behavior at the support edge.
```

Possible next script:

```text
candidate_compact_support_admissibility_conditions.py
```

---

# 3. `candidate_compact_support_admissibility_conditions.py`

## Locked-Door Question

```text
When is compact support admissible rather than imposed?
```

## Purpose

Separate structural support from declared support.

## Required Conditions

```text
support follows from field/source law,
boundary value vanishes,
boundary slope vanishes,
distributional shell terms vanish,
support radius is not recovery-selected,
no hidden coefficient tuning,
no non-A A-tail,
no residual scalar 1/r exterior tail.
```

## Expected Result

```text
Compact support is admissible only with structural origin, matching, no-shell behavior, and recovery independence.
```

Possible next script:

```text
candidate_transition_layer_mass_flux_audit.py
```

---

# 4. `candidate_transition_layer_mass_flux_audit.py`

## Locked-Door Question

```text
Can a smooth transition layer hide mass or scalar flux?
```

## Purpose

Audit smoothing layers.

## Core Dangers

```text
finite transition layer carrying net scalar flux,
transition layer inducing A-tail q/r,
smoothing coefficient chosen from recovery,
smoothing absorbs residual mismatch,
layer acts as shell source in smooth disguise.
```

## Expected Result

```text
Smoothness is not enough.
Transition layers must have zero net flux, no A-tail, no scalar tail, no recovery-tuned parameters, and no hidden source load.
```

Possible next script:

```text
candidate_boundary_parameter_independence.py
```

---

# 5. `candidate_boundary_parameter_independence.py`

## Locked-Door Question

```text
Are support and smoothing parameters independent of recovery targets?
```

## Purpose

Audit parameter selection.

## Forbidden Dependencies

```text
support radius chosen to recover Schwarzschild,
smoothing width chosen to recover PPN gamma_like,
coefficient chosen to enforce AB=1,
boundary residual status chosen to pass recovery,
transition profile chosen to suppress a visible tail.
```

## Expected Result

```text
Support/matching parameters must be structural or source-derived, not recovery-selected.
```

Possible next script:

```text
candidate_matching_law_source_compatibility.py
```

---

# 6. `candidate_matching_law_source_compatibility.py`

## Locked-Door Question

```text
Can matching conditions coexist with ordinary source routing and no-double-counting?
```

## Purpose

Ensure matching conditions do not reroute ordinary matter.

## Required

```text
rho/M_enc remains A-sector routed,
no boundary shell source from ordinary rho,
no residual scalar source,
no non-A current repair,
no curvature/H/exchange/dark repair,
no source cancellation ledger.
```

## Expected Result

```text
Matching laws must not create duplicate ordinary source channels.
```

Possible next script:

```text
candidate_matching_law_theorem_obligations.py
```

---

# 7. `candidate_matching_law_theorem_obligations.py`

## Locked-Door Question

```text
What must be proved before claiming a real matching/support law?
```

## Purpose

Consolidate obligations.

## Obligations

```text
derive support origin,
derive value matching,
derive slope matching,
derive distributional shell absence,
derive transition layer neutrality,
derive recovery independence,
derive source-routing compatibility,
derive residual non-reentry,
derive no repair route.
```

## Expected Result

```text
Matching/support law remains theorem-targeted unless all obligations are closed.
```

Possible next script:

```text
candidate_group_23_matching_laws_status_summary.py
```

---

# 8. `candidate_group_23_matching_laws_status_summary.py`

## Purpose

Close Group 23.

This summary should record:

```text
matching regularity ladder,
distributional shell audit,
compact-support admissibility,
transition-layer mass/flux audit,
boundary parameter independence,
source compatibility,
theorem obligations,
handoff options.
```

## Good Closure Outcomes

### Outcome A: Matching Ladder Explicit

```text
The exact boundary regularity ladder is visible.
```

### Outcome B: Shell Dangers Explicit

```text
Sharp support and derivative jumps are classified.
```

### Outcome C: Compact Support Constrained

```text
Compact support is allowed only with structural origin, matching, no-shell, and recovery independence.
```

### Outcome D: Transition Layers Constrained

```text
Smooth transition layers cannot hide mass/scalar/source load.
```

### Outcome E: Boundary Neutrality Still Theorem Target Unless Derived

```text
If no support theorem is derived, boundary neutrality remains open.
```

---

## Handoff Options After Group 23

If Group 23 makes matching/support law sufficiently sharp:

```text
24_metric_insertion_recovery_retest
```

If matching/support still remains too underived:

```text
24_role_specific_boundary_projectors
```

If source compatibility becomes the bottleneck:

```text
24_source_compatible_boundary_laws
```

If reduced tests are ready but parent closure is not:

```text
24_reduced_observational_audit
```

Do not choose until Group 23 closes.

---

## Known Unknowns Carried Into Group 23

```text
boundary neutrality theorem,
exterior scalar silence theorem,
no-shell matching law,
compact support support law,
value/slope boundary matching theorem,
distributional shell absence theorem,
sector scalar coefficient vanishing theorem,
sector current flux neutrality theorem,
neutral transport theorem,
diagnostic residual inertness theorem,
diagnostic residual non-reentry theorem,
recovery-independent boundary data theorem,
source-routing compatibility with boundary/scalar silence,
no-repair boundary theorem,
parent identity.
```

---

## Group 23 Output Should Not Claim

```text
boundary neutrality is solved,
scalar silence is solved,
compact support is solved,
no-shell matching is solved,
residual-kill is derived,
O exists,
H is insertable,
J_V is defined,
neutral transport is derived,
source routing is parent-derived,
B_s/F_zeta insertion is licensed,
parent field equation is ready.
```

---

## Group 23 Should Preserve

```text
A-sector mass charge remains protected.

Non-A sectors do not carry exterior mass.

Residual 1/r scalar tails are dangerous.

Boundary A-tail shifts mass.

Non-A current fluxes are dangerous.

Repair routes are rejected.

No active O is assumed.

No H insertion is allowed.

No dark patch is allowed.

No recovery-selected boundary behavior.

Diagnostic residuals remain inert or theorem-targeted.

Parent equation remains not ready.
```

---

## Final Summary

Group 23 should attack the seam.

Core rule:

```text
A smooth-looking boundary is not enough.
A declared compact support is not enough.
The support and matching law must explain why there is no shell, no tail,
no current flux, no A-tail, no recovery tuning, and no source rerouting.
```

Operational target:

```text
Make the matching/support conditions precise enough that future work can test
whether boundary neutrality and scalar silence can be derived rather than repaired.
```

Good failure:

```text
Compact support and matching laws remain theorem-targeted,
but the exact regularity, distributional, parameter-independence,
and source-compatibility burdens are explicit.
```

Tiny goblin label:

```text
Inspect the seam.
Count the jumps.
Trust no smooth paint.
```
