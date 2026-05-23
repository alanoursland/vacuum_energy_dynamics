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

SCRIPT_LABEL = 'Candidate Weighted Profile Energy'
MARKER_ID = 'g58_energy'
DEPENDENCIES = [('g57_summary', '57_layer_unify_probe__candidate_group_57_status_summary', 'g57_summary'), ('g58_problem', '58_weighted_neutral_layer__candidate_weighted_problem', 'g58_problem'), ('g58_profile', '58_weighted_neutral_layer__candidate_weighted_profile', 'g58_profile'), ('g58_compare', '58_weighted_neutral_layer__candidate_flat_vs_weighted', 'g58_compare')]
QUESTION = 'Does the weighted-neutral profile have finite explicit reduced gradient energy?'
DISCIPLINE = 'This script computes reduced gradient-energy scaling for the weighted-neutral layer profile. It does not prove full stress-energy accounting.'
OPENING_LINE = 'Weighted-neutral layer energy audit opened'
SCOPE = 'Group 58 weighted profile energy'
NEXT_SCRIPT = 'candidate_tail_mass_zero.py'

ENTRIES = [('E1: profile energy', 'integral (drho/dr)^2 dr is finite for finite ell', 'WEIGHTED_ENERGY_CONDITION_DERIVED', 'weighted-neutral profile has explicit energy cost', 'reduced diagnostic'), ('E2: no free neutrality', 'energy scales with rho0 and ell', 'ENERGY_ACCOUNTING_REQUIRED', 'neutrality is not free', 'not stress tensor'), ('E3: hard-shell warning', 'thin-layer scaling remains costly', 'ENERGY_ACCOUNTING_REQUIRED', 'finite width matters', 'not obstruction by itself')]
SHORTCUTS = [('X1: neutral means free', 'treat weighted charge zero as zero energy', 'gradient energy remains'), ('X2: energy as mass proof', 'treat finite profile energy as mass neutrality', 'mass diagnostic remains separate'), ('X3: reduced energy as covariant stress', 'promote reduced energy directly to stress tensor', 'covariant lift remains required')]
OBLIGATIONS = [('O1: tail/mass zero check', 'SAFETY_THEOREMS_REQUIRED', 'verify Q=0 kills exterior tail and mass-shift diagnostics', 'avoid hidden exterior load'), ('O2: covariant energy accounting', 'COVARIANT_LIFT_REQUIRED', 'lift reduced profile energy to geometric stress accounting', 'avoid reduced overclaim')]
LOCAL_CONCLUSIONS = [('weighted profile energy derived', 'PASS', 'weighted-neutral profile has finite explicit reduced energy for finite ell'), ('physical use blocked', 'NOT_INSERTABLE', 'energy result is not insertion')]


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



def case_weighted_energy(out: ScriptOutput):
    header("Case 0: Weighted-neutral profile reduced gradient energy")

    y, R, ell, rho0 = sp.symbols("y R ell rho0", positive=True)
    c_star = sp.simplify(2*R*ell/(7*R**2 + ell**2))
    w = sp.simplify((1 - y**2)**2)
    rho = sp.simplify(rho0 * w * (y - c_star))
    drho_dy = sp.diff(rho, y)
    E_y = sp.simplify(sp.integrate(drho_dy**2, (y, -1, 1)))
    E_r = sp.simplify(E_y / ell)
    E_r_factored = sp.factor(E_r)
    thin_limit_coeff = sp.simplify(sp.limit(ell * E_r / rho0**2, ell, 0, dir="+"))

    print(f"rho(y) = {rho}")
    print(f"drho/dy = {drho_dy}")
    print(f"Integral (drho/dy)^2 dy = {sp.factor(E_y)}")
    print(f"Reduced gradient energy scaling E ~ {E_r_factored}")
    print(f"thin-layer coefficient limit ell*E/rho0^2 = {thin_limit_coeff}")

    with out.derived_results():
        out.line("profile gradient", StatusMark.PASS, f"drho/dy={drho_dy}")
        out.line("finite y-energy", StatusMark.PASS, f"E_y={sp.factor(E_y)}")
        out.line("finite layer energy", StatusMark.PASS, f"E_r={E_r_factored}")
        out.line("thin limit scaling", StatusMark.INFO, f"ell*E/rho0^2 -> {thin_limit_coeff}")

    return {"y": y, "R": R, "ell": ell, "rho0": rho0, "rho": rho, "E_y": E_y, "E_r": E_r}


def record_energy(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g58_E",
        inputs=[data["y"], data["R"], data["ell"], data["rho0"]],
        output=data["E_r"],
        method="compute reduced gradient energy of weighted-neutral profile",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="weighted_profile_energy",
        scope="reduced layer energy diagnostic; not stress theorem",
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

    data = case_weighted_energy(out)

    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)
    record_energy(ns, data)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
