# Candidate Closure Minimal Equation Set

## Canonical Filename

```text
candidate_closure_minimal_equation_set.md
```

This document summarizes the output of:

```text
candidate_closure_minimal_equation_set.py
```

---

## What This Document Is

This document is a development note for the `11_field_equation_closure/` group.

It is not a final field-equation system, not a covariant parent theory, and not a proof of closure. It does not add a formal commitment to the theory.

Its purpose is to state the smallest honest current field-equation set, with labels and caveats.

The guiding question was:

```text
What is the smallest honest current field-equation set?
```

The answer is:

```text
The current minimal equation set is coherent enough to state.

It is not closed.

Strongest result:
  reduced Schwarzschild exterior from A-sector

Main missing result:
  parent conservation / recombination identity
```

---

## Minimal Equation Inventory

| Equation | Role | Status | Missing |
|---|---|---|---|
| E1: \(A\)-sector scalar constraint | scalar monopole / mass flux constraint | DERIVED_REDUCED | full nonlinear nonspherical parent equation |
| E2: exterior \(A\) solution | static spherical exterior scalar factor | DERIVED_REDUCED | general exterior / nonspherical nonlinear form |
| E3: \(B/\kappa\) areal relation | radial reciprocal companion / \(\kappa\) diagnostic | DERIVED_REDUCED | covariant gauge / physical split |
| E4: weak scalar multipole limit | weak scalar / Newtonian limit | DERIVED_REDUCED | full nonlinear nonspherical closure |
| E5: vector current response | transverse vector / frame-dragging shape | STRUCTURAL | \(\alpha_W/K_c,\;\beta_W,\) normalization |
| E6: tensor radiation equation | ordinary long-range gravitational radiation | STRUCTURAL | \(C_T\), TT source identity, tensor action stiffness |
| E7: tensor radiation energy flux | tensor radiation energy accounting | MATCHED | \(K_T\) from vacuum action / stiffness |
| E8: \(\kappa\) non-inertial relaxation | trace / vacuum-volume relaxation | STRUCTURAL | \(K_\kappa,\mu_\kappa,\chi_\kappa,S_{\rm trace,effective}\), covariant origin |
| E9: exterior \(\kappa\) safety | no exterior scalar / \(\kappa\) charge | CONSTRAINED | boundary / interface theorem |
| E10: scalar radiation rejection | TT-only ordinary radiation safety | REJECTED | parent mechanism proving exclusion |
| E11: ordinary closed regime | ordinary conservative closure | CONSTRAINED | active-regime trigger / exclusion law |
| E12: parent closure target | candidate parent identity target | MISSING | \(E_{\rm parent},B_{\rm closed},B_{\rm relax}\) definitions and proof |

---

## Status Counts

The run counted:

```text
CONSTRAINED:      2
DERIVED_REDUCED:  4
MATCHED:          1
MISSING:          1
REJECTED:         1
STRUCTURAL:       3
```

Interpretation:

```text
The minimal set has strong reduced scalar equations,
structural vector / tensor / kappa rules,
constrained scalar-radiation safety,
one matched tensor energy coefficient,
and missing parent closure.
```

---

## Minimal Current Reduced System

The minimal current reduced system is:

\[
\Delta_{\rm areal}A
=
\frac{8\pi G}{c^2}\rho.
\]

\[
A_{\rm ext}
=
1-\frac{2GM}{c^2r}.
\]

\[
AB=e^{2\kappa},
\qquad
\kappa_{\rm ext}=0
\Rightarrow
B=\frac{1}{A}.
\]

\[
\nabla\times\nabla\times W
=
-\frac{\alpha_W}{2K_c}j_T.
\]

\[
\Box h_{ij}^{TT}
=
-C_T S_{ij}^{TT}.
\]

\[
\dot{\kappa}
=
-\mu_\kappa K_\kappa(\kappa-\kappa_{\min}).
\]

\[
\kappa_{\min}
=
\chi_\kappa S_{\rm trace,effective}.
\]

\[
{\rm source}(A_{\rm rad}\ {\rm ordinary\ massless})=0.
\]

\[
\Sigma_{\rm creation}=0
\]

in the ordinary closed regime.

Parent closure target:

\[
{\rm Div}\,
E_{\rm parent}[A,W,h_{TT},\kappa]
=
B_{\rm closed}[T]
+
B_{\rm relax}[\Gamma_{\rm relax}].
\]

Status:

```text
CONSTRAINED / MISSING
```

The parent target is a template, not closure.

---

## E1: A-Sector Scalar Constraint

Equation:

\[
\Delta_{\rm areal}A
=
\frac{8\pi G}{c^2}\rho.
\]

Role:

```text
scalar monopole / mass flux constraint
```

Source:

```text
rho, M_enc
```

Status:

```text
DERIVED_REDUCED
```

Caveat:

```text
valid strongest in static spherical / reduced scalar sector.
```

Missing:

```text
full nonlinear nonspherical parent equation.
```

---

## E2: Exterior A Solution

Equation:

\[
A(r)
=
1-\frac{2GM}{c^2r}.
\]

Role:

```text
static spherical exterior scalar factor
```

Status:

```text
DERIVED_REDUCED
```

Caveat:

```text
main real reconstruction result.
```

Missing:

```text
general exterior / nonspherical nonlinear form.
```

---

## E3: B/Kappa Areal Relation

Equation:

\[
AB=e^{2\kappa}.
\]

Exterior target:

\[
\kappa=0.
\]

Therefore:

\[
B=\frac{1}{A}.
\]

Role:

```text
radial reciprocal companion / kappa diagnostic
```

Status:

```text
DERIVED_REDUCED
```

Caveat:

```text
reduced areal-gauge relation, not full parent metric.
```

Missing:

```text
covariant gauge / physical split.
```

---

## E4: Weak Scalar Multipole Limit

Equation:

\[
A\simeq1+\frac{2\Phi}{c^2}.
\]

\[
\nabla^2\Phi=4\pi G\rho.
\]

Role:

```text
weak scalar / Newtonian limit
```

Status:

```text
DERIVED_REDUCED
```

Caveat:

```text
supports weak multipoles and reduced gamma=1, not full PPN audit.
```

Missing:

```text
full nonlinear nonspherical closure.
```

---

## E5: Vector Current Response

Equation:

\[
\nabla\times\nabla\times W
=
-\frac{\alpha_W}{2K_c}j_T.
\]

Gauge / projection condition:

\[
\nabla\cdot W=0.
\]

Source:

\[
j_T=P_T(\rho v).
\]

Role:

```text
transverse vector / frame-dragging shape
```

Status:

```text
STRUCTURAL
```

Caveat:

```text
far-field shape / J dependence supported; coefficient not derived.
```

Missing:

```text
alpha_W/K_c,
beta_W,
normalization.
```

---

## E6: Tensor Radiation Equation

Equation:

\[
\Box h_{ij}^{TT}
=
-C_T S_{ij}^{TT}.
\]

Role:

```text
ordinary long-range gravitational radiation
```

Source:

```text
TT stress / quadrupole source
```

Status:

```text
STRUCTURAL
```

Caveat:

```text
TT role structural; coupling coefficient not derived.
```

Missing:

```text
C_T,
TT source identity,
tensor action stiffness.
```

---

## E7: Tensor Radiation Energy Flux

Equation:

\[
F_T
\sim
K_T
\left\langle
\dot h_{ij}^{TT}
\dot h_{ij}^{TT}
\right\rangle.
\]

Role:

```text
tensor radiation energy accounting
```

Status:

```text
MATCHED
```

Caveat:

```text
absolute GR flux coefficient not derived.
```

Missing:

```text
K_T from vacuum action / stiffness.
```

---

## E8: Kappa Non-Inertial Relaxation

Equation:

\[
\dot{\kappa}
=
-\mu_\kappa K_\kappa(\kappa-\kappa_{\min}).
\]

Minimum shift:

\[
\kappa_{\min}
=
\chi_\kappa S_{\rm trace,effective}.
\]

Role:

```text
trace / vacuum-volume relaxation
```

Status:

```text
STRUCTURAL
```

Caveat:

```text
not a wave equation;
no independent momentum channel.
```

Missing:

```text
K_kappa,
mu_kappa,
chi_kappa,
S_trace_effective,
covariant origin.
```

---

## E9: Exterior Kappa Safety

Equation / condition:

\[
\kappa\to0,
\qquad
\kappa_{\min}\to0,
\qquad
F_\kappa(R+)=0.
\]

Role:

```text
no exterior scalar / kappa charge
```

Status:

```text
CONSTRAINED
```

Caveat:

```text
required to avoid scalar tail and mass tuning.
```

Missing:

```text
boundary / interface theorem.
```

---

## E10: Scalar Radiation Rejection

Rule:

\[
{\rm source}(A_{\rm rad}\ {\rm ordinary\ massless})=0.
\]

Also rejected:

\[
\Box\kappa
\]

as an ordinary scalar wave equation.

Role:

```text
TT-only ordinary radiation safety
```

Status:

```text
REJECTED
```

Caveat:

```text
constraint, not yet derivation.
```

Missing:

```text
parent mechanism proving exclusion.
```

---

## E11: Ordinary Closed Regime

Equation:

\[
\Sigma_{\rm creation}=0.
\]

Role:

```text
ordinary conservative closure
```

Status:

```text
CONSTRAINED
```

Caveat:

```text
creation / exchange regimes are not part of ordinary gravity closure by default.
```

Missing:

```text
active-regime trigger / exclusion law.
```

---

## E12: Parent Closure Target

Template:

\[
{\rm Div}\,
E_{\rm parent}[A,W,h_{TT},\kappa]
=
B_{\rm closed}[T]
+
B_{\rm relax}[\Gamma_{\rm relax}].
\]

Role:

```text
candidate parent identity target
```

Status:

```text
MISSING
```

Caveat:

```text
template only;
not closure.
```

Missing:

```text
E_parent,
B_closed,
B_relax,
definitions and proof.
```

---

## GR Recovery Status

Recovered strongly / reduced:

```text
static spherical exterior A,
B=1/A once exterior kappa=0,
weak scalar / Newtonian limit.
```

Supported structurally:

```text
vector frame-dragging shape,
TT tensor radiation sector,
kappa non-radiative trace relaxation.
```

Matched or missing:

```text
vector normalization,
tensor coupling,
tensor energy flux coefficient,
parent conservation identity,
covariant recombination.
```

---

## Failure Controls

This minimal set fails if:

1. Parent closure target is advertised as derived.
2. Tensor / vector coefficients are advertised as derived.
3. \(\kappa\) becomes a second scalar gravity field.
4. Boundary smoothing changes exterior \(M\).
5. \(A_{\rm rad}\) or \(\Box\kappa\) scalar radiation appears.
6. \(\Sigma_{\rm creation}\) enters ordinary closed regime.
7. Recombination silently copies GR.

---

## What This Study Established

This study established that the current minimal field-equation set is coherent enough to state.

It also established that the set is not closed.

The strongest result is:

```text
reduced Schwarzschild exterior from A-sector.
```

The main missing result is:

```text
parent conservation / recombination identity.
```

---

## What This Study Did Not Establish

This study did not derive the parent identity.

It did not derive covariant recombination.

It did not derive vector normalization.

It did not derive tensor coupling.

It did not derive tensor flux coefficient.

It did not derive \(\kappa\)'s covariant source law.

It did not prove full GR recovery.

It only assembled the minimal current equation set.

---

## Current Best Interpretation

The current minimal equation set is coherent enough to state.

It is not closed.

Strongest result:

```text
reduced Schwarzschild exterior from A-sector.
```

Main missing result:

```text
parent conservation / recombination identity.
```

---

## Next Development Target

The output recommended:

```text
field_equation_closure_summary.md
```

Reason:

```text
Group 11 has reached a natural summary point after inventory, recombination,
sources, constraints, evolution split, GR audit, parent scaffold, failure modes,
and minimal equation set.
```

---

## Summary

The current minimal equation set is a useful field-equation status statement.

It is not a final theory.

The next document should summarize group 11.
