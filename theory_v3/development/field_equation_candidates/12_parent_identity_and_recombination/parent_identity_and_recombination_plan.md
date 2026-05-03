# 12 Parent Identity and Recombination Plan

## Recommended Directory Name

Recommended:

```text
12_parent_identity_and_recombination
```

Yes — this is still the right group name.

Reason:

```text
The two unresolved closure gaps are now clearly:
  parent conservation / Bianchi-like identity,
  covariant or disciplined metric recombination.
```

However, the group should not begin by trying to invent a beautiful full parent identity.

It should begin by asking:

```text
What can the parent identity not be?
```

The group should first cut away impossible or dangerous parent-identity forms.

Only after that should it attempt a positive parent identity.

---

## Alternative Names Considered

```text
12_parent_closure_identity
12_covariant_recombination_identity
12_bianchi_compatibility
12_parent_identity_constraints
12_parent_identity_no_go_tests
12_reduced_identity_constraints
```

Best name:

```text
12_parent_identity_and_recombination
```

Why:

```text
The group is not only about conservation.
It is also about how A, W_i, h_ij^TT, and kappa recombine into one geometry-like object.
```

The shorter alternatives are narrower.

---

## One-Line Goal

Group 12 should determine whether the group-11 sector ledger can be forced by a parent identity rather than merely organized by hand.

The goal is:

```text
find the structural requirements and exclusions that any parent identity must satisfy.
```

Only then:

```text
try a candidate parent identity.
```

---

## Group Motto

```text
Cut away false parents before naming the real one.
```

Or, goblin version:

```text
Do not crown the first shiny equation.
```

---

## Why This Group Is Needed

Group 11 produced a minimal current equation set:

\[
\Delta_{\rm areal}A
=
\frac{8\pi G}{c^2}\rho,
\]

\[
A_{\rm ext}
=
1-\frac{2GM}{c^2r},
\]

\[
AB=e^{2\kappa},
\qquad
\kappa_{\rm ext}=0
\Rightarrow
B=\frac{1}{A},
\]

\[
\nabla\times\nabla\times W
=
-\frac{\alpha_W}{2K_c}j_T,
\]

\[
\Box h_{ij}^{TT}
=
-C_T S_{ij}^{TT},
\]

\[
\dot{\kappa}
=
-\mu_\kappa K_\kappa(\kappa-\kappa_{\min}),
\]

\[
\kappa_{\min}
=
\chi_\kappa S_{\rm trace,effective},
\]

\[
{\rm source}(A_{\rm rad}\ {\rm ordinary\ massless})=0,
\]

\[
\Sigma_{\rm creation}=0
\]

in the ordinary closed regime.

Group 11 also identified the parent closure target:

\[
{\rm Div}\,
E_{\rm parent}[A,W,h_{TT},\kappa]
=
B_{\rm closed}[T]
+
B_{\rm relax}[\Gamma_{\rm relax}].
\]

But this is only a template.

Group 12 must determine whether such an identity can actually exist in a non-decorative way.

---

## Core Question

The central question for group 12 is:

```text
Can one parent identity explain the reduced sectors without importing GR by hand?
```

More specifically:

```text
Can the parent identity force:
  A as scalar constraint,
  W_i as transverse current response,
  h_ij^TT as the only ordinary radiative sector,
  kappa as non-radiative trace relaxation,
  exterior mass preservation,
  ordinary Sigma_creation = 0,
  and metric recombination without scalar double-counting?
```

---

## Group Strategy

The group should proceed in three phases.

### Phase 1: Exclusion / No-Go Constraints

Ask:

```text
What forms of parent identity are already ruled out?
```

This protects the work from decorative closure.

### Phase 2: Reduced Implication Tests

Ask:

```text
What must any surviving parent identity imply in each reduced sector?
```

This converts the sector ledger into formal tests.

### Phase 3: Candidate Parent / Recombination Scaffold

Only after exclusions and reduced tests:

```text
try a positive parent identity and recombination map.
```

---

# Proposed Study Sequence

## 1. candidate_parent_identity_exclusion_constraints.py

Purpose:

```text
Determine what forms the parent identity cannot take.
```

This is the recommended first script.

Reason:

```text
Before writing a candidate parent identity, rule out bad identity classes.
```

Questions:

```text
Can the parent identity contain an ordinary scalar wave operator on A?
Can it contain Box kappa?
Can it let rho source both A and kappa?
Can it let trace stress source TT radiation?
Can it let boundary smoothing change exterior mass?
Can it include Sigma_creation in ordinary closed gravity?
Can it merely restate the GR Bianchi identity?
```

Expected exclusions:

```text
no ordinary massless scalar A_rad channel,
no Box kappa trace channel,
no independent rho-sourced long-range kappa,
no metric recombination that duplicates scalar trace,
no ordinary Sigma_creation term,
no boundary mass tuning,
no decorative Bianchi restatement.
```

Expected artifact:

```text
candidate_parent_identity_exclusion_constraints.md
```

Success condition:

```text
A list of forbidden parent-identity structures.
```

---

## 2. candidate_parent_identity_reduced_implications.py

Purpose:

```text
State what the parent identity must imply in each reduced sector.
```

This is the earlier proposed first script, but it should come second.

Questions:

```text
What does the parent identity imply in the static spherical sector?
What does it imply in the weak scalar sector?
What does it imply in the stationary vector sector?
What does it imply in the TT radiation sector?
What does it imply in the kappa trace sector?
What does it imply at boundaries?
```

Required reductions:

```text
A-sector:
  recover areal flux law.

Exterior:
  recover B=1/A when kappa=0.

Vector:
  recover transverse curl-curl W equation.

Tensor:
  recover TT wave equation.

Kappa:
  recover first-order relaxation, not Box kappa.

Radiation:
  ordinary long-range radiation is TT-only.

Boundary:
  preserve exterior mass.

Closed regime:
  Sigma_creation = 0.
```

Expected artifact:

```text
candidate_parent_identity_reduced_implications.md
```

Success condition:

```text
A parent-identity test suite.
```

---

## 3. candidate_projector_structure_for_parent_identity.py

Purpose:

```text
Work out the projector structure needed to separate scalar, vector, tensor, and trace sectors.
```

Reason:

```text
The parent identity likely lives or dies by its projection structure.
```

Questions:

```text
What projector sends rho to A?
What projector sends j_T to W_i?
What projector sends TT stress to h_ij^TT?
What projector sends trace/pressure to kappa_min?
What projector prevents scalar radiation?
What projector prevents trace contamination of TT waves?
```

Expected projectors:

```text
P_scalar
P_T
P_TT
P_trace
P_constraint
P_relax
```

Possible schematic decomposition:

\[
T
\rightarrow
P_{\rm scalar}T
+
P_TT
+
P_{\rm trace}T
+
P_{\rm vector}T.
\]

Expected artifact:

```text
candidate_projector_structure_for_parent_identity.md
```

Success condition:

```text
A decomposition showing which source components feed which sector and which are forbidden.
```

---

## 4. candidate_scalar_constraint_not_radiation_identity.py

Purpose:

```text
Attack the hardest scalar question:
why does the scalar sector constrain rather than radiate?
```

Reason:

```text
This is one of the essential differences between a safe theory and an excluded scalar-gravity theory.
```

Questions:

```text
Why does A have an elliptic/constraint role?
Why is A_rad rejected?
Why does kappa relax but not propagate?
Can the same structural feature explain both?
```

Possible target:

```text
scalar/trace projectors have constraint or first-order relaxation operators,
not second-order hyperbolic wave operators.
```

Expected artifact:

```text
candidate_scalar_constraint_not_radiation_identity.md
```

Success condition:

```text
A clear structural reason for scalar non-radiation, or an explicit statement that it remains imposed.
```

---

## 5. candidate_kappa_covariant_relaxation_requirement.py

Purpose:

```text
Test what a covariant or frame-consistent kappa relaxation law must look like.
```

Reason:

```text
Kappa is currently the most elaborate but fragile sector.
```

Questions:

```text
Can dot(kappa) be replaced by a flow derivative?
What defines the local vacuum frame?
Does relaxation preserve covariance or require preferred slicing?
Does kappa_min transform as a scalar?
Does relaxation energy have a destination variable?
```

Candidate replacement:

\[
u^\mu\nabla_\mu\kappa
=
-\mu_\kappa K_\kappa(\kappa-\kappa_{\min}).
\]

Status should remain:

```text
STRUCTURAL / UNFINISHED
```

Expected artifact:

```text
candidate_kappa_covariant_relaxation_requirement.md
```

Success condition:

```text
A covariantization requirement list, not a final covariant kappa law.
```

---

## 6. candidate_boundary_mass_preservation_identity.py

Purpose:

```text
Prove or require that kappa / boundary relaxation cannot change exterior mass.
```

Reason:

```text
Boundary smoothing tuning measured mass was identified as a fatal closure failure.
```

Questions:

```text
What is exterior mass in the A-sector?
What does kappa boundary smoothing modify?
What must be held fixed?
Can boundary relaxation alter local curvature while preserving the exterior 1/r coefficient?
```

Required condition:

\[
\delta M_{\rm ext}\big|_{\kappa\ {\rm relaxation}}=0.
\]

Expected artifact:

```text
candidate_boundary_mass_preservation_identity.md
```

Success condition:

```text
A boundary mass preservation condition or no-go result.
```

---

## 7. candidate_recombination_without_double_counting.py

Purpose:

```text
Try a more disciplined recombination map.
```

Reason:

```text
Metric recombination remains unfinished and is the main place silent GR import can occur.
```

Questions:

```text
How does A enter g_tt?
How does W_i enter g_0i?
How does h_ij^TT enter g_ij?
Where, if anywhere, does kappa enter g_ij or AB?
How is scalar trace counted exactly once?
```

Constraints:

```text
rho -> A, not long-range kappa;
trace -> kappa_min, not scalar wave;
h_TT trace-free;
W_i transverse;
exterior kappa=0.
```

Expected artifact:

```text
candidate_recombination_without_double_counting.md
```

Success condition:

```text
A reduced recombination map with explicit no-double-counting checks.
```

---

## 8. candidate_parent_identity_template_v2.py

Purpose:

```text
After exclusions, projectors, scalar/radiation rules, kappa requirements, and boundary mass preservation, try an improved parent identity scaffold.
```

Reason:

```text
The previous parent template was intentionally loose.
This one should be more constrained by group-12 tests.
```

Expected form:

\[
{\rm Div}\,
E_{\rm parent}^{(2)}[A,W,h_{TT},\kappa]
=
B_{\rm closed}^{(2)}[T]
+
B_{\rm relax}^{(2)}[\Gamma_{\rm relax}]
\]

with explicit sector projections:

\[
P_{\rm scalar},
\quad
P_T,
\quad
P_{TT},
\quad
P_{\rm trace}.
\]

Expected artifact:

```text
candidate_parent_identity_template_v2.md
```

Success condition:

```text
A tighter parent identity scaffold than group 11, or an explicit failure statement.
```

---

## 9. parent_identity_and_recombination_summary.md

Purpose:

```text
Summarize group 12.
```

This should answer:

```text
What parent identity forms are excluded?
What reduced implications are required?
What projector structure is needed?
Can scalar non-radiation be made structural?
Can kappa relaxation be made frame/covariance-consistent?
Can boundary mass be preserved?
Can recombination avoid double-counting?
Is a parent identity closer, or still missing?
```

Expected status:

```text
probably still UNFINISHED,
but with a much smaller candidate space.
```

---

# Proposed File List

Recommended group file sequence:

```text
candidate_parent_identity_exclusion_constraints.py
candidate_parent_identity_exclusion_constraints.md

candidate_parent_identity_reduced_implications.py
candidate_parent_identity_reduced_implications.md

candidate_projector_structure_for_parent_identity.py
candidate_projector_structure_for_parent_identity.md

candidate_scalar_constraint_not_radiation_identity.py
candidate_scalar_constraint_not_radiation_identity.md

candidate_kappa_covariant_relaxation_requirement.py
candidate_kappa_covariant_relaxation_requirement.md

candidate_boundary_mass_preservation_identity.py
candidate_boundary_mass_preservation_identity.md

candidate_recombination_without_double_counting.py
candidate_recombination_without_double_counting.md

candidate_parent_identity_template_v2.py
candidate_parent_identity_template_v2.md

parent_identity_and_recombination_summary.md
```

---

# Recommended First Script

Start with:

```text
candidate_parent_identity_exclusion_constraints.py
```

Reason:

```text
The next group should not begin by constructing.
It should begin by excluding.
```

The first script should output:

```text
forbidden parent identity structures,
why each is forbidden,
which group-11 result forbids it,
what failure mode it triggers,
and what kind of parent identity remains possible.
```

---

# What Would Count as Success for Group 12

Group 12 succeeds if it can say:

```text
The parent identity is still unfinished,
but its candidate space is now sharply constrained.
```

More specifically, success means:

```text
bad parent identities are ruled out,
reduced-sector requirements are explicit,
projector structure is clarified,
scalar non-radiation is either structurally motivated or honestly still imposed,
kappa relaxation has a covariance/frame requirement,
boundary mass preservation is formalized,
recombination has a no-double-counting map.
```

A stronger success would be:

```text
a parent identity template that is no longer decorative.
```

The strongest success would be:

```text
a reduced parent identity that actually forces the known sectors.
```

But that should not be expected immediately.

---

# What Would Count as Failure

Group 12 fails if it:

```text
writes a parent identity that merely restates GR,
claims Bianchi compatibility without derivation,
lets kappa become a repair knob,
lets scalar radiation reappear,
duplicates scalar source response,
uses tensor/vector GR coefficients as if derived,
or hides metric recombination assumptions.
```

---

# Current Recommendation

Use:

```text
12_parent_identity_and_recombination
```

Start with:

```text
candidate_parent_identity_exclusion_constraints.py
```

Do not start with:

```text
candidate_parent_identity_template_v2.py
```

Reason:

```text
The theory is not ready to name the parent.
It is ready to rule out false parents.
```
