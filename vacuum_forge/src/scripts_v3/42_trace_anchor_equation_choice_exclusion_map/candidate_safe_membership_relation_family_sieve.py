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

SCRIPT_LABEL = 'Candidate Safe-Membership Relation Family Sieve'
MARKER_ID = 'g42_membership_sieve'
GROUP_SCOPE = 'Group 42 trace-anchor equation choice exclusion map'
DEPENDENCIES = [('g41_summary', '41_safe_membership_precondition_continuation__candidate_group_41_status_summary', 'g41_summary'), ('g41_zeta_object', '41_safe_membership_precondition_continuation__candidate_zeta_Bs_object_precondition_ledger', 'g41_zeta_object'), ('g41_tzeta_sector', '41_safe_membership_precondition_continuation__candidate_Tzeta_sector_precondition_ledger', 'g41_tzeta_sector'), ('g41_criterion_matrix', '41_safe_membership_precondition_continuation__candidate_membership_criterion_precondition_matrix', 'g41_criterion_matrix'), ('g42_trace_norm_sieve', '42_trace_anchor_equation_choice_exclusion_map__candidate_trace_normalization_equation_family_sieve', 'g42_trace_norm_sieve')]
QUESTION = 'Which zeta_Bs -> T_zeta relation families remain diagnostic or future-route candidates, and which shortcuts are eliminated?'
DISCIPLINE = 'This script classifies safe-membership relation families. It preserves zeta_Bs -> T_zeta as diagnostic / compatible-if-declared only and installs no active membership.'
OPENING_DETAIL = 'safe-membership relation sieve only; no membership declaration, proof, incidence, active O, or insertion'
CASE1_TITLE = 'Case 1: Safe-membership relation-family entries'
NEXT_SCRIPT = 'candidate_spatial_response_equation_family_sieve.py'
CONCLUSIONS = [('safe-membership relation sieve complete', 'EQUATION_SPACE_NARROWED', 'diagnostic, compatible-if-declared, future-route, and forbidden shortcut classes separated'), ('active membership not installed', 'NOT_READY', 'membership remains diagnostic / compatible-if-declared only')]


def build_entries() -> List[Entry]:
    return [
        Entry('M1: diagnostic compatibility relation', 'zeta_Bs -> T_zeta may remain a diagnostic compatibility label', 'DIAGNOSTIC_ONLY', 'labels object/sector compatibility only', 'no source, metric, divergence, projector, theorem, adoption, insertion, or parent effect'),
        Entry('M2: compatible-if-declared relation', 'zeta_Bs -> T_zeta may remain compatible-if-declared', 'COMPATIBLE_IF_DECLARED', 'future declaration support may be investigated later', 'not declaration-ready or theorem-ready'),
        Entry('M3: branch-indexed membership candidates', 'zeta_Bs_metric -> T_zeta_metric and zeta_Bs_scale -> T_zeta_scale may be carried in parallel', 'BRANCH_INDEXED', 'branch-sensitive cases stay explicit', 'parallel candidates are not active membership'),
        Entry('M4: future declaration candidate', 'a later membership declaration route may exist if object, sector, domain/codomain, criteria, role-purity, branch-status, and exclusions close', 'CONDITIONAL_CANDIDATE', 'future route made visible', 'not current declaration'),
        Entry('M5: future theorem target', 'a membership theorem would require actual derivation beyond relation naming', 'NOT_DERIVED', 'theorem burden remains explicit', 'not proved here'),
        Entry('M6: membership as incidence', 'membership used as trace/residual zero-incidence is eliminated', 'ELIMINATED', 'incidence is a separate theorem target', 'membership cannot prove incidence'),
        Entry('M7: membership as active O', 'membership used as active O or projector is eliminated', 'FORBIDDEN_BY_GUARDRAIL', 'T_zeta is not O', 'no active projector by membership label'),
        Entry('M8: membership as insertion support', 'membership used to insert B_s/F_zeta is eliminated', 'ELIMINATED', 'insertion remains downstream', 'compatible-if-declared is not insertable'),
    ]


def build_shortcuts() -> List[Shortcut]:
    return [
        Shortcut('X1: compatibility as declaration', 'treat compatible-if-declared as declared membership', 'declaration route remains future'),
        Shortcut('X2: relation as theorem', 'treat zeta_Bs -> T_zeta syntax as proof', 'relation syntax is not derivation'),
        Shortcut('X3: membership as residual control', 'use membership to prove residual nonentry or residual kill', 'residual control remains separate'),
        Shortcut('X4: membership as active projector', 'let T_zeta become O', 'sector target is not a projector'),
        Shortcut('X5: membership as insertion', 'insert B_s/F_zeta from membership status', 'insertion remains not ready'),
    ]


def build_obligations() -> List[ObligationEntry]:
    return [
        ObligationEntry('O1: keep diagnostic relation inert', 'DIAGNOSTIC_ONLY', 'diagnostic compatibility labels must remain inert', 'avoid active drift'),
        ObligationEntry('O2: keep future declarations future', 'NOT_DECLARED', 'safe-membership declaration requires separate later record', 'avoid declaration by relation family sieve'),
        ObligationEntry('O3: preserve incidence boundary', 'POLICY_RULE', 'do not let membership imply incidence, no-overlap, or residual control', 'avoid theorem shortcut'),
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
