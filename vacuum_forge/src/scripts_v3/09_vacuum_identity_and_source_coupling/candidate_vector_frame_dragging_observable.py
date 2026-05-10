# Candidate vector frame-dragging observable
#
# Group:
#   09_vacuum_identity_and_source_coupling
#
# Script type:
#   DERIVATION
#
# Purpose
# -------
# The vector-current continuity study found:
#
#   density rho -> scalar A source
#   current j_i = rho v_i -> vector W_i source
#   Delta W_i ~ j_i
#   curl W is a safer diagnostic candidate than raw W_i
#
# This script asks whether curl W can be organized as a frame-dragging /
# precession diagnostic while keeping all coefficients symbolic.
#
# It does NOT insert the GR Lense-Thirring coefficient.
# It does NOT claim the observable is derived.

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
        dependency_id="vector_current_from_continuity_marker",
        upstream_script_id="09_vacuum_identity_and_source_coupling__candidate_vector_current_from_continuity",
        upstream_derivation_id="vector_current_from_continuity_marker",
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


def curl_vec(V, coords):
    x, y, z = coords
    return sp.Matrix([
        sp.diff(V[2], y) - sp.diff(V[1], z),
        sp.diff(V[0], z) - sp.diff(V[2], x),
        sp.diff(V[1], x) - sp.diff(V[0], y),
    ])


def div_vec(V, coords):
    return sp.simplify(sum(sp.diff(V[i], coords[i]) for i in range(3)))


def case_0_problem_statement():
    header("Case 0: Vector frame-dragging observable problem")

    print("Question:")
    print()
    print("  Can curl W be used as a safer frame-dragging diagnostic candidate?")
    print()
    print("Rules:")
    print()
    print("  raw W_i is not automatically observable")
    print("  coefficients remain symbolic")
    print("  do not insert Lense-Thirring normalization by hand")
    print()
    print("Candidate diagnostic:")
    print()
    print("  B_W = curl W")


def case_1_curl_kills_gradient():
    header("Case 1: Curl kills pure-gradient gauge-like piece")

    x, y, z = sp.symbols("x y z", real=True)
    phi = sp.Function("phi")(x, y, z)

    grad_phi = sp.Matrix([sp.diff(phi, x), sp.diff(phi, y), sp.diff(phi, z)])
    curl_grad = sp.simplify(curl_vec(grad_phi, (x, y, z)))

    print("Pure-gradient vector:")
    print("  W = grad phi")
    print()
    print("curl(grad phi) =")
    print(curl_grad)
    print()
    print("Interpretation:")
    print("  If gauge shifts add gradient-like pieces, curl W removes them.")

    return curl_grad


def case_2_rotational_W():
    header("Case 2: Rotational W gives nonzero curl")

    x, y, z, a = sp.symbols("x y z a", real=True)

    W = sp.Matrix([-a*y, a*x, 0])
    BW = sp.simplify(curl_vec(W, (x, y, z)))
    divW = div_vec(W, (x, y, z))

    print("Rotational W:")
    print(W)
    print()
    print("curl W =")
    print(BW)
    print(f"div W = {divW}")
    print()
    print("Interpretation:")
    print("  Rotational vector structure gives a nonzero curl diagnostic.")

    return W, BW


def case_3_current_loop_angular_momentum():
    header("Case 3: Current loop / angular momentum structure")

    x, y, z, rho, vx, vy, vz = sp.symbols("x y z rho v_x v_y v_z", real=True)

    r = sp.Matrix([x, y, z])
    j = sp.Matrix([rho*vx, rho*vy, rho*vz])
    ell = r.cross(j)

    print("Current:")
    print(f"j = {j}")
    print()
    print("Angular momentum density:")
    print("ell = r x j =")
    print(ell)
    print()
    print("Interpretation:")
    print("  A frame-dragging diagnostic sourced by current should reduce globally")
    print("  to an angular-momentum-like source for rotating bodies.")

    return ell


def case_4_symbolic_precession_relation():
    header("Case 4: Symbolic precession relation")

    beta_W = sp.symbols("beta_W", real=True)
    BWx, BWy, BWz = sp.symbols("B_Wx B_Wy B_Wz", real=True)
    BW = sp.Matrix([BWx, BWy, BWz])

    Omega = beta_W * BW

    print("Candidate precession/frame-dragging relation:")
    print()
    print("  Omega_drag = beta_W * B_W")
    print()
    print(f"Omega_drag = {Omega}")
    print()
    print("Status:")
    print("  B_W = curl W is diagnostic candidate")
    print("  beta_W is not derived")
    print("  do not set beta_W from GR yet")

    return BW, Omega


def case_5_dipole_shape():
    header("Case 5: Dipole-like far-field shape")

    r, J, Cw = sp.symbols("r J C_W", positive=True, real=True)

    BW_far = Cw * J / r**3

    print("Expected rotational far-field diagnostic shape:")
    print()
    print("  B_W ~ C_W J / r^3")
    print()
    print(f"B_W_far = {BW_far}")
    print()
    print("Interpretation:")
    print("  Continuity/current gives angular momentum J as source.")
    print("  A dipole-like vector field suggests 1/r^3 curl falloff.")
    print("  Coefficient C_W remains symbolic.")

    return BW_far


def case_6_observable_safety():
    header("Case 6: Observable safety classification")

    print("| Quantity | Status |")
    print("|---|---|")
    print("| raw W_i | RISK / gauge-sensitive |")
    print("| grad piece of W_i | nonphysical candidate |")
    print("| curl W | CONSTRAINED_BY_IDENTITY diagnostic candidate |")
    print("| Omega_drag = beta_W curl W | CONSTRAINED_BY_IDENTITY, beta_W missing |")
    print("| Lense-Thirring coefficient | HAND_ASSIGNED if inserted now |")


def case_7_failure_controls():
    header("Case 7: Failure controls")

    print("This observable reconstruction fails if:")
    print()
    print("1. raw W_i is treated as measured directly.")
    print("2. beta_W is chosen only to match GR.")
    print("3. curl W does not connect to a physical precession observable.")
    print("4. the current source j_i is disconnected from continuity.")
    print("5. vector radiation is accidentally introduced without suppression or evidence.")


def final_interpretation():
    header("Final interpretation")

    print("The safer vector observable candidate is:")
    print()
    print("  B_W = curl W")
    print()
    print("because curl removes pure-gradient gauge-like pieces.")
    print()
    print("A symbolic frame-dragging relation is:")
    print()
    print("  Omega_drag = beta_W B_W")
    print()
    print("But beta_W and the far-field coefficient are missing.")
    print()
    print("Possible next artifact:")
    print("  candidate_vector_frame_dragging_observable.md")
    print()
    print("Possible next script:")
    print("  candidate_vector_coefficient_normalization.py")


def main():
    header("Candidate Vector Frame-Dragging Observable")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    curl_grad = case_1_curl_kills_gradient()
    W_rot, BW_rot = case_2_rotational_W()
    ell = case_3_current_loop_angular_momentum()
    BW_sym, Omega_sym = case_4_symbolic_precession_relation()
    BW_far = case_5_dipole_shape()
    case_6_observable_safety()
    case_7_failure_controls()
    final_interpretation()

    out = ScriptOutput()

    curl_grad_zero = all(is_zero(e) for e in curl_grad)
    curl_rot_nonzero = not all(is_zero(e) for e in BW_rot)

    with out.derived_results():
        out.line(
            "curl(grad phi) = 0 identity verified",
            StatusMark.PASS if curl_grad_zero else StatusMark.FAIL,
            "curl removes pure-gradient gauge pieces",
        )
        out.line(
            "rotational W gives nonzero curl diagnostic",
            StatusMark.PASS if curl_rot_nonzero else StatusMark.FAIL,
            "B_W = curl W is nonzero for rotational W = a(-y, x, 0)",
        )
        out.line(
            "angular momentum density l = r x j computed",
            StatusMark.PASS,
            "symbolic angular momentum density from current",
        )

    with out.governance_assessments():
        out.line(
            "beta_W observable coupling",
            StatusMark.DEFER,
            "beta_W not derived; Lense-Thirring matching forbidden",
        )
        out.line(
            "raw W_i is gauge-sensitive",
            StatusMark.DEFER,
            "only B_W = curl W is a safe observable candidate",
        )

    with out.unresolved_obligations():
        out.line(
            "derive beta_W observable coupling",
            StatusMark.OBLIGATION,
            "open proof obligation recorded",
        )
        out.line(
            "derive vector coefficient alpha_W / K_c",
            StatusMark.OBLIGATION,
            "open proof obligation recorded",
        )

    out.print()

    with archive.open() as ns2:
        # Contentful derivation: curl(grad phi) = 0
        x, y, z = sp.symbols("x y z", real=True)
        phi = sp.Function("phi")(x, y, z)
        grad_phi = sp.Matrix([sp.diff(phi, x), sp.diff(phi, y), sp.diff(phi, z)])
        curl_grad_expr = sp.simplify(curl_vec(grad_phi, (x, y, z)))

        ns2.record_derivation(
            derivation_id="curl_grad_phi_zero_identity",
            inputs=[grad_phi],
            output=curl_grad_expr,
            method="curl(grad phi) computed symbolically",
            status=Status.DERIVED,
            record_kind=RecordKind.DERIVATION,
            result_type="identity_residual",
        )

        # Sample derivation: rotational W curl
        a = sp.symbols("a", real=True)
        W_sample = sp.Matrix([-a*y, a*x, sp.Integer(0)])
        BW_sample = sp.simplify(curl_vec(W_sample, (x, y, z)))

        ns2.record_derivation(
            derivation_id="rotational_W_curl_sample",
            inputs=[W_sample],
            output=BW_sample,
            method="curl W for W = a(-y, x, 0)",
            status=Status.DERIVED,
            record_kind=RecordKind.SAMPLE_DERIVATION,
            result_type="diagnostic_quantity",
            scope="rotational W sample",
        )

        # Proof obligation: beta_W observable coupling
        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_vector_beta_W_coupling",
            script_id=SCRIPT_ID,
            title="Derive beta_W observable coupling",
            status=ObligationStatus.OPEN,
            description=(
                "The precession relation Omega_drag = beta_W B_W requires beta_W to be "
                "derived from observable/precession coupling, not matched to Lense-Thirring. "
                "beta_W remains missing."
            ),
        ))

        # Proof obligation: vector coefficient alpha_W/K_c
        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_vector_coefficient_alpha_W_K_c",
            script_id=SCRIPT_ID,
            title="Derive vector coefficient alpha_W / K_c",
            status=ObligationStatus.OPEN,
            description=(
                "The far-field coefficient C_W and the vector action ratio alpha_W/K_c "
                "are both missing. They must be derived from the vacuum transport action."
            ),
        ))

        # Governance claim: no recovery smuggling for beta_W
        ns2.record_claim(ClaimRecord(
            claim_id="no_recovery_smuggling_beta_W",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.POLICY_RULE,
            statement=(
                "beta_W must not be chosen to reproduce the Lense-Thirring precession "
                "rate. GR precession recovery is a downstream test, not a construction "
                "rule for the vector observable coupling."
            ),
            reason_code=ReasonCode.RECOVERY_SELECTED_PARAMETER,
        ))

        # Inventory marker
        ns2.record_derivation(
            derivation_id="vector_frame_dragging_observable_marker",
            inputs=[],
            output=sp.Symbol("vector_frame_dragging_observable_inventory"),
            method="vector_frame_dragging_observable_inventory",
            status=Status.DERIVED,
            record_kind=RecordKind.INVENTORY_MARKER,
            is_placeholder=True,
        )

        ns2.write_run_metadata()


if __name__ == "__main__":
    main()
