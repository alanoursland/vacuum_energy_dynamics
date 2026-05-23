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

SCRIPT_LABEL = 'Candidate Weighted Neutralizer'
MARKER_ID = 'g59_neu'
DEPENDENCIES = [('g58_summary', '58_weighted_neutral_layer__candidate_group_58_status_summary', 'g58_summary'), ('g59_problem', '59_transition_term_audit__candidate_transition_problem', 'g59_problem'), ('g59_inv', '59_transition_term_audit__candidate_residue_inventory', 'g59_inv'), ('g59_loc', '59_transition_term_audit__candidate_locality_filter', 'g59_loc')]
QUESTION = 'Can candidate scalar layer profiles be neutralized by a weighted rule that reproduces the Group 58 skew?'
DISCIPLINE = 'This script derives a reduced weighted-neutralization rule. It is not a covariant projection or insertion law.'
OPENING_LINE = 'Weighted-neutralization operator derivation opened'
SCOPE = 'Group 59 weighted neutralizer'
NEXT_SCRIPT = 'candidate_source_trace_filter.py'

ENTRIES = [('N1: neutralizer', 'N_w[f]=w*(f-mu_w[f])', 'WEIGHTED_NEUTRALIZER_DERIVED', 'candidate scalar profiles can be weighted-neutralized', 'reduced'), ('N2: weighted mean', 'mu_w[f]=int r^2*w*f / int r^2*w', 'WEIGHTED_NEUTRALIZER_DERIVED', 'neutrality condition fixes the subtraction', 'not arbitrary tuning'), ('N3: Group 58 recovery', 'mu_w[y]=2Rell/(7R^2+ell^2)', 'WEIGHTED_NEUTRALITY_CONFIRMED', 'neutralizer reproduces Group 58 skew', 'reduced'), ('N4: scalar charge', 'int r^2*N_w[y] dy=0', 'WEIGHTED_NEUTRALITY_CONFIRMED', 'neutralized basis is charge silent', 'not source safety')]
SHORTCUTS = [('X1: neutralizer as O', 'call N_w a full active no-overlap operator', 'it is only reduced scalar neutralization'), ('X2: neutralizer as insertion', 'insert N_w profile as field-equation term', 'not licensed'), ('X3: neutralized means source-safe', 'claim weighted charge zero proves source no-double-counting', 'source safety remains required')]
OBLIGATIONS = [('O1: source/trace filter', 'SOURCE_SAFETY_REQUIRED', 'test neutralized candidates against source and trace incidence', 'avoid hidden load'), ('O2: covariant lift', 'COVARIANT_LIFT_REQUIRED', 'lift weighted mean to geometric layer measure', 'avoid radial-only proof')]
LOCAL_CONCLUSIONS = [('weighted neutralizer derived', 'PASS', 'N_w reproduces Group 58 skew and zero weighted charge'), ('physical use blocked', 'NOT_INSERTABLE', 'neutralizer is not insertion')]


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



def case_weighted_neutralizer(out: ScriptOutput):
    header("Case 0: Weighted-neutralization operator")

    y, R, ell = sp.symbols("y R ell", positive=True)
    f = sp.Function("f")(y)
    r = sp.simplify(R + ell*y)
    w = sp.simplify((1 - y**2)**2)

    denom = sp.simplify(sp.integrate(r**2 * w, (y, -1, 1)))

    # Explicit f=y case recovers Group 58 skew.
    f_y = y
    mu_y = sp.simplify(sp.integrate(r**2 * w * f_y, (y, -1, 1)) / denom)
    N_y = sp.simplify(w * (f_y - mu_y))
    Q_N_y = sp.simplify(sp.integrate(r**2 * N_y, (y, -1, 1)))

    # Explicit f=1 case neutralizes to zero; useful rejected/degenerated case.
    f_1 = sp.Integer(1)
    mu_1 = sp.simplify(sp.integrate(r**2 * w * f_1, (y, -1, 1)) / denom)
    N_1 = sp.simplify(w * (f_1 - mu_1))
    Q_N_1 = sp.simplify(sp.integrate(r**2 * N_1, (y, -1, 1)))

    print(f"denom = {denom}")
    print("General operator:")
    print("  N_w[f] = w*(f - mu_w[f])")
    print("  mu_w[f] = integral r^2*w*f dy / integral r^2*w dy")
    print(f"mu_w[y] = {mu_y}")
    print(f"N_w[y] = {N_y}")
    print(f"Q[N_w[y]] = {Q_N_y}")
    print(f"mu_w[1] = {mu_1}")
    print(f"N_w[1] = {N_1}")
    print(f"Q[N_w[1]] = {Q_N_1}")

    with out.derived_results():
        out.line("weighted denominator", StatusMark.PASS, f"denom={denom}")
        out.line("mu_y", StatusMark.PASS, f"mu_w[y]={mu_y}")
        out.line("neutralized y", StatusMark.PASS, f"N_y={N_y}")
        out.line("charge of N_y", StatusMark.PASS if is_zero(Q_N_y) else StatusMark.FAIL, f"Q={Q_N_y}")
        out.line("constant degeneracy", StatusMark.INFO if is_zero(N_1) else StatusMark.PASS, f"N_1={N_1}")

    return {"y": y, "R": R, "ell": ell, "w": w, "denom": denom, "mu_y": mu_y, "N_y": N_y, "Q_N_y": Q_N_y}


def record_neu(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g59_neu",
        inputs=[data["y"], data["R"], data["ell"]],
        output=data["N_y"],
        method="derive weighted-neutralization operator N_w[f]=w(f-mu_w[f]) and verify f=y case",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="weighted_neutralizer",
        scope="reduced layer neutralization operator; not covariant projection",
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

    data = case_weighted_neutralizer(out)

    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)
    record_neu(ns, data)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
