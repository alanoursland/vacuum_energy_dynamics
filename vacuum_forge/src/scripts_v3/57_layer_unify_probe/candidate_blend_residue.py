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

SCRIPT_LABEL = 'Candidate Blend Residue'
MARKER_ID = 'g57_res'
DEPENDENCIES = [('g56_summary', '56_silent_insert_law__candidate_group_56_status_summary', 'g56_summary'), ('g57_problem', '57_layer_unify_probe__candidate_layer_problem', 'g57_problem'), ('g57_s', '57_layer_unify_probe__candidate_smoothstep_profile', 'g57_s')]
QUESTION = 'What derivative residue terms appear when interior and exterior profiles are smoothly blended?'
DISCIPLINE = 'This script derives symbolic transition residues from a finite-layer blend. Residues are candidate clues, not inserted terms.'
OPENING_LINE = 'Blend residue derivation opened'
SCOPE = 'Group 57 blend residue'
NEXT_SCRIPT = 'candidate_layer_energy.py'

ENTRIES = [('R1: blended field', 'F=(1-s)F_in+sF_out', 'BLEND_RESIDUE_DERIVED', 'finite layer interpolates between reduced interior and exterior profiles', 'not physical law'), ('R2: first residue', "R1=s'(F_out-F_in)", 'BLEND_RESIDUE_DERIVED', 'first derivative exposes transition mismatch', 'candidate layer term only'), ('R3: second residue', "R2 contains s''(F_out-F_in)+2s'(F_out'-F_in')", 'BLEND_RESIDUE_DERIVED', 'second derivative exposes curvature/transition residue', 'not parent equation'), ('R4: unification hint', "residues vanish outside layer if s' and s'' vanish", 'LAYER_RESIDUE_LOCALIZED', 'localized transition terms can be audited', 'not safety proof')]
SHORTCUTS = [('X1: residue as repair tensor', 'insert residues as H_curv/H_exch repair', 'residues are diagnostics'), ('X2: residue ignored', 'blend profiles without accounting for derivative residues', 'layer cost must be explicit'), ('X3: mismatch hidden', 'hide F_out-F_in in notation', 'mismatch is the signal being tested')]
OBLIGATIONS = [('O1: energy accounting', 'ENERGY_ACCOUNTING_REQUIRED', 'evaluate whether residues imply finite localized layer energy', 'avoid free blending'), ('O2: candidate term discipline', 'POLICY_RULE', 'treat residues as candidate-term surface only', 'avoid insertion drift')]
LOCAL_CONCLUSIONS = [('blend residues derived', 'PASS', 'finite-layer blend exposes explicit transition residues'), ('physical use blocked', 'NOT_INSERTABLE', 'residues are not inserted terms')]


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



def case_blend_residue(out: ScriptOutput):
    header("Case 0: Blended profile derivative residues")

    r = sp.symbols("r", positive=True)
    s = sp.Function("s")(r)
    F_in = sp.Function("F_in")(r)
    F_out = sp.Function("F_out")(r)

    F = sp.simplify((1 - s)*F_in + s*F_out)
    expected_dF = sp.simplify((1 - s)*sp.diff(F_in, r) + s*sp.diff(F_out, r))
    residue_1 = sp.simplify(sp.diff(F, r) - expected_dF)

    expected_d2F = sp.simplify((1 - s)*sp.diff(F_in, r, 2) + s*sp.diff(F_out, r, 2))
    residue_2 = sp.simplify(sp.diff(F, r, 2) - expected_d2F)

    print(f"F = {F}")
    print(f"first derivative residue = {residue_1}")
    print(f"second derivative residue = {residue_2}")

    with out.derived_results():
        out.line("blended field", StatusMark.PASS, f"F={F}")
        out.line("first derivative residue", StatusMark.PASS, f"R1={residue_1}")
        out.line("second derivative residue", StatusMark.PASS, f"R2={residue_2}")

    return {"r": r, "F": F, "R1": residue_1, "R2": residue_2}


def record_res(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g57_res",
        inputs=[data["r"]],
        output=data["R2"],
        method="derive first and second derivative residues of F=(1-s)F_in+sF_out",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="layer_blend_residue",
        scope="symbolic layer residue; candidate transition term surface only",
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

    data = case_blend_residue(out)

    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)
    record_res(ns, data)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
