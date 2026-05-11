# Boundary Neutrality and Scalar Silence Plan

## Canonical Filename

```text
boundary_neutrality_and_scalar_silence_plan.md
```

## Group Name

```text
22_boundary_neutrality_and_scalar_silence
```

## Why This Group Comes Next

Group 21 closed by protecting the A-sector mass charge as the current reduced ordinary-exterior mass reference:

```text
M_A = c^2 F_A/(8*pi*G)
```

It also sharpened the rule that all non-A sectors must be mass-neutral, diagnostic, non-metric, role-level, non-insertable, or theorem-targeted.

The most direct remaining theorem burden is:

```text
boundary neutrality and exterior scalar silence.
```

Group 21 repeatedly found that non-A sectors become dangerous when they leave:

```text
1/r exterior scalar tails,
boundary A-tail shifts,
shell sources,
far-zone flux,
smoothing layers that tune M_ext,
or residual metric traces.
```

So Group 22 should not start with a parent equation.

It should not assume an active no-overlap operator.

It should not insert correction tensors.

It should ask:

```text
What conditions actually make boundary behavior and residual scalar sectors silent outside the ordinary source?
```

Tiny goblin reason:

```text
No boundary purse.
No hidden tail.
Show the empty edge.
```

---

## Central Question

```text
Can the ordinary closed regime enforce boundary neutrality and exterior scalar silence without repair mechanisms?
```

Equivalently:

\[
\delta F_A|_{\rm boundary,non-A}=0,
\]

\[
C_{\rm residual}=0,
\]

\[
\Phi_{\rm non-A}^{\infty}=0,
\]

with no shell source, no counterterm, no recovery-tuned smoothing, no active O, no H insertion, and no dark patch.

---

## Starting Status Imported From Group 21

```text
A-sector mass charge:
  protected reduced reference.

Non-A sectors:
  no independent exterior mass carrier licensed.

Residual scalar tails:
  C/r carries F = -4*pi*C.

Boundary A-tail:
  q/r shifts delta_M_A = -c^2 q/(2G).

Zeta/kappa:
  residual-kill / non-metric residual is safest but provisional.

J_V:
  unresolved.

J_sub/J_exch:
  role-level only.

Curvature:
  diagnostic/accounting/branch-filter only.

H_curv/H_exch:
  non-insertable.

O:
  unresolved; no universal active projector.

Parent equation:
  not ready.
```

Group 22 must preserve all of this.

---

## What This Group Is Not

This group is not:

```text
a parent field equation group,
a correction tensor insertion group,
a source projector group,
a dark-sector group,
a metric recovery group,
a PPN group,
a curvature dynamics group,
a vacuum-current definition group,
a GR-copy group.
```

It is a boundary and exterior-silence theorem-target group.

---

## Core Discipline Rules

```text
Do not preserve mass by smoothing.

Do not erase scalar tails with O.

Do not insert H as a boundary counterterm.

Do not make a shell source unless a source law independently derives it.

Do not choose boundary conditions from Schwarzschild, PPN, gamma_like, AB, or B=1/A recovery.

Do not use compact support if the derivative jump hides flux.

Do not call residual-kill a theorem.

Do not let faster falloff bypass boundary/domain checks.

Do not let diagnostic labels become source filters.

Do not let dark labels patch ordinary failure.
```

Tiny goblin guardrail:

```text
No seam-money.
No tail-ghost.
No smoothing theft.
```

---

## Group Success Criterion

A useful success would produce a boundary/silence ledger:

```text
residual scalar exterior coefficients:
  audited and required to vanish.

boundary flux:
  checked for non-A A-tail and scalar-tail leakage.

shell sources:
  classified and rejected unless independently derived.

compact support:
  allowed only with smooth matching and no hidden flux.

diagnostic residuals:
  allowed only if they have no metric, source, boundary, or A-flux effect.

future theorem targets:
  stated explicitly.
```

A stronger success would produce a theorem target:

```text
Ordinary closed-regime boundary neutrality and scalar silence theorem:

  delta F_A|boundary,non-A = 0
  C_zeta = 0
  C_kappa = 0
  C_JV = 0
  C_curv = 0
  C_H = 0
  I_non-A = 0
  no shell source
  no recovery-tuned smoothing
  no boundary counterterm
```

A good negative success would say:

```text
Boundary neutrality is not derived.

Exterior scalar silence is not derived.

Only diagnostic, non-metric, compact-neutral, smooth-matched, or theorem-targeted behavior is safe.
```

---

## Group Failure Criterion

The group fails if it allows:

```text
boundary neutrality by assumption,
scalar silence by assumption,
O as scalar-tail eraser,
H as boundary counterterm,
smoothing chosen after recovery failure,
shell source hidden by derivative jump,
compact support without matching law,
residual-kill treated as derived no-overlap,
dark label boundary patch,
curvature boundary rescue,
exchange boundary repair,
J_V boundary current without definition,
source cancellation across non-A sectors,
recovery-selected boundary condition.
```

---

# Recommended Script Chain

The group should remain narrow. A likely chain is eight scripts.

---

# 1. `candidate_boundary_scalar_silence_targets.py`

## Locked-Door Question

```text
What exactly must vanish for boundary neutrality and exterior scalar silence?
```

## Purpose

Define the target ledger for Group 22.

## Required Targets

```text
delta F_A|boundary,non-A = 0
C_zeta = 0
C_kappa = 0
C_JV = 0
C_curv = 0
C_H = 0
I_non-A = 0
no shell source
no recovery-tuned smoothing
no active O
no H insertion
```

## Expected Result

```text
Boundary/scalar silence is a theorem target, not yet derived.
```

Possible next script:

```text
candidate_smooth_compact_support_no_shell_conditions.py
```

---

# 2. `candidate_smooth_compact_support_no_shell_conditions.py`

## Locked-Door Question

```text
When does compact support avoid hiding a shell source?
```

## Purpose

Test value/slope matching conditions.

## Core Tests

For a residual profile \(\phi(r)\) supported inside or near boundary \(R\):

```text
phi(R) = 0
phi'(R) = 0
```

are safer than value continuity alone.

## Branches

```text
C0 match only,
C1 match,
C2 diagnostic profile,
smooth compact bump,
sharp cutoff,
derivative jump,
delta-shell source.
```

## Expected Result

```text
Compact support is safe only with smooth matching and no hidden boundary flux.
```

Possible next script:

```text
candidate_scalar_tail_silence_sector_conditions.py
```

---

# 3. `candidate_scalar_tail_silence_sector_conditions.py`

## Locked-Door Question

```text
Which sectors must have vanishing exterior 1/r scalar coefficients?
```

## Purpose

Apply scalar silence to each residual sector.

## Sectors

```text
zeta,
kappa,
J_V residue,
J_sub residue,
J_exch residue,
A_curv/e_curv residue,
J_curv residue,
H trace leakage,
boundary shell residue,
dark label residue.
```

## Expected Result

```text
All ordinary-sector residual scalar coefficients must vanish or remain strictly non-metric/diagnostic.
```

Possible next script:

```text
candidate_boundary_current_flux_silence.py
```

---

# 4. `candidate_boundary_current_flux_silence.py`

## Locked-Door Question

```text
Can non-A boundary or far-zone currents remain silent?
```

## Purpose

Audit current fluxes.

## Core Tests

For radial current:

\[
j^r=\frac{I}{4\pi r^2},
\]

sphere flux is:

\[
\Phi=I.
\]

Silence requires:

\[
I=0
\]

unless a future theorem gives a neutral transport interpretation.

## Expected Result

```text
J_V, J_sub, J_exch, J_curv, and H fluxes remain theorem-targeted or zero in ordinary exterior.
```

Possible next script:

```text
candidate_boundary_repair_route_exclusion.py
```

---

# 5. `candidate_boundary_repair_route_exclusion.py`

## Locked-Door Question

```text
Which boundary repair routes must remain rejected?
```

## Purpose

Inventory forbidden repair mechanisms.

## Rejected

```text
surface counterterm,
boundary repair current,
R_V boundary cancellation,
J_exch repair,
curvature boundary rescue,
H boundary counterterm,
O boundary eraser,
dark boundary patch,
recovery-tuned smoothing,
sharp support hiding shell charge.
```

## Expected Result

```text
Boundary repair routes remain rejected unless independently derived before the failure they repair.
```

Possible next script:

```text
candidate_diagnostic_residual_nonmetric_conditions.py
```

---

# 6. `candidate_diagnostic_residual_nonmetric_conditions.py`

## Locked-Door Question

```text
When can a residual survive as diagnostic/non-metric without affecting mass or boundary behavior?
```

## Purpose

Clarify safe diagnostic residual conditions.

## Required Conditions

```text
no A-flux effect,
no metric trace effect,
no source role,
no boundary flux,
no far-zone tail,
no coefficient reservoir,
no later re-entry through accounting,
no recovery tuning.
```

## Expected Result

```text
Diagnostic residuals are safe only if they remain causally inert for metric/source/boundary/mass routing.
```

Possible next script:

```text
candidate_boundary_neutrality_theorem_obligations.py
```

---

# 7. `candidate_boundary_neutrality_theorem_obligations.py`

## Locked-Door Question

```text
What theorem obligations are required before claiming boundary neutrality?
```

## Purpose

Turn boundary/scalar silence requirements into explicit obligations.

## Obligations

```text
derive no-shell condition,
derive residual scalar silence,
derive non-A boundary A-flux neutrality,
derive current flux silence,
derive compact-support matching law,
derive diagnostic residual non-reentry,
derive no recovery-tuned boundary data,
derive source routing compatibility.
```

## Expected Result

```text
Boundary neutrality remains theorem-targeted with explicit prerequisites.
```

Possible next script:

```text
candidate_group_22_boundary_neutrality_status_summary.py
```

---

# 8. `candidate_group_22_boundary_neutrality_status_summary.py`

## Purpose

Close Group 22 with a status summary.

This summary should record:

```text
boundary/scalar silence targets,
smooth compact support and no-shell conditions,
sector scalar-tail silence,
boundary/current flux silence,
repair-route exclusions,
diagnostic residual non-metric conditions,
theorem obligations,
handoff options.
```

## Good Closure Outcomes

### Outcome A: Silence Targets Explicit

```text
The exact vanishing conditions are visible.
```

### Outcome B: Repair Routes Rejected

```text
No boundary or scalar silence repair route is licensed.
```

### Outcome C: Diagnostic Residuals Constrained

```text
Residuals may survive only if non-metric, diagnostic, compact-neutral, and non-reentering.
```

### Outcome D: Boundary Neutrality Still Theorem Target

```text
The theorem burden is clearer, not solved by naming it.
```

### Outcome E: Parent Equation Still Not Ready

```text
Boundary/scalar silence requirements may prepare a parent identity,
but do not provide one.
```

---

## Handoff Options After Group 22

If boundary/scalar silence clarifies enough:

```text
23_metric_insertion_recovery_retest
```

If the theorem burden is still too high:

```text
23_smooth_support_and_matching_laws
```

If source projectors become plausible:

```text
23_role_specific_boundary_projectors
```

If the A-sector plus silence ledger is stable enough:

```text
23_reduced_observational_audit
```

Do not choose until Group 22 closes.

---

## Known Unknowns Carried Into Group 22

```text
boundary mass preservation theorem,
static-source neutrality theorem,
ordinary matter decoupling theorem,
B_s/F_zeta insertion law,
residual-kill derivation,
O no-overlap,
J_V definition,
J_sub/J_exch definition,
Sigma/R operators,
curvature admissibility functional,
J_curv,
H_curv/H_exch tensor definitions,
correction tensor divergence safety,
source separation,
parent identity.
```

---

## Group 22 Output Should Not Claim

```text
boundary neutrality is solved,
scalar silence is solved,
compact support is derived,
shell sources are impossible,
residual-kill is derived,
O exists,
H is insertable,
J_V is defined,
source routing is parent-derived,
B_s/F_zeta insertion is licensed,
parent field equation is ready.
```

---

## Group 22 Should Preserve

```text
A-sector mass result remains protected.

Non-A sectors do not carry exterior mass.

Residual 1/r scalar tails are dangerous.

Boundary A-tail shifts mass.

No boundary repair routes are licensed.

No active O is assumed.

No H insertion is allowed.

No dark patch is allowed.

No recovery-selected boundary behavior.

Diagnostic residuals remain inert or theorem-targeted.

Parent equation remains not ready.
```

---

## Final Summary

Group 22 should decide how boundary neutrality and exterior scalar silence are made explicit.

Core rule:

```text
No hidden tail leaves the source.
No boundary seam changes the mass coin.
```

Operational target:

```text
State and audit the vanishing conditions for residual scalar tails,
boundary A-flux shifts, far-zone non-A currents, shell sources, and repair routes.
```

Good failure:

```text
Boundary neutrality and scalar silence remain theorem-targeted,
but all repair shortcuts are rejected and all future obligations are explicit.
```

Tiny goblin label:

```text
No boundary purse.
No tail ghost.
Show the empty edge.
```
