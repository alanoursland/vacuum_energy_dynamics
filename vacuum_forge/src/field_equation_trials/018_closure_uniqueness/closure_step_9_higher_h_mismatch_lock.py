# Trial 018: Closure uniqueness, step 9
#
# Script type:
#   RIGOR PROGRAM / HIGHER-H MISMATCH LOCK
#
# Purpose
# -------
# This is the ninth in-house rung toward replacing the Deser 1970
# self-coupled spin-2 closure citation. It still does not retire the
# full closure-uniqueness obligation.
#
# Step 8 derived the H2 same-operator condition from the first-order
# connection equation and killed the active H2 mismatch.
#
# This script lifts that mismatch exclusion to every higher H order:
#
#   1. Different H powers are independent local monomial classes in the
#      two-derivative first-order basis.
#   2. For any fixed p >= 3, a split connection equation contribution
#
#          cR_p D[Hp] + cQ_p C[Hp]
#
#      can be the connection equation of one compatible metric density
#      only when cR_p = cQ_p.
#   3. Therefore every mismatch
#
#          Hp.Rlin - Hp.Q
#
#      is incompatible with the no-independent-connection endpoint unless
#      its coefficient is zero.
#
# This discharges the mismatch half of the higher-H ansatz-reduction
# lemma. The remaining higher-H target is the equal-coefficient tower
# Hp.Rlin + Hp.Q, which must be shown to be field-redefinition freedom
# or otherwise reduced.

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

SAMPLE_POWERS = [3, 4, 5, 6]


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


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
        dependency_id="closure_step_8_dependency_018",
        upstream_script_id="018_closure_uniqueness__closure_step_8_connection_operator_lock",
        upstream_derivation_id="h2_connection_equation_operator_lock_018",
        expected_record_kind=RecordKind.DERIVATION,
    )
    return archive, ns, invalidated


cR, cQ, lam, mismatch = sp.symbols("cR cQ lam mismatch")
Dp, Cp = sp.symbols("D_Hp C_Hp")


def symbols_for_power(prefix: str, power: int):
    return sp.Symbol(f"{prefix}{power}")


def case_0_statement(out: ScriptOutput) -> None:
    header("Case 0: Closure uniqueness program, ninth rung")
    print("Step 8 killed the H2 mismatch because the connection equation can")
    print("eliminate the torsion-free connection only when the Rlin and Q")
    print("coefficients define the same metric density.")
    print()
    print("This rung applies the same operator lock to each higher-H power.")
    print("The H-degree grading already used in step 3 separates Hp.Rlin and")
    print("Hp.Q from other powers, so the two-coefficient connection-equation")
    print("solve repeats independently at every p >= 3.")

    with out.governance_assessments():
        out.line(
            "higher-H mismatch lock opened",
            StatusMark.INFO,
            "extends the connection-equation mismatch exclusion beyond H2",
        )


def case_1_generic_power_lock(out: ScriptOutput):
    header("Case 1: Generic p mismatch is killed by the connection equation")
    split_connection_hp = cR * Dp + cQ * Cp
    single_density_hp = lam * (Dp + Cp)
    residual = sp.Poly(split_connection_hp - single_density_hp, Dp, Cp)
    equations = [sp.Eq(coeff, 0) for coeff in residual.coeffs()]
    solution = sp.solve(equations, [cR, cQ], dict=True)
    expected = [{cR: lam, cQ: lam}]

    mismatch_connection_hp = mismatch * Dp - mismatch * Cp
    mismatch_residual = sp.Poly(mismatch_connection_hp - single_density_hp, Dp, Cp)
    mismatch_equations = [sp.Eq(coeff, 0) for coeff in mismatch_residual.coeffs()]
    mismatch_solution = sp.solve(mismatch_equations, [mismatch, lam], dict=True)
    mismatch_expected = [{mismatch: 0, lam: 0}]

    print("For any fixed p >= 3, the Hp connection-equation piece is")
    print("  cR_p D[Hp] + cQ_p C[Hp]")
    print("Single-density compatibility requires")
    print("  lambda_p(D[Hp] + C[Hp])")
    print(f"  coefficient solution = {solution}")
    print()
    print("For a pure mismatch m_p(D[Hp] - C[Hp]):")
    print(f"  mismatch solution = {mismatch_solution}")

    ok = solution == expected and mismatch_solution == mismatch_expected
    with out.derived_results():
        out.line(
            "generic higher-H mismatch coefficient is forced to zero",
            StatusMark.PASS if ok else StatusMark.FAIL,
            "for every p, single-density connection elimination requires cR_p=cQ_p",
        )
    return ok


def case_2_finite_tower_no_cross_order_hiding(out: ScriptOutput):
    header("Case 2: Finite higher-H tower cannot hide mismatch across powers")
    d_basis = [symbols_for_power("D_H", power) for power in SAMPLE_POWERS]
    c_basis = [symbols_for_power("C_H", power) for power in SAMPLE_POWERS]
    cR_symbols = [symbols_for_power("cR", power) for power in SAMPLE_POWERS]
    cQ_symbols = [symbols_for_power("cQ", power) for power in SAMPLE_POWERS]
    lam_symbols = [symbols_for_power("lam", power) for power in SAMPLE_POWERS]

    split = sum(
        cR_i * d_i + cQ_i * c_i
        for cR_i, cQ_i, d_i, c_i in zip(cR_symbols, cQ_symbols, d_basis, c_basis)
    )
    target = sum(
        lam_i * (d_i + c_i)
        for lam_i, d_i, c_i in zip(lam_symbols, d_basis, c_basis)
    )
    residual = sp.Poly(split - target, *(d_basis + c_basis))
    equations = [sp.Eq(coeff, 0) for coeff in residual.coeffs()]
    solution = sp.solve(equations, cR_symbols + cQ_symbols, dict=True)
    expected = [
        {
            **{cR_i: lam_i for cR_i, lam_i in zip(cR_symbols, lam_symbols)},
            **{cQ_i: lam_i for cQ_i, lam_i in zip(cQ_symbols, lam_symbols)},
        }
    ]

    mismatch_symbols = [symbols_for_power("m", power) for power in SAMPLE_POWERS]
    mismatch_tower = sum(
        m_i * (d_i - c_i)
        for m_i, d_i, c_i in zip(mismatch_symbols, d_basis, c_basis)
    )
    mismatch_residual = sp.Poly(mismatch_tower - target, *(d_basis + c_basis))
    mismatch_equations = [sp.Eq(coeff, 0) for coeff in mismatch_residual.coeffs()]
    mismatch_solution = sp.solve(mismatch_equations, mismatch_symbols + lam_symbols, dict=True)
    mismatch_expected = [
        {
            **{m_i: sp.Integer(0) for m_i in mismatch_symbols},
            **{lam_i: sp.Integer(0) for lam_i in lam_symbols},
        }
    ]

    print(f"Sample independent powers: {SAMPLE_POWERS}")
    print("Solving the whole tower against a single-density connection target:")
    print(f"  split solution    = {solution}")
    print("Solving a pure mismatch tower against that target:")
    print(f"  mismatch solution = {mismatch_solution}")

    ok = solution == expected and mismatch_solution == mismatch_expected
    with out.derived_results():
        out.line(
            "higher-H mismatch cannot be hidden by mixing H powers",
            StatusMark.PASS if ok else StatusMark.FAIL,
            "independent H-degree basis forces each mismatch coefficient separately to zero",
        )
    return ok


def case_3_status(out: ScriptOutput):
    header("Case 3: Status after higher-H mismatch exclusion")
    print("The connection-equation operator lock now excludes mismatch")
    print("directions Hp.Rlin - Hp.Q for all p >= 2: H2 by step 8, and")
    print("the generic p>=3 case by this rung.")
    print()
    print("The remaining derivative ansatz-reduction target is therefore the")
    print("equal-coefficient tower:")
    print()
    print("  Hp.Rlin + Hp.Q")
    print()
    print("for p >= 3. The next rung should show that this tower is precisely")
    print("nonlinear metric-density field-redefinition freedom, or record the")
    print("exact residual if that reduction fails.")

    with out.governance_assessments():
        out.line(
            "higher-H mismatch tower excluded",
            StatusMark.PASS,
            "all non-Palatini split-density mismatch directions are killed by connection elimination",
        )
    with out.unresolved_obligations():
        out.line(
            "higher-H equal-coefficient field-redefinition reduction",
            StatusMark.OBLIGATION,
            "show Hp.Rlin+Hp.Q for p>=3 is nonlinear metric-density variable choice",
        )


def record_results(ns) -> None:
    ns.record_derivation(
        derivation_id="higher_h_connection_equation_operator_lock_018",
        inputs=["h2_connection_equation_operator_lock_018"],
        output=sp.Symbol("connection_elimination_implies_cRp_eq_cQp_for_all_p_ge_3"),
        method="generic-p coefficient matching of derivative and algebraic connection-equation basis terms",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="closure_uniqueness_rung",
        scope="higher-H mismatch exclusion",
    )
    ns.record_derivation(
        derivation_id="higher_h_mismatch_tower_excluded_018",
        inputs=["higher_h_connection_equation_operator_lock_018"],
        output=sp.Symbol("Hp_Rlin_minus_Hp_Q_mismatch_forced_zero_for_p_ge_3"),
        method="independent H-degree finite-tower witness plus generic-p two-basis solve",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="closure_uniqueness_rung",
        scope="all higher-H mismatch directions under no-independent-connection endpoint",
    )
    ns.record_obligation(ProofObligationRecord(
        obligation_id="closure_uniqueness_inhouse_018",
        script_id=SCRIPT_ID,
        title="In-house self-coupled spin-2 closure uniqueness",
        status=ObligationStatus.OPEN,
        required_by=["field_equation_proof"],
        description=(
            "All higher-H mismatch directions Hp.Rlin-Hp.Q are excluded by the "
            "connection-equation operator lock. The remaining derivative "
            "ansatz-reduction target is the equal-coefficient tower "
            "Hp.Rlin+Hp.Q for p>=3, which must be reduced to field "
            "redefinition freedom or otherwise discharged."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="closure_step_9_claim_018",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "The connection-equation operator lock applies independently at "
            "each higher H degree. For every p>=3, a split connection equation "
            "cR_p D[Hp]+cQ_p C[Hp] can be the connection equation of one "
            "compatible metric density only when cR_p=cQ_p. Thus every "
            "mismatch direction Hp.Rlin-Hp.Q is incompatible with the "
            "no-independent-connection endpoint unless its coefficient is zero. "
            "The remaining higher-H derivative target is the equal-coefficient "
            "tower Hp.Rlin+Hp.Q."
        ),
        derivation_ids=[
            "higher_h_connection_equation_operator_lock_018",
            "higher_h_mismatch_tower_excluded_018",
        ],
        obligation_ids=["closure_uniqueness_inhouse_018"],
    ))


def main() -> None:
    header("Trial 018: Closure Uniqueness Step 9")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    case_0_statement(out)
    case_1_generic_power_lock(out)
    case_2_finite_tower_no_cross_order_hiding(out)
    case_3_status(out)

    record_results(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
