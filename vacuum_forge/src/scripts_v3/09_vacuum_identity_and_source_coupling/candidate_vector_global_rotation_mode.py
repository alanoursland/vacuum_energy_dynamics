# Candidate vector global rotation mode
#
# Group:
#   09_vacuum_identity_and_source_coupling
#
# Script type:
#   DERIVATION
#
# Purpose
# -------
# The vector projection-operator study showed that the local Fourier projector
#
#   P_T = I - k k^T/k^2
#
# works for k^2 != 0, but the k=0/global mode requires boundary treatment.
#
# This script studies the global rotation / angular momentum issue.
#
# It asks:
#
#   1. how angular momentum arises from current,
#   2. why a purely local projector misses global/boundary modes,
#   3. how a rotating compact source can set exterior vector boundary data,
#   4. why the far field should be angular-momentum-like,
#   5. why the coefficient is still missing.
#
# This does NOT derive the Lense-Thirring coefficient.
# It keeps the coefficient symbolic.

from pathlib import Path

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    ClaimRecord,
    ClaimTier,
    GovernanceStatus,
    ObligationStatus,
    ProofObligationRecord,
    ReasonCode,
    RecordKind,
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


def is_zero(expr) -> bool:
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="vector_current_projection_operator_marker",
        upstream_script_id="09_vacuum_identity_and_source_coupling__candidate_vector_current_projection_operator",
        upstream_derivation_id="vector_current_projection_operator_marker",
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
    header("Case 0: Global rotation mode problem")

    print("The transverse projector uses 1/k^2 and works for local k != 0 modes.")
    print()
    print("But global rotation / total angular momentum is a boundary/global issue.")
    print()
    print("Question:")
    print()
    print("  How should a compact rotating source set exterior vector boundary data?")
    print()
    print("Rules:")
    print()
    print("  keep coefficients symbolic")
    print("  do not insert Lense-Thirring normalization")
    print("  treat global angular momentum as boundary/source data")


def case_1_angular_momentum_from_current():
    header("Case 1: Angular momentum from current")

    x, y, z, rho, vx, vy, vz = sp.symbols("x y z rho v_x v_y v_z", real=True)

    r = sp.Matrix([x, y, z])
    j = sp.Matrix([rho*vx, rho*vy, rho*vz])
    ell = sp.simplify(r.cross(j))

    print("Current:")
    print(f"j = {j}")
    print()
    print("Angular momentum density:")
    print("ell = r x j =")
    print(ell)
    print()
    print("Global angular momentum:")
    print()
    print("  J = integral r x j d^3x")
    print()
    print("Interpretation:")
    print("  A rotating source supplies global vector boundary data through J.")

    return ell


def case_2_uniform_rotation_current():
    header("Case 2: Uniform rotation current")

    x, y, z, rho, Omega = sp.symbols("x y z rho Omega", real=True)

    v = sp.Matrix([-Omega*y, Omega*x, 0])
    j = rho * v
    div_j = sp.simplify(sp.diff(j[0], x) + sp.diff(j[1], y) + sp.diff(j[2], z))

    print("Rigid rotation about z:")
    print("v = Omega x r =")
    print(v)
    print()
    print("j = rho v =")
    print(j)
    print()
    print(f"div j = {div_j}")
    print()
    print("For constant rho and Omega, the current is divergence-free.")

    return j, div_j


def case_3_boundary_source_view():
    header("Case 3: Boundary source view")

    J, R, Cb = sp.symbols("J R C_b", positive=True, real=True)

    boundary_flux = Cb * J

    print("For a compact rotating source of radius R:")
    print()
    print("  interior current determines total angular momentum J")
    print("  exterior vector solution should be fixed by boundary data at R")
    print()
    print("Symbolic boundary condition:")
    print()
    print("  vector boundary circulation/flux ~ C_b J")
    print()
    print(f"boundary data = {boundary_flux}")
    print()
    print("C_b is not derived.")

    return boundary_flux


def case_4_far_field_shape():
    header("Case 4: Far-field angular-momentum shape")

    r, J, Cw = sp.symbols("r J C_W", positive=True, real=True)

    BW = Cw * J / r**3

    print("Symbolic far-field curl diagnostic:")
    print()
    print("  B_W ~ C_W J/r^3")
    print()
    print(f"B_W = {BW}")
    print()
    print("Interpretation:")
    print("  J is the only available axial vector for a stationary rotating source.")
    print("  1/r^3 is the expected dipole-like curl falloff.")
    print()
    print("But C_W is missing.")

    return BW


def case_5_zero_mode_boundary_warning():
    header("Case 5: k=0 / boundary warning")

    print("The local projector cannot decide global rotation by itself because:")
    print()
    print("  P_T(k) uses 1/k^2")
    print("  k=0 mode is singular")
    print("  total angular momentum depends on boundary/source integrals")
    print()
    print("Therefore:")
    print()
    print("  local transverse projection handles local current modes")
    print("  global angular momentum must be supplied by boundary/source data")
    print()
    print("This is not failure; it is a boundary problem.")


def case_6_no_gr_matching():
    header("Case 6: No GR matching")

    print("Forbidden at this stage:")
    print()
    print("  set C_W or beta_W to reproduce Lense-Thirring")
    print()
    print("Allowed:")
    print()
    print("  keep C_W symbolic")
    print("  derive C_W from vector action + boundary conditions")
    print("  or declare C_W phenomenological")
    print()
    print("Current status:")
    print()
    print("  source object J: constrained by current")
    print("  far-field shape: constrained")
    print("  coefficient: missing")


def case_7_classification():
    header("Case 7: Classification")

    print("| Item | Status |")
    print("|---|---|")
    print("| angular momentum J = integral r x j d^3x | CONSTRAINED_BY_IDENTITY |")
    print("| uniform rotation current div j = 0 | DERIVED_REDUCED |")
    print("| global rotation as boundary data | CONSTRAINED_BY_IDENTITY |")
    print("| far-field B_W ~ J/r^3 shape | CONSTRAINED_BY_IDENTITY |")
    print("| boundary coefficient C_b | MISSING |")
    print("| far-field coefficient C_W | MISSING |")
    print("| Lense-Thirring normalization | HAND_ASSIGNED if inserted now |")


def case_8_next_tests():
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_vector_boundary_value_problem.py")
    print("   Solve symbolic exterior vector equation with boundary data.")
    print()
    print("2. candidate_kappa_source_law_from_trace_exchange.py")
    print("   Work missing kappa source law.")
    print()
    print("3. candidate_tensor_source_from_exchange_identity.py")
    print("   Work hand-assigned tensor coupling.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_vector_boundary_value_problem.py")


def final_interpretation():
    header("Final interpretation")

    print("The local projection operator handles k != 0 current splitting.")
    print()
    print("Global rotation is different:")
    print()
    print("  J = integral r x j d^3x")
    print()
    print("A compact rotating source should set exterior vector boundary data.")
    print()
    print("The expected symbolic far-field shape is:")
    print()
    print("  B_W ~ C_W J/r^3")
    print()
    print("But C_W is missing.")
    print()
    print("Possible next artifact:")
    print("  candidate_vector_global_rotation_mode.md")
    print()
    print("Possible next script:")
    print("  candidate_vector_boundary_value_problem.py")


def main():
    header("Candidate Vector Global Rotation Mode")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    ell = case_1_angular_momentum_from_current()
    j_rot, div_jrot = case_2_uniform_rotation_current()
    boundary_flux = case_3_boundary_source_view()
    BW = case_4_far_field_shape()
    case_5_zero_mode_boundary_warning()
    case_6_no_gr_matching()
    case_7_classification()
    case_8_next_tests()
    final_interpretation()

    out = ScriptOutput()

    rot_div_zero = is_zero(div_jrot)

    with out.derived_results():
        out.line(
            "uniform rotation current is divergence-free",
            StatusMark.PASS if rot_div_zero else StatusMark.FAIL,
            f"div j = {div_jrot} for rigid rotation j = rho*Omega*(-y, x, 0)",
        )
        out.line(
            "angular momentum density ell = r x j computed",
            StatusMark.PASS,
            "symbolic angular momentum density from current",
        )
        out.line(
            "far-field B_W ~ C_W J/r^3 shape stated",
            StatusMark.PASS,
            "constrained by dimensionality and symmetry; coefficient symbolic",
        )

    with out.governance_assessments():
        out.line(
            "boundary coefficient C_b",
            StatusMark.FAIL,
            "missing; k=0 global mode not resolved by local projector",
        )
        out.line(
            "GR matching forbidden",
            StatusMark.DEFER,
            "C_W and beta_W must not be set to reproduce Lense-Thirring",
        )

    with out.unresolved_obligations():
        out.line(
            "derive global boundary normalization",
            StatusMark.OBLIGATION,
            "open proof obligation recorded",
        )
        out.line(
            "derive vector coefficient alpha_W / K_c",
            StatusMark.OBLIGATION,
            "open proof obligation recorded",
        )


    with archive.open() as ns2:
        # Contentful derivation: uniform rotation current divergence-free
        x, y, z, rho, Omega = sp.symbols("x y z rho Omega", real=True)
        j_sample = rho * sp.Matrix([-Omega*y, Omega*x, sp.Integer(0)])
        div_sample = sp.simplify(
            sp.diff(j_sample[0], x) + sp.diff(j_sample[1], y) + sp.diff(j_sample[2], z)
        )

        ns2.record_derivation(
            derivation_id="uniform_rotation_current_divergence_free",
            inputs=[j_sample],
            output=div_sample,
            method="div(rho*Omega*(-y, x, 0)) for constant rho, Omega",
            status=Status.DERIVED,
            record_kind=RecordKind.SAMPLE_DERIVATION,
            result_type="identity_residual",
            scope="uniform rotation current sample",
        )

        # Proof obligation: global boundary normalization
        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_global_boundary_normalization",
            script_id=SCRIPT_ID,
            title="Derive global boundary normalization",
            status=ObligationStatus.OPEN,
            description=(
                "The global rotation mode requires boundary data C_b that connects "
                "interior angular momentum J to the exterior vector field amplitude. "
                "C_b and C_W are both missing and cannot be set by GR matching."
            ),
        ))

        # Proof obligation: vector coefficient alpha_W/K_c
        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_vector_coefficient_alpha_W_K_c",
            script_id=SCRIPT_ID,
            title="Derive vector coefficient alpha_W / K_c",
            status=ObligationStatus.OPEN,
            description=(
                "The far-field coefficient C_W is ultimately controlled by alpha_W/K_c "
                "and source geometry. alpha_W/K_c remains missing from the vacuum transport action."
            ),
        ))

        # Governance claim: no recovery smuggling for C_W
        ns2.record_claim(ClaimRecord(
            claim_id="no_recovery_smuggling_C_W",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.POLICY_RULE,
            statement=(
                "C_W and C_b must not be chosen to reproduce Lense-Thirring frame "
                "dragging. Matching to GR is a downstream test, not a construction rule "
                "for the global rotation boundary problem."
            ),
            reason_code=ReasonCode.RECOVERY_SELECTED_PARAMETER,
        ))

        # Inventory marker
        ns2.record_derivation(
            derivation_id="vector_global_rotation_mode_marker",
            inputs=[],
            output=sp.Symbol("vector_global_rotation_mode_classified"),
            method="vector_global_rotation_mode_inventory",
            status=Status.DERIVED,
            record_kind=RecordKind.INVENTORY_MARKER,
            is_placeholder=True,
        )

        ns2.write_run_metadata()


if __name__ == "__main__":
    main()
