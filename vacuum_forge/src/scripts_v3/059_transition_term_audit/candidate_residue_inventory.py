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

SCRIPT_LABEL = 'Candidate Residue Inventory'
MARKER_ID = 'g59_inv'
DEPENDENCIES = [('g58_summary', '58_weighted_neutral_layer__candidate_group_58_status_summary', 'g58_summary'), ('g59_problem', '59_transition_term_audit__candidate_transition_problem', 'g59_problem')]
QUESTION = 'What candidate ingredients are available from blend residues and the weighted-neutral layer shape?'
DISCIPLINE = 'This script inventories transition-term ingredients. It does not adopt or insert them.'
OPENING_LINE = 'Transition residue inventory opened'
SCOPE = 'Group 59 residue inventory'
NEXT_SCRIPT = 'candidate_locality_filter.py'

ENTRIES = [('I1: first residue', "R1=(F_out-F_in)s'", 'RESIDUE_INVENTORY_DERIVED', 'first derivative transition mismatch is a candidate clue', 'not inserted'), ('I2: second residue', "R2=(F_out-F_in)s''+2(F_out'-F_in')s'", 'RESIDUE_INVENTORY_DERIVED', 'second derivative transition mismatch is a candidate clue', 'not parent equation'), ('I3: weighted-neutral shape', 'eta=w(y)*(y-c*)', 'WEIGHTED_NEUTRALITY_CONFIRMED', 'Group 58 shape can seed neutral candidate terms', 'reduced'), ('I4: stress basis', 'eta^2', 'CANDIDATE_TERM_SURFACE_OPENED', 'stress-like positive layer basis can be filtered', 'not stress tensor')]
SHORTCUTS = [('X1: residue as equation', 'treat R1/R2 as inserted equation terms', 'inventory is not insertion'), ('X2: eta as source', 'treat eta as ordinary matter source', 'source safety remains required'), ('X3: eta^2 as stress tensor', 'promote eta^2 to stress tensor without divergence/covariant checks', 'filters remain required')]
OBLIGATIONS = [('O1: locality filter', 'POLICY_RULE', 'test endpoint locality of inventory terms', 'avoid layer leakage'), ('O2: weighted neutrality filter', 'POLICY_RULE', 'test scalar-charge status of candidate terms', 'avoid exterior tail')]
LOCAL_CONCLUSIONS = [('inventory derived', 'PASS', 'transition residue and weighted layer bases available for filters'), ('physical use blocked', 'NOT_INSERTABLE', 'inventory is not insertion')]


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



def case_residue_inventory(out: ScriptOutput):
    header("Case 0: Transition residue and basis inventory")

    r, y, R, ell = sp.symbols("r y R ell", positive=True)
    s = sp.Function("s")(r)
    F_in = sp.Function("F_in")(r)
    F_out = sp.Function("F_out")(r)

    R1 = sp.simplify((F_out - F_in) * sp.diff(s, r))
    R2 = sp.simplify((F_out - F_in) * sp.diff(s, r, 2) + 2*(sp.diff(F_out, r) - sp.diff(F_in, r))*sp.diff(s, r))

    w = sp.simplify((1 - y**2)**2)
    c_star = sp.simplify(2*R*ell/(7*R**2 + ell**2))
    eta = sp.simplify(w * (y - c_star))
    stress_basis = sp.simplify(eta**2)

    print(f"R1 = {R1}")
    print(f"R2 = {R2}")
    print(f"w(y) = {w}")
    print(f"eta(y) = {eta}")
    print(f"stress_basis = {stress_basis}")

    with out.derived_results():
        out.line("R1 residue", StatusMark.PASS, f"R1={R1}")
        out.line("R2 residue", StatusMark.PASS, f"R2={R2}")
        out.line("weighted-neutral eta", StatusMark.PASS, f"eta={eta}")
        out.line("stress basis", StatusMark.PASS, f"eta^2={stress_basis}")

    return {"r": r, "y": y, "R": R, "ell": ell, "R1": R1, "R2": R2, "w": w, "eta": eta, "stress_basis": stress_basis}


def record_inv(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g59_inv",
        inputs=[data["r"], data["y"], data["R"], data["ell"]],
        output=data["eta"],
        method="inventory blend residues R1/R2 and weighted-neutral layer basis eta",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="transition_candidate_inventory",
        scope="candidate transition-term inventory; not insertion",
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

    data = case_residue_inventory(out)

    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)
    record_inv(ns, data)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
