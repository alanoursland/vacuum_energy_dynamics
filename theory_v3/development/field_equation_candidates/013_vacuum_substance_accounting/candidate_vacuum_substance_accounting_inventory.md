# Candidate Vacuum Substance Accounting Inventory

## Canonical Filename

```text
candidate_vacuum_substance_accounting_inventory.md
```

This document summarizes the output of:

```text
candidate_vacuum_substance_accounting_inventory.py
```

---

## What This Document Is

This document is a development note for the `13_vacuum_substance_accounting/` group.

It is not a derivation of \(E_{\rm vac,config}\), not a parent identity, and not a final vacuum-substance theory. It does not add a formal commitment to the theory.

Its purpose is to inventory the variables and balances needed to make \(E_{\rm vac,config}\), \(q_v\), and \(J_v\) more than repair-reservoir language.

The guiding question was:

```text
What variables and balances are needed to make E_vac_config / q_v / J_v
more than a repair reservoir?
```

The answer is:

```text
E_vac_config must be geometric or tightly constrained bookkeeping.
The best immediate geometric targets are sqrt_gamma and ln_sqrt_gamma.
q_v / J_v remain optional bookkeeping until tied to geometry.
M_ext and A_flux are protected A-sector quantities.
Sigma_creation is excluded from ordinary closed accounting.
Gamma_relax is exchange / restoration, not destruction.
```

---

## Corrected Ontology

The inventory starts from:

```text
vacuum is spacetime.
creating vacuum creates spacetime.
changing local spacetime creates curvature.
```

Therefore:

```text
vacuum-substance accounting must be geometric accounting,
or explicitly constrained bookkeeping tied to geometry.
```

The discipline is:

```text
name the geometry,
no bottomless bucket,
no duplicate A-sector mass,
no hidden Sigma_creation,
no coefficient tuning reservoir.
```

---

## Compact Accounting Ledger

| Variable | Kind | Status | Forbidden Role | Missing | Next Test |
|---|---|---|---|---|---|
| \(\epsilon_{\rm vac,config}\) | geometric / spacetime-configuration candidate | CANDIDATE | bottomless reservoir, coefficient tuning knob, or \(A\)-sector mass charge | geometric definition, units, measure, relation to \(\sqrt{\gamma}\) or \(\kappa\) | `candidate_volume_form_configuration_variable.py` |
| \(E_{\rm vac,config}\) | integrated configuration functional | CANDIDATE | global repair bucket invoked only after contradictions appear | integration measure, support, boundary terms, locality / constraint status | `candidate_vacuum_transport_current_constraints.py` |
| \(q_v\) | bookkeeping / ontology-native density proxy | STRUCTURAL | duplicate of matter density \(\rho\) or exterior mass source | physical / geometric meaning and relation to volume form | `candidate_volume_form_configuration_variable.py` |
| \(J_v\) | bookkeeping / transport or constraint current | STRUCTURAL | acausal repair current or hidden radiation channel | transport law, causal speed or constraint status, boundary behavior | `candidate_vacuum_transport_current_constraints.py` |
| \(\sqrt{\gamma}\) | geometric volume-form candidate | CANDIDATE | unqualified observable before slicing / frame is specified | choice of spatial metric / slicing and relation to \(\kappa\) | `candidate_volume_form_configuration_variable.py` |
| \(\ln\sqrt{\gamma}\) | geometric trace / volume strain candidate | CANDIDATE | duplicating \(A\)-sector scalar mass response | background / reference volume and recombination role | `candidate_trace_vs_tt_geometric_split.py` |
| \(\kappa\) | trace / volume mismatch variable | STRUCTURAL | ordinary scalar radiation, \(\Box\kappa\), or \(\rho\)-sourced exterior scalar charge | covariant origin, \(u^\mu\), source law, relation to volume form | `candidate_scalar_conversion_not_damping.py` |
| \(\kappa_{\min}\) | local equilibrium / target configuration | STRUCTURAL | coordinate pressure knob or scalar wave source | \(S_{\rm trace,effective}\) and \(\chi_\kappa\) | `candidate_trace_vs_tt_geometric_split.py` |
| \(e_\kappa\) | local free-energy candidate | CANDIDATE | independent kinetic / momentum reservoir for scalar waves | \(K_\kappa\) derivation, volume measure, relation to geometry | `candidate_scalar_conversion_not_damping.py` |
| \(\Gamma_{\rm relax}\) | exchange / restoration term | CONSTRAINED | energy destruction, \(\Sigma_{\rm creation}\), or damping without destination | parent balance expression and sign convention | `candidate_vacuum_accounting_parent_balance.py` |
| \(\Sigma_{\rm exchange}\) | matter / vacuum exchange source candidate | UNRESOLVED | free source knob or duplicate of existing sector sources | covariant tensor expression for coupling | `candidate_mass_acceleration_gradient_coupling.py` |
| \(\Sigma_{\rm creation}\) | active-regime source | CONSTRAINED | ordinary closed-regime relaxation or hidden nonconservation | active-regime trigger / exclusion law | `candidate_vacuum_accounting_parent_balance.py` |
| \(M_{\rm ext}\) | \(A\)-sector exterior charge | DERIVED_REDUCED | changed by \(\kappa\) relaxation, boundary smoothing, or \(E_{\rm vac,config}\) | parent flux-charge theorem | `candidate_boundary_volume_mode_no_exterior_charge.py` |
| \(A_{\rm flux}\) | scalar constraint / exterior charge functional | DERIVED_REDUCED | adjusted by trace relaxation or vacuum accounting | parent scalar constraint propagation for moving sources | `candidate_boundary_volume_mode_no_exterior_charge.py` |
| \(P_{\rm trace}\) | projector | STRUCTURAL | source of \(h_{TT}\), \(A_{\rm rad}\), \(\Box\kappa\), or exterior \(\kappa\) charge | parent projector definition | `candidate_trace_vs_tt_geometric_split.py` |
| \(P_{TT}\) | projector | STRUCTURAL | trace / volume creation channel | parent TT source identity and coefficient \(C_T\) | `candidate_trace_vs_tt_geometric_split.py` |
| \(P_{\rm boundary}\) | projector / interface condition | CONSTRAINED | boundary mass tuning or exterior scalar tail | boundary mass theorem | `candidate_boundary_volume_mode_no_exterior_charge.py` |
| \(P_{\rm recombination}\) | projector / assembly map | UNRESOLVED | GR metric copy or \(A/\kappa\) duplicate mass response | covariant or reduced recombination identity | `candidate_vacuum_accounting_parent_balance.py` |

---

## Status Counts

The run counted:

```text
CANDIDATE:       5
CONSTRAINED:     3
DERIVED_REDUCED: 2
STRUCTURAL:      6
UNRESOLVED:      2
```

Interpretation:

```text
The accounting inventory is mostly structural / candidate.
The only reduced-derived pieces are the A-sector exterior mass / flux quantities.
The central missing definition is the geometric meaning of epsilon_vac_config.
```

---

## Geometric Versus Bookkeeping Variables

Geometric candidates:

```text
epsilon_vac_config,
sqrt_gamma,
ln_sqrt_gamma,
kappa,
kappa_min.
```

Bookkeeping candidates:

```text
q_v,
J_v,
E_vac_config,
Gamma_relax,
Sigma_exchange.
```

Protected / excluded from the vacuum reservoir:

```text
M_ext,
A_flux,
Sigma_creation in ordinary regime.
```

Interpretation:

```text
prefer geometric definitions first.
Bookkeeping variables are allowed only if tied to geometry or explicitly constrained.
```

---

## No-Repair-Reservoir Tests

A vacuum-substance accounting variable fails if:

1. It absorbs arbitrary contradictions.
2. It changes \(M_{\rm ext}\).
3. It duplicates \(\rho\) or \(A_{\rm flux}\).
4. It acts as \(\Sigma_{\rm creation}\) in ordinary gravity.
5. It hides acausal \(J_v\) transport.
6. It tunes \(\alpha_W/K_c,\beta_W,C_T,\) or \(K_T\).
7. It converts scalar waves into far-zone scalar radiation.
8. It makes near-boundary predictions before observables are derived.

---

## Scalar / Trace Conversion Picture

Working picture:

```text
scalar / trace disturbance is not an ordinary damped wave,
scalar / trace disturbance converts into vacuum-spacetime configuration,
curvature excess deposits into vacuum configuration,
curvature deficit pulls from vacuum configuration,
TT shear is volume-preserving and may propagate.
```

Key mathematical target:

```text
identify the geometric variable whose change represents vacuum / spacetime creation.
```

Likely first candidate:

```text
ln_sqrt_gamma = log spatial volume element.
```

This is a target, not a derivation.

---

## What This Study Established

This study established that \(E_{\rm vac,config}\) must be either:

```text
geometric,
```

or:

```text
tightly constrained bookkeeping tied to geometry.
```

It identified the best immediate geometric targets as:

\[
\sqrt{\gamma},
\]

and:

\[
\ln\sqrt{\gamma}.
\]

It also protected:

```text
M_ext,
A_flux,
Sigma_creation in ordinary gravity.
```

from being absorbed into vacuum-substance accounting.

---

## What This Study Did Not Establish

This study did not define \(E_{\rm vac,config}\).

It did not define \(\epsilon_{\rm vac,config}\).

It did not derive \(q_v\) or \(J_v\).

It did not derive a transport law.

It did not prove that \(\ln\sqrt{\gamma}\) is the correct variable.

It did not derive the trace / TT split.

It only inventoried the candidate variables and constraints.

---

## Current Best Interpretation

The accounting inventory says:

```text
E_vac_config must be geometric or tightly constrained bookkeeping.
The best immediate geometric targets are sqrt_gamma and ln_sqrt_gamma.
q_v / J_v remain optional bookkeeping until tied to geometry.
M_ext and A_flux are protected A-sector quantities.
Sigma_creation is excluded from ordinary closed accounting.
Gamma_relax is exchange / restoration, not destruction.
```

---

## Next Development Target

The next script should be:

```text
candidate_volume_form_configuration_variable.py
```

Purpose:

```text
Test whether vacuum configuration is represented by volume form / ln sqrt gamma.
```

Reason:

```text
The inventory shows the central missing definition is geometric:
what is epsilon_vac_config?
```

Expected result:

```text
A volume-form candidate ledger:
  sqrt_gamma as physical volume element,
  ln_sqrt_gamma as volume strain,
  relation to kappa,
  relation to TT trace-free modes,
  protected A-sector mass,
  slicing/frame caveat,
  failure modes if volume-form duplicates scalar mass response.
```

---

## Summary

Group 13 starts with a variable audit.

The next goblin gate is:

```text
Can vacuum-spacetime configuration be identified with a volume-form variable?
```
