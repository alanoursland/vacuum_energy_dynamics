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

SCRIPT_LABEL = 'Candidate Weighted Layer Divergence'
MARKER_ID = 'g58_div'
DEPENDENCIES = [('g57_summary', '57_layer_unify_probe__candidate_group_57_status_summary', 'g57_summary'), ('g58_problem', '58_weighted_neutral_layer__candidate_weighted_problem', 'g58_problem'), ('g58_profile', '58_weighted_neutral_layer__candidate_weighted_profile', 'g58_profile'), ('g58_tailmass', '58_weighted_neutral_layer__candidate_tail_mass_zero', 'g58_tailmass')]
QUESTION = 'Can the weighted-neutral layer shape support reduced divergence-silent closure?'
DISCIPLINE = 'This script constructs a reduced divergence-silent closure using the weighted-neutral layer shape. It is not a covariant Bianchi proof.'
OPENING_LINE = 'Weighted-neutral layer divergence closure opened'
SCOPE = 'Group 58 weighted layer divergence'
NEXT_SCRIPT = 'candidate_weighted_route_classifier.py'

ENTRIES = [('D1: weighted shape stress', 'p_r proportional to weighted-neutral shape squared', 'WEIGHTED_DIVERGENCE_CLOSURE_DERIVED', 'stress is localized to layer', 'reduced'), ('D2: tangential closure', "p_t=p_r+r*p_r'/2", 'WEIGHTED_DIVERGENCE_CLOSURE_DERIVED', 'closure cancels reduced radial divergence', 'not covariant'), ('D3: divergence diagnostic', 'D=0', 'WEIGHTED_DIVERGENCE_CLOSURE_DERIVED', 'weighted-neutral layer can be reduced-divergence silent', 'not Bianchi proof'), ('D4: endpoint stress', 'p_r and p_t vanish at endpoints', 'LOCALIZED_LAYER_PROFILE_DERIVED', 'no endpoint stress leak in reduced diagnostic', 'not full boundary theorem')]
SHORTCUTS = [('X1: D=0 as Bianchi proof', 'treat reduced divergence as covariant identity', 'covariant lift remains required'), ('X2: stress closure as insertion', 'insert closure into parent equation', 'not licensed'), ('X3: divergence as source safety', 'claim D=0 proves no source duplication', 'source safety remains separate')]
OBLIGATIONS = [('O1: covariant divergence lift', 'DIVERGENCE_IDENTITY_REQUIRED', 'lift reduced D=0 to covariant identity structure', 'avoid parent overclaim'), ('O2: candidate term audit', 'DEFERRED_WITH_TARGET', 'audit whether weighted layer stress is admissible candidate transition term', 'avoid repair insertion')]
LOCAL_CONCLUSIONS = [('weighted divergence closure derived', 'PASS', 'weighted-neutral layer shape supports reduced D=0 closure'), ('physical use blocked', 'NOT_INSERTABLE', 'divergence closure is not parent equation')]


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



def case_weighted_divergence(out: ScriptOutput):
    header("Case 0: Weighted-neutral layer divergence closure")

    y, R, ell, p0 = sp.symbols("y R ell p0", positive=True)
    r = sp.simplify(R + ell*y)
    c_star = sp.simplify(2*R*ell/(7*R**2 + ell**2))
    w = sp.simplify((1 - y**2)**2)
    shape = sp.simplify(w * (y - c_star))
    p_r_y = sp.simplify(p0 * shape**2)
    dp_dr = sp.simplify(sp.diff(p_r_y, y) / ell)
    p_t = sp.simplify(p_r_y + r * dp_dr / 2)
    D = sp.simplify(dp_dr + 2*(p_r_y - p_t)/r)
    left_pr = sp.simplify(p_r_y.subs(y, -1))
    right_pr = sp.simplify(p_r_y.subs(y, 1))
    left_pt = sp.simplify(p_t.subs(y, -1))
    right_pt = sp.simplify(p_t.subs(y, 1))

    print(f"shape = {shape}")
    print(f"p_r = {p_r_y}")
    print(f"p_t = {p_t}")
    print(f"D = {D}")
    print(f"p_r(-1) = {left_pr}")
    print(f"p_r(1) = {right_pr}")
    print(f"p_t(-1) = {left_pt}")
    print(f"p_t(1) = {right_pt}")

    with out.derived_results():
        out.line("weighted shape", StatusMark.PASS, f"shape={shape}")
        out.line("radial pressure", StatusMark.PASS, f"p_r={p_r_y}")
        out.line("tangential closure", StatusMark.PASS, f"p_t={p_t}")
        out.line("divergence", StatusMark.PASS if is_zero(D) else StatusMark.FAIL, f"D={D}")
        out.line("left p_r", StatusMark.PASS if is_zero(left_pr) else StatusMark.FAIL, f"p_r(-1)={left_pr}")
        out.line("right p_r", StatusMark.PASS if is_zero(right_pr) else StatusMark.FAIL, f"p_r(1)={right_pr}")
        out.line("left p_t", StatusMark.PASS if is_zero(left_pt) else StatusMark.FAIL, f"p_t(-1)={left_pt}")
        out.line("right p_t", StatusMark.PASS if is_zero(right_pt) else StatusMark.FAIL, f"p_t(1)={right_pt}")

    return {"y": y, "R": R, "ell": ell, "p_r": p_r_y, "p_t": p_t, "D": D}


def record_div(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g58_div",
        inputs=[data["y"], data["R"], data["ell"]],
        output=data["D"],
        method="construct divergence closure from weighted-neutral layer shape",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="weighted_layer_divergence_closure",
        scope="reduced layer divergence diagnostic; not covariant Bianchi proof",
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

    data = case_weighted_divergence(out)

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
