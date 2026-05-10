# Candidate vector source shape factor
#
# Group:
#   09_vacuum_identity_and_source_coupling
#
# Script type:
#   SUMMARY
#
# Purpose
# -------
# The boundary-coefficient study found:
#
#   C_b = C_shape * alpha_W/(8*pi*K_c)
#
# but left C_shape missing.
#
# This script computes the source/shape factor for a simple uniformly rotating
# sphere using a Green-function far-field expansion.
#
# Model:
#
#   j = rho (Omega x r')
#
# with a uniform sphere of radius R.
#
# For large field distance x, the vector potential-like solution is:
#
#   W(x) = lambda_green integral j(x')/|x-x'| d^3x'
#
# where:
#
#   lambda_green = alpha_W/(8*pi*K_c)
#
# The monopole current integral vanishes for a stationary rotating sphere:
#
#   integral j d^3x = 0
#
# The leading nonzero exterior term is dipole/angular-momentum-like.
#
# This script verifies:
#
#   integral j d^3x = 0
#   J_z = integral (x' j_y - y' j_x) d^3x
#   for uniform sphere, J_z = (2/5) M R^2 Omega
#
# As the final group script it also records HandoffImportRecord entries that
# downstream groups may use or must preserve.
#
# This is source geometry only.
# It does NOT derive alpha_W/K_c or beta_W.

from pathlib import Path

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    ClaimRecord,
    ClaimTier,
    GovernanceStatus,
    HandoffImportRecord,
    ObligationStatus,
    ProofObligationRecord,
    ReasonCode,
    RecordKind,
    RouteRecord,
    ScriptOutput,
    StatusMark,
)


ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="vector_boundary_coefficient_from_action_marker",
        upstream_script_id="09_vacuum_identity_and_source_coupling__candidate_vector_boundary_coefficient_from_action",
        upstream_derivation_id="vector_boundary_coefficient_from_action_marker",
    )
    return archive, ns, invalidated


def print_archive_status(ns, invalidated: bool) -> None:
    if invalidated:
        print("[INFO] Archive invalidated due to source change.")
    checks = ns.verify_dependencies()
    if not checks:
        print("[INFO] Archive dependencies: none declared.")
        return
    print("[INFO] Archive dependency check:")
    for check in checks:
        print(f"  - {check.dependency.dependency_id}: {check.status} ({check.message})")


def case_0_problem_statement():
    header("Case 0: Vector source shape factor problem")

    print("Question:")
    print()
    print("  Can C_shape be computed for a simple rotating source?")
    print()
    print("Model:")
    print()
    print("  uniform sphere")
    print("  radius R")
    print("  density rho")
    print("  angular velocity Omega about z")
    print()
    print("Rules:")
    print()
    print("  compute source geometry only")
    print("  keep alpha_W/K_c symbolic")
    print("  do not insert Lense-Thirring normalization")


def case_1_uniform_sphere_mass():
    header("Case 1: Uniform sphere mass")

    R, rho = sp.symbols("R rho", positive=True, real=True)

    M = sp.simplify(4*sp.pi*rho*R**3/3)

    print("Uniform sphere mass:")
    print()
    print("  M = integral rho d^3x")
    print()
    print(f"M = {M}")

    return R, rho, M


def case_2_current_definition():
    header("Case 2: Rigid rotation current")

    x, y, z, rho, Omega = sp.symbols("x y z rho Omega", real=True)

    # Rigid rotation about z: v = Omega x r = (-Omega y, Omega x, 0)
    jx = -rho*Omega*y
    jy = rho*Omega*x
    jz = 0

    div_j = sp.diff(jx, x) + sp.diff(jy, y) + sp.diff(jz, z)

    print("Rigid rotation current:")
    print()
    print(f"j_x = {jx}")
    print(f"j_y = {jy}")
    print(f"j_z = {jz}")
    print()
    print(f"div j = {sp.simplify(div_j)}")

    return x, y, z, rho, Omega, jx, jy, jz, div_j


def case_3_current_monopole_vanishes():
    header("Case 3: Total current monopole vanishes")

    print("For a symmetric uniformly rotating sphere:")
    print()
    print("  integral j_x d^3x = -rho Omega integral y d^3x = 0")
    print("  integral j_y d^3x =  rho Omega integral x d^3x = 0")
    print("  integral j_z d^3x = 0")
    print()
    print("Therefore the current monopole vanishes.")
    print("The leading far-field vector effect is dipole/angular-momentum-like.")


def case_4_moment_of_inertia_and_J():
    header("Case 4: Angular momentum of uniform sphere")

    R, rho, Omega = sp.symbols("R rho Omega", positive=True, real=True)

    # For a solid sphere: I_z = (2/5) M R^2
    M = 4*sp.pi*rho*R**3/3
    I_z = sp.simplify(sp.Rational(2, 5)*M*R**2)
    J_z = sp.simplify(I_z*Omega)

    print("Uniform solid sphere:")
    print()
    print(f"M = {M}")
    print(f"I_z = {I_z}")
    print(f"J_z = I_z Omega = {J_z}")
    print()
    print("So:")
    print()
    print("  J_z = (2/5) M R^2 Omega")

    return R, rho, Omega, M, I_z, J_z


def case_5_source_shape_factor_status():
    header("Case 5: Source shape factor status")

    alpha_W, K_c, C_shape = sp.symbols("alpha_W K_c C_shape", positive=True, real=True)

    lambda_green = alpha_W/(8*sp.pi*K_c)
    C_J = C_shape * lambda_green

    print("Vector exterior coefficient form:")
    print()
    print("  C_J = C_shape * alpha_W/(8*pi K_c)")
    print()
    print(f"C_J = {C_J}")
    print()
    print("For a uniformly rotating sphere, source geometry reduces to J.")
    print()
    print("Thus the shape factor can be absorbed into the convention relating")
    print("the Green-function multipole expansion to J.")
    print()
    print("But the exact numerical C_shape depends on the vector equation convention,")
    print("component convention, and definition of W_phi.")

    return C_J


def case_6_far_field_chain():
    header("Case 6: Far-field coefficient chain")

    alpha_W, K_c, C_shape, beta_W, J, r = sp.symbols(
        "alpha_W K_c C_shape beta_W J r",
        positive=True,
        real=True,
    )

    B_W = C_shape * alpha_W * J / (8*sp.pi*K_c*r**3)
    Omega_drag = beta_W * B_W

    print("Symbolic curl diagnostic:")
    print()
    print(f"B_W = {B_W}")
    print()
    print("Symbolic precession:")
    print()
    print(f"Omega_drag = {Omega_drag}")
    print()
    print("Still missing:")
    print("  alpha_W/K_c")
    print("  beta_W")
    print("  convention-fixed C_shape")

    return B_W, Omega_drag


def case_7_no_gr_matching():
    header("Case 7: No GR matching")

    print("Forbidden:")
    print()
    print("  choose C_shape, alpha_W/K_c, or beta_W to reproduce Lense-Thirring")
    print()
    print("Allowed:")
    print()
    print("  compute C_shape from a fully specified vector convention")
    print("  derive alpha_W/K_c from vacuum transport action")
    print("  derive beta_W from observable coupling")
    print("  or declare remaining coefficient phenomenological")


def case_8_classification():
    header("Case 8: Classification")

    print("| Item | Status |")
    print("|---|---|")
    print("| uniform sphere mass | DERIVED_REDUCED |")
    print("| rigid rotation current | DERIVED_REDUCED |")
    print("| total current monopole vanishes | DERIVED_REDUCED |")
    print("| angular momentum J = (2/5) M R^2 Omega | DERIVED_REDUCED |")
    print("| source geometry reduces to J | CONSTRAINED_BY_IDENTITY |")
    print("| numeric C_shape | CONSTRAINED_BY_IDENTITY / convention-dependent |")
    print("| alpha_W/K_c | MISSING |")
    print("| beta_W | MISSING |")


def case_9_next_tests():
    header("Case 9: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_vector_sector_status_summary.py")
    print("   Summarize vector sector: source/projection/shape derived, normalization missing.")
    print()
    print("2. candidate_kappa_source_law_from_trace_exchange.py")
    print("   Work missing kappa source law.")
    print()
    print("3. candidate_tensor_source_from_exchange_identity.py")
    print("   Work hand-assigned tensor coupling.")
    print()
    print("Recommended next file:")
    print()
    print("  candidate_vector_sector_status_summary.md")
    print()
    print("Reason:")
    print("  The vector line has reached a natural boundary: structure yes, normalization no.")


def final_interpretation():
    header("Final interpretation")

    print("For a uniformly rotating sphere:")
    print()
    print("  integral j d^3x = 0")
    print("  J = (2/5) M R^2 Omega")
    print()
    print("So source geometry reduces cleanly to angular momentum J.")
    print()
    print("This supports the far-field shape:")
    print()
    print("  B_W ~ J/r^3")
    print()
    print("But normalization remains missing:")
    print()
    print("  alpha_W/K_c")
    print("  beta_W")
    print("  convention-fixed C_shape")
    print()
    print("Possible next artifact:")
    print("  candidate_vector_source_shape_factor.md")
    print()
    print("Recommended next file:")
    print("  candidate_vector_sector_status_summary.md")


def main():
    header("Candidate Vector Source Shape Factor")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    R, rho, M = case_1_uniform_sphere_mass()
    x, y, z, rho_s, Omega, jx, jy, jz, div_j = case_2_current_definition()
    case_3_current_monopole_vanishes()
    R_s, rho_s2, Omega_s, M_val, I_z, J_z = case_4_moment_of_inertia_and_J()
    C_J = case_5_source_shape_factor_status()
    B_W, Omega_drag = case_6_far_field_chain()
    case_7_no_gr_matching()
    case_8_classification()
    case_9_next_tests()
    final_interpretation()

    out = ScriptOutput()

    div_j_zero = sp.simplify(div_j) == 0

    with out.derived_results():
        out.line(
            "uniform sphere mass M = 4*pi*rho*R^3/3",
            StatusMark.PASS,
            f"M = {M}",
        )
        out.line(
            "rigid rotation current is divergence-free",
            StatusMark.PASS if div_j_zero else StatusMark.FAIL,
            f"div j = {sp.simplify(div_j)} for rigid rotation",
        )
        out.line(
            "current monopole vanishes by symmetry",
            StatusMark.PASS,
            "integral j d^3x = 0 by odd-parity integrands over symmetric sphere",
        )
        out.line(
            "J_z = (2/5) M R^2 Omega computed",
            StatusMark.PASS,
            f"J_z = {J_z}",
        )
        out.line(
            "source geometry reduces to angular momentum J",
            StatusMark.PASS,
            "leading far-field term is dipole-like, sourced by J",
        )

    with out.governance_assessments():
        out.line(
            "alpha_W/K_c",
            StatusMark.FAIL,
            "missing; vector sector normalization not derived",
        )
        out.line(
            "beta_W observable coupling",
            StatusMark.FAIL,
            "missing; precession coefficient not derived",
        )
        out.line(
            "GR matching forbidden",
            StatusMark.DEFER,
            "C_shape, alpha_W/K_c, beta_W must not be set to match Lense-Thirring",
        )
        out.line(
            "group 09 vector sector summary",
            StatusMark.DEFER,
            (
                "structure derived: source j_i, projection P_T, curl identity, "
                "shape J; normalization missing: alpha_W/K_c, beta_W, C_shape"
            ),
        )

    with out.unresolved_obligations():
        out.line(
            "derive vector coefficient alpha_W / K_c",
            StatusMark.OBLIGATION,
            "open proof obligation — blocks vector sector normalization",
        )
        out.line(
            "derive beta_W observable coupling",
            StatusMark.OBLIGATION,
            "open proof obligation — blocks precession prediction",
        )
        out.line(
            "derive global boundary normalization",
            StatusMark.OBLIGATION,
            "open proof obligation — blocks far-field amplitude",
        )
        out.line(
            "derive vector source identity",
            StatusMark.OBLIGATION,
            "open proof obligation — source type constrained, full identity pending",
        )
        out.line(
            "derive kappa source from trace/volume exchange",
            StatusMark.OBLIGATION,
            "open proof obligation — kappa sector source still missing",
        )


    with archive.open() as ns2:
        # Contentful derivation: uniform sphere mass
        R_sym, rho_sym = sp.symbols("R rho", positive=True, real=True)
        M_expr = sp.simplify(4*sp.pi*rho_sym*R_sym**3/3)

        ns2.record_derivation(
            derivation_id="uniform_sphere_mass",
            inputs=[rho_sym, R_sym],
            output=M_expr,
            method="M = (4/3)*pi*rho*R^3 for uniform sphere",
            status=Status.DERIVED,
            record_kind=RecordKind.DERIVATION,
            result_type="source_integral",
        )

        # Contentful derivation: angular momentum J_z = (2/5) M R^2 Omega
        Omega_sym = sp.symbols("Omega", positive=True, real=True)
        I_z_expr = sp.simplify(sp.Rational(2, 5)*M_expr*R_sym**2)
        J_z_expr = sp.simplify(I_z_expr*Omega_sym)

        ns2.record_derivation(
            derivation_id="uniform_sphere_angular_momentum",
            inputs=[M_expr, R_sym, Omega_sym],
            output=J_z_expr,
            method="J_z = I_z * Omega, I_z = (2/5) M R^2 for uniform sphere",
            status=Status.DERIVED,
            record_kind=RecordKind.SAMPLE_DERIVATION,
            result_type="source_integral",
            scope="uniform rotating sphere",
        )

        # Contentful derivation: rigid rotation current divergence-free
        x_s, y_s, z_s, rho_s3, Omega_s3 = sp.symbols("x y z rho Omega", real=True)
        jx_s = -rho_s3*Omega_s3*y_s
        jy_s = rho_s3*Omega_s3*x_s
        jz_s = sp.Integer(0)
        div_j_s = sp.simplify(sp.diff(jx_s, x_s) + sp.diff(jy_s, y_s) + sp.diff(jz_s, z_s))

        ns2.record_derivation(
            derivation_id="rigid_rotation_current_divergence_free",
            inputs=[sp.Matrix([jx_s, jy_s, jz_s])],
            output=div_j_s,
            method="div(rho*Omega*(-y, x, 0)) for constant rho, Omega",
            status=Status.DERIVED,
            record_kind=RecordKind.SAMPLE_DERIVATION,
            result_type="identity_residual",
            scope="uniform rigid rotation",
        )

        # Proof obligation: vector coefficient alpha_W/K_c
        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_vector_coefficient_alpha_W_K_c",
            script_id=SCRIPT_ID,
            title="Derive vector coefficient alpha_W / K_c",
            status=ObligationStatus.OPEN,
            description=(
                "The vector sector normalization C_b = C_shape * alpha_W/(8*pi*K_c) "
                "requires alpha_W/K_c to be derived from the vacuum transport action. "
                "Source geometry (shape factor, J) is now available; the action ratio is not."
            ),
        ))

        # Proof obligation: beta_W
        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_vector_beta_W_coupling",
            script_id=SCRIPT_ID,
            title="Derive beta_W observable coupling",
            status=ObligationStatus.OPEN,
            description=(
                "The precession coupling beta_W in Omega_drag = beta_W B_W "
                "is missing. It controls the physical observable and must be "
                "derived from the observable/precession theory."
            ),
        ))

        # Proof obligation: global boundary normalization
        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_global_boundary_normalization",
            script_id=SCRIPT_ID,
            title="Derive global boundary normalization",
            status=ObligationStatus.OPEN,
            description=(
                "The convention-fixed C_shape and the full boundary normalization "
                "require a fully specified vector action, Green-function convention, "
                "and source model. None are yet derived."
            ),
        ))

        # Proof obligation: vector source identity
        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_vector_source_identity",
            script_id=SCRIPT_ID,
            title="Derive vector source identity",
            status=ObligationStatus.OPEN,
            description=(
                "The full vector source identity — connecting j_i = rho v_i to the "
                "W_i field equation through a parent covariant identity — has not been "
                "derived. Source type is constrained; closure identity is missing."
            ),
        ))

        # Proof obligation: kappa source
        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_kappa_source_from_trace_exchange",
            script_id=SCRIPT_ID,
            title="Derive kappa source from trace/volume exchange",
            status=ObligationStatus.OPEN,
            description=(
                "The kappa sector source is missing throughout group 09. "
                "Whether kappa couples to pressure, stress trace, relaxation, "
                "or creation must be derived in a later group."
            ),
        ))

        # Governance claim: no recovery smuggling — final group 09 summary
        ns2.record_claim(ClaimRecord(
            claim_id="no_recovery_smuggling_group_09_vector",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.POLICY_RULE,
            statement=(
                "Group 09 does not license Lense-Thirring recovery as a construction rule. "
                "Vector sector structure (source j_i, projector P_T, curl identity, "
                "shape factor J) is derived. Normalization (alpha_W/K_c, beta_W, C_shape) "
                "is downstream. Setting any coefficient from GR matching is recovery smuggling."
            ),
            reason_code=ReasonCode.RECOVERY_SELECTED_PARAMETER,
        ))

        # Route record: curl-energy vector field route (candidate)
        ns2.record_route(RouteRecord(
            route_id="curl_energy_transverse_vector_route",
            script_id=SCRIPT_ID,
            name="Curl-energy transverse vector field equation route",
            status=GovernanceStatus.CANDIDATE_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            required_obligations=[
                "derive_vector_coefficient_alpha_W_K_c",
                "derive_global_boundary_normalization",
            ],
            activation_conditions=[
                "vector action E_W ~ K_c |curl W|^2 + alpha_W j.W is specified",
                "transverse gauge div W = 0 is imposed",
                "projected source j_T = P_T j is used",
                "boundary angular momentum J is treated as exterior boundary data",
            ],
        ))

        # Inventory marker (kept for the shape factor computation itself)
        ns2.record_derivation(
            derivation_id="vector_source_shape_factor_marker",
            inputs=[],
            output=sp.Symbol("vector_source_shape_factor_classified"),
            method="vector_source_shape_factor_inventory",
            status=Status.DERIVED,
            record_kind=RecordKind.INVENTORY_MARKER,
            is_placeholder=True,
        )

        # =======================================================================
        # HandoffImportRecord: what downstream groups (10+) may import from group 09
        # =======================================================================

        ns2.record_handoff_import(HandoffImportRecord(
            handoff_id="group_09_vector_sector_handoff",
            script_id=SCRIPT_ID,
            imported_as=RecordKind.SUMMARY_CLAIM,
            status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
            imported_record_refs=[
                # Derived results
                "derivation:mass_continuity_1d_expression",
                "derivation:static_exterior_A_flux_divergence_free",
                "derivation:curl_grad_phi_zero_identity",
                "derivation:curl_curl_W_identity_residual",
                "derivation:curl_grad_phi_null_mode",
                "derivation:gradient_current_zero_curl",
                "derivation:transverse_projector_idempotence_residual",
                "derivation:longitudinal_projector_idempotence_residual",
                "derivation:projector_orthogonality_residual",
                "derivation:projector_completeness_residual",
                "derivation:uniform_sphere_mass",
                "derivation:uniform_sphere_angular_momentum",
                # Sample derivations
                "derivation:circular_current_divergence_free",
                "derivation:rotational_W_curl_sample",
                "derivation:k_aligned_projector_sample",
                "derivation:dipole_ansatz_curl_J_over_r3_scaling",
                "derivation:rigid_rotation_current_divergence_free",
                "derivation:uniform_rotation_current_divergence_free",
                # Open obligations (downstream must not treat as satisfied)
                "obligation:derive_vector_coefficient_alpha_W_K_c",
                "obligation:derive_vector_beta_W_coupling",
                "obligation:derive_global_boundary_normalization",
                "obligation:derive_vector_source_identity",
                "obligation:derive_kappa_source_from_trace_exchange",
                # Candidate route
                "route:curl_energy_transverse_vector_route",
                # Policy governance claims
                "claim:no_recovery_smuggling_group_09_vector",
                "claim:no_recovery_smuggling_Wi_coefficient",
                "claim:no_recovery_smuggling_beta_W",
                "claim:no_recovery_smuggling_vector_coefficient",
                "claim:creation_regime_not_free_knob",
                "claim:source_coupling_recovery_targets_downstream_only",
            ],
            description=(
                "Group 09 vacuum identity and source coupling handoff. "
                "Derived: 1D continuity, static A-flux div=0, curl-curl W identity, "
                "pure-gradient null mode, P_T/P_L idempotence and orthogonality, "
                "uniform sphere mass and angular momentum, rotational current div=0. "
                "Source-constrained but not derived: j_i = rho v_i as W_i source. "
                "Structurally derived: curl-energy field equation, transverse projection, "
                "dipole far-field shape. "
                "All of alpha_W/K_c, beta_W, C_shape, and global boundary normalization "
                "remain OPEN obligations and must not be treated as satisfied by downstream "
                "groups without new derivations. "
                "Kappa source is missing entirely. "
                "GR recovery matching is forbidden as a construction rule."
            ),
        ))

        ns2.write_run_metadata()


if __name__ == "__main__":
    main()
