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
        "EQUATION_CHOICE_EXCLUSION_MAP": StatusMark.INFO,
        "EQUATION_SPACE_NARROWED": StatusMark.PASS,
        "CONDITIONAL_CANDIDATE": StatusMark.DEFER,
        "AXIOM_REQUIRED": StatusMark.DEFER,
        "PRECONDITION_ONLY": StatusMark.INFO,
        "COMPATIBLE_IF_DECLARED": StatusMark.INFO,
        "DIAGNOSTIC_ONLY": StatusMark.INFO,
        "BRANCH_INDEXED": StatusMark.INFO,
        "NOT_WELL_POSED": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "DEFER": StatusMark.DEFER,
        "DECLARATION_DEFERRED": StatusMark.DEFER,
        "NOT_DECLARED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NO_EQUATION_CHOSEN": StatusMark.DEFER,
        "NO_ADOPTION": StatusMark.DEFER,
        "NO_INSERTION": StatusMark.DEFER,
        "PARENT_NOT_READY": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "FORBIDDEN_BY_GUARDRAIL": StatusMark.FAIL,
        "ELIMINATED": StatusMark.FAIL,
        "DEMOTED_TO_DIAGNOSTIC": StatusMark.INFO,
        "RECOVERY_SELECTOR_REJECTED": StatusMark.FAIL,
        "REPAIR_TOOL_REJECTED": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
    }.get(status, StatusMark.INFO)


def _governance(name: str, fallback=None):
    if fallback is None:
        fallback = GovernanceStatus.POLICY_RULE
    return getattr(GovernanceStatus, name, fallback)


def governance_status_for(status: str):
    info_status = _governance("HEURISTIC")
    deferred_status = _governance("DEFERRED_PENDING_PREREQUISITES", _governance("DEFERRED"))
    candidate_status = _governance("CANDIDATE_ROUTE", info_status)
    policy_status = GovernanceStatus.POLICY_RULE
    rejected_status = _governance("REJECTED", policy_status)

    return {
        "PASS": info_status,
        "MATCHED_EXPECTATION": info_status,
        "EQUATION_CHOICE_EXCLUSION_MAP": info_status,
        "EQUATION_SPACE_NARROWED": info_status,
        "CONDITIONAL_CANDIDATE": candidate_status,
        "AXIOM_REQUIRED": deferred_status,
        "PRECONDITION_ONLY": info_status,
        "COMPATIBLE_IF_DECLARED": candidate_status,
        "DIAGNOSTIC_ONLY": info_status,
        "BRANCH_INDEXED": info_status,
        "NOT_WELL_POSED": deferred_status,
        "OPEN": deferred_status,
        "DEFER": deferred_status,
        "DECLARATION_DEFERRED": deferred_status,
        "NOT_DECLARED": deferred_status,
        "NOT_DERIVED": deferred_status,
        "NOT_READY": deferred_status,
        "NOT_ADOPTED": deferred_status,
        "NO_EQUATION_CHOSEN": deferred_status,
        "NO_ADOPTION": deferred_status,
        "NO_INSERTION": deferred_status,
        "PARENT_NOT_READY": deferred_status,
        "POLICY_RULE": policy_status,
        "FORBIDDEN_BY_GUARDRAIL": rejected_status,
        "ELIMINATED": rejected_status,
        "DEMOTED_TO_DIAGNOSTIC": info_status,
        "RECOVERY_SELECTOR_REJECTED": rejected_status,
        "REPAIR_TOOL_REJECTED": rejected_status,
        "FORBIDDEN_SHORTCUT": policy_status,
    }.get(status, info_status)


def obligation_status(status: str) -> ObligationStatus:
    if status in {
        "AXIOM_REQUIRED",
        "CONDITIONAL_CANDIDATE",
        "NOT_WELL_POSED",
        "OPEN",
        "DEFER",
        "DECLARATION_DEFERRED",
        "NOT_DECLARED",
        "NOT_DERIVED",
        "NOT_READY",
        "NOT_ADOPTED",
        "NO_EQUATION_CHOSEN",
        "NO_ADOPTION",
        "NO_INSERTION",
        "PARENT_NOT_READY",
    }:
        return getattr(ObligationStatus, "DEFERRED", ObligationStatus.OPEN)
    return ObligationStatus.OPEN

# Group:
#   42_trace_anchor_equation_choice_exclusion_map
# Script type:
#   AUDIT / EXCLUSION MAP

SCRIPT_LABEL = 'Candidate Spatial-Response Equation Family Sieve'
MARKER_ID = 'g42_spatial_response'
GROUP_SCOPE = 'Group 42 trace-anchor equation choice exclusion map'
DEPENDENCIES = [('g41_summary', '041_safe_membership_precondition_continuation__candidate_group_41_status_summary', 'g41_summary'), ('g42_trace_norm_sieve', '042_trace_anchor_equation_choice_exclusion_map__candidate_trace_normalization_equation_family_sieve', 'g42_trace_norm_sieve'), ('g42_membership_sieve', '042_trace_anchor_equation_choice_exclusion_map__candidate_safe_membership_relation_family_sieve', 'g42_membership_sieve')]
QUESTION = 'Which B_s/F_zeta scalar spatial-response equation families are eliminated before insertion can be attempted?'
DISCIPLINE = 'This script classifies scalar spatial-response and B_s/F_zeta equation families. It does not derive or insert B_s/F_zeta.'
OPENING_DETAIL = 'spatial-response equation-family sieve only; B_s/F_zeta insertion remains not ready'
CASE1_TITLE = 'Case 1: Scalar spatial-response equation-family entries'
NEXT_SCRIPT = 'candidate_residual_source_equation_elimination_audit.py'
CONCLUSIONS = [('spatial-response sieve complete', 'EQUATION_SPACE_NARROWED', 'recovery-selected, hidden-expression, mass-duplicating, scalar-tail, and undefined families separated'), ('B_s/F_zeta insertion not ready', 'NOT_READY', 'surviving response candidates require later axiom/declaration/derivation support')]


def build_entries() -> List[Entry]:
    return [
        Entry('S1: AB recovery-selected response', 'B_s/F_zeta chosen from AB=1 or B=1/A is eliminated', 'RECOVERY_SELECTOR_REJECTED', 'reduced exterior recovery cannot construct spatial response', 'recovery is audit only'),
        Entry('S2: Schwarzschild or PPN-selected response', 'response chosen from Schwarzschild recovery, weak-field success, or PPN gamma is eliminated', 'RECOVERY_SELECTOR_REJECTED', 'observational recovery cannot select the equation', 'construction must be independently licensed'),
        Entry('S3: neutral F_zeta with concrete response', 'neutral F_zeta carrying a concrete expression is eliminated', 'FORBIDDEN_BY_GUARDRAIL', 'neutral placeholder must remain expression-free', 'no hidden branch or response law'),
        Entry('S4: branch-indexed non-active response candidate', 'branch-indexed B_s/F_zeta candidate forms may be inventoried without insertion', 'CONDITIONAL_CANDIDATE', 'candidate forms may survive as future axiom/declaration objects', 'not insertable'),
        Entry('S5: insertion axiom candidate', 'a real scalar spatial-response insertion law likely requires an explicit later axiom or derivation', 'AXIOM_REQUIRED', 'axiom need may be recorded', 'axiom is not adopted here'),
        Entry('S6: mass-duplicating scalar response', 'response equation that duplicates the protected A-sector mass coin is eliminated', 'ELIMINATED', 'ordinary mass response cannot be duplicated through B_s, zeta, or kappa', 'source no-double-counting remains required'),
        Entry('S7: ordinary long-range scalar-tail response', 'ordinary scalar spatial response that creates an unlicensed exterior scalar tail is eliminated or demoted', 'ELIMINATED', 'ordinary long-range scalar gravity channel is not licensed', 'scalar silence must not be patched after recovery'),
        Entry('S8: undefined object response', 'response equation with undefined object, sector, domain, codomain, or branch status is not well-posed', 'NOT_WELL_POSED', 'objects must be typed before equation use', 'undefined response is not a candidate equation'),
    ]


def build_shortcuts() -> List[Shortcut]:
    return [
        Shortcut('X1: recovery constructs response', 'derive B_s/F_zeta from B=1/A or gamma=1', 'recovery is not construction'),
        Shortcut('X2: neutral response hides expression', 'write F_zeta as a concrete response while calling it neutral', 'neutral means expression-free'),
        Shortcut('X3: candidate form as insertion', 'insert a branch-indexed non-active candidate form', 'candidate inventory is not insertion'),
        Shortcut('X4: scalar response duplicates A mass', 'let B_s/zeta/kappa carry independent ordinary mass charge', 'A-sector mass protection remains required'),
        Shortcut('X5: scalar tail patched by filter', 'suppress far-zone scalar behavior by an after-the-fact filter', 'scalar silence must be derived, not patched'),
    ]


def build_obligations() -> List[ObligationEntry]:
    return [
        ObligationEntry('O1: preserve recovery-selector ban', 'POLICY_RULE', 'do not select scalar spatial response from recovery targets', 'avoid construction by audit'),
        ObligationEntry('O2: preserve A-sector mass protection', 'NOT_DERIVED', 'future response laws need source no-double-counting support', 'avoid mass duplication'),
        ObligationEntry('O3: keep insertion not ready', 'NOT_READY', 'do not insert B_s/F_zeta until prior gates close', 'avoid premature recombination'),
        ObligationEntry('O4: require typed objects', 'OPEN', 'object, sector, domain, codomain, and branch status must be explicit', 'avoid not-well-posed equations'),
    ]


def record_marker(ns, marker_id: str, symbol_name: str) -> None:
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[],
        output=sp.Symbol(symbol_name),
        method="inventory marker; no physical derivation",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
        scope=GROUP_SCOPE,
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


@dataclass(frozen=True)
class Entry:
    name: str
    subject: str
    status: str
    detail: str
    boundary: str


@dataclass(frozen=True)
class Shortcut:
    name: str
    shortcut: str
    reason: str


@dataclass(frozen=True)
class ObligationEntry:
    name: str
    status: str
    obligation: str
    discipline: str


def case_0(out: ScriptOutput) -> None:
    header(SCRIPT_LABEL)
    print("Question:\n")
    for line in QUESTION.splitlines():
        print("  " + line if line else "")
    print("\nDiscipline:\n")
    for line in DISCIPLINE.splitlines():
        print("  " + line if line else "")
    with out.governance_assessments():
        out.line(
            f"{SCRIPT_LABEL} opened",
            StatusMark.PASS,
            OPENING_DETAIL,
        )


def case_1(out: ScriptOutput, entries: List[Entry]) -> None:
    header(CASE1_TITLE)
    for item in entries:
        subheader(item.name)
        print(f"Subject: {item.subject}")
        print(f"Detail: {item.detail}")
        print(f"Boundary: {item.boundary}")
        with out.governance_assessments():
            out.line(item.name, mark(item.status), f"{item.status}: {item.detail}. Boundary: {item.boundary}")


def case_2(out: ScriptOutput, shortcuts: List[Shortcut]) -> None:
    header("Case 2: Invalid upgrades and forbidden shortcuts")
    for item in shortcuts:
        subheader(item.name)
        print(f"Shortcut: {item.shortcut}")
        with out.counterexamples():
            out.line(item.name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {item.reason}")


def case_3(out: ScriptOutput, obligations: List[ObligationEntry]) -> None:
    header("Case 3: Open obligations")
    for item in obligations:
        subheader(item.name)
        print(f"Obligation: {item.obligation}")
        with out.unresolved_obligations():
            out.line(item.name, mark(item.status), f"{item.status}: {item.obligation}; discipline: {item.discipline}")


def case_4(out: ScriptOutput) -> None:
    header("Case 4: Local conclusions")
    with out.governance_assessments():
        for name, status, detail in CONCLUSIONS:
            out.line(name, mark(status), detail)
    print("\nPossible next script:")
    print("  " + NEXT_SCRIPT)


def record_governance(ns, entries: List[Entry], shortcuts: List[Shortcut], obligations: List[ObligationEntry]) -> None:
    record_marker(ns, MARKER_ID, MARKER_ID)
    for idx, item in enumerate(entries, 1):
        record_claim(
            ns,
            f"{MARKER_ID}_c{idx}",
            MARKER_ID,
            item.status,
            f"{item.name}: {item.subject}. {item.detail}. Boundary: {item.boundary}.",
        )
    for idx, item in enumerate(shortcuts, 1):
        record_claim(
            ns,
            f"{MARKER_ID}_x{idx}",
            MARKER_ID,
            "FORBIDDEN_SHORTCUT",
            f"{item.name}: {item.shortcut}. Rejected because {item.reason}.",
        )
    for idx, item in enumerate(obligations, 1):
        record_obligation(
            ns,
            f"{MARKER_ID}_o{idx}",
            item.name,
            f"{item.obligation}. Discipline: {item.discipline}.",
            item.status,
        )


def main() -> None:
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    entries = build_entries()
    shortcuts = build_shortcuts()
    obligations = build_obligations()
    case_0(out)
    case_1(out, entries)
    case_2(out, shortcuts)
    case_3(out, obligations)
    case_4(out)
    record_governance(ns, entries, shortcuts, obligations)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
