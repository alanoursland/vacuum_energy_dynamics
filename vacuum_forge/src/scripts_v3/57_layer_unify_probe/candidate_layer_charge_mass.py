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

SCRIPT_LABEL = 'Candidate Layer Charge / Mass'
MARKER_ID = 'g57_qm'
DEPENDENCIES = [('g56_summary', '56_silent_insert_law__candidate_group_56_status_summary', 'g56_summary'), ('g57_problem', '57_layer_unify_probe__candidate_layer_problem', 'g57_problem'), ('g57_energy', '57_layer_unify_probe__candidate_layer_energy', 'g57_energy')]
QUESTION = 'Does the finite transition layer create net scalar charge or mass shift?'
DISCIPLINE = 'This script computes reduced layer charge and mass-shift diagnostics. It does not prove charge neutrality.'
OPENING_LINE = 'Layer charge/mass diagnostic opened'
SCOPE = 'Group 57 layer charge mass'
NEXT_SCRIPT = 'candidate_layer_divergence.py'

ENTRIES = [('Q1: charge diagnostic', 'Q_layer=integral r^2*rho_layer dr', 'LAYER_CHARGE_CONDITION_DERIVED', 'layer charge must be explicit', 'not theorem closure'), ('Q2: flat odd cancellation', 'odd layer profile cancels in unweighted integral', 'LAYER_CHARGE_CONDITION_DERIVED', 'symmetry can help neutrality', 'not enough with r^2 weighting'), ('Q3: weighted charge warning', 'r^2 weighting can leave net charge', 'CHARGE_NEUTRALITY_REQUIRED', 'finite spherical layer needs weighted neutrality', 'not optional'), ('Q4: mass shift', 'Delta_M_layer=alpha Q_layer', 'LAYER_MASS_SHIFT_CONDITION_DERIVED', 'mass shift tied to net layer charge', 'conditional')]
SHORTCUTS = [('X1: odd profile as full neutrality', 'claim odd density guarantees spherical charge neutrality', 'r^2 weighting can spoil cancellation'), ('X2: hide layer charge', 'ignore Q_layer because layer is thin', 'thin is not zero'), ('X3: mass patch', 'absorb Delta_M_layer into exterior mass', 'mass shift must be neutral or derived')]
OBLIGATIONS = [('O1: weighted charge neutrality', 'CHARGE_NEUTRALITY_REQUIRED', 'construct or derive weighted zero-charge layer condition', 'avoid exterior scalar tail'), ('O2: mass neutrality', 'SAFETY_THEOREMS_REQUIRED', 'prove layer charge does not shift protected A-sector mass', 'avoid mass leakage')]
LOCAL_CONCLUSIONS = [('layer charge/mass diagnostic derived', 'PASS', 'weighted charge and mass-shift terms are explicit'), ('neutrality remains required', 'CHARGE_NEUTRALITY_REQUIRED', 'finite layer cannot hide charge by naming')]


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
        "LAYER_PROBE_OPENED": StatusMark.INFO,
        "SMOOTHSTEP_PROFILE_DERIVED": StatusMark.PASS,
        "BLEND_RESIDUE_DERIVED": StatusMark.PASS,
        "LAYER_RESIDUE_LOCALIZED": StatusMark.INFO,
        "LAYER_ENERGY_CONDITION_DERIVED": StatusMark.PASS,
        "LAYER_CHARGE_CONDITION_DERIVED": StatusMark.PASS,
        "LAYER_MASS_SHIFT_CONDITION_DERIVED": StatusMark.PASS,
        "LAYER_DIVERGENCE_CLOSURE_DERIVED": StatusMark.PASS,
        "LAYER_ROUTE_SURVIVES_CONDITIONALLY": StatusMark.INFO,
        "UNIFICATION_PROBE_SURVIVES_CONDITIONALLY": StatusMark.INFO,
        "CANDIDATE_TERM_SURFACE_OPENED": StatusMark.INFO,
        "COVARIANT_LIFT_REQUIRED": StatusMark.OBLIGATION,
        "ENERGY_ACCOUNTING_REQUIRED": StatusMark.OBLIGATION,
        "CHARGE_NEUTRALITY_REQUIRED": StatusMark.OBLIGATION,
        "DIVERGENCE_IDENTITY_REQUIRED": StatusMark.OBLIGATION,
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
        "ENERGY_ACCOUNTING_REQUIRED",
        "CHARGE_NEUTRALITY_REQUIRED",
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



def case_charge_mass(out: ScriptOutput):
    header("Case 0: Layer charge and mass-shift diagnostics")

    y, ell, R, beta, alpha = sp.symbols("y ell R beta alpha", positive=True)
    rho0, rho1 = sp.symbols("rho0 rho1")
    r = sp.simplify(R + ell*y)

    # Choose an odd layer charge density about y=0; leading net charge cancels in thin-layer approximation.
    rho_layer = sp.simplify(rho1 * y)
    Q_flat = sp.simplify(sp.integrate(rho_layer, (y, -1, 1)))
    Q_weighted = sp.simplify(sp.integrate(r**2 * rho_layer * ell, (y, -1, 1)))
    Q_condition = sp.solve(sp.Eq(Q_weighted, 0), rho1)
    delta_M = sp.simplify(alpha * Q_weighted)
    delta_M_zero = sp.simplify(delta_M.subs(rho1, 0))

    print(f"rho_layer(y) = {rho_layer}")
    print(f"flat charge integral = {Q_flat}")
    print(f"weighted reduced layer charge = {Q_weighted}")
    print(f"zero weighted charge condition solve for rho1 = {Q_condition}")
    print(f"Delta_M_layer = {delta_M}")
    print(f"Delta_M_layer with rho1=0 = {delta_M_zero}")

    with out.derived_results():
        out.line("flat layer charge", StatusMark.PASS if is_zero(Q_flat) else StatusMark.FAIL, f"Q_flat={Q_flat}")
        out.line("weighted layer charge", StatusMark.INFO if not is_zero(Q_weighted) else StatusMark.PASS, f"Q_weighted={Q_weighted}")
        out.line("zero charge condition", StatusMark.PASS, f"solve={Q_condition}")
        out.line("mass shift diagnostic", StatusMark.INFO if not is_zero(delta_M) else StatusMark.PASS, f"Delta_M={delta_M}")
        out.line("zero charge mass shift", StatusMark.PASS if is_zero(delta_M_zero) else StatusMark.FAIL, f"Delta_M={delta_M_zero}")

    return {"y": y, "ell": ell, "R": R, "rho_layer": rho_layer, "Q_flat": Q_flat, "Q_weighted": Q_weighted, "delta_M": delta_M}


def record_qm(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g57_qm",
        inputs=[data["y"], data["ell"], data["R"]],
        output=data["Q_weighted"],
        method="compute reduced weighted layer charge and mass-shift diagnostic",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="layer_charge_mass_condition",
        scope="reduced layer charge/mass diagnostic; not neutrality theorem",
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

    data = case_charge_mass(out)

    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)
    record_qm(ns, data)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
