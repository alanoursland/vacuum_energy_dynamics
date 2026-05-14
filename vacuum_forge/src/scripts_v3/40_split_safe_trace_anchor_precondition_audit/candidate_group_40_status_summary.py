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
#   40_split_safe_trace_anchor_precondition_audit
# Script type:
#   STATUS SUMMARY

SCRIPT_LABEL = "Candidate Group 40 Status Summary"
MARKER_ID = "g40_summary"

DEPENDENCIES = [
    ("g40_recon", "40_split_safe_trace_anchor_precondition_audit__candidate_split_safe_precondition_batch_reconciliation", "g40_recon"),
    ("g40_safety_split", "40_split_safe_trace_anchor_precondition_audit__candidate_residual_source_safety_split_audit", "g40_safety_split"),
    ("g40_membership_precond", "40_split_safe_trace_anchor_precondition_audit__candidate_safe_membership_split_safe_preconditions", "g40_membership_precond"),
    ("g40_fzeta_precond", "40_split_safe_trace_anchor_precondition_audit__candidate_neutral_Fzeta_split_safe_preconditions", "g40_fzeta_precond"),
    ("g40_branch_indexed", "40_split_safe_trace_anchor_precondition_audit__candidate_branch_indexed_precondition_ledger", "g40_branch_indexed"),
    ("g40_problem", "40_split_safe_trace_anchor_precondition_audit__candidate_split_safe_precondition_problem", "g40_problem"),
    ("g39_summary", "39_trace_anchor_branch_choice_readiness_audit__candidate_group_39_status_summary", "g39_summary"),
    ("g38_summary", "38_trace_anchor_explicit_declaration_record__candidate_group_38_status_summary", "g38_summary"),
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
        "SPLIT_SAFE_PRECONDITION_AUDIT": StatusMark.INFO,
        "BRANCH_INDEXED": StatusMark.INFO,
        "SPLIT_SAFE": StatusMark.INFO,
        "NEUTRAL_SAFE": StatusMark.INFO,
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


def obligation_status(status: str) -> ObligationStatus:
    if status in {"NOT_READY", "DECLARATION_DEFERRED", "NOT_DECLARED", "NOT_CHOSEN", "NOT_ADOPTED", "NOT_DERIVED"}:
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
        scope="Group 40 split-safe trace-anchor precondition audit summary",
    )


def record_claim(ns, claim_id: str, marker_id: str, status, statement: str) -> None:
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
            "G40-1: split-safe precondition opener",
            "Group 40 opened as a split-safe trace-anchor precondition audit",
            "SPLIT_SAFE_PRECONDITION_AUDIT",
            "precondition work continued under split notation while preserving B_s_metric and b_s_scale as parallel named branches",
            "the opener chooses no active branch and completes no declaration",
        ),
        StatusEntry(
            "G40-2: branch-indexed ledger",
            "metric and scale branch slots were carried in parallel",
            "BRANCH_INDEXED",
            "B_s_metric may carry the metric-coefficient candidate form and b_s_scale may carry the scale-factor candidate form, but only as branch-indexed candidates",
            "parallel branch indexing is not one completed declaration and not active branch selection",
        ),
        StatusEntry(
            "G40-3: neutral F_zeta preconditions",
            "neutral F_zeta deferral boundary was preserved",
            "NEUTRAL_SAFE",
            "F_zeta may remain a neutral response placeholder only while expression-free; branch-indexed variants must remain explicitly parallel and non-active",
            "neutral placeholder is not trace normalization, proof, adoption, or insertion",
        ),
        StatusEntry(
            "G40-4: safe-membership preconditions",
            "safe-membership slots were audited under split notation",
            "CONDITIONAL",
            "object, sector, domain/codomain, criterion, role-purity, diagnostic scope, and exclusion-zone slots can be inventoried as split-safe or conditional preconditions",
            "membership preconditions are not active membership, incidence, residual control, or insertion",
        ),
        StatusEntry(
            "G40-5: residual/source safety gates",
            "general no-hidden-load safety preconditions were inventoried",
            "SPLIT_SAFE",
            "source visibility, divergence explicitness, and boundary/support visibility can be stated branch-independently; residual nonentry and branch-specific metric entry remain theorem targets or branch-required work",
            "safety gates are not solved residual/source/divergence theorems",
        ),
        StatusEntry(
            "G40-6: batch reconciliation",
            "speculative batch outputs were reconciled before summary",
            "MATCHED_EXPECTATION",
            "actual outputs matched the expected split-safe precondition-audit shape: parallel branches visible, neutral F_zeta expression-free, membership and safety slots audited, no choices made",
            "reconciliation is not declaration completion or theorem proof",
        ),
        StatusEntry(
            "G40-7: active branch and declarations",
            "metric_coefficient versus scale_factor branch and Package B declarations",
            "DECLARATION_DEFERRED",
            "no active branch is chosen; no trace-normalization declaration, safe-membership declaration, or joint Package B declaration is completed",
            "Package B remains compatible-if-declared only",
        ),
        StatusEntry(
            "G40-8: downstream gates",
            "B_s/F_zeta insertion, active O, residual control, and parent closure",
            "NOT_READY",
            "all downstream gates remain closed",
            "Group 40 is not insertion, active O, residual control, or parent readiness",
        ),
    ]


def build_gaps() -> List[GapEntry]:
    return [
        GapEntry(
            "G1: active branch choice",
            "OPEN",
            "B_s_metric and b_s_scale remain parallel candidate branches, but neither is active",
            "a later explicit branch-choice record is required for a completed single-branch declaration",
        ),
        GapEntry(
            "G2: exact trace-normalization declaration",
            "DECLARATION_DEFERRED",
            "branch-indexed candidate forms are visible, but no single exact normalization is installed",
            "do not collapse log(B_s_metric)=2*zeta/d and log(b_s_scale)=zeta/d into one neutral law",
        ),
        GapEntry(
            "G3: neutral F_zeta expression boundary",
            "OPEN",
            "F_zeta remains safe only while expression-free or explicitly branch-indexed as non-active variants",
            "neutral notation cannot hide zeta/d or 2*zeta/d",
        ),
        GapEntry(
            "G4: safe-membership completion",
            "NOT_DECLARED",
            "membership slots are visible but no active membership is installed",
            "membership remains compatible-if-declared and does not imply incidence, residual control, active O, or insertion",
        ),
        GapEntry(
            "G5: residual/source/divergence theorem support",
            "NOT_DERIVED",
            "source visibility, divergence explicitness, boundary/support visibility, and residual nonentry remain preconditions or theorem targets",
            "precondition visibility is not proof",
        ),
        GapEntry(
            "G6: Package B declaration and adoption",
            "NOT_ADOPTED",
            "no branch choice means no completed joint Package B declaration; Group 40 is not adoption",
            "adoption remains a separate explicit decision",
        ),
        GapEntry(
            "G7: insertion and parent closure",
            "NOT_READY",
            "split-safe preconditions do not resolve residual, source, divergence, recombination, or parent gates",
            "B_s/F_zeta insertion and parent equation remain closed",
        ),
    ]


def build_handoffs() -> List[HandoffEntry]:
    return [
        HandoffEntry(
            "H1: explicit branch-choice record",
            "OPEN",
            "may deliberately choose metric_coefficient or scale_factor branch after split-safe preconditions are visible",
            "choice is declaration support only, not adoption, proof, or insertion",
        ),
        HandoffEntry(
            "H2: branch-indexed parallel declaration record",
            "OPEN",
            "may carry both branch-indexed candidate forms explicitly rather than choosing one",
            "parallel record must not collapse back into overloaded B_s or neutral F_zeta",
        ),
        HandoffEntry(
            "H3: neutral F_zeta deferral record",
            "NEUTRAL_SAFE",
            "may preserve F_zeta as expression-free placeholder",
            "must not attach zeta/d or 2*zeta/d while calling it neutral",
        ),
        HandoffEntry(
            "H4: safe-membership precondition continuation",
            "CONDITIONAL",
            "may continue object/sector/criterion/role-purity inventory under explicit split or branch-neutral assumptions",
            "cannot install active membership or no-overlap/incidence theorem by label",
        ),
        HandoffEntry(
            "H5: residual/source safety theorem route",
            "OPEN",
            "may attempt to turn no-hidden-load preconditions into actual residual/source/divergence theorems",
            "theorem route must not assume proof from Group 40 inventories",
        ),
        HandoffEntry(
            "H6: exact trace-normalization declaration",
            "BRANCH_REQUIRED",
            "requires active branch or two explicitly parallel branch records",
            "cannot be completed as one neutral declaration",
        ),
        HandoffEntry(
            "H7: insertion or parent route",
            "NOT_READY",
            "not available from Group 40",
            "forbidden as immediate handoff",
        ),
    ]


def build_rejected_upgrades() -> List[RuleEntry]:
    return [
        RuleEntry("R1: split preconditions as branch choice", "treat branch-indexed preconditions as choosing metric or scale branch", "preconditions are not choice records"),
        RuleEntry("R2: parallel branches as one declaration", "collapse B_s_metric and b_s_scale back into one active B_s", "that reintroduces the notation conflict"),
        RuleEntry("R3: neutral F_zeta as hidden expression", "attach zeta/d or 2*zeta/d to F_zeta while calling it neutral", "neutral deferral must remain expression-free"),
        RuleEntry("R4: membership preconditions as active membership", "treat object/sector/criterion visibility as installed Package B membership", "preconditions are not declarations or proofs"),
        RuleEntry("R5: safety gates as theorems", "say residual/source/divergence preconditions prove safety", "theorem support remains separate"),
        RuleEntry("R6: split-safe audit as adoption", "treat split-safe Package B preconditions as adopted Package B", "adoption requires a separate explicit decision"),
        RuleEntry("R7: split-safe audit as insertion", "open B_s/F_zeta insertion or parent closure from precondition visibility", "downstream gates remain closed"),
    ]


def case_0(out: ScriptOutput) -> None:
    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  What did Group 40 establish about split-safe trace-anchor preconditions")
    print("  while B_s_metric and b_s_scale remain unchosen parallel branches?")
    print("\nDiscipline:\n")
    print("  This script summarizes Group 40.")
    print("  It does not choose metric_coefficient or scale_factor.")
    print("  It does not fill trace-normalization or safe-membership declarations.")
    print("  It adopts nothing, proves nothing, and opens no downstream gate.")
    print("\nTiny goblin rule:\n  Both jars are labeled on the shelf. No jar is poured.")
    with out.governance_assessments():
        out.line(
            "Group 40 status summary opened",
            StatusMark.PASS,
            "closing split-safe precondition audit while preserving branch-deferred/no-adoption/no-insertion boundary",
        )


def case_1(out: ScriptOutput) -> None:
    header("Case 1: Group 40 symbolic summary loads")
    branch_indexed, neutral_safe, membership_slots, safety_gates = sp.symbols(
        "branch_indexed neutral_safe membership_slots safety_gates"
    )
    branch_defer, declaration_defer, theorem_boundary, adoption_boundary = sp.symbols(
        "branch_defer declaration_defer theorem_boundary adoption_boundary"
    )
    P_insertion, P_active_O, P_residual_kill, P_parent = sp.symbols(
        "P_insertion P_active_O P_residual_kill P_parent"
    )
    L_preconditions = sp.simplify(branch_indexed + neutral_safe + membership_slots + safety_gates)
    L_boundaries = sp.simplify(branch_defer + declaration_defer + theorem_boundary + adoption_boundary)
    L_downstream_closed = sp.simplify(P_insertion + P_active_O + P_residual_kill + P_parent)
    L_group40_summary = sp.simplify(L_preconditions + L_boundaries + L_downstream_closed)
    print(f"Precondition load: L_preconditions = {L_preconditions}")
    print(f"Boundary/deferred load: L_boundaries = {L_boundaries}")
    print(f"Downstream closed load: L_downstream_closed = {L_downstream_closed}")
    print(f"Group 40 summary load: L_group40_summary = {L_group40_summary}")
    with out.derived_results():
        out.line(
            "Group 40 symbolic summary loads stated",
            StatusMark.PASS,
            f"L_preconditions={L_preconditions}; L_downstream_closed={L_downstream_closed}",
        )


def case_2(out: ScriptOutput, entries: List[StatusEntry]) -> None:
    header("Case 2: Group 40 status entries")
    for item in entries:
        subheader(item.name)
        print(f"Topic: {item.topic}")
        with out.governance_assessments():
            out.line(item.name, mark(item.status), f"{item.status}: {item.result}. Boundary: {item.boundary}")
    with out.governance_assessments():
        out.line("Group 40 status entries stated", StatusMark.PASS, f"{len(entries)} status entries stated")


def case_3(out: ScriptOutput, gaps: List[GapEntry]) -> None:
    header("Case 3: Final open gaps")
    for item in gaps:
        subheader(item.name)
        with out.unresolved_obligations():
            out.line(item.name, mark(item.status), f"{item.status}: {item.reason}. Discipline: {item.discipline}")
    with out.unresolved_obligations():
        out.line("Group 40 final gaps stated", StatusMark.PASS, f"{len(gaps)} gaps remain open, deferred, or not ready")


def case_4(out: ScriptOutput, handoffs: List[HandoffEntry]) -> None:
    header("Case 4: Final handoffs")
    for item in handoffs:
        subheader(item.name)
        with out.governance_assessments():
            out.line(item.name, mark(item.status), f"{item.status}: {item.reason}. Caution: {item.caution}")
    with out.governance_assessments():
        out.line("Group 40 handoffs stated", StatusMark.DEFER, f"{len(handoffs)} handoffs stated; choices/downstream gates remain separate")


def case_5(out: ScriptOutput, rules: List[RuleEntry]) -> None:
    header("Case 5: Rejected summary upgrades")
    for item in rules:
        subheader(item.name)
        print(f"Upgrade: {item.upgrade}")
        with out.governance_assessments():
            out.line(item.name, StatusMark.OBLIGATION, f"POLICY_RULE: {item.reason}")
    with out.governance_assessments():
        out.line("Group 40 summary upgrades rejected", StatusMark.PASS, f"{len(rules)} upgrade shortcuts rejected as policy rules")


def case_6(out: ScriptOutput) -> None:
    header("Case 6: Group 40 conclusions")
    conclusions = [
        ("C1: Group 40 result", "SPLIT_SAFE_PRECONDITION_AUDIT", "Group 40 completed a split-safe trace-anchor precondition audit"),
        ("C2: branch-indexed branches", "BRANCH_INDEXED", "B_s_metric and b_s_scale remain distinct visible candidate branches"),
        ("C3: neutral F_zeta", "NEUTRAL_SAFE", "F_zeta may remain neutral only while expression-free"),
        ("C4: membership status", "DECLARATION_DEFERRED", "safe-membership slots are visible but active membership is not installed"),
        ("C5: safety gates", "CONDITIONAL", "residual/source/divergence gates are visible as preconditions or theorem targets, not solved theorems"),
        ("C6: no adoption or theorem", "NOT_ADOPTED", "Group 40 adopts nothing and derives nothing"),
        ("C7: downstream gates", "NOT_READY", "B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready"),
    ]
    for name, status, meaning in conclusions:
        subheader(name)
        with out.governance_assessments():
            out.line(name, mark(status), f"{status}: {meaning}")
    with out.governance_assessments():
        out.line(
            "Group 40 status summary conclusion stated",
            StatusMark.PASS,
            "split-safe precondition audit closed; no active branch, no declaration completion, no adoption, downstream gates closed",
        )


def final_interpretation() -> None:
    header("Final interpretation")
    print("Group 40 status summary result:\n")
    print("  Group 40 completed a split-safe trace-anchor precondition audit.")
    print("  B_s_metric and b_s_scale remain distinct branch-indexed candidate objects.")
    print("  No active metric_coefficient or scale_factor branch is chosen.")
    print("  Neutral F_zeta remains safe only while expression-free.")
    print("  Branch-indexed candidate forms may be carried in parallel, but not collapsed into one law.")
    print("  Safe-membership object, sector, criterion, role-purity, and exclusion-zone slots are visible as preconditions.")
    print("  Residual/source/divergence/boundary safety gates are visible as preconditions or theorem targets.")
    print("  No trace-normalization or safe-membership declaration is completed.")
    print("  Package B remains compatible-if-declared only.")
    print("  Package B is not adopted or recommended for adoption.")
    print("  B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready.")
    print("\nPossible next step:")
    print("  explicit branch-choice record, branch-indexed parallel declaration record,")
    print("  neutral F_zeta deferral record, safe-membership precondition continuation,")
    print("  or residual/source safety theorem route")
    print("\nTiny goblin label:")
    print("  Both jars are labeled on the shelf. No jar is poured.")


def record_governance(ns, statuses: List[StatusEntry], gaps: List[GapEntry], handoffs: List[HandoffEntry], rules: List[RuleEntry]) -> None:
    record_marker(ns, MARKER_ID, MARKER_ID)
    for idx, item in enumerate(statuses, 1):
        record_claim(
            ns,
            f"g40_status_c{idx}",
            MARKER_ID,
            GovernanceStatus.POLICY_RULE,
            f"{item.name}: {item.topic}. Result: {item.result}. Boundary: {item.boundary}.",
        )
    for idx, item in enumerate(gaps, 1):
        record_obligation(
            ns,
            f"g40_gap_{idx}",
            MARKER_ID,
            item.name,
            f"{item.reason}. Discipline: {item.discipline}.",
            item.status,
        )
    for idx, item in enumerate(handoffs, 1):
        record_claim(
            ns,
            f"g40_handoff_{idx}",
            MARKER_ID,
            GovernanceStatus.POLICY_RULE,
            f"{item.name}: {item.reason}. Caution: {item.caution}.",
        )
    for idx, item in enumerate(rules, 1):
        record_claim(
            ns,
            f"g40_rule_{idx}",
            MARKER_ID,
            GovernanceStatus.POLICY_RULE,
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
