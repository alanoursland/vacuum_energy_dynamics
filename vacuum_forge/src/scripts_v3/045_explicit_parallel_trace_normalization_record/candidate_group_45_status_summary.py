from __future__ import annotations

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
#   45_explicit_parallel_trace_normalization_record
# Script type:
#   STATUS SUMMARY

SCRIPT_LABEL = "Candidate Group 45 Status Summary"
MARKER_ID = "g45_summary"

DEPENDENCIES = [
    ("g45_recon", "45_explicit_parallel_trace_normalization_record__candidate_parallel_trace_record_batch_reconciliation", "g45_recon"),
    ("g45_downstream_lock", "45_explicit_parallel_trace_normalization_record__candidate_parallel_record_downstream_lock_audit", "g45_downstream_lock"),
    ("g45_decl_boundary", "45_explicit_parallel_trace_normalization_record__candidate_parallel_record_declaration_boundary", "g45_decl_boundary"),
    ("g45_consistency", "45_explicit_parallel_trace_normalization_record__candidate_parallel_record_consistency_audit", "g45_consistency"),
    ("g45_scale_record", "45_explicit_parallel_trace_normalization_record__candidate_scale_trace_record_schema", "g45_scale_record"),
    ("g45_metric_record", "45_explicit_parallel_trace_normalization_record__candidate_metric_trace_record_schema", "g45_metric_record"),
    ("g45_problem", "45_explicit_parallel_trace_normalization_record__candidate_parallel_trace_record_problem", "g45_problem"),
    ("g44_summary", "44_trace_normalization_selector_context_audit__candidate_group_44_status_summary", "g44_summary"),
]


@dataclass(frozen=True)
class StatusEntry:
    name: str
    topic: str
    status: str
    result: str
    boundary: str


@dataclass(frozen=True)
class GapEntry:
    name: str
    status: str
    reason: str
    discipline: str


@dataclass(frozen=True)
class HandoffEntry:
    name: str
    status: str
    reason: str
    caution: str


@dataclass(frozen=True)
class RuleEntry:
    name: str
    upgrade: str
    reason: str


@dataclass(frozen=True)
class LedgerEntry:
    name: str
    status: str
    detail: str


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
        "MATCHED_EXPECTATION": StatusMark.PASS,
        "PARALLEL_RECORD_AUDIT": StatusMark.INFO,
        "PARALLEL_RECORD_CANDIDATE": StatusMark.INFO,
        "METRIC_RECORD_CANDIDATE": StatusMark.INFO,
        "SCALE_RECORD_CANDIDATE": StatusMark.INFO,
        "SCHEMA_FIELD": StatusMark.INFO,
        "CONDITIONAL": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "DEFER": StatusMark.DEFER,
        "NOT_DECLARED": StatusMark.DEFER,
        "DECLARATION_DEFERRED": StatusMark.DEFER,
        "NOT_CHOSEN": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "CONSISTENCY_RULE": StatusMark.OBLIGATION,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
    }.get(status, StatusMark.INFO)


def obligation_status(status: str) -> ObligationStatus:
    if status in {"NOT_READY", "NOT_DECLARED", "DECLARATION_DEFERRED", "NOT_CHOSEN", "NOT_DERIVED", "NOT_ADOPTED"}:
        return ObligationStatus.DEFERRED
    return ObligationStatus.OPEN


def record_marker(ns, marker_id: str, symbol_name: str) -> None:
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[],
        output=sp.Symbol(symbol_name),
        method="inventory marker; no physical derivation",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
        scope="Group 45 explicit parallel trace-normalization record summary",
    )


def record_claim(ns, claim_id: str, marker_id: str, statement: str) -> None:
    ns.record_claim(
        ClaimRecord(
            claim_id=claim_id,
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.POLICY_RULE,
            statement=statement,
            derivation_ids=[marker_id],
            obligation_ids=[],
        )
    )


def record_obligation(ns, obligation_id: str, title: str, description: str, status: str = "OPEN") -> None:
    ns.record_obligation(
        ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=obligation_status(status),
            required_by=[SCRIPT_ID],
            description=description,
        )
    )


def build_ledger() -> List[LedgerEntry]:
    return [
        LedgerEntry("parallel record route", "PARALLEL_RECORD_AUDIT", "two explicit non-active trace-normalization record surfaces were made concrete"),
        LedgerEntry("metric record", "METRIC_RECORD_CANDIDATE", "B_s_metric carries log(B_s_metric)=2*zeta/d only as a non-active candidate expression"),
        LedgerEntry("scale record", "SCALE_RECORD_CANDIDATE", "b_s_scale carries log(b_s_scale)=zeta/d only as a non-active candidate expression"),
        LedgerEntry("factor-of-two burden", "CONSISTENCY_RULE", "zeta/d and 2*zeta/d remain separated and visible"),
        LedgerEntry("declaration boundary", "NOT_DECLARED", "record schemas are pre-declaration infrastructure only"),
        LedgerEntry("branch status", "NOT_CHOSEN", "neither metric nor scale branch is selected"),
        LedgerEntry("downstream gates", "NOT_READY", "adoption, insertion, active O, residual control, recombination, and parent closure remain closed"),
    ]


def build_status_entries() -> List[StatusEntry]:
    return [
        StatusEntry(
            "G45-1: parallel trace-record opener",
            "Group 45 opened as an explicit parallel trace-normalization record audit",
            "PARALLEL_RECORD_AUDIT",
            "the group made the metric and scale record surfaces concrete while keeping both non-active",
            "parallel record work is visibility infrastructure, not branch choice, declaration, adoption, insertion, or parent readiness",
        ),
        StatusEntry(
            "G45-2: metric trace record schema",
            "B_s_metric non-active trace-normalization record",
            "METRIC_RECORD_CANDIDATE",
            "the metric record names B_s_metric, carries log(B_s_metric)=2*zeta/d as candidate expression, reserves zeta/dimension/scope fields, and marks itself non-active/not chosen",
            "the metric schema does not choose B_s_metric and does not complete trace normalization",
        ),
        StatusEntry(
            "G45-3: scale trace record schema",
            "b_s_scale non-active trace-normalization record",
            "SCALE_RECORD_CANDIDATE",
            "the scale record names b_s_scale, carries log(b_s_scale)=zeta/d as candidate expression, reserves zeta/dimension/scope fields, and marks itself non-active/not chosen",
            "the scale schema does not choose b_s_scale and does not complete trace normalization",
        ),
        StatusEntry(
            "G45-4: parallel consistency",
            "paired metric and scale records",
            "CONSISTENCY_RULE",
            "the two records remain explicitly labeled, expression-separated, status-aligned, and equally non-insertable",
            "the pair is not one neutral law, not a compromise law, and not a joint active declaration",
        ),
        StatusEntry(
            "G45-5: declaration boundary",
            "pre-declaration status of the record surface",
            "NOT_DECLARED",
            "the explicit record surface is sharp enough for later review but still lacks closed assumptions, zeta convention, traced dimension, scope, and declaration status",
            "record schemas are not trace-normalization declaration and not Package B adoption",
        ),
        StatusEntry(
            "G45-6: downstream locks",
            "insertion, active O, residual/source, boundary/divergence, adoption, and parent gates",
            "NOT_READY",
            "parallel trace records do not define an insertion law, active projector, residual control, source protection, boundary neutrality, parent identity, or adoption decision",
            "record clarity cannot be used as field-equation machinery",
        ),
        StatusEntry(
            "G45-7: batch reconciliation",
            "actual batch outputs were reconciled before summary",
            "MATCHED_EXPECTATION",
            "outputs matched the expected explicit parallel record shape: metric and scale schemas concrete, labels preserved, factor-of-two burden visible, no declaration or downstream opening",
            "reconciliation is not group closure by itself, branch choice, declaration completion, adoption, theorem proof, or insertion",
        ),
    ]


def build_gaps() -> List[GapEntry]:
    return [
        GapEntry(
            "G1: no active branch",
            "NOT_CHOSEN",
            "B_s_metric and b_s_scale are both recorded as non-active candidates, but neither is selected",
            "a later explicit branch-choice record is still required for a single active branch",
        ),
        GapEntry(
            "G2: trace-normalization declaration",
            "NOT_DECLARED",
            "the metric and scale schemas are explicit, but declaration prerequisites remain open",
            "future declaration must close assumptions, zeta convention, traced dimension, scope, and status",
        ),
        GapEntry(
            "G3: factor-of-two preservation",
            "POLICY_RULE",
            "log(B_s_metric)=2*zeta/d and log(b_s_scale)=zeta/d remain separate",
            "do not collapse the pair into unqualified B_s, neutral F_zeta, or a compromise expression",
        ),
        GapEntry(
            "G4: Package B adoption",
            "NOT_ADOPTED",
            "explicit trace records do not adopt Package B or recommend adoption",
            "adoption remains a separate explicit theory decision after declarations and support exist",
        ),
        GapEntry(
            "G5: B_s/F_zeta insertion",
            "NOT_READY",
            "candidate records are not recombination or insertion laws",
            "insertion requires separate licensed scalar-response law and downstream safety gates",
        ),
        GapEntry(
            "G6: residual/source theorems",
            "NOT_DERIVED",
            "record clarity does not prove residual nonentry, residual kill, or source no-double-counting",
            "residual and source safety remain separate theorem or axiom routes",
        ),
        GapEntry(
            "G7: active O and parent identity",
            "NOT_READY",
            "parallel labels do not construct active O, boundary neutrality, divergence safety, recombination, or parent closure",
            "parent equation remains closed until identity and recombination loads are licensed",
        ),
    ]


def build_handoffs() -> List[HandoffEntry]:
    return [
        HandoffEntry(
            "H1: parallel trace-normalization declaration attempt",
            "NOT_DECLARED",
            "may later evaluate whether the two explicit record schemas can support a formal parallel declaration route",
            "must close assumptions, zeta convention, traced dimension, scope, status, and non-insertion caveats first",
        ),
        HandoffEntry(
            "H2: explicit branch-choice record",
            "NOT_CHOSEN",
            "may later choose metric or scale branch using a daylight-labeled choice record",
            "must not treat the existence of both records as choosing either branch",
        ),
        HandoffEntry(
            "H3: convention-field closure route",
            "OPEN",
            "may fill or audit the zeta convention, traced dimension d, and normalization-scope fields shared by both records",
            "field closure would still not be declaration unless a separate declaration record says so",
        ),
        HandoffEntry(
            "H4: residual/source safety theorem route",
            "NOT_DERIVED",
            "may attempt residual nonentry, source no-double-counting, or A-sector mass protection theorems after record clarity",
            "record schemas provide no theorem support by themselves",
        ),
        HandoffEntry(
            "H5: insertion or parent route",
            "NOT_READY",
            "not available from Group 45",
            "forbidden as immediate handoff",
        ),
    ]


def build_rejected_upgrades() -> List[RuleEntry]:
    return [
        RuleEntry("R1: records as branch choice", "treat carrying both records as choosing metric, scale, or both branches", "parallel records remain non-active candidates"),
        RuleEntry("R2: schemas as declaration", "treat metric or scale schemas as completed trace-normalization declaration", "schema visibility is pre-declaration infrastructure only"),
        RuleEntry("R3: pair as neutral law", "collapse 2*zeta/d and zeta/d into unqualified B_s, neutral F_zeta, or a compromise law", "that hides or fabricates the factor-of-two burden"),
        RuleEntry("R4: record as insertion", "use either candidate record directly in B_s/F_zeta insertion", "insertion law remains separate and not ready"),
        RuleEntry("R5: records as active O", "treat branch labels or record pair as no-overlap projector", "labels are not projector construction"),
        RuleEntry("R6: record clarity as residual/source theorem", "claim records prove residual control or source no-double-counting", "residual and source theorems remain separate"),
        RuleEntry("R7: record boundary as adoption", "treat parallel record infrastructure as Package B adoption", "adoption requires separate theory decision"),
        RuleEntry("R8: records as parent readiness", "open recombination or parent closure from record clarity", "downstream gates remain closed"),
    ]


def case_0(out: ScriptOutput) -> None:
    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  What did Group 45 establish by making explicit parallel trace-normalization")
    print("  records for B_s_metric and b_s_scale while avoiding branch choice?")
    print("\nDiscipline:\n")
    print("  This script summarizes Group 45 after reviewing the batch outputs.")
    print("  It does not choose B_s_metric or b_s_scale.")
    print("  It does not complete trace-normalization declaration.")
    print("  It adopts nothing, inserts nothing, constructs no active O, and opens no parent gate.")
    with out.governance_assessments():
        out.line(
            "Group 45 status summary opened",
            StatusMark.PASS,
            "closing explicit parallel trace-normalization record audit while preserving non-active / no-declaration / no-insertion boundary",
        )


def case_1(out: ScriptOutput, ledger: List[LedgerEntry]) -> None:
    header("Case 1: Group 45 summary boundary ledger")
    for item in ledger:
        with out.governance_assessments():
            out.line(item.name, mark(item.status), f"{item.status}: {item.detail}")


def case_2(out: ScriptOutput, entries: List[StatusEntry]) -> None:
    header("Case 2: Group 45 status entries")
    for item in entries:
        subheader(item.name)
        print(f"Topic: {item.topic}")
        with out.governance_assessments():
            out.line(item.name, mark(item.status), f"{item.status}: {item.result}. Boundary: {item.boundary}")
    with out.governance_assessments():
        out.line("Group 45 status entries stated", StatusMark.PASS, f"{len(entries)} status entries stated")


def case_3(out: ScriptOutput, gaps: List[GapEntry]) -> None:
    header("Case 3: Final open gaps")
    for item in gaps:
        subheader(item.name)
        with out.unresolved_obligations():
            out.line(item.name, mark(item.status), f"{item.status}: {item.reason}. Discipline: {item.discipline}")
    with out.unresolved_obligations():
        out.line("Group 45 final gaps stated", StatusMark.PASS, f"{len(gaps)} gaps remain open, not chosen, not declared, not derived, not adopted, or not ready")


def case_4(out: ScriptOutput, handoffs: List[HandoffEntry]) -> None:
    header("Case 4: Final handoffs")
    for item in handoffs:
        subheader(item.name)
        with out.governance_assessments():
            out.line(item.name, mark(item.status), f"{item.status}: {item.reason}. Caution: {item.caution}")
    with out.governance_assessments():
        out.line("Group 45 handoffs stated", StatusMark.DEFER, f"{len(handoffs)} handoffs stated; declaration, choice, theorem, insertion, and parent gates remain separate")


def case_5(out: ScriptOutput, rules: List[RuleEntry]) -> None:
    header("Case 5: Rejected summary upgrades")
    for item in rules:
        subheader(item.name)
        print(f"Upgrade: {item.upgrade}")
        with out.governance_assessments():
            out.line(item.name, StatusMark.OBLIGATION, f"POLICY_RULE: {item.reason}")
    with out.governance_assessments():
        out.line("Group 45 summary upgrades rejected", StatusMark.PASS, f"{len(rules)} upgrade shortcuts rejected as policy rules")


def case_6(out: ScriptOutput) -> None:
    header("Case 6: Group 45 conclusions")
    conclusions = [
        ("C1: Group 45 result", "PARALLEL_RECORD_AUDIT", "Group 45 completed an explicit parallel trace-normalization record audit"),
        ("C2: metric record status", "METRIC_RECORD_CANDIDATE", "B_s_metric record schema is explicit and non-active"),
        ("C3: scale record status", "SCALE_RECORD_CANDIDATE", "b_s_scale record schema is explicit and non-active"),
        ("C4: factor-of-two status", "CONSISTENCY_RULE", "2*zeta/d and zeta/d remain separated"),
        ("C5: branch/declaration status", "NOT_DECLARED", "no branch is chosen and trace normalization is not declared"),
        ("C6: no adoption or theorem", "NOT_ADOPTED", "Group 45 adopts nothing and proves no residual/source theorem"),
        ("C7: downstream gates", "NOT_READY", "B_s/F_zeta insertion, active O, residual control, recombination, and parent equation remain not ready"),
    ]
    for name, status, meaning in conclusions:
        subheader(name)
        with out.governance_assessments():
            out.line(name, mark(status), f"{status}: {meaning}")
    with out.governance_assessments():
        out.line(
            "Group 45 status summary conclusion stated",
            StatusMark.PASS,
            "parallel record surface made concrete; no branch, declaration, adoption, insertion, active O, recombination, or parent route opened",
        )


def final_interpretation() -> None:
    header("Final interpretation")
    print("Group 45 status summary result:\n")
    print("  Group 45 completed an explicit parallel trace-normalization record audit.")
    print("  It made two non-active branch-indexed trace-normalization record schemas concrete.")
    print("  The metric record names B_s_metric and carries log(B_s_metric)=2*zeta/d only as a candidate expression.")
    print("  The scale record names b_s_scale and carries log(b_s_scale)=zeta/d only as a candidate expression.")
    print("  Both records reserve convention fields for zeta convention, traced dimension d, and normalization scope.")
    print("  Both records explicitly report non-active / candidate / not-chosen status.")
    print("  The factor-of-two burden remains visible: 2*zeta/d and zeta/d are not collapsed.")
    print("  Parallel records are visibility infrastructure and pre-declaration review surfaces.")
    print("  No B_s branch is chosen.")
    print("  No trace-normalization declaration is completed.")
    print("  Package B is not adopted or recommended for adoption.")
    print("  B_s/F_zeta insertion, active O, residual control, source protection, recombination, and parent equation remain not ready.")
    print("\nPossible next step:")
    print("  parallel trace-normalization declaration attempt after conventions close,")
    print("  convention-field closure route, explicit branch-choice record,")
    print("  or residual/source safety theorem route")
    print("\nForbidden immediate next step:")
    print("  Package B adoption, B_s/F_zeta insertion, active O, residual control, recombination, or parent closure")


def record_governance(ns, statuses: List[StatusEntry], gaps: List[GapEntry], handoffs: List[HandoffEntry], rules: List[RuleEntry]) -> None:
    record_marker(ns, MARKER_ID, MARKER_ID)
    for idx, item in enumerate(statuses, 1):
        record_claim(
            ns,
            f"g45_status_c{idx}",
            MARKER_ID,
            f"{item.name}: {item.topic}. Result: {item.result}. Boundary: {item.boundary}.",
        )
    for idx, item in enumerate(gaps, 1):
        record_obligation(
            ns,
            f"g45_gap_{idx}",
            item.name,
            f"{item.reason}. Discipline: {item.discipline}.",
            item.status,
        )
    for idx, item in enumerate(handoffs, 1):
        record_claim(
            ns,
            f"g45_handoff_{idx}",
            MARKER_ID,
            f"{item.name}: {item.reason}. Caution: {item.caution}.",
        )
    for idx, item in enumerate(rules, 1):
        record_claim(
            ns,
            f"g45_rule_{idx}",
            MARKER_ID,
            f"Rejected upgrade: {item.upgrade}. Reason: {item.reason}.",
        )


def main() -> None:
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    ledger = build_ledger()
    statuses = build_status_entries()
    gaps = build_gaps()
    handoffs = build_handoffs()
    rules = build_rejected_upgrades()
    case_0(out)
    case_1(out, ledger)
    case_2(out, statuses)
    case_3(out, gaps)
    case_4(out, handoffs)
    case_5(out, rules)
    case_6(out)
    final_interpretation()
    record_governance(ns, statuses, gaps, handoffs, rules)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
