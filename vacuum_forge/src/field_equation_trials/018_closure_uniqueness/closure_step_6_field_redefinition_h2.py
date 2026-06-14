# Trial 018: Closure uniqueness, step 6
#
# Script type:
#   RIGOR PROGRAM / FIELD-REDEFINITION WITNESS
#
# Purpose
# -------
# This is the sixth in-house rung toward replacing the Deser 1970
# self-coupled spin-2 closure citation. It still does not retire the
# full closure-uniqueness obligation.
#
# Step 5 isolated the remaining ansatz-reduction target to higher-H
# two-derivative deformations, starting with H2.Rlin and H2.Q.
#
# This script checks the first reduction:
#
#   A nonlinear redefinition of the densitized inverse-metric
#   perturbation,
#
#       K = H + a H2,
#
#   inside the Palatini replacement produces the locked pair
#
#       a (H2.Rlin + H2.Q).
#
# Therefore the equal-coefficient H2 direction is variable choice, not a
# new closure. At quadratic order in H, only the coefficient mismatch
# direction
#
#       H2.Rlin - H2.Q
#
# remains genuinely non-Palatini and must be excluded by a later
# gauge/conservation consistency check or shown to be boundary.

from pathlib import Path

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    ClaimRecord,
    ClaimTier,
    GovernanceStatus,
    ObligationStatus,
    ProofObligationRecord,
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


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="closure_step_5_dependency_018",
        upstream_script_id="018_closure_uniqueness__closure_step_5_ansatz_reduction_gate",
        upstream_derivation_id="palatini_ansatz_reduction_gate_018",
        expected_record_kind=RecordKind.DERIVATION,
    )
    return archive, ns, invalidated


a, cR, cQ, u, v = sp.symbols("a cR cQ u v")
R0, Q0, HR, HQ, H2R, H2Q = sp.symbols("eta_Rlin eta_Q H_Rlin H_Q H2_Rlin H2_Q")

PALATINI_H = R0 + Q0 + HR + HQ
PALATINI_K_WITH_H2 = R0 + Q0 + HR + HQ + a * H2R + a * H2Q


def case_0_statement(out: ScriptOutput) -> None:
    header("Case 0: Closure uniqueness program, sixth rung")
    print("Step 5 isolated higher-H two-derivative deformations as the")
    print("remaining ansatz-reduction target. This script checks which H2")
    print("direction is just a nonlinear variable choice:")
    print()
    print("  K = H + a H2")
    print()
    print("inserted into the Palatini replacement.")

    with out.governance_assessments():
        out.line(
            "H2 field-redefinition witness opened",
            StatusMark.INFO,
            "removable direction only; full higher-H exclusion remains open",
        )


def case_1_redefinition_generates_locked_pair(out: ScriptOutput):
    header("Case 1: Nonlinear field redefinition generates H2.Rlin + H2.Q")
    generated = sp.simplify(PALATINI_K_WITH_H2 - PALATINI_H)
    target = a * (H2R + H2Q)
    residual = sp.simplify(generated - target)

    print("Palatini with H:")
    print("  eta.Rlin + eta.Q + H.Rlin + H.Q")
    print("Palatini with K = H + a H2:")
    print("  eta.Rlin + eta.Q + H.Rlin + H.Q + a H2.Rlin + a H2.Q")
    print(f"  generated residual vs a(H2.Rlin + H2.Q) = {sp.sstr(residual)}")

    ok = is_zero(residual)
    with out.derived_results():
        out.line(
            "equal-coefficient H2 derivative pair is a field redefinition",
            StatusMark.PASS if ok else StatusMark.FAIL,
            "K=H+aH2 generates a(H2.Rlin+H2.Q), so that direction is not new physics",
        )
    return ok


def case_2_decompose_general_h2_deformation(out: ScriptOutput):
    header("Case 2: General H2 deformation splits into removable and residual parts")
    deformation = cR * H2R + cQ * H2Q
    removable = u * (H2R + H2Q)
    residual_direction = v * (H2R - H2Q)
    equations_poly = sp.Poly(deformation - removable - residual_direction, H2R, H2Q)
    equations = [sp.Eq(coeff, 0) for coeff in equations_poly.coeffs()]
    solution = sp.solve(equations, [u, v], dict=True)
    expected = [{u: (cQ + cR) / 2, v: (-cQ + cR) / 2}]

    print("General H2 deformation:")
    print("  cR H2.Rlin + cQ H2.Q")
    print("Decomposition basis:")
    print("  u(H2.Rlin + H2.Q) + v(H2.Rlin - H2.Q)")
    print(f"  solution = {solution}")

    ok = solution == expected
    with out.derived_results():
        out.line(
            "H2 deformation decomposes into redefinition plus mismatch residual",
            StatusMark.PASS if ok else StatusMark.FAIL,
            "u=(cR+cQ)/2 is removable; v=(cR-cQ)/2 is the non-Palatini mismatch",
        )
    return ok


def case_3_remaining_h2_target(out: ScriptOutput):
    header("Case 3: Remaining H2 target")
    print("After allowing nonlinear metric-density field redefinitions:")
    print()
    print("  removable:  H2.Rlin + H2.Q")
    print("  remaining:  H2.Rlin - H2.Q")
    print()
    print("The next proof step must show the mismatch direction is not an")
    print("admissible self-coupled spin-2 deformation: either it is a boundary")
    print("term after fuller reduction, or it violates the gauge/conservation")
    print("identity that started the bootstrap.")

    with out.unresolved_obligations():
        out.line(
            "H2 mismatch exclusion",
            StatusMark.OBLIGATION,
            "exclude or reduce H2.Rlin-H2.Q under gauge/conservation consistency",
        )


def record_results(ns) -> None:
    ns.record_derivation(
        derivation_id="h2_field_redefinition_locked_pair_018",
        inputs=["palatini_ansatz_reduction_gate_018"],
        output=sp.Symbol("K_eq_H_plus_aH2_generates_a_H2Rlin_plus_a_H2Q"),
        method="symbolic expansion of Palatini replacement under K=H+aH2",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="closure_uniqueness_rung",
        scope="quadratic field-redefinition witness; not full ansatz reduction",
    )
    ns.record_derivation(
        derivation_id="h2_deformation_residual_split_018",
        inputs=["h2_field_redefinition_locked_pair_018"],
        output=sp.Symbol("h2_general_deformation_splits_into_removable_and_mismatch"),
        method="coefficient matching in basis {H2.Rlin+H2.Q, H2.Rlin-H2.Q}",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="closure_uniqueness_rung",
        scope="quadratic H ansatz-reduction audit",
    )
    ns.record_obligation(ProofObligationRecord(
        obligation_id="closure_uniqueness_inhouse_018",
        script_id=SCRIPT_ID,
        title="In-house self-coupled spin-2 closure uniqueness",
        status=ObligationStatus.OPEN,
        required_by=["field_equation_proof"],
        description=(
            "At H2 order the equal-coefficient pair H2.Rlin+H2.Q is removable "
            "by a nonlinear metric-density field redefinition. The remaining "
            "target is the mismatch H2.Rlin-H2.Q, which must be excluded or "
            "reduced by a later gauge/conservation consistency check."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="closure_step_6_claim_018",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "The quadratic higher-H ansatz-reduction problem narrows further: "
            "the equal-coefficient pair H2.Rlin+H2.Q is generated by the "
            "nonlinear field redefinition K=H+aH2 and is therefore removable "
            "variable choice. The non-Palatini mismatch H2.Rlin-H2.Q remains "
            "the active H2 target."
        ),
        derivation_ids=[
            "h2_field_redefinition_locked_pair_018",
            "h2_deformation_residual_split_018",
        ],
        obligation_ids=["closure_uniqueness_inhouse_018"],
    ))


def main() -> None:
    header("Trial 018: Closure Uniqueness Step 6")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    case_0_statement(out)
    case_1_redefinition_generates_locked_pair(out)
    case_2_decompose_general_h2_deformation(out)
    case_3_remaining_h2_target(out)

    record_results(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
