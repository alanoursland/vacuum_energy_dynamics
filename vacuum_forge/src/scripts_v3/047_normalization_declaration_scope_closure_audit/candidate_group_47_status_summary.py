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

SCRIPT_LABEL = "Candidate Group 47 Status Summary"
MARKER_ID = "g47_summary"
DEPENDENCIES = [
    ("g47_recon", "047_normalization_declaration_scope_closure_audit__candidate_declaration_scope_closure_batch_reconciliation", "g47_recon"),
    ("g47_route_classifier", "047_normalization_declaration_scope_closure_audit__candidate_declaration_scope_route_classifier", "g47_route_classifier"),
    ("g47_parent_scope_reject", "047_normalization_declaration_scope_closure_audit__candidate_parent_facing_scope_rejection_audit", "g47_parent_scope_reject"),
    ("g47_scope_status_matrix", "047_normalization_declaration_scope_closure_audit__candidate_scope_status_and_assumption_matrix", "g47_scope_status_matrix"),
    ("g47_scope_candidate_sieve", "047_normalization_declaration_scope_closure_audit__candidate_declaration_scope_candidate_sieve", "g47_scope_candidate_sieve"),
    ("g47_review_decl_boundary", "047_normalization_declaration_scope_closure_audit__candidate_review_vs_declaration_scope_boundary", "g47_review_decl_boundary"),
    ("g47_problem", "047_normalization_declaration_scope_closure_audit__candidate_declaration_scope_closure_problem", "g47_problem"),
    ("g46_summary", "046_parallel_trace_convention_field_closure_audit__candidate_group_46_status_summary", "g46_summary"),
]


@dataclass(frozen=True)
class StatusEntry:
    name: str
    topic: str
    status: str
    conclusion: str
    boundary: str


@dataclass(frozen=True)
class GapEntry:
    name: str
    status: str
    gap: str
    discipline: str


@dataclass(frozen=True)
class HandoffEntry:
    name: str
    status: str
    route: str
    caution: str


@dataclass(frozen=True)
class RejectedUpgrade:
    name: str
    upgrade: str
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
        "MATCHED_EXPECTATION": StatusMark.PASS,
        "DECLARATION_SCOPE_AUDIT": StatusMark.INFO,
        "DECLARATION_SCOPE_READY_FOR_RECORD": StatusMark.INFO,
        "DECLARATION_SCOPE_CANDIDATE": StatusMark.INFO,
        "STATUS_FIELD": StatusMark.INFO,
        "ASSUMPTION_FIELD": StatusMark.INFO,
        "CLOSED_FOR_REVIEW": StatusMark.INFO,
        "REVIEW_READY_ONLY": StatusMark.INFO,
        "NON_ACTIVE": StatusMark.INFO,
        "REJECTED_ROUTE": StatusMark.FAIL,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "SCOPE_REQUIRED": StatusMark.OBLIGATION,
        "CHOICE_REQUIRED": StatusMark.DEFER,
        "THEOREM_REQUIRED": StatusMark.DEFER,
        "DEFERRED_WITH_TARGET": StatusMark.DEFER,
        "NOT_DECLARED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
    }.get(status, StatusMark.INFO)


def governance_status(status: str) -> GovernanceStatus:
    if status in {"REJECTED_ROUTE", "FORBIDDEN_SHORTCUT"}:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {"POLICY_RULE", "SCOPE_REQUIRED"}:
        return GovernanceStatus.POLICY_RULE
    return GovernanceStatus.UNVERIFIED


def obligation_status(status: str) -> ObligationStatus:
    return ObligationStatus.OPEN


def record_marker(ns, marker_id: str, symbol_name: str, scope: str) -> None:
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[],
        output=sp.Symbol(symbol_name),
        method="inventory marker; no physical derivation",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
        scope=scope,
    )


def record_claim(ns, claim_id: str, marker_id: str, status: str, statement: str) -> None:
    ns.record_claim(
        ClaimRecord(
            claim_id=claim_id,
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=governance_status(status),
            statement=statement,
            derivation_ids=[marker_id],
            obligation_ids=[],
        )
    )


def record_obligation(ns, obligation_id: str, statement: str, status: str = "OPEN") -> None:
    ns.record_obligation(
        ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=obligation_id,
            status=obligation_status(status),
            required_by=[SCRIPT_ID],
            description=statement,
        )
    )


def build_status_entries() -> List[StatusEntry]:
    return [
        StatusEntry(
            "G47-1: declaration-scope blocker targeted",
            "Group 47 attacked the Group 46 normalization declaration-scope/status blocker directly",
            "DECLARATION_SCOPE_AUDIT",
            "The batch did not rerun all convention fields; it focused on the boundary between review-ready records and declaration-scope record readiness.",
            "A scope audit is not trace-normalization declaration, branch choice, adoption, insertion, or parent readiness.",
        ),
        StatusEntry(
            "G47-2: review/declaration boundary",
            "record-review scope versus declaration scope",
            "DECLARATION_SCOPE_READY_FOR_RECORD",
            "Review scope and declaration scope are now separated sharply enough that a future declaration-scope/status record can be written.",
            "Review-ready remains distinct from declaration-ready, and a scope record is not equation installation.",
        ),
        StatusEntry(
            "G47-3: surviving limited paired scope",
            "limited paired-record declaration-scope candidate",
            "DECLARATION_SCOPE_CANDIDATE",
            "The strongest surviving route is limited to the paired non-active metric/scale record surface under explicit assumptions and caveats.",
            "The surviving candidate is not a neutral law, not a single-branch scope, not insertion-facing, and not parent-facing.",
        ),
        StatusEntry(
            "G47-4: status and assumption matrix",
            "future scope/status record requirements",
            "STATUS_FIELD",
            "A future record must state status, paired-record domain, shared zeta assumption, symbolic d and numeric-d condition, non-active branch status, and downstream caveats.",
            "The matrix prepares a record; it does not close assumptions as trace-normalization declaration.",
        ),
        StatusEntry(
            "G47-5: downstream scope rejection",
            "parent-facing, insertion-facing, active-O, residual/source, and parent shortcuts",
            "REJECTED_ROUTE",
            "Scope broadening toward insertion, active O, residual/source proof, or parent-facing trace normalization was rejected without independent theorem support.",
            "Limited declaration-scope clarity cannot become field-equation machinery.",
        ),
        StatusEntry(
            "G47-6: route classification",
            "honest next route after scope audits",
            "DEFERRED_WITH_TARGET",
            "The next non-looping target is an explicit paired declaration-scope/status record.",
            "That target is not a trace-normalization declaration and cannot open insertion or parent routes.",
        ),
        StatusEntry(
            "G47-7: batch reconciliation",
            "actual batch outputs reconciled before summary",
            "MATCHED_EXPECTATION",
            "Outputs matched the expected shape: blocker targeted, limited paired scope survives, assumptions are mapped, and downstream gates remain closed.",
            "Reconciliation is not group closure by itself, branch choice, declaration completion, adoption, theorem proof, or insertion.",
        ),
    ]


def build_gaps() -> List[GapEntry]:
    return [
        GapEntry(
            "G1: explicit paired declaration-scope/status record",
            "OPEN",
            "The scope/status record has been identified as the next target but has not been instantiated.",
            "Do not proceed directly to trace-normalization declaration before writing this record.",
        ),
        GapEntry(
            "G2: trace-normalization declaration",
            "NOT_DECLARED",
            "Trace normalization is still not declared; scope-record readiness is only pre-declaration infrastructure.",
            "Avoid reporting limited scope as completed equation status.",
        ),
        GapEntry(
            "G3: numeric d condition",
            "SCOPE_REQUIRED",
            "Numeric d remains scope-dependent and must be handled explicitly in the future scope/status record.",
            "Do not fix d by recovery, algebraic aesthetics, or silent convention leak.",
        ),
        GapEntry(
            "G4: branch choice",
            "CHOICE_REQUIRED",
            "Single-branch declaration scope still requires an explicit metric or scale branch choice.",
            "Do not smuggle branch selection through scope language.",
        ),
        GapEntry(
            "G5: parent-facing scope",
            "THEOREM_REQUIRED",
            "Parent-facing scope remains unavailable without residual/source/boundary/divergence and identity support.",
            "Do not call a scope parent-facing by name alone.",
        ),
        GapEntry(
            "G6: downstream gates",
            "NOT_READY",
            "B_s/F_zeta insertion, active O, residual/source safety, recombination, and parent closure remain closed.",
            "Scope clarity cannot be used as field-equation machinery.",
        ),
    ]


def build_handoffs() -> List[HandoffEntry]:
    return [
        HandoffEntry(
            "H1: explicit paired declaration-scope/status record",
            "DEFERRED_WITH_TARGET",
            "Write the paired scope/status record that names the limited paired-record domain, status, assumptions, numeric-d condition, and downstream caveats.",
            "This is the next non-looping target and still is not a trace-normalization declaration.",
        ),
        HandoffEntry(
            "H2: parallel trace-normalization declaration attempt",
            "NOT_DECLARED",
            "Attempt only after the paired scope/status record is explicit and any remaining assumptions are acceptable.",
            "Do not jump directly from Group 47 to declaration.",
        ),
        HandoffEntry(
            "H3: explicit branch-choice route",
            "CHOICE_REQUIRED",
            "Use only if the project decides to leave the paired route and choose metric or scale explicitly.",
            "Branch choice requires a daylight-labeled choice record, not scope inference.",
        ),
        HandoffEntry(
            "H4: parent-facing or insertion route",
            "NOT_READY",
            "Not available from Group 47.",
            "Requires separate scalar-response law, safety theorems, active-projector construction if needed, and parent identity support.",
        ),
    ]


def build_rejected_upgrades() -> List[RejectedUpgrade]:
    return [
        RejectedUpgrade("R1: scope-record-ready as declaration-ready", "Treat the surviving scope candidate as trace-normalization declaration readiness", "Scope record readiness is not equation declaration."),
        RejectedUpgrade("R2: limited scope as neutral law", "Collapse paired scope into unqualified B_s or neutral F_zeta", "The factor-of-two burden remains visible."),
        RejectedUpgrade("R3: scope as branch choice", "Use declaration scope to select metric or scale branch", "Single-branch scope remains choice-required."),
        RejectedUpgrade("R4: scope as insertion", "Open B_s/F_zeta insertion from limited declaration scope", "Insertion requires a separate scalar-response law and safety gates."),
        RejectedUpgrade("R5: scope as active O", "Treat scope terms as no-overlap projector machinery", "Scope fields do not define projector structure."),
        RejectedUpgrade("R6: scope as safety theorem", "Claim residual/source safety from declaration-scope limits", "Safety theorems remain separate."),
        RejectedUpgrade("R7: parent-facing scope by label", "Call the limited scope parent-facing without theorem support", "Parent-facing status requires identity and safety support."),
        RejectedUpgrade("R8: scope audit as Package B adoption", "Treat scope/status clarity as Package B adoption", "Adoption remains a separate explicit theory decision."),
    ]


def case_0(out: ScriptOutput) -> None:
    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  What did Group 47 establish about closing the normalization declaration-scope")
    print("  blocker named by Group 46?\n")
    print("Discipline:\n")
    print("  This script summarizes Group 47 after reviewing the batch outputs.")
    print("  It does not choose B_s_metric or b_s_scale, does not declare trace normalization,")
    print("  adopts nothing, inserts nothing, constructs no active O, and opens no parent gate.")
    with out.governance_assessments():
        out.line("Group 47 status summary opened", StatusMark.PASS, "closing declaration-scope closure audit while preserving scope-record-ready / no-declaration / no-insertion boundary")


def case_1(out: ScriptOutput) -> None:
    header("Case 1: Group 47 summary boundary ledger")
    ledger = [
        ("declaration-scope audit", "DECLARATION_SCOPE_AUDIT", "normalization declaration scope/status blocker targeted directly"),
        ("review/declaration boundary", "DECLARATION_SCOPE_READY_FOR_RECORD", "review scope and declaration scope separated"),
        ("limited paired scope", "DECLARATION_SCOPE_CANDIDATE", "paired non-active metric/scale record surface survives as future scope-record domain"),
        ("status/assumption fields", "STATUS_FIELD", "future record requirements are explicit but not declaration"),
        ("downstream scope routes", "REJECTED_ROUTE", "insertion-facing, parent-facing, active-O, and safety-proof scope shortcuts rejected"),
        ("next target", "DEFERRED_WITH_TARGET", "explicit paired declaration-scope/status record"),
        ("trace declaration", "NOT_DECLARED", "trace normalization remains undeclared"),
        ("downstream gates", "NOT_READY", "adoption, insertion, active O, residual control, recombination, and parent closure remain closed"),
    ]
    for subject, status, text in ledger:
        with out.governance_assessments():
            out.line(subject, mark(status), f"{status}: {text}")


def case_2(out: ScriptOutput, entries: List[StatusEntry]) -> None:
    header("Case 2: Group 47 status entries")
    for entry in entries:
        subheader(entry.name)
        print(f"Topic: {entry.topic}")
        with out.governance_assessments():
            out.line(entry.name, mark(entry.status), f"{entry.status}: {entry.conclusion} Boundary: {entry.boundary}")
    with out.governance_assessments():
        out.line("Group 47 status entries stated", StatusMark.PASS, f"{len(entries)} status entries stated")


def case_3(out: ScriptOutput, gaps: List[GapEntry]) -> None:
    header("Case 3: Final open gaps")
    for gap in gaps:
        subheader(gap.name)
        with out.unresolved_obligations():
            out.line(gap.name, mark(gap.status), f"{gap.status}: {gap.gap} Discipline: {gap.discipline}")
    with out.unresolved_obligations():
        out.line("Group 47 final gaps stated", StatusMark.PASS, f"{len(gaps)} gaps remain open, choice-required, theorem-required, not declared, or not ready")


def case_4(out: ScriptOutput, handoffs: List[HandoffEntry]) -> None:
    header("Case 4: Final handoffs")
    for handoff in handoffs:
        subheader(handoff.name)
        with out.governance_assessments():
            out.line(handoff.name, mark(handoff.status), f"{handoff.status}: {handoff.route} Caution: {handoff.caution}")
    with out.governance_assessments():
        out.line("Group 47 handoffs stated", StatusMark.DEFER, f"{len(handoffs)} handoffs stated; paired declaration-scope/status record is the next non-looping target")


def case_5(out: ScriptOutput, rejected: List[RejectedUpgrade]) -> None:
    header("Case 5: Rejected summary upgrades")
    for item in rejected:
        subheader(item.name)
        print(f"Upgrade: {item.upgrade}")
        with out.governance_assessments():
            out.line(item.name, StatusMark.OBLIGATION, f"POLICY_RULE: {item.reason}")
    with out.governance_assessments():
        out.line("Group 47 summary upgrades rejected", StatusMark.PASS, f"{len(rejected)} upgrade shortcuts rejected as policy rules")


def case_6(out: ScriptOutput) -> None:
    header("Case 6: Group 47 conclusions")
    conclusions = [
        ("C1: Group 47 result", "DECLARATION_SCOPE_AUDIT", "Group 47 completed a targeted normalization declaration-scope closure audit"),
        ("C2: review/declaration boundary", "DECLARATION_SCOPE_READY_FOR_RECORD", "review scope and declaration scope are separated enough to write a future scope/status record"),
        ("C3: surviving scope", "DECLARATION_SCOPE_CANDIDATE", "limited paired-record declaration-scope candidate survives"),
        ("C4: next target", "DEFERRED_WITH_TARGET", "explicit paired declaration-scope/status record is the next non-looping target"),
        ("C5: declaration status", "NOT_DECLARED", "trace normalization is not declared"),
        ("C6: downstream status", "NOT_READY", "B_s/F_zeta insertion, active O, recombination, and parent equation remain not ready"),
    ]
    for name, status, text in conclusions:
        subheader(name)
        with out.governance_assessments():
            out.line(name, mark(status), f"{status}: {text}")
    with out.governance_assessments():
        out.line("Group 47 status summary conclusion stated", StatusMark.PASS, "scope blocker narrowed to a record-writing target; no declaration, adoption, insertion, active O, recombination, or parent route opened")
    header("Final interpretation")
    print("Group 47 status summary result:\n")
    print("  Group 47 completed a targeted normalization declaration-scope closure audit.")
    print("  It separated record-review scope from declaration scope.")
    print("  A limited paired-record declaration-scope candidate survives as the strongest route.")
    print("  The future scope/status record must state status, paired-record domain, shared zeta assumption,")
    print("  symbolic d and numeric-d condition, non-active branch status, and downstream caveats.")
    print("  Parent-facing, insertion-facing, active-O, safety-proof, neutral-law, and single-branch-without-choice routes remain blocked.")
    print("  No branch is chosen.")
    print("  No trace-normalization declaration is completed.")
    print("  Package B is not adopted or recommended for adoption.")
    print("  B_s/F_zeta insertion, active O, residual control, source protection, recombination, and parent equation remain not ready.\n")
    print("Possible next step:")
    print("  explicit paired declaration-scope/status record, then only later a parallel trace-normalization declaration attempt if assumptions remain acceptable\n")
    print("Forbidden immediate next step:")
    print("  trace-normalization declaration, Package B adoption, B_s/F_zeta insertion, active O, recombination, or parent closure")


def record_governance(
    ns,
    entries: List[StatusEntry],
    gaps: List[GapEntry],
    handoffs: List[HandoffEntry],
    rejected: List[RejectedUpgrade],
) -> None:
    record_marker(ns, MARKER_ID, "g47_scope_status_record_target", "Group 47 status summary marker: declaration-scope record target only")
    for idx, entry in enumerate(entries, 1):
        record_claim(ns, f"{MARKER_ID}_c{idx}", MARKER_ID, entry.status, f"{entry.name}: {entry.conclusion} Boundary: {entry.boundary}")
    for idx, gap in enumerate(gaps, 1):
        oid = f"{MARKER_ID}_gap{idx}"
        record_obligation(ns, oid, f"{gap.name}: {gap.gap} Discipline: {gap.discipline}", gap.status)
        record_claim(ns, f"{MARKER_ID}_gap_claim{idx}", MARKER_ID, gap.status, f"{gap.name}: {gap.gap}")
    for idx, handoff in enumerate(handoffs, 1):
        record_claim(ns, f"{MARKER_ID}_h{idx}", MARKER_ID, handoff.status, f"{handoff.name}: {handoff.route} Caution: {handoff.caution}")
    for idx, item in enumerate(rejected, 1):
        record_claim(ns, f"{MARKER_ID}_r{idx}", MARKER_ID, "POLICY_RULE", f"Rejected upgrade: {item.upgrade}. Reason: {item.reason}")


def main() -> None:
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    entries = build_status_entries()
    gaps = build_gaps()
    handoffs = build_handoffs()
    rejected = build_rejected_upgrades()
    case_0(out)
    case_1(out)
    case_2(out, entries)
    case_3(out, gaps)
    case_4(out, handoffs)
    case_5(out, rejected)
    case_6(out)
    record_governance(ns, entries, gaps, handoffs, rejected)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
