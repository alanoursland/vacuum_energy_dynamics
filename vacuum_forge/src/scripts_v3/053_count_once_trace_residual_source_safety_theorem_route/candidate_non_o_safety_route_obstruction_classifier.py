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
#   53_count_once_trace_residual_source_safety_theorem_route
#
# Script type:
#   GOVERNANCE / DIAGNOSTIC / CONDITIONAL THEOREM-SURFACE

SCRIPT_LABEL = 'Candidate Non-O Safety Route Obstruction Classifier'
MARKER_ID = 'g53_non_o_obstruction'
DEPENDENCIES = [('g52_summary', '052_residual_source_boundary_safety_load_testing__candidate_group_52_status_summary', 'g52_summary'), ('g53_problem', '053_count_once_trace_residual_source_safety_theorem_route__candidate_residual_source_safety_theorem_problem', 'g53_problem'), ('g53_count_once_condition', '053_count_once_trace_residual_source_safety_theorem_route__candidate_count_once_trace_condition_formalization', 'g53_count_once_condition'), ('g53_residual_non_o', '053_count_once_trace_residual_source_safety_theorem_route__candidate_residual_nonentry_non_o_route_audit', 'g53_residual_non_o'), ('g53_source_role_purity', '053_count_once_trace_residual_source_safety_theorem_route__candidate_source_routing_role_purity_matrix', 'g53_source_role_purity'), ('g53_mass_neutrality', '053_count_once_trace_residual_source_safety_theorem_route__candidate_a_sector_mass_neutrality_condition_audit', 'g53_mass_neutrality')]
QUESTION = 'Can the required incidence-zero and source-purity conditions be carried as theorem targets without active O, or do they require a projector-like mechanism?'
DISCIPLINE = 'This script classifies non-O route viability. It does not construct active O and does not prove the safety theorems.'
OPENING_LINE = 'Non-O safety route obstruction classifier opened -- no active O construction'
SCOPE = 'Group 53 non-O safety route obstruction classifier'
NEXT_SCRIPT = 'candidate_residual_source_safety_route_classifier.py'

ENTRIES = [('N1: count-once condition', 'i_Bs+i_res=1 survives as formal incidence condition', 'COUNT_ONCE_TRACE_CONDITION_FORMALIZED', 'condition is not dynamics', 'not theorem closure'), ('N2: residual nonentry route', 'residual metric/source incidence zero can be stated as theorem target', 'RESIDUAL_NONENTRY_ROUTE_DEFINED', 'zero incidence requires proof', 'not by declaration'), ('N3: source role-purity route', 'A-sector-only ordinary source routing can be stated as theorem target', 'SOURCE_NO_DOUBLE_COUNTING_ROUTE_DEFINED', 'role-purity requires proof', 'not closed'), ('N4: mass neutrality route', 'Q_trace neutrality can be stated as theorem target', 'A_SECTOR_MASS_PROTECTION_ROUTE_DEFINED', 'zero/inert trace charge requires proof', 'not closed'), ('N5: non-O route status', 'non-O route survives conditionally as theorem target', 'NON_O_ROUTE_SURVIVES_CONDITIONALLY', 'no actual obstruction forces active O yet', 'not physical use'), ('N6: active O necessity', 'active O necessity is not established by Group 53 conditions alone', 'ACTIVE_O_NECESSITY_NOT_ESTABLISHED', 'O audit may be later if theorem routes fail', 'not constructed')]
SHORTCUTS = [('X1: conditional route as proof', 'treat conditional survival of non-O route as theorem closure', 'the conditions remain open'), ('X2: active O by anxiety', 'jump to active O because conditions are hard', 'difficulty is not obstruction'), ('X3: no-O as insertion', 'insert B_s/F_zeta because non-O route was stated', 'physical use remains blocked'), ('X4: zero conditions as assumptions', 'silently assume all zero-incidence and neutrality conditions', 'conditions need proof or explicit postulate status')]
OBLIGATIONS = [('O1: prove non-O conditions', 'SAFETY_THEOREMS_REQUIRED', 'derive residual nonentry, source role-purity, and trace mass neutrality', 'convert theorem targets into support'), ('O2: active O necessity audit deferred', 'ACTIVE_O_NECESSITY_NOT_ESTABLISHED', 'consider O necessity only after non-O theorem route fails or is obstructed', 'avoid repair-by-name'), ('O3: insertion remains closed', 'NOT_INSERTABLE', 'do not use conditional non-O route as B_s/F_zeta insertion license', 'avoid field-equation drift')]
LOCAL_CONCLUSIONS = [('non-O route conditionally survives', 'NON_O_ROUTE_SURVIVES_CONDITIONALLY', 'conditions can be stated without active O, but are unproved'), ('active O not yet necessary', 'ACTIVE_O_NECESSITY_NOT_ESTABLISHED', 'no projector-like mechanism is forced by this classifier')]


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
        "COUNT_ONCE_TRACE_THEOREM_SURFACE_OPENED": StatusMark.INFO,
        "COUNT_ONCE_TRACE_CONDITION_FORMALIZED": StatusMark.INFO,
        "TRACE_DOUBLE_ENTRY_REJECTED": StatusMark.FAIL,
        "TRACE_MISSING_ENTRY_REJECTED": StatusMark.FAIL,
        "RESIDUAL_NONENTRY_ROUTE_DEFINED": StatusMark.INFO,
        "RESIDUAL_NONENTRY_THEOREM_REQUIRED": StatusMark.OBLIGATION,
        "RESIDUAL_ZERO_INCIDENCE_CONDITION": StatusMark.INFO,
        "SOURCE_NO_DOUBLE_COUNTING_ROUTE_DEFINED": StatusMark.INFO,
        "SOURCE_ROLE_PURITY_CONDITION": StatusMark.INFO,
        "SOURCE_NO_DOUBLE_COUNTING_REQUIRED": StatusMark.OBLIGATION,
        "A_SECTOR_MASS_PROTECTION_ROUTE_DEFINED": StatusMark.INFO,
        "TRACE_MASS_NEUTRALITY_CONDITION": StatusMark.INFO,
        "A_SECTOR_MASS_PROTECTION_REQUIRED": StatusMark.OBLIGATION,
        "NON_O_ROUTE_SURVIVES_CONDITIONALLY": StatusMark.INFO,
        "NON_O_ROUTE_OBSTRUCTED": StatusMark.FAIL,
        "ACTIVE_O_NECESSITY_NOT_ESTABLISHED": StatusMark.DEFER,
        "ACTIVE_O_NECESSITY_CONDITIONED": StatusMark.DEFER,
        "THEOREM_TARGET_REFINED": StatusMark.DEFER,
        "CANDIDATE_SURVIVES_AS_AUDIT_ONLY": StatusMark.INFO,
        "CANDIDATE_BLOCKED_FOR_PHYSICAL_USE": StatusMark.DEFER,
        "DEFERRED_WITH_TARGET": StatusMark.DEFER,
        "NOT_INSERTABLE": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "CHOICE_REQUIRED": StatusMark.DEFER,
        "SAFETY_THEOREMS_REQUIRED": StatusMark.OBLIGATION,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REJECTED_ROUTE": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
        "OBSTRUCTION_WITNESS_FOUND": StatusMark.FAIL,
        "OPEN": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def governance_status(status: str) -> GovernanceStatus:
    if status in {
        "TRACE_DOUBLE_ENTRY_REJECTED",
        "TRACE_MISSING_ENTRY_REJECTED",
        "NON_O_ROUTE_OBSTRUCTED",
        "REJECTED_ROUTE",
        "FORBIDDEN_SHORTCUT",
        "OBSTRUCTION_WITNESS_FOUND",
    }:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {
        "RESIDUAL_NONENTRY_THEOREM_REQUIRED",
        "SOURCE_NO_DOUBLE_COUNTING_REQUIRED",
        "A_SECTOR_MASS_PROTECTION_REQUIRED",
        "SAFETY_THEOREMS_REQUIRED",
        "POLICY_RULE",
    }:
        return GovernanceStatus.POLICY_RULE
    return GovernanceStatus.UNVERIFIED


def obligation_status(status: str) -> ObligationStatus:
    if status in {
        "CANDIDATE_BLOCKED_FOR_PHYSICAL_USE",
        "DEFERRED_WITH_TARGET",
        "NOT_INSERTABLE",
        "NOT_ADOPTED",
        "CHOICE_REQUIRED",
        "ACTIVE_O_NECESSITY_NOT_ESTABLISHED",
        "ACTIVE_O_NECESSITY_CONDITIONED",
        "THEOREM_TARGET_REFINED",
    }:
        return ObligationStatus.DEFERRED
    return ObligationStatus.OPEN


def is_zero(expr) -> bool:
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


def record_marker(ns, marker_id: str, scope: str) -> None:
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[],
        output=sp.Symbol(marker_id),
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


def record_obligation(ns, obligation_id: str, title: str, statement: str, status: str = "OPEN") -> None:
    ns.record_obligation(
        ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=obligation_status(status),
            required_by=[SCRIPT_ID],
            description=statement,
        )
    )


def record_governance(ns, marker_id: str, entries: List[Entry], obligations: List[ObligationEntry], scope: str) -> None:
    record_marker(ns, marker_id, scope)
    for idx, item in enumerate(entries, 1):
        record_claim(
            ns,
            f"{marker_id}_c{idx}",
            marker_id,
            item.status,
            f"{item.name}: {item.subject}. {item.detail}. Boundary: {item.boundary}.",
        )
    for idx, item in enumerate(obligations, 1):
        record_obligation(
            ns,
            f"{marker_id}_o{idx}",
            item.name,
            f"{item.obligation}. Discipline: {item.discipline}.",
            item.status,
        )


def print_entries(out: ScriptOutput, entries: List[Entry], title: str) -> None:
    header(title)
    for item in entries:
        subheader(item.name)
        print(f"Subject: {item.subject}")
        print(f"Detail: {item.detail}")
        print(f"Boundary: {item.boundary}")
        with out.governance_assessments():
            out.line(item.name, mark(item.status), f"{item.status}: {item.detail}. Boundary: {item.boundary}")


def print_shortcuts(out: ScriptOutput, shortcuts: List[Shortcut]) -> None:
    header("Rejected shortcuts and invalid upgrades")
    for item in shortcuts:
        subheader(item.name)
        print(f"Shortcut: {item.shortcut}")
        with out.counterexamples():
            out.line(item.name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {item.reason}")


def print_obligations(out: ScriptOutput, obligations: List[ObligationEntry]) -> None:
    header("Open obligations and deferred burdens")
    for item in obligations:
        subheader(item.name)
        print(f"Obligation: {item.obligation}")
        with out.unresolved_obligations():
            out.line(item.name, mark(item.status), f"{item.status}: {item.obligation}; discipline: {item.discipline}")


def build_entries() -> List[Entry]:
    return [Entry(*item) for item in ENTRIES]


def build_shortcuts() -> List[Shortcut]:
    return [Shortcut(*item) for item in SHORTCUTS]


def build_obligations() -> List[ObligationEntry]:
    return [ObligationEntry(*item) for item in OBLIGATIONS]





def main() -> None:
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    entries = build_entries()
    shortcuts = build_shortcuts()
    obligations = build_obligations()

    header(SCRIPT_LABEL)
    print("Question:\n")
    print(QUESTION)
    print("\nDiscipline:\n")
    print(DISCIPLINE)
    with out.governance_assessments():
        out.line(f"{SCRIPT_LABEL} opened", StatusMark.PASS, OPENING_LINE)


    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
