# Candidate Source Coupling From Vacuum Exchange

## What This Document Is

This document is a development note for the `09_vacuum_identity_and_source_coupling/` group.

It is not a covariant source law, not a final stress-energy coupling, and not a derivation of all sector coefficients. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_source_coupling_from_vacuum_exchange.py
```

The guiding question was:

```text
Can the sector sources be interpreted as projections of one vacuum-exchange
balance law?
```

The candidate balance law is:

```text
partial_t q_v + div J_v = Sigma_exchange + Sigma_creation - Gamma_relax
```

or:

\[
\partial_t q_v+\nabla\cdot J_v
=
\Sigma_{\rm exchange}
+
\Sigma_{\rm creation}
-
\Gamma_{\rm relax}.
\]

The answer is:

```text
The vacuum-exchange picture begins to constrain source coupling, but major
pieces remain underived.
```

The most important classification is:

```text
density    -> A_constraint
current    -> W_i
relaxation -> A_rad suppression

missing:
  kappa source

hand-assigned:
  tensor coupling coefficient
```

---

## Method Note

This script used these status categories:

```text
DERIVED_REDUCED
CONSTRAINED_BY_IDENTITY
HAND_ASSIGNED
MISSING
RISK
```

The status counts were:

```text
DERIVED_REDUCED: 1
CONSTRAINED_BY_IDENTITY: 2
HAND_ASSIGNED: 1
MISSING: 1
RISK: 1
```

This is the right shape for group 09.

It does not pretend that the ontology has derived everything.

It asks where the ontology is doing work and where matching remains.

---

## Source Coupling Problem

The current sector sources are:

```text
A_constraint <- mass density / enclosed mass
W_i          <- mass current / angular momentum
kappa        <- pressure / stress / trace candidate
h_ij^TT      <- time-varying trace-free quadrupole derivatives
A_rad        <- scalar breathing perturbation / relaxation target
```

The group-09 goal is to reduce hand assignment.

The question is whether these sources can be seen as different projections of:

```text
Sigma_exchange,
J_v,
Gamma_relax,
Sigma_creation.
```

---

## A_constraint Scalar Source

Status:

```text
DERIVED_REDUCED
```

Source object:

```text
mass density rho / enclosed mass M
```

Exchange projection:

```text
scalar part of Sigma_exchange
```

Current support:

```text
Areal flux law gives Delta_areal A = 8*pi*G*rho/c^2 and recovers static
exterior A = 1 - 2GM/(c^2 r).
```

Missing piece:

```text
Derive the 8*pi*G/c^2 coefficient from vacuum exchange ontology, not just
reduced flux normalization.
```

This is currently the strongest source-coupling result.

The scalar mass source is not arbitrary at the reduced level.

But the deeper coefficient still needs an ontology-native derivation.

---

## W_i Vector / Current Source

Status:

```text
CONSTRAINED_BY_IDENTITY
```

Source object:

```text
mass current j_i = rho v_i / angular momentum
```

Exchange projection:

```text
vector/current part of vacuum transport J_v
```

Current support:

```text
Continuity bookkeeping points from density to current, suggesting W_i should
couple to transport rather than be assigned only by analogy.
```

Missing piece:

```text
Derive W_i field equation, coefficient, gauge behavior, and frame-dragging
observable.
```

This is the most promising next sector because the continuity identity naturally introduces current.

The ontology does not yet produce the \(W_i\) equation, but it does constrain the kind of source \(W_i\) should have.

---

## Kappa Trace / Interior Source

Status:

```text
MISSING
```

Source object:

```text
pressure, stress trace, volume exchange candidate
```

Exchange projection:

```text
trace/compressive part of exchange or relaxation
```

Current support:

```text
Kappa is interpreted as trace/interior response, but no source identity exists.
```

Missing piece:

```text
Derive whether kappa couples to pressure, stress trace, density gradients,
relaxation, or creation-like terms.
```

This remains a major weakness.

The \(\kappa\) sector still risks being a placeholder unless it is forced into one primary role.

---

## h_ij^TT Tensor Source

Status:

```text
HAND_ASSIGNED
```

Source object:

```text
time-varying trace-free quadrupole derivatives
```

Exchange projection:

```text
trace-free shear/tensor part of conserved source motion
```

Current support:

```text
Tensor studies established TT basis, quadrupole projection, and target scaling.
```

Missing piece:

```text
Derive quadrupole coupling and 2G/c^4 normalization from the exchange identity
or a parent action.
```

This is an important honesty marker.

The tensor sector is structurally strong, but the coupling coefficient remains matched rather than derived.

---

## A_rad Scalar Radiative Hazard

Status:

```text
CONSTRAINED_BY_IDENTITY
```

Source object:

```text
scalar breathing perturbation
```

Exchange projection:

```text
relaxation/deviation term Gamma_relax
```

Current support:

```text
Relaxation term can represent vacuum absorption of scalar radiative
perturbations.
```

Missing piece:

```text
Show relaxation suppresses A_rad without erasing A_constraint or violating
energy balance.
```

This preserves the vacuum-absorption idea as a mechanism candidate.

But it is still not a proof.

---

## Creation Regime

Status:

```text
RISK
```

Source object:

```text
Sigma_creation
```

Exchange projection:

```text
nonconservative vacuum amount change
```

Current support:

```text
Creation is classified as special-regime behavior, not ordinary exterior gravity.
```

Missing piece:

```text
Define when creation is allowed and prevent it from becoming a free knob.
```

This is an important guardrail.

Creation cannot be used to patch mismatches whenever the equations fail.

---

## Coupling Status Table

The script produced this table:

| Sector | Source object | Status |
|---|---|---|
| \(A_{\rm constraint}\) scalar source | mass density \(\rho\) / enclosed mass \(M\) | DERIVED_REDUCED |
| \(W_i\) vector/current source | mass current \(j_i=\rho v_i\) / angular momentum | CONSTRAINED_BY_IDENTITY |
| \(\kappa\) trace/interior source | pressure, stress trace, volume exchange candidate | MISSING |
| \(h_{ij}^{TT}\) tensor source | time-varying trace-free quadrupole derivatives | HAND_ASSIGNED |
| \(A_{\rm rad}\) scalar radiative hazard | scalar breathing perturbation | CONSTRAINED_BY_IDENTITY |
| creation regime | \(\Sigma_{\rm creation}\) | RISK |

This table is the main output.

---

## Ontology Work Versus GR Matching

The script explicitly drew the line.

Ontology is doing work when:

```text
density naturally sources scalar exchange,
current naturally sources vector transport,
relaxation naturally suppresses radiative scalar deviations.
```

Ontology is not yet doing enough work when:

```text
tensor coefficient is set to 2G/c^4 by target matching,
W_i coefficient is chosen to match frame dragging,
kappa source is left as pressure/stress/trace placeholder,
creation is invoked to solve mismatches.
```

This is the right discipline for the reconstruction project.

---

## What This Study Established

This study established:

1. \(A_{\rm constraint}\)'s source is reduced-derived.
2. \(W_i\)'s source type is constrained by continuity: it should couple to current.
3. \(A_{\rm rad}\)'s control is naturally associated with relaxation.
4. \(\kappa\)'s source is still missing.
5. Tensor source shape is structurally motivated, but coupling remains hand-assigned.
6. Creation remains risky and must not become a free knob.
7. The next best concrete test is the vector current sector.

---

## What This Study Did Not Establish

This study did not derive \(W_i\)'s equation.

It did not derive \(W_i\)'s coefficient.

It did not derive \(\kappa\)'s source law.

It did not derive tensor coupling normalization.

It did not define \(q_v\).

It did not produce Bianchi-like closure.

It only audited source coupling from the vacuum-exchange ontology.

---

## Current Best Interpretation

The vacuum-exchange picture begins to constrain source coupling:

```text
density -> A_constraint
current -> W_i
relaxation -> A_rad suppression
```

But major pieces remain underived:

```text
kappa source,
tensor coupling coefficient,
W_i field equation and coefficient,
closure identity.
```

This means the ontology has begun doing work, but not enough yet.

---

## Next Development Target

The next script should be:

```text
candidate_vector_current_from_continuity.py
```

Purpose:

```text
Derive or fail to derive W_i source form from current continuity.
```

Reason:

```text
W_i is the nearest sector where continuity gives a concrete new source object:
j_i = rho v_i.
```

A successful next step would not merely say:

```text
W_i should match frame dragging.
```

It should ask:

```text
What vector equation is demanded by mass-current continuity and vacuum exchange?
```

---

## Summary

The source-coupling audit is an important group-09 checkpoint.

It says:

```text
A source:
  reduced-derived.

W_i source:
  constrained by current continuity.

A_rad control:
  constrained by relaxation.

kappa source:
  missing.

tensor coupling:
  hand-assigned/matched.

creation:
  risky.
```

The next move is the vector-current sector because it is where continuity most directly gives a new source object.
