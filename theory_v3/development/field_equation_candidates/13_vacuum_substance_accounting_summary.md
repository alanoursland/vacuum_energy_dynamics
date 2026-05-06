# Vacuum Substance Accounting Summary

## Group

```text
13_vacuum_substance_accounting
```

## One-Line Result

Group 13 turned the vague vacuum-substance accounting idea into a constrained geometric accounting scaffold.

It did not derive the final parent identity.

The strongest result is:

```text
epsilon_vac_config is no longer a generic reservoir.
It is provisionally a zeta-volume configuration functional,
with zeta = ln sqrt(gamma),
and e_kappa is kept separate to avoid double-counting.
```

---

## Starting Ontology

Group 13 carried forward the corrected ontology:

```text
vacuum is spacetime.
creating vacuum creates spacetime.
changing local spacetime creates curvature.
```

Therefore:

```text
vacuum accounting is geometric accounting,
not thermodynamic reservoir bookkeeping.
```

The working geometric variable became:

\[
\zeta=\ln\sqrt{\gamma}.
\]

Here:

\[
dV_{\rm phys}=\sqrt{\gamma}\,d^3x.
\]

At linear order:

\[
\delta\zeta
=
\frac12\gamma^{ij}\delta\gamma_{ij}.
\]

For TT perturbations:

\[
\gamma^{ij}h_{ij}^{TT}=0,
\]

so:

\[
\delta\zeta|_{TT}=0.
\]

Interpretation:

```text
trace / volume modes change vacuum-spacetime amount,
TT modes are volume-preserving shear.
```

---

## Study Sequence

Group 13 proceeded through:

```text
candidate_vacuum_substance_accounting_inventory.py
candidate_volume_form_configuration_variable.py
candidate_trace_vs_tt_geometric_split.py
candidate_scalar_conversion_not_damping.py
candidate_mass_acceleration_gradient_coupling.py
candidate_binary_radiation_scalar_conversion_safety.py
candidate_boundary_volume_mode_no_exterior_charge.py
candidate_vacuum_transport_current_constraints.py
candidate_vacuum_accounting_parent_balance.py
candidate_epsilon_vac_config_functional.py
candidate_epsilon_kappa_double_counting_check.py
```

This summary closes the group.

---

# 1. Accounting Inventory

The inventory established that \(E_{\rm vac,config}\) must be:

```text
geometric,
```

or:

```text
tightly constrained bookkeeping tied to geometry.
```

Best immediate geometric targets:

\[
\sqrt{\gamma},
\]

and:

\[
\ln\sqrt{\gamma}.
\]

Optional bookkeeping variables:

```text
q_v,
J_v.
```

Protected quantities:

```text
M_ext,
A_flux,
Sigma_creation in ordinary gravity.
```

Hard rule:

```text
no bottomless bucket.
```

---

# 2. Volume-Form Configuration Variable

The best geometric candidate became:

\[
\zeta=\ln\sqrt{\gamma}.
\]

Physical volume element:

\[
dV_{\rm phys}
=
\sqrt{\gamma}\,d^3x.
\]

Linear variation:

\[
\delta\zeta
=
\frac12\gamma^{ij}\delta\gamma_{ij}.
\]

This makes \(\zeta\) the leading candidate for the vacuum-spacetime configuration variable.

Status:

```text
CANDIDATE / FRAME-DEPENDENT UNTIL u^mu OR FOLIATION IS DEFINED
```

---

# 3. Trace Versus TT Geometric Split

Pure trace perturbation:

\[
h_{ij}
=
\frac13\gamma_{ij}h.
\]

Then:

\[
\delta\zeta=\frac12h.
\]

TT perturbation:

\[
\gamma^{ij}h_{ij}^{TT}=0.
\]

Then:

\[
\delta\zeta|_{TT}=0.
\]

The theorem target is:

```text
ordinary far-zone radiation is TT-only because
volume-changing trace / scalar modes convert into vacuum-spacetime configuration,
while volume-preserving TT shear propagates.
```

Status:

```text
THEOREM TARGET / NOT FULL THEOREM
```

Missing:

```text
nonlinear/covariant extension,
P_trace,
P_TT,
binary scalar-conversion safety proof.
```

---

# 4. Scalar Conversion Is Not Damping

Group 13 rejected the ordinary damped scalar wave as the default model:

\[
\phi_{tt}+\gamma\phi_t+\omega^2\phi=0.
\]

Reason:

```text
no scalar inertia / momentum channel has been derived.
```

Current preferred language:

```text
scalar / trace disturbances are conversion-limited,
not friction-damped waves.
```

Candidate skeleton:

\[
P_{\rm trace}[\text{source/geometry}]
\rightarrow
\delta\zeta.
\]

\[
\zeta=\ln\sqrt{\gamma}.
\]

\[
\kappa\sim\zeta-\zeta_{\min}.
\]

\[
u^\mu\nabla_\mu\kappa
=
-\lambda_\kappa(\kappa-\kappa_{\min}).
\]

Forbidden:

```text
Box A,
A_rad ordinary massless source,
Box kappa,
Box zeta,
exterior zeta/kappa 1/r tail.
```

---

# 5. Coupling: Mass Accelerating Across a Gradient

The phrase:

```text
mass accelerating across a gradient
```

was found to have multiple possible mathematical meanings.

Promising directions:

```text
P_trace[T] -> delta zeta,
nabla_mu(T^munu nabla_nu A),
T^munu nabla_mu nabla_nu A,
geodesic identity / geometry bookkeeping.
```

Dangerous directions:

```text
raw rho v dot grad A,
raw rho a dot grad A,
Box zeta,
Box kappa.
```

Reason:

```text
raw reduced power-like terms may create extra orbital damping,
and proper-acceleration terms may vanish for geodesic motion.
```

No coupling was selected.

---

# 6. Binary Radiation Safety

Scalar / trace conversion is safe only if it is:

```text
conservative bookkeeping,
local compact conversion,
or compensated constraint response.
```

Required:

```text
no far-zone scalar flux,
no exterior zeta / kappa charge,
no secular orbital damping,
ordinary far-zone radiation remains TT-only.
```

Forbidden:

```text
A_rad,
Box zeta,
Box kappa,
far-zone scalar flux,
secular scalar orbital damping.
```

This led directly to the boundary theorem target.

---

# 7. Boundary Volume Mode With No Exterior Charge

Central theorem target:

```text
local trace / volume reconfiguration has zero exterior scalar charge.
```

Equivalent requirements:

\[
\zeta_{\rm ext}\to0,
\]

\[
\kappa_{\rm ext}\to0,
\]

\[
Q_{\rm volume}=0,
\]

\[
F_\zeta(R+)=0,
\]

\[
F_\kappa(R+)=0,
\]

\[
\delta M_{\rm ext}|_{\rm volume/\kappa}=0.
\]

Necessary ingredients:

```text
compact support,
zero flux,
compensation,
A-flux protection.
```

Missing:

```text
P_boundary P_trace.
```

---

# 8. Vacuum Transport Current \(J_v\)

Allowed \(J_v\) classes:

```text
J_v = 0 / local exchange,
compact-support J_v,
constraint redistribution J_v with zero exterior flux,
causal transport J_v only if separately derived.
```

Forbidden \(J_v\) classes:

```text
acausal repair current,
far-zone scalar-energy current,
coefficient tuning current,
exterior mass-changing current,
unlabeled nonlocal transport.
```

Candidate balance skeleton introduced:

\[
u^\mu\nabla_\mu\epsilon_{\rm vac,config}
+
\nabla_\mu J_v^\mu
=
\Sigma_{\rm exchange}
-
\Gamma_{\rm relax}.
\]

---

# 9. Vacuum Accounting Parent Balance

First concrete balance skeleton:

\[
u^\mu\nabla_\mu\epsilon_{\rm vac,config}
+
\nabla_\mu J_v^\mu
=
\Sigma_{\rm exchange}
-
\Gamma_{\rm relax}.
\]

Ordinary conditions:

\[
\Sigma_{\rm creation}=0.
\]

\[
\oint J_v\cdot dS=0.
\]

\[
Q_{\rm volume}=0.
\]

\[
\delta M_{\rm ext}=0.
\]

\[
F_{\rm scalar,far}=0.
\]

Status:

```text
CANDIDATE SKELETON / NOT DERIVED
```

Missing:

```text
epsilon_vac_config,
Sigma_exchange,
u^mu,
parent embedding.
```

---

# 10. Epsilon Functional

Initial scaffold considered:

\[
\epsilon_{\rm vac,config}
=
\frac12K_\zeta(\zeta-\zeta_{\min})^2
+
\frac12L_\zeta|\nabla\zeta|^2
+
\frac12K_{\rm lock}
[
\kappa-(\zeta-\zeta_{\min})
]^2.
\]

But this risked double-counting \(e_\kappa\).

Hard exclusions:

```text
no A_flux,
no M_ext,
no coefficient tuning,
no scalar kinetic wave term.
```

---

# 11. Epsilon / Kappa Double-Counting Fix

Final provisional convention for group 13:

\[
\epsilon_{\rm vac,config}
=
\frac12K_\zeta(\zeta-\zeta_{\min})^2
+
\frac12L_\zeta|\nabla\zeta|^2.
\]

Separate \(\kappa\) relaxation energy:

\[
e_\kappa
=
\frac12K_\kappa(\kappa-\kappa_{\min})^2.
\]

Provisional exchange accounting:

\[
\frac{de_\kappa}{d\tau}
+
\frac{d\epsilon_{\rm vac,config}}{d\tau}
=
0.
\]

Constraint target:

\[
\kappa\sim\zeta-\zeta_{\min}.
\]

No \(K_{\rm lock}\) energy is counted yet.

Interpretation:

```text
epsilon_vac_config is zeta-volume configuration,
e_kappa is separate kappa relaxation energy,
K_lock is diagnostic / constraint target until derived.
```

---

# 12. What Group 13 Established

Group 13 established:

1. \(E_{\rm vac,config}\) should be geometric, not a generic reservoir.
2. \(\zeta=\ln\sqrt{\gamma}\) is the leading geometric candidate.
3. Trace modes change \(\zeta\); TT modes preserve \(\zeta\) at linear order.
4. Scalar / trace behavior should be treated as conversion, not ordinary damping.
5. Raw reduced coupling terms are dangerous until proven conservative.
6. Binary safety requires no far-zone scalar flux or secular scalar damping.
7. Local volume reconfiguration must have zero exterior charge.
8. \(J_v\) is optional and tightly constrained.
9. The first parent-balance skeleton is now explicit.
10. \(\epsilon_{\rm vac,config}\) has a provisional functional form.
11. \(e_\kappa\) remains separate for now to avoid double-counting.

---

# 13. What Group 13 Did Not Establish

Group 13 did not derive:

```text
u^mu,
zeta_min,
K_zeta,
L_zeta,
K_kappa,
Sigma_exchange,
Gamma_relax sign convention,
P_trace,
P_boundary,
P_recombination,
P_TT,
J_v transport law,
Q_volume,
S_volume,
boundary mass theorem,
binary scalar-safety theorem,
parent identity embedding.
```

It also did not prove:

```text
nonlinear TT volume preservation,
covariant volume-form theorem,
kappa-zeta map,
far-zone scalar exclusion,
coefficient derivation.
```

---

# 14. Current Best Reduced Accounting Set

Variables:

\[
\zeta=\ln\sqrt{\gamma}.
\]

\[
\epsilon_{\rm vac,config}
=
\frac12K_\zeta(\zeta-\zeta_{\min})^2
+
\frac12L_\zeta|\nabla\zeta|^2.
\]

\[
e_\kappa
=
\frac12K_\kappa(\kappa-\kappa_{\min})^2.
\]

Balance skeleton:

\[
u^\mu\nabla_\mu\epsilon_{\rm vac,config}
+
\nabla_\mu J_v^\mu
=
\Sigma_{\rm exchange}
-
\Gamma_{\rm relax}.
\]

Exchange condition:

\[
\frac{de_\kappa}{d\tau}
+
\frac{d\epsilon_{\rm vac,config}}{d\tau}
=
0.
\]

Ordinary constraints:

\[
\Sigma_{\rm creation}=0,
\]

\[
\oint J_v\cdot dS=0,
\]

\[
Q_{\rm volume}=0,
\]

\[
\delta M_{\rm ext}=0,
\]

\[
F_{\rm scalar,far}=0.
\]

Forbidden:

```text
A_flux inside epsilon_vac_config,
M_ext inside epsilon_vac_config,
coefficient tuning,
scalar kinetic wave term,
Box zeta,
Box kappa,
far-zone scalar flux,
exterior zeta/kappa charge.
```

---

# 15. Recommended Next Group

Group 13 has reached a natural stopping point.

Recommended next group:

```text
14_kappa_zeta_map_and_projectors
```

Purpose:

```text
Determine whether kappa is an independent relaxation variable,
a diagnostic projection of zeta,
or a constrained mismatch variable.
```

Core questions:

```text
Is kappa = zeta - zeta_min?
Is kappa only the reduced areal-gauge diagnostic 1/2 ln(AB)?
Does kappa have independent relaxation energy?
What is P_trace?
What is P_boundary?
What is P_recombination?
How does the kappa-zeta map preserve exterior neutrality and avoid double-counting?
```

Alternative group names:

```text
14_kappa_zeta_relation
14_trace_volume_projectors
14_kappa_volume_map
14_trace_volume_recombination
```

Recommended:

```text
14_kappa_zeta_map_and_projectors
```

First possible script:

```text
candidate_kappa_zeta_map_inventory.py
```

Purpose:

```text
Inventory possible kappa-zeta relations and decide which are safe:
  kappa = zeta-zeta_min,
  kappa as projection of zeta mismatch,
  kappa as independent relaxation variable,
  kappa as areal-gauge diagnostic only.
```

---

## Final Statement

Group 13 succeeded.

It made vacuum-substance accounting geometric enough to stop being a bucket.

It did not close the theory.

It revealed the next central goblin:

```text
what exactly is kappa relative to zeta?
```
