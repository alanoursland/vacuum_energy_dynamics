from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

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

# Group:
#   38_trace_anchor_explicit_declaration_record
# Script type:
#   SIEVE / EXPLICIT BRANCH-CHOICE ROUTE
#
# Purpose:
#   After the B_s notation split, classify explicit branch-choice routes.
#   This script may record a chosen branch only if CONFIGURED_BRANCH is set
#   deliberately. By default it leaves the active branch deferred.

SCRIPT_LABEL = "Candidate B_s Explicit Branch Choice Sieve"
MARKER_ID = "g38_bs_branch_choice"

DEPENDENCIES = [
    ("g38_bs_split", "038_trace_anchor_explicit_declaration_record__candidate_Bs_notation_split_declaration", "g38_bs_split_decl"),
    ("g38_bs_repair", "038_trace_anchor_explicit_declaration_record__candidate_Bs_notation_conflict_repair", "g38_bs_conflict_repair"),
    ("g38_bs_usage", "038_trace_anchor_explicit_declaration_record__candidate_Bs_actual_notation_usage_collector", "g38_bs_usage"),
    ("g38_recon", "038_trace_anchor_explicit_declaration_record__candidate_trace_anchor_declaration_batch_reconciliation", "g38_recon"),
]

# Configuration:
# Leave None to keep Group 38 declaration deferred.
# Set to exactly one of the allowed values only by explicit user/theory choice.
#
# Allowed values:
#   None
#   "metric_coefficient"
#   "scale_factor"
CONFIGURED_BRANCH: Optional[str] = None


@dataclass(frozen=True)
class BranchRoute:
    name: str
    branch: str
    object_name: str
    normalization: str
    status: str
    allowed_if: str
    blocked_if: str
    consequence: str


@dataclass(frozen=True)
class Rule:
    name: str
    rule: str
    reason: str


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


def prepare_archive(dependencies):
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    for dep_id, upstream_script_id, upstream_derivation_id in dependencies:
        ns.declare_dependency(
            dependency_id=dep_id,
            upstream_script_id=upstream_script_id,
            upstream_derivation_id=upstream_derivation_id,
            expected_record_kind=RecordKind.INVENTORY_MARKER,
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


def mark(status: str) -> StatusMark:
    return {
        "PASS": StatusMark.PASS,
        "CHOSEN": StatusMark.PASS,
        "BRANCH_CHOSEN": StatusMark.PASS,
        "DECLARATION_READY": StatusMark.INFO,
        "DECLARATION_DEFERRED": StatusMark.DEFER,
        "EXPLICIT_CHOICE": StatusMark.DEFER,
        "NOT_CHOSEN": StatusMark.DEFER,
        "CONFLICT": StatusMark.FAIL,
        "REJECTED": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
    }.get(status, StatusMark.INFO)


def record_marker(ns, marker_id: str, symbol_name: str):
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[],
        output=sp.Symbol(symbol_name),
        method="explicit branch-choice route marker; no physical derivation",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
        scope="Group 38 B_s explicit branch-choice sieve",
    )


def record_claim(ns, claim_id: str, marker_id: str, status, statement: str):
    ns.record_claim(
        ClaimRecord(
            claim_id=claim_id,
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=status,
            statement=statement,
            derivation_ids=[marker_id],
            obligation_ids=[],
        )
    )


def record_obligation(ns, obligation_id: str, marker_id: str, description: str, status=ObligationStatus.OPEN):
    ns.record_obligation(
        ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=obligation_id,
            status=status,
            required_by=[SCRIPT_ID],
            description=description,
        )
    )


def build_routes() -> List[BranchRoute]:
    return [
        BranchRoute(
            name="B1: metric-coefficient branch",
            branch="metric_coefficient",
            object_name="B_s_metric",
            normalization="log(B_s_metric)=2*zeta/d",
            status="EXPLICIT_CHOICE",
            allowed_if="theory owner explicitly chooses the metric-coefficient branch after notation split",
            blocked_if="choice is justified by recovery, hit count, insertion convenience, or parent fit",
            consequence="can feed later trace-normalization declaration attempt as declared candidate only",
        ),
        BranchRoute(
            name="B2: scale-factor branch",
            branch="scale_factor",
            object_name="b_s_scale",
            normalization="log(b_s_scale)=zeta/d",
            status="EXPLICIT_CHOICE",
            allowed_if="theory owner explicitly chooses the scale-factor branch after notation split",
            blocked_if="choice is justified by recovery, hit count, insertion convenience, or parent fit",
            consequence="can feed later trace-normalization declaration attempt as declared candidate only",
        ),
        BranchRoute(
            name="B3: no branch chosen",
            branch="none",
            object_name="F_zeta neutral placeholder",
            normalization="none installed",
            status="DECLARATION_DEFERRED",
            allowed_if="theory owner is not ready to choose either named branch",
            blocked_if="later scripts pretend a branch was chosen",
            consequence="Group 38 declaration remains deferred; further exploration or explicit decision needed",
        ),
    ]


def build_rules() -> List[Rule]:
    return [
        Rule(
            name="R1: explicit choice only",
            rule="A branch may be chosen only by explicit user/theory decision or a later named declaration record.",
            reason="The actual usage collector found conflicting notation evidence, so evidence inventory alone cannot choose.",
        ),
        Rule(
            name="R2: branch choice is not adoption",
            rule="Choosing a notation branch, if it occurs, creates a declared-candidate surface only.",
            reason="Package B adoption requires a separate explicit adoption decision.",
        ),
        Rule(
            name="R3: branch choice is not theorem proof",
            rule="Choosing metric_coefficient or scale_factor does not prove trace normalization.",
            reason="A declaration fixes terms; it does not derive the law.",
        ),
        Rule(
            name="R4: downstream gates stay closed",
            rule="Branch-choice clarity does not license B_s/F_zeta insertion, active O, residual control, or parent closure.",
            reason="Those remain downstream theorem targets.",
        ),
    ]


def branch_result() -> str:
    if CONFIGURED_BRANCH is None:
        return "DECLARATION_DEFERRED"
    if CONFIGURED_BRANCH in {"metric_coefficient", "scale_factor"}:
        return "BRANCH_CHOSEN"
    return "CONFLICT"


def chosen_route(routes: List[BranchRoute]) -> Optional[BranchRoute]:
    for route in routes:
        if route.branch == CONFIGURED_BRANCH:
            return route
    return None


def case_0(out):
    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  After splitting B_s notation into metric-coefficient and scale-factor objects,")
    print("  is an active declaration branch explicitly chosen, or does Group 38 remain deferred?")
    print("\nDiscipline:\n")
    print("  This script classifies branch-choice routes.")
    print("  It does not choose from evidence counts, recovery, insertion, or parent fit.")
    print("  It installs a branch only if CONFIGURED_BRANCH is deliberately set.")
    print("  It adopts no Package B component and opens no downstream gate.")
    print("\nTiny goblin rule:\n  Pick a jar only if the owner points to it. Do not sniff and pretend it chose itself.")
    with out.governance_assessments():
        out.line("B_s explicit branch-choice sieve opened", StatusMark.PASS, "branch choice is explicit-or-deferred only")


def case_1(out):
    header("Case 1: Symbolic branch-choice ledger")
    B_metric, B_scale, B_defer, B_conflict = sp.symbols("B_metric B_scale B_defer B_conflict")
    P_insertion, P_active_O, P_residual_kill, P_parent = sp.symbols("P_insertion P_active_O P_residual_kill P_parent")
    L_branch_choice = sp.simplify(B_metric + B_scale + B_defer + B_conflict)
    L_downstream = sp.simplify(P_insertion + P_active_O + P_residual_kill + P_parent)
    print(f"Branch-choice load: L_branch_choice = {L_branch_choice}")
    print(f"Downstream closed load: L_downstream_closed = {L_downstream}")
    with out.derived_results():
        out.line("B_s branch-choice symbolic ledger stated", StatusMark.PASS, f"L_branch_choice={L_branch_choice}; L_downstream_closed={L_downstream}")


def case_2(out, routes):
    header("Case 2: Branch-choice routes")
    for item in routes:
        subheader(item.name)
        print(f"Branch: {item.branch}")
        print(f"Object: {item.object_name}")
        print(f"Candidate normalization: {item.normalization}")
        print(f"Allowed if: {item.allowed_if}")
        print(f"Blocked if: {item.blocked_if}")
        print(f"Consequence: {item.consequence}")
        with out.governance_assessments():
            out.line(item.name, mark(item.status), f"{item.status}: {item.consequence}")


def case_3(out, routes):
    header("Case 3: Configured branch classification")
    print(f"CONFIGURED_BRANCH = {CONFIGURED_BRANCH!r}")
    result = branch_result()
    route = chosen_route(routes)
    if result == "BRANCH_CHOSEN" and route is not None:
        detail = f"explicit branch selected: {route.branch}; object={route.object_name}; normalization={route.normalization}; declared candidate only"
    elif result == "DECLARATION_DEFERRED":
        detail = "no active branch chosen; Group 38 declaration remains deferred"
    else:
        detail = "invalid branch configuration; must be None, metric_coefficient, or scale_factor"
    with out.governance_assessments():
        out.line("configured B_s branch classified", mark(result), f"{result}: {detail}")


def case_4(out, rules):
    header("Case 4: Branch-choice governance rules")
    for item in rules:
        subheader(item.name)
        print(f"Rule: {item.rule}")
        print(f"Reason: {item.reason}")
        with out.governance_assessments():
            out.line(item.name, StatusMark.OBLIGATION, f"POLICY_RULE: {item.rule} Reason: {item.reason}")


def case_5(out):
    header("Case 5: Invalid branch-choice upgrades")
    shortcuts = [
        ("X1: branch by hit count", "choose branch by majority of collector hits", "hit counts are not context-quality theorem or declaration source"),
        ("X2: branch by recovery", "choose branch because Schwarzschild, gamma, AB=1, or parent fit works", "recovery is audit, not declaration source"),
        ("X3: branch choice as adoption", "treat selected branch as adopted Package B", "adoption requires separate decision"),
        ("X4: branch choice as theorem", "treat selected branch as derived normalization", "declaration is not proof"),
        ("X5: branch choice as insertion", "treat selected branch as B_s/F_zeta insertion readiness", "downstream gates remain closed"),
    ]
    for name, shortcut, reason in shortcuts:
        subheader(name)
        print(f"Shortcut: {shortcut}")
        with out.counterexamples():
            out.line(name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {reason}")


def case_6(out):
    header("Case 6: Local conclusions")
    result = branch_result()
    with out.governance_assessments():
        if result == "BRANCH_CHOSEN":
            out.line("B_s branch explicitly chosen", StatusMark.PASS, f"{CONFIGURED_BRANCH}; declared candidate only, not adoption or theorem")
            out.line("trace-normalization declaration can be retried", StatusMark.DEFER, "next script may fill normalization fields under explicit branch")
        elif result == "DECLARATION_DEFERRED":
            out.line("B_s branch remains deferred", StatusMark.DEFER, "no explicit branch configured; Group 38 remains declaration-deferred")
            out.line("more exploration or explicit choice needed", StatusMark.DEFER, "do not rerun declaration completion as if branch is chosen")
        else:
            out.line("B_s branch configuration conflict", StatusMark.FAIL, "repair CONFIGURED_BRANCH before proceeding")
        out.line("downstream gates remain closed", StatusMark.DEFER, "branch-choice sieve is not insertion, active O, residual control, or parent readiness")


def record_governance(ns, routes, rules):
    record_marker(ns, MARKER_ID, "g38_Bs_explicit_branch_choice_classified")
    for idx, item in enumerate(routes, 1):
        record_claim(
            ns,
            f"g38_bs_branch_route_{idx}",
            MARKER_ID,
            GovernanceStatus.POLICY_RULE,
            f"{item.name}: branch={item.branch}; object={item.object_name}; normalization={item.normalization}; status={item.status}; consequence={item.consequence}",
        )
    for idx, item in enumerate(rules, 1):
        record_claim(
            ns,
            f"g38_bs_branch_rule_{idx}",
            MARKER_ID,
            GovernanceStatus.POLICY_RULE,
            f"{item.name}: {item.rule} Reason: {item.reason}",
        )
    result = branch_result()
    if result == "BRANCH_CHOSEN":
        record_obligation(
            ns,
            "g38_bs_branch_declared_candidate_only",
            MARKER_ID,
            "Carry explicit B_s branch choice as declared candidate only; do not treat as adoption, theorem proof, or insertion.",
            ObligationStatus.OPEN,
        )
    else:
        record_obligation(
            ns,
            "g38_bs_branch_choice_needed",
            MARKER_ID,
            "Choose metric_coefficient or scale_factor explicitly in a later record, or close Group 38 as declaration-deferred.",
            ObligationStatus.OPEN,
        )
    record_obligation(
        ns,
        "g38_bs_branch_downstream_closed",
        MARKER_ID,
        "Keep B_s/F_zeta insertion, active O, residual control, and parent closure closed after branch-choice classification.",
        ObligationStatus.DEFERRED,
    )


def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    routes = build_routes()
    rules = build_rules()
    case_0(out)
    case_1(out)
    case_2(out, routes)
    case_3(out, routes)
    case_4(out, rules)
    case_5(out)
    case_6(out)
    record_governance(ns, routes, rules)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
