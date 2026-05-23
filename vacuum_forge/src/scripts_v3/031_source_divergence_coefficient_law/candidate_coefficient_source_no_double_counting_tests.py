# Candidate coefficient source no double counting tests
#
# Group:
#   31_source_divergence_coefficient_law
#
# Script type:
#   COEFFICIENT SOURCE NO-DOUBLE-COUNTING TESTS
#
# Purpose
# -------
# Test whether coefficient behavior can be source-neutral without postulate adoption.
#
# Locked-door question:
#
#   Can the coefficient side remain free of ordinary rho/M_enc source load
#   without choosing the coefficient by repair or recovery?
#
# This script does not adopt a new postulate.
# It does not derive full source no-double-counting.
# It does not derive divergence-safe coefficient law.
# It does not derive B_s/F_zeta insertion.
# It does not construct active O.
# It does not derive residual control.
# It does not open the parent equation.
#
# Tiny goblin rule:
#
#   If the coefficient carries the gold, count it twice.

from dataclasses import dataclass
from pathlib import Path
from typing import List

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    BranchDecisionRecord,
    ClaimRecord,
    ClaimTier,
    GovernanceStatus,
    ObligationStatus,
    ProofObligationRecord,
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


def status_mark(status: str) -> StatusMark:
    return {
        "BLOCKED": StatusMark.FAIL,
        "CONSTRAINED": StatusMark.INFO,
        "DUPLICATE_RISK": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "PARTIAL_CONSTRAINT": StatusMark.INFO,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "THEOREM_TARGET": StatusMark.OBLIGATION,
        "UNDERDETERMINED": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g31_dup",
            "031_source_divergence_coefficient_law__candidate_source_duplicate_load_ledger",
            "g31_source_duplicate_ledger",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_problem",
            "031_source_divergence_coefficient_law__candidate_source_divergence_problem_ledger",
            "g31_source_divergence_problem",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g30_summary",
            "030_minimal_coefficient_sector_postulate_inventory__candidate_group_30_status_summary",
            "g30_status_summary",
            RecordKind.INVENTORY_MARKER,
        ),
    ]

    for dependency_id, upstream_script_id, upstream_derivation_id, expected_record_kind in dependencies:
        ns.declare_dependency(
            dependency_id=dependency_id,
            upstream_script_id=upstream_script_id,
            upstream_derivation_id=upstream_derivation_id,
            expected_record_kind=expected_record_kind,
        )

    return archive, ns, invalidated


def ensure_archive_write_dirs(ns) -> None:
    for attr in (
        "routes_path",
        "branch_decisions_path",
        "claims_path",
        "obligations_path",
        "derivations_path",
        "governance_path",
    ):
        path_obj = getattr(ns, attr, None)
        if path_obj is not None:
            path_obj.mkdir(parents=True, exist_ok=True)


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


@dataclass
class CoefficientSourceSymbols:
    rho_A: sp.Symbol
    rho_coeff: sp.Symbol
    C_zeta: sp.Symbol
    F_zeta: sp.Symbol
    S_ord: sp.Symbol
    S_coeff: sp.Symbol
    repair_selector: sp.Symbol
    recovery_selector: sp.Symbol
    hidden_source: sp.Symbol
    L_coeff_source: sp.Expr


@dataclass
class CoeffTest:
    name: str
    test: str
    status: str
    result: str
    caution: str


@dataclass
class NeutralityRoute:
    name: str
    route: str
    status: str
    requirement: str
    failure_mode: str


@dataclass
class RejectedRoute:
    name: str
    route: str
    status: str
    reason: str


@dataclass
class CoeffObligation:
    name: str
    obligation: str
    status: str
    blocks: str
    discipline: str


@dataclass
class CoeffConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_symbols() -> CoefficientSourceSymbols:
    (
        rho_A,
        rho_coeff,
        C_zeta,
        F_zeta,
        S_ord,
        S_coeff,
        repair_selector,
        recovery_selector,
        hidden_source,
    ) = sp.symbols(
        "rho_A rho_coeff C_zeta F_zeta S_ord S_coeff repair_selector recovery_selector hidden_source",
        real=True,
    )

    L_coeff_source = sp.simplify(rho_coeff + S_coeff + repair_selector + recovery_selector + hidden_source)

    return CoefficientSourceSymbols(
        rho_A=rho_A,
        rho_coeff=rho_coeff,
        C_zeta=C_zeta,
        F_zeta=F_zeta,
        S_ord=S_ord,
        S_coeff=S_coeff,
        repair_selector=repair_selector,
        recovery_selector=recovery_selector,
        hidden_source=hidden_source,
        L_coeff_source=L_coeff_source,
    )


def build_tests(symbols: CoefficientSourceSymbols) -> List[CoeffTest]:
    return [
        CoeffTest(
            name="T1: coefficient source load",
            test="rho_coeff = 0 sector-by-sector",
            status="THEOREM_TARGET",
            result="required for coefficient source neutrality",
            caution="not derived by this test alone",
        ),
        CoeffTest(
            name="T2: coefficient-side ordinary source",
            test="S_coeff = 0 or derived neutral source-free coefficient route",
            status="THEOREM_TARGET",
            result="coefficient side may not carry ordinary source load",
            caution="do not relabel source as coefficient response",
        ),
        CoeffTest(
            name="T3: repair selector exclusion",
            test="repair_selector = 0",
            status="REQUIRED",
            result="coefficient may not be selected to repair source leakage",
            caution="failure may reject but not select",
        ),
        CoeffTest(
            name="T4: recovery selector exclusion",
            test="recovery_selector = 0",
            status="REQUIRED",
            result="coefficient may not be selected from AB=1, Schwarzschild, weak-field, gamma/PPN, or kappa=0",
            caution="recovery audits only after construction",
        ),
        CoeffTest(
            name="T5: hidden source exclusion",
            test="hidden_source = 0",
            status="REQUIRED",
            result="ordinary source may not be hidden in coefficient definition",
            caution="source visibility remains required",
        ),
        CoeffTest(
            name="T6: coefficient source obstruction load",
            test=f"L_coeff_source = {sp.sstr(symbols.L_coeff_source)}",
            status="THEOREM_TARGET",
            result="all coefficient-side source selectors and hidden loads must vanish",
            caution="this constrains but does not derive full coefficient law",
        ),
    ]


def build_routes() -> List[NeutralityRoute]:
    return [
        NeutralityRoute(
            name="N1: structural source neutrality",
            route="derive coefficient dependence only from non-source volume/trace structure",
            status="OPEN",
            requirement="coefficient law must not include ordinary rho/M_enc source load",
            failure_mode="if rho/M_enc enters, coefficient double-counts A-sector source",
        ),
        NeutralityRoute(
            name="N2: residual-neutral route",
            route="show zeta/kappa residual channels do not carry ordinary source load into coefficient",
            status="OPEN",
            requirement="residual source channels must be neutral before coefficient use",
            failure_mode="residuals become source reservoirs",
        ),
        NeutralityRoute(
            name="N3: correction-neutral route",
            route="show divergence/correction term does not carry ordinary source load into coefficient",
            status="OPEN",
            requirement="correction must be non-reservoir",
            failure_mode="correction becomes hidden source pocket",
        ),
        NeutralityRoute(
            name="N4: source-free coefficient classifier",
            route="classify coefficient law as source-free, partially constrained, or underdetermined",
            status="OPEN",
            requirement="must distinguish constraint from derivation",
            failure_mode="partial constraint mistaken for coefficient law",
        ),
    ]


def build_rejected_routes() -> List[RejectedRoute]:
    return [
        RejectedRoute(
            name="R1: coefficient source carrier",
            route="allow coefficient to carry ordinary rho/M_enc source load",
            status="REJECTED",
            reason="ordinary source is already carried by A-sector",
        ),
        RejectedRoute(
            name="R2: source repair coefficient",
            route="choose coefficient to cancel duplicate source leakage",
            status="REJECTED",
            reason="repair may reject but not select",
        ),
        RejectedRoute(
            name="R3: recovery-selected coefficient",
            route="choose coefficient from AB=1, Schwarzschild, weak-field, gamma/PPN, or kappa=0",
            status="REJECTED",
            reason="recovery may audit only after construction",
        ),
        RejectedRoute(
            name="R4: hidden source definition",
            route="define coefficient with implicit ordinary source dependence",
            status="REJECTED",
            reason="source visibility requires explicit accounting",
        ),
        RejectedRoute(
            name="R5: source neutrality as insertion",
            route="treat coefficient source neutrality as B_s/F_zeta insertion",
            status="REJECTED",
            reason="source neutrality is necessary but not sufficient for insertion",
        ),
        RejectedRoute(
            name="R6: source neutrality as parent readiness",
            route="treat source-neutral coefficient as parent equation readiness",
            status="REJECTED",
            reason="parent gate remains closed",
        ),
    ]


def build_obligations() -> List[CoeffObligation]:
    return [
        CoeffObligation(
            name="O1: coefficient source exclusion",
            obligation="derive or retain as open rho_coeff = 0 sector-by-sector",
            status="OPEN",
            blocks="source no-double-counting",
            discipline="do not hide source in coefficient",
        ),
        CoeffObligation(
            name="O2: selector exclusion",
            obligation="enforce repair_selector = 0 and recovery_selector = 0",
            status="REQUIRED",
            blocks="coefficient admissibility",
            discipline="no repair or recovery selection",
        ),
        CoeffObligation(
            name="O3: residual/correction carryover",
            obligation="carry residual and correction source channels into later audits",
            status="OPEN",
            blocks="full source no-double-counting",
            discipline="coefficient test alone is not full theorem",
        ),
        CoeffObligation(
            name="O4: divergence reservoir next",
            obligation="test whether correction/divergence term becomes hidden reservoir",
            status="OPEN",
            blocks="divergence-safe coefficient behavior",
            discipline="source-neutral coefficient is not divergence-safe law",
        ),
        CoeffObligation(
            name="O5: downstream gates",
            obligation="keep insertion, active O, residual control, and parent equation closed",
            status="NOT_READY",
            blocks="premature closure",
            discipline="source neutrality is not insertion",
        ),
    ]


def build_conclusions() -> List[CoeffConclusion]:
    return [
        CoeffConclusion(
            name="C1: coefficient source neutrality target",
            conclusion="coefficient-side ordinary source load must vanish sector-by-sector or be derived neutral",
            status="THEOREM_TARGET",
            meaning="rho_coeff remains central source no-double-counting target",
        ),
        CoeffConclusion(
            name="C2: partial constraint",
            conclusion="source neutrality constrains coefficient behavior but does not derive full coefficient law",
            status="PARTIAL_CONSTRAINT",
            meaning="necessary condition only",
        ),
        CoeffConclusion(
            name="C3: no adoption",
            conclusion="no Group 30 candidate postulate is adopted",
            status="NOT_ADOPTED",
            meaning="the test is theorem-route discipline only",
        ),
        CoeffConclusion(
            name="C4: no insertion",
            conclusion="B_s/F_zeta insertion is not derived",
            status="NOT_READY",
            meaning="source neutrality is not insertion",
        ),
        CoeffConclusion(
            name="C5: next",
            conclusion="divergence reservoir obstruction should run next",
            status="OPEN",
            meaning="correction/divergence source hiding remains open",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Coefficient source no-double-counting problem")
    print("Question:")
    print()
    print("  Can the coefficient side remain free of ordinary rho/M_enc source load without choosing the coefficient by repair or recovery?")
    print()
    print("Discipline:")
    print()
    print("  This script tests coefficient source neutrality.")
    print("  It does not derive full source no-double-counting.")
    print("  It does not derive insertion.")
    print()
    print("Tiny goblin rule:")
    print("  If the coefficient carries the gold, count it twice.")

    with out.governance_assessments():
        out.line(
            "coefficient source no-double-counting tests opened",
            StatusMark.INFO,
            "testing coefficient-side ordinary source exclusion",
        )


def case_1_symbolic_ledger(symbols: CoefficientSourceSymbols, out: ScriptOutput) -> None:
    header("Case 1: Coefficient source symbolic ledger")
    print("Coefficient source symbols:")
    print()
    for name in [
        "rho_A",
        "rho_coeff",
        "C_zeta",
        "F_zeta",
        "S_ord",
        "S_coeff",
        "repair_selector",
        "recovery_selector",
        "hidden_source",
    ]:
        print(f"  {name} = {sp.sstr(getattr(symbols, name))}")

    print()
    print("Coefficient source obstruction load:")
    print(f"  L_coeff_source = {sp.sstr(symbols.L_coeff_source)}")

    with out.derived_results():
        out.line(
            "coefficient source obstruction load stated",
            StatusMark.OBLIGATION,
            f"L_coeff_source = {sp.sstr(symbols.L_coeff_source)}",
        )


def case_2_tests(items: List[CoeffTest], out: ScriptOutput) -> None:
    header("Case 2: Coefficient source tests")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Test: {item.test}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Result: {item.result}")
        print(f"Caution: {item.caution}")

    with out.governance_assessments():
        out.line(
            "coefficient source tests stated",
            StatusMark.DEFER,
            f"{len(items)} coefficient source tests stated",
        )


def case_3_routes(items: List[NeutralityRoute], out: ScriptOutput) -> None:
    header("Case 3: Coefficient source-neutrality routes")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Route: {item.route}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Requirement: {item.requirement}")
        print(f"Failure mode: {item.failure_mode}")

    with out.unresolved_obligations():
        out.line(
            "coefficient source-neutrality routes remain open",
            StatusMark.OBLIGATION,
            f"{len(items)} neutrality routes remain open",
        )


def case_4_rejected(items: List[RejectedRoute], out: ScriptOutput) -> None:
    header("Case 4: Rejected coefficient source routes")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Route: {item.route}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Reason: {item.reason}")

    with out.counterexamples():
        out.line(
            "rejected coefficient source routes stated",
            StatusMark.FAIL,
            "source carrier, repair, recovery, hidden definition, insertion shortcut, parent readiness rejected",
        )


def case_5_obligations(items: List[CoeffObligation], out: ScriptOutput) -> None:
    header("Case 5: Coefficient source obligations")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Obligation: {item.obligation}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Blocks: {item.blocks}")
        print(f"Discipline: {item.discipline}")

    with out.unresolved_obligations():
        out.line(
            "coefficient source obligations stated",
            StatusMark.OBLIGATION,
            f"{len(items)} obligations remain",
        )


def case_6_conclusions(items: List[CoeffConclusion], out: ScriptOutput) -> None:
    header("Case 6: Coefficient source conclusions")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Conclusion: {item.conclusion}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Meaning: {item.meaning}")

    with out.governance_assessments():
        out.line(
            "coefficient source conclusion stated",
            StatusMark.PASS,
            "coefficient source neutrality constrained; no full theorem or insertion",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Coefficient source no-double-counting test result:")
    print()
    print("  Coefficient-side ordinary source load must vanish sector-by-sector or be independently derived neutral.")
    print("  Source neutrality constrains coefficient behavior but does not derive the full coefficient law.")
    print("  Coefficient source carrier, repair-selected coefficient, recovery-selected coefficient, hidden source definition, insertion shortcut, and parent-readiness shortcut are rejected.")
    print("  No Group 30 candidate postulate is adopted.")
    print("  Full source no-double-counting is not yet derived.")
    print("  B_s/F_zeta insertion is not derived.")
    print("  Active O, residual control, and parent equation remain not ready.")
    print()
    print("Possible next script:")
    print("  candidate_divergence_reservoir_obstruction.py")
    print()
    print("Tiny goblin label:")
    print("  If the coefficient carries the gold, count it twice.")

    with out.governance_assessments():
        out.line(
            "coefficient source no-double-counting tests complete",
            StatusMark.PASS,
            "divergence reservoir obstruction should run next",
        )


def record_derivations(ns, symbols: CoefficientSourceSymbols) -> None:
    ns.record_derivation(
        derivation_id="g31_coeff_source_tests",
        inputs=[
            symbols.rho_coeff,
            symbols.S_coeff,
            symbols.repair_selector,
            symbols.recovery_selector,
            symbols.hidden_source,
        ],
        output=symbols.L_coeff_source,
        method="test coefficient-side ordinary source exclusion without postulate adoption",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="coefficient_source_no_double_counting_marker",
        scope="Group 31 source/divergence coefficient law",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g31_coeff_rho_zero", "Derive or leave open rho_coeff = 0 sector-by-sector"),
        ("g31_coeff_selector_zero", "Enforce repair and recovery selector exclusions"),
        ("g31_coeff_residual_carryover", "Carry residual source channels forward"),
        ("g31_coeff_correction_carryover", "Carry correction source channel into divergence obstruction"),
        ("g31_coeff_no_insertion", "Do not treat coefficient source neutrality as insertion"),
        ("g31_coeff_downstream_closed", "Keep insertion/O/residual/parent gates closed"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g31_coeff_source_route"],
            description=(
                "Coefficient source neutrality is constrained as a theorem target. Full source no-double-counting and insertion are not derived."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g31_coeff_rho_zero",
        "g31_coeff_selector_zero",
        "g31_coeff_residual_carryover",
        "g31_coeff_correction_carryover",
        "g31_coeff_no_insertion",
        "g31_coeff_downstream_closed",
    ]

    ns.record_route(RouteRecord(
        route_id="g31_coeff_source_route",
        script_id=SCRIPT_ID,
        name="Group 31 coefficient source no-double-counting route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "coefficient-side ordinary source load must vanish or be derived neutral",
            "repair and recovery selected coefficient routes rejected",
            "source neutrality is a necessary constraint, not full coefficient law",
            "no postulate adopted",
            "downstream gates remain closed",
        ],
    ))

    for branch_id in [
        "coefficient_as_source_carrier",
        "source_repair_selected_coefficient",
        "recovery_selected_coefficient",
        "hidden_source_coefficient_definition",
        "source_neutrality_as_insertion",
        "source_neutrality_as_parent_readiness",
        "coefficient_source_tests_as_full_theorem",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; coefficient source tests are not insertion or parent closure.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g31_coeff_source_constraint",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Coefficient-side ordinary source load must vanish sector-by-sector or be independently derived neutral. This constrains coefficient behavior but does not derive the full coefficient law. "
            "Coefficient source carrier, repair-selected coefficient, recovery-selected coefficient, hidden source definition, insertion shortcut, and parent-readiness shortcut are rejected. "
            "No Group 30 candidate postulate is adopted. Full source no-double-counting, B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready."
        ),
        derivation_ids=["g31_coeff_source_tests"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Coefficient Source No Double Counting Tests")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    tests = build_tests(symbols)
    routes = build_routes()
    rejected = build_rejected_routes()
    obligations = build_obligations()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_symbolic_ledger(symbols, out)
    case_2_tests(tests, out)
    case_3_routes(routes, out)
    case_4_rejected(rejected, out)
    case_5_obligations(obligations, out)
    case_6_conclusions(conclusions, out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns, symbols)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
