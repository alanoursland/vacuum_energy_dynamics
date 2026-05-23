# Source Routing and Mass Neutrality Plan

## Canonical Filename

```text
source_routing_and_mass_neutrality_plan.md
```

## Group Name

```text
21_source_routing_and_mass_neutrality
```

## Why This Group Comes Next

Group 20 closed the no-overlap / projection audit with a negative but useful result:

```text
No universal active O is defined.

No-overlap remains a theorem target.

Role-specific projector requirements are explicit.

Diagnostic-only labels are safe only if they do not alter equations.

Parent equation forms remain not ready.
```

That means the next group should not assume a real projector exists.

It should also not try to write the parent field equation.

The most repeated unresolved obligation after Groups 16–20 is:

```text
mass neutrality outside the A-sector.
```

Many branches require this but do not yet prove it:

```text
zeta residual,
kappa residual,
J_V,
J_sub,
J_exch,
curvature admissibility,
e_curv,
H_curv,
H_exch,
boundary smoothing,
metric insertion,
residual-kill,
source routing,
ordinary matter decoupling.
```

The A-sector has the strongest reduced reconstruction and gives a clean exterior mass charge through A-flux. Therefore Group 21 should use that as the reference charge and audit every other sector against it.

Tiny goblin reason:

```text
Count the mass coins before opening another magic door.
```

---

## Central Question

```text
Can the ordinary closed regime enforce that exterior mass charge is carried
only by the A-sector, while all non-A sectors remain mass-neutral, scalar-silent,
boundary-neutral, diagnostic, or non-metric unless separately derived?
```

Equivalently:

[
\rho / M_{\rm enc}\rightarrow A\text{-flux}
]

and:

[
\delta M_{\rm ext}|_{\rm non-A}=0.
]

The group should not ask whether other sectors exist.

They do.

It should ask whether they are allowed to alter ordinary exterior mass.

---

## Current Starting Status

From the current field-equation snapshot:

```text
A-sector:
  strongest reduced branch.

A_ext:
  A = 1 - 2GM/(c^2 r).

A-flux mass:
  F_A = 4pi r^2 A'.

B_s / A_spatial:
  recovery theorem target.

zeta:
  volume-form candidate.

kappa:
  diagnostic / non-metric / separately neutral unless derived.

J_V:
  unresolved.

J_sub / J_exch:
  role-level only.

O:
  not active; theorem target only.

A_curv / e_curv:
  diagnostic / accounting only.

H_curv / H_exch:
  not defined and not insertable.

Parent equation:
  not ready.
```

Group 21 should preserve all of this.

It should not weaken the A-sector result, and it should not upgrade any non-A object into an active source by accident.

---

## What This Group Is Not

This group is not:

```text
a parent field equation group,
a no-overlap projector group,
a metric insertion group,
a vacuum current definition group,
a curvature dynamics group,
a correction tensor insertion group,
a dark-sector group,
an anti-singularity group,
a PPN recovery group,
a GR-copy group.
```

It is also not a group for choosing coefficients by recovery.

It is a mass-routing audit.

---

## Core Discipline Rules

```text
Do not let non-A sectors shift M_ext by declaration.

Do not use O to enforce mass neutrality.

Do not use residual-kill as if it were derived.

Do not let zeta or kappa carry a 1/r exterior scalar tail.

Do not let J_V become a hidden mass current.

Do not let J_sub gravitate by being a pure wind.

Do not let J_exch repair ordinary matter routing.

Do not let e_curv become source energy.

Do not let H_curv or H_exch enter a field equation.

Do not treat boundary smoothing as mass preservation.

Do not choose boundary conditions by Schwarzschild recovery.

Do not use gamma_like, AB, or B=1/A as construction rules.

Do not reroute ordinary T_mu_nu into multiple independent sources.
```

Tiny goblin guardrail:

```text
No second mass spoon.
No hidden tail.
No boundary purse.
```

---

## Group Success Criterion

A useful success would produce a mass-neutrality ledger:

```text
A-sector mass charge:
  defined operationally.

Non-A sectors:
  audited for whether they can alter exterior mass.

Residual scalar tails:
  classified by surface flux.

Boundary behavior:
  tested for mass leakage.

Ordinary source routing:
  protected from double-counting.

Failure conditions:
  explicit.
```

A stronger success would produce a theorem target:

```text
Ordinary closed-regime mass neutrality theorem:

  M_ext = M_A

  delta M_ext|zeta_residual = 0
  delta M_ext|kappa_residual = 0
  delta M_ext|J_V = 0
  delta M_ext|J_sub = 0
  delta M_ext|J_exch = 0
  delta M_ext|A_curv/e_curv = 0
  delta M_ext|H_curv/H_exch = 0
```

A good negative success would say:

```text
Mass neutrality is not derived.

The A-sector remains the only licensed exterior mass-charge carrier.

All other sectors remain diagnostic, non-metric, compact/neutral, or theorem-targeted.
```

---

## Group Failure Criterion

The group fails if it allows:

```text
mass neutrality by assumption,
O as mass-neutrality patch,
boundary counterterm preserving mass by name,
zeta/kappa scalar tail with nonzero exterior flux,
J_V shifting M_ext,
J_sub gravitating by existence,
J_exch repairing ordinary matter,
curvature admissibility acting as mass source,
e_curv as source reservoir,
H_curv/H_exch insertion,
dark-sector mass patch,
recovery-fitted boundary behavior,
ordinary matter double-counting,
sector ledger mistaken for theorem.
```

---

# Recommended Script Chain

The group should remain narrow. A likely chain is ten scripts.

---

# 1. `candidate_A_sector_mass_charge_definition.py`

## Locked-Door Question

```text
What is the operational exterior mass charge in the current theory?
```

## Purpose

Define the A-sector mass charge as the reference quantity.

## Core Definitions

Areal flux:

[
F_A(r)=4\pi r^2 A'(r).
]

A-sector exterior mass:

[
M_A(r)=\frac{c^2}{8\pi G}F_A(r).
]

For exterior vacuum:

[
F_A=\text{constant},
]

so:

[
M_A=M_{\rm ext}.
]

For Schwarzschild exterior:

[
A=1-\frac{2GM}{c^2r},
]

[
A'=\frac{2GM}{c^2r^2},
]

so:

[
F_A=4\pi r^2A'=\frac{8\pi GM}{c^2},
]

and:

[
M_A=M.
]

## Required Output

```text
M_A is the only currently derived exterior mass charge.

All other sectors must be checked against delta M_A = 0
unless independently derived as modifying the mass definition.
```

## Expected Result

```text
A-sector mass charge is DERIVED_REDUCED.

It becomes the reference for all neutrality audits.
```

Possible next script:

```text
candidate_non_A_sector_mass_neutrality_inventory.py
```

---

# 2. `candidate_non_A_sector_mass_neutrality_inventory.py`

## Locked-Door Question

```text
Which non-A sectors could accidentally carry or shift exterior mass?
```

## Purpose

Inventory every non-A branch that might leak mass charge.

## Sectors To Audit

```text
B_s / A_spatial,
zeta residual,
kappa residual,
epsilon_vac_config,
e_kappa,
J_V,
J_sub,
J_exch,
Sigma_V / R_V,
Sigma_exch / R_exch,
A_curv,
e_curv,
J_curv,
H_curv,
H_exch,
boundary smoothing,
metric insertion,
dark-sector labels.
```

## Required Classification

For each sector:

```text
can enter A-flux?
can create 1/r scalar tail?
can shift boundary A'?
can change M_A?
can alter measured M_ext?
is it metric, non-metric, diagnostic, or theorem target?
what neutrality condition is required?
```

## Expected Result

Likely result:

```text
Most non-A sectors are not licensed to carry mass.
They require explicit delta M_ext = 0 conditions.
```

Possible next script:

```text
candidate_residual_scalar_tail_flux_audit.py
```

---

# 3. `candidate_residual_scalar_tail_flux_audit.py`

## Locked-Door Question

```text
What exterior scalar tails are automatically mass-dangerous?
```

## Purpose

Audit scalar residual tails by surface flux.

## Core Test

For a scalar residual tail:

[
\phi_{\rm tail}=\frac{C}{r},
]

surface flux is:

[
F_\phi=4\pi r^2\phi'
=4\pi r^2\left(-\frac{C}{r^2}\right)
=-4\pi C.
]

Thus a (1/r) residual scalar tail carries nonzero exterior scalar flux unless:

[
C=0.
]

## Apply To

```text
zeta_residual,
kappa_residual,
J_V-induced scalar residue,
A_curv scalar residue,
H_curv/H_exch scalar leakage,
boundary shell scalar residue.
```

## Required Result

```text
Any ordinary-sector residual scalar tail with C != 0 fails neutrality
unless it is explicitly routed through the A-sector mass charge.
```

## Expected Result

```text
Exterior scalar silence requires C_residual = 0.
```

Possible next script:

```text
candidate_boundary_flux_mass_preservation.py
```

---

# 4. `candidate_boundary_flux_mass_preservation.py`

## Locked-Door Question

```text
Can boundary or smoothing behavior preserve A-sector mass without repair?
```

## Purpose

Test boundary mass preservation.

## Required Conditions

At a matter boundary or transition region:

```text
A-flux outside must remain fixed by A-sector mass charge.

Non-A boundary behavior must not change exterior A'.

No boundary shell source may be hidden.

No smoothing layer may tune M_ext.

No residual scalar tail may emerge.

No curvature or exchange boundary term may shift mass.
```

In symbols:

[
\delta F_A|_{\rm boundary,non-A}=0,
]

[
\delta M_A|_{\rm boundary,non-A}=0.
]

## Branches

```text
smooth compact residual,
C1 residual profile,
C2 residual profile,
boundary shell source,
surface counterterm,
diagnostic boundary audit,
residual-kill convention,
neutral residual theorem target.
```

## Rejected

```text
boundary repair current,
R_V boundary cancellation,
H boundary counterterm,
curvature boundary rescue,
recovery-tuned smoothing,
sharp support that hides shell charge.
```

## Expected Result

Likely result:

```text
Boundary mass preservation remains theorem target.
Only compact/neutral diagnostic behavior is safe.
```

Possible next script:

```text
candidate_zeta_kappa_mass_neutrality_conditions.py
```

---

# 5. `candidate_zeta_kappa_mass_neutrality_conditions.py`

## Locked-Door Question

```text
Under what conditions can zeta/kappa exist without shifting exterior mass?
```

## Purpose

Apply mass-neutrality logic to the residual trace variables.

## Starting Rules

```text
zeta may be a volume-form candidate.

kappa is diagnostic / non-metric / separately neutral unless derived.

If zeta enters B_s,
residual zeta/kappa metric trace is killed or non-metric.

No Box zeta.

No Box kappa.

No exterior zeta/kappa 1/r tail.
```

## Required Conditions

```text
zeta_residual_metric = 0
or exterior-neutral with C_zeta = 0.

kappa_residual_metric = 0
or exterior-neutral with C_kappa = 0.

e_kappa does not become source reservoir.

epsilon_vac_config does not shift M_A.

residual relaxation does not alter A-flux.
```

In compact form:

[
\delta M_A|*{\zeta*{\rm residual}}=0,
]

[
\delta M_A|*{\kappa*{\rm residual}}=0.
]

## Expected Result

Likely result:

```text
Residual-kill / non-metric residual remains the safest convention.

Neutral residual metric trace remains theorem-heavy.
```

Possible next script:

```text
candidate_JV_mass_neutrality_conditions.py
```

---

# 6. `candidate_JV_mass_neutrality_conditions.py`

## Locked-Door Question

```text
Can J_V, J_sub, or J_exch be ordinary-sector mass-neutral?
```

## Purpose

Audit vacuum-current branches for exterior mass leakage.

## Starting Status

```text
J_V:
  unresolved.

J_sub/J_exch:
  role-level only.

Sigma/R:
  role-level only.

Flux direction:
  missing.

u_vac:
  unresolved / domain-limited.
```

## Required Conditions

For (J_V):

```text
no independent A-flux shift,
no exterior scalar charge,
no far-zone scalar current,
no boundary repair,
no scalar trace source.
```

For (J_{\rm sub}):

```text
pure wind neutrality,
no M_ext shift,
no ordinary matter push,
no scalar trace,
no boundary repair,
no preferred-frame force.
```

For (J_{\rm exch}):

```text
no ordinary-sector source side by convenience,
no matter rerouting,
no repair current,
zero-net or zero-creation ordinary branch unless derived otherwise.
```

In symbols:

[
\delta M_A|_{J_V}=0,
]

[
\delta M_A|*{J*{\rm sub}}=0,
]

[
\delta M_A|*{J*{\rm exch}}=0.
]

## Expected Result

Likely result:

```text
Vacuum currents remain role-level unless mass-neutrality and source laws are derived.

Zero-net exchange, zero creation, curvature-from-warping,
and latent exchange remain safest ordinary-sector branches.
```

Possible next script:

```text
candidate_curvature_accounting_mass_neutrality.py
```

---

# 7. `candidate_curvature_accounting_mass_neutrality.py`

## Locked-Door Question

```text
Can curvature admissibility or e_curv affect exterior mass?
```

## Purpose

Protect curvature diagnostics from becoming hidden sources.

## Starting Status

```text
A_curv:
  diagnostic / branch-filter theorem target.

e_curv:
  diagnostic / accounting only.

J_curv:
  unresolved.

curvature balance:
  theorem target only.

anti-singularity:
  theorem target only.
```

## Required Conditions

```text
A_curv does not alter A-flux.

e_curv is not source energy.

J_curv is not repair current.

curvature admissibility does not change M_ext.

curvature boundary behavior does not smooth mass by repair.

curvature branch filtering is not dynamics.
```

In symbols:

[
\delta M_A|*{A*{\rm curv}}=0,
]

[
\delta M_A|*{e*{\rm curv}}=0,
]

[
\delta M_A|*{J*{\rm curv}}=0
\quad \text{unless }J_{\rm curv}\text{ is independently derived.}
]

## Rejected

```text
e_curv as source reservoir,
curvature balance as mass repair,
J_curv as gradient-by-fiat,
branch-kill called bounce,
H_curv introduced as curvature rescue.
```

## Expected Result

Likely result:

```text
Curvature remains diagnostic / branch-filter only.
Mass neutrality is required and not derived.
```

Possible next script:

```text
candidate_correction_tensor_mass_neutrality_guard.py
```

---

# 8. `candidate_correction_tensor_mass_neutrality_guard.py`

## Locked-Door Question

```text
Could H_curv or H_exch alter exterior mass if inserted?
```

## Purpose

Show why correction tensors remain non-insertable without mass neutrality.

## Starting Status

```text
H_curv:
  not defined,
  not insertable.

H_exch:
  not defined,
  not insertable.

Divergence safety:
  required, not derived.

Source separation:
  required, not derived.

Boundary/mass neutrality:
  required, not derived.
```

## Required Conditions For Future Insertability

Any future (H) must satisfy:

```text
independent tensor definition,
independent source-side counterpart,
divergence safety,
ordinary matter separation,
A-sector mass neutrality,
scalar trace neutrality,
boundary neutrality,
far-zone flux neutrality,
no shell source,
no recovery tuning.
```

In symbols:

[
\delta M_A|*{H*{\rm curv}}=0,
]

[
\delta M_A|*{H*{\rm exch}}=0,
]

unless a future parent identity explicitly redefines total mass in a derived way.

## Rejected

```text
H as M_ext correction,
H as scalar tail cancellation,
H as boundary counterterm,
H as Bianchi paint,
H as source-by-divergence,
H as dark-sector patch.
```

## Expected Result

Likely result:

```text
H_curv/H_exch remain diagnostic-only audit labels.
No correction tensor is insertable.
```

Possible next script:

```text
candidate_source_routing_no_double_counting.py
```

---

# 9. `candidate_source_routing_no_double_counting.py`

## Locked-Door Question

```text
Can ordinary matter be routed without being counted multiple times?
```

## Purpose

Consolidate source-routing rules.

## Current Ordinary Routing

```text
rho / M_enc -> A-sector mass charge.

longitudinal current -> scalar continuity / density redistribution.

transverse current -> W_i.

TT stress / quadrupole -> h_TT.

pressure / trace -> diagnostic or non-metric kappa/zeta relaxation only if neutral.

ordinary scalar radiation -> rejected.

ordinary matter -> not rerouted into J_sub/J_exch/Sigma_exch/H_exch/H_curv.
```

## Required No-Double-Counting Rules

```text
rho does not also source kappa mass charge.

pressure trace does not create exterior kappa Poisson charge.

ordinary T_mu_nu does not become Sigma_exch by convenience.

curvature diagnostics do not become matter sources.

H tensors do not absorb ordinary source mismatch.

dark labels do not patch ordinary failure.

zeta/kappa residuals do not become second scalar metric source.

energy/accounting terms do not become coefficient reservoirs.
```

## Expected Result

```text
Source routing remains constrained but not parent-derived.

Mass neutrality sharpens which future source theorems are required.
```

Possible next script:

```text
candidate_group_21_source_routing_status_summary.py
```

---

# 10. `candidate_group_21_source_routing_status_summary.py`

## Purpose

Close Group 21 with a status summary.

This summary should record:

```text
A-sector mass charge definition,
non-A mass-neutrality inventory,
residual scalar tail flux audit,
boundary mass preservation status,
zeta/kappa neutrality,
J_V/J_sub/J_exch neutrality,
curvature neutrality,
correction tensor neutrality,
ordinary source routing,
double-counting guardrails.
```

## Good Closure Outcomes

### Outcome A: A-Sector Charge Protected

```text
M_A = c^2 F_A / (8pi G)
is the only currently derived exterior mass charge.
```

### Outcome B: Non-A Sectors Neutral Or Deferred

```text
All non-A sectors must satisfy delta M_A = 0
or remain diagnostic / non-metric / theorem-targeted.
```

### Outcome C: Scalar Tail Rule

```text
Any residual 1/r scalar tail carries nonzero surface flux.
Ordinary residual exterior scalar tails must vanish.
```

### Outcome D: Boundary Mass Preservation Still Theorem Target

```text
Boundary neutrality is required but not derived.
```

### Outcome E: Parent Equation Still Not Ready

```text
Mass-neutrality requirements sharpen future parent identity,
but do not make it available.
```

## Handoff Options After Group 21

If mass routing clarifies enough:

```text
22_metric_insertion_recovery_retest
```

If source routing remains too unresolved:

```text
22_boundary_neutrality_and_scalar_silence
```

If the A-sector mass charge is now stable enough for observational comparison:

```text
22_reduced_observational_audit
```

If a real route to source projectors appears:

```text
22_role_specific_source_projectors
```

Do not choose until Group 21 closes.

---

## Known Unknowns Carried Into Group 21

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

## Group 21 Output Should Not Claim

```text
mass neutrality is solved,
boundary neutrality is solved,
ordinary matter decoupling is solved,
J_V is defined,
J_sub/J_exch are real currents,
O exists,
B_s/F_zeta insertion is derived,
H_curv/H_exch are insertable,
curvature dynamics are derived,
parent field equation is ready.
```

---

## Group 21 Should Preserve

```text
A-sector mass result remains protected.

A-flux defines the current reduced exterior mass charge.

B_s/F_zeta insertion remains theorem target.

Residual-kill / non-metric residual remains provisional.

O remains unresolved.

J_V remains unresolved.

J_sub/J_exch remain role-level only.

Sigma/R remain role-level only.

A_curv remains diagnostic / branch-filter only.

e_curv remains diagnostic / accounting only.

J_curv remains undefined.

H_curv/H_exch remain non-insertable.

Ordinary matter stays routed to A-sector unless a theorem derives otherwise.

Pure wind is not gravity.

Exchange is not repair.

Dark sector is not patch.

Boundary and exterior scalar neutrality remain obligations.

Recovery remains downstream.

No scalar charge leakage.

No exterior mass shift from non-A sectors.
```

---

## Final Summary

Group 21 should decide how exterior mass charge is protected.

Core rule:

```text
A carries the ordinary exterior mass coin.
Every other sector must show empty pockets.
```

Operational target:

```text
Define M_A from A-flux,
then audit zeta, kappa, J_V, J_sub, J_exch, curvature diagnostics,
and correction-tensor candidates for mass neutrality.
```

Good failure:

```text
Mass neutrality remains theorem-targeted.
Non-A sectors stay diagnostic, non-metric, role-level, or deferred.
Parent equation remains not ready.
```

Tiny goblin label:

```text
No second mass spoon.
No hidden 1/r tail.
No boundary purse.
Show the flux, or drop the coin.
```
