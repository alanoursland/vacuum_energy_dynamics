# 14 Kappa Zeta Map and Projectors Plan

## Recommended Directory Name

Recommended:

```text
14_kappa_zeta_map_and_projectors
```

Reason:

```text
Group 13 made epsilon_vac_config geometric enough to stop being a bucket.
The next unresolved object is the relation between kappa and zeta.
```

The core question is:

```text
What exactly is kappa relative to zeta = ln sqrt(gamma)?
```

Alternative names:

```text
14_kappa_zeta_relation
14_trace_volume_projectors
14_kappa_volume_map
14_trace_volume_recombination
14_volume_trace_projector_structure
```

Best name:

```text
14_kappa_zeta_map_and_projectors
```

---

## One-Line Goal

Determine whether \(\kappa\) is:

```text
an independent non-inertial relaxation variable,
a diagnostic projection of zeta,
a constrained mismatch variable,
or only the reduced areal-gauge diagnostic kappa = 1/2 ln(AB).
```

Then define the projectors required to keep the scalar / trace / volume sectors from double-counting.

---

## Starting Point From Group 13

Group 13 ended with:

\[
\zeta=\ln\sqrt{\gamma}.
\]

Provisional vacuum-volume configuration density:

\[
\epsilon_{\rm vac,config}
=
\frac12K_\zeta(\zeta-\zeta_{\min})^2
+
\frac12L_\zeta|\nabla\zeta|^2.
\]

Separate kappa relaxation energy:

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

But no \(K_{\rm lock}\) energy is counted yet.

Reason:

```text
the kappa-zeta map is not derived,
so combining kappa mismatch energy into epsilon_vac_config risks double-counting.
```

Group 14 exists to resolve or further constrain this.

---

## Core Guardrails

Group 14 must preserve:

```text
no scalar breathing radiation,
no Box kappa,
no Box zeta,
no exterior kappa 1/r tail,
no exterior zeta 1/r tail,
no change to M_ext from kappa/zeta reconfiguration,
no A-sector mass duplicated as volume charge,
no e_kappa double-counting,
no K_lock energy counted unless derived,
no recombination double-counting,
no coefficient tuning.
```

Required exterior neutrality:

\[
\kappa_{\rm ext}\to0,
\]

\[
\zeta_{\rm ext}\to0,
\]

\[
Q_\kappa=0,
\]

\[
Q_{\rm volume}=0,
\]

\[
F_\kappa(R+)=0,
\]

\[
F_\zeta(R+)=0,
\]

\[
\delta M_{\rm ext}|_{\kappa/\zeta}=0.
\]

---

# Proposed Study Sequence

## 1. candidate_kappa_zeta_map_inventory.py

Purpose:

```text
Inventory possible kappa-zeta relations and classify which are safe.
```

Candidate relations:

```text
A. kappa = zeta - zeta_min
B. kappa = P_trace[zeta - zeta_min]
C. kappa is independent relaxation variable coupled to zeta
D. kappa is only the reduced areal-gauge diagnostic 1/2 ln(AB)
E. kappa is boundary/interface mismatch only
F. kappa is an auxiliary Lagrange multiplier enforcing volume equilibrium
```

Tests:

```text
Does the relation avoid double-counting?
Does it preserve exterior neutrality?
Does it avoid scalar radiation?
Does it preserve A-sector mass?
Does it support first-order relaxation?
Does it fit AB=e^(2kappa) in the spherical exterior/interior diagnostic?
```

Expected artifact:

```text
candidate_kappa_zeta_map_inventory.md
```

Success condition:

```text
A safe relation shortlist, with dangerous interpretations rejected.
```

---

## 2. candidate_kappa_as_zeta_mismatch.py

Purpose:

```text
Test the direct relation kappa = zeta - zeta_min.
```

Reason:

```text
This is the cleanest relation if kappa measures local volume deviation from equilibrium.
```

Candidate:

\[
\kappa=\zeta-\zeta_{\min}.
\]

Questions:

```text
Does this make kappa redundant?
Does e_kappa become the same thing as epsilon_vac_config?
Does this force e_kappa inside epsilon_vac_config?
Does it break the group-13 provisional convention?
Does it preserve exterior kappa=zeta=0?
```

Expected artifact:

```text
candidate_kappa_as_zeta_mismatch.md
```

Likely risk:

```text
direct equality may erase kappa as independent relaxation variable,
or cause e_kappa / epsilon double-counting unless one energy is removed.
```

---

## 3. candidate_kappa_as_projected_zeta_mismatch.py

Purpose:

```text
Test kappa as a projected trace / volume mismatch rather than raw zeta difference.
```

Candidate:

\[
\kappa
=
P_{\rm trace}(\zeta-\zeta_{\min}).
\]

or:

\[
\kappa
=
P_{\rm relax}P_{\rm trace}(\zeta-\zeta_{\min}).
\]

Reason:

```text
Projection may preserve exterior neutrality and prevent raw volume strain from becoming a second scalar charge.
```

Questions:

```text
What does P_trace remove?
Does it remove exterior monopole?
Does it enforce Q_volume=0?
Does it distinguish local trace/volume mismatch from A-sector mass response?
Does it make kappa a constrained variable rather than an independent field?
```

Expected artifact:

```text
candidate_kappa_as_projected_zeta_mismatch.md
```

Success condition:

```text
A projected map that can preserve no exterior charge and avoid double-counting.
```

---

## 4. candidate_kappa_independent_relaxation_variable.py

Purpose:

```text
Test whether kappa should remain independent from zeta.
```

Candidate:

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

with exchange:

\[
\frac{de_\kappa}{d\tau}
+
\frac{d\epsilon_{\rm vac,config}}{d\tau}
=
0.
\]

Questions:

```text
If kappa is independent, what prevents it from becoming a second scalar charge?
What ties it to zeta?
Is Gamma_relax the coupling between them?
Does independence create an extra degree of freedom?
Can kappa stay first-order and non-radiative?
```

Expected artifact:

```text
candidate_kappa_independent_relaxation_variable.md
```

Success condition:

```text
A clear rule for independent kappa that does not add scalar radiation or double-counting.
```

---

## 5. candidate_areal_kappa_diagnostic_vs_physical_variable.py

Purpose:

```text
Separate the reduced areal diagnostic kappa = 1/2 ln(AB) from the physical trace/volume variable.
```

Known reduced diagnostic:

\[
\kappa=\frac12\ln(AB).
\]

Questions:

```text
Is this an identity only in areal-gauge spherical reduction?
Is it a physical scalar?
Is it merely a diagnostic of mismatch between A and B?
Can it be generalized covariantly?
How does it relate to zeta?
```

Expected artifact:

```text
candidate_areal_kappa_diagnostic_vs_physical_variable.md
```

Success condition:

```text
A precise distinction between reduced diagnostic kappa and any covariant physical kappa.
```

---

## 6. candidate_trace_projector_definition.py

Purpose:

```text
Define what P_trace must do.
```

Required roles:

```text
extract trace / volume source,
route trace into zeta/kappa sector,
exclude A-sector exterior mass charge,
exclude TT source contamination,
enforce or support Q_volume=0,
prevent scalar radiation.
```

Mathematical handles:

\[
\delta\zeta
=
\frac12\gamma^{ij}\delta\gamma_{ij}.
\]

\[
\delta\zeta|_{TT}=0.
\]

Potential projection:

\[
P_{\rm trace}h_{ij}
=
\frac13\gamma_{ij}\gamma^{ab}h_{ab}.
\]

But source projection is harder:

```text
P_trace[T] must not simply become raw T or raw pressure,
or it may create exterior scalar charge.
```

Expected artifact:

```text
candidate_trace_projector_definition.md
```

Success condition:

```text
A list of required mathematical actions for P_trace and no-go rules for raw trace sources.
```

---

## 7. candidate_boundary_projector_for_volume_neutrality.py

Purpose:

```text
Define P_boundary as the projector / interface rule enforcing exterior neutrality.
```

Required conditions:

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
Q_\kappa=0,
\]

\[
F_\zeta(R+)=0,
\]

\[
F_\kappa(R+)=0,
\]

\[
\delta M_{\rm ext}=0.
\]

Questions:

```text
Is P_boundary compact support?
Is it compensation?
Is it zero-flux boundary condition?
Is it a junction condition?
Is it derived from parent closure?
```

Expected artifact:

```text
candidate_boundary_projector_for_volume_neutrality.md
```

Success condition:

```text
P_boundary requirements become explicit enough to support the boundary mass theorem.
```

---

## 8. candidate_recombination_projector_for_trace_volume.py

Purpose:

```text
Define how A, zeta, kappa, W_i, and h_TT recombine without scalar double-counting.
```

Current reduced map:

```text
g_tt <- A
g_0i <- W_i
g_ij <- scalar_spatial_response(A) + kappa_trace + h_TT
```

Group 13 complication:

```text
zeta also describes spatial volume configuration.
```

Questions:

```text
Does zeta replace kappa_trace?
Does kappa project zeta?
Does kappa appear only as diagnostic?
Does scalar_spatial_response(A) already change spatial volume?
How does recombination avoid counting A-spatial response and zeta-volume response twice?
```

Expected artifact:

```text
candidate_recombination_projector_for_trace_volume.md
```

Success condition:

```text
A recombination no-double-counting ledger for A/zeta/kappa.
```

---

## 9. candidate_kappa_zeta_exterior_neutrality_toy_tests.py

Purpose:

```text
Run toy profiles for kappa/zeta maps and check exterior neutrality diagnostics.
```

Toy profiles:

\[
\zeta(r)
=
\zeta_0
\left(1-\frac{r^2}{R^2}\right)^n.
\]

\[
\kappa(r)
=
\kappa_0
\left(1-\frac{r^2}{R^2}\right)^m.
\]

Diagnostics:

\[
F_\zeta(R)=4\pi R^2\zeta'(R).
\]

\[
F_\kappa(R)=4\pi R^2\kappa'(R).
\]

\[
Q_{\rm volume}.
\]

\[
Q_\kappa.
\]

\[
\delta M_{\rm ext}.
\]

Expected artifact:

```text
candidate_kappa_zeta_exterior_neutrality_toy_tests.md
```

Success condition:

```text
Toy conditions for smooth compact support are explicit,
without claiming physical derivation.
```

---

## 10. kappa_zeta_map_and_projectors_summary.md

Purpose:

```text
Summarize group 14.
```

The summary should answer:

```text
What is the safest current kappa-zeta relation?
Is kappa independent or projected?
Is K_lock still diagnostic?
Can e_kappa remain separate?
What must P_trace do?
What must P_boundary do?
What must P_recombination do?
Does the map preserve exterior neutrality?
Does it avoid scalar double-counting?
```

Expected status:

```text
likely still unfinished,
but with the kappa-zeta relation much less vague.
```

---

# Proposed File List

Recommended group file sequence:

```text
candidate_kappa_zeta_map_inventory.py
candidate_kappa_zeta_map_inventory.md

candidate_kappa_as_zeta_mismatch.py
candidate_kappa_as_zeta_mismatch.md

candidate_kappa_as_projected_zeta_mismatch.py
candidate_kappa_as_projected_zeta_mismatch.md

candidate_kappa_independent_relaxation_variable.py
candidate_kappa_independent_relaxation_variable.md

candidate_areal_kappa_diagnostic_vs_physical_variable.py
candidate_areal_kappa_diagnostic_vs_physical_variable.md

candidate_trace_projector_definition.py
candidate_trace_projector_definition.md

candidate_boundary_projector_for_volume_neutrality.py
candidate_boundary_projector_for_volume_neutrality.md

candidate_recombination_projector_for_trace_volume.py
candidate_recombination_projector_for_trace_volume.md

candidate_kappa_zeta_exterior_neutrality_toy_tests.py
candidate_kappa_zeta_exterior_neutrality_toy_tests.md

kappa_zeta_map_and_projectors_summary.md
```

---

# Recommended First Script

Start with:

```text
candidate_kappa_zeta_map_inventory.py
```

Reason:

```text
Before deriving any one map, inventory all safe and unsafe kappa-zeta interpretations.
```

The first script should output:

```text
a relation ledger:
  map,
  role of kappa,
  role of zeta,
  energy accounting,
  exterior neutrality,
  double-counting risk,
  scalar radiation risk,
  status,
  next test.
```

---

# What Would Count As Success For Group 14

Minimal success:

```text
kappa-zeta interpretations are classified.
```

Better success:

```text
one or two safe kappa-zeta maps survive.
```

Strong success:

```text
P_trace and P_boundary requirements are explicit.
```

Very strong success:

```text
P_recombination can state how A, zeta, kappa, W_i, and h_TT assemble without scalar double-counting.
```

Best possible success:

```text
a clean provisional map emerges:
  kappa is either projected zeta mismatch,
  or independent first-order relaxation coupled to zeta,
  with exterior neutrality and no double-counting preserved.
```

---

# What Would Count As Failure

Group 14 fails if:

```text
kappa and zeta become independent exterior scalar charges,
e_kappa and epsilon_vac_config count the same mismatch twice,
A-sector mass is duplicated as zeta/kappa charge,
K_lock is counted as physical energy before derivation,
Box kappa or Box zeta reappears,
P_trace is just raw pressure/trace without compensation,
P_boundary is imposed by hand with no parent role,
P_recombination copies the GR metric without explaining sector assembly.
```

---

# Current Recommendation

Use:

```text
14_kappa_zeta_map_and_projectors
```

Start with:

```text
candidate_kappa_zeta_map_inventory.py
```

Main concrete target:

```text
candidate_kappa_as_projected_zeta_mismatch.py
```

Main projector target:

```text
candidate_trace_projector_definition.py
```

Main recombination target:

```text
candidate_recombination_projector_for_trace_volume.py
```

Final warning:

```text
Do not let kappa and zeta become two scalar gravities.
One trace/volume response enters once.
```
