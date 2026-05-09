# Marker-to-Derivation Upgrade Candidates

Scripts that perform genuine symbolic computation (identity verification,
equation solving, condition checking) but record only generic archive markers
(`inputs=[]`, `output=sp.Symbol("..._stated")`) instead of preserving the
actual mathematical content in the derivation record.

Upgrading these would let the archive carry verifiable mathematical results
rather than just execution bookmarks. Downstream scripts or audit tools could
then confirm that specific symbolic identities still hold, rather than only
that a script ran.

This list was compiled during the v2 archive retrofit review of groups 08-10.
Groups 01-07 were reviewed before this pattern was identified and have not
been audited for the same issue.

---

## Group 08: covariant_parent_structure

**Scripts 2-7 (inventory/requirements scripts)**

These scripts classify sector requirements as `SATISFIED_REDUCED`, `PARTIAL`,
or `MISSING` using hardcoded dataclass fields. The assessments could instead
be verified against the archive -- checking that the upstream derivation
records actually exist before reporting `SATISFIED_REDUCED`. This would turn
expert assertions into archive-verified assertions.

Affected scripts:
- `candidate_covariant_parent_requirements.py` (R1, R6 marked SATISFIED_REDUCED)
- `candidate_constraint_vs_evolution_split.py` (scalar static, tensor radiation marked SATISFIED_REDUCED)
- `candidate_gauge_structure_requirements.py` (G5 TT gauge marked SATISFIED_REDUCED)
- `candidate_metric_geometric_recombination.py` (A_constraint, h_ij^TT marked SATISFIED_REDUCED)
- `candidate_gauge_invariant_diagnostics.py` (areal radius, lapse, TT strain marked SAFE)
- `candidate_conservation_identity_requirements.py` (problem posed marked SATISFIED_REDUCED)

---

## Group 09: vacuum_identity_and_source_coupling

**`candidate_vector_current_projection_operator.py`**

Verifies projector identities symbolically:
- P_T^2 = P_T (idempotence)
- P_T + P_L = I (completeness)
- P_T * P_L = 0 (orthogonality)
- P_T applied to transverse current preserves it
- P_T applied to longitudinal current annihilates it

Currently records: `vector_current_projection_operator_marker` with empty inputs.

**`candidate_vector_curl_energy_field_equation.py`**

Verifies the curl-curl vector identity symbolically:
- curl(curl(V)) = grad(div(V)) - laplacian(V)

Currently records: `vector_curl_energy_field_equation_marker` with empty inputs.

**`candidate_vector_transverse_current_projection.py`**

Verifies fundamental vector calculus identities:
- curl(grad(phi)) = 0
- div(curl(V)) = 0

Currently records: `vector_transverse_current_projection_marker` with empty inputs.

**`candidate_vector_source_shape_factor.py`**

Computes concrete physical quantities for uniform sphere:
- M = 4*pi*rho*R^3/3
- J = 2*M*R^2*Omega/5
- div(j) = 0 for rigid rotation current
- Monopole current vanishes by symmetry

Currently records: `vector_source_shape_factor_marker` with empty inputs.

---

## Group 10: kappa_trace_response

**`candidate_kappa_exterior_suppression_condition.py`**

Verifies that kappa=0 in exterior recovers the reciprocal metric factor AB=1.
This is the same reciprocal_scaling condition that ConcreteMetricCheck
classifies in earlier groups. The actual A*B expression could be recorded
as a derivation output and cross-checked against the 02_mechanics
exact_recovery result.

Currently records: `kappa_exterior_suppression_condition_marker` with empty inputs.

**`candidate_kappa_constraint_projection_identity.py`**

Verifies projection operator properties:
- Zero-charge projection operator is idempotent (for fixed support)

Currently records: `kappa_constraint_projection_identity_marker` with empty inputs.

**`candidate_kappa_boundary_layer_model.py`**

Verifies boundary layer properties symbolically:
- Smooth compact profile has zero value and flux at boundary
- Boundary flux vanishes
- Effective source has zero net charge

Currently records: `kappa_boundary_layer_model_marker` with empty inputs.

**`candidate_kappa_joint_minimum_energy_functional.py`**

Computes variational results:
- Euler-Lagrange equation for kappa energy functional
- Constant-weight minimizer equation

Currently records: `kappa_joint_minimum_energy_functional_marker` with empty inputs.
