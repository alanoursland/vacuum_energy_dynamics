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

SCRIPT_LABEL = 'Candidate Term Sieve Classifier'
MARKER_ID = 'g60_class'
DEPENDENCIES = [('g59_summary', '059_transition_term_audit__candidate_group_59_status_summary', 'g59_summary'), ('g60_problem', '060_term_exclusion_sieve__candidate_sieve_problem', 'g60_problem'), ('g60_repair', '060_term_exclusion_sieve__candidate_repair_sieve', 'g60_repair'), ('g60_der', '060_term_exclusion_sieve__candidate_derivative_sieve', 'g60_der'), ('g60_neu', '060_term_exclusion_sieve__candidate_neutrality_sieve', 'g60_neu'), ('g60_tune', '060_term_exclusion_sieve__candidate_tuning_sieve', 'g60_tune'), ('g60_src', '060_term_exclusion_sieve__candidate_source_trace_sieve', 'g60_src'), ('g60_div', '060_term_exclusion_sieve__candidate_div_energy_sieve', 'g60_div')]
QUESTION = 'After stricter repair, derivative, neutrality, tuning, source/trace, divergence, and energy filters, what survives?'
DISCIPLINE = 'This classifier reports Group 60 survivor status without upgrading it to insertion.'
OPENING_LINE = 'Term exclusion sieve classifier opened'
SCOPE = 'Group 60 sieve classifier'
NEXT_SCRIPT = 'candidate_sieve_reconcile.py'

ENTRIES = [('C1: repair rejection', 'raw residue/counterterm forms rejected', 'REPAIR_TERM_REJECTED', 'R1/R2 remain clues only', 'not inserted'), ('C2: derivative narrowing', 'eta has second-derivative endpoint burden; eta^2 stronger', 'DERIVATIVE_BURDEN_FOUND', 'scalar route narrowed toward stress-like route', 'reduced'), ('C3: scalar neutrality', 'eta neutral; eta^2 not neutral as scalar', 'SCALAR_CHARGE_TERM_REJECTED', 'eta^2 cannot be scalar response', 'rejected as scalar'), ('C4: stress-only route', 'eta^2 may survive only as stress-like closure basis', 'STRESS_ONLY_INTERPRETATION_REQUIRED', 'interpretation narrowed', 'conditional'), ('C5: tuning', 'constant admixture rejected', 'TUNING_ROUTE_REJECTED', 'bad bases cannot survive by zero coefficient', 'rejected'), ('C6: source/trace', 'source repair/carrying and trace double-count rejected', 'SOURCE_TRACE_SIEVE_APPLIED', 'incidence guardrails preserved', 'not theorem'), ('C7: divergence/energy', 'radial-only rejected; closure route survives with energy burden', 'CLOSURE_SUPPORTED_TERM_SURVIVES', 'reduced D=0 route remains conditional', 'not Bianchi'), ('C8: narrowed survivor', 'stress-only localized weighted-neutral-generated closure-supported response', 'TERM_SURVIVES_NARROWLY', 'survives only as audit candidate', 'not insertable'), ('C9: physical use', 'candidate remains blocked', 'PHYSICAL_USE_BLOCKED', 'no insertion, active O, recombination, or parent closure', 'not parent-ready')]
SHORTCUTS = [('X1: raw residue repair', 'insert R1/R2 or counterterm', 'rejected'), ('X2: eta^2 scalar source', 'use eta^2 as scalar charge/source profile', 'weighted charge is nonzero'), ('X3: tuned constant', 'keep constant term with coefficient forced to zero', 'rejected'), ('X4: source repair', 'transition response repairs/replaces A-sector source', 'rejected'), ('X5: trace reentry', 'transition response adds trace count', 'rejected'), ('X6: radial-only stress', 'omit tangential closure', 'rejected'), ('X7: active O by disguise', 'promote N_w to active O', 'not licensed')]
OBLIGATIONS = [('O1: source safety', 'SOURCE_SAFETY_REQUIRED', 'prove surviving stress-only transition response does not duplicate ordinary source load', 'protect A-sector'), ('O2: covariant lift', 'COVARIANT_LIFT_REQUIRED', 'lift locality/neutralizer/closure to geometric layer formalism', 'avoid radial-only proof'), ('O3: divergence identity', 'DIVERGENCE_IDENTITY_REQUIRED', 'lift reduced D=0 closure to covariant identity', 'avoid parent overclaim'), ('O4: energy/stress accounting', 'ENERGY_ACCOUNTING_REQUIRED', 'derive admissible energy/stress role', 'avoid free response'), ('O5: physical use blocked', 'NOT_INSERTABLE', 'keep insertion, active O, recombination, and parent closure closed', 'avoid status inflation')]
LOCAL_CONCLUSIONS = [('term sieve classified', 'PASS', 'candidate survived only in narrower stress-only closure-supported form'), ('bad families rejected', 'REJECTED_ROUTE', 'repair, scalar-charge, tuning, source/trace, and radial-only routes rejected'), ('physical use remains blocked', 'PHYSICAL_USE_BLOCKED', 'no insertion or parent closure opened')]


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


    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
