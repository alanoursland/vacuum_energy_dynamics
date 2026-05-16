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

SCRIPT_LABEL = 'Candidate Divergence-Silent Stress'
MARKER_ID = 'g56_div'
DEPENDENCIES = [('g55_summary', '55_insertion_exclusion_sieve__candidate_group_55_status_summary', 'g55_summary'), ('g56_problem', '56_silent_insert_law__candidate_silent_problem', 'g56_problem'), ('g56_shell', '56_silent_insert_law__candidate_shell_neutral_match', 'g56_shell')]
QUESTION = 'Can a reduced anisotropic stress closure be made divergence-silent and boundary-null?'
DISCIPLINE = 'This script constructs a reduced spherical divergence-silent stress closure. It is not a covariant Bianchi identity proof.'
OPENING_LINE = 'Divergence-silent stress closure opened'
SCOPE = 'Group 56 divergence-silent stress'
NEXT_SCRIPT = 'candidate_silent_route_classifier.py'

ENTRIES = [('D1: radial stress profile', 'p_r=p0*r^2*(R-r)^2', 'DIVERGENCE_SILENT_CLOSURE_DERIVED', 'radial stress is boundary-null', 'reduced'), ('D2: tangential closure', "p_t=p_r+r*p_r'/2", 'DIVERGENCE_SILENT_CLOSURE_DERIVED', 'closure cancels reduced radial divergence', 'not covariant'), ('D3: divergence diagnostic', "D=p_r'+2*(p_r-p_t)/r=0", 'DIVERGENCE_SILENT_CLOSURE_DERIVED', 'reduced divergence vanishes', 'not Bianchi proof'), ('D4: boundary stress', 'p_r(R)=0 and p_t(R)=0', 'DIVERGENCE_SILENT_CLOSURE_DERIVED', 'stress is boundary-null', 'reduced')]
SHORTCUTS = [('X1: reduced divergence as Bianchi proof', 'treat D=0 as full covariant divergence identity', 'scope is reduced'), ('X2: closure as physical stress law', 'treat tangential closure as adopted physics', 'closure is theorem surface'), ('X3: divergence silence as insertion', 'insert because reduced divergence vanishes', 'physical use remains blocked')]
OBLIGATIONS = [('O1: covariant divergence lift', 'COVARIANT_LIFT_REQUIRED', 'lift reduced divergence-silent closure to geometric/covariant identity', 'avoid parent overclaim'), ('O2: insertion law still required', 'INSERTION_LAW_REQUIRED', 'derive actual silent insertion law if route continues', 'avoid ad hoc closure')]
LOCAL_CONCLUSIONS = [('divergence-silent closure derived', 'PASS', 'reduced anisotropic closure gives D=0'), ('physical use blocked', 'NOT_INSERTABLE', 'reduced divergence silence is not insertion')]


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
        "SILENT_LAW_SURFACE_OPENED": StatusMark.INFO,
        "BOUNDARY_NULL_PROFILE_DERIVED": StatusMark.PASS,
        "CHARGE_NEUTRAL_PROFILE_DERIVED": StatusMark.PASS,
        "EXTERIOR_TAIL_ZERO_CONDITION_DERIVED": StatusMark.PASS,
        "SHELL_NEUTRAL_CONDITION_DERIVED": StatusMark.PASS,
        "DIVERGENCE_SILENT_CLOSURE_DERIVED": StatusMark.PASS,
        "SILENT_INSERTION_ROUTE_SURVIVES_CONDITIONALLY": StatusMark.INFO,
        "COVARIANT_LIFT_REQUIRED": StatusMark.OBLIGATION,
        "INSERTION_LAW_REQUIRED": StatusMark.OBLIGATION,
        "SAFETY_THEOREMS_REQUIRED": StatusMark.OBLIGATION,
        "PHYSICAL_USE_BLOCKED": StatusMark.DEFER,
        "NOT_INSERTABLE": StatusMark.DEFER,
        "ACTIVE_O_NECESSITY_NOT_ESTABLISHED": StatusMark.DEFER,
        "DEFERRED_WITH_TARGET": StatusMark.DEFER,
        "CANDIDATE_SURVIVES_AS_AUDIT_ONLY": StatusMark.INFO,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REJECTED_ROUTE": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
        "OBSTRUCTION_WITNESS_FOUND": StatusMark.FAIL,
    }.get(status, StatusMark.INFO)


def governance_status(status: str) -> GovernanceStatus:
    if status in {"REJECTED_ROUTE", "FORBIDDEN_SHORTCUT", "OBSTRUCTION_WITNESS_FOUND"}:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {
        "COVARIANT_LIFT_REQUIRED",
        "INSERTION_LAW_REQUIRED",
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



def case_divergence_silent_stress(out: ScriptOutput):
    header("Case 0: Reduced divergence-silent anisotropic stress closure")

    r, R, p0 = sp.symbols("r R p0", positive=True)
    p_r = sp.simplify(p0 * r**2 * (R-r)**2)
    dp_r = sp.diff(p_r, r)
    p_t = sp.simplify(p_r + r*dp_r/2)
    D = sp.simplify(dp_r + 2*(p_r - p_t)/r)
    p_r_R = sp.simplify(p_r.subs(r, R))
    p_t_R = sp.simplify(p_t.subs(r, R))

    print(f"p_r = {p_r}")
    print(f"p_t = p_r + r*p_r'/2 = {p_t}")
    print(f"D = p_r' + 2*(p_r-p_t)/r = {D}")
    print(f"p_r(R) = {p_r_R}")
    print(f"p_t(R) = {p_t_R}")

    with out.derived_results():
        out.line("radial stress", StatusMark.PASS, f"p_r={p_r}")
        out.line("tangential closure", StatusMark.PASS, f"p_t={p_t}")
        out.line("divergence diagnostic", StatusMark.PASS if is_zero(D) else StatusMark.FAIL, f"D={D}")
        out.line("boundary radial stress", StatusMark.PASS if is_zero(p_r_R) else StatusMark.FAIL, f"p_r(R)={p_r_R}")
        out.line("boundary tangential stress", StatusMark.PASS if is_zero(p_t_R) else StatusMark.FAIL, f"p_t(R)={p_t_R}")

    return {"r": r, "R": R, "p0": p0, "p_r": p_r, "p_t": p_t, "D": D}


def record_div(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g56_div",
        inputs=[data["r"], data["R"], data["p0"]],
        output=data["D"],
        method="choose p_t=p_r+r*p_r'/2 so p_r'+2(p_r-p_t)/r=0",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="divergence_silent_stress",
        scope="reduced spherical divergence diagnostic; not covariant Bianchi proof",
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

    data = case_divergence_silent_stress(out)

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
