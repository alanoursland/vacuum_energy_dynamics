# Group 21 Summary: Source Routing And Mass Neutrality

## Purpose

Group 21 tested how ordinary exterior mass charge should be protected before attempting any parent field equation, source projector, metric insertion, vacuum-current law, curvature dynamics, or correction-tensor insertion.

The group asked whether the ordinary closed regime can enforce:

```text
exterior mass charge is carried only by the A-sector,
while all non-A sectors remain mass-neutral, scalar-silent,
boundary-neutral, diagnostic, non-metric, role-level, deferred,
or theorem-targeted unless separately derived.
```

The working reference charge was the reduced A-sector areal-flux mass:

\[
F_A(r)=4\pi r^2 A'(r),
\]

\[
M_A(r)=\frac{c^2}{8\pi G}F_A(r).
\]

For the reduced exterior A-sector solution,

\[
A(r)=1-\frac{2GM}{c^2r},
\]

this gives:

\[
M_A=M.
\]

The group’s job was not to define a final covariant mass, ADM mass, source projector, no-overlap operator, or parent field equation.

The group’s job was to count the ordinary exterior mass coin and make every possible duplicate pocket visible.

Tiny goblin plaque:

```text
A carries the coin.
Everyone else shows empty pockets.
```

---

## Main Result

Group 21 is complete.

The main result is:

```text
A-sector mass charge is protected as the current reduced ordinary-exterior reference.

No non-A sector is licensed as an independent ordinary exterior mass carrier.

Residual 1/r scalar tails are mass-dangerous.

Boundary A-tail contributions shift A-sector mass unless neutral.

Zeta/kappa residuals must be killed, non-metric, compact-neutral, coefficient-zero,
or theorem-targeted.

J_V remains unresolved.

J_sub/J_exch remain role-level.

Curvature accounting remains diagnostic/accounting/branch-filter only.

H_curv/H_exch remain non-insertable.

Ordinary source routing remains constrained but not parent-derived.

Parent equation remains not ready.
```

This is a useful negative result. Group 21 did not solve mass neutrality, but it converted loose mass-neutrality language into concrete reduced witnesses, sector ledgers, rejected repair branches, and explicit theorem obligations.

---

## Scripts In This Group

```text
candidate_A_sector_mass_charge_definition.py
candidate_non_A_sector_mass_neutrality_inventory.py
candidate_residual_scalar_tail_flux_audit.py
candidate_boundary_flux_mass_preservation.py
candidate_zeta_kappa_mass_neutrality_conditions.py
candidate_JV_mass_neutrality_conditions.py
candidate_curvature_accounting_mass_neutrality.py
candidate_correction_tensor_mass_neutrality_guard.py
candidate_source_routing_no_double_counting.py
candidate_group_21_source_routing_status_summary.py
```

---

## Script-Level Results

### 1. A-Sector Mass Charge Definition

`candidate_A_sector_mass_charge_definition.py` defined the reduced ordinary-exterior reference charge:

\[
M_A=\frac{c^2}{8\pi G}F_A.
\]

For:

\[
A=1-\frac{2GM}{c^2r},
\]

the A-sector charge evaluates to:

\[
M_A=M.
\]

Status:

```text
CLOSED_REDUCED
```

Consequence:

```text
A-sector mass charge is the Group 21 reference coin.
All non-A sectors are audited against delta M_A = 0.
```

This does not define a final covariant parent mass.

---

### 2. Non-A Sector Mass-Neutrality Inventory

`candidate_non_A_sector_mass_neutrality_inventory.py` audited 18 non-A sectors for possible exterior mass leakage:

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
metric insertion / residual-kill,
dark-sector labels.
```

Status:

```text
SUMMARY
```

Consequence:

```text
No non-A sector is licensed as an independent ordinary exterior mass carrier.
Each sector remains diagnostic, non-metric, role-level, deferred,
non-insertable, risk-bearing, or theorem-targeted.
```

---

### 3. Residual Scalar Tail Flux Audit

`candidate_residual_scalar_tail_flux_audit.py` derived the basic reduced scalar-tail witness.

For:

\[
\phi_{\rm tail}(r)=\frac{C}{r},
\]

the surface flux is:

\[
F_\phi=4\pi r^2\phi_{\rm tail}'=-4\pi C.
\]

Status:

```text
CLOSED_REDUCED
```

Consequence:

```text
An ordinary residual 1/r scalar tail is not neutral unless C = 0,
or unless it is strictly non-metric/diagnostic,
or unless a future parent theorem routes it without double counting.
```

This became the reusable tail witness for zeta, kappa, J_V residue, curvature residue, H trace leakage, and boundary shell residue.

---

### 4. Boundary Flux Mass Preservation

`candidate_boundary_flux_mass_preservation.py` tested whether boundary or smoothing behavior can preserve A-sector mass without repair.

For a non-A boundary A-tail:

\[
\delta A_{\rm boundary}(r)=\frac{q}{r},
\]

the flux shift is:

\[
\delta F_A=-4\pi q,
\]

and the A-sector mass shift is:

\[
\delta M_A=-\frac{c^2q}{2G}.
\]

Status:

```text
THEOREM_TARGET
```

Consequence:

```text
Boundary mass preservation remains required but not derived.
No shell source, surface counterterm, recovery-tuned smoothing,
sharp-support patch, or boundary purse is licensed.
```

The script also showed that value continuity alone is not enough: a C1-style residual can carry boundary flux if its derivative is nonzero, while C2-style or smooth compact toy profiles can be flux-neutral as diagnostics.

---

### 5. Zeta/Kappa Mass-Neutrality Conditions

`candidate_zeta_kappa_mass_neutrality_conditions.py` applied the scalar-tail witness to the residual trace variables.

For:

\[
\zeta_{\rm tail}=\frac{C_\zeta}{r},
\]

\[
\kappa_{\rm tail}=\frac{C_\kappa}{r},
\]

the fluxes are:

\[
F_\zeta=-4\pi C_\zeta,
\]

\[
F_\kappa=-4\pi C_\kappa.
\]

Status:

```text
THEOREM_TARGET
```

Consequence:

```text
Exterior scalar silence requires C_zeta = 0 and C_kappa = 0,
unless residuals are killed, non-metric, compact-neutral, diagnostic,
or routed by a future parent theorem without double counting.
```

The script explicitly rejected:

```text
zeta/kappa cancellation by hand,
nonzero residual metric 1/r tails,
Box zeta / Box kappa ordinary scalar routes,
residual relaxation as A-flux repair,
recovery-chosen residual status.
```

The safest current convention remains:

```text
residual-kill / non-metric residual.
```

But that convention is still provisional, not a theorem.

---

### 6. J_V / J_sub / J_exch Mass-Neutrality Conditions

`candidate_JV_mass_neutrality_conditions.py` audited vacuum-current branches.

For a possible J_V scalar residue:

\[
\phi_{JV}=\frac{C_{JV}}{r},
\]

the scalar flux is:

\[
F_{\phi JV}=-4\pi C_{JV}.
\]

For a far-zone radial current:

\[
j^r=\frac{I}{4\pi r^2},
\]

the sphere flux is:

\[
\Phi=I.
\]

Status:

```text
UNRESOLVED / ROLE_LEVEL / THEOREM_TARGET
```

Consequence:

```text
J_V remains unresolved.
J_sub and J_exch remain role-level only.
Sigma/R zero-net exchange remains a theorem target, not a declaration.
Pure wind is not gravity.
Exchange is not repair.
```

The script rejected:

```text
undefined J_V mass current,
J_V scalar 1/r residue,
pure wind gravity,
exchange repair current,
Sigma/R tuning knob,
recovery-chosen u_vac.
```

---

### 7. Curvature Accounting Mass Neutrality

`candidate_curvature_accounting_mass_neutrality.py` protected curvature diagnostics from becoming hidden sources.

For a curvature scalar residue:

\[
\phi_{\rm curv}=\frac{C_{\rm curv}}{r},
\]

the scalar flux is:

\[
F_{\phi{\rm curv}}=-4\pi C_{\rm curv}.
\]

If curvature accounting were incorrectly allowed to induce an A-like tail:

\[
\delta A_e=\frac{q_e}{r},
\]

then:

\[
\delta M_A|_{e_{\rm curv}}=-\frac{c^2q_e}{2G}.
\]

For a far-zone curvature current:

\[
j_{\rm curv}^r=\frac{I_{\rm curv}}{4\pi r^2},
\]

the sphere flux is:

\[
\Phi_{J{\rm curv}}=I_{\rm curv}.
\]

Status:

```text
DIAGNOSTIC_ONLY / ACCOUNTING_ONLY / THEOREM_TARGET
```

Consequence:

```text
A_curv remains diagnostic / branch-filter.
e_curv remains accounting-only.
J_curv remains unresolved.
Curvature balance remains theorem-targeted.
Curvature accounting is not source energy.
```

The script rejected:

```text
e_curv as source reservoir,
curvature balance as mass repair,
J_curv gradient by fiat,
branch-kill called bounce,
H_curv curvature rescue,
recovery-chosen curvature route.
```

---

### 8. Correction Tensor Mass Neutrality Guard

`candidate_correction_tensor_mass_neutrality_guard.py` showed why \(H_{\rm curv}\) and \(H_{\rm exch}\) remain non-insertable.

For a generic H trace leakage:

\[
\phi_H=\frac{C_H}{r},
\]

the scalar flux is:

\[
F_{\phi H}=-4\pi C_H.
\]

For an H-induced A-tail:

\[
\delta A_H=\frac{q_H}{r},
\]

the mass shift is:

\[
\delta M_A|_H=-\frac{c^2q_H}{2G}.
\]

For far-zone H flux:

\[
j_H^r=\frac{I_H}{4\pi r^2},
\]

the sphere flux is:

\[
\Phi_H=I_H.
\]

Status:

```text
NOT_INSERTABLE
```

Consequence:

```text
H_curv and H_exch remain diagnostic-only audit labels.
No correction tensor is insertable.
```

Future H insertion would require:

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

The script rejected:

```text
H as M_ext correction,
H scalar tail cancellation,
H boundary counterterm,
H as Bianchi paint,
H source by divergence,
H dark-sector patch,
recovery-chosen H insertion.
```

---

### 9. Source Routing No Double Counting

`candidate_source_routing_no_double_counting.py` consolidated ordinary source-routing rules.

It protected:

```text
rho / M_enc -> A-sector mass charge.
```

It kept other routes constrained:

```text
longitudinal current -> continuity / density redistribution only if derived,
transverse current -> W_i without scalar mass duplication,
TT stress / quadrupole -> h_TT without scalar mass duplication,
pressure / trace -> diagnostic or non-metric kappa/zeta relaxation only if neutral,
ordinary scalar radiation -> rejected,
ordinary matter -> not rerouted into J_sub/J_exch/Sigma_exch/H_exch/H_curv.
```

The script recorded duplicate-source danger witnesses.

For a duplicate scalar tail:

\[
\phi_{\rm dup}=\frac{C_{\rm dup}}{r},
\]

\[
F_{\rm dup}=-4\pi C_{\rm dup}.
\]

For a duplicate A-tail:

\[
\delta A_{\rm dup}=\frac{q_{\rm dup}}{r},
\]

\[
\delta M_A|_{\rm dup}=-\frac{c^2q_{\rm dup}}{2G}.
\]

It also built an extra non-A source-load ledger and rejected cancellation as a substitute for sector-by-sector neutrality.

Status:

```text
PROTECTED / THEOREM_TARGET / DIAGNOSTIC_ONLY / ROLE_LEVEL
```

Consequence:

```text
Ordinary matter remains routed through protected channels.
Source routing remains constrained but not parent-derived.
Source cancellation ledgers do not count as no-double-counting.
```

---

### 10. Group Status Summary

`candidate_group_21_source_routing_status_summary.py` closed the group.

Status:

```text
SUMMARY
```

Consequence:

```text
A-sector mass charge is protected.
Non-A neutrality is sharpened but not solved.
Boundary neutrality and scalar silence remain theorem-targeted.
Parent equation remains not ready.
```

The recommended next group is:

```text
22_boundary_neutrality_and_scalar_silence
```

---

## Final Status Ledger

| Topic | Status | Result |
|---|---|---|
| A-sector mass charge | CLOSED_REDUCED | \(M_A=c^2F_A/(8\pi G)\), and \(M_A=M\) for the reduced exterior A-branch |
| Non-A mass inventory | SUMMARY | 18 non-A sectors audited; no second mass carrier licensed |
| Residual scalar tail | CLOSED_REDUCED | \(C/r\) tail carries \(F=-4\pi C\) |
| Boundary mass preservation | THEOREM_TARGET | \(q/r\) A-tail shifts \(\delta M_A=-c^2q/(2G)\); neutrality not derived |
| Zeta/kappa residuals | THEOREM_TARGET | \(C_\zeta=C_\kappa=0\), non-metric, killed, compact-neutral, or future theorem required |
| J_V | UNRESOLVED | no physical current definition or mass route |
| J_sub/J_exch | ROLE_LEVEL | pure wind is not gravity; exchange is not repair |
| Sigma/R | THEOREM_TARGET | zero-net language needs operators, signs, strengths, domains |
| A_curv/e_curv | DIAGNOSTIC_ONLY / ACCOUNTING_ONLY | curvature is not source energy |
| J_curv | UNRESOLVED | no curvature-current mass route |
| H_curv/H_exch | NOT_INSERTABLE | no correction tensor is insertable |
| Ordinary source routing | PROTECTED | \(\rho/M_{\rm enc}\) remains routed to A-sector |
| Source cancellation ledgers | REJECTED | cancellation is not no-double-counting |
| Parent equation | NOT_READY | Group 21 does not define a parent field equation |

---

## Rejected Branches

Rejected uses and regressions to preserve:

1. Second exterior mass spoon.
2. Nonzero residual \(1/r\) scalar tail.
3. Boundary shell source hidden by smoothing.
4. Surface counterterm preserving mass by name.
5. Recovery-tuned smoothing.
6. Sharp support hiding shell charge.
7. Zeta/kappa cancellation by hand.
8. Box zeta / Box kappa ordinary scalar source route.
9. Undefined J_V mass current.
10. J_sub gravitating by being pure wind.
11. J_exch repairing ordinary matter routing.
12. Sigma/R as tuning knobs.
13. Curvature admissibility as active source.
14. e_curv as source reservoir.
15. J_curv gradient by fiat.
16. Branch-kill called bounce.
17. H as M_ext correction.
18. H as scalar-tail cancellation.
19. H as boundary counterterm.
20. H as Bianchi paint.
21. H source by divergence.
22. Dark-sector mass patch.
23. Ordinary \(T_{\mu\nu}\) rerouted into exchange, curvature, H, or dark labels.
24. Source cancellation ledger standing in for sector neutrality.
25. O or source projectors enforcing neutrality without domain, kernel, image, and boundary law.
26. Recovery-selected non-A mass route.

---

## Safe Current Status

```text
A-sector mass charge remains protected.

A-flux defines the current reduced exterior mass charge.

No non-A sector carries ordinary exterior mass by declaration.

B_s/F_zeta insertion remains theorem target.

Residual-kill / non-metric residual remains provisional.

Residual 1/r scalar tails are mass-dangerous.

Boundary and exterior scalar neutrality remain obligations.

O remains unresolved.

J_V remains unresolved.

J_sub/J_exch remain role-level.

Sigma/R remain role-level / theorem-targeted.

A_curv remains diagnostic / branch-filter only.

e_curv remains diagnostic / accounting only.

J_curv remains undefined.

H_curv/H_exch remain non-insertable.

Ordinary matter stays routed to A-sector unless a theorem derives otherwise.

Pure wind is not gravity.

Exchange is not repair.

Dark sector is not patch.

Recovery remains downstream.

No scalar charge leakage.

No exterior mass shift from non-A sectors.
```

---

## Known Unknowns Preserved

Group 21 did not close these obligations:

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

## What Group 21 Established

Group 21 established a reduced mass-routing and no-double-counting discipline.

Established:

```text
A-sector mass charge is the current reduced ordinary-exterior reference.

Non-A sectors are audited against delta M_A = 0.

No non-A sector is currently licensed as an independent ordinary mass carrier.

Residual 1/r scalar tails carry nonzero flux.

Boundary 1/r A-tails shift A-sector mass.

Zeta/kappa residual tails must vanish, be killed, be non-metric, be compact-neutral, or remain theorem-targeted.

J_V remains unresolved.

J_sub/J_exch remain role-level.

Curvature accounting remains diagnostic/accounting.

H_curv/H_exch remain non-insertable.

Ordinary matter routing is protected from duplicate non-A source channels.

Parent equation remains not ready.
```

---

## What Group 21 Did Not Establish

Group 21 did not derive:

```text
final covariant mass definition,
full mass-neutrality theorem,
boundary neutrality,
exterior scalar silence,
ordinary matter decoupling,
B_s/F_zeta insertion,
residual-kill theorem,
O no-overlap,
J_V,
J_sub,
J_exch,
Sigma/R operators,
curvature dynamics,
J_curv,
H_curv,
H_exch,
source projector,
parent field equation.
```

---

## Handoff

The recommended next group is:

```text
22_boundary_neutrality_and_scalar_silence
```

Reason:

```text
Boundary mass preservation and exterior scalar silence are the most direct remaining theorem burdens.
```

Caution:

```text
Do not use smoothing, O, H, dark labels, shell sources, counterterms,
or recovery tuning as shortcuts.
```

Other possible directions remain candidates:

```text
22_metric_insertion_recovery_retest
22_role_specific_source_projectors
22_reduced_observational_audit
```

But the safest direct handoff is boundary neutrality and scalar silence.

---

## Final Interpretation

Group 21 protected the A-sector mass charge as the current reduced ordinary-exterior reference. It did not prove that every non-A sector is mass-neutral. Instead, it made the no-second-mass rule explicit: residual scalar tails, boundary A-tails, vacuum currents, curvature accounting, correction tensors, exchange roles, dark labels, and duplicate source ledgers cannot alter exterior mass by declaration.

The group’s useful result is therefore:

```text
Mass neutrality remains theorem-targeted,
but the A-sector remains the only licensed exterior mass-charge carrier.
All other sectors must stay diagnostic, non-metric, role-level, non-insertable,
or explicitly prove delta M_A = 0.
Parent equation remains not ready.
```

Tiny goblin final tag:

```text
One coin. No hidden pockets. No parent spell yet.
```
