from dataclasses import dataclass
from pathlib import Path
from typing import List

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

# Group:
#   38_trace_anchor_explicit_declaration_record
# Script type:
#   REPAIR / SIEVE

ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"
SCRIPT_LABEL = "Candidate B_s Notation Conflict Repair"
MARKER_ID = "g38_bs_conflict_repair"

DEPENDENCIES = [
    (
        "g38_bs_usage",
        "38_trace_anchor_explicit_declaration_record__candidate_Bs_actual_notation_usage_collector",
        "g38_bs_usage",
    ),
    (
        "g38_bs_evsrc",
        "38_trace_anchor_explicit_declaration_record__candidate_Bs_notation_evidence_source_inventory",
        "g38_bs_evsrc",
    ),
    (
        "g38_recon",
        "38_trace_anchor_explicit_declaration_record__candidate_trace_anchor_declaration_batch_reconciliation",
        "g38_recon",
    ),
]


@dataclass
class RepairRoute:
    name: str
    route: str
    status: str
    allowed_if: str
    blocked_if: str
    consequence: str


@dataclass
class Shortcut:
    name: str
    shortcut: str
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
        "REPAIR_READY": StatusMark.PASS,
        "SPLIT_RECOMMENDED": StatusMark.PASS,
        "EXPLICIT_CHOICE": StatusMark.DEFER,
        "DEFER": StatusMark.DEFER,
        "AMBIGUOUS": StatusMark.DEFER,
        "REJECTED": StatusMark.FAIL,
        "CONFLICT": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "NOT_READY": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def record_marker(ns, marker_id: str, symbol_name: str):
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[],
        output=sp.Symbol(symbol_name),
        method="inventory marker; no physical derivation",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
        scope="Group 38 B_s notation conflict repair",
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


def build_routes() -> List[RepairRoute]:
    return [
        RepairRoute(
            name="R1: notation split route",
            route="split ambiguous B_s usage into distinct named objects, e.g. B_s_metric and b_s_scale or equivalent",
            status="SPLIT_RECOMMENDED",
            allowed_if="existing metric-like and scale-like usages are both preserved but assigned distinct names before declaration",
            blocked_if="the same B_s symbol continues to carry both metric-coefficient and scale-factor meanings",
            consequence="best repair candidate; later declaration can choose one named object without hiding a factor of two",
        ),
        RepairRoute(
            name="R2: explicit theory-choice route",
            route="choose either metric-coefficient or scale-factor convention by explicit user/theory decision",
            status="EXPLICIT_CHOICE",
            allowed_if="the choice is recorded as declaration choice, not as evidence-derived theorem",
            blocked_if="choice is justified by recovery, insertion convenience, or parent fit",
            consequence="can complete the convention declaration if accepted, but remains a choice rather than proof",
        ),
        RepairRoute(
            name="R3: neutral F_zeta route",
            route="keep F_zeta as a neutral response placeholder while blocking concrete zeta/d or 2*zeta/d installation",
            status="DEFER",
            allowed_if="F_zeta is not used to hide the scale-vs-metric convention and no concrete normalization is installed",
            blocked_if="functional notation is treated as declaration completion",
            consequence="safe deferral route; declaration remains incomplete",
        ),
        RepairRoute(
            name="R4: source-priority route",
            route="restrict admissible evidence to the earliest notation-origin or explicitly authoritative summary source",
            status="AMBIGUOUS",
            allowed_if="a source hierarchy is itself justified before convention selection",
            blocked_if="later or recovery-facing hits are cherry-picked",
            consequence="possible later evidence-quality script, not enough here to choose convention",
        ),
        RepairRoute(
            name="R5: silent majority route",
            route="choose the convention with the most collector hits",
            status="REJECTED",
            allowed_if="never as convention selector",
            blocked_if="hit count is used as declaration evidence without context quality",
            consequence="rejected because broad scans count repeated snippets and recovery-facing contexts",
        ),
        RepairRoute(
            name="R6: immediate declaration route",
            route="declare B_s convention now despite conflict",
            status="REJECTED",
            allowed_if="never unless replaced by explicit theory-choice route with clear status",
            blocked_if="conflict is ignored or hidden",
            consequence="rejected as shortcut; repair or explicit choice must happen first",
        ),
    ]


def build_shortcuts() -> List[Shortcut]:
    return [
        Shortcut(
            name="X1: conflict as metric convention",
            shortcut="treat metric-like hits as decisive while ignoring scale-like and determinant-root hits",
            reason="collector found genuine mixed evidence; selective use hides conflict",
        ),
        Shortcut(
            name="X2: conflict as scale convention",
            shortcut="treat scale-like or determinant-root hits as decisive while ignoring inherited B metric usage",
            reason="root evidence still requires explicit convention and does not erase metric-like usage",
        ),
        Shortcut(
            name="X3: F_zeta as repair",
            shortcut="use F_zeta to avoid choosing or splitting the convention while installing a normalization",
            reason="neutral functional notation cannot hide the factor-of-two burden",
        ),
        Shortcut(
            name="X4: hit count as theorem",
            shortcut="declare the most frequent usage class as derived convention",
            reason="collector hit counts are evidence inventory, not theorem proof or declaration record",
        ),
        Shortcut(
            name="X5: repair as insertion",
            shortcut="treat notation repair as B_s/F_zeta insertion readiness",
            reason="insertion, active O, residual control, and parent closure remain downstream and not ready",
        ),
    ]


def case_0(out):
    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  How should the B_s notation conflict be repaired before Group 38 can")
    print("  install a trace-anchor declaration surface?")
    print("\nDiscipline:\n")
    print("  This script classifies repair routes only.")
    print("  It does not choose a B_s convention.")
    print("  It does not split notation by decree.")
    print("  It does not fill trace-normalization or safe-membership declarations.")
    print("  It does not adopt Package B, prove either component, or open insertion.")
    print("\nTiny goblin rule:\n  If two jar labels disagree, make two jars or ask the owner. Do not relabel in the dark.")
    with out.governance_assessments():
        out.line(
            "B_s notation conflict repair opened",
            StatusMark.PASS,
            "repair-route sieve only; no convention installed",
        )


def case_1(out):
    header("Case 1: Symbolic conflict-repair ledger")
    B_metric, B_scale, B_split, explicit_choice, F_neutral = sp.symbols("B_metric B_scale B_split explicit_choice F_neutral")
    silent_majority, immediate_declare, P_insertion, P_active_O, P_residual_kill, P_parent = sp.symbols(
        "silent_majority immediate_declare P_insertion P_active_O P_residual_kill P_parent"
    )
    L_conflict = sp.simplify(B_metric + B_scale)
    L_repairs = sp.simplify(B_split + explicit_choice + F_neutral)
    L_rejected = sp.simplify(silent_majority + immediate_declare)
    L_downstream = sp.simplify(P_insertion + P_active_O + P_residual_kill + P_parent)
    print(f"Notation conflict load: L_conflict = {L_conflict}")
    print(f"Repair route load: L_repairs = {L_repairs}")
    print(f"Rejected repair load: L_rejected = {L_rejected}")
    print(f"Downstream closed load: L_downstream_closed = {L_downstream}")
    with out.derived_results():
        out.line(
            "B_s conflict-repair symbolic ledger stated",
            StatusMark.PASS,
            f"L_repairs={L_repairs}; L_downstream_closed={L_downstream}",
        )


def case_2(out, routes: List[RepairRoute]):
    header("Case 2: Repair route classes")
    for item in routes:
        subheader(item.name)
        print(f"Route: {item.route}")
        with out.governance_assessments():
            out.line(
                item.name,
                mark(item.status),
                f"{item.status}: allowed if {item.allowed_if}; blocked if {item.blocked_if}; consequence: {item.consequence}",
            )


def case_3(out, shortcuts: List[Shortcut]):
    header("Case 3: Invalid conflict-repair shortcuts")
    for item in shortcuts:
        subheader(item.name)
        print(f"Shortcut: {item.shortcut}")
        with out.counterexamples():
            out.line(item.name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {item.reason}")


def case_4(out):
    header("Case 4: Repair obligations")
    obligations = [
        (
            "O1: preserve conflict visibility",
            "carry both metric-like and scale-like usage as real notation conflict until repaired",
            "hidden conflict",
        ),
        (
            "O2: prefer notation split or explicit choice",
            "repair must either split notation into distinct objects or record an explicit theory choice",
            "silent convention installation",
        ),
        (
            "O3: block F_zeta hiding",
            "F_zeta may remain neutral only if it does not install zeta/d or 2*zeta/d by implication",
            "factor-of-two smuggling",
        ),
        (
            "O4: downstream gates",
            "keep insertion, active O, residual control, and parent closure closed",
            "downstream overreach",
        ),
    ]
    for name, obligation, blocks in obligations:
        subheader(name)
        print(f"Obligation: {obligation}")
        with out.unresolved_obligations():
            out.line(name, StatusMark.DEFER, f"OPEN: blocks {blocks}")


def case_5(out):
    header("Case 5: Local conclusions")
    with out.governance_assessments():
        out.line(
            "B_s notation conflict repair classified",
            StatusMark.PASS,
            "notation split is the safest repair candidate; explicit theory choice remains possible; no convention installed",
        )
        out.line(
            "declaration remains blocked",
            StatusMark.DEFER,
            "write notation-split declaration or explicit convention-choice script before completing Group 38",
        )
        out.line(
            "downstream gates remain closed",
            StatusMark.DEFER,
            "repair classification is not declaration, adoption, theorem proof, insertion, active O, residual control, or parent readiness",
        )


def record_governance(ns, routes: List[RepairRoute], shortcuts: List[Shortcut]):
    record_marker(ns, MARKER_ID, "g38_bs_notation_conflict_repair")
    for idx, item in enumerate(routes, 1):
        status = GovernanceStatus.POLICY_RULE if item.status in {"SPLIT_RECOMMENDED", "REJECTED"} else GovernanceStatus.CANDIDATE_ROUTE
        record_claim(
            ns,
            f"g38_bs_repair_r{idx}",
            MARKER_ID,
            status,
            f"{item.name}: {item.route}. Status: {item.status}. Allowed if {item.allowed_if}. Blocked if {item.blocked_if}. Consequence: {item.consequence}.",
        )
    for idx, item in enumerate(shortcuts, 1):
        record_claim(
            ns,
            f"g38_bs_repair_x{idx}",
            MARKER_ID,
            GovernanceStatus.REJECTED_ROUTE,
            f"{item.name}: forbidden shortcut. {item.shortcut}. Reason: {item.reason}.",
        )
    record_obligation(
        ns,
        "g38_bs_repair_split_or_choose",
        MARKER_ID,
        "Resolve B_s notation conflict by explicit notation split or explicit theory choice before completing declaration record.",
    )
    record_obligation(
        ns,
        "g38_bs_repair_downstream_closed",
        MARKER_ID,
        "Keep B_s/F_zeta insertion, active O, residual control, and parent closure closed during notation repair.",
        status=ObligationStatus.DEFERRED,
    )


def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    routes = build_routes()
    shortcuts = build_shortcuts()
    case_0(out)
    case_1(out)
    case_2(out, routes)
    case_3(out, shortcuts)
    case_4(out)
    case_5(out)
    record_governance(ns, routes, shortcuts)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
