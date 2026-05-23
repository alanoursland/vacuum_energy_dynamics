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
    RouteRecord,
    ScriptOutput,
    StatusMark,
)

ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"

# Group:
#   41_safe_membership_precondition_continuation
# Script type:
#   STATUS SUMMARY

SCRIPT_LABEL = "Candidate Group 41 Status Summary"
MARKER_ID = "g41_summary"

DEPENDENCIES = [
    ("g41_recon", "41_safe_membership_precondition_continuation__candidate_safe_membership_precondition_batch_reconciliation", "g41_recon"),
    ("g41_active_boundary", "41_safe_membership_precondition_continuation__candidate_diagnostic_vs_active_membership_boundary", "g41_active_boundary"),
    ("g41_role_purity", "41_safe_membership_precondition_continuation__candidate_role_purity_exclusion_zone_audit", "g41_role_purity"),
    ("g41_criterion_matrix", "41_safe_membership_precondition_continuation__candidate_membership_criterion_precondition_matrix", "g41_criterion_matrix"),
    ("g41_tzeta_sector", "41_safe_membership_precondition_continuation__candidate_Tzeta_sector_precondition_ledger", "g41_tzeta_sector"),
    ("g41_zeta_object", "41_safe_membership_precondition_continuation__candidate_zeta_Bs_object_precondition_ledger", "g41_zeta_object"),
    ("g41_problem", "41_safe_membership_precondition_continuation__candidate_safe_membership_precondition_problem", "g41_problem"),
    ("g40_summary", "40_split_safe_trace_anchor_precondition_audit__candidate_group_40_status_summary", "g40_summary"),
    ("g40_membership_precond", "40_split_safe_trace_anchor_precondition_audit__candidate_safe_membership_split_safe_preconditions", "g40_membership_precond"),
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
        "MATCHED_EXPECTATION": StatusMark.PASS,
        "SAFE_MEMBERSHIP_PRECONDITION_CONTINUATION": StatusMark.INFO,
        "COMPATIBLE_IF_DECLARED": StatusMark.INFO,
        "DIAGNOSTIC_ONLY": StatusMark.INFO,
        "SPLIT_SAFE": StatusMark.INFO,
        "BRANCH_INDEXED": StatusMark.INFO,
        "CONDITIONAL": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "DEFER": StatusMark.DEFER,
        "DECLARATION_DEFERRED": StatusMark.DEFER,
        "NOT_DECLARED": StatusMark.DEFER,
        "NOT_CHOSEN": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "BRANCH_REQUIRED": StatusMark.OBLIGATION,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
    }.get(status, StatusMark.INFO)


def _governance(name: str, fallback=None):
    if fallback is None:
        fallback = GovernanceStatus.POLICY_RULE
    return getattr(GovernanceStatus, name, fallback)


def governance_status_for(status: str):
    """Map script-facing status labels to archive governance statuses when available."""
    info_status = _governance("HEURISTIC")
    deferred_status = _governance("DEFERRED_PENDING_PREREQUISITES", _governance("DEFERRED"))
    candidate_status = _governance("CANDIDATE_ROUTE", info_status)
    policy_status = GovernanceStatus.POLICY_RULE

    return {
        "PASS": info_status,
        "MATCHED_EXPECTATION": info_status,
        "SAFE_MEMBERSHIP_PRECONDITION_CONTINUATION": info_status,
        "COMPATIBLE_IF_DECLARED": candidate_status,
        "DIAGNOSTIC_ONLY": info_status,
        "SPLIT_SAFE": info_status,
        "BRANCH_INDEXED": info_status,
        "CONDITIONAL": deferred_status,
        "OPEN": deferred_status,
        "DEFER": deferred_status,
        "DECLARATION_DEFERRED": deferred_status,
        "NOT_DECLARED": deferred_status,
        "NOT_CHOSEN": deferred_status,
        "NOT_READY": deferred_status,
        "NOT_ADOPTED": deferred_status,
        "NOT_DERIVED": deferred_status,
        "BRANCH_REQUIRED": deferred_status,
        "POLICY_RULE": policy_status,
        "FORBIDDEN_SHORTCUT": policy_status,
    }.get(status, info_status)


def obligation_status(status: str) -> ObligationStatus:
    if status in {
        "NOT_READY",
        "DECLARATION_DEFERRED",
        "NOT_DECLARED",
        "NOT_CHOSEN",
        "NOT_ADOPTED",
        "NOT_DERIVED",
        "BRANCH_REQUIRED",
        "CONDITIONAL",
    }:
        return getattr(ObligationStatus, "DEFERRED", ObligationStatus.OPEN)
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
        scope="Group 41 safe-membership precondition continuation summary",
    )


def record_claim(ns, claim_id: str, marker_id: str, status: str, statement: str) -> None:
    ns.record_claim(
        ClaimRecord(
            claim_id=claim_id,
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=governance_status_for(status),
            statement=statement,
            derivation_ids=[marker_id],
            obligation_ids=[],
        )
    )


def record_obligation(ns, obligation_id: str, marker_id: str, title: str, description: str, status: str = "OPEN") -> None:
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


def build_status_entries() -> List[StatusEntry]:
    return [
        StatusEntry(
            "G41-1: safe-membership continuation opener",
            "Group 41 opened as a safe-membership precondition continuation",
            "SAFE_MEMBERSHIP_PRECONDITION_CONTINUATION",
            "zeta_Bs -> T_zeta was kept diagnostic / compatible-if-declared only while the group sharpened preconditions",
            "the opener chooses no branch, installs no membership, adopts nothing, proves nothing, and opens no downstream route",
        ),
        StatusEntry(
            "G41-2: zeta_Bs object slot",
            "membership-test payload object",
            "CONDITIONAL",
            "zeta_Bs was sharpened as the payload object being tested for membership; branch-sensitive cases must use zeta_Bs_metric and zeta_Bs_scale",
            "object inventory is not F_zeta, not trace normalization, not branch choice, and not B_s/F_zeta insertion",
        ),
        StatusEntry(
            "G41-3: T_zeta sector slot",
            "safe trace-sector target for membership testing",
            "COMPATIBLE_IF_DECLARED",
            "T_zeta was sharpened as a safe trace-sector target or diagnostic label, with conditional branch-indexed sector variants if needed",
            "T_zeta is not active O, not a projector, not incidence, not residual control, and not a field-equation sector",
        ),
        StatusEntry(
            "G41-4: membership criteria",
            "criterion matrix for later membership testing",
            "CONDITIONAL",
            "type, trace-payload, role-purity, branch-index consistency, diagnostic-inertness, exclusion-zone, declaration-support, and theorem-support criteria were stated",
            "membership-testable means precondition clarity only, not theorem-ready or declaration-ready",
        ),
        StatusEntry(
            "G41-5: role purity and exclusion zones",
            "mandatory payload exclusions",
            "POLICY_RULE",
            "residual, ordinary source, A-sector mass, correction tensor, boundary/shell, divergence repair, trace-normalization/branch-choice, recombination, active O, insertion, and parent closure payloads were excluded",
            "exclusion zones are preconditions, not no-overlap, residual-nonentry, source-routing, divergence-safety, or boundary-neutrality theorems",
        ),
        StatusEntry(
            "G41-6: diagnostic versus active boundary",
            "membership status ladder",
            "DIAGNOSTIC_ONLY",
            "diagnostic label, compatible-if-declared, candidate-if-preconditions-met, future declaration candidate, future theorem target, and active-membership-forbidden statuses were separated",
            "future route labels are not current declarations, proofs, adoption, active O, insertion, or parent readiness",
        ),
        StatusEntry(
            "G41-7: batch reconciliation",
            "actual batch outputs were reconciled before summary",
            "MATCHED_EXPECTATION",
            "outputs matched the expected safe-membership precondition sharpening shape: object, sector, criteria, role-purity, and diagnostic boundaries sharpened; active membership not installed",
            "reconciliation is not declaration completion or theorem proof",
        ),
        StatusEntry(
            "G41-8: Package B and downstream gates",
            "Package B, insertion, active O, residual control, and parent closure",
            "NOT_READY",
            "Package B remains compatible-if-declared only and all downstream gates remain closed",
            "Group 41 is not Package B adoption, B_s/F_zeta insertion, active O, residual control, or parent readiness",
        ),
    ]


def build_gaps() -> List[GapEntry]:
    return [
        GapEntry(
            "G1: active safe-membership declaration",
            "NOT_DECLARED",
            "safe-membership slots are sharper but no active zeta_Bs -> T_zeta membership is installed",
            "later declaration work requires separate explicit record and closed preconditions",
        ),
        GapEntry(
            "G2: membership-test object domain",
            "OPEN",
            "the class of candidate trace-payload objects remains a required later definition",
            "object-domain clarity is required before theorem or declaration use",
        ),
        GapEntry(
            "G3: T_zeta sector definition",
            "OPEN",
            "T_zeta is sharpened as a safe trace-sector target but not defined as an active sector",
            "diagnostic label and future sector route must remain separate",
        ),
        GapEntry(
            "G4: domain/codomain and criteria closure",
            "OPEN",
            "domain, codomain, and membership criteria remain preconditions rather than proof",
            "membership-testable means only that later requirements are visible",
        ),
        GapEntry(
            "G5: role-purity enforcement",
            "NOT_DERIVED",
            "exclusion zones are visible but enforcement is not proved",
            "no source no-double-counting, no-overlap, residual nonentry, divergence safety, or boundary neutrality theorem is supplied",
        ),
        GapEntry(
            "G6: branch status and trace normalization",
            "DECLARATION_DEFERRED",
            "B_s_metric and b_s_scale remain unchosen; trace normalization remains separate and branch-required",
            "membership cannot carry zeta/d, 2*zeta/d, or branch choice payloads",
        ),
        GapEntry(
            "G7: Package B declaration and adoption",
            "NOT_ADOPTED",
            "Package B remains minimal plausible-to-audit / compatible-if-declared only",
            "adoption remains a separate explicit decision after declarations and support exist",
        ),
        GapEntry(
            "G8: insertion and parent closure",
            "NOT_READY",
            "membership precondition sharpening does not resolve insertion, active O, residual control, recombination, or parent gates",
            "B_s/F_zeta insertion and parent equation remain closed",
        ),
    ]


def build_handoffs() -> List[HandoffEntry]:
    return [
        HandoffEntry(
            "H1: safe-membership declaration attempt",
            "NOT_DECLARED",
            "may later evaluate whether the sharpened preconditions are enough for an explicit declaration attempt",
            "must not treat Group 41 as declaration-ready by itself",
        ),
        HandoffEntry(
            "H2: membership theorem route",
            "NOT_DERIVED",
            "may later attempt actual membership proof after declarations, assumptions, object, sector, domain/codomain, criteria, branch status, and exclusions are explicit",
            "criteria visibility is not theorem support",
        ),
        HandoffEntry(
            "H3: role-purity theorem route",
            "NOT_DERIVED",
            "may later try to prove source/no-double-counting, residual nonentry, divergence safety, or boundary neutrality claims",
            "role-purity policy boundaries are not those theorems",
        ),
        HandoffEntry(
            "H4: branch-indexed membership comparison",
            "BRANCH_INDEXED",
            "may keep zeta_Bs_metric / zeta_Bs_scale and T_zeta_metric / T_zeta_scale variants parallel where branch-sensitive",
            "parallel branch indexing is not branch choice or exact trace normalization",
        ),
        HandoffEntry(
            "H5: neutral diagnostic membership use",
            "DIAGNOSTIC_ONLY",
            "may use diagnostic compatibility labels for bookkeeping",
            "diagnostic labels must stay source, metric, divergence, projector, insertion, theorem, adoption, and parent inert",
        ),
        HandoffEntry(
            "H6: Package B adoption route",
            "NOT_ADOPTED",
            "not available from Group 41 alone",
            "requires separate declaration/adoption decision and theorem or explicit support",
        ),
        HandoffEntry(
            "H7: insertion or parent route",
            "NOT_READY",
            "not available from Group 41",
            "forbidden as immediate handoff",
        ),
    ]


def build_rejected_upgrades() -> List[RuleEntry]:
    return [
        RuleEntry("R1: compatibility as declaration", "treat diagnostic / compatible-if-declared membership as declared", "current status is not declaration-ready"),
        RuleEntry("R2: object as response/insertion", "treat zeta_Bs as F_zeta, trace normalization, branch choice, or B_s/F_zeta insertion", "object slot is only a membership-test payload slot"),
        RuleEntry("R3: sector as active projector", "treat T_zeta as active O or a projection operator", "T_zeta is a safe trace-sector target, not O"),
        RuleEntry("R4: criteria as theorem", "treat membership criteria as proof of membership", "criterion visibility is precondition clarity only"),
        RuleEntry("R5: role purity as no-overlap theorem", "treat exclusion zones as no-overlap, source-routing, or residual-nonentry proof", "theorem support remains separate"),
        RuleEntry("R6: diagnostic as active", "let diagnostic membership label gain metric, source, divergence, projector, insertion, adoption, or theorem effect", "diagnostic labels remain inert"),
        RuleEntry("R7: membership as Package B adoption", "treat future declaration candidate as Package B adoption", "adoption requires a separate explicit decision"),
        RuleEntry("R8: membership as downstream readiness", "open insertion, active O, residual control, recombination, or parent route", "downstream gates remain closed"),
    ]


def case_0(out: ScriptOutput) -> None:
    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  What did Group 41 establish about safe-membership preconditions for")
    print("  zeta_Bs -> T_zeta while active membership remains uninstalled?")
    print("\nDiscipline:\n")
    print("  This script summarizes Group 41 after reviewing the batch outputs.")
    print("  It does not choose B_s_metric or b_s_scale.")
    print("  It does not complete trace-normalization or safe-membership declarations.")
    print("  It adopts nothing, proves nothing, installs no active O, inserts nothing, and opens no parent gate.")
    with out.governance_assessments():
        out.line(
            "Group 41 status summary opened",
            StatusMark.PASS,
            "closing safe-membership precondition continuation while preserving compatible-if-declared / no-adoption / no-insertion boundary",
        )


def case_1(out: ScriptOutput) -> None:
    header("Case 1: Group 41 summary boundary ledger")
    entries = [
        ("current membership", "COMPATIBLE_IF_DECLARED", "diagnostic / compatible-if-declared only"),
        ("object slot", "CONDITIONAL", "zeta_Bs payload object sharpened; branch variants explicit when needed"),
        ("sector slot", "COMPATIBLE_IF_DECLARED", "T_zeta safe trace-sector target; not O"),
        ("criterion matrix", "CONDITIONAL", "testability means precondition clarity only"),
        ("role purity", "POLICY_RULE", "mandatory exclusion zones stated as boundaries"),
        ("diagnostic boundary", "DIAGNOSTIC_ONLY", "diagnostic labels remain inert"),
        ("downstream gates", "NOT_READY", "adoption, insertion, active O, residual control, and parent closure remain closed"),
    ]
    for name, status, detail in entries:
        with out.governance_assessments():
            out.line(name, mark(status), f"{status}: {detail}")


def case_2(out: ScriptOutput, entries: List[StatusEntry]) -> None:
    header("Case 2: Group 41 status entries")
    for item in entries:
        subheader(item.name)
        print(f"Topic: {item.topic}")
        with out.governance_assessments():
            out.line(item.name, mark(item.status), f"{item.status}: {item.result}. Boundary: {item.boundary}")
    with out.governance_assessments():
        out.line("Group 41 status entries stated", StatusMark.PASS, f"{len(entries)} status entries stated")


def case_3(out: ScriptOutput, gaps: List[GapEntry]) -> None:
    header("Case 3: Final open gaps")
    for item in gaps:
        subheader(item.name)
        with out.unresolved_obligations():
            out.line(item.name, mark(item.status), f"{item.status}: {item.reason}. Discipline: {item.discipline}")
    with out.unresolved_obligations():
        out.line("Group 41 final gaps stated", StatusMark.PASS, f"{len(gaps)} gaps remain open, deferred, not declared, not adopted, not derived, or not ready")


def case_4(out: ScriptOutput, handoffs: List[HandoffEntry]) -> None:
    header("Case 4: Final handoffs")
    for item in handoffs:
        subheader(item.name)
        with out.governance_assessments():
            out.line(item.name, mark(item.status), f"{item.status}: {item.reason}. Caution: {item.caution}")
    with out.governance_assessments():
        out.line("Group 41 handoffs stated", StatusMark.DEFER, f"{len(handoffs)} handoffs stated; declaration, theorem, adoption, and downstream gates remain separate")


def case_5(out: ScriptOutput, rules: List[RuleEntry]) -> None:
    header("Case 5: Rejected summary upgrades")
    for item in rules:
        subheader(item.name)
        print(f"Upgrade: {item.upgrade}")
        with out.governance_assessments():
            out.line(item.name, StatusMark.OBLIGATION, f"POLICY_RULE: {item.reason}")
    with out.governance_assessments():
        out.line("Group 41 summary upgrades rejected", StatusMark.PASS, f"{len(rules)} upgrade shortcuts rejected as policy rules")


def case_6(out: ScriptOutput) -> None:
    header("Case 6: Group 41 conclusions")
    conclusions = [
        ("C1: Group 41 result", "SAFE_MEMBERSHIP_PRECONDITION_CONTINUATION", "Group 41 sharpened safe-membership preconditions"),
        ("C2: current membership status", "COMPATIBLE_IF_DECLARED", "zeta_Bs -> T_zeta remains diagnostic / compatible-if-declared only"),
        ("C3: object/sector status", "CONDITIONAL", "zeta_Bs object and T_zeta sector are sharper but not declared active"),
        ("C4: criteria status", "CONDITIONAL", "membership-testable means precondition clarity only"),
        ("C5: role-purity status", "POLICY_RULE", "exclusion zones are policy/precondition boundaries only"),
        ("C6: no adoption or theorem", "NOT_ADOPTED", "Group 41 adopts nothing and proves nothing"),
        ("C7: downstream gates", "NOT_READY", "B_s/F_zeta insertion, active O, residual control, recombination, and parent equation remain not ready"),
    ]
    for name, status, meaning in conclusions:
        subheader(name)
        with out.governance_assessments():
            out.line(name, mark(status), f"{status}: {meaning}")
    with out.governance_assessments():
        out.line(
            "Group 41 status summary conclusion stated",
            StatusMark.PASS,
            "safe-membership preconditions sharpened; active membership, declaration, adoption, theorem, and downstream routes remain closed",
        )


def final_interpretation() -> None:
    header("Final interpretation")
    print("Group 41 status summary result:\n")
    print("  Group 41 completed a safe-membership precondition continuation.")
    print("  zeta_Bs -> T_zeta remains diagnostic / compatible-if-declared only.")
    print("  zeta_Bs is the membership-test payload object, not F_zeta, not trace normalization, not branch choice, and not insertion.")
    print("  Branch-sensitive object claims must use zeta_Bs_metric and zeta_Bs_scale explicitly.")
    print("  T_zeta is a safe trace-sector target or diagnostic label, not active O and not a projector.")
    print("  Membership-testable means precondition clarity only, not theorem-readiness or declaration-readiness.")
    print("  Role-purity exclusion zones are mandatory policy/precondition boundaries.")
    print("  Diagnostic membership labels remain inert.")
    print("  No trace-normalization or safe-membership declaration is completed.")
    print("  Package B remains compatible-if-declared only and is not adopted or recommended for adoption.")
    print("  B_s/F_zeta insertion, active O, residual control, recombination, and parent equation remain not ready.")
    print("\nPossible next step:")
    print("  safe-membership declaration attempt, membership theorem route, role-purity theorem route,")
    print("  branch-indexed membership comparison, or diagnostic bookkeeping continuation")
    print("\nForbidden immediate next step:")
    print("  Package B adoption, B_s/F_zeta insertion, active O, residual control, or parent closure")


def record_governance(ns, statuses: List[StatusEntry], gaps: List[GapEntry], handoffs: List[HandoffEntry], rules: List[RuleEntry]) -> None:
    record_marker(ns, MARKER_ID, MARKER_ID)

    for idx, item in enumerate(statuses, 1):
        record_claim(
            ns,
            f"g41_status_c{idx}",
            MARKER_ID,
            item.status,
            f"{item.name}: {item.topic}. Result: {item.result}. Boundary: {item.boundary}.",
        )

    for idx, item in enumerate(gaps, 1):
        record_obligation(
            ns,
            f"g41_gap_{idx}",
            MARKER_ID,
            item.name,
            f"{item.reason}. Discipline: {item.discipline}.",
            item.status,
        )

    for idx, item in enumerate(handoffs, 1):
        route_status = governance_status_for(item.status)
        ns.record_route(
            RouteRecord(
                route_id=f"g41_handoff_{idx}",
                script_id=SCRIPT_ID,
                name=item.name,
                status=route_status,
                tier=ClaimTier.CONSTRAINED,
                required_obligations=[],
                activation_conditions=[item.reason, item.caution],
            )
        )

    for idx, item in enumerate(rules, 1):
        record_claim(
            ns,
            f"g41_rule_{idx}",
            MARKER_ID,
            "POLICY_RULE",
            f"Rejected upgrade: {item.upgrade}. Reason: {item.reason}.",
        )


def main() -> None:
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    statuses = build_status_entries()
    gaps = build_gaps()
    handoffs = build_handoffs()
    rules = build_rejected_upgrades()

    case_0(out)
    case_1(out)
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
