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

# Group:
#   52_residual_source_boundary_safety_load_testing
#
# Script type:
#   GOVERNANCE / DIAGNOSTIC

SCRIPT_LABEL = 'Candidate A-Sector Mass Protection Audit'
MARKER_ID = 'g52_a_mass_protection'
DEPENDENCIES = [('g51_summary', '051_trace_normalization_adopt_defer_reject_decision_surface__candidate_group_51_status_summary', 'g51_summary'), ('g52_problem', '052_residual_source_boundary_safety_load_testing__candidate_safety_load_test_problem', 'g52_problem'), ('g52_source_matrix', '052_residual_source_boundary_safety_load_testing__candidate_source_no_double_counting_matrix', 'g52_source_matrix')]
QUESTION = 'Does retaining the trace-normalization candidate threaten the protected reduced A-sector mass coin?'
DISCIPLINE = 'This script protects the reduced A-sector mass result by auditing independent scalar trace charge. It does not derive a full covariant mass theorem.'
OPENING_LINE = 'A-sector mass protection audit opened -- protect reduced mass coin'
SCOPE = 'Group 52 A-sector mass protection audit'
NEXT_SCRIPT = 'candidate_boundary_scalar_silence_dependency_audit.py'

ENTRIES = [('A1: reduced mass coin', 'F_A and M_A recover M in the reduced static spherical A-sector', 'A_SECTOR_MASS_COIN_PROTECTED', 'this remains the protected ordinary exterior mass reference', 'not covariant mass theorem'), ('A2: extra scalar charge risk', 'an independent trace charge would shift the effective mass unless neutralized', 'A_SECTOR_MASS_PROTECTION_REQUIRED', 'Q_trace must vanish, be inert, or be otherwise forbidden', 'not solved here'), ('A3: no B_s mass duplicate', 'B_s, zeta, kappa, residual variables, and boundary terms must not become independent mass channels', 'SOURCE_NO_DOUBLE_COUNTING_REQUIRED', 'trace normalization cannot carry ordinary mass charge by record status', 'not insertion')]
SHORTCUTS = [('X1: trace charge as mass support', 'let zeta or B_s carry an independent long-range mass charge', 'that duplicates the protected A-sector mass coin'), ('X2: boundary mass patch', 'shift M_ext through trace-normalization boundary terms', 'boundary mass neutrality must be derived'), ('X3: reduced mass as parent mass', 'treat M_A as final covariant mass theorem', 'it is a reduced exterior audit object')]
OBLIGATIONS = [('O1: A-sector mass protection theorem', 'A_SECTOR_MASS_PROTECTION_REQUIRED', 'prove scalar trace candidates do not duplicate or shift M_A', 'protect strongest reduced result'), ('O2: scalar charge neutrality', 'SAFETY_THEOREMS_REQUIRED', 'show any trace-sector charge is zero, inert, or non-mass-carrying outside A-sector', 'avoid extra scalar mass')]
LOCAL_CONCLUSIONS = [('A-sector mass audit complete', 'PASS', 'reduced A-sector mass coin preserved as reference'), ('extra scalar charge remains forbidden unless neutralized', 'A_SECTOR_MASS_PROTECTION_REQUIRED', 'trace-sector mass shifts remain safety burden')]


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
        "SAFETY_LOAD_TEST_SURFACE_OPENED": StatusMark.INFO,
        "COUNT_ONCE_TRACE_BURDEN_EXPLICIT": StatusMark.OBLIGATION,
        "TRACE_INCIDENCE_DIAGNOSTIC": StatusMark.INFO,
        "RESIDUAL_NONENTRY_THEOREM_REQUIRED": StatusMark.OBLIGATION,
        "RESIDUAL_ENTRY_REJECTED": StatusMark.FAIL,
        "SOURCE_NO_DOUBLE_COUNTING_REQUIRED": StatusMark.OBLIGATION,
        "SOURCE_DUPLICATION_WITNESS": StatusMark.FAIL,
        "A_SECTOR_MASS_PROTECTION_REQUIRED": StatusMark.OBLIGATION,
        "A_SECTOR_MASS_COIN_PROTECTED": StatusMark.INFO,
        "BOUNDARY_SCALAR_SILENCE_REQUIRED": StatusMark.OBLIGATION,
        "SCALAR_TAIL_WITNESS": StatusMark.FAIL,
        "CANDIDATE_SURVIVES_AS_AUDIT_ONLY": StatusMark.INFO,
        "CANDIDATE_BLOCKED_FOR_PHYSICAL_USE": StatusMark.DEFER,
        "THEOREM_TARGET_REFINED": StatusMark.DEFER,
        "OBSTRUCTION_WITNESS_FOUND": StatusMark.FAIL,
        "DEFERRED_WITH_TARGET": StatusMark.DEFER,
        "NOT_INSERTABLE": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "THEORY_DECISION_REQUIRED": StatusMark.DEFER,
        "CHOICE_REQUIRED": StatusMark.DEFER,
        "NUMERIC_D_CONDITION": StatusMark.OBLIGATION,
        "SAFETY_THEOREMS_REQUIRED": StatusMark.OBLIGATION,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REJECTED_ROUTE": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
        "OPEN": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def governance_status(status: str) -> GovernanceStatus:
    if status in {
        "REJECTED_ROUTE",
        "FORBIDDEN_SHORTCUT",
        "RESIDUAL_ENTRY_REJECTED",
        "SOURCE_DUPLICATION_WITNESS",
        "SCALAR_TAIL_WITNESS",
        "OBSTRUCTION_WITNESS_FOUND",
    }:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {
        "POLICY_RULE",
        "SAFETY_THEOREMS_REQUIRED",
        "COUNT_ONCE_TRACE_BURDEN_EXPLICIT",
        "RESIDUAL_NONENTRY_THEOREM_REQUIRED",
        "SOURCE_NO_DOUBLE_COUNTING_REQUIRED",
        "A_SECTOR_MASS_PROTECTION_REQUIRED",
        "BOUNDARY_SCALAR_SILENCE_REQUIRED",
        "NUMERIC_D_CONDITION",
    }:
        return GovernanceStatus.POLICY_RULE
    return GovernanceStatus.UNVERIFIED


def obligation_status(status: str) -> ObligationStatus:
    if status in {
        "DEFERRED_WITH_TARGET",
        "NOT_INSERTABLE",
        "NOT_ADOPTED",
        "THEORY_DECISION_REQUIRED",
        "CHOICE_REQUIRED",
        "CANDIDATE_BLOCKED_FOR_PHYSICAL_USE",
        "THEOREM_TARGET_REFINED",
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
        record_claim(
            ns,
            f"{marker_id}_c{idx}",
            marker_id,
            item.status,
            f"{item.name}: {item.subject}. {item.detail}. Boundary: {item.boundary}.",
        )
    for idx, item in enumerate(obligations, 1):
        record_obligation(
            ns,
            f"{marker_id}_o{idx}",
            item.name,
            f"{item.obligation}. Discipline: {item.discipline}.",
            item.status,
        )


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



def case_a_sector_mass_coin(out: ScriptOutput):
    header("Case 0: Reduced A-sector mass coin and extra scalar charge diagnostic")

    G, c, M, r, Q_trace = sp.symbols("G c M r Q_trace", nonzero=True)
    A_ext = 1 - 2 * G * M / (c**2 * r)
    A_prime = sp.diff(A_ext, r)
    F_A = sp.simplify(4 * sp.pi * r**2 * A_prime)
    M_A = sp.simplify(c**2 * F_A / (8 * sp.pi * G))
    mass_residual = sp.simplify(M_A - M)
    M_effective = sp.simplify(M_A + Q_trace)
    extra_charge_residual = sp.simplify(M_effective - M)

    print(f"A_ext = {A_ext}")
    print(f"A' = {A_prime}")
    print(f"F_A = 4*pi*r^2*A' = {F_A}")
    print(f"M_A = c^2 F_A/(8*pi*G) = {M_A}")
    print(f"M_A - M = {mass_residual}")
    print()
    print(f"If an independent scalar trace charge Q_trace is added:")
    print(f"M_effective = {M_effective}")
    print(f"M_effective - M = {extra_charge_residual}")

    with out.derived_results():
        out.line(
            "reduced A-sector mass coin recovers M",
            StatusMark.PASS if is_zero(mass_residual) else StatusMark.FAIL,
            f"M_A - M = {mass_residual}",
        )
        out.line(
            "extra scalar charge witness",
            StatusMark.FAIL if not is_zero(extra_charge_residual) else StatusMark.PASS,
            f"M_effective - M = {extra_charge_residual}",
        )

    return {
        "G": G,
        "c": c,
        "M": M,
        "r": r,
        "Q_trace": Q_trace,
        "A_ext": A_ext,
        "F_A": F_A,
        "M_A": M_A,
        "mass_residual": mass_residual,
        "extra_charge_residual": extra_charge_residual,
    }


def record_mass_coin(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g52_a_sector_mass_coin_residual",
        inputs=[data["A_ext"], data["G"], data["c"], data["M"], data["r"]],
        output=data["mass_residual"],
        method="compute F_A=4*pi*r^2*A' and M_A=c^2*F_A/(8*pi*G), then simplify M_A-M",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="mass_coin_residual",
        scope="reduced static spherical A-sector diagnostic",
    )
    ns.record_derivation(
        derivation_id="g52_extra_scalar_charge_mass_shift_witness",
        inputs=[data["M_A"], data["Q_trace"], data["M"]],
        output=data["extra_charge_residual"],
        method="add independent scalar trace charge Q_trace to M_A",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="obstruction_witness",
        scope="diagnostic mass-shift witness; not a boundary theorem",
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

    data = case_a_sector_mass_coin(out)

    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)
    record_mass_coin(ns, data)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
