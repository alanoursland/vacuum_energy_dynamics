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

SCRIPT_LABEL = 'Candidate Quadratic Scalar Origin'
MARKER_ID = 'g64_quad'
DEPENDENCIES = [('g63_summary', '063_obstruction_decision__candidate_group_63_status_summary', 'g63_summary'), ('g64_problem', '064_variational_stress_origin__candidate_variational_problem', 'g64_problem'), ('g64_req', '064_variational_stress_origin__candidate_functional_requirements', 'g64_req')]
QUESTION = 'Can eta arise as a stationary profile of a simple constant-coefficient quadratic scalar functional?'
DISCIPLINE = "This script tests the necessary condition f''=k f with constant k."
OPENING_LINE = 'Quadratic scalar origin test opened'
SCOPE = 'Group 64 quadratic scalar origin'
NEXT_SCRIPT = 'candidate_linear_closure_origin.py'

ENTRIES = [('Q1: simple EL test', "f''=k f", 'QUADRATIC_ORIGIN_REJECTED', 'eta does not pass the constant-k ratio test', 'rejected simple origin'), ('Q2: ratio obstruction', "f''/f not constant", 'EL_RATIO_NOT_CONSTANT', 'constant-coefficient quadratic origin is unavailable', 'reduced witness'), ('Q3: more complex origin', 'variable coefficient or nonlinear functional', 'DEFERRED_WITH_TARGET', 'not ruled out by this simple test', 'future route')]
SHORTCUTS = [('X1: endpoint silence as EL', 'use boundary behavior as full variational origin', 'interior Euler equation fails simple test'), ('X2: pick k locally', 'choose k at one point', 'constant-k must hold globally'), ('X3: reject all variational origins', 'overgeneralize simple-origin failure', 'only simple constant-coeff route was tested')]
OBLIGATIONS = [('O1: stronger origin if retained', 'ENERGY_ACCOUNTING_REQUIRED', 'derive variable-coefficient/nonlinear/tensor principle if candidate remains live', 'avoid simple-origin overclaim')]
LOCAL_CONCLUSIONS = [('quadratic origin rejected', 'QUADRATIC_ORIGIN_REJECTED', 'simple constant-coefficient scalar functional does not derive eta'), ('retention weakened', 'CONDITIONAL_AUDIT_RETENTION_WEAKENED', 'one plausible origin route failed')]


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
        "VARIATIONAL_ORIGIN_OPENED": StatusMark.INFO,
        "REQUIREMENTS_RESTATED": StatusMark.PASS,
        "QUADRATIC_ORIGIN_REJECTED": StatusMark.FAIL,
        "EL_RATIO_NOT_CONSTANT": StatusMark.OBLIGATION,
        "LINEAR_CLOSURE_TESTED": StatusMark.PASS,
        "TRACE_MASS_TENSION_REPRODUCED": StatusMark.OBLIGATION,
        "AMPLITUDE_UNDERIVED": StatusMark.OBLIGATION,
        "AMPLITUDE_REPAIR_REJECTED": StatusMark.FAIL,
        "SOURCE_COUPLING_REJECTED": StatusMark.FAIL,
        "ZERO_RESPONSE_REJECTED_AS_TRIVIAL": StatusMark.FAIL,
        "NORMALIZATION_NOT_ORIGIN": StatusMark.OBLIGATION,
        "BOUNDARY_VARIATION_TESTED": StatusMark.PASS,
        "BOUNDARY_SILENCE_NOT_ORIGIN": StatusMark.OBLIGATION,
        "SIMPLE_ORIGIN_FAILED": StatusMark.FAIL,
        "DIAGNOSTIC_DOWNGRADE_STRENGTHENED": StatusMark.INFO,
        "CONDITIONAL_AUDIT_RETENTION_WEAKENED": StatusMark.DEFER,
        "RETENTION_CONTRACT_REQUIRED": StatusMark.OBLIGATION,
        "STRESS_ACCOUNTING_NOT_CLOSED": StatusMark.OBLIGATION,
        "AUDIT_CANDIDATE_RETAINED": StatusMark.INFO,
        "DIAGNOSTIC_ONLY_DOWNGRADE_POSSIBLE": StatusMark.DEFER,
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
        "QUADRATIC_ORIGIN_REJECTED",
        "AMPLITUDE_REPAIR_REJECTED",
        "SOURCE_COUPLING_REJECTED",
        "ZERO_RESPONSE_REJECTED_AS_TRIVIAL",
        "SIMPLE_ORIGIN_FAILED",
        "REJECTED_ROUTE",
        "FORBIDDEN_SHORTCUT",
    }:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {
        "EL_RATIO_NOT_CONSTANT",
        "TRACE_MASS_TENSION_REPRODUCED",
        "AMPLITUDE_UNDERIVED",
        "NORMALIZATION_NOT_ORIGIN",
        "BOUNDARY_SILENCE_NOT_ORIGIN",
        "RETENTION_CONTRACT_REQUIRED",
        "STRESS_ACCOUNTING_NOT_CLOSED",
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
        "DIAGNOSTIC_ONLY_DOWNGRADE_POSSIBLE",
        "CONDITIONAL_AUDIT_RETENTION_WEAKENED",
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


def layer_symbols():
    y, R, ell, p0 = sp.symbols("y R ell p0", positive=True)
    c = sp.simplify(2*R*ell/(7*R**2 + ell**2))
    eta = sp.simplify((1 - y**2)**2 * (y - c))
    r = sp.simplify(R + ell*y)
    p_r = sp.simplify(p0 * eta**2)
    dp_dr = sp.simplify(sp.diff(p_r, y) / ell)
    p_t = sp.simplify(p_r + r*dp_dr/2)
    P = sp.simplify(p_r + 2*p_t)
    return y, R, ell, p0, r, eta, p_r, p_t, P



def case_quadratic_scalar_origin(out: ScriptOutput):
    header("Case 0: Constant-coefficient quadratic scalar origin")

    y, R, ell, p0, r, eta, p_r, p_t, P = layer_symbols()
    k = sp.symbols("k")

    f = eta
    f2 = sp.diff(f, y, 2)
    residual = sp.simplify(f2 - k*f)

    # If f solves f'' = k f with constant k, f''/f must be same at two interior points.
    ratio0 = sp.simplify(f2.subs(y, 0) / f.subs(y, 0))
    ratio_half = sp.simplify(f2.subs(y, sp.Rational(1, 2)) / f.subs(y, sp.Rational(1, 2)))
    diff = sp.simplify(ratio0 - ratio_half)

    print(f"eta = {f}")
    print(f"f'' - k f = {sp.factor(residual)}")
    print(f"(f''/f)(0) = {sp.factor(ratio0)}")
    print(f"(f''/f)(1/2) = {sp.factor(ratio_half)}")
    print(f"difference = {sp.factor(diff)}")

    with out.derived_results():
        out.line("Euler residual", StatusMark.OBLIGATION, f"{sp.factor(residual)}")
        out.line("ratio at 0", StatusMark.INFO, f"{sp.factor(ratio0)}")
        out.line("ratio at 1/2", StatusMark.INFO, f"{sp.factor(ratio_half)}")
        out.line("ratio difference", StatusMark.FAIL if not is_zero(diff) else StatusMark.PASS, f"{sp.factor(diff)}")

    return {"y": y, "R": R, "ell": ell, "eta": eta, "ratio_diff": diff}


def record_quad(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g64_quad",
        inputs=[data["y"], data["R"], data["ell"]],
        output=data["ratio_diff"],
        method="test whether eta can solve f''=k f for constant k by comparing f''/f at two interior points",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="quadratic_scalar_origin_sieve",
        scope="reduced constant-coefficient Euler-Lagrange test; not full variational theorem",
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

    data = case_quadratic_scalar_origin(out)

    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)
    record_quad(ns, data)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
