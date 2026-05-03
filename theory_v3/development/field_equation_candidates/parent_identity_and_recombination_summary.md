# Parent Identity and Recombination Summary

## Group

```text
12_parent_identity_and_recombination
```

## One-Line Result

Group 12 narrowed the parent-identity candidate space.

It did not derive the parent identity.

The strongest result is:

```text
false parent identities are now sharply excluded,
and the surviving parent scaffold must be projector-routed,
scalar-safe,
TT-radiative,
kappa-first-order,
vacuum-substance-exchange-accounted,
boundary-mass-preserving,
and recombination-safe.
```

---

## What Group 12 Was For

Group 11 ended with a coherent minimal reduced field-equation set, but not closure.

The unresolved core was:

```text
parent conservation / recombination identity.
```

Group 12 asked:

```text
What can the parent identity not be?
What must any surviving parent identity imply?
What projectors does it require?
How can scalar radiation remain excluded?
How can kappa remain first-order relaxation?
How can boundary mass be preserved?
How can recombination avoid scalar double-counting?
Where does relaxation energy go?
What could E_vac_config be?
```

---

## Main Strategy

Group 12 did not begin by naming the parent identity.

It began by excluding false parents.

Group motto:

```text
Cut away false parents before naming the real one.
```

This was the right strategy.

The parent identity is still not ready to be crowned.

---

## Study Sequence

Group 12 proceeded through:

```text
candidate_parent_identity_exclusion_constraints.py
candidate_parent_identity_reduced_implications.py
candidate_projector_structure_for_parent_identity.py
candidate_scalar_constraint_not_radiation_identity.py
candidate_kappa_covariant_relaxation_requirement.py
candidate_boundary_mass_preservation_identity.py
candidate_recombination_without_double_counting.py
candidate_relaxation_energy_accounting_identity.py
candidate_parent_identity_template_v2.py
candidate_vacuum_configuration_energy_variable.py
```

This summary closes the group.

---

# 1. Excluded Parent Identity Forms

The parent identity cannot be:

```text
a decorative Bianchi restatement,
an ordinary scalar A wave,
Box kappa,
rho double-sourced into kappa,
nonzero exterior kappa charge,
trace contamination of TT,
longitudinal current sourcing W_i,
boundary smoothing changing exterior mass,
Sigma_creation in ordinary closure,
GR coefficients inserted as derivation,
metric recombination copied from GR.
```

This was the first major success of the group.

The candidate parent space is narrower now.

---

# 2. Reduced-Sector Test Suite

Any surviving parent identity must imply:

```text
A constraint,
exterior Schwarzschild,
B=1/A when kappa=0,
weak scalar / Newtonian limit,
scalar constraint propagation from continuity,
transverse W_i sourcing,
angular momentum far-field vector shape,
TT-only ordinary radiation,
trace exclusion from TT source,
kappa first-order trace relaxation,
exterior kappa neutrality,
boundary mass preservation,
Sigma_creation=0 in ordinary closed gravity,
relaxation energy accounting,
recombination without scalar double-counting.
```

The hardest reduced implications are:

```text
scalar constraint propagation,
kappa trace relaxation,
boundary mass preservation,
tensor / vector coefficient derivation,
recombination.
```

---

# 3. Projector Structure

The parent identity requires projectors before it can be meaningful.

Current clearest projectors:

```text
P_L,
P_T.
```

Current structural projectors:

```text
P_scalar,
P_TT,
P_trace,
P_relax,
P_boundary.
```

Current unresolved or missing projectors:

```text
P_recombination,
P_coeff.
```

Required routing:

```text
rho / scalar charge
  -> P_scalar
  -> A

longitudinal current
  -> P_L
  -> scalar continuity

transverse current
  -> P_T
  -> W_i

TT stress
  -> P_TT
  -> h_ij^TT

trace / pressure
  -> P_trace
  -> kappa_min

kappa imbalance
  -> P_relax
  -> first-order relaxation

boundary data
  -> P_boundary
  -> M_ext preservation and kappa exterior safety

active-regime terms
  -> P_closed
  -> Sigma_creation=0 in ordinary regime

sector fields
  -> P_recombination
  -> geometry without double-counting
```

---

# 4. Scalar Constraint, Not Radiation

The scalar sector is safe only if:

```text
rho routes only to A,
A remains a constraint,
A_rad has no ordinary massless source,
rho does not source long-range kappa,
trace shifts kappa_min without Box kappa,
moving sources update A through continuity,
recombination counts scalar response once.
```

The missing scalar piece remains:

```text
continuity-compatible scalar constraint propagation.
```

This is still one of the hardest gaps.

---

# 5. Kappa Relaxation Requirement

The current safe \(\kappa\) form is:

\[
u^\mu\nabla_\mu\kappa
=
-\lambda_\kappa(\kappa-\kappa_{\min}).
\]

Requirements:

```text
u^mu must be defined,
kappa remains first-order,
kappa_min is scalar / frame-defined,
exterior kappa relaxes to zero,
boundary kappa flux vanishes,
relaxation energy is accounted,
rho does not source kappa,
recombination does not use kappa as duplicate scalar mass response.
```

Unresolved:

```text
the frame field u^mu.
```

Missing:

```text
relaxation energy accounting variable,
S_trace_effective,
chi_kappa.
```

---

# 6. Boundary Mass Preservation

Boundary / \(\kappa\) relaxation can remain safe only if:

\[
\delta M_{\rm ext}\big|_{\kappa{\rm\ relaxation}}=0,
\]

\[
Q_\kappa=0,
\]

\[
F_\kappa(R+)=0,
\]

and:

\[
\kappa_{\rm ext}\to0.
\]

Interpretation:

```text
kappa may smooth trace / volume matching,
but it cannot change exterior mass.
```

This is a requirement, not a theorem.

Missing:

```text
boundary mass preservation theorem.
```

---

# 7. Recombination Without Double-Counting

Candidate reduced map:

```text
g_tt  <- A
g_0i  <- W_i
g_ij  <- scalar_spatial_response(A) + kappa_trace_matching + h_ij^TT
```

with guardrails:

```text
rho -> A only,
trace / pressure -> kappa_min only,
kappa_ext = 0,
h_ij^TT trace-free,
W_i transverse,
source(A_rad ordinary massless)=0,
delta M_ext|kappa_relaxation=0.
```

This remains a reduced map, not a covariant derivation.

Missing:

```text
P_recombination.
```

---

# 8. Relaxation Energy Accounting

Relaxation cannot be energy destruction.

Candidate local free-energy form:

\[
E_\kappa
=
\frac12K_\kappa(\kappa-\kappa_{\min})^2.
\]

Candidate exchange:

\[
\frac{dE_\kappa}{d\tau}
+
\frac{dE_{\rm vac,config}}{d\tau}
=
0.
\]

Interpretation:

```text
curvature excess deposits into vacuum-substance configuration,
curvature deficit pulls from vacuum-substance configuration,
both move toward the local minimum without sloshing.
```

This is candidate accounting, not a parent identity.

Missing:

```text
E_vac_config.
```

---

# 9. Parent Identity Template V2

The tighter scaffold is:

\[
{\rm Div}\,
E_{\rm parent}
[
A,W,h_{TT},\kappa;
P_{\rm scalar},P_T,P_{TT},P_{\rm trace},P_{\rm boundary}
]
=
B_{\rm closed}[T]
+
B_{\rm relax}[\Gamma_{\rm relax},E_{\rm vac,config}].
\]

Ordinary closed regime:

\[
\Sigma_{\rm creation}=0.
\]

Relaxation exchange:

\[
\frac{dE_\kappa}{d\tau}
+
\frac{dE_{\rm vac,config}}{d\tau}
=
0.
\]

Status:

```text
CANDIDATE / SCAFFOLD ONLY
```

It is more constrained than v1.

It is still not closure.

---

# 10. Vacuum Configuration Energy Variable

The best current minimal interpretation is:

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

It must support:

```text
curvature excess depositing into vacuum substance,
curvature deficit pulling from vacuum substance,
ordinary closed-regime accounting,
exterior mass preservation.
```

---

# 11. Current Parent-Identity Candidate Space

A surviving parent identity must now be:

```text
projector-routed,
scalar-safe,
TT-radiative,
kappa-first-order,
vacuum-substance-exchange-accounted,
boundary-mass-preserving,
recombination-safe,
coefficient-honest.
```

It must not be:

```text
decorative,
scalar-radiative,
Box-kappa,
rho-double-counting,
mass-tuning,
active-creation-leaking,
energy-destroying,
metric-copying,
coefficient-matching-disguised-as-derivation.
```

---

# 12. What Group 12 Established

Group 12 established:

1. False parent identities are sharply excluded.
2. Reduced-sector implication tests are explicit.
3. Projector routing is required.
4. Scalar \(A\) must remain constraint, not radiation.
5. \(\kappa\) must remain first-order relaxation, not \(\Box\kappa\).
6. Boundary relaxation must preserve exterior mass.
7. Recombination must count scalar response once.
8. Relaxation energy must exchange with vacuum substance.
9. \(E_{\rm vac,config}\) is the current best name for the missing vacuum-substance configuration variable.
10. Parent template v2 is meaningfully tighter than v1.

---

# 13. What Group 12 Did Not Establish

Group 12 did not derive:

```text
E_parent,
B_closed,
B_relax,
P_scalar,
P_TT,
P_trace,
P_boundary,
P_recombination,
P_coeff,
scalar constraint propagation,
boundary mass theorem,
E_vac_config,
q_v,
J_v,
coefficient action / stiffness principle.
```

It also did not prove:

```text
covariant recombination,
Bianchi-compatible closure,
tensor coupling,
vector normalization,
full GR recovery,
near-boundary observability.
```

---

# 14. Remaining Hard Problems

The hardest remaining problems are:

```text
1. scalar constraint propagation,
2. parent definition of E_parent / B_closed / B_relax,
3. definition of E_vac_config or q_v / J_v,
4. boundary mass preservation theorem,
5. P_recombination,
6. coefficient action / stiffness principle,
7. covariant frame choice u^mu for kappa relaxation.
```

---

# 15. Recommended Next Group

Group 12 has reached a natural stopping point.

Recommended next group:

```text
13_vacuum_substance_accounting
```

Purpose:

```text
Define or constrain the vacuum-substance accounting variables needed by the
parent identity:
  E_vac_config,
  q_v,
  J_v,
  relaxation exchange,
  active-regime separation,
  and ordinary closed-regime conservation.
```

Alternative names:

```text
13_vacuum_configuration_accounting
13_vacuum_exchange_accounting
13_vacuum_substance_energy
13_relaxation_exchange_closure
```

Recommended:

```text
13_vacuum_substance_accounting
```

First possible script:

```text
candidate_vacuum_substance_accounting_inventory.py
```

Purpose:

```text
Inventory all variables and balances needed to make E_vac_config / q_v / J_v
more than a repair reservoir.
```

---

## Final Statement

Group 12 succeeded as a constraint-narrowing group.

It did not produce the parent identity.

It made the parent identity much harder to fake.

That is progress.
