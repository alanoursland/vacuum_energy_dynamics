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

SCRIPT_LABEL = "Candidate Group 46 Status Summary"
MARKER_ID = "g46_summary"
DEPENDENCIES = [
    ("g46_recon", "46_parallel_trace_convention_field_closure_audit__candidate_convention_field_closure_batch_reconciliation", "g46_recon"),
    ("g46_route_classifier", "46_parallel_trace_convention_field_closure_audit__candidate_convention_closure_route_classifier", "g46_route_classifier"),
    ("g46_pair_consistency", "46_parallel_trace_convention_field_closure_audit__candidate_branch_pair_convention_consistency_sieve", "g46_pair_consistency"),
    ("g46_scope_field", "46_parallel_trace_convention_field_closure_audit__candidate_normalization_scope_field_audit", "g46_scope_field"),
    ("g46_dimension_field", "46_parallel_trace_convention_field_closure_audit__candidate_traced_dimension_field_audit", "g46_dimension_field"),
    ("g46_zeta_convention", "46_parallel_trace_convention_field_closure_audit__candidate_zeta_convention_field_audit", "g46_zeta_convention"),
    ("g46_problem", "46_parallel_trace_convention_field_closure_audit__candidate_convention_field_closure_problem", "g46_problem"),
    ("g45_summary", "45_explicit_parallel_trace_normalization_record__candidate_group_45_status_summary", "g45_summary"),
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
        "CLOSED_FOR_REVIEW": StatusMark.INFO,
        "REVIEW_READY_ONLY": StatusMark.INFO,
        "CONVENTION_FIELD_AUDIT": StatusMark.INFO,
        "SHARED_FIELD": StatusMark.INFO,
        "CONSISTENCY_RULE": StatusMark.OBLIGATION,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "SCOPE_REQUIRED": StatusMark.OBLIGATION,
        "CONVENTION_BLOCKED": StatusMark.DEFER,
        "DEFERRED_WITH_TARGET": StatusMark.DEFER,
        "THEOREM_REQUIRED": StatusMark.DEFER,
        "NOT_DECLARED": StatusMark.DEFER,
        "NOT_CHOSEN": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "REJECTED": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
    }.get(status, StatusMark.INFO)


def governance_status(status: str) -> GovernanceStatus:
    rejected = {"REJECTED", "FORBIDDEN_SHORTCUT"}
    policy = {"POLICY_RULE", "CONSISTENCY_RULE", "SCOPE_REQUIRED"}
    pending = {
        "CONVENTION_BLOCKED",
        "DEFERRED_WITH_TARGET",
        "THEOREM_REQUIRED",
        "NOT_DECLARED",
        "NOT_CHOSEN",
        "NOT_ADOPTED",
        "NOT_DERIVED",
        "NOT_READY",
        "OPEN",
    }
    if status in rejected:
        return GovernanceStatus.REJECTED_ROUTE
    if status in policy:
        return GovernanceStatus.POLICY_RULE
    if status in pending:
        return GovernanceStatus.UNVERIFIED
    return GovernanceStatus.UNVERIFIED


def obligation_status(status: str) -> ObligationStatus:
    if status in {"CLOSED_FOR_REVIEW", "REVIEW_READY_ONLY", "PASS", "MATCHED_EXPECTATION"}:
        return ObligationStatus.OPEN
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
            "G46-1: convention-field audit",
            "Group 46 opened as a convention-field closure audit for explicit parallel trace records",
            "CONVENTION_FIELD_AUDIT",
            "The group attacked zeta convention, traced dimension d, normalization scope, branch-pair consistency, and handoff classification without branch choice.",
            "Field closure or classification is not trace-normalization declaration, adoption, insertion, or parent readiness.",
        ),
        StatusEntry(
            "G46-2: zeta convention",
            "shared zeta field inside the paired records",
            "CLOSED_FOR_REVIEW",
            "zeta may be carried for record review as a shared record-local trace-payload symbol across both metric and scale records.",
            "zeta is not F_zeta, not an active field, not residual control, not active O, and not B_s/F_zeta insertion.",
        ),
        StatusEntry(
            "G46-3: traced dimension d",
            "symbolic traced-dimension field",
            "CLOSED_FOR_REVIEW",
            "symbolic d is closed for record review as the denominator attached to the traced payload and may be shared across the pair.",
            "numeric d remains scope-dependent and cannot absorb the factor-of-two burden.",
        ),
        StatusEntry(
            "G46-4: normalization scope",
            "record-review, declaration, insertion, and parent-facing scope",
            "CONVENTION_BLOCKED",
            "record-review scope is usable, but declaration scope and parent-facing scope remain blocked by missing status, assumptions, and theorem support.",
            "scope review cannot become declaration, insertion, or parent-facing trace normalization by summary prose.",
        ),
        StatusEntry(
            "G46-5: branch-pair consistency",
            "paired metric and scale record consistency after convention classification",
            "REVIEW_READY_ONLY",
            "the pair is convention-consistent for review: shared zeta, shared symbolic d, expression separation, and record-domain limits are preserved.",
            "review consistency is not declaration readiness and the pair is not one neutral law.",
        ),
        StatusEntry(
            "G46-6: route classification",
            "honest route classification after field audits",
            "DEFERRED_WITH_TARGET",
            "the next non-looping target is normalization declaration-scope closure or an explicit declaration-scope axiom/choice audit.",
            "do not loop over all convention fields again and do not attempt declaration before scope/status closure.",
        ),
        StatusEntry(
            "G46-7: batch reconciliation",
            "actual batch outputs reconciled before summary",
            "MATCHED_EXPECTATION",
            "outputs matched the expected shape: zeta and symbolic d closed for review, scope is the main blocker, pair remains review-ready only.",
            "reconciliation is not group closure by itself, branch choice, trace declaration, adoption, theorem proof, or insertion.",
        ),
        StatusEntry(
            "G46-8: downstream locks",
            "adoption, insertion, active O, residual/source safety, recombination, and parent closure",
            "NOT_READY",
            "all downstream gates remain closed after convention-field clarification.",
            "Group 46 supplies no B_s/F_zeta insertion law, no active projector, no residual/source theorem, no recombination, and no parent equation.",
        ),
    ]


def build_gaps() -> List[GapEntry]:
    return [
        GapEntry(
            "G1: declaration scope",
            "CONVENTION_BLOCKED",
            "normalization declaration scope remains the principal blocker before any parallel trace-normalization declaration attempt",
            "target declaration-scope closure directly rather than repeating the full convention-field audit",
        ),
        GapEntry(
            "G2: declaration status",
            "NOT_DECLARED",
            "review-ready records still lack declaration status and explicit assumptions",
            "review-ready only must not be reported as declaration-ready",
        ),
        GapEntry(
            "G3: numeric dimension",
            "SCOPE_REQUIRED",
            "numeric d remains tied to an explicit normalization scope",
            "do not set d by recovery, algebraic prettiness, or factor-of-two erasure",
        ),
        GapEntry(
            "G4: parent-facing scope",
            "THEOREM_REQUIRED",
            "parent-facing trace scope requires residual/source/boundary/divergence support that is not supplied here",
            "do not call any scope parent-facing by name alone",
        ),
        GapEntry(
            "G5: branch choice",
            "NOT_CHOSEN",
            "B_s_metric and b_s_scale remain paired non-active candidates",
            "shared zeta and d fields cannot choose either branch",
        ),
        GapEntry(
            "G6: Package B adoption",
            "NOT_ADOPTED",
            "convention-field clarity does not adopt Package B",
            "adoption remains a separate explicit theory decision after declarations and support exist",
        ),
        GapEntry(
            "G7: insertion and downstream safety",
            "NOT_READY",
            "B_s/F_zeta insertion, active O, residual control, source protection, recombination, and parent closure remain closed",
            "field clarity cannot be used as field-equation machinery",
        ),
    ]


def build_handoffs() -> List[HandoffEntry]:
    return [
        HandoffEntry(
            "H1: declaration-scope closure audit",
            "DEFERRED_WITH_TARGET",
            "attack the normalization declaration-scope blocker directly",
            "must distinguish record-review scope from declaration scope and parent-facing scope",
        ),
        HandoffEntry(
            "H2: declaration-scope axiom or choice audit",
            "DEFERRED_WITH_TARGET",
            "if scope cannot be derived, classify whether a daylight-labeled convention or axiom is required",
            "axiom need is not axiom adoption and cannot be chosen from recovery or insertion convenience",
        ),
        HandoffEntry(
            "H3: parallel declaration attempt after scope closure",
            "NOT_DECLARED",
            "attempt only after declaration scope, status, assumptions, zeta convention, and dimension requirements are explicit",
            "not available directly from Group 46",
        ),
        HandoffEntry(
            "H4: residual/source safety theorem route",
            "NOT_DERIVED",
            "continue theorem work if declaration scope depends on residual/source/boundary safety",
            "review-ready records provide no theorem support by themselves",
        ),
        HandoffEntry(
            "H5: insertion or parent route",
            "NOT_READY",
            "not available from Group 46",
            "forbidden as immediate handoff",
        ),
    ]


def build_rejected_upgrades() -> List[RejectedUpgrade]:
    return [
        RejectedUpgrade("R1: review-ready as declaration-ready", "treat review-ready parallel records as trace-normalization declaration", "scope/status blockers remain"),
        RejectedUpgrade("R2: zeta convention as active field", "let shared zeta become F_zeta, residual control, active O, or insertion support", "zeta is record-local trace payload only"),
        RejectedUpgrade("R3: symbolic d as numeric declaration", "fix a numerical d before normalization scope is explicit", "numeric dimension remains scope-dependent"),
        RejectedUpgrade("R4: d erases factor of two", "change dimension fields to collapse zeta/d and 2*zeta/d", "factor-of-two burden must stay visible"),
        RejectedUpgrade("R5: review scope as declaration scope", "treat record-review scope as declaration or parent-facing scope", "scope is the main remaining convention blocker"),
        RejectedUpgrade("R6: pair consistency as neutral law", "collapse the pair into unqualified B_s, neutral F_zeta, or a compromise law", "parallel records are not one law"),
        RejectedUpgrade("R7: scope blocker as no-go theorem", "treat scope blockage as proof the parallel route fails", "blocker means targeted next work"),
        RejectedUpgrade("R8: field audit as insertion", "open B_s/F_zeta insertion, recombination, active O, or parent route from field clarity", "downstream gates remain closed"),
    ]


def case_0(out: ScriptOutput) -> None:
    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  What did Group 46 establish about the shared convention fields for the explicit")
    print("  parallel trace-normalization records?")
    print("\nDiscipline:\n")
    print("  This script summarizes Group 46 after reviewing the batch outputs.")
    print("  It keeps the result at review-ready-only status.")
    print("  It does not choose a branch, declare trace normalization, adopt Package B,")
    print("  insert B_s/F_zeta, construct active O, or open parent closure.")
    with out.governance_assessments():
        out.line(
            "Group 46 status summary opened",
            StatusMark.PASS,
            "closing convention-field closure audit while preserving review-ready-only / declaration-scope-blocked boundary",
        )


def case_1(out: ScriptOutput) -> None:
    header("Case 1: Group 46 summary boundary ledger")
    ledger = [
        ("zeta convention", "CLOSED_FOR_REVIEW", "shared record-local trace-payload symbol for paired record review"),
        ("symbolic d", "CLOSED_FOR_REVIEW", "shared traced-dimension field for review; numeric d remains scope-dependent"),
        ("normalization scope", "CONVENTION_BLOCKED", "record-review scope usable; declaration and parent-facing scope blocked"),
        ("pair consistency", "REVIEW_READY_ONLY", "parallel records convention-consistent for review and noncollapsed"),
        ("factor-of-two burden", "CONSISTENCY_RULE", "2*zeta/d and zeta/d remain separated"),
        ("trace declaration", "NOT_DECLARED", "declaration remains blocked by scope/status and explicit assumptions"),
        ("downstream gates", "NOT_READY", "adoption, insertion, active O, residual control, recombination, and parent closure remain closed"),
    ]
    with out.governance_assessments():
        for name, status, detail in ledger:
            out.line(name, mark(status), f"{status}: {detail}")


def case_2(out: ScriptOutput, entries: List[StatusEntry]) -> None:
    header("Case 2: Group 46 status entries")
    with out.governance_assessments():
        for item in entries:
            subheader(item.name)
            print(f"Topic: {item.topic}")
            out.line(item.name, mark(item.status), f"{item.status}: {item.conclusion} Boundary: {item.boundary}")
    with out.governance_assessments():
        out.line("Group 46 status entries stated", StatusMark.PASS, f"{len(entries)} status entries stated")


def case_3(out: ScriptOutput, gaps: List[GapEntry]) -> None:
    header("Case 3: Final open gaps")
    with out.unresolved_obligations():
        for item in gaps:
            subheader(item.name)
            out.line(item.name, mark(item.status), f"{item.status}: {item.gap}. Discipline: {item.discipline}")
        out.line("Group 46 final gaps stated", StatusMark.PASS, f"{len(gaps)} gaps remain open, blocked, not declared, not adopted, not derived, or not ready")


def case_4(out: ScriptOutput, handoffs: List[HandoffEntry]) -> None:
    header("Case 4: Final handoffs")
    with out.governance_assessments():
        for item in handoffs:
            subheader(item.name)
            out.line(item.name, mark(item.status), f"{item.status}: {item.route}. Caution: {item.caution}")
        out.line("Group 46 handoffs stated", StatusMark.DEFER, f"{len(handoffs)} handoffs stated; declaration-scope closure is the next non-looping target")


def case_5(out: ScriptOutput, rejected: List[RejectedUpgrade]) -> None:
    header("Case 5: Rejected summary upgrades")
    with out.governance_assessments():
        for item in rejected:
            subheader(item.name)
            print(f"Upgrade: {item.upgrade}")
            out.line(item.name, StatusMark.OBLIGATION, f"POLICY_RULE: {item.reason}")
        out.line("Group 46 summary upgrades rejected", StatusMark.PASS, f"{len(rejected)} upgrade shortcuts rejected as policy rules")


def case_6(out: ScriptOutput) -> None:
    header("Case 6: Group 46 conclusions")
    conclusions = [
        ("C1: Group 46 result", "CONVENTION_FIELD_AUDIT", "Group 46 completed a parallel trace convention-field closure audit"),
        ("C2: zeta status", "CLOSED_FOR_REVIEW", "zeta is shared and record-local for review only"),
        ("C3: dimension status", "CLOSED_FOR_REVIEW", "symbolic d is shared for review; numeric d is scope-dependent"),
        ("C4: scope status", "CONVENTION_BLOCKED", "record-review scope is usable, but declaration scope remains the main blocker"),
        ("C5: pair status", "REVIEW_READY_ONLY", "parallel records are convention-consistent for review only"),
        ("C6: declaration status", "NOT_DECLARED", "trace normalization is not declared"),
        ("C7: downstream status", "NOT_READY", "B_s/F_zeta insertion, active O, recombination, and parent equation remain not ready"),
    ]
    with out.governance_assessments():
        for name, status, detail in conclusions:
            subheader(name)
            out.line(name, mark(status), f"{status}: {detail}")
        out.line("Group 46 status summary conclusion stated", StatusMark.PASS, "convention fields sharpened; review-ready-only status preserved; declaration-scope closure named as next target")
    print("\n" + "=" * 120)
    print("Final interpretation")
    print("=" * 120)
    print("Group 46 status summary result:\n")
    print("  Group 46 completed a parallel trace convention-field closure audit.")
    print("  The zeta convention is closed for record review as a shared trace-payload symbol.")
    print("  Symbolic d is closed for record review as the shared traced-dimension field.")
    print("  Numeric d remains tied to explicit normalization scope.")
    print("  Record-review scope is usable for comparing the paired records.")
    print("  Declaration scope and parent-facing scope remain blocked.")
    print("  The metric/scale pair is convention-consistent for review only.")
    print("  The factor-of-two burden remains visible: 2*zeta/d and zeta/d are not collapsed.")
    print("  No branch is chosen.")
    print("  No trace-normalization declaration is completed.")
    print("  Package B is not adopted or recommended for adoption.")
    print("  B_s/F_zeta insertion, active O, residual control, source protection, recombination, and parent equation remain not ready.")
    print("\nPossible next step:")
    print("  normalization declaration-scope closure audit, declaration-scope axiom/choice audit,")
    print("  or residual/source theorem route if scope closure depends on safety theorems")
    print("\nForbidden immediate next step:")
    print("  trace-normalization declaration, Package B adoption, B_s/F_zeta insertion, active O, recombination, or parent closure")


def record_governance(ns, entries: List[StatusEntry], gaps: List[GapEntry], handoffs: List[HandoffEntry], rejected: List[RejectedUpgrade]) -> None:
    record_marker(ns, MARKER_ID, MARKER_ID, "Group 46 parallel trace convention-field closure audit status summary")
    claim_index = 1
    for item in entries:
        record_claim(ns, f"{MARKER_ID}_c{claim_index}", MARKER_ID, item.status, f"{item.name}: {item.topic}. {item.conclusion}. Boundary: {item.boundary}")
        claim_index += 1
    for item in handoffs:
        record_claim(ns, f"{MARKER_ID}_c{claim_index}", MARKER_ID, item.status, f"{item.name}: {item.route}. Caution: {item.caution}")
        claim_index += 1
    for item in rejected:
        record_claim(ns, f"{MARKER_ID}_c{claim_index}", MARKER_ID, "POLICY_RULE", f"{item.name}: rejected upgrade: {item.upgrade}. Reason: {item.reason}")
        claim_index += 1
    for idx, item in enumerate(gaps, 1):
        record_obligation(ns, f"{MARKER_ID}_o{idx}", f"Carry forward {item.name}: {item.gap}. Discipline: {item.discipline}", item.status)


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
