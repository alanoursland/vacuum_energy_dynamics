# Candidate trace-normalization origin problem
#
# Group:
#   33_trace_normalization_candidate_origin
#
# Human title:
#   Trace Normalization Candidate Origin
#
# Script type:
#   PROBLEM LEDGER / ORIGIN-ROUTE OPENER
#
# Purpose
# -------
# Open the trace-normalization candidate-origin route.
# Define admissible origin routes, forbidden selector routes, and initial
# obligations for asking how B_s reads zeta without selecting the answer from
# recovery, repair, insertion, active O, or parent fit.
#
# Locked-door question:
#
#   Can the trace normalization rule for how B_s reads zeta be derived,
#   structurally constrained, or honestly left open without selecting it from
#   recovery, repair, insertion, active O, or parent fit?
#
# This script does not adopt trace normalization.
# It does not derive trace normalization.
# It does not derive safe trace membership.
# It does not derive trace/residual incidence.
# It does not derive the complete B_s/F_zeta coefficient law.
# It does not derive B_s/F_zeta insertion.
# It does not derive active O.
# It does not derive residual control.
# It does not open the parent equation.
#
# Tiny goblin rule:
#
#   Find the cup shape before pouring the trace.

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


def subheader(title: str) -> None:
    print()
    print("-" * 120)
    print(title)
    print("-" * 120)


def status_mark(status: str) -> StatusMark:
    return {
        "ADMISSIBLE_ORIGIN_ROUTE": StatusMark.INFO,
        "CANDIDATE_REMAINS": StatusMark.DEFER,
        "COMPATIBILITY_ONLY": StatusMark.INFO,
        "CONSTRAINED_CANDIDATE": StatusMark.INFO,
        "DEPENDENCY_SATISFIED": StatusMark.INFO,
        "EXPLICIT_CHOICE_REQUIRED": StatusMark.OBLIGATION,
        "FORBIDDEN_SELECTOR": StatusMark.FAIL,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "ORIGIN_ROUTE": StatusMark.INFO,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REJECTED_AS_SELECTOR": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "THEOREM_TARGET": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g32_summary",
            "32_explicit_minimal_postulate_selection__candidate_group_32_status_summary",
            "g32_status_summary",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g32_minimality",
            "32_explicit_minimal_postulate_selection__candidate_postulate_package_minimality",
            "g32_postulate_package_minimality",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g32_candidate_ledger",
            "32_explicit_minimal_postulate_selection__candidate_postulate_candidate_ledger",
            "g32_candidate_postulate_ledger",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_trace_norm",
            "31_source_divergence_coefficient_law__candidate_trace_normalization_from_source_divergence",
            "g31_trace_normalization_fork",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_summary",
            "31_source_divergence_coefficient_law__candidate_group_31_status_summary",
            "g31_status_summary",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g30_summary",
            "30_minimal_coefficient_sector_postulate_inventory__candidate_group_30_status_summary",
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
class OriginSymbols:
    N_trace: sp.Symbol
    O_volume_trace: sp.Symbol
    O_determinant_split: sp.Symbol
    O_dimension_count: sp.Symbol
    O_linear_trace: sp.Symbol
    C_source_neutral: sp.Symbol
    C_div_explicit: sp.Symbol
    C_safe_membership: sp.Symbol
    S_recovery: sp.Symbol
    S_repair: sp.Symbol
    S_hidden_source: sp.Symbol
    S_insertion: sp.Symbol
    S_active_O: sp.Symbol
    S_parent: sp.Symbol
    L_admissible_origins: sp.Expr
    L_compatibility_checks: sp.Expr
    L_forbidden_selectors: sp.Expr
    L_origin_problem_gap: sp.Expr


@dataclass
class OriginRoute:
    name: str
    route: str
    status: str
    allowed_use: str
    forbidden_use: str
    next_test: str


@dataclass
class SelectorRejection:
    name: str
    selector: str
    status: str
    reason: str
    allowed_future_use: str


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


def build_symbols() -> OriginSymbols:
    (
        N_trace,
        O_volume_trace,
        O_determinant_split,
        O_dimension_count,
        O_linear_trace,
        C_source_neutral,
        C_div_explicit,
        C_safe_membership,
        S_recovery,
        S_repair,
        S_hidden_source,
        S_insertion,
        S_active_O,
        S_parent,
    ) = sp.symbols(
        "N_trace O_volume_trace O_determinant_split O_dimension_count O_linear_trace "
        "C_source_neutral C_div_explicit C_safe_membership "
        "S_recovery S_repair S_hidden_source S_insertion S_active_O S_parent",
        real=True,
    )

    L_admissible_origins = sp.simplify(
        O_volume_trace
        + O_determinant_split
        + O_dimension_count
        + O_linear_trace
    )

    L_compatibility_checks = sp.simplify(
        C_source_neutral
        + C_div_explicit
        + C_safe_membership
    )

    L_forbidden_selectors = sp.simplify(
        S_recovery
        + S_repair
        + S_hidden_source
        + S_insertion
        + S_active_O
        + S_parent
    )

    L_origin_problem_gap = sp.simplify(
        N_trace
        + L_admissible_origins
        + L_compatibility_checks
        + L_forbidden_selectors
    )

    return OriginSymbols(
        N_trace=N_trace,
        O_volume_trace=O_volume_trace,
        O_determinant_split=O_determinant_split,
        O_dimension_count=O_dimension_count,
        O_linear_trace=O_linear_trace,
        C_source_neutral=C_source_neutral,
        C_div_explicit=C_div_explicit,
        C_safe_membership=C_safe_membership,
        S_recovery=S_recovery,
        S_repair=S_repair,
        S_hidden_source=S_hidden_source,
        S_insertion=S_insertion,
        S_active_O=S_active_O,
        S_parent=S_parent,
        L_admissible_origins=L_admissible_origins,
        L_compatibility_checks=L_compatibility_checks,
        L_forbidden_selectors=L_forbidden_selectors,
        L_origin_problem_gap=L_origin_problem_gap,
    )


def build_origin_routes() -> List[OriginRoute]:
    return [
        OriginRoute(
            name="O1: volume-trace definition",
            route="derive or constrain N_trace from a structural definition of zeta as volume trace",
            status="ADMISSIBLE_ORIGIN_ROUTE",
            allowed_use="candidate theorem route for how B_s reads zeta",
            forbidden_use="must not tune trace definition from AB=1, gamma recovery, insertion, or parent fit",
            next_test="define the trace object and reading rule before recovery audits",
        ),
        OriginRoute(
            name="O2: determinant / unimodular split",
            route="use a determinant/unimodular decomposition to isolate scalar trace normalization",
            status="ADMISSIBLE_ORIGIN_ROUTE",
            allowed_use="structural decomposition route if coefficient follows before recovery",
            forbidden_use="must not become residual kill, active O, or insertion by decomposition language",
            next_test="state determinant split, sector dimension, and whether result is exact or reduced",
        ),
        OriginRoute(
            name="O3: dimensional counting",
            route="fix or constrain normalization from the number of trace dimensions or sector weights",
            status="ADMISSIBLE_ORIGIN_ROUTE",
            allowed_use="counting/convention route if the counted space is explicit",
            forbidden_use="must not choose the count after target coefficient or recovery is known",
            next_test="state the counted sector and compare to volume-trace convention",
        ),
        OriginRoute(
            name="O4: linearized trace convention",
            route="use first-order trace bookkeeping to constrain the normalization",
            status="ADMISSIBLE_ORIGIN_ROUTE",
            allowed_use="linearized candidate route or convention classifier",
            forbidden_use="must not promote first-order convention to exact insertion theorem",
            next_test="separate first-order trace convention from exact coefficient law",
        ),
        OriginRoute(
            name="O5: source-neutral compatibility",
            route="test whether candidate normalization remains compatible with inherited no-hidden-source discipline",
            status="COMPATIBILITY_ONLY",
            allowed_use="compatibility sieve after candidate forms are defined",
            forbidden_use="source neutrality must not select the normalization by repair",
            next_test="carry hidden-source selectors as forbidden selector load",
        ),
        OriginRoute(
            name="O6: divergence-explicitness compatibility",
            route="test whether candidate normalization remains compatible with explicit non-reservoir correction behavior",
            status="COMPATIBILITY_ONLY",
            allowed_use="compatibility sieve against non-reservoir correction discipline",
            forbidden_use="explicitness must not become trace-normalization theorem or divergence-safe law",
            next_test="keep explicitness weaker than divergence safety",
        ),
        OriginRoute(
            name="O7: safe-membership compatibility",
            route="test whether candidate normalization can coexist with zeta_Bs -> T_zeta membership",
            status="COMPATIBILITY_ONLY",
            allowed_use="compatibility relation between Package B components",
            forbidden_use="membership must not choose normalization or imply incidence",
            next_test="keep normalization and membership as separate nodes",
        ),
    ]


def build_selector_rejections() -> List[SelectorRejection]:
    return [
        SelectorRejection(
            name="S1: recovery selector",
            selector="choose N_trace because AB=1, B=1/A, Schwarzschild, weak-field, gamma/PPN, or kappa=0 works",
            status="REJECTED_AS_SELECTOR",
            reason="recovery may audit after construction but cannot choose the normalization",
            allowed_future_use="post-construction recovery check only",
        ),
        SelectorRejection(
            name="S2: repair selector",
            selector="choose N_trace because it repairs source, divergence, boundary, residual, or coefficient failure",
            status="REJECTED_AS_SELECTOR",
            reason="failure may reject bad candidates but not select the normalization",
            allowed_future_use="negative filter only",
        ),
        SelectorRejection(
            name="S3: hidden-source selector",
            selector="choose N_trace to hide or cancel ordinary source load in coefficient or residual channels",
            status="REJECTED_AS_SELECTOR",
            reason="ordinary source load must remain visible and may not pick the trace normalization",
            allowed_future_use="source-neutral compatibility test only",
        ),
        SelectorRejection(
            name="S4: insertion selector",
            selector="choose N_trace because it makes B_s/F_zeta insertion work",
            status="REJECTED_AS_SELECTOR",
            reason="insertion is downstream and not ready",
            allowed_future_use="conditional precondition audit only after adoption or theorem support",
        ),
        SelectorRejection(
            name="S5: active-O selector",
            selector="choose N_trace because it makes no-overlap operator O easier to state",
            status="REJECTED_AS_SELECTOR",
            reason="active O is not constructed and cannot select upstream normalization",
            allowed_future_use="future compatibility check only after O is constructed",
        ),
        SelectorRejection(
            name="S6: parent-fit selector",
            selector="choose N_trace because it helps close the parent equation",
            status="REJECTED_AS_SELECTOR",
            reason="parent field equation is not ready and cannot choose trace normalization",
            allowed_future_use="future parent audit only after upstream gates close",
        ),
    ]


def build_obligations() -> List[InitialObligation]:
    return [
        InitialObligation(
            name="O1: origin route ledger",
            obligation="inventory admissible non-recovery origin routes for trace normalization",
            status="OPEN",
            blocks="candidate-form testing",
            discipline="origin route is not adoption",
        ),
        InitialObligation(
            name="O2: selector rejection ledger",
            obligation="reject recovery, repair, hidden-source, insertion, active-O, and parent-fit selectors",
            status="OPEN",
            blocks="normalization drift",
            discipline="bad selector may reject candidates but not choose one",
        ),
        InitialObligation(
            name="O3: candidate form visibility",
            obligation="define candidate normalization forms or families before compatibility tests",
            status="OPEN",
            blocks="compatibility sieve",
            discipline="do not hide normalization in prose",
        ),
        InitialObligation(
            name="O4: compatibility boundary",
            obligation="separate structural derivation from source/divergence/membership compatibility",
            status="OPEN",
            blocks="theorem overclaim",
            discipline="compatibility is not proof",
        ),
        InitialObligation(
            name="O5: adoption boundary",
            obligation="keep P_trace_norm unadopted unless a separate explicit decision is requested",
            status="REQUIRED",
            blocks="accidental adoption",
            discipline="candidate origin route is not explicit adoption",
        ),
        InitialObligation(
            name="O6: downstream gates",
            obligation="keep insertion, active O, residual control, and parent equation closed",
            status="NOT_READY",
            blocks="downstream overreach",
            discipline="trace-normalization origin is not insertion or parent closure",
        ),
    ]


def build_conclusions() -> List[InitialConclusion]:
    return [
        InitialConclusion(
            name="C1: route opened",
            conclusion="trace-normalization candidate-origin route is opened",
            status="ORIGIN_ROUTE",
            meaning="next route after Group 32 audit, without adoption",
        ),
        InitialConclusion(
            name="C2: no derivation yet",
            conclusion="this opener derives no trace-normalization rule",
            status="NOT_DERIVED",
            meaning="origin routes are listed, not solved",
        ),
        InitialConclusion(
            name="C3: selectors rejected",
            conclusion="recovery, repair, insertion, active-O, and parent-fit selectors are rejected",
            status="REQUIRED",
            meaning="normalization must not be chosen from target success or repair need",
        ),
        InitialConclusion(
            name="C4: no adoption",
            conclusion="this opener adopts no trace-normalization postulate",
            status="NOT_ADOPTED",
            meaning="separate explicit decision required for adoption",
        ),
        InitialConclusion(
            name="C5: downstream gates",
            conclusion="B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready",
            status="NOT_READY",
            meaning="origin problem does not open downstream gates",
        ),
        InitialConclusion(
            name="C6: next",
            conclusion="volume-trace / determinant / dimensional origin ledger should run next",
            status="OPEN",
            meaning="first concrete origin-route audit",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Trace-normalization origin problem")

    print("Question:")
    print()
    print("  Can the trace normalization rule for how B_s reads zeta be derived,")
    print("  structurally constrained, or honestly left open without selecting it from")
    print("  recovery, repair, insertion, active O, or parent fit?")
    print()
    print("Discipline:")
    print()
    print("  This script opens a candidate-origin route.")
    print("  It adopts no trace-normalization postulate.")
    print("  It derives no trace-normalization rule.")
    print("  It derives no coefficient law and no insertion.")
    print("  It keeps active O, residual control, and parent closure closed.")
    print()
    print("Tiny goblin rule:")
    print("  Find the cup shape before pouring the trace.")

    with out.governance_assessments():
        out.line(
            "trace-normalization origin route opened",
            StatusMark.INFO,
            "opening non-recovery origin route after Group 32 explicit-choice audit",
        )


def case_1_symbolic_ledger(symbols: OriginSymbols, out: ScriptOutput) -> None:
    header("Case 1: Trace-normalization origin symbolic ledger")

    print("Origin / compatibility / selector symbols:")
    print()
    for name in (
        "N_trace",
        "O_volume_trace",
        "O_determinant_split",
        "O_dimension_count",
        "O_linear_trace",
        "C_source_neutral",
        "C_div_explicit",
        "C_safe_membership",
        "S_recovery",
        "S_repair",
        "S_hidden_source",
        "S_insertion",
        "S_active_O",
        "S_parent",
    ):
        print(f"  {name} = {getattr(symbols, name)}")

    print()
    print("Admissible structural-origin load:")
    print(f"  L_admissible_origins = {symbols.L_admissible_origins}")
    print()
    print("Compatibility-check load:")
    print(f"  L_compatibility_checks = {symbols.L_compatibility_checks}")
    print()
    print("Forbidden selector load:")
    print(f"  L_forbidden_selectors = {symbols.L_forbidden_selectors}")
    print()
    print("Trace-normalization origin problem gap:")
    print(f"  L_origin_problem_gap = {symbols.L_origin_problem_gap}")

    with out.derived_results():
        out.line(
            "trace-normalization origin ledgers stated",
            StatusMark.OBLIGATION,
            f"L_admissible_origins = {symbols.L_admissible_origins}; L_forbidden_selectors = {symbols.L_forbidden_selectors}",
        )


def case_2_origin_routes(routes: List[OriginRoute], out: ScriptOutput) -> None:
    header("Case 2: Admissible origin and compatibility routes")

    for item in routes:
        subheader(item.name)
        print(f"Route: {item.route}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Allowed use: {item.allowed_use}")
        print(f"Forbidden use: {item.forbidden_use}")
        print(f"Next test: {item.next_test}")

    with out.governance_assessments():
        out.line(
            "trace-normalization origin routes initialized",
            StatusMark.INFO,
            f"{len(routes)} origin / compatibility routes initialized",
        )


def case_3_selector_rejections(rejections: List[SelectorRejection], out: ScriptOutput) -> None:
    header("Case 3: Rejected trace-normalization selector routes")

    for item in rejections:
        subheader(item.name)
        print(f"Selector: {item.selector}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Reason: {item.reason}")
        print(f"Allowed future use: {item.allowed_future_use}")

    with out.counterexamples():
        out.line(
            "trace-normalization selector shortcuts rejected",
            StatusMark.FAIL,
            "recovery, repair, hidden-source, insertion, active-O, and parent-fit selectors rejected",
        )


def case_4_obligations(obligations: List[InitialObligation], out: ScriptOutput) -> None:
    header("Case 4: Initial trace-normalization origin obligations")

    for item in obligations:
        subheader(item.name)
        print(f"Obligation: {item.obligation}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Blocks: {item.blocks}")
        print(f"Discipline: {item.discipline}")

    with out.unresolved_obligations():
        out.line(
            "initial trace-normalization origin obligations stated",
            StatusMark.OBLIGATION,
            f"{len(obligations)} obligations opened",
        )


def case_5_conclusions(conclusions: List[InitialConclusion], out: ScriptOutput) -> None:
    header("Case 5: Initial trace-normalization origin conclusions")

    for item in conclusions:
        subheader(item.name)
        print(f"Conclusion: {item.conclusion}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Meaning: {item.meaning}")

    with out.governance_assessments():
        out.line(
            "trace-normalization origin problem conclusion stated",
            StatusMark.PASS,
            "origin route opened; no normalization adopted; selector shortcuts rejected; downstream gates closed",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")

    print("Trace-normalization origin opener result:")
    print()
    print("  Group 33 is opened as a candidate-origin route for P_trace_norm.")
    print("  The route asks whether how B_s reads zeta can be derived or structurally constrained.")
    print("  Volume-trace, determinant/unimodular, dimension-counting, and linearized-trace routes are admissible to test.")
    print("  Source-neutral, divergence-explicit, and safe-membership relations are compatibility checks only.")
    print("  Recovery, repair, hidden-source, insertion, active-O, and parent-fit selectors are rejected.")
    print("  No trace-normalization rule is derived or adopted by this opener.")
    print("  B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready.")
    print()
    print("Possible next script:")
    print("  candidate_trace_normalization_volume_trace_ledger.py")
    print()
    print("Tiny goblin label:")
    print("  Find the cup shape before pouring the trace.")

    with out.governance_assessments():
        out.line(
            "trace-normalization origin opener complete",
            StatusMark.PASS,
            "volume-trace / determinant / dimensional origin ledger should run next",
        )


def record_inventory_marker(ns, symbols: OriginSymbols) -> None:
    ns.record_derivation(
        derivation_id="g33_trace_normalization_origin_problem",
        inputs=[
            symbols.N_trace,
            symbols.O_volume_trace,
            symbols.O_determinant_split,
            symbols.O_dimension_count,
            symbols.O_linear_trace,
            symbols.C_source_neutral,
            symbols.C_div_explicit,
            symbols.C_safe_membership,
            symbols.S_recovery,
            symbols.S_repair,
            symbols.S_hidden_source,
            symbols.S_insertion,
            symbols.S_active_O,
            symbols.S_parent,
        ],
        output=symbols.L_origin_problem_gap,
        method="open trace-normalization origin route and classify origin/selector ledgers",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="trace_normalization_origin_problem_marker",
        scope="Group 33 trace-normalization candidate origin",
        is_placeholder=True,
    )


def record_obligations(ns, obligations: List[InitialObligation]) -> None:
    obligation_id_map = {
        "O1: origin route ledger": "g33_origin_route_ledger",
        "O2: selector rejection ledger": "g33_selector_rejection_ledger",
        "O3: candidate form visibility": "g33_candidate_form_visibility",
        "O4: compatibility boundary": "g33_compatibility_boundary",
        "O5: adoption boundary": "g33_adoption_boundary",
        "O6: downstream gates": "g33_downstream_gates_closed",
    }

    for item in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id_map[item.name],
            script_id=SCRIPT_ID,
            title=item.obligation,
            status=ObligationStatus.OPEN,
            required_by=["g33_trace_normalization_origin_problem"],
            description=f"{item.discipline} Blocks: {item.blocks}.",
        ))


def record_governance(
    ns,
    routes: List[OriginRoute],
    rejections: List[SelectorRejection],
    conclusions: List[InitialConclusion],
) -> None:
    obligation_ids = [
        "g33_origin_route_ledger",
        "g33_selector_rejection_ledger",
        "g33_candidate_form_visibility",
        "g33_compatibility_boundary",
        "g33_adoption_boundary",
        "g33_downstream_gates_closed",
    ]

    ns.record_route(RouteRecord(
        route_id="g33_trace_normalization_origin_route",
        script_id=SCRIPT_ID,
        name="Trace-normalization candidate-origin route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "Group 32 closed as explicit-choice audit",
            "Package B minimal plausible-to-audit only",
            "P_trace_norm remains candidate, not adopted",
            "normalization must not be selected from recovery or repair",
        ],
    ))

    for item in routes:
        ns.record_claim(ClaimRecord(
            claim_id=f"g33_origin_route_{item.name.split(':')[0].lower()}",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.CANDIDATE_ROUTE,
            statement=f"{item.route}. Allowed use: {item.allowed_use}. Forbidden use: {item.forbidden_use}.",
            derivation_ids=["g33_trace_normalization_origin_problem"],
            obligation_ids=obligation_ids,
        ))

    for item in rejections:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"g33_rejected_selector_{item.name.split(':')[0].lower()}",
            script_id=SCRIPT_ID,
            branch_id=item.selector,
            status=GovernanceStatus.POLICY_RULE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"{item.selector}. Reason: {item.reason}. Allowed future use: {item.allowed_future_use}.",
        ))

    for item in conclusions:
        status = GovernanceStatus.CANDIDATE_ROUTE
        if item.status in {"NOT_DERIVED", "NOT_ADOPTED", "NOT_READY", "OPEN"}:
            status = GovernanceStatus.DEFERRED_PENDING_PREREQUISITES
        elif item.status == "REQUIRED":
            status = GovernanceStatus.POLICY_RULE

        ns.record_claim(ClaimRecord(
            claim_id=f"g33_origin_conclusion_{item.name.split(':')[0].lower()}",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=status,
            statement=f"{item.conclusion}. Meaning: {item.meaning}.",
            derivation_ids=["g33_trace_normalization_origin_problem"],
            obligation_ids=obligation_ids,
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g33_trace_normalization_origin_problem_complete",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement=(
            "Group 33 is opened as a trace-normalization candidate-origin route. "
            "No normalization is derived or adopted. Recovery, repair, insertion, active-O, and parent-fit selectors are rejected. "
            "Downstream gates remain closed."
        ),
        derivation_ids=["g33_trace_normalization_origin_problem"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Trace-Normalization Origin Problem")
    archive, ns, invalidated = prepare_archive()
    ensure_archive_write_dirs(ns)
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    routes = build_origin_routes()
    rejections = build_selector_rejections()
    obligations = build_obligations()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_symbolic_ledger(symbols, out)
    case_2_origin_routes(routes, out)
    case_3_selector_rejections(rejections, out)
    case_4_obligations(obligations, out)
    case_5_conclusions(conclusions, out)
    final_interpretation(out)

    record_inventory_marker(ns, symbols)
    record_obligations(ns, obligations)
    record_governance(ns, routes, rejections, conclusions)

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
