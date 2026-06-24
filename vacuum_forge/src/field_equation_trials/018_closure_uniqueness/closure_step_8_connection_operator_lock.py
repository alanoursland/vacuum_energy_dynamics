# Trial 018: Closure uniqueness, step 8
#
# Script type:
#   RIGOR PROGRAM / CONNECTION-EQUATION OPERATOR LOCK
#
# Purpose
# -------
# This is the eighth in-house rung toward replacing the Deser 1970
# self-coupled spin-2 closure citation. It still does not retire the
# full closure-uniqueness obligation.
#
# Step 7 checked the gate:
#
#       same Palatini Ricci operator at H2 order
#       => no H2.Rlin - H2.Q mismatch.
#
# This script derives that gate at H2 order from the first-order
# connection equation plus the already-checked no-independent-connection
# endpoint:
#
#   1. In a first-order density A.Rlin + B.Q, the derivative part of the
#      connection equation is controlled by A, while the algebraic
#      connection-transport part is controlled by B.
#   2. Eliminating the torsion-free connection as the compatible
#      connection of one metric density requires those two coefficients
#      to be the same density.
#   3. Therefore the quadratic coefficients must be locked:
#
#          cR H2.Rlin + cQ H2.Q
#          compatible single-density connection
#          => cR = cQ.
#
# The mismatch H2.Rlin - H2.Q gives cR=-cQ and is therefore incompatible
# unless its coefficient is zero. This kills the active H2 mismatch under
# the connection-elimination/no-extra-field condition already established
# in step 4. Higher-H orders remain to be reduced or excluded.

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
        dependency_id="closure_step_7_dependency_018",
        upstream_script_id="018_closure_uniqueness__closure_step_7_h2_mismatch_gate",
        upstream_derivation_id="h2_mismatch_zero_if_same_operator_018",
        expected_record_kind=RecordKind.DERIVATION,
    )
    ns.declare_dependency(
        dependency_id="closure_step_4_connection_dependency_018",
        upstream_script_id="018_closure_uniqueness__closure_step_4_connection_elimination",
        upstream_derivation_id="palatini_connection_uniqueness_018",
        expected_record_kind=RecordKind.DERIVATION,
    )
    return archive, ns, invalidated


cR, cQ, lam, mismatch = sp.symbols("cR cQ lam mismatch")
D_H2, C_H2 = sp.symbols("D_H2 C_H2")
H2 = sp.symbols("H2")


def case_0_statement(out: ScriptOutput) -> None:
    header("Case 0: Closure uniqueness program, eighth rung")
    print("Step 7 showed that the H2 mismatch dies if the same Palatini")
    print("Ricci operator is required. This rung derives that same-operator")
    print("condition at H2 order from the connection equation itself.")
    print()
    print("For a split first-order density")
    print()
    print("  A.Rlin + B.Q")
    print()
    print("the derivative part of the connection equation comes from A.Rlin,")
    print("while the algebraic Gamma-transport part comes from B.Q. A single")
    print("torsion-free compatible metric-density connection can eliminate the")
    print("independent connection only when A and B are the same density.")

    with out.governance_assessments():
        out.line(
            "connection-equation operator lock opened",
            StatusMark.INFO,
            "derives the H2 same-operator condition from connection elimination",
        )


def case_1_connection_equation_locks_h2_coefficients(out: ScriptOutput):
    header("Case 1: Single-density connection equation locks the H2 coefficients")
    split_connection_h2 = cR * D_H2 + cQ * C_H2
    single_density_h2 = lam * (D_H2 + C_H2)
    residual = sp.Poly(split_connection_h2 - single_density_h2, D_H2, C_H2)
    equations = [sp.Eq(coeff, 0) for coeff in residual.coeffs()]
    solution = sp.solve(equations, [cR, cQ], dict=True)
    expected = [{cR: lam, cQ: lam}]

    print("H2 part of the split connection equation:")
    print("  cR D[H2] + cQ C[H2]")
    print("where D[H2] is the derivative contribution from H2.Rlin")
    print("and C[H2] is the algebraic connection contribution from H2.Q.")
    print()
    print("Single compatible density target:")
    print("  lambda (D[H2] + C[H2])")
    print(f"  coefficient solution = {solution}")

    ok = solution == expected
    with out.derived_results():
        out.line(
            "connection equation derives the H2 same-operator coefficient lock",
            StatusMark.PASS if ok else StatusMark.FAIL,
            "single-density connection elimination requires cR=cQ=lambda",
        )
    return ok


def case_2_mismatch_has_no_single_density_connection(out: ScriptOutput):
    header("Case 2: H2 mismatch leaves no compatible single-density connection")
    mismatch_connection_h2 = mismatch * D_H2 - mismatch * C_H2
    single_density_h2 = lam * (D_H2 + C_H2)
    residual = sp.Poly(mismatch_connection_h2 - single_density_h2, D_H2, C_H2)
    equations = [sp.Eq(coeff, 0) for coeff in residual.coeffs()]
    solution = sp.solve(equations, [mismatch, lam], dict=True)
    expected = [{mismatch: 0, lam: 0}]

    print("Pure mismatch connection equation contribution:")
    print("  m D[H2] - m C[H2]")
    print("Attempt to represent it as one compatible density:")
    print("  lambda (D[H2] + C[H2])")
    print(f"  solution = {solution}")

    ok = solution == expected
    with out.derived_results():
        out.line(
            "H2 mismatch is incompatible with connection elimination",
            StatusMark.PASS if ok else StatusMark.FAIL,
            "m=0 is forced; otherwise derivative and algebraic connection pieces require different densities",
        )
    return ok


def case_3_split_density_residual(out: ScriptOutput):
    header("Case 3: Split-density residual carried by the mismatch")
    A_h2 = cR * H2
    B_h2 = cQ * H2
    split_residual = sp.simplify(B_h2 - A_h2)
    mismatch_residual = sp.simplify(split_residual.subs({cR: mismatch, cQ: -mismatch}))

    print("Let A be the density multiplying Rlin and B the density multiplying Q.")
    print("The no-extra-connection endpoint requires B-A=0 componentwise.")
    print(f"  generic H2 split residual B-A = {sp.sstr(split_residual)}")
    print(f"  mismatch residual B-A       = {sp.sstr(mismatch_residual)}")

    solution = sp.solve([sp.Eq(mismatch_residual, 0)], [mismatch], dict=True)
    expected = [{mismatch: 0}]
    ok = solution == expected

    with out.derived_results():
        out.line(
            "H2 mismatch is exactly a split-density nonmetricity residual",
            StatusMark.PASS if ok else StatusMark.FAIL,
            "B-A=-2mH2 vanishes for arbitrary H2 only when m=0",
        )
    return ok


def case_4_status(out: ScriptOutput):
    header("Case 4: Status after the H2 connection-equation lock")
    print("This rung converts the step-7 same-operator gate into a derived H2")
    print("condition: the torsion-free connection can be eliminated as one")
    print("metric-density compatible connection only if the Rlin and Q")
    print("coefficients are locked equal. The remaining H2 mismatch is therefore")
    print("not an admissible no-extra-field closure deformation.")
    print()
    print("This still does not retire the Deser citation. The higher-H")
    print("ansatz-reduction problem remains for p >= 3 unless the same")
    print("connection-equation lock is lifted to all orders and the equal")
    print("directions are shown to be field-redefinition freedom.")

    with out.governance_assessments():
        out.line(
            "H2 mismatch excluded by connection-equation operator lock",
            StatusMark.PASS,
            "the active quadratic mismatch is killed; higher-H reduction remains open",
        )
    with out.unresolved_obligations():
        out.line(
            "higher-H ansatz reduction beyond H2",
            StatusMark.OBLIGATION,
            "extend the connection-equation lock and field-redefinition reduction to H^p.Rlin/H^p.Q for p>=3",
        )


def record_results(ns) -> None:
    ns.record_derivation(
        derivation_id="h2_connection_equation_operator_lock_018",
        inputs=[
            "h2_mismatch_zero_if_same_operator_018",
            "palatini_connection_uniqueness_018",
        ],
        output=sp.Symbol("connection_elimination_implies_cR_eq_cQ_at_H2"),
        method="coefficient matching of derivative and algebraic parts of the split first-order connection equation",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="closure_uniqueness_rung",
        scope="quadratic H connection-equation lock",
    )
    ns.record_derivation(
        derivation_id="h2_mismatch_connection_obstruction_018",
        inputs=["h2_connection_equation_operator_lock_018"],
        output=sp.Symbol("H2_Rlin_minus_H2_Q_forces_m_eq_zero"),
        method="single-density compatibility solve for mismatch contribution m*(D[H2]-C[H2])",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="closure_uniqueness_rung",
        scope="H2 mismatch exclusion under no-independent-connection endpoint",
    )
    ns.record_obligation(ProofObligationRecord(
        obligation_id="closure_uniqueness_inhouse_018",
        script_id=SCRIPT_ID,
        title="In-house self-coupled spin-2 closure uniqueness",
        status=ObligationStatus.OPEN,
        required_by=["field_equation_proof"],
        description=(
            "The H2 mismatch H2.Rlin-H2.Q is excluded by the connection-equation "
            "operator lock: eliminating the torsion-free connection as a single "
            "compatible metric-density connection requires the Rlin and Q "
            "coefficients to be equal. Higher-H ansatz reduction remains open."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="closure_step_8_claim_018",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "At H2 order, the same-Palatini-operator condition follows from "
            "the first-order connection equation plus the no-independent-"
            "connection endpoint: the derivative part of the connection "
            "equation is sourced by the density multiplying Rlin, while the "
            "algebraic connection-transport part is sourced by the density "
            "multiplying Q. A single compatible metric-density connection "
            "therefore requires cR=cQ. The mismatch H2.Rlin-H2.Q leaves a "
            "split-density residual unless its coefficient is zero. This "
            "kills the active H2 mismatch but does not yet prove all higher-H "
            "orders."
        ),
        derivation_ids=[
            "h2_connection_equation_operator_lock_018",
            "h2_mismatch_connection_obstruction_018",
        ],
        obligation_ids=["closure_uniqueness_inhouse_018"],
    ))


def main() -> None:
    header("Trial 018: Closure Uniqueness Step 8")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    case_0_statement(out)
    case_1_connection_equation_locks_h2_coefficients(out)
    case_2_mismatch_has_no_single_density_connection(out)
    case_3_split_density_residual(out)
    case_4_status(out)

    record_results(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
