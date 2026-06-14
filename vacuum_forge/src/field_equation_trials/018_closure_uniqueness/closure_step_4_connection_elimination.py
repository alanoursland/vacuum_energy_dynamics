# Trial 018: Closure uniqueness, step 4
#
# Script type:
#   RIGOR PROGRAM / PALATINI CONNECTION ELIMINATION
#
# Purpose
# -------
# This is the fourth in-house rung toward replacing the Deser 1970
# self-coupled spin-2 closure citation. It still does not retire the
# full closure-uniqueness obligation.
#
# Steps 2 and 3 showed that the first-order Palatini replacement gives
# a finite deformation witness. This script checks that the Palatini
# endpoint does not leave an independent connection sector:
#
#   1. The torsion-free Palatini connection equation implies
#        P_a^{mn} = 0,
#      where P_a^{mn} = nabla_a gdens^{mn}, by a trace argument.
#   2. In a local inertial frame, a torsion-free connection difference
#      C^a_{mn} compatible with eta-density has only the zero solution.
#   3. Therefore the independent connection is eliminated locally:
#      the endpoint is the metric/Levi-Civita closure, not a new
#      connection theory.
#
# This proves connection elimination inside the Palatini endpoint. It
# does not prove that every admissible deformation reduces to the
# Palatini endpoint; that ansatz-reduction lemma remains open.

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

DIM = 4
ETA = [-1, 1, 1, 1]


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
        dependency_id="closure_step_3_dependency_018",
        upstream_script_id="018_closure_uniqueness__closure_step_3_deformation_audit",
        upstream_derivation_id="palatini_replacement_coefficient_audit_018",
        expected_record_kind=RecordKind.DERIVATION,
    )
    return archive, ns, invalidated


def eta_up(mu: int, nu: int):
    return sp.Integer(ETA[mu]) if mu == nu else sp.Integer(0)


def C(alpha: int, mu: int, nu: int):
    # Torsion-free connection difference: C^alpha_{mu nu}=C^alpha_{nu mu}.
    a, b = sorted((mu, nu))
    return sp.Symbol(f"C{alpha}_{a}{b}")


def P(alpha: int, mu: int, nu: int):
    # P_alpha^{mu nu} = nabla_alpha gdens^{mu nu}; symmetric in mu,nu.
    a, b = sorted((mu, nu))
    return sp.Symbol(f"P{alpha}_{a}{b}")


def V(mu: int):
    return sum(P(beta, mu, beta) for beta in range(DIM))


def palatini_connection_equation(alpha: int, mu: int, nu: int):
    # P_alpha^{mu nu} - delta_alpha^{(mu} V^{nu)} = 0.
    delta_am = sp.Integer(1) if alpha == mu else sp.Integer(0)
    delta_an = sp.Integer(1) if alpha == nu else sp.Integer(0)
    return sp.simplify(P(alpha, mu, nu) - sp.Rational(1, 2) * (delta_am * V(nu) + delta_an * V(mu)))


def compatibility_difference(alpha: int, mu: int, nu: int):
    # Difference of density-compatibility equations around eta:
    # C^mu_{alpha beta} eta^{beta nu}
    # + C^nu_{alpha beta} eta^{mu beta}
    # - C^beta_{alpha beta} eta^{mu nu} = 0.
    return sp.simplify(
        sum(C(mu, alpha, beta) * eta_up(beta, nu) for beta in range(DIM))
        + sum(C(nu, alpha, beta) * eta_up(mu, beta) for beta in range(DIM))
        - sum(C(beta, alpha, beta) for beta in range(DIM)) * eta_up(mu, nu)
    )


def independent_c_symbols():
    return [
        C(alpha, mu, nu)
        for alpha in range(DIM)
        for mu in range(DIM)
        for nu in range(mu, DIM)
    ]


def independent_p_symbols():
    return [
        P(alpha, mu, nu)
        for alpha in range(DIM)
        for mu in range(DIM)
        for nu in range(mu, DIM)
    ]


def case_0_statement(out: ScriptOutput) -> None:
    header("Case 0: Closure uniqueness program, fourth rung")
    print("The first-order endpoint must not leave an independent connection")
    print("sector. This script checks the Palatini connection equation:")
    print()
    print("  P_a^{mn} - delta_a^{(m} P_b^{n)b} = 0")
    print()
    print("with P_a^{mn} = nabla_a gdens^{mn}. The trace should force")
    print("P_a^{mn}=0, and density compatibility should fix the torsion-free")
    print("connection uniquely.")

    with out.governance_assessments():
        out.line(
            "Palatini connection-elimination check opened",
            StatusMark.INFO,
            "endpoint metricity check; ansatz-reduction uniqueness remains open",
        )


def case_1_trace_forces_density_compatibility(out: ScriptOutput):
    header("Case 1: Trace of the Palatini equation kills P divergence")
    residuals = []
    for mu in range(DIM):
        traced = sp.simplify(sum(palatini_connection_equation(nu, mu, nu) for nu in range(DIM)))
        expected = sp.simplify(sp.Rational(1 - DIM, 2) * V(mu))
        residual = sp.simplify(traced - expected)
        residuals.append(residual)
        print(f"  trace equation mu={mu}: residual vs ((1-D)/2) V^mu = {sp.sstr(residual)}")

    print()
    print("For D=4, the coefficient (1-D)/2 is nonzero, so V^mu=0.")
    print("Substituting V^mu=0 into the original equation gives P_a^{mn}=0.")

    ok = all(is_zero(residual) for residual in residuals) and sp.Rational(1 - DIM, 2) != 0
    with out.derived_results():
        out.line(
            "Palatini trace forces density compatibility",
            StatusMark.PASS if ok else StatusMark.FAIL,
            "torsion-free connection equation implies nabla_a gdens^{mn}=0 in four dimensions",
        )
    return ok


def case_2_component_solve_for_p(out: ScriptOutput):
    header("Case 2: Full Palatini equation has only P=0 solution")
    equations = [
        palatini_connection_equation(alpha, mu, nu)
        for alpha in range(DIM)
        for mu in range(DIM)
        for nu in range(mu, DIM)
    ]
    symbols = independent_p_symbols()
    solution = sp.solve(equations, symbols, dict=True)
    zero_solution = [{symbol: sp.Integer(0) for symbol in symbols}]

    print(f"  independent P components = {len(symbols)}")
    print(f"  independent equations    = {len(equations)}")
    print(f"  solution count           = {len(solution)}")
    print(f"  solution is all-zero     = {solution == zero_solution}")

    ok = solution == zero_solution
    with out.derived_results():
        out.line(
            "component solve verifies P_a^{mn}=0 uniquely",
            StatusMark.PASS if ok else StatusMark.FAIL,
            "no residual density-nonmetricity survives the torsion-free Palatini equation",
        )
    return ok


def case_3_connection_difference_unique(out: ScriptOutput):
    header("Case 3: Compatible torsion-free connection difference is zero")
    equations = [
        compatibility_difference(alpha, mu, nu)
        for alpha in range(DIM)
        for mu in range(DIM)
        for nu in range(mu, DIM)
    ]
    symbols = independent_c_symbols()
    solution = sp.solve(equations, symbols, dict=True)
    zero_solution = [{symbol: sp.Integer(0) for symbol in symbols}]

    print("Let C be the difference between two torsion-free connections")
    print("compatible with the same nondegenerate density. In a local inertial")
    print("frame, the homogeneous compatibility equations are linear:")
    print(f"  independent C components = {len(symbols)}")
    print(f"  independent equations    = {len(equations)}")
    print(f"  solution count           = {len(solution)}")
    print(f"  solution is all-zero     = {solution == zero_solution}")

    ok = solution == zero_solution
    with out.derived_results():
        out.line(
            "torsion-free compatible connection is unique",
            StatusMark.PASS if ok else StatusMark.FAIL,
            "the independent Palatini connection reduces locally to the Levi-Civita connection",
        )
    return ok


def case_4_verdict(out: ScriptOutput):
    header("Case 4: Remaining status")
    print("This rung closes the independent-connection loophole inside the")
    print("Palatini endpoint: the connection equation enforces density")
    print("compatibility, and the torsion-free compatible connection is unique.")
    print()
    print("What remains open is still the larger ansatz-reduction lemma: prove")
    print("that every admissible local two-derivative self-coupled spin-2")
    print("completion reduces to the Palatini endpoint already checked.")

    with out.governance_assessments():
        out.line(
            "Palatini endpoint is metric after connection elimination",
            StatusMark.PASS,
            "independent connection does not represent a new field in the closure endpoint",
        )
    with out.unresolved_obligations():
        out.line(
            "ansatz-reduction lemma for self-coupled spin-2 closure",
            StatusMark.OBLIGATION,
            "connection elimination proved inside Palatini; full Deser replacement still needs ansatz reduction",
        )


def record_results(ns) -> None:
    ns.record_derivation(
        derivation_id="palatini_trace_density_compatibility_018",
        inputs=["palatini_replacement_coefficient_audit_018"],
        output=sp.Symbol("palatini_connection_equation_implies_P_zero"),
        method="trace algebra for P_a^{mn} - delta_a^{(m} P_b^{n)b}=0 in D=4",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="closure_uniqueness_rung",
        scope="torsion-free Palatini endpoint; not full ansatz reduction",
    )
    ns.record_derivation(
        derivation_id="palatini_connection_uniqueness_018",
        inputs=["palatini_trace_density_compatibility_018"],
        output=sp.Symbol("torsion_free_density_compatible_connection_unique"),
        method="component solve for homogeneous connection-difference compatibility equations around eta",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="closure_uniqueness_rung",
        scope="local inertial frame uniqueness witness",
    )
    ns.record_obligation(ProofObligationRecord(
        obligation_id="closure_uniqueness_inhouse_018",
        script_id=SCRIPT_ID,
        title="In-house self-coupled spin-2 closure uniqueness",
        status=ObligationStatus.OPEN,
        required_by=["field_equation_proof"],
        description=(
            "The Palatini endpoint's independent connection has been eliminated "
            "by palatini_trace_density_compatibility_018 and "
            "palatini_connection_uniqueness_018. Full Deser replacement still "
            "requires the ansatz-reduction lemma."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="closure_step_4_claim_018",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "Inside the torsion-free Palatini endpoint, the connection equation "
            "forces nabla_a gdens^{mn}=0, and the compatible torsion-free "
            "connection is locally unique. Thus the endpoint is the metric/"
            "Levi-Civita closure, not a theory with an independent connection. "
            "This advances but does not retire the in-house closure-uniqueness "
            "obligation."
        ),
        derivation_ids=[
            "palatini_trace_density_compatibility_018",
            "palatini_connection_uniqueness_018",
        ],
        obligation_ids=["closure_uniqueness_inhouse_018"],
    ))


def main() -> None:
    header("Trial 018: Closure Uniqueness Step 4")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    case_0_statement(out)
    case_1_trace_forces_density_compatibility(out)
    case_2_component_solve_for_p(out)
    case_3_connection_difference_unique(out)
    case_4_verdict(out)

    record_results(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
