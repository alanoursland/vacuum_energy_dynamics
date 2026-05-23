# Postmortem: `theory_v3/development/field_equation_candidates`

## Status

This directory should be frozen as an active field-equation search.

It should remain as an archive of failed routes, useful diagnostics, and one surviving formal branch. New work should not continue here except to clean up, index, or migrate surviving material into a narrower directory.

Recommended successor directory:

```text
theory_v3/development/projection_origin_probe
```

## One-Line Summary

The field-equation-candidate search produced a large amount of disciplined but overgrown scaffolding. It did not produce an active field equation. Its useful output is a smaller set of guardrails, failed-route diagnostics, and a formal projection hierarchy that may be worth one focused follow-up investigation.

## What This Directory Was Trying To Do

The directory attempted to search for parent field-equation structure behind the vacuum/spacetime theory.

The main goals were roughly:

```text
derive or constrain source routing;
understand trace/spatial response;
avoid scalar-radiation failure;
recover GR-compatible weak-field behavior;
find admissible correction or transition terms;
identify a parent divergence/conservation identity;
move toward a covariant field-equation structure.
```

The search was useful in detecting many bad routes, but it drifted into too many intermediate status artifacts.

## Final Judgment

This directory should not be treated as a failed pile of nothing.

It should also not be treated as a live field-equation candidate set.

Correct status:

```text
archive of guardrails, diagnostics, and reduced mathematical artifacts
```

Incorrect statuses:

```text
parent field equation
field-equation derivation
physical source law
vacuum burden functional
curvature-energy functional
exchange-energy theory
ready recombination package
```

## What Actually Survived

### 1. Source / Trace / Residual Discipline

The count-once logic is worth preserving.

Useful rule:

```text
ordinary source enters through one channel;
trace response enters through one channel;
residuals do not re-enter as hidden source, trace, mass, or divergence carriers.
```

This should remain a hard filter for future candidate equations.

Keep:

```text
source count-once diagnostics
trace count-once diagnostics
residual nonentry rule
A-sector mass-protection rule
scalar-tail witness
boundary flux witness
```

Do not keep expanding this into new readiness ledgers.

### 2. `B_s` Notation Repair

The search identified a real notation trap.

The overloaded `B_s` had to be split into:

```text
B_s_metric
b_s_scale
```

with candidate symbolic forms:

```text
log(B_s_metric) = 2*zeta/d
log(b_s_scale) = zeta/d
```

This split should be kept as notation hygiene.

The large trace-normalization declaration machinery around it should be compressed.

Useful result:

```text
factor-of-two burden is real;
metric coefficient and scale factor must not be collapsed.
```

Non-useful continuation:

```text
more declaration-scope groups;
more Package B adoption surfaces;
neutral F_zeta expression smuggling;
readiness ledgers without new mathematics.
```

### 3. Transition-Layer Diagnostics

The transition-layer branch produced useful reduced diagnostics and then correctly failed as a physical insertion route.

Keep as diagnostics:

```text
weighted neutrality under spherical/radial measure;
endpoint locality is not boundary legitimacy;
flat odd cancellation is not weighted neutrality;
reduced D=0 is not covariant conservation;
stress-energy accounting obstruction;
trace-free and active-mass-neutral closure conflict;
p_free remains underived.
```

Final status:

```text
transition response = diagnostic-only
```

Forbidden use:

```text
do not insert transition response into field equations;
do not use eta, eta^2, N_w, R1, R2 as physical D_layer;
do not treat reduced closure as Bianchi compatibility;
do not revive this branch without a new variational/stress principle.
```

### 4. Boundary-Lift Route Obstruction

The boundary-lift route did useful cleanup, then stalled.

Useful result:

```text
D_lift + D_boundary = 0
```

was sharpened into split obligations, but no theorem closed.

Open blockers:

```text
D_layer geometric legitimacy;
L_bulk neutrality;
L_gauge neutrality;
rho zero/exact/inert status;
boundary-lift matching theorem;
parent divergence identity.
```

Final status:

```text
boundary-lift route = blocked pending concrete input
```

Future work must provide a real object, such as:

```text
concrete boundary/layer geometry;
concrete exactness operator;
concrete boundary divergence object;
concrete covariant lift identity.
```

Without that, no more boundary-lift theorem attempts should be run.

### 5. Projection / Moment Hierarchy

This is the main surviving mathematical artifact.

Core projection representation:

```text
A[k,j] = 2 ∫_0^1 psi_k(x) phi_j(x) (1 - x^2)^4 dx
```

with:

```text
phi_j(x) = x^(2j)

psi_k(x) = x^(2k) - ((2k - 1)/(2k + 3)) x^(2k - 2)

w(x) = (1 - x^2)^4
```

The projection branch produced:

```text
weighted exactness object;
measure-gradient skew derivation;
moment-suppression hierarchy;
Beta/Cramer finite-N formula;
determinant/sign/Schur structure;
formal source-vector map;
endpoint/source-signature trends.
```

Current status:

```text
formal weighted projection / auxiliary admissibility hierarchy
```

Not current status:

```text
physical source law;
vacuum burden;
J_curv;
H_curv;
H_exch;
field equation;
parent equation.
```

This branch should be migrated into a new focused directory.

Recommended destination:

```text
theory_v3/development/projection_origin_probe
```

## What Went Wrong

### 1. Group Inflation

Too many groups were created for state management rather than construction.

Repeated pattern:

```text
blocker found;
blocker inventoried;
decision surface built;
preconditions listed;
readiness reviewed;
nothing adopted;
next group repeats at a higher meta-level.
```

This created local coherence but poor global progress.

### 2. Candidate Hoarding

Several branches stayed alive after they should have been frozen.

Examples:

```text
active O;
boundary-lift matching;
trace-normalization adoption;
transition insertion;
rho exactness without payload inertness;
D_layer without geometry.
```

A candidate should not survive merely because it has not been disproven. It should survive only if it has a concrete object, theorem target, or testable derivation path.

### 3. Compatibility Was Often Mistaken For Origin

Several scripts derived values or signs required for compatibility.

Examples:

```text
sigma = 1;
a_jump = -1;
a_layer = -1;
a_tail = -1;
rho = 0;
D_layer anti-match;
trace branch forms.
```

Compatibility values are not derivations.

A future route must distinguish:

```text
value required for cancellation
```

from:

```text
value forced by geometry, variational structure, or conservation law
```

### 4. Diagnostic Objects Kept Trying To Become Physical Objects

The transition-layer branch repeatedly generated useful diagnostics. Those diagnostics then tried to reappear as candidate physical terms.

Final rule:

```text
diagnostic evidence may constrain future equations;
diagnostic evidence may not become a field-equation term by relabeling.
```

### 5. Too Much Governance, Not Enough Object Construction

The best groups introduced actual objects:

```text
rho = dJ/dy;
weighted measure mu;
projection matrix A;
test functions psi_k;
source-vector map b_k(S);
Schur pivots;
moment hierarchy.
```

The weakest groups introduced statuses:

```text
ready;
compatible-if-declared;
future target;
adoption surface;
scope record;
route split;
ledger.
```

Statuses are useful only when they stop false promotion. They are not progress by themselves.

## What Should Be Kept In This Directory

Keep this directory as an archive with a short index.

Recommended retained files or sections:

```text
source_trace_residual_guardrails.md
trace_normalization_notation_split.md
transition_layer_diagnostic_ledger.md
boundary_lift_obstruction_ledger.md
projection_hierarchy_handoff.md
failed_routes_index.md
```

The current large sequence of numbered groups should not be treated as equally important.

## What Should Be Moved Out

Move the projection hierarchy work to:

```text
theory_v3/development/projection_origin_probe
```

Move or summarize these topics there:

```text
exactness object;
weighted skew derivation;
moment hierarchy;
Beta/Cramer formula;
determinant/sign/Schur work;
formal projection representation;
residual/source reconstruction;
source-vector signature classification;
boundary/endpoint trend analysis.
```

Do not move the whole field-equation-candidate directory. Only move the compact branch.

## What Should Be Frozen

Freeze these branches unless new concrete input appears:

```text
active O;
boundary-lift matching;
D_layer legitimacy;
transition response insertion;
Package B adoption;
trace normalization declaration;
parent recombination;
field-equation construction.
```

Frozen does not mean deleted. It means:

```text
no new scripts;
no new groups;
no status churn;
only revisit with a concrete mathematical object or explicit theory-owner axiom.
```

## What Should Be Deleted Or Compressed

Compress repeated readiness/declaration groups into one archival note.

Candidates for compression:

```text
trace-normalization decision surfaces;
paired declaration readiness records;
Package B adoption surfaces;
repeated safe-membership precondition ledgers;
repeated no-insertion reminders;
boundary-lift route summaries without new objects.
```

The compressed note should say:

```text
These groups established notation and guardrails, but did not produce a physical law or insertion rule.
```

## Current Best Next Step

Do not continue this directory.

Start:

```text
theory_v3/development/projection_origin_probe
```

First target:

```text
derive or kill the origin of psi_k
```

Core question:

```text
Why does the row-test function have the form

psi_k(x) = x^(2k) - ((2k - 1)/(2k + 3)) x^(2k - 2)?
```

Possible origins to test:

```text
weighted orthogonality;
integration by parts;
Sturm-Liouville-like operator;
boundary term cancellation;
moment-ratio identity;
projection residual;
pure artifact of construction.
```

Success means:

```text
psi_k and w(x) arise naturally from an operator/source/boundary problem.
```

Failure means:

```text
the projection hierarchy is probably only formal admissibility machinery.
```

Either outcome is useful.

## Decision Rules Going Forward

Use these rules before adding new work.

### Rule 1: No object, no theorem attempt.

A new group must start from a concrete object:

```text
operator;
functional;
measure;
boundary condition;
source profile;
projection identity;
geometric variable.
```

Labels do not count.

### Rule 2: No compatibility-only promotion.

If a value is chosen because it makes a residual vanish, it is compatibility-only until independently derived.

### Rule 3: No diagnostic promotion.

Diagnostic profiles, witnesses, and reduced checks cannot become physical terms.

### Rule 4: No parent equation before conservation identity.

Parent recombination stays blocked until a divergence/Bianchi-compatible identity exists.

### Rule 5: No physical ledger assignment without source/origin.

Do not call something curvature energy, exchange energy, burden, or source unless the functional/source/current is defined.

## Final Archive Status

Recommended archive label:

```text
field_equation_candidates = archived exploratory search
```

Recommended successor label:

```text
projection_origin_probe = active focused investigation
```

## Final Summary

The `field_equation_candidates` directory was useful as a filter and failure detector. It should not remain the active home of the theory search.

Its main surviving output is not a field equation.

Its main surviving output is:

```text
a formal weighted projection hierarchy with possible admissibility significance,
plus a set of guardrails preventing common false derivations.
```

The next project is to determine whether that hierarchy has a real operator/source/boundary origin.

If it does, continue from there.

If it does not, archive the whole branch.

```
