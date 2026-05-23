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

ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"

# Group:
#   38_trace_anchor_explicit_declaration_record
# Script type:
#   RECONCILIATION / DEFERRED DECLARATION STATUS
#
# Purpose:
#   Reconcile the Group 38 explicit declaration attempt after notation conflict,
#   notation split, and branch-choice sieve. If no active branch has been chosen,
#   record that Group 38 remains declaration-deferred and that a final status
#   summary should close it as a deferred declaration attempt, not as a completed
#   declaration record.

SCRIPT_LABEL = "Candidate Trace Anchor Declaration Deferred Reconciliation"
MARKER_ID = "g38_decl_defer_recon"

DEPENDENCIES = [
    ("g38_recon", "38_trace_anchor_explicit_declaration_record__candidate_trace_anchor_declaration_batch_reconciliation", "g38_recon"),
    ("g38_bs_usage", "38_trace_anchor_explicit_declaration_record__candidate_Bs_actual_notation_usage_collector", "g38_bs_usage"),
    ("g38_bs_split", "38_trace_anchor_explicit_declaration_record__candidate_Bs_notation_split_declaration", "g38_bs_split_decl"),
    ("g38_bs_choice", "38_trace_anchor_explicit_declaration_record__candidate_Bs_explicit_branch_choice_sieve", "g38_bs_branch_choice"),
    ("g38_norm", "38_trace_anchor_explicit_declaration_record__candidate_trace_normalization_declaration_attempt", "g38_norm"),
    ("g38_mem", "38_trace_anchor_explicit_declaration_record__candidate_safe_membership_declaration_attempt", "g38_mem"),
    ("g38_joint", "38_trace_anchor_explicit_declaration_record__candidate_joint_trace_anchor_declaration_record", "g38_joint"),
]


@dataclass(frozen=True)
class ReconciliationEntry:
    name: str
    topic: str
    status: str
    result: str
    consequence: str


@dataclass(frozen=True)
class Handoff:
    name: str
    route: str
    status: str
    allowed_if: str
    caution: str


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
        "MATCHED": StatusMark.PASS,
        "DECLARATION_DEFERRED": StatusMark.DEFER,
        "DEFERRED": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "NOT_CHOSEN": StatusMark.DEFER,
        "NOT_DECLARED": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
        "CONFLICT_REPAIRED_BY_SPLIT": StatusMark.INFO,
        "COMPATIBLE_IF_DECLARED": StatusMark.INFO,
    }.get(status, StatusMark.INFO)


def record_marker(ns, marker_id: str, symbol_name: str):
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[],
        output=sp.Symbol(symbol_name),
        method="inventory marker; deferred declaration reconciliation; no physical derivation",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
        scope="Group 38 trace-anchor explicit declaration attempt",
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


def record_obligation(ns, obligation_id: str, title: str, description: str, status=ObligationStatus.OPEN):
    ns.record_obligation(
        ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=status,
            required_by=[SCRIPT_ID],
            description=description,
        )
    )


def build_entries() -> List[ReconciliationEntry]:
    return [
        ReconciliationEntry(
            "D1: original declaration attempt",
            "Group 38 opened an explicit declaration route",
            "MATCHED",
            "route opened as choice-tolerant; no automatic declaration made",
            "safe to summarize as declaration attempt, not completed declaration",
        ),
        ReconciliationEntry(
            "D2: B_s notation conflict",
            "actual usage collector found mixed metric-like and scale-like usage",
            "CONFLICT_REPAIRED_BY_SPLIT",
            "conflict required repair before convention could be chosen",
            "same B_s symbol must not carry both meanings silently",
        ),
        ReconciliationEntry(
            "D3: notation split",
            "B_s_metric and b_s_scale were separated as named objects",
            "PASS",
            "split repairs naming conflict but does not choose active branch",
            "two named jars exist; neither is poured from by default",
        ),
        ReconciliationEntry(
            "D4: branch choice",
            "explicit branch-choice sieve left CONFIGURED_BRANCH unset",
            "DECLARATION_DEFERRED",
            "no metric_coefficient or scale_factor branch was chosen",
            "Group 38 remains declaration-deferred",
        ),
        ReconciliationEntry(
            "D5: trace normalization",
            "normalization declaration attempt had no convention, zeta convention, dimension, or scope",
            "NOT_DECLARED",
            "normalization declaration remains incomplete",
            "no trace-normalization law is selected, declared, adopted, or derived",
        ),
        ReconciliationEntry(
            "D6: safe membership",
            "safe-membership declaration attempt had no membership form, object, sector, criterion, or scope",
            "NOT_DECLARED",
            "membership declaration remains incomplete",
            "no safe-membership claim is selected, declared, adopted, or derived",
        ),
        ReconciliationEntry(
            "D7: joint package",
            "joint declaration record had no chosen package",
            "DECLARATION_DEFERRED",
            "no joint Package B declaration surface is installed",
            "Package B remains compatible-if-declared only",
        ),
        ReconciliationEntry(
            "D8: downstream gates",
            "B_s/F_zeta insertion, active O, residual control, and parent closure",
            "NOT_READY",
            "all downstream gates remain closed",
            "deferred declaration is not field-equation readiness",
        ),
    ]


def build_handoffs() -> List[Handoff]:
    return [
        Handoff(
            "H1: Group 38 deferred status summary",
            "candidate_group_38_status_summary.py",
            "PASS",
            "summary closes Group 38 as declaration-deferred, not declaration-completed",
            "must preserve that no active branch or joint package was chosen",
        ),
        Handoff(
            "H2: explicit branch-choice record",
            "future explicit user/theory choice of metric_coefficient or scale_factor branch",
            "OPEN",
            "theory owner deliberately chooses one branch after notation split",
            "choice is declaration only, not adoption or theorem proof",
        ),
        Handoff(
            "H3: notation-quality source hierarchy",
            "optional evidence-quality script",
            "OPEN",
            "project wants to rank earliest or authoritative notation sources before branch choice",
            "must not cherry-pick recovery-facing evidence",
        ),
        Handoff(
            "H4: neutral F_zeta deferral",
            "keep F_zeta neutral until a branch is chosen",
            "DECLARATION_DEFERRED",
            "no concrete zeta/d or 2*zeta/d normalization is installed",
            "neutral notation cannot hide a convention choice",
        ),
        Handoff(
            "H5: downstream route",
            "B_s/F_zeta insertion or parent closure",
            "NOT_READY",
            "not available from Group 38 deferred result",
            "forbidden as immediate handoff",
        ),
    ]


def case_0(out):
    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  After the Group 38 declaration batch, notation conflict repair, notation split,")
    print("  and explicit branch-choice sieve, what is the honest current declaration status?")
    print("\nDiscipline:\n")
    print("  This script reconciles actual Group 38 exploration results.")
    print("  It does not choose a branch.")
    print("  It does not fill trace-normalization or safe-membership declarations.")
    print("  It does not adopt Package B or prove either component.")
    print("  It keeps insertion, active O, residual control, and parent closure closed.")
    print("\nTiny goblin rule:\n  The jars are labeled, but the owner has not picked one.")
    with out.governance_assessments():
        out.line(
            "Group 38 deferred reconciliation opened",
            StatusMark.PASS,
            "actual outputs support declaration-deferred close unless a later explicit choice is supplied",
        )


def case_1(out):
    header("Case 1: Deferred declaration symbolic ledger")
    split, branch_defer, norm_defer, mem_defer, joint_defer = sp.symbols(
        "split branch_defer norm_defer mem_defer joint_defer"
    )
    P_insertion, P_active_O, P_residual_kill, P_parent = sp.symbols(
        "P_insertion P_active_O P_residual_kill P_parent"
    )
    L_deferred = sp.simplify(split + branch_defer + norm_defer + mem_defer + joint_defer)
    L_downstream = sp.simplify(P_insertion + P_active_O + P_residual_kill + P_parent)
    L_gap = sp.simplify(L_deferred + L_downstream)
    print(f"Deferred declaration load: L_deferred = {L_deferred}")
    print(f"Downstream closed load: L_downstream_closed = {L_downstream}")
    print(f"Total local gap: L_gap = {L_gap}")
    with out.derived_results():
        out.line(
            "deferred declaration symbolic ledger stated",
            StatusMark.PASS,
            f"L_deferred={L_deferred}; L_downstream_closed={L_downstream}",
        )


def case_2(out, entries: List[ReconciliationEntry]):
    header("Case 2: Actual-output reconciliation entries")
    for item in entries:
        subheader(item.name)
        print(f"Topic: {item.topic}")
        print(f"Result: {item.result}")
        print(f"Consequence: {item.consequence}")
        with out.governance_assessments():
            out.line(item.name, mark(item.status), f"{item.status}: {item.result}. Consequence: {item.consequence}")


def case_3(out, handoffs: List[Handoff]):
    header("Case 3: Safe handoffs")
    for item in handoffs:
        subheader(item.name)
        print(f"Route: {item.route}")
        print(f"Allowed if: {item.allowed_if}")
        print(f"Caution: {item.caution}")
        with out.governance_assessments():
            out.line(item.name, mark(item.status), f"{item.status}: {item.allowed_if}. Caution: {item.caution}")


def case_4(out):
    header("Case 4: Invalid deferred-reconciliation upgrades")
    shortcuts = [
        ("X1: split as active declaration", "treat B_s_metric/b_s_scale split as choosing one branch", "split repairs naming only"),
        ("X2: deferred as failed theorem", "treat declaration deferral as mathematical failure", "deferral is governance status, not no-go theorem"),
        ("X3: deferred as hidden choice", "use F_zeta or prose to proceed as if a branch was chosen", "neutral notation cannot hide factor-of-two choice"),
        ("X4: declaration attempt as adoption", "treat declaration exploration as Package B adoption", "adoption requires separate decision"),
        ("X5: declaration attempt as insertion", "treat branch clarity or split as B_s/F_zeta insertion", "downstream gates remain closed"),
    ]
    for name, shortcut, reason in shortcuts:
        subheader(name)
        print(f"Shortcut: {shortcut}")
        with out.counterexamples():
            out.line(name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {reason}")


def case_5(out):
    header("Case 5: Local conclusions")
    with out.governance_assessments():
        out.line(
            "Group 38 declaration remains deferred",
            StatusMark.DEFER,
            "notation split exists but no active branch, normalization declaration, membership declaration, or joint package was chosen",
        )
        out.line(
            "Group 38 status summary is ready",
            StatusMark.PASS,
            "summary should close Group 38 as deferred declaration attempt unless user supplies an explicit branch choice first",
        )
        out.line(
            "downstream gates remain closed",
            StatusMark.DEFER,
            "deferred reconciliation is not insertion, active O, residual control, or parent readiness",
        )


def record_governance(ns, entries: List[ReconciliationEntry], handoffs: List[Handoff]):
    record_marker(ns, MARKER_ID, "g38_declaration_deferred_reconciled")
    for idx, item in enumerate(entries, 1):
        record_claim(
            ns,
            f"g38_defer_entry_{idx}",
            MARKER_ID,
            GovernanceStatus.POLICY_RULE,
            f"{item.name}: {item.topic}. Status: {item.status}. Result: {item.result}. Consequence: {item.consequence}.",
        )
    for idx, item in enumerate(handoffs, 1):
        record_claim(
            ns,
            f"g38_defer_handoff_{idx}",
            MARKER_ID,
            GovernanceStatus.POLICY_RULE,
            f"{item.name}: {item.route}. Status: {item.status}. Allowed if: {item.allowed_if}. Caution: {item.caution}.",
        )
    record_obligation(
        ns,
        "g38_obl_preserve_deferred_status",
        "Preserve Group 38 declaration-deferred status",
        "Do not report Group 38 as completed declaration unless a later explicit branch-choice/declaration record installs one active package.",
    )
    record_obligation(
        ns,
        "g38_obl_keep_downstream_closed",
        "Keep downstream gates closed",
        "B_s/F_zeta insertion, active O, residual control, and parent closure remain not ready after deferred reconciliation.",
        status=ObligationStatus.DEFERRED,
    )


def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    entries = build_entries()
    handoffs = build_handoffs()
    case_0(out)
    case_1(out)
    case_2(out, entries)
    case_3(out, handoffs)
    case_4(out)
    case_5(out)
    record_governance(ns, entries, handoffs)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
