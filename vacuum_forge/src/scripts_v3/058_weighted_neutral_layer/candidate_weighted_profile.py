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

SCRIPT_LABEL = 'Candidate Weighted-Neutral Profile'
MARKER_ID = 'g58_profile'
DEPENDENCIES = [('g57_summary', '057_layer_unify_probe__candidate_group_57_status_summary', 'g57_summary'), ('g58_problem', '058_weighted_neutral_layer__candidate_weighted_problem', 'g58_problem')]
QUESTION = 'Can a localized nontrivial layer profile be made exactly neutral under spherical weighting?'
DISCIPLINE = 'This script constructs a windowed profile and solves for the geometric skew required by weighted neutrality. It does not make the profile physical source.'
OPENING_LINE = 'Weighted-neutral profile construction opened'
SCOPE = 'Group 58 weighted-neutral profile'
NEXT_SCRIPT = 'candidate_flat_vs_weighted.py'

ENTRIES = [('W1: localized window', 'w=(1-y^2)^2', 'LOCALIZED_LAYER_PROFILE_DERIVED', 'profile vanishes at layer endpoints', 'reduced layer'), ('W2: geometric skew', 'c=2Rell/(7R^2+ell^2)', 'GEOMETRIC_SKEW_DERIVED', 'spherical weighting requires a small asymmetric shift', 'not arbitrary tuning'), ('W3: weighted charge', 'integral (R+ell*y)^2 rho dy = 0', 'WEIGHTED_NEUTRALITY_CONFIRMED', 'weighted scalar charge vanishes exactly', 'reduced theorem surface'), ('W4: nontriviality', 'rho is not identically zero', 'WEIGHTED_NEUTRAL_PROFILE_DERIVED', 'silent layer can be internally nontrivial', 'not matter source')]
SHORTCUTS = [('X1: skew as arbitrary knob', 'treat c as free tuning', 'c is fixed by weighted neutrality'), ('X2: profile as source', 'treat rho as ordinary matter source', 'source safety remains required'), ('X3: neutrality as insertion', 'insert B_s/F_zeta because weighted charge is zero', 'weighted neutrality is not insertion')]
OBLIGATIONS = [('O1: energy audit', 'ENERGY_ACCOUNTING_REQUIRED', 'compute profile energy cost', 'avoid free neutral profile'), ('O2: source safety', 'SOURCE_SAFETY_REQUIRED', 'prove profile does not duplicate ordinary source load', 'avoid source leakage')]
LOCAL_CONCLUSIONS = [('weighted-neutral profile derived', 'PASS', 'nontrivial localized profile satisfies weighted charge zero exactly'), ('physical use blocked', 'NOT_INSERTABLE', 'profile is not insertion or source law')]


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



def case_weighted_profile(out: ScriptOutput):
    header("Case 0: Weighted-neutral localized layer profile")

    y, R, ell, rho0, c = sp.symbols("y R ell rho0 c", positive=True)
    r = sp.simplify(R + ell*y)
    w = sp.simplify((1 - y**2)**2)
    base = sp.simplify(w * (y - c))
    Q_base = sp.simplify(sp.integrate(r**2 * base, (y, -1, 1)))
    c_solution = sp.solve(sp.Eq(Q_base, 0), c)
    c_star = sp.simplify(c_solution[0])
    rho = sp.simplify(rho0 * w * (y - c_star))
    Q = sp.simplify(sp.integrate(r**2 * rho, (y, -1, 1)))
    left = sp.simplify(rho.subs(y, -1))
    right = sp.simplify(rho.subs(y, 1))
    center = sp.simplify(rho.subs(y, 0))
    sample = sp.simplify(rho.subs(y, sp.Rational(1, 2)))

    print(f"r(y) = {r}")
    print(f"w(y) = {w}")
    print(f"base profile = {base}")
    print(f"weighted charge before solve = {Q_base}")
    print(f"c* = {c_star}")
    print(f"rho_weighted(y) = {rho}")
    print(f"Q_weighted = {Q}")
    print(f"rho(-1) = {left}")
    print(f"rho(1) = {right}")
    print(f"rho(0) = {center}")
    print(f"rho(1/2) = {sample}")

    with out.derived_results():
        out.line("geometric skew", StatusMark.PASS, f"c={c_star}")
        out.line("weighted-neutral profile", StatusMark.PASS, f"rho={rho}")
        out.line("weighted charge", StatusMark.PASS if is_zero(Q) else StatusMark.FAIL, f"Q={Q}")
        out.line("left endpoint", StatusMark.PASS if is_zero(left) else StatusMark.FAIL, f"rho(-1)={left}")
        out.line("right endpoint", StatusMark.PASS if is_zero(right) else StatusMark.FAIL, f"rho(1)={right}")
        out.line("nontrivial center", StatusMark.PASS if not is_zero(center) else StatusMark.INFO, f"rho(0)={center}")
        out.line("nontrivial sample", StatusMark.PASS if not is_zero(sample) else StatusMark.INFO, f"rho(1/2)={sample}")

    return {
        "y": y,
        "R": R,
        "ell": ell,
        "rho0": rho0,
        "w": w,
        "c_star": c_star,
        "rho": rho,
        "Q": Q,
    }


def record_profile(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g58_profile",
        inputs=[data["y"], data["R"], data["ell"], data["rho0"]],
        output=data["rho"],
        method="construct rho=rho0*(1-y^2)^2*(y-c) with c solving weighted charge zero",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="weighted_neutral_layer_profile",
        scope="reduced finite-layer weighted neutrality; not physical source",
    )
    ns.record_derivation(
        derivation_id="g58_Q0",
        inputs=[data["rho"]],
        output=data["Q"],
        method="verify integral (R+ell*y)^2*rho(y) dy = 0",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="weighted_neutral_charge_zero",
        scope="reduced finite-layer charge diagnostic; not mass theorem",
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

    data = case_weighted_profile(out)

    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)
    record_profile(ns, data)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
