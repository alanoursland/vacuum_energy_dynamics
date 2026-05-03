# Candidate Vacuum Configuration Energy Variable

## Canonical Filename

```text
candidate_vacuum_configuration_energy_variable.md
```

This document summarizes the output of:

```text
candidate_vacuum_configuration_energy_variable.py
```

---

## What This Document Is

This document is a development note for the `12_parent_identity_and_recombination/` group.

It is not a final definition of vacuum substance, not a parent identity, and not a completed energy-conservation theorem. It does not add a formal commitment to the theory.

Its purpose is to audit what \(E_{\rm vac,config}\) could be without turning it into a repair reservoir.

The guiding question was:

```text
What could E_vac_config be?
```

The answer is:

```text
E_vac_config should currently be treated as:
  a local vacuum-substance configuration energy density,
  possibly with q_v / J_v bookkeeping,
  excluding A-sector mass charge and Sigma_creation.

It must support:
  curvature excess depositing into vacuum substance,
  curvature deficit pulling from vacuum substance,
  ordinary closed-regime accounting,
  exterior mass preservation.
```

---

## Why This Study Matters

Parent identity template v2 now depends explicitly on:

\[
E_{\rm vac,config}.
\]

The relaxation-energy audit interpreted \(\Gamma_{\rm relax}\) as exchange:

```text
curvature excess deposits into vacuum-substance configuration,
curvature deficit pulls from vacuum-substance configuration,
and ordinary closed-regime total accounting is conserved.
```

But an undefined reservoir is dangerous.

If \(E_{\rm vac,config}\) can absorb any mismatch, it becomes a repair knob.

This study therefore asks:

```text
What can the vacuum configuration variable be,
and what is it forbidden to do?
```

---

## Compact Vacuum Variable Ledger

| Candidate | Role | Status | Risk | Missing |
|---|---|---|---|---|
| \(\epsilon_{\rm vac,config}(x)\) | local destination / source for \(\kappa\) relaxation imbalance | CANDIDATE | can become a repair reservoir if not tied to measurable / configurational variables | definition, units, measure, coupling to \(\kappa\) |
| \(q_v\) | ontology-native substance-density or configuration charge | STRUCTURAL | may duplicate \(A\)-sector mass density if not separated | physical meaning and relation to curvature / volume |
| \(J_v\) | flux of vacuum-substance configuration between regions | STRUCTURAL | could hide acausal transfer if support / speed is undefined | transport law and causal / constraint status |
| \(E_{\rm vac,config,global}\) | global constraint reservoir for non-propagating relaxation bookkeeping | RISK | looks unfalsifiable unless derived as a constraint | constraint origin and locality / observability rules |
| \(E_{\rm boundary,config}\) | energy associated with boundary smoothing or trace / volume matching near interfaces | CANDIDATE | boundary overclaim or mass tuning | boundary mass theorem, weights, \(\sigma\), observable map |
| \(E_{\min{\rm shift}}=E_{\rm vac,config}[\kappa_{\min}]\) | stores energy associated with shifting the local \(\kappa\) minimum | CANDIDATE | double-counting trace energy with matter stress | \(S_{\rm trace,effective}\), \(\chi_\kappa\), source accounting |
| \(E_A\) not included as relaxable vacuum reservoir | protects exterior mass flux from relaxation bookkeeping | CONSTRAINED | relaxation tunes measured mass | parent separation of \(A\) flux and vacuum configuration energy |
| \(\Sigma_{\rm creation}\) not part of \(E_{\rm vac,config}\) exchange | protects ordinary closure | CONSTRAINED | active-regime leakage | active-regime trigger / exclusion law |
| \(E_{\rm recombination,accounting}\) | ensures scalar response is counted once when geometry is assembled | UNRESOLVED | energy / scalar double-counting in metric map | \(P_{\rm recombination}\) and source accounting |
| \(E_{\rm action,stiffness}\) | could derive \(K_\kappa,C_T,K_T,\alpha_W/K_c\) from a shared stiffness principle | MISSING | coefficient repair knob | action / stiffness principle |

---

## Status Counts

The run counted:

```text
CANDIDATE:    3
CONSTRAINED:  2
MISSING:      1
RISK:         1
STRUCTURAL:   2
UNRESOLVED:   1
```

Interpretation:

```text
Several candidates are plausible, but none are derived.
The safest immediate interpretation is local vacuum configuration energy plus
q_v / J_v bookkeeping, while excluding A-sector mass and Sigma_creation.
```

---

## Candidate Minimal Accounting

Minimal candidate accounting:

\[
e_\kappa
=
\frac12K_\kappa(\kappa-\kappa_{\min})^2.
\]

Local relaxation:

\[
u^\mu\nabla_\mu e_\kappa\le0.
\]

Vacuum-substance exchange:

\[
u^\mu\nabla_\mu\epsilon_{\rm vac,config}
=
-u^\mu\nabla_\mu e_\kappa.
\]

Ordinary closed regime:

\[
\Sigma_{\rm creation}=0.
\]

\[
\delta M_{\rm ext}=0.
\]

No scalar radiation:

\[
A_{\rm rad}=0.
\]

No breathing wave:

\[
\Box\kappa
\]

is rejected as an ordinary scalar-radiation equation.

Interpretation:

```text
curvature excess deposits into vacuum-substance configuration,
curvature deficit pulls from vacuum-substance configuration,
total local accounting closes.
```

Status:

```text
CANDIDATE BOOKKEEPING / NOT DERIVED
```

---

## No-Repair-Reservoir Tests

\(E_{\rm vac,config}\) fails if:

1. It is invoked only after contradictions appear.
2. It can absorb arbitrary energy without a state variable.
3. It changes exterior \(M_{\rm ext}\).
4. It acts like \(\Sigma_{\rm creation}\) in ordinary regime.
5. It duplicates \(A\)-sector mass energy.
6. It tunes \(\kappa\), vector, or tensor coefficients.
7. It allows acausal nonlocal vacuum transport without being declared a constraint.
8. It makes near-boundary predictions before recombination / observables are derived.

---

## Best Current Minimal Interpretation

Best current minimal interpretation:

```text
epsilon_vac_config:
  local vacuum-substance configuration energy density

q_v, J_v:
  optional ontology-native density / current bookkeeping variables

E_boundary_config:
  possible interface contribution, diagnostic only
```

Excluded from this variable:

```text
A-sector exterior mass charge,
Sigma_creation in ordinary regime,
coefficient tuning reservoir.
```

Status:

```text
STRUCTURAL / NOT DERIVED
```

---

## Vacuum-Substance Exchange Reading

The useful ontology-native statement is:

```text
curvature relaxation goes into vacuum substance;
curvature deficit pulls from vacuum substance to reduce the deficit.
```

More precisely:

```text
curvature excess:
  deposits into epsilon_vac_config.

curvature deficit:
  draws from epsilon_vac_config.

ordinary relaxation:
  transfers imbalance between e_kappa and epsilon_vac_config.

ordinary closed regime:
  total accounting closes and Sigma_creation remains zero.
```

This avoids:

```text
energy deletion,
hidden creation,
scalar radiation,
and exterior mass tuning.
```

---

## What This Study Established

This study established that \(E_{\rm vac,config}\) should currently be treated as:

```text
a local vacuum-substance configuration energy density,
possibly with q_v / J_v bookkeeping,
excluding A-sector mass charge and Sigma_creation.
```

It must support:

```text
curvature excess depositing into vacuum substance,
curvature deficit pulling from vacuum substance,
ordinary closed-regime accounting,
exterior mass preservation.
```

It also established strong restrictions:

```text
E_vac_config cannot tune coefficients,
cannot absorb arbitrary contradictions,
cannot change exterior mass,
cannot act as Sigma_creation,
cannot duplicate A-sector scalar mass response.
```

---

## What This Study Did Not Establish

This study did not define \(E_{\rm vac,config}\).

It did not define \(q_v\) or \(J_v\).

It did not derive the transport law.

It did not derive the volume measure.

It did not derive \(K_\kappa\).

It did not derive recombination accounting.

It did not derive coefficient stiffness.

It only narrowed the safe interpretation of the variable.

---

## Current Best Interpretation

\(E_{\rm vac,config}\) is currently best treated as:

```text
local vacuum-substance configuration energy density.
```

It may be accompanied by:

```text
q_v:
  vacuum-substance configuration charge / density proxy

J_v:
  vacuum-substance configuration transport current
```

But these remain structural.

They are not yet derived.

---

## Next Development Target

The output recommended:

```text
parent_identity_and_recombination_summary.md
```

Reason:

```text
Group 12 has reached a natural summary point after exclusions, implications,
projectors, scalar / kappa / boundary / recombination / accounting, and
E_vac_config.
```

---

## Summary

The vacuum configuration variable should not be a magic reservoir.

It is allowed only as a constrained vacuum-substance configuration energy variable that supports:

```text
curvature excess -> vacuum substance,
vacuum substance -> curvature deficit,
closed ordinary accounting,
exterior mass preservation.
```

The next step is to summarize group 12.
