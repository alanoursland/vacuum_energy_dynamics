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

SCRIPT_LABEL = 'Candidate Smoothstep Profile'
MARKER_ID = 'g57_s'
DEPENDENCIES = [('g56_summary', '056_silent_insert_law__candidate_group_56_status_summary', 'g56_summary'), ('g57_problem', '057_layer_unify_probe__candidate_layer_problem', 'g57_problem')]
QUESTION = 'Can a finite transition layer have smooth endpoint value, slope, and curvature matching?'
DISCIPLINE = 'This script constructs a quintic smoothstep layer profile and verifies endpoint behavior. It does not prove physical boundary neutrality.'
OPENING_LINE = 'Smoothstep finite-layer profile construction opened'
SCOPE = 'Group 57 smoothstep profile'
NEXT_SCRIPT = 'candidate_blend_residue.py'

ENTRIES = [('S1: layer coordinate', 'x=(r-(R-ell))/(2ell)', 'SMOOTHSTEP_PROFILE_DERIVED', 'finite layer maps to x in [0,1]', 'reduced radial coordinate'), ('S2: smoothstep', 's=10x^3-15x^4+6x^5', 'SMOOTHSTEP_PROFILE_DERIVED', 'profile transitions from 0 to 1', 'not physical law'), ('S3: endpoint slope', "s'(0)=s'(1)=0", 'SMOOTHSTEP_PROFILE_DERIVED', 'first-derivative endpoint mismatch can be avoided', 'not full junction theorem'), ('S4: endpoint curvature', "s''(0)=s''(1)=0", 'SMOOTHSTEP_PROFILE_DERIVED', 'second-derivative endpoint mismatch can be softened', 'not covariant lift')]
SHORTCUTS = [('X1: smoothstep as physics', 'treat smoothstep as the final physical law', 'it is a probe function'), ('X2: endpoint smoothness as neutrality', 'claim zero layer charge from endpoint behavior alone', 'charge/mass must be computed'), ('X3: finite layer as parent equation', 'promote s(r) to parent structure', 'candidate term work remains later')]
OBLIGATIONS = [('O1: blend residue', 'ENERGY_ACCOUNTING_REQUIRED', 'compute derivative residues created by blending', 'identify layer terms'), ('O2: covariant lift', 'COVARIANT_LIFT_REQUIRED', 'replace radial layer coordinate with geometric object later', 'avoid overclaim')]
LOCAL_CONCLUSIONS = [('smoothstep profile derived', 'PASS', 'quintic layer has smooth endpoint value/slope/curvature behavior'), ('physical use blocked', 'NOT_INSERTABLE', 'smoothstep is not insertion')]


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



def case_smoothstep(out: ScriptOutput):
    header("Case 0: Quintic smoothstep finite-layer profile")

    r, R, ell = sp.symbols("r R ell", positive=True)
    x = sp.symbols("x", real=True)
    s_x = sp.simplify(10*x**3 - 15*x**4 + 6*x**5)
    ds_x = sp.diff(s_x, x)
    d2s_x = sp.diff(s_x, x, 2)

    x_r = sp.simplify((r - (R - ell))/(2*ell))
    s_r = sp.simplify(s_x.subs(x, x_r))
    ds_r = sp.diff(s_r, r)
    d2s_r = sp.diff(s_r, r, 2)

    endpoint_values = {
        "s(0)": sp.simplify(s_x.subs(x, 0)),
        "s(1)": sp.simplify(s_x.subs(x, 1)),
        "s_x'(0)": sp.simplify(ds_x.subs(x, 0)),
        "s_x'(1)": sp.simplify(ds_x.subs(x, 1)),
        "s_x''(0)": sp.simplify(d2s_x.subs(x, 0)),
        "s_x''(1)": sp.simplify(d2s_x.subs(x, 1)),
        "s_r(R-ell)": sp.simplify(s_r.subs(r, R-ell)),
        "s_r(R+ell)": sp.simplify(s_r.subs(r, R+ell)),
        "s_r'(R-ell)": sp.simplify(ds_r.subs(r, R-ell)),
        "s_r'(R+ell)": sp.simplify(ds_r.subs(r, R+ell)),
        "s_r''(R-ell)": sp.simplify(d2s_r.subs(r, R-ell)),
        "s_r''(R+ell)": sp.simplify(d2s_r.subs(r, R+ell)),
    }

    print(f"x(r) = {x_r}")
    print(f"s(x) = {s_x}")
    print(f"s'(x) = {ds_x}")
    print(f"s''(x) = {d2s_x}")
    for key, value in endpoint_values.items():
        print(f"{key} = {value}")

    with out.derived_results():
        out.line("smoothstep", StatusMark.PASS, f"s(x)={s_x}")
        for key, value in endpoint_values.items():
            expected = 1 if key in {"s(1)", "s_r(R+ell)"} else 0
            ok = bool(sp.simplify(value - expected) == 0)
            out.line(key, StatusMark.PASS if ok else StatusMark.FAIL, f"{key}={value}")

    return {"r": r, "R": R, "ell": ell, "x": x, "x_r": x_r, "s_x": s_x, "s_r": s_r, "ds_r": ds_r, "d2s_r": d2s_r}


def record_s(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g57_s",
        inputs=[data["r"], data["R"], data["ell"]],
        output=data["s_r"],
        method="construct quintic smoothstep transition profile and verify endpoint behavior",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="layer_smoothstep_profile",
        scope="reduced finite-layer profile; not covariant theorem",
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

    data = case_smoothstep(out)

    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)
    record_s(ns, data)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
