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

SCRIPT_LABEL = 'Candidate Repair-Term Sieve'
MARKER_ID = 'g60_repair'
DEPENDENCIES = [('g59_summary', '059_transition_term_audit__candidate_group_59_status_summary', 'g59_summary'), ('g60_problem', '060_term_exclusion_sieve__candidate_sieve_problem', 'g60_problem')]
QUESTION = 'Do raw residues or counterterms survive as admissible transition terms?'
DISCIPLINE = 'This script rejects raw residue insertion and arbitrary counterterm repair. Residues remain clues only.'
OPENING_LINE = 'Repair-term exclusion sieve opened'
SCOPE = 'Group 60 repair sieve'
NEXT_SCRIPT = 'candidate_derivative_sieve.py'

ENTRIES = [('R1: raw residue insertion', 'R1/R2 as direct field-equation terms', 'REPAIR_TERM_REJECTED', 'raw residues are clues, not inserted terms', 'rejected'), ('R2: counterterm repair', 'choose coefficients to cancel a defect', 'REPAIR_TERM_REJECTED', 'counterterm-by-construction is not derivation', 'rejected'), ('R3: residue clue retention', 'R1/R2 can still guide candidate families', 'RESIDUE_CLUE_RETAINED', 'residues remain diagnostic', 'audit-only')]
SHORTCUTS = [('X1: R1/R2 insertion', 'insert blend residues directly', 'repair insertion is forbidden'), ('X2: arbitrary cancellation', 'choose C=-defect', 'not a field equation derivation'), ('X3: residue adoption', 'treat residue clues as adopted term', 'candidate surface only')]
OBLIGATIONS = [('O1: candidate construction discipline', 'POLICY_RULE', 'candidate terms must be independently filtered, not defined as repairs', 'avoid counterterm trap')]
LOCAL_CONCLUSIONS = [('repair terms rejected', 'REPAIR_TERM_REJECTED', 'raw residues and arbitrary counterterms do not survive'), ('residues retained as clues', 'RESIDUE_CLUE_RETAINED', 'R1/R2 can still guide filtered candidates')]


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
        "SIEVE_OPENED": StatusMark.INFO,
        "REPAIR_TERM_REJECTED": StatusMark.FAIL,
        "RESIDUE_CLUE_RETAINED": StatusMark.INFO,
        "DERIVATIVE_SIEVE_APPLIED": StatusMark.PASS,
        "DERIVATIVE_BURDEN_FOUND": StatusMark.OBLIGATION,
        "STRONG_LOCALITY_CONFIRMED": StatusMark.PASS,
        "WEIGHTED_NEUTRALITY_CONFIRMED": StatusMark.PASS,
        "SCALAR_CHARGE_TERM_REJECTED": StatusMark.FAIL,
        "STRESS_ONLY_INTERPRETATION_REQUIRED": StatusMark.OBLIGATION,
        "TUNING_ROUTE_REJECTED": StatusMark.FAIL,
        "SOURCE_CARRYING_TERM_REJECTED": StatusMark.FAIL,
        "TRACE_DOUBLE_COUNT_TERM_REJECTED": StatusMark.FAIL,
        "SOURCE_TRACE_SIEVE_APPLIED": StatusMark.PASS,
        "DIVERGENCE_FAILING_TERM_REJECTED": StatusMark.FAIL,
        "CLOSURE_SUPPORTED_TERM_SURVIVES": StatusMark.INFO,
        "ENERGY_ACCOUNTING_REQUIRED": StatusMark.OBLIGATION,
        "TERM_SURVIVES_NARROWLY": StatusMark.INFO,
        "COVARIANT_LIFT_REQUIRED": StatusMark.OBLIGATION,
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
        "REPAIR_TERM_REJECTED",
        "SCALAR_CHARGE_TERM_REJECTED",
        "TUNING_ROUTE_REJECTED",
        "SOURCE_CARRYING_TERM_REJECTED",
        "TRACE_DOUBLE_COUNT_TERM_REJECTED",
        "DIVERGENCE_FAILING_TERM_REJECTED",
        "REJECTED_ROUTE",
        "FORBIDDEN_SHORTCUT",
    }:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {
        "DERIVATIVE_BURDEN_FOUND",
        "STRESS_ONLY_INTERPRETATION_REQUIRED",
        "ENERGY_ACCOUNTING_REQUIRED",
        "COVARIANT_LIFT_REQUIRED",
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



def case_repair_sieve(out: ScriptOutput):
    header("Case 0: Repair and raw-residue insertion sieve")

    R1, R2, H, a, b = sp.symbols("R1 R2 H a b")
    raw_R1 = sp.simplify(H - R1)
    raw_R2 = sp.simplify(H - R2)
    counterterm = sp.simplify(H + a*R1 + b*R2)

    repair_conditions = sp.solve([sp.Eq(counterterm, 0)], [a], dict=True)

    print(f"raw R1 insertion residual H-R1 = {raw_R1}")
    print(f"raw R2 insertion residual H-R2 = {raw_R2}")
    print(f"counterterm H+aR1+bR2 = {counterterm}")
    print(f"formal solve for a in H+aR1+bR2=0: {repair_conditions}")

    with out.derived_results():
        out.line("raw R1 insertion", StatusMark.FAIL, f"H-R1={raw_R1}")
        out.line("raw R2 insertion", StatusMark.FAIL, f"H-R2={raw_R2}")
        out.line("counterterm form", StatusMark.FAIL, f"H+aR1+bR2={counterterm}")
        out.line("repair solve", StatusMark.INFO, f"formal repair requires choosing coefficients: {repair_conditions}")

    return {"raw_R1": raw_R1, "raw_R2": raw_R2, "counterterm": counterterm}


def record_repair(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g60_repair",
        inputs=[],
        output=data["counterterm"],
        method="classify raw residues/counterterms as repair forms, not admissible transition terms",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="repair_term_sieve",
        scope="candidate exclusion filter; no insertion",
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

    data = case_repair_sieve(out)

    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)
    record_repair(ns, data)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
