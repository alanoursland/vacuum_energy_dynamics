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
SCRIPT_LABEL = "Candidate Group 38 Status Summary"
MARKER_ID = "g38_summary"

DEPENDENCIES = [
    ("g38_defer_recon", "038_trace_anchor_explicit_declaration_record__candidate_trace_anchor_declaration_deferred_reconciliation", "g38_decl_defer_recon"),
    ("g38_bs_choice", "038_trace_anchor_explicit_declaration_record__candidate_Bs_explicit_branch_choice_sieve", "g38_bs_branch_choice"),
    ("g38_bs_split", "038_trace_anchor_explicit_declaration_record__candidate_Bs_notation_split_declaration", "g38_bs_split_decl"),
    ("g38_bs_usage", "038_trace_anchor_explicit_declaration_record__candidate_Bs_actual_notation_usage_collector", "g38_bs_usage"),
    ("g38_recon", "038_trace_anchor_explicit_declaration_record__candidate_trace_anchor_declaration_batch_reconciliation", "g38_recon"),
    ("g37_status_summary", "037_trace_anchor_declaration_option_sieve__candidate_group_37_status_summary", "g37_status_summary"),
    ("g36_status_summary", "036_conditional_trace_anchor_precondition_inventory__candidate_group_36_status_summary", "g36_status_summary"),
]


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
        "CONFLICT_REPAIRED_BY_SPLIT": StatusMark.INFO,
        "DECLARATION_DEFERRED": StatusMark.DEFER,
        "NOT_DECLARED": StatusMark.DEFER,
        "COMPATIBLE_IF_DECLARED": StatusMark.INFO,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
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
        scope="Group 38 declaration-deferred status summary",
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


@dataclass
class StatusEntry:
    name: str
    topic: str
    status: str
    result: str
    boundary: str


@dataclass
class GapEntry:
    name: str
    status: str
    reason: str
    discipline: str


@dataclass
class HandoffEntry:
    name: str
    status: str
    reason: str
    caution: str


@dataclass
class RuleEntry:
    name: str
    upgrade: str
    reason: str


def build_status_entries() -> List[StatusEntry]:
    return [
        StatusEntry(
            "G38-1: declaration route",
            "Group 38 opened an explicit trace-anchor declaration route",
            "PASS",
            "route opened as choice-tolerant rather than automatic declaration",
            "route opening is not declaration completion",
        ),
        StatusEntry(
            "G38-2: notation conflict",
            "actual B_s usage contained metric-like and scale-like evidence",
            "CONFLICT_REPAIRED_BY_SPLIT",
            "same B_s symbol was found overloaded; conflict required repair",
            "usage evidence alone cannot choose the convention",
        ),
        StatusEntry(
            "G38-3: notation split",
            "B_s_metric and b_s_scale were separated as named objects",
            "PASS",
            "the split repairs hidden overload by giving metric and scale meanings distinct names",
            "split is not active branch selection",
        ),
        StatusEntry(
            "G38-4: active branch",
            "metric_coefficient versus scale_factor branch choice",
            "DECLARATION_DEFERRED",
            "no active branch was configured or chosen",
            "Group 38 remains declaration-deferred",
        ),
        StatusEntry(
            "G38-5: trace normalization",
            "trace-normalization declaration attempt",
            "NOT_DECLARED",
            "no B_s convention, zeta convention, traced dimension, scope, or normalization expression was installed",
            "no trace-normalization form is selected, declared, adopted, or derived",
        ),
        StatusEntry(
            "G38-6: safe membership",
            "safe-membership declaration attempt",
            "NOT_DECLARED",
            "no membership form, object, sector, domain, codomain, criterion, role purity, or scope was installed",
            "no safe-membership claim is selected, declared, adopted, or derived",
        ),
        StatusEntry(
            "G38-7: joint package",
            "joint Package B declaration surface",
            "DECLARATION_DEFERRED",
            "no joint declaration package was chosen",
            "Package B remains compatible-if-declared only",
        ),
        StatusEntry(
            "G38-8: downstream gates",
            "B_s/F_zeta insertion, active O, residual control, and parent closure",
            "NOT_READY",
            "all downstream gates remain closed",
            "Group 38 is not insertion, active O, residual control, or parent readiness",
        ),
    ]


def build_gaps() -> List[GapEntry]:
    return [
        GapEntry(
            "G1: active branch choice",
            "OPEN",
            "B_s_metric and b_s_scale are named, but neither is active",
            "a later explicit branch-choice record must choose if declarations are to complete",
        ),
        GapEntry(
            "G2: trace-normalization declaration",
            "NOT_DECLARED",
            "B_s convention, zeta convention, traced dimension, scope, and expression remain unfilled",
            "normalization remains compatible-if-declared only",
        ),
        GapEntry(
            "G3: safe-membership declaration",
            "NOT_DECLARED",
            "membership form, object, sector, domain/codomain, criterion, role purity, and scope remain unfilled",
            "safe membership remains compatible-if-declared only",
        ),
        GapEntry(
            "G4: joint Package B declaration",
            "DECLARATION_DEFERRED",
            "no joint package is chosen after the split",
            "Package B remains an audit package, not a declared surface",
        ),
        GapEntry(
            "G5: adoption",
            "NOT_ADOPTED",
            "Group 38 is declaration exploration, not adoption",
            "Package B adoption requires a separate explicit decision",
        ),
        GapEntry(
            "G6: theorem support",
            "NOT_DERIVED",
            "notation repair and branch classification are not proofs",
            "trace-normalization and safe-membership theorem routes remain separate",
        ),
        GapEntry(
            "G7: insertion and parent closure",
            "NOT_READY",
            "deferred declaration does not resolve recombination or safety gates",
            "B_s/F_zeta insertion and parent equation remain closed",
        ),
    ]


def build_handoffs() -> List[HandoffEntry]:
    return [
        HandoffEntry(
            "H1: explicit branch-choice record",
            "OPEN",
            "theory owner may deliberately choose metric_coefficient or scale_factor branch after notation split",
            "choice is declaration only, not adoption or proof",
        ),
        HandoffEntry(
            "H2: notation-quality source hierarchy",
            "OPEN",
            "optional script may rank earliest or authoritative notation sources before choosing",
            "must not cherry-pick recovery-facing evidence",
        ),
        HandoffEntry(
            "H3: neutral F_zeta deferral",
            "DECLARATION_DEFERRED",
            "F_zeta may remain neutral while no concrete zeta/d or 2*zeta/d expression is installed",
            "neutral notation cannot hide branch choice",
        ),
        HandoffEntry(
            "H4: explicit declaration record after branch choice",
            "OPEN",
            "later work may rerun declaration completion after a branch is chosen",
            "declaration remains non-adoptive and non-theorem unless separately changed",
        ),
        HandoffEntry(
            "H5: adoption decision",
            "OPEN",
            "possible only as a separate explicit user/theory decision",
            "adoption must not be called derived",
        ),
        HandoffEntry(
            "H6: theorem route after declarations",
            "OPEN",
            "possible after declarations are explicit",
            "theorem target is not theorem proof",
        ),
        HandoffEntry(
            "H7: downstream route",
            "NOT_READY",
            "not available from Group 38 deferred result",
            "forbidden as immediate handoff",
        ),
    ]


def build_rules() -> List[RuleEntry]:
    return [
        RuleEntry("R1: split as active declaration", "treat B_s_metric/b_s_scale split as choosing one branch", "split repairs naming only"),
        RuleEntry("R2: deferred as failure", "treat declaration deferral as mathematical no-go", "deferral is governance status, not theorem failure"),
        RuleEntry("R3: deferred as hidden choice", "use F_zeta or prose to proceed as if a branch was chosen", "neutral notation cannot hide factor-of-two choice"),
        RuleEntry("R4: branch evidence as adoption", "treat branch clarity as Package B adoption", "adoption requires a separate explicit decision"),
        RuleEntry("R5: notation repair as theorem", "treat notation split as derived trace-normalization law", "notation repair is not proof"),
        RuleEntry("R6: declaration attempt as insertion", "treat branch clarity or split as B_s/F_zeta insertion", "downstream gates remain closed"),
        RuleEntry("R7: declaration attempt as parent readiness", "open parent closure from declaration exploration", "parent gate remains closed"),
    ]


def case_0(out):
    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  What did Group 38 establish after attempting an explicit trace-anchor")
    print("  declaration record, finding B_s notation conflict, repairing the notation")
    print("  by split, and leaving the active branch unchosen?")
    print("\nDiscipline:\n")
    print("  This script summarizes Group 38.")
    print("  It closes Group 38 as declaration-deferred, not declaration-completed.")
    print("  It chooses no active branch and installs no joint Package B declaration.")
    print("  It adopts nothing, proves nothing, and opens no downstream gate.")
    print("\nTiny goblin rule:\n  Two jars are labeled. No jar is chosen.")
    with out.governance_assessments():
        out.line("Group 38 status summary opened", StatusMark.PASS, "closing as declaration-deferred while preserving no-adoption/no-insertion boundary")


def case_1(out):
    header("Case 1: Group 38 symbolic summary loads")
    B_metric, B_scale, split, branch_defer, norm_defer, mem_defer, joint_defer = sp.symbols(
        "B_metric B_scale split branch_defer norm_defer mem_defer joint_defer"
    )
    adoption_boundary, theorem_boundary = sp.symbols("adoption_boundary theorem_boundary")
    P_insertion, P_active_O, P_residual_kill, P_parent = sp.symbols("P_insertion P_active_O P_residual_kill P_parent")
    L_declaration = sp.simplify(B_metric + B_scale + split + branch_defer + norm_defer + mem_defer + joint_defer)
    L_boundaries = sp.simplify(adoption_boundary + theorem_boundary)
    L_downstream = sp.simplify(P_insertion + P_active_O + P_residual_kill + P_parent)
    L_total = sp.simplify(L_declaration + L_boundaries + L_downstream)
    print(f"Declaration-deferred load: L_declaration_deferred = {L_declaration}")
    print(f"Boundary load: L_boundaries = {L_boundaries}")
    print(f"Downstream closed load: L_downstream_closed = {L_downstream}")
    print(f"Group 38 summary load: L_group38_summary = {L_total}")
    with out.derived_results():
        out.line("Group 38 symbolic summary loads stated", StatusMark.PASS, f"L_declaration_deferred={L_declaration}; L_downstream_closed={L_downstream}")


def case_2(out, entries: List[StatusEntry]):
    header("Case 2: Group 38 status entries")
    for item in entries:
        subheader(item.name)
        print(f"Topic: {item.topic}")
        with out.governance_assessments():
            out.line(item.name, mark(item.status), f"{item.status}: {item.result}. Boundary: {item.boundary}")
    with out.governance_assessments():
        out.line("Group 38 status entries stated", StatusMark.PASS, f"{len(entries)} status entries stated")


def case_3(out, gaps: List[GapEntry]):
    header("Case 3: Final open gaps")
    for item in gaps:
        subheader(item.name)
        with out.unresolved_obligations():
            out.line(item.name, mark(item.status), f"{item.status}: {item.reason}. Discipline: {item.discipline}")
    with out.unresolved_obligations():
        out.line("Group 38 final gaps stated", StatusMark.PASS, f"{len(gaps)} gaps remain open, deferred, or not ready")


def case_4(out, handoffs: List[HandoffEntry]):
    header("Case 4: Final handoffs")
    for item in handoffs:
        subheader(item.name)
        with out.governance_assessments():
            out.line(item.name, mark(item.status), f"{item.status}: {item.reason}. Caution: {item.caution}")
    with out.governance_assessments():
        out.line("Group 38 handoffs stated", StatusMark.DEFER, f"{len(handoffs)} handoffs stated; choices/downstream gates remain separate")


def case_5(out, rules: List[RuleEntry]):
    header("Case 5: Rejected summary upgrades")
    for item in rules:
        subheader(item.name)
        print(f"Upgrade: {item.upgrade}")
        with out.governance_assessments():
            out.line(item.name, StatusMark.OBLIGATION, f"POLICY_RULE: {item.reason}")
    with out.governance_assessments():
        out.line("Group 38 summary upgrades rejected", StatusMark.PASS, f"{len(rules)} upgrade shortcuts rejected as policy rules")


def case_6(out):
    header("Case 6: Group 38 conclusions")
    conclusions = [
        ("C1: Group 38 result", "DECLARATION_DEFERRED", "Group 38 completed a declaration attempt and notation repair, but not an explicit declaration record"),
        ("C2: notation split result", "PASS", "B_s_metric and b_s_scale are distinct named objects"),
        ("C3: active branch", "DECLARATION_DEFERRED", "no metric_coefficient or scale_factor branch is chosen"),
        ("C4: Package B status", "COMPATIBLE_IF_DECLARED", "Package B remains compatible-if-declared only"),
        ("C5: no adoption or recommendation", "NOT_ADOPTED", "Group 38 adopts no Package B component and recommends no adoption"),
        ("C6: no theorem support", "NOT_DERIVED", "trace normalization and safe membership remain not derived"),
        ("C7: downstream gates", "NOT_READY", "B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready"),
    ]
    for name, status, meaning in conclusions:
        subheader(name)
        with out.governance_assessments():
            out.line(name, mark(status), f"{status}: {meaning}")
    with out.governance_assessments():
        out.line("Group 38 status summary conclusion stated", StatusMark.PASS, "declaration attempt closed as deferred; no active branch, no declaration completion, no adoption, downstream gates closed")


def final_interpretation(out):
    header("Final interpretation")
    print("Group 38 status summary result:\n")
    print("  Group 38 attempted an explicit trace-anchor declaration record.")
    print("  Actual B_s usage showed conflicting metric-like and scale-like meanings.")
    print("  The conflict was repaired by splitting B_s into B_s_metric and b_s_scale.")
    print("  The split repairs notation but does not choose an active branch.")
    print("  No metric_coefficient or scale_factor branch is selected.")
    print("  No trace-normalization declaration is completed.")
    print("  No safe-membership declaration is completed.")
    print("  No joint Package B declaration surface is installed.")
    print("  Package B remains compatible-if-declared only.")
    print("  Package B is not adopted or recommended for adoption.")
    print("  B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready.")
    print("\nPossible next step:")
    print("  explicit branch-choice record, notation-quality source hierarchy, neutral F_zeta deferral,")
    print("  or theorem/precondition work that does not require a completed declaration")
    print("\nTiny goblin label:")
    print("  Two jars are labeled. No jar is chosen.")
    with out.governance_assessments():
        out.line("candidate Group 38 status summary complete", StatusMark.PASS, "Group 38 closes as declaration-deferred; choices and downstream gates remain separate")


def record_governance(ns, entries: List[StatusEntry], gaps: List[GapEntry], handoffs: List[HandoffEntry], rules: List[RuleEntry]):
    record_marker(ns, MARKER_ID, "g38_declaration_deferred_summary")
    for idx, item in enumerate(entries, 1):
        record_claim(ns, f"g38_status_c{idx}", MARKER_ID, GovernanceStatus.POLICY_RULE, f"{item.name}: {item.topic}. Result: {item.result}. Boundary: {item.boundary}.")
    for idx, item in enumerate(gaps, 1):
        status = ObligationStatus.DEFERRED if item.status in {"NOT_READY", "NOT_DECLARED", "DECLARATION_DEFERRED", "NOT_ADOPTED", "NOT_DERIVED"} else ObligationStatus.OPEN
        record_obligation(ns, f"g38_gap_{idx}", MARKER_ID, f"{item.name}: {item.reason}. Discipline: {item.discipline}.", status=status)
    for idx, item in enumerate(handoffs, 1):
        record_claim(ns, f"g38_handoff_h{idx}", MARKER_ID, GovernanceStatus.POLICY_RULE, f"{item.name}: {item.reason}. Caution: {item.caution}.")
    for idx, item in enumerate(rules, 1):
        record_claim(ns, f"g38_rule_r{idx}", MARKER_ID, GovernanceStatus.POLICY_RULE, f"{item.name}: {item.upgrade}. Reason: {item.reason}.")


def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    entries = build_status_entries()
    gaps = build_gaps()
    handoffs = build_handoffs()
    rules = build_rules()
    case_0(out)
    case_1(out)
    case_2(out, entries)
    case_3(out, gaps)
    case_4(out, handoffs)
    case_5(out, rules)
    case_6(out)
    final_interpretation(out)
    record_governance(ns, entries, gaps, handoffs, rules)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
