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

SCRIPT_LABEL = 'Candidate Escape-Hatch Requirements'
MARKER_ID = 'g63_escape'
DEPENDENCIES = [('g62_summary', '62_stress_energy_accounting__candidate_group_62_status_summary', 'g62_summary'), ('g63_problem', '63_obstruction_decision__candidate_obstruction_problem', 'g63_problem'), ('g63_contract', '63_obstruction_decision__candidate_retention_contract', 'g63_contract')]
QUESTION = 'Which future routes could legitimately escape the obstruction, and which are just shortcuts?'
DISCIPLINE = 'This script separates real future theorem routes from rejected shortcut escapes.'
OPENING_LINE = 'Escape-hatch requirement matrix opened'
SCOPE = 'Group 63 escape hatch requirements'
NEXT_SCRIPT = 'candidate_obstruction_route_classifier.py'

ENTRIES = [('E1: variational/stress origin', 'derive u and p_free', 'ESCAPE_REQUIREMENTS_DERIVED', 'valid future route if actually derived', 'open'), ('E2: compensation/inertness', 'derive mass/trace inertness', 'ESCAPE_REQUIREMENTS_DERIVED', 'valid future route if not repair', 'open'), ('E3: covariant layer lift', 'lift reduced diagnostics', 'ESCAPE_REQUIREMENTS_DERIVED', 'valid future route but not closure by itself', 'open'), ('E4: shortcut closures', 'choose u=±P or P=0 by fiat', 'ESCAPE_HATCH_REJECTED', 'not valid escape', 'rejected'), ('E5: zero/O disguise', 'p_free=0 or hide in O', 'ESCAPE_HATCH_REJECTED', 'not valid escape', 'rejected')]
SHORTCUTS = [('X1: u=P escape', 'trace closure only', 'active burden remains'), ('X2: u=-P escape', 'active closure only', 'trace burden remains'), ('X3: P=0 escape', 'declare pressure sum zero', 'reduced witness nonzero'), ('X4: O escape', 'hide transition load in active O', 'not constructed')]
OBLIGATIONS = [('O1: route choice', 'DEFERRED_WITH_TARGET', 'choose between diagnostic downgrade, variational stress origin, covariant lift, or obstruction decision', 'avoid looping')]
LOCAL_CONCLUSIONS = [('escape requirements derived', 'PASS', 'valid future routes must derive something real'), ('shortcut escapes rejected', 'ESCAPE_HATCH_REJECTED', 'choosing u/P/p_free/O by convenience fails')]


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
        "OBSTRUCTION_DECISION_OPENED": StatusMark.INFO,
        "OBSTRUCTION_INPUTS_RESTATED": StatusMark.PASS,
        "DECISION_SURFACE_DERIVED": StatusMark.PASS,
        "INSERTION_REJECTED": StatusMark.FAIL,
        "UNQUALIFIED_RETENTION_REJECTED": StatusMark.FAIL,
        "DIAGNOSTIC_DOWNGRADE_ALLOWED": StatusMark.INFO,
        "CONDITIONAL_AUDIT_RETENTION_ALLOWED": StatusMark.INFO,
        "RETENTION_CONTRACT_REQUIRED": StatusMark.OBLIGATION,
        "ESCAPE_REQUIREMENTS_DERIVED": StatusMark.PASS,
        "ESCAPE_HATCH_REJECTED": StatusMark.FAIL,
        "ZERO_RESPONSE_REJECTED_AS_TRIVIAL": StatusMark.FAIL,
        "REPAIR_ROUTE_REJECTED": StatusMark.FAIL,
        "AMPLITUDE_UNDERIVED": StatusMark.OBLIGATION,
        "STRESS_ACCOUNTING_NOT_CLOSED": StatusMark.OBLIGATION,
        "AUDIT_CANDIDATE_RETAINED": StatusMark.INFO,
        "DIAGNOSTIC_ONLY_DOWNGRADE_POSSIBLE": StatusMark.DEFER,
        "DIAGNOSTIC_ONLY_STATUS_DEFINED": StatusMark.PASS,
        "COVARIANT_LIFT_REQUIRED": StatusMark.OBLIGATION,
        "ENERGY_ACCOUNTING_REQUIRED": StatusMark.OBLIGATION,
        "SOURCE_SAFETY_REQUIRED": StatusMark.OBLIGATION,
        "DIVERGENCE_IDENTITY_REQUIRED": StatusMark.OBLIGATION,
        "SAFETY_THEOREMS_REQUIRED": StatusMark.OBLIGATION,
        "PHYSICAL_USE_BLOCKED": StatusMark.DEFER,
        "NOT_INSERTABLE": StatusMark.DEFER,
        "ACTIVE_O_NECESSITY_NOT_ESTABLISHED": StatusMark.DEFER,
        "DEFERRED_WITH_TARGET": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REJECTED_ROUTE": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
    }.get(status, StatusMark.INFO)


def governance_status(status: str) -> GovernanceStatus:
    if status in {
        "INSERTION_REJECTED",
        "UNQUALIFIED_RETENTION_REJECTED",
        "ESCAPE_HATCH_REJECTED",
        "ZERO_RESPONSE_REJECTED_AS_TRIVIAL",
        "REPAIR_ROUTE_REJECTED",
        "REJECTED_ROUTE",
        "FORBIDDEN_SHORTCUT",
    }:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {
        "RETENTION_CONTRACT_REQUIRED",
        "AMPLITUDE_UNDERIVED",
        "STRESS_ACCOUNTING_NOT_CLOSED",
        "COVARIANT_LIFT_REQUIRED",
        "ENERGY_ACCOUNTING_REQUIRED",
        "SOURCE_SAFETY_REQUIRED",
        "DIVERGENCE_IDENTITY_REQUIRED",
        "SAFETY_THEOREMS_REQUIRED",
        "POLICY_RULE",
    }:
        return GovernanceStatus.POLICY_RULE
    return GovernanceStatus.UNVERIFIED


def obligation_status(status: str) -> ObligationStatus:
    if status in {
        "PHYSICAL_USE_BLOCKED",
        "NOT_INSERTABLE",
        "DEFERRED_WITH_TARGET",
        "ACTIVE_O_NECESSITY_NOT_ESTABLISHED",
        "DIAGNOSTIC_ONLY_DOWNGRADE_POSSIBLE",
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
        record_claim(ns, f"{marker_id}_c{idx}", marker_id, item.status, f"{item.name}: {item.subject}. {item.detail}. Boundary: {item.boundary}.")
    for idx, item in enumerate(obligations, 1):
        record_obligation(ns, f"{marker_id}_o{idx}", item.name, f"{item.obligation}. Discipline: {item.discipline}.", item.status)


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


def layer_symbols():
    y, R, ell, p0 = sp.symbols("y R ell p0", positive=True)
    c = sp.simplify(2*R*ell/(7*R**2 + ell**2))
    eta = sp.simplify((1 - y**2)**2 * (y - c))
    r = sp.simplify(R + ell*y)
    p_r = sp.simplify(p0 * eta**2)
    dp_dr = sp.simplify(sp.diff(p_r, y) / ell)
    p_t = sp.simplify(p_r + r*dp_dr/2)
    P = sp.simplify(p_r + 2*p_t)
    E_pr = sp.simplify(sp.integrate(p_r*ell, (y, -1, 1)))
    I_P = sp.simplify(sp.integrate(P*ell, (y, -1, 1)))
    return y, R, ell, p0, r, eta, p_r, p_t, P, E_pr, I_P



def case_escape_hatch(out: ScriptOutput):
    header("Case 0: Escape-hatch requirement matrix")

    routes = [
        ("variational stress origin", True, "must derive u, p_free, and closure"),
        ("compensation/inertness principle", True, "must explain mass/trace neutrality without repair"),
        ("covariant layer lift", True, "must lift reduced diagnostics to geometry"),
        ("modified closure relation", True, "must derive, not choose, replacement for u=gammaP"),
        ("new tensor sector", True, "must have independent role and no source/trace double count"),
        ("choose u=P", False, "only trace-free"),
        ("choose u=-P", False, "only active-mass-neutral"),
        ("declare P=0", False, "P witness nonzero"),
        ("set p_free=0", False, "trivial no-response"),
        ("hide load in O", False, "active O not constructed"),
    ]

    for name, possible, requirement in routes:
        print(f"{name}: possible={possible}; {requirement}")

    with out.derived_results():
        for name, possible, requirement in routes:
            out.line(name, StatusMark.PASS if possible else StatusMark.FAIL, requirement)

    return {"possible_count": sp.Integer(sum(1 for _, possible, _ in routes if possible))}


def record_escape(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g63_escape",
        inputs=[],
        output=data["possible_count"],
        method="classify possible future escape hatches versus rejected shortcuts",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="escape_hatch_requirements",
        scope="future-route requirements; no physical closure",
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

    data = case_escape_hatch(out)

    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)
    record_escape(ns, data)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
