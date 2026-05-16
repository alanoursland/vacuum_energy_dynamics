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

SCRIPT_LABEL = 'Candidate Tail / Mass Zero'
MARKER_ID = 'g58_tailmass'
DEPENDENCIES = [('g57_summary', '57_layer_unify_probe__candidate_group_57_status_summary', 'g57_summary'), ('g58_problem', '58_weighted_neutral_layer__candidate_weighted_problem', 'g58_problem'), ('g58_profile', '58_weighted_neutral_layer__candidate_weighted_profile', 'g58_profile'), ('g58_energy', '58_weighted_neutral_layer__candidate_weighted_energy', 'g58_energy')]
QUESTION = 'Does the weighted-neutral layer profile kill reduced exterior tail and mass-shift diagnostics?'
DISCIPLINE = 'This script uses Q_weighted=0 to check reduced tail and mass-shift diagnostics. It does not prove full boundary or mass theorem.'
OPENING_LINE = 'Tail and mass zero diagnostic opened'
SCOPE = 'Group 58 tail mass zero'
NEXT_SCRIPT = 'candidate_weighted_divergence.py'

ENTRIES = [('T1: weighted charge', 'Q_weighted=0', 'WEIGHTED_NEUTRALITY_CONFIRMED', 'layer scalar charge vanishes in spherical weighting', 'reduced'), ('T2: exterior tail', 'phi_ext=C0+kQ/r', 'TAIL_MASS_ZERO_CONFIRMED', 'Q=0 and C0=0 kill exterior scalar tail', 'conditional'), ('T3: mass shift', 'Delta_M=alpha Q=0', 'TAIL_MASS_ZERO_CONFIRMED', 'weighted neutrality kills charge-driven mass diagnostic', 'not full mass theorem')]
SHORTCUTS = [('X1: Q=0 as full boundary theorem', 'treat zero weighted charge as all boundary safety', 'shell/stress/covariant lift remain'), ('X2: C0 ignored', 'forget zero-offset condition for exterior scalar silence', 'C0=0 remains required'), ('X3: mass theorem by diagnostic', 'treat Delta_M=0 diagnostic as full mass theorem', 'full mass neutrality remains open')]
OBLIGATIONS = [('O1: source safety', 'SOURCE_SAFETY_REQUIRED', 'prove weighted-neutral layer does not duplicate ordinary source', 'avoid source leakage'), ('O2: covariant lift', 'COVARIANT_LIFT_REQUIRED', 'lift weighted neutrality to geometric layer measure', 'avoid radial-only proof')]
LOCAL_CONCLUSIONS = [('tail and mass diagnostics zero', 'PASS', 'weighted-neutral profile kills reduced Q-driven exterior tail and mass shift'), ('physical use blocked', 'NOT_INSERTABLE', 'tail/mass diagnostics are not insertion')]


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



def case_tail_mass_zero(out: ScriptOutput):
    header("Case 0: Exterior tail and mass-shift diagnostics from weighted neutrality")

    y, R, ell, rho0, r, C0, k, alpha = sp.symbols("y R ell rho0 r C0 k alpha", positive=True)
    c_star = sp.simplify(2*R*ell/(7*R**2 + ell**2))
    w = sp.simplify((1 - y**2)**2)
    rho = sp.simplify(rho0 * w * (y - c_star))
    Q = sp.simplify(sp.integrate((R + ell*y)**2 * rho, (y, -1, 1)))
    phi_ext = sp.simplify(C0 + k*Q/r)
    phi_silent = sp.simplify(phi_ext.subs(C0, 0))
    delta_M = sp.simplify(alpha * Q)

    print(f"Q_weighted = {Q}")
    print(f"phi_ext = {phi_ext}")
    print(f"phi_ext with C0=0 = {phi_silent}")
    print(f"Delta_M = {delta_M}")

    with out.derived_results():
        out.line("weighted charge", StatusMark.PASS if is_zero(Q) else StatusMark.FAIL, f"Q={Q}")
        out.line("exterior tail", StatusMark.PASS, f"phi_ext={phi_ext}")
        out.line("zero-offset tail", StatusMark.PASS if is_zero(phi_silent) else StatusMark.FAIL, f"phi={phi_silent}")
        out.line("mass shift", StatusMark.PASS if is_zero(delta_M) else StatusMark.FAIL, f"Delta_M={delta_M}")

    return {"Q": Q, "phi_silent": phi_silent, "delta_M": delta_M}


def record_tailmass(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g58_tailmass",
        inputs=[],
        output=data["Q"],
        method="verify weighted-neutral profile gives zero tail coefficient and mass-shift diagnostic",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="weighted_tail_mass_zero",
        scope="reduced exterior tail/mass diagnostic; not full theorem",
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

    data = case_tail_mass_zero(out)

    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)
    record_tailmass(ns, data)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
