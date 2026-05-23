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

SCRIPT_LABEL = 'Candidate Residual Nonentry Non-O Route Audit'
MARKER_ID = 'g53_residual_non_o'
DEPENDENCIES = [('g52_summary', '052_residual_source_boundary_safety_load_testing__candidate_group_52_status_summary', 'g52_summary'), ('g53_problem', '053_count_once_trace_residual_source_safety_theorem_route__candidate_residual_source_safety_theorem_problem', 'g53_problem'), ('g53_count_once_condition', '053_count_once_trace_residual_source_safety_theorem_route__candidate_count_once_trace_condition_formalization', 'g53_count_once_condition')]
QUESTION = 'Can residual zeta/kappa nonentry be defined as a role-purity theorem target without constructing active O?'
DISCIPLINE = 'This script tests the non-O residual nonentry route as a role-purity condition. It does not construct O and does not prove residual nonentry.'
OPENING_LINE = 'Residual non-O route audit opened -- role-purity condition only'
SCOPE = 'Group 53 residual nonentry non-O route audit'
NEXT_SCRIPT = 'candidate_source_routing_role_purity_matrix.py'

ENTRIES = [('R1: non-O route defined', 'residual nonentry can be stated as zero metric/source incidence condition', 'RESIDUAL_NONENTRY_ROUTE_DEFINED', 'the route is a theorem target rather than active O construction', 'not proof'), ('R2: clean role-purity condition', 'i_res_metric=0 and i_res_source=0 removes residual reentry load', 'RESIDUAL_ZERO_INCIDENCE_CONDITION', 'zero incidence must be proven or carried as a condition', 'not by declaration'), ('R3: metric reentry witness', 'i_res_metric=1 produces trace reentry load', 'OBSTRUCTION_WITNESS_FOUND', 'metric reentry obstructs physical use', 'not allowed'), ('R4: source reentry witness', 'i_res_source=1 produces source reentry load', 'OBSTRUCTION_WITNESS_FOUND', 'source reentry obstructs physical use', 'not allowed'), ('R5: active O status', 'active O necessity is not established by defining a non-O theorem target', 'ACTIVE_O_NECESSITY_NOT_ESTABLISHED', 'O remains deferred unless non-O route is obstructed', 'not constructed')]
SHORTCUTS = [('X1: zero incidence by fiat', 'set residual metric/source incidence to zero without theorem support', 'that is an unsupported assumption'), ('X2: O by role label', 'call role-purity an active projector', 'no domain/kernel/image/operator was constructed'), ('X3: residual survival as insertion', 'use non-O route definition to insert B_s/F_zeta', 'the theorem target is not a license')]
OBLIGATIONS = [('O1: residual nonentry theorem', 'RESIDUAL_NONENTRY_THEOREM_REQUIRED', 'prove residual metric/source incidence vanishes under the retained candidate', 'avoid residual reentry'), ('O2: active O necessity deferred', 'ACTIVE_O_NECESSITY_NOT_ESTABLISHED', 'do not construct O unless non-O route fails by actual obstruction', 'avoid repair-by-name')]
LOCAL_CONCLUSIONS = [('non-O residual route defined', 'PASS', 'residual nonentry can be stated as role-purity theorem target'), ('residual theorem still open', 'RESIDUAL_NONENTRY_THEOREM_REQUIRED', 'zero incidence condition is not derived')]


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



def case_residual_non_o_conditions(out: ScriptOutput):
    header("Case 0: Non-O residual nonentry condition audit")

    T_zeta, S_M = sp.symbols("T_zeta S_M")
    i_res_metric, i_res_source = sp.symbols("i_res_metric i_res_source")
    residual_reentry_load = sp.simplify(i_res_metric * T_zeta + i_res_source * S_M)

    clean_role_purity = sp.simplify(residual_reentry_load.subs({i_res_metric: 0, i_res_source: 0}))
    metric_reentry = sp.simplify(residual_reentry_load.subs({i_res_metric: 1, i_res_source: 0}))
    source_reentry = sp.simplify(residual_reentry_load.subs({i_res_metric: 0, i_res_source: 1}))
    both_reentry = sp.simplify(residual_reentry_load.subs({i_res_metric: 1, i_res_source: 1}))

    print(f"residual_reentry_load = {residual_reentry_load}")
    print(f"clean role-purity condition (0,0): {clean_role_purity}")
    print(f"metric reentry witness (1,0): {metric_reentry}")
    print(f"source reentry witness (0,1): {source_reentry}")
    print(f"metric+source reentry witness (1,1): {both_reentry}")

    with out.derived_results():
        out.line("residual reentry load", StatusMark.PASS, f"load = {residual_reentry_load}")
        out.line("clean role-purity condition", StatusMark.PASS if is_zero(clean_role_purity) else StatusMark.FAIL, f"load = {clean_role_purity}")
        out.line("metric reentry witness", StatusMark.FAIL if not is_zero(metric_reentry) else StatusMark.PASS, f"load = {metric_reentry}")
        out.line("source reentry witness", StatusMark.FAIL if not is_zero(source_reentry) else StatusMark.PASS, f"load = {source_reentry}")
        out.line("combined reentry witness", StatusMark.FAIL if not is_zero(both_reentry) else StatusMark.PASS, f"load = {both_reentry}")

    return {
        "T_zeta": T_zeta,
        "S_M": S_M,
        "i_res_metric": i_res_metric,
        "i_res_source": i_res_source,
        "residual_reentry_load": residual_reentry_load,
        "metric_reentry": metric_reentry,
        "source_reentry": source_reentry,
        "both_reentry": both_reentry,
    }


def record_residual_non_o(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g53_residual_non_o_reentry_load",
        inputs=[data["i_res_metric"], data["i_res_source"], data["T_zeta"], data["S_M"]],
        output=data["residual_reentry_load"],
        method="residual metric/source incidence load",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="residual_non_o_condition",
        scope="diagnostic non-O residual nonentry condition; not theorem closure",
    )



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

    data = case_residual_non_o_conditions(out)

    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)
    record_residual_non_o(ns, data)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
