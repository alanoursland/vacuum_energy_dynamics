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

SCRIPT_LABEL = 'Candidate Flat vs Weighted Neutrality'
MARKER_ID = 'g58_compare'
DEPENDENCIES = [('g57_summary', '57_layer_unify_probe__candidate_group_57_status_summary', 'g57_summary'), ('g58_problem', '58_weighted_neutral_layer__candidate_weighted_problem', 'g58_problem'), ('g58_profile', '58_weighted_neutral_layer__candidate_weighted_profile', 'g58_profile')]
QUESTION = 'Does the new weighted-neutral profile fix the Group 57 flat-neutrality failure?'
DISCIPLINE = 'This script compares flat odd cancellation to weighted spherical neutrality. It rejects flat neutrality as sufficient.'
OPENING_LINE = 'Flat versus weighted neutrality comparison opened'
SCOPE = 'Group 58 flat vs weighted neutrality'
NEXT_SCRIPT = 'candidate_weighted_energy.py'

ENTRIES = [('F1: odd flat cancellation', 'rho_odd=rho1*y gives Q_flat=0', 'FLAT_NEUTRALITY_REJECTED', 'flat cancellation alone is not enough', 'rejected as sufficient'), ('F2: odd weighted charge', 'rho_odd leaves nonzero weighted charge', 'FLAT_NEUTRALITY_REJECTED', 'spherical r^2 weighting spoils naive symmetry', 'rejected'), ('F3: skewed weighted profile', 'rho=rho0*w*(y-c*) gives Q_weighted=0', 'WEIGHTED_NEUTRALITY_CONFIRMED', 'geometry-aware skew fixes weighted charge', 'reduced'), ('F4: flat charge not target', 'weighted-neutral profile need not have zero flat integral', 'WEIGHTED_NEUTRALITY_CONFIRMED', 'correct target is weighted charge', 'not flat neutrality')]
SHORTCUTS = [('X1: flat charge target', 'use flat integral as the neutrality condition', 'spherical weighting is required'), ('X2: odd symmetry shortcut', 'claim oddness implies physical neutrality', 'Group 57 found the failure'), ('X3: weighted profile as proof of source safety', 'claim weighted charge zero proves source role-purity', 'source safety remains separate')]
OBLIGATIONS = [('O1: weighted neutrality standard', 'POLICY_RULE', 'future layer profiles must use weighted neutrality', 'avoid flat-coordinate shortcut'), ('O2: mass/tail audit', 'SAFETY_THEOREMS_REQUIRED', 'connect weighted Q=0 to tail and mass diagnostics', 'avoid hidden mass shift')]
LOCAL_CONCLUSIONS = [('flat neutrality rejected', 'FLAT_NEUTRALITY_REJECTED', 'odd flat cancellation is not sufficient'), ('weighted neutrality confirmed', 'PASS', 'skewed localized profile has zero weighted charge')]


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
        "WEIGHTED_LAYER_PROBLEM_OPENED": StatusMark.INFO,
        "WEIGHTED_NEUTRAL_PROFILE_DERIVED": StatusMark.PASS,
        "GEOMETRIC_SKEW_DERIVED": StatusMark.PASS,
        "FLAT_NEUTRALITY_REJECTED": StatusMark.FAIL,
        "WEIGHTED_NEUTRALITY_CONFIRMED": StatusMark.PASS,
        "LOCALIZED_LAYER_PROFILE_DERIVED": StatusMark.PASS,
        "WEIGHTED_ENERGY_CONDITION_DERIVED": StatusMark.PASS,
        "TAIL_MASS_ZERO_CONFIRMED": StatusMark.PASS,
        "WEIGHTED_DIVERGENCE_CLOSURE_DERIVED": StatusMark.PASS,
        "WEIGHTED_LAYER_ROUTE_SURVIVES_CONDITIONALLY": StatusMark.INFO,
        "UNIFICATION_PROBE_SURVIVES_CONDITIONALLY": StatusMark.INFO,
        "CANDIDATE_TERM_SURFACE_OPENED": StatusMark.INFO,
        "COVARIANT_LIFT_REQUIRED": StatusMark.OBLIGATION,
        "ENERGY_ACCOUNTING_REQUIRED": StatusMark.OBLIGATION,
        "CHARGE_NEUTRALITY_REQUIRED": StatusMark.OBLIGATION,
        "DIVERGENCE_IDENTITY_REQUIRED": StatusMark.OBLIGATION,
        "SAFETY_THEOREMS_REQUIRED": StatusMark.OBLIGATION,
        "SOURCE_SAFETY_REQUIRED": StatusMark.OBLIGATION,
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
    if status in {
        "REJECTED_ROUTE",
        "FORBIDDEN_SHORTCUT",
        "OBSTRUCTION_WITNESS_FOUND",
        "FLAT_NEUTRALITY_REJECTED",
    }:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {
        "COVARIANT_LIFT_REQUIRED",
        "ENERGY_ACCOUNTING_REQUIRED",
        "CHARGE_NEUTRALITY_REQUIRED",
        "DIVERGENCE_IDENTITY_REQUIRED",
        "SAFETY_THEOREMS_REQUIRED",
        "SOURCE_SAFETY_REQUIRED",
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



def case_flat_vs_weighted(out: ScriptOutput):
    header("Case 0: Flat odd cancellation versus weighted neutrality")

    y, R, ell, rho0, rho1 = sp.symbols("y R ell rho0 rho1", positive=True)
    r = sp.simplify(R + ell*y)
    rho_odd = sp.simplify(rho1*y)
    Q_flat_odd = sp.simplify(sp.integrate(rho_odd, (y, -1, 1)))
    Q_weighted_odd = sp.simplify(sp.integrate(r**2 * rho_odd, (y, -1, 1)))

    w = sp.simplify((1 - y**2)**2)
    c_star = sp.simplify(2*R*ell/(7*R**2 + ell**2))
    rho_weighted = sp.simplify(rho0 * w * (y - c_star))
    Q_flat_weighted = sp.simplify(sp.integrate(rho_weighted, (y, -1, 1)))
    Q_weighted = sp.simplify(sp.integrate(r**2 * rho_weighted, (y, -1, 1)))

    print(f"rho_odd = {rho_odd}")
    print(f"Q_flat_odd = {Q_flat_odd}")
    print(f"Q_weighted_odd = {Q_weighted_odd}")
    print(f"rho_weighted = {rho_weighted}")
    print(f"Q_flat_weighted = {Q_flat_weighted}")
    print(f"Q_weighted = {Q_weighted}")

    with out.derived_results():
        out.line("odd flat charge", StatusMark.PASS if is_zero(Q_flat_odd) else StatusMark.FAIL, f"Q_flat={Q_flat_odd}")
        out.line("odd weighted charge", StatusMark.FAIL if not is_zero(Q_weighted_odd) else StatusMark.PASS, f"Q_weighted={Q_weighted_odd}")
        out.line("weighted profile flat charge", StatusMark.INFO if not is_zero(Q_flat_weighted) else StatusMark.PASS, f"Q_flat={Q_flat_weighted}")
        out.line("weighted profile weighted charge", StatusMark.PASS if is_zero(Q_weighted) else StatusMark.FAIL, f"Q_weighted={Q_weighted}")

    return {
        "Q_flat_odd": Q_flat_odd,
        "Q_weighted_odd": Q_weighted_odd,
        "Q_flat_weighted": Q_flat_weighted,
        "Q_weighted": Q_weighted,
    }


def record_compare(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g58_compare",
        inputs=[],
        output=data["Q_weighted_odd"],
        method="compare odd flat profile and weighted-neutral skewed profile",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="flat_vs_weighted_neutrality",
        scope="reduced finite-layer neutrality comparison; not source theorem",
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

    data = case_flat_vs_weighted(out)

    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)
    record_compare(ns, data)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
