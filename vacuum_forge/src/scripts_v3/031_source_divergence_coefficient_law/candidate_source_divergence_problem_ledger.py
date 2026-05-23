# Candidate source divergence problem ledger
#
# Group:
#   31_source_divergence_coefficient_law
#
# Human title:
#   Source / Divergence Coefficient Law
#
# Script type:
#   PROBLEM LEDGER / SOURCE-DIVERGENCE THEOREM ROUTE OPENER
#
# Purpose
# -------
# Open the source/divergence coefficient-law theorem route.
# Define the duplicate-source and divergence-reservoir ledgers.
# Record that Group 30 completed the minimal postulate inventory without adopting postulates.
#
# Locked-door question:
#
#   Can source no-double-counting and divergence-safe coefficient behavior
#   constrain the B_s/F_zeta law without postulate adoption?
#
# This script does not adopt a new postulate.
# It does not derive B_s/F_zeta insertion.
# It does not derive the complete coefficient law.
# It does not derive no-overlap sector geometry.
# It does not construct active O.
# It does not derive residual control.
# It does not open the parent equation.
#
# Tiny goblin rule:
#
#   Try to forge the key from flow, not declare a tooth.

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
        "ADMISSIBLE_CANDIDATE": StatusMark.INFO,
        "CANDIDATE_ROUTE": StatusMark.DEFER,
        "COMPLETED_INVENTORY": StatusMark.PASS,
        "HIGH_RISK": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "THEOREM_ROUTE": StatusMark.OBLIGATION,
        "THEOREM_ROUTE_PREFERRED": StatusMark.INFO,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g30_summary",
            "030_minimal_coefficient_sector_postulate_inventory__candidate_group_30_status_summary",
            "g30_status_summary",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g30_obligations",
            "030_minimal_coefficient_sector_postulate_inventory__candidate_minimal_postulate_obligations",
            "g30_obligations",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g30_obstruction",
            "030_minimal_coefficient_sector_postulate_inventory__candidate_minimal_postulate_set_obstruction",
            "g30_postulate_set_obstruction",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g29_summary",
            "029_Bs_Fzeta_coefficient_origin__candidate_group_29_status_summary",
            "g29_status_summary",
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
class SourceDivergenceSymbols:
    rho_A: sp.Symbol
    rho_coeff: sp.Symbol
    rho_zeta_res: sp.Symbol
    rho_kappa_res: sp.Symbol
    rho_boundary: sp.Symbol
    rho_corr: sp.Symbol
    R_div: sp.Symbol
    hidden_source: sp.Symbol
    hidden_boundary: sp.Symbol
    hidden_current: sp.Symbol
    hidden_mass: sp.Symbol
    hidden_support: sp.Symbol
    L_source_dup: sp.Expr
    L_div_reservoir: sp.Expr
    L_source_divergence: sp.Expr


@dataclass
class ProblemItem:
    name: str
    item: str
    status: str
    meaning: str


@dataclass
class LedgerEntry:
    name: str
    expression: str
    status: str
    requirement: str
    forbidden_use: str


@dataclass
class RejectedRoute:
    name: str
    route: str
    status: str
    reason: str


@dataclass
class InitialObligation:
    name: str
    obligation: str
    status: str
    blocks: str
    discipline: str


@dataclass
class InitialConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_symbols() -> SourceDivergenceSymbols:
    (
        rho_A,
        rho_coeff,
        rho_zeta_res,
        rho_kappa_res,
        rho_boundary,
        rho_corr,
        R_div,
        hidden_source,
        hidden_boundary,
        hidden_current,
        hidden_mass,
        hidden_support,
    ) = sp.symbols(
        "rho_A rho_coeff rho_zeta_res rho_kappa_res rho_boundary rho_corr "
        "R_div hidden_source hidden_boundary hidden_current hidden_mass hidden_support",
        real=True,
    )

    L_source_dup = sp.simplify(
        rho_coeff + rho_zeta_res + rho_kappa_res + rho_boundary + rho_corr
    )

    L_div_reservoir = sp.simplify(
        R_div + hidden_source + hidden_boundary + hidden_current + hidden_mass + hidden_support
    )

    L_source_divergence = sp.simplify(L_source_dup + L_div_reservoir)

    return SourceDivergenceSymbols(
        rho_A=rho_A,
        rho_coeff=rho_coeff,
        rho_zeta_res=rho_zeta_res,
        rho_kappa_res=rho_kappa_res,
        rho_boundary=rho_boundary,
        rho_corr=rho_corr,
        R_div=R_div,
        hidden_source=hidden_source,
        hidden_boundary=hidden_boundary,
        hidden_current=hidden_current,
        hidden_mass=hidden_mass,
        hidden_support=hidden_support,
        L_source_dup=L_source_dup,
        L_div_reservoir=L_div_reservoir,
        L_source_divergence=L_source_divergence,
    )


def build_problem_items() -> List[ProblemItem]:
    return [
        ProblemItem(
            name="P1: Group 30 status",
            item="minimal coefficient/sector postulate inventory",
            status="COMPLETED_INVENTORY",
            meaning="completed as inventory/obstruction; no postulate adopted; minimal set not identified",
        ),
        ProblemItem(
            name="P2: source no-double-counting",
            item="ordinary source load remains routed to A-sector and is not duplicated through coefficient/residual/correction channels",
            status="THEOREM_ROUTE_PREFERRED",
            meaning="must be tested as theorem route before postulating",
        ),
        ProblemItem(
            name="P3: divergence-safe coefficient behavior",
            item="coefficient-side divergence behavior is explicit and non-reservoir",
            status="THEOREM_ROUTE_PREFERRED",
            meaning="must not hide source, boundary, current, mass, or support load",
        ),
        ProblemItem(
            name="P4: admissible candidates",
            item="trace normalization, safe trace membership, guardrail visibility, divergence explicitness",
            status="ADMISSIBLE_CANDIDATE",
            meaning="survived Group 30 only as candidates; not adopted",
        ),
        ProblemItem(
            name="P5: trace/residual incidence",
            item="I(T_zeta,R_zeta)=0 and I(T_zeta,R_kappa)=0",
            status="HIGH_RISK",
            meaning="not adopted; too close to no-overlap/residual-control smuggling",
        ),
        ProblemItem(
            name="P6: insertion and parent gates",
            item="B_s/F_zeta insertion, active O, residual control, parent equation",
            status="NOT_READY",
            meaning="all remain closed in this group opener",
        ),
    ]


def build_ledgers(symbols: SourceDivergenceSymbols) -> List[LedgerEntry]:
    return [
        LedgerEntry(
            name="L1: protected A-sector source",
            expression="rho_A",
            status="REQUIRED",
            requirement="ordinary rho/M_enc remains routed to A-sector mass charge",
            forbidden_use="do not reroute ordinary source into coefficient, residual, correction, or parent placeholder",
        ),
        LedgerEntry(
            name="L2: duplicate source load",
            expression=sp.sstr(symbols.L_source_dup),
            status="THEOREM_ROUTE",
            requirement="must vanish sector-by-sector or each term must have a derived neutral route",
            forbidden_use="do not cancel only in total; do not hide source in coefficient/residual/boundary/correction",
        ),
        LedgerEntry(
            name="L3: divergence reservoir load",
            expression=sp.sstr(symbols.L_div_reservoir),
            status="THEOREM_ROUTE",
            requirement="must vanish sector-by-sector or be explicitly derived as neutral and non-reservoir",
            forbidden_use="do not use divergence correction as hidden source/boundary/current/mass/support pocket",
        ),
        LedgerEntry(
            name="L4: combined source/divergence obstruction load",
            expression=sp.sstr(symbols.L_source_divergence),
            status="THEOREM_ROUTE",
            requirement="must be controlled before any coefficient law can be used for insertion",
            forbidden_use="do not treat source/divergence discipline as B_s/F_zeta insertion",
        ),
    ]


def build_rejected_routes() -> List[RejectedRoute]:
    return [
        RejectedRoute(
            name="R1: postulate adoption by theorem route",
            route="adopt Group 30 candidates because source/divergence route needs them",
            status="REJECTED",
            reason="candidate survival is not adoption; explicit user/theory decision required",
        ),
        RejectedRoute(
            name="R2: source repair selection",
            route="choose coefficient because otherwise source duplicate load appears",
            status="REJECTED",
            reason="failure may reject but not select coefficient",
        ),
        RejectedRoute(
            name="R3: divergence reservoir",
            route="put source/boundary/current/mass/support load into divergence correction",
            status="REJECTED",
            reason="divergence correction must be explicit, auditable, and non-reservoir",
        ),
        RejectedRoute(
            name="R4: recovery selection",
            route="select source/divergence coefficient behavior from AB=1, B=1/A, Schwarzschild, gamma/PPN, weak-field, or kappa=0",
            status="REJECTED",
            reason="recovery may audit only after construction",
        ),
        RejectedRoute(
            name="R5: active-O convenience",
            route="select coefficient behavior to make active O easier",
            status="REJECTED",
            reason="active O remains not constructed and not usable",
        ),
        RejectedRoute(
            name="R6: parent-fit closure",
            route="select source/divergence law so parent equation closes",
            status="REJECTED",
            reason="parent fit cannot select coefficient or correction law",
        ),
        RejectedRoute(
            name="R7: insertion shortcut",
            route="treat source/divergence discipline as B_s/F_zeta insertion",
            status="REJECTED",
            reason="source/divergence constraints are not insertion theorem",
        ),
    ]


def build_obligations() -> List[InitialObligation]:
    return [
        InitialObligation(
            name="O1: duplicate source ledger",
            obligation="inventory all duplicate ordinary source loads through coefficient/residual/boundary/correction channels",
            status="OPEN",
            blocks="source no-double-counting",
            discipline="sector-by-sector zero, not total cancellation",
        ),
        InitialObligation(
            name="O2: coefficient source neutrality",
            obligation="test whether coefficient behavior can be source-neutral without postulate adoption",
            status="OPEN",
            blocks="coefficient law",
            discipline="do not hide rho/M_enc in coefficient",
        ),
        InitialObligation(
            name="O3: divergence reservoir obstruction",
            obligation="test whether divergence correction becomes hidden reservoir",
            status="OPEN",
            blocks="divergence-safe coefficient behavior",
            discipline="explicit/auditable/non-reservoir only",
        ),
        InitialObligation(
            name="O4: trace-normalization fork",
            obligation="test whether source/divergence constraints force trace normalization or leave it open",
            status="OPEN",
            blocks="coefficient normalization",
            discipline="do not select from recovery",
        ),
        InitialObligation(
            name="O5: downstream gates",
            obligation="keep B_s/F_zeta insertion, active O, residual control, and parent equation closed",
            status="NOT_READY",
            blocks="premature closure",
            discipline="source/divergence law is not insertion or parent readiness",
        ),
    ]


def build_conclusions() -> List[InitialConclusion]:
    return [
        InitialConclusion(
            name="C1: group opened",
            conclusion="source/divergence coefficient-law route is opened",
            status="THEOREM_ROUTE",
            meaning="next theorem route after Group 30 inventory/obstruction",
        ),
        InitialConclusion(
            name="C2: no adoption",
            conclusion="no Group 30 candidate postulate is adopted",
            status="NOT_ADOPTED",
            meaning="trace normalization, safe membership, guardrail visibility, and divergence explicitness remain candidates only",
        ),
        InitialConclusion(
            name="C3: ledgers",
            conclusion="duplicate-source and divergence-reservoir ledgers are explicit",
            status="REQUIRED",
            meaning="they define the obstruction loads for the group",
        ),
        InitialConclusion(
            name="C4: insertion",
            conclusion="B_s/F_zeta insertion is not derived",
            status="NOT_READY",
            meaning="source/divergence problem ledger is not a coefficient law or insertion theorem",
        ),
        InitialConclusion(
            name="C5: next",
            conclusion="duplicate source load ledger should run next",
            status="OPEN",
            meaning="first concrete audit in the source/divergence route",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Source/divergence coefficient-law problem")
    print("Question:")
    print()
    print("  Can source no-double-counting and divergence-safe coefficient behavior constrain the B_s/F_zeta law without postulate adoption?")
    print()
    print("Discipline:")
    print()
    print("  This script opens a theorem route.")
    print("  It adopts no postulate.")
    print("  It derives no insertion.")
    print()
    print("Tiny goblin rule:")
    print("  Try to forge the key from flow, not declare a tooth.")

    with out.governance_assessments():
        out.line(
            "source/divergence coefficient-law route opened",
            StatusMark.INFO,
            "testing theorem route after Group 30 completed inventory without postulate adoption",
        )


def case_1_symbolic_ledger(symbols: SourceDivergenceSymbols, out: ScriptOutput) -> None:
    header("Case 1: Source/divergence symbolic ledger")
    print("Source/divergence symbols:")
    print()
    for name in [
        "rho_A",
        "rho_coeff",
        "rho_zeta_res",
        "rho_kappa_res",
        "rho_boundary",
        "rho_corr",
        "R_div",
        "hidden_source",
        "hidden_boundary",
        "hidden_current",
        "hidden_mass",
        "hidden_support",
    ]:
        print(f"  {name} = {sp.sstr(getattr(symbols, name))}")

    print()
    print("Duplicate source load:")
    print(f"  L_source_dup = {sp.sstr(symbols.L_source_dup)}")
    print()
    print("Divergence reservoir load:")
    print(f"  L_div_reservoir = {sp.sstr(symbols.L_div_reservoir)}")
    print()
    print("Combined source/divergence load:")
    print(f"  L_source_divergence = {sp.sstr(symbols.L_source_divergence)}")

    with out.derived_results():
        out.line(
            "source/divergence obstruction ledgers stated",
            StatusMark.OBLIGATION,
            f"L_source_divergence = {sp.sstr(symbols.L_source_divergence)}",
        )


def case_2_problem_items(items: List[ProblemItem], out: ScriptOutput) -> None:
    header("Case 2: Source/divergence problem items")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Item: {item.item}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Meaning: {item.meaning}")

    with out.governance_assessments():
        out.line(
            "source/divergence problem items classified",
            StatusMark.DEFER,
            f"{len(items)} problem items classified",
        )


def case_3_ledgers(items: List[LedgerEntry], out: ScriptOutput) -> None:
    header("Case 3: Source/divergence ledgers")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Expression: {item.expression}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Requirement: {item.requirement}")
        print(f"Forbidden use: {item.forbidden_use}")

    with out.unresolved_obligations():
        out.line(
            "source/divergence ledgers opened",
            StatusMark.OBLIGATION,
            f"{len(items)} source/divergence ledgers opened",
        )


def case_4_rejected_routes(items: List[RejectedRoute], out: ScriptOutput) -> None:
    header("Case 4: Rejected source/divergence routes")
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
            "rejected source/divergence routes stated",
            StatusMark.FAIL,
            "postulate adoption, source repair, divergence reservoir, recovery selection, active-O convenience, parent fit, and insertion shortcut rejected",
        )


def case_5_obligations(items: List[InitialObligation], out: ScriptOutput) -> None:
    header("Case 5: Initial source/divergence obligations")
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
            "initial source/divergence obligations stated",
            StatusMark.OBLIGATION,
            f"{len(items)} obligations opened",
        )


def case_6_conclusions(items: List[InitialConclusion], out: ScriptOutput) -> None:
    header("Case 6: Initial source/divergence conclusions")
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
            "source/divergence problem ledger conclusion stated",
            StatusMark.PASS,
            "route opened; no postulate adopted; no insertion derived",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Source/divergence problem ledger result:")
    print()
    print("  Group 31 is opened as the source/divergence coefficient-law theorem route.")
    print("  Group 30 is treated as completed inventory/obstruction, not as postulate adoption.")
    print("  No postulate is adopted.")
    print("  Duplicate-source and divergence-reservoir ledgers are explicit.")
    print("  Source no-double-counting remains theorem-route preferred.")
    print("  Divergence-safe coefficient behavior remains theorem-route preferred.")
    print("  Trace/residual incidence remains high-risk.")
    print("  B_s/F_zeta insertion is not derived.")
    print("  Active O, residual control, and parent equation remain not ready.")
    print()
    print("Possible next script:")
    print("  candidate_source_duplicate_load_ledger.py")
    print()
    print("Tiny goblin label:")
    print("  Try to forge the key from flow, not declare a tooth.")

    with out.governance_assessments():
        out.line(
            "source/divergence problem ledger complete",
            StatusMark.PASS,
            "duplicate source load ledger should run next",
        )


def record_derivations(ns, symbols: SourceDivergenceSymbols) -> None:
    ns.record_derivation(
        derivation_id="g31_source_divergence_problem",
        inputs=[
            symbols.rho_coeff,
            symbols.rho_zeta_res,
            symbols.rho_kappa_res,
            symbols.rho_boundary,
            symbols.rho_corr,
            symbols.R_div,
            symbols.hidden_source,
            symbols.hidden_boundary,
            symbols.hidden_current,
            symbols.hidden_mass,
            symbols.hidden_support,
        ],
        output=symbols.L_source_divergence,
        method="open source/divergence coefficient-law theorem route and define obstruction ledgers",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="source_divergence_problem_marker",
        scope="Group 31 source/divergence coefficient law",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g31_dup_source_ledger", "Inventory duplicate ordinary source loads"),
        ("g31_coeff_source_neutrality", "Test coefficient source neutrality"),
        ("g31_div_reservoir", "Test divergence reservoir obstruction"),
        ("g31_nonreservoir_explicitness", "Classify non-reservoir divergence explicitness"),
        ("g31_trace_norm_fork", "Test trace normalization from source/divergence constraints"),
        ("g31_no_postulate_adoption", "Do not adopt Group 30 candidates"),
        ("g31_downstream_closed", "Keep insertion/O/residual/parent gates closed"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g31_source_divergence_route"],
            description=(
                "Group 31 opens the source/divergence coefficient-law theorem route. No postulate is adopted and no downstream theorem is derived."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g31_dup_source_ledger",
        "g31_coeff_source_neutrality",
        "g31_div_reservoir",
        "g31_nonreservoir_explicitness",
        "g31_trace_norm_fork",
        "g31_no_postulate_adoption",
        "g31_downstream_closed",
    ]

    ns.record_route(RouteRecord(
        route_id="g31_source_divergence_route",
        script_id=SCRIPT_ID,
        name="Group 31 source/divergence coefficient-law theorem route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "Group 30 inventory is completed but no postulate is adopted",
            "duplicate source load ledger is explicit",
            "divergence reservoir ledger is explicit",
            "source no-double-counting is theorem-route preferred",
            "divergence-safe coefficient behavior is theorem-route preferred",
            "B_s/F_zeta insertion remains not ready",
            "active O, residual control, and parent equation remain closed",
        ],
    ))

    for branch_id in [
        "postulate_adoption_by_source_divergence",
        "source_repair_selected_coefficient",
        "divergence_reservoir_correction",
        "recovery_selected_source_divergence_law",
        "active_O_convenience_selected_law",
        "parent_fit_selected_law",
        "source_divergence_as_insertion",
        "source_divergence_as_parent_readiness",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; source/divergence route is not adoption, repair, insertion, or parent closure.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g31_source_divergence_problem_opened",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Group 31 opens the source/divergence coefficient-law theorem route. Group 30 is treated as completed inventory/obstruction, not postulate adoption. "
            "No postulate is adopted. Duplicate-source and divergence-reservoir ledgers are explicit. Source no-double-counting and divergence-safe coefficient behavior remain theorem-route preferred. "
            "Trace/residual incidence remains high-risk. B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready."
        ),
        derivation_ids=["g31_source_divergence_problem"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Source Divergence Problem Ledger")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    problem_items = build_problem_items()
    ledgers = build_ledgers(symbols)
    rejected_routes = build_rejected_routes()
    obligations = build_obligations()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_symbolic_ledger(symbols, out)
    case_2_problem_items(problem_items, out)
    case_3_ledgers(ledgers, out)
    case_4_rejected_routes(rejected_routes, out)
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
