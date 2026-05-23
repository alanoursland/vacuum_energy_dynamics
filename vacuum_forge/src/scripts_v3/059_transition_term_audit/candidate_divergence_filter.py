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

SCRIPT_LABEL = 'Candidate Divergence Filter'
MARKER_ID = 'g59_div'
DEPENDENCIES = [('g58_summary', '58_weighted_neutral_layer__candidate_group_58_status_summary', 'g58_summary'), ('g59_problem', '59_transition_term_audit__candidate_transition_problem', 'g59_problem'), ('g59_neu', '59_transition_term_audit__candidate_weighted_neutralizer', 'g59_neu'), ('g59_src', '59_transition_term_audit__candidate_source_trace_filter', 'g59_src')]
QUESTION = 'Which transition stress candidates satisfy the reduced divergence diagnostic?'
DISCIPLINE = 'This script rejects radial-only divergence-failing candidates and retains closure-supported reduced candidates. It is not a covariant Bianchi proof.'
OPENING_LINE = 'Transition divergence filter opened'
SCOPE = 'Group 59 divergence filter'
NEXT_SCRIPT = 'candidate_transition_route_classifier.py'

ENTRIES = [('D1: radial-only rejection', 'p_t=0 generally gives D != 0', 'DIVERGENCE_FAILING_TERM_REJECTED', 'radial-only layer stress is not admissible', 'rejected'), ('D2: closure route', "p_t=p_r+r*p_r'/2", 'CLOSURE_SUPPORTED_TERM_SURVIVES', 'closure-supported stress satisfies reduced D=0', 'conditional'), ('D3: divergence filter', "D=p_r'+2(p_r-p_t)/r", 'DIVERGENCE_FILTER_APPLIED', 'reduced divergence is explicit', 'not Bianchi proof'), ('D4: route status', 'closure-supported weighted layer stress survives conditionally', 'TRANSITION_TERM_SURVIVES_CONDITIONALLY', 'requires covariant lift and source safety', 'not insertion')]
SHORTCUTS = [('X1: radial-only stress', 'accept p_r layer stress without tangential closure', 'reduced divergence fails'), ('X2: D=0 as Bianchi', 'treat reduced closure as covariant identity', 'covariant lift required'), ('X3: closure as insertion', 'insert closure-supported stress into parent equation', 'not licensed')]
OBLIGATIONS = [('O1: covariant divergence identity', 'DIVERGENCE_IDENTITY_REQUIRED', 'lift closure route to covariant divergence identity', 'avoid parent overclaim'), ('O2: candidate-term audit', 'DEFERRED_WITH_TARGET', 'keep closure-supported term as candidate surface only', 'avoid insertion drift')]
LOCAL_CONCLUSIONS = [('divergence filter applied', 'PASS', 'radial-only route rejected and closure route survives conditionally'), ('physical use blocked', 'NOT_INSERTABLE', 'divergence filter is not parent equation')]


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
        "TRANSITION_AUDIT_OPENED": StatusMark.INFO,
        "RESIDUE_INVENTORY_DERIVED": StatusMark.PASS,
        "CANDIDATE_TERM_SURFACE_OPENED": StatusMark.INFO,
        "LOCALITY_FILTER_APPLIED": StatusMark.PASS,
        "LOCALIZED_LAYER_TERM_CONFIRMED": StatusMark.PASS,
        "NONLOCAL_TERM_REJECTED": StatusMark.FAIL,
        "WEIGHTED_NEUTRALIZER_DERIVED": StatusMark.PASS,
        "WEIGHTED_NEUTRALITY_CONFIRMED": StatusMark.PASS,
        "SCALAR_CHARGE_TERM_REJECTED": StatusMark.FAIL,
        "SOURCE_CARRYING_TERM_REJECTED": StatusMark.FAIL,
        "TRACE_DOUBLE_COUNT_TERM_REJECTED": StatusMark.FAIL,
        "SOURCE_TRACE_FILTER_APPLIED": StatusMark.PASS,
        "DIVERGENCE_FILTER_APPLIED": StatusMark.PASS,
        "DIVERGENCE_FAILING_TERM_REJECTED": StatusMark.FAIL,
        "CLOSURE_SUPPORTED_TERM_SURVIVES": StatusMark.INFO,
        "TRANSITION_TERM_SURVIVES_CONDITIONALLY": StatusMark.INFO,
        "WEIGHTED_LAYER_ROUTE_SURVIVES_CONDITIONALLY": StatusMark.INFO,
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
        "REJECTED_ROUTE",
        "FORBIDDEN_SHORTCUT",
        "NONLOCAL_TERM_REJECTED",
        "SCALAR_CHARGE_TERM_REJECTED",
        "SOURCE_CARRYING_TERM_REJECTED",
        "TRACE_DOUBLE_COUNT_TERM_REJECTED",
        "DIVERGENCE_FAILING_TERM_REJECTED",
    }:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {
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



def case_divergence_filter(out: ScriptOutput):
    header("Case 0: Divergence filter for transition candidates")

    y, R, ell, p0 = sp.symbols("y R ell p0", positive=True)
    r = sp.simplify(R + ell*y)
    w = sp.simplify((1 - y**2)**2)
    c_star = sp.simplify(2*R*ell/(7*R**2 + ell**2))
    eta = sp.simplify(w * (y - c_star))

    p_r = sp.simplify(p0 * eta**2)
    dp_dr = sp.simplify(sp.diff(p_r, y) / ell)

    # Failing radial-only candidate with p_t=0.
    p_t_fail = sp.Integer(0)
    D_fail = sp.simplify(dp_dr + 2*(p_r - p_t_fail)/r)

    # Closure-supported candidate.
    p_t_closure = sp.simplify(p_r + r*dp_dr/2)
    D_closure = sp.simplify(dp_dr + 2*(p_r - p_t_closure)/r)

    print(f"p_r = {p_r}")
    print(f"D with p_t=0 = {D_fail}")
    print(f"p_t closure = {p_t_closure}")
    print(f"D with closure = {D_closure}")

    with out.derived_results():
        out.line("radial stress", StatusMark.PASS, f"p_r={p_r}")
        out.line("radial-only divergence", StatusMark.FAIL if not is_zero(D_fail) else StatusMark.PASS, f"D_fail={D_fail}")
        out.line("closure tangential stress", StatusMark.PASS, f"p_t={p_t_closure}")
        out.line("closure divergence", StatusMark.PASS if is_zero(D_closure) else StatusMark.FAIL, f"D={D_closure}")

    return {"y": y, "R": R, "ell": ell, "p_r": p_r, "D_fail": D_fail, "p_t": p_t_closure, "D": D_closure}


def record_div(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g59_div",
        inputs=[data["y"], data["R"], data["ell"]],
        output=data["D"],
        method="reject radial-only layer stress and retain closure p_t=p_r+r*p_r'/2 in reduced divergence filter",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="transition_divergence_filter",
        scope="reduced divergence filter; not covariant Bianchi proof",
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

    data = case_divergence_filter(out)

    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)
    record_div(ns, data)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
