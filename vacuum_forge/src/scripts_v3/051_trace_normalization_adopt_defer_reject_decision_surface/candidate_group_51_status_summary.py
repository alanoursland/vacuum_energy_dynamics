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
SCRIPT_LABEL = "Candidate Group 51 Status Summary"
MARKER_ID = "g51_summary"

DEPENDENCIES = [
    (
        "g50_summary",
        "050_symbolic_paired_trace_normalization_declaration_attempt__candidate_group_50_status_summary",
        "g50_summary",
    ),
    (
        "g51_problem",
        "051_trace_normalization_adopt_defer_reject_decision_surface__candidate_adopt_defer_reject_decision_problem",
        "g51_problem",
    ),
    (
        "g51_record_level_adoption",
        "051_trace_normalization_adopt_defer_reject_decision_surface__candidate_record_level_adoption_meaning_audit",
        "g51_record_level_adoption",
    ),
    (
        "g51_branch_burden_sanity",
        "051_trace_normalization_adopt_defer_reject_decision_surface__candidate_branch_burden_symbolic_sanity_check",
        "g51_branch_burden_sanity",
    ),
    (
        "g51_prereq_matrix",
        "051_trace_normalization_adopt_defer_reject_decision_surface__candidate_adoption_prerequisite_matrix",
        "g51_prereq_matrix",
    ),
    (
        "g51_defer_route",
        "051_trace_normalization_adopt_defer_reject_decision_surface__candidate_defer_route_and_theorem_dependency_audit",
        "g51_defer_route",
    ),
    (
        "g51_rejection_sieve",
        "051_trace_normalization_adopt_defer_reject_decision_surface__candidate_rejection_trigger_sieve",
        "g51_rejection_sieve",
    ),
    (
        "g51_route_classifier",
        "051_trace_normalization_adopt_defer_reject_decision_surface__candidate_decision_surface_route_classifier",
        "g51_route_classifier",
    ),
    (
        "g51_reconciliation",
        "051_trace_normalization_adopt_defer_reject_decision_surface__candidate_adopt_defer_reject_decision_batch_reconciliation",
        "g51_reconciliation",
    ),
]


@dataclass(frozen=True)
class StatusEntry:
    name: str
    topic: str
    status: str
    conclusion: str
    boundary: str


@dataclass(frozen=True)
class BurdenEntry:
    name: str
    status: str
    burden: str
    discipline: str


@dataclass(frozen=True)
class RejectedUpgrade:
    name: str
    upgrade: str
    reason: str


@dataclass(frozen=True)
class HandoffEntry:
    name: str
    status: str
    route: str
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
        "ADOPTION_DECISION_SURFACE": StatusMark.INFO,
        "BRANCH_BURDEN_LIVE": StatusMark.PASS,
        "CONDITIONAL_RECORD_ONLY": StatusMark.INFO,
        "CANDIDATE_RETAINED_FOR_AUDIT": StatusMark.INFO,
        "ADOPTION_DECISION_DEFERRED": StatusMark.DEFER,
        "THEORY_DECISION_REQUIRED": StatusMark.DEFER,
        "DEFERRED_WITH_TARGET": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_INSERTABLE": StatusMark.DEFER,
        "NOT_PARENT_FACING": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "CHOICE_REQUIRED": StatusMark.DEFER,
        "NUMERIC_D_CONDITION": StatusMark.OBLIGATION,
        "SAFETY_THEOREMS_REQUIRED": StatusMark.OBLIGATION,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REJECTED_ROUTE": StatusMark.FAIL,
        "PHYSICAL_USE_REJECTED": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
        "OPEN": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def governance_status(status: str) -> GovernanceStatus:
    if status in {"REJECTED_ROUTE", "PHYSICAL_USE_REJECTED", "FORBIDDEN_SHORTCUT"}:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {
        "POLICY_RULE",
        "SAFETY_THEOREMS_REQUIRED",
        "NUMERIC_D_CONDITION",
        "BRANCH_BURDEN_LIVE",
    }:
        return GovernanceStatus.POLICY_RULE
    return GovernanceStatus.UNVERIFIED


def obligation_status(status: str) -> ObligationStatus:
    if status in {
        "ADOPTION_DECISION_DEFERRED",
        "THEORY_DECISION_REQUIRED",
        "DEFERRED_WITH_TARGET",
        "NOT_ADOPTED",
        "NOT_INSERTABLE",
        "NOT_PARENT_FACING",
        "NOT_READY",
        "CHOICE_REQUIRED",
    }:
        return ObligationStatus.DEFERRED
    return ObligationStatus.OPEN


def record_marker(ns, marker_id: str, symbol_name: str, scope: str) -> None:
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[],
        output=sp.Symbol(symbol_name),
        method="inventory marker; group status summary, no physical derivation",
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


def record_obligation(ns, obligation_id: str, statement: str, status: str) -> None:
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


def emit_line(out: ScriptOutput, label: str, status: str, text: str, *, obligation: bool = False) -> None:
    if obligation:
        with out.unresolved_obligations():
            out.line(label, mark(status), f"{status}: {text}")
    else:
        with out.governance_assessments():
            out.line(label, mark(status), f"{status}: {text}")


def build_status_entries() -> List[StatusEntry]:
    return [
        StatusEntry(
            name="G51-1: decision-surface scope",
            topic="adopt/defer/reject route classification",
            status="ADOPTION_DECISION_SURFACE",
            conclusion="Group 51 classified the decision surface for the Group 50 conditional paired attempt",
            boundary="classification is not adoption",
        ),
        StatusEntry(
            name="G51-2: branch burden anchor",
            topic="symbolic factor-of-two check",
            status="BRANCH_BURDEN_LIVE",
            conclusion="the paired expressions differ by zeta/d, so the branch burden remains live",
            boundary="not branch choice, neutral collapse, or adoption evidence",
        ),
        StatusEntry(
            name="G51-3: conditional candidate retention",
            topic="narrow record route",
            status="CANDIDATE_RETAINED_FOR_AUDIT",
            conclusion="the conditional attempt can be retained only as caveated audit material",
            boundary="not Package B adoption or physical use",
        ),
        StatusEntry(
            name="G51-4: strong adoption route",
            topic="adoption stronger than candidate retention",
            status="ADOPTION_DECISION_DEFERRED",
            conclusion="strong adoption remains deferred pending explicit decision, choices, and safety prerequisites",
            boundary="not adopted by script output",
        ),
        StatusEntry(
            name="G51-5: rejected adoption upgrades",
            topic="bad broadenings",
            status="REJECTED_ROUTE",
            conclusion="neutral collapse, numeric-d leak, recovery support, hidden branch choice, insertion drift, and caveats-as-theorems are rejected",
            boundary="rejection of broadenings is not rejection of the narrow conditional candidate",
        ),
        StatusEntry(
            name="G51-6: physical-use status",
            topic="B_s/F_zeta insertion and parent route",
            status="NOT_INSERTABLE",
            conclusion="B_s/F_zeta insertion, active O, recombination, and parent closure remain closed",
            boundary="not field-equation machinery",
        ),
        StatusEntry(
            name="G51-7: handoff status",
            topic="next non-looping route",
            status="DEFERRED_WITH_TARGET",
            conclusion="the best technical handoff is residual/source/boundary safety load testing, with separate theory-owner decision still available",
            boundary="not another trace-declaration loop",
        ),
    ]


def build_burdens() -> List[BurdenEntry]:
    return [
        BurdenEntry(
            name="B1: numeric-d burden",
            status="NUMERIC_D_CONDITION",
            burden="numeric d remains conditioned and unfixed",
            discipline="do not hide a dimension choice inside symbolic d",
        ),
        BurdenEntry(
            name="B2: branch-choice burden",
            status="CHOICE_REQUIRED",
            burden="metric and scale branches remain paired unless a separate branch decision is made",
            discipline="do not collapse the zeta/d branch difference by prose",
        ),
        BurdenEntry(
            name="B3: residual/source burden",
            status="SAFETY_THEOREMS_REQUIRED",
            burden="count-once scalar trace, residual nonentry, source no-double-counting, and A-sector mass protection remain required",
            discipline="do not treat caveats as positive safety theorems",
        ),
        BurdenEntry(
            name="B4: boundary/scalar-silence burden",
            status="SAFETY_THEOREMS_REQUIRED",
            burden="boundary neutrality and exterior scalar silence remain required before insertion",
            discipline="do not allow scalar tail or boundary leakage by record status",
        ),
        BurdenEntry(
            name="B5: insertion-law burden",
            status="NOT_INSERTABLE",
            burden="B_s/F_zeta insertion requires a separate law and cannot be inferred from the trace-normalization record",
            discipline="do not let retained candidate status become field-equation use",
        ),
        BurdenEntry(
            name="B6: theory-owner decision burden",
            status="THEORY_DECISION_REQUIRED",
            burden="any actual adopt/defer/reject decision remains a separate theory-owner decision",
            discipline="do not let summary wording perform adoption",
        ),
    ]


def build_rejected_upgrades() -> List[RejectedUpgrade]:
    return [
        RejectedUpgrade(
            name="R1: summary as adoption",
            upgrade="write Group 51 as if the conditional attempt were adopted",
            reason="Group 51 classified routes only",
        ),
        RejectedUpgrade(
            name="R2: retained candidate as insertion",
            upgrade="use retained audit candidate status to insert B_s/F_zeta",
            reason="physical use remains closed",
        ),
        RejectedUpgrade(
            name="R3: single-expression summary",
            upgrade="summarize with only one trace-normalization expression",
            reason="the branch-burden check keeps the zeta/d difference visible",
        ),
        RejectedUpgrade(
            name="R4: recovery-supported adoption",
            upgrade="support trace normalization with Schwarzschild, AB=1, gamma, or weak-field recovery",
            reason="recovery remains audit, not construction",
        ),
        RejectedUpgrade(
            name="R5: caveats as theorems",
            upgrade="treat non-use caveats as residual/source/boundary safety proofs",
            reason="negative caveats are not positive theorems",
        ),
        RejectedUpgrade(
            name="R6: decision-surface as parent readiness",
            upgrade="treat the decision surface as recombination or parent-equation readiness",
            reason="parent identity and divergence support remain absent",
        ),
    ]


def build_handoffs() -> List[HandoffEntry]:
    return [
        HandoffEntry(
            name="H1: residual/source safety route",
            status="DEFERRED_WITH_TARGET",
            route="test whether the conditional trace-normalization attempt can coexist with count-once scalar trace, residual nonentry, source no-double-counting, and A-sector mass protection",
            caution="this would be safety load testing, not insertion",
        ),
        HandoffEntry(
            name="H2: boundary/scalar silence route",
            status="DEFERRED_WITH_TARGET",
            route="test boundary neutrality and exterior scalar silence before any insertion attempt",
            caution="do not use trace-record status to suppress boundary or scalar-tail problems",
        ),
        HandoffEntry(
            name="H3: explicit theory-owner decision route",
            status="THEORY_DECISION_REQUIRED",
            route="make an explicit adopt/defer/reject decision only as a separate theory-owner action",
            caution="a script can inventory burdens but must not decide adoption by theorem-like output",
        ),
        HandoffEntry(
            name="H4: forbidden immediate route",
            status="NOT_INSERTABLE",
            route="do not move directly to B_s/F_zeta insertion, active O, recombination, or parent closure",
            caution="Group 51 sharpened the decision burden but opened no physical-use route",
        ),
    ]


def record_governance(
    ns,
    entries: List[StatusEntry],
    burdens: List[BurdenEntry],
    rejected: List[RejectedUpgrade],
    handoffs: List[HandoffEntry],
) -> None:
    record_marker(
        ns,
        MARKER_ID,
        "G51_trace_normalization_decision_surface_summary",
        "Group 51 adopt/defer/reject decision surface summary; no adoption or insertion",
    )

    for idx, item in enumerate(entries, start=1):
        record_claim(
            ns,
            f"{MARKER_ID}_entry_{idx}",
            MARKER_ID,
            item.status,
            f"{item.name}: {item.conclusion}. Boundary: {item.boundary}.",
        )

    for idx, item in enumerate(burdens, start=1):
        record_obligation(
            ns,
            f"{MARKER_ID}_burden_{idx}",
            f"{item.name}: {item.burden}. Discipline: {item.discipline}.",
            item.status,
        )

    for idx, item in enumerate(rejected, start=1):
        record_claim(
            ns,
            f"{MARKER_ID}_rejected_{idx}",
            MARKER_ID,
            "REJECTED_ROUTE",
            f"Rejected upgrade: {item.upgrade}. Reason: {item.reason}.",
        )

    for idx, item in enumerate(handoffs, start=1):
        record_obligation(
            ns,
            f"{MARKER_ID}_handoff_{idx}",
            f"{item.name}: {item.route}. Caution: {item.caution}.",
            item.status,
        )


def case_0(out: ScriptOutput) -> None:
    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  What did Group 51 establish about the adopt/defer/reject decision")
    print("  surface for the Group 50 conditional paired trace-normalization attempt?\n")
    print("Discipline:\n")
    print("  This script summarizes the Group 51 decision-surface batch.")
    print("  It must preserve the distinction between candidate retention,")
    print("  strong adoption, physical use, rejection triggers, and theory-owner")
    print("  decision authority.")
    emit_line(
        out,
        "Group 51 status summary opened",
        "PASS",
        "closing decision-surface audit while preserving no-adoption, no-insertion, and no-parent boundary",
    )


def case_1(out: ScriptOutput) -> None:
    header("Case 1: Group 51 compact result ledger")
    ledger = [
        (
            "decision-surface audit",
            "ADOPTION_DECISION_SURFACE",
            "Group 51 classified routes and burdens without deciding adoption",
        ),
        (
            "branch burden",
            "BRANCH_BURDEN_LIVE",
            "the paired expressions differ by zeta/d, so factor-of-two burden remains visible",
        ),
        (
            "candidate retention",
            "CANDIDATE_RETAINED_FOR_AUDIT",
            "the conditional attempt survives only as caveated audit candidate",
        ),
        (
            "strong adoption",
            "ADOPTION_DECISION_DEFERRED",
            "strong adoption remains deferred pending explicit decision and prerequisites",
        ),
        (
            "bad broadenings",
            "REJECTED_ROUTE",
            "neutral collapse, numeric leak, recovery support, hidden branch choice, insertion drift, and caveats-as-theorems are rejected",
        ),
        (
            "physical use",
            "NOT_INSERTABLE",
            "B_s/F_zeta insertion, active O, recombination, and parent closure remain closed",
        ),
        (
            "handoff",
            "DEFERRED_WITH_TARGET",
            "residual/source/boundary safety load testing is the best non-looping technical target",
        ),
    ]
    for label, status, text in ledger:
        emit_line(out, label, status, text)


def case_2(out: ScriptOutput, entries: List[StatusEntry]) -> None:
    header("Case 2: Group 51 status entries")
    for entry in entries:
        subheader(entry.name)
        print(f"Topic: {entry.topic}")
        emit_line(out, entry.name, entry.status, f"{entry.conclusion}. Boundary: {entry.boundary}.")
    emit_line(out, "Group 51 status entries stated", "PASS", f"{len(entries)} status entries stated")


def case_3(out: ScriptOutput, burdens: List[BurdenEntry]) -> None:
    header("Case 3: Open burdens after Group 51")
    for burden in burdens:
        subheader(burden.name)
        emit_line(
            out,
            burden.name,
            burden.status,
            f"{burden.burden}. Discipline: {burden.discipline}.",
            obligation=True,
        )
    emit_line(
        out,
        "Group 51 burdens preserved",
        "PASS",
        f"{len(burdens)} adoption/use burdens remain explicit",
        obligation=True,
    )


def case_4(out: ScriptOutput, rejected: List[RejectedUpgrade]) -> None:
    header("Case 4: Rejected summary upgrades")
    for item in rejected:
        subheader(item.name)
        print(f"Upgrade: {item.upgrade}")
        emit_line(out, item.name, "REJECTED_ROUTE", item.reason)
    emit_line(out, "Group 51 rejected upgrades preserved", "PASS", f"{len(rejected)} upgrade shortcuts rejected")


def case_5(out: ScriptOutput, handoffs: List[HandoffEntry]) -> None:
    header("Case 5: Safe handoffs")
    for handoff in handoffs:
        subheader(handoff.name)
        emit_line(out, handoff.name, handoff.status, f"{handoff.route}. Caution: {handoff.caution}.")
    emit_line(
        out,
        "Group 51 handoffs stated",
        "DEFERRED_WITH_TARGET",
        f"{len(handoffs)} handoff routes stated without opening physical use",
    )


def case_6(out: ScriptOutput) -> None:
    header("Case 6: Final interpretation")
    conclusions = [
        (
            "C1: Group 51 result",
            "ADOPTION_DECISION_SURFACE",
            "Group 51 classified the adopt/defer/reject decision surface for the Group 50 conditional attempt",
        ),
        (
            "C2: candidate status",
            "CANDIDATE_RETAINED_FOR_AUDIT",
            "the conditional attempt may be retained only as caveated audit material",
        ),
        (
            "C3: symbolic burden status",
            "BRANCH_BURDEN_LIVE",
            "the metric and scale expressions differ by zeta/d and must both remain visible",
        ),
        (
            "C4: adoption status",
            "ADOPTION_DECISION_DEFERRED",
            "strong adoption is deferred and requires separate explicit decision plus prerequisites",
        ),
        (
            "C5: physical-use status",
            "NOT_INSERTABLE",
            "B_s/F_zeta insertion, active O, recombination, and parent route remain closed",
        ),
        (
            "C6: next technical pressure",
            "DEFERRED_WITH_TARGET",
            "residual/source/boundary safety load testing is the best non-looping technical target",
        ),
    ]
    for label, status, text in conclusions:
        emit_line(out, label, status, text)

    header("Final summary")
    print("Group 51 status summary result:\n")
    print("  Group 51 audited the adopt/defer/reject decision surface for the")
    print("  Group 50 conditional symbolic paired trace-normalization attempt.")
    print()
    print("  The paired expressions remain visible:")
    print("    log(B_s_metric)=2*zeta/d")
    print("    log(b_s_scale)=zeta/d")
    print("  The symbolic sanity check confirmed that their difference is zeta/d,")
    print("  so the branch burden remains live.")
    print()
    print("  The conditional attempt can be retained only as a caveated audit candidate.")
    print("  Strong adoption is deferred and requires a separate theory-owner decision,")
    print("  branch/numeric-d discipline, and safety support.")
    print()
    print("  Rejected upgrades remain rejected: neutral collapse, numeric-d leakage,")
    print("  recovery support, hidden branch choice, insertion drift, active-O drift,")
    print("  caveats-as-theorems, recombination, and parent use.")
    print()
    print("  No Package B adoption occurred. No branch was chosen. No B_s/F_zeta")
    print("  insertion was licensed. No active O was constructed. No residual/source")
    print("  or boundary safety theorem was proved. Recombination and parent closure")
    print("  remain closed.")
    print()
    print("Best next technical target:")
    print("  residual/source/boundary safety load testing")
    print()
    print("Separate non-technical/theory-owner option:")
    print("  explicit adopt/defer/reject decision with caveats preserved")
    print()
    print("Forbidden immediate next step:")
    print("  B_s/F_zeta insertion, active O, recombination, or parent closure")


def main() -> None:
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    entries = build_status_entries()
    burdens = build_burdens()
    rejected = build_rejected_upgrades()
    handoffs = build_handoffs()

    case_0(out)
    case_1(out)
    case_2(out, entries)
    case_3(out, burdens)
    case_4(out, rejected)
    case_5(out, handoffs)
    case_6(out)

    record_governance(ns, entries, burdens, rejected, handoffs)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
