# Trial 018: Closure uniqueness, step 7
#
# Script type:
#   RIGOR PROGRAM / H2 MISMATCH GATE
#
# Purpose
# -------
# This is the seventh in-house rung toward replacing the Deser 1970
# self-coupled spin-2 closure citation. It still does not retire the
# full closure-uniqueness obligation.
#
# Step 6 reduced the quadratic higher-H ambiguity to one mismatch:
#
#       H2.Rlin - H2.Q.
#
# This script checks exactly what excludes that mismatch. If the
# self-coupled closure is required to keep coupling each metric-density
# coefficient to the same Palatini Ricci object,
#
#       Rlin + Q,
#
# then the H2 coefficients must be locked equal and the mismatch
# coefficient is zero. If that same-operator condition is not accepted,
# this script records the precise remaining lemma instead of claiming
# the Deser replacement is complete.

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
        dependency_id="closure_step_6_dependency_018",
        upstream_script_id="018_closure_uniqueness__closure_step_6_field_redefinition_h2",
        upstream_derivation_id="h2_deformation_residual_split_018",
        expected_record_kind=RecordKind.DERIVATION,
    )
    return archive, ns, invalidated


cR, cQ, lam, mismatch = sp.symbols("cR cQ lam mismatch")
H2R, H2Q = sp.symbols("H2_Rlin H2_Q")


def case_0_statement(out: ScriptOutput) -> None:
    header("Case 0: Closure uniqueness program, seventh rung")
    print("Step 6 reduced the H2 ambiguity to the mismatch")
    print()
    print("  H2.Rlin - H2.Q")
    print()
    print("This script checks the same-operator gate: if every metric-density")
    print("coefficient couples to the same Palatini Ricci object Rlin + Q,")
    print("then H2.Rlin and H2.Q must have equal coefficients.")

    with out.governance_assessments():
        out.line(
            "H2 mismatch gate opened",
            StatusMark.INFO,
            "conditional exclusion under same-Palatini-operator closure",
        )


def case_1_same_operator_locks_coefficients(out: ScriptOutput):
    header("Case 1: Same Palatini operator locks the H2 coefficients")
    general_h2 = cR * H2R + cQ * H2Q
    same_operator_h2 = lam * (H2R + H2Q)
    residual = sp.Poly(general_h2 - same_operator_h2, H2R, H2Q)
    equations = [sp.Eq(coeff, 0) for coeff in residual.coeffs()]
    solution = sp.solve(equations, [cR, cQ], dict=True)
    expected = [{cR: lam, cQ: lam}]

    print("General H2 deformation:")
    print("  cR H2.Rlin + cQ H2.Q")
    print("Same-operator H2 target:")
    print("  lambda H2.(Rlin + Q)")
    print(f"  coefficient solution = {solution}")

    ok = solution == expected
    with out.derived_results():
        out.line(
            "same-operator condition locks H2.Rlin and H2.Q coefficients",
            StatusMark.PASS if ok else StatusMark.FAIL,
            "cR=cQ=lambda; the mismatch direction is not compatible with same Ricci coupling",
        )
    return ok


def case_2_mismatch_coefficient_forced_zero(out: ScriptOutput):
    header("Case 2: Mismatch coefficient is zero under same-operator closure")
    deformation = lam * (H2R + H2Q) + mismatch * (H2R - H2Q)
    same_operator_h2 = lam * (H2R + H2Q)
    residual = sp.Poly(deformation - same_operator_h2, H2R, H2Q)
    equations = [sp.Eq(coeff, 0) for coeff in residual.coeffs()]
    solution = sp.solve(equations, [mismatch], dict=True)
    expected = [{mismatch: 0}]

    print("Decompose H2 deformation into:")
    print("  lambda(H2.Rlin + H2.Q) + m(H2.Rlin - H2.Q)")
    print("Require same-operator form:")
    print("  lambda(H2.Rlin + H2.Q)")
    print(f"  mismatch solution = {solution}")

    ok = solution == expected
    with out.derived_results():
        out.line(
            "H2 mismatch vanishes under same-operator closure",
            StatusMark.PASS if ok else StatusMark.FAIL,
            "m=0 is forced if the deformation must remain H2 times the Palatini Ricci object",
        )
    return ok


def case_3_status(out: ScriptOutput):
    header("Case 3: Status of the remaining lemma")
    print("This rung proves a conditional exclusion:")
    print()
    print("  same Palatini Ricci operator at H2 order")
    print("  => no H2.Rlin - H2.Q mismatch.")
    print()
    print("To retire Deser in-house, the proof still needs one of:")
    print()
    print("  A. derive the same-operator condition from relabeling gauge")
    print("     consistency plus universal self-coupling, or")
    print("  B. directly show the mismatch violates the conservation identity.")

    with out.governance_assessments():
        out.line(
            "H2 mismatch conditionally excluded",
            StatusMark.INFO,
            "same-operator gate is checked; deriving that gate remains the open lemma",
        )
    with out.unresolved_obligations():
        out.line(
            "derive same-operator closure condition or directly kill mismatch",
            StatusMark.OBLIGATION,
            "prove H2 mismatch violates gauge/conservation, rather than assuming same-Palatini-operator form",
        )


def record_results(ns) -> None:
    ns.record_derivation(
        derivation_id="h2_same_operator_coefficient_lock_018",
        inputs=["h2_deformation_residual_split_018"],
        output=sp.Symbol("same_operator_implies_cR_eq_cQ"),
        method="coefficient matching against lambda*H2*(Rlin+Q)",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="closure_uniqueness_rung",
        scope="conditional H2 mismatch gate",
    )
    ns.record_derivation(
        derivation_id="h2_mismatch_zero_if_same_operator_018",
        inputs=["h2_same_operator_coefficient_lock_018"],
        output=sp.Symbol("mismatch_coefficient_eq_zero_under_same_operator"),
        method="coefficient matching in basis {H2.Rlin+H2.Q, H2.Rlin-H2.Q}",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="closure_uniqueness_rung",
        scope="conditional H2 mismatch gate",
    )
    ns.record_obligation(ProofObligationRecord(
        obligation_id="closure_uniqueness_inhouse_018",
        script_id=SCRIPT_ID,
        title="In-house self-coupled spin-2 closure uniqueness",
        status=ObligationStatus.OPEN,
        required_by=["field_equation_proof"],
        description=(
            "The H2 mismatch is excluded if the same-Palatini-Ricci-operator "
            "condition is derived. That condition has been checked as a gate "
            "but not yet derived from gauge/conservation consistency."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="closure_step_7_claim_018",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "At H2 order, the remaining mismatch H2.Rlin-H2.Q is forbidden "
            "provided the closure must keep coupling to the same Palatini "
            "Ricci object Rlin+Q. The forge check locks cR=cQ and forces "
            "the mismatch coefficient to zero under that condition. The "
            "remaining obligation is to derive the same-operator condition "
            "from gauge/conservation consistency or directly kill the mismatch."
        ),
        derivation_ids=[
            "h2_same_operator_coefficient_lock_018",
            "h2_mismatch_zero_if_same_operator_018",
        ],
        obligation_ids=["closure_uniqueness_inhouse_018"],
    ))


def main() -> None:
    header("Trial 018: Closure Uniqueness Step 7")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    case_0_statement(out)
    case_1_same_operator_locks_coefficients(out)
    case_2_mismatch_coefficient_forced_zero(out)
    case_3_status(out)

    record_results(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
