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
SCRIPT_LABEL = "Candidate Group 64 Status Summary"
MARKER_ID = "g64_summary"

DEPENDENCIES = [
    ("g63_summary", "63_obstruction_decision__candidate_group_63_status_summary", "g63_summary"),
    ("g64_problem", "64_variational_stress_origin__candidate_variational_problem", "g64_problem"),
    ("g64_req", "64_variational_stress_origin__candidate_functional_requirements", "g64_req"),
    ("g64_quad", "64_variational_stress_origin__candidate_quadratic_scalar_origin", "g64_quad"),
    ("g64_lin", "64_variational_stress_origin__candidate_linear_closure_origin", "g64_lin"),
    ("g64_amp", "64_variational_stress_origin__candidate_amplitude_origin_scale", "g64_amp"),
    ("g64_bdy", "64_variational_stress_origin__candidate_boundary_variation_sieve", "g64_bdy"),
    ("g64_class", "64_variational_stress_origin__candidate_variational_route_classifier", "g64_class"),
    ("g64_reconcile", "64_variational_stress_origin__candidate_variational_batch_reconcile", "g64_reconcile"),
]


@dataclass(frozen=True)
class StatusEntry:
    name: str
    status: str
    conclusion: str
    boundary: str


@dataclass(frozen=True)
class ResultEntry:
    name: str
    status: str
    result: str
    meaning: str
    boundary: str


@dataclass(frozen=True)
class BurdenEntry:
    name: str
    status: str
    burden: str
    discipline: str


@dataclass(frozen=True)
class RejectedRoute:
    name: str
    route: str
    reason: str


@dataclass(frozen=True)
class HandoffEntry:
    name: str
    status: str
    route: str
    caution: str


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
        "DEFERRED_WITH_TARGET": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REJECTED_ROUTE": StatusMark.FAIL,
    }.get(status, StatusMark.INFO)


def governance_status(status: str) -> GovernanceStatus:
    if status in {
        "QUADRATIC_ORIGIN_REJECTED",
        "AMPLITUDE_REPAIR_REJECTED",
        "SOURCE_COUPLING_REJECTED",
        "ZERO_RESPONSE_REJECTED_AS_TRIVIAL",
        "SIMPLE_ORIGIN_FAILED",
        "REJECTED_ROUTE",
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
        "DIAGNOSTIC_ONLY_DOWNGRADE_POSSIBLE",
        "CONDITIONAL_AUDIT_RETENTION_WEAKENED",
    }:
        return ObligationStatus.DEFERRED
    return ObligationStatus.OPEN


def record_marker(ns, marker_id: str, symbol_name: str, scope: str) -> None:
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[],
        output=sp.Symbol(symbol_name),
        method="inventory marker; group status summary, no physical derivation",
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


def record_obligation(ns, obligation_id: str, statement: str, status: str) -> None:
    ns.record_obligation(
        ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=obligation_id,
            status=obligation_status(status),
            required_by=[SCRIPT_ID],
            description=statement,
        )
    )


def emit_line(out: ScriptOutput, label: str, status: str, text: str, *, obligation: bool = False) -> None:
    if obligation:
        with out.unresolved_obligations():
            out.line(label, mark(status), f"{status}: {text}")
    else:
        with out.governance_assessments():
            out.line(label, mark(status), f"{status}: {text}")


def build_status_entries() -> List[StatusEntry]:
    return [
        StatusEntry("G64-1: origin attempt", "VARIATIONAL_ORIGIN_OPENED", "Group 64 attempted a simple reduced variational/stress origin route", "not insertion"),
        StatusEntry("G64-2: simple origin status", "SIMPLE_ORIGIN_FAILED", "simple local variational/stress origins did not license the candidate", "negative but useful"),
        StatusEntry("G64-3: downgrade", "DIAGNOSTIC_DOWNGRADE_STRENGTHENED", "diagnostic-only downgrade is more strongly supported", "candidate not deleted"),
        StatusEntry("G64-4: physical use", "PHYSICAL_USE_BLOCKED", "candidate remains blocked for physical use", "not parent-ready"),
    ]


def build_result_entries() -> List[ResultEntry]:
    return [
        ResultEntry("C1: requirements", "REQUIREMENTS_RESTATED", "a real origin must derive profile/stress basis, u, p_free, source independence, boundary behavior, trace/mass status, and avoid O disguise", "retention contract made concrete", "basis"),
        ResultEntry("C2: scalar origin", "QUADRATIC_ORIGIN_REJECTED", "eta fails the constant-k f''=k f test", "simple constant-coefficient quadratic scalar origin is rejected", "simple route only"),
        ResultEntry("C3: EL ratio", "EL_RATIO_NOT_CONSTANT", "f''/f differs between y=0 and y=1/2", "eta is not a constant-k stationary profile", "reduced witness"),
        ResultEntry("C4: linear closure", "TRACE_MASS_TENSION_REPRODUCED", "u=a p_r+b p_t gives trace closure a=1,b=2 and active closure a=-1,b=-2 with no simultaneous solution", "simple stress closure reproduces obstruction", "open"),
        ResultEntry("C5: amplitude", "AMPLITUDE_UNDERIVED", "source-coupled, normalization-as-origin, diagnostic-repair, and zero-response amplitude routes fail", "p_free remains underived", "open"),
        ResultEntry("C6: boundary", "BOUNDARY_SILENCE_NOT_ORIGIN", "endpoint value/slope silence holds, but eta'' endpoint burden remains and bulk origin is missing", "boundary behavior alone is not a variational origin", "open"),
        ResultEntry("C7: route status", "SIMPLE_ORIGIN_FAILED", "simple scalar, closure, amplitude, and boundary origin attempts fail", "conditional audit retention is weakened", "not full no-go"),
        ResultEntry("C8: downgrade status", "DIAGNOSTIC_DOWNGRADE_STRENGTHENED", "diagnostic-only downgrade is now more strongly supported", "preserve diagnostics, block physical use", "allowed"),
    ]


def build_burdens() -> List[BurdenEntry]:
    return [
        BurdenEntry("B1: downgrade record", "DEFERRED_WITH_TARGET", "record diagnostic-only downgrade unless a stronger origin route is explicitly attempted", "avoid looping"),
        BurdenEntry("B2: stronger origin", "ENERGY_ACCOUNTING_REQUIRED", "derive nonlinear, variable-coefficient, tensor, constrained, or covariant variational principle if retention continues", "avoid simple-origin failure"),
        BurdenEntry("B3: stress accounting", "STRESS_ACCOUNTING_NOT_CLOSED", "derive u relation and p_free if candidate remains live", "avoid arbitrary stress"),
        BurdenEntry("B4: source/covariant safety", "SAFETY_THEOREMS_REQUIRED", "prove source/trace/mass/covariant safety if candidate remains live", "avoid hidden load"),
        BurdenEntry("B5: physical-use block", "NOT_INSERTABLE", "keep insertion, active O, recombination, and parent closure closed", "avoid status inflation"),
    ]


def build_rejected() -> List[RejectedRoute]:
    return [
        RejectedRoute("R1: variational label", "claim origin from idea alone", "simple origin tests failed"),
        RejectedRoute("R2: constant-k scalar origin", "derive eta from f''=k f", "f''/f is not constant"),
        RejectedRoute("R3: linear closure as solution", "choose trace or active closure and stop", "only one diagnostic closes"),
        RejectedRoute("R4: source amplitude", "derive p_free from rho_M", "hidden source coupling"),
        RejectedRoute("R5: normalization as physics", "use target normalization as physical origin", "normalization is scale-setting only"),
        RejectedRoute("R6: zero response", "set p_free=0", "trivial no-response"),
        RejectedRoute("R7: boundary-only proof", "use endpoint silence as origin", "bulk Euler/stress law missing"),
        RejectedRoute("R8: insertion anyway", "insert the audit candidate", "not licensed"),
    ]


def build_handoffs() -> List[HandoffEntry]:
    return [
        HandoffEntry("H1: transition diagnostic downgrade", "DIAGNOSTIC_DOWNGRADE_STRENGTHENED", "record diagnostic-only status for the transition response", "preserve clues but forbid physical use"),
        HandoffEntry("H2: stronger variational origin", "ENERGY_ACCOUNTING_REQUIRED", "attempt nonlinear/variable/tensor/covariant origin only if deliberately chosen", "do not treat simple failure as full no-go"),
        HandoffEntry("H3: parent blocker inventory", "DEFERRED_WITH_TARGET", "return to parent blockers after quarantining transition diagnostics", "avoid looping on failed candidate"),
    ]


def record_governance(ns, entries, results, burdens, rejected, handoffs) -> None:
    record_marker(ns, MARKER_ID, "G64_variational_origin_summary", "Group 64 simple variational/stress origin summary; no physical insertion")
    for idx, item in enumerate(entries, 1):
        record_claim(ns, f"{MARKER_ID}_entry_{idx}", MARKER_ID, item.status, f"{item.name}: {item.conclusion}. Boundary: {item.boundary}.")
    for idx, item in enumerate(results, 1):
        record_claim(ns, f"{MARKER_ID}_result_{idx}", MARKER_ID, item.status, f"{item.name}: {item.result}. Meaning: {item.meaning}. Boundary: {item.boundary}.")
    for idx, item in enumerate(burdens, 1):
        record_obligation(ns, f"{MARKER_ID}_burden_{idx}", f"{item.name}: {item.burden}. Discipline: {item.discipline}.", item.status)
    for idx, item in enumerate(rejected, 1):
        record_claim(ns, f"{MARKER_ID}_rejected_{idx}", MARKER_ID, "REJECTED_ROUTE", f"Rejected route: {item.route}. Reason: {item.reason}.")
    for idx, item in enumerate(handoffs, 1):
        record_obligation(ns, f"{MARKER_ID}_handoff_{idx}", f"{item.name}: {item.route}. Caution: {item.caution}.", item.status)


def main() -> None:
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    entries = build_status_entries()
    results = build_result_entries()
    burdens = build_burdens()
    rejected = build_rejected()
    handoffs = build_handoffs()

    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  Did a simple reduced variational/stress origin license the transition response?\n")
    print("Discipline:\n")
    print("  Preserve failed simple-origin result, diagnostic downgrade strengthened, and blocked physical use.")
    emit_line(out, "Group 64 status summary opened", "PASS", "closing simple origin attempt without inserting the candidate")

    header("Case 1: Group 64 compact result ledger")
    ledger = [
        ("origin attempt", "VARIATIONAL_ORIGIN_OPENED", "simple reduced variational/stress origin route tested"),
        ("requirements", "REQUIREMENTS_RESTATED", "origin contract made concrete"),
        ("quadratic scalar origin", "QUADRATIC_ORIGIN_REJECTED", "eta does not satisfy constant-k f''=k f"),
        ("EL ratio", "EL_RATIO_NOT_CONSTANT", "f''/f is not constant"),
        ("linear closure", "TRACE_MASS_TENSION_REPRODUCED", "linear stress closure reproduces trace/mass obstruction"),
        ("amplitude", "AMPLITUDE_UNDERIVED", "p_free remains underived after bad origins fail"),
        ("boundary", "BOUNDARY_SILENCE_NOT_ORIGIN", "endpoint silence is useful but not an origin"),
        ("simple origin", "SIMPLE_ORIGIN_FAILED", "no simple origin route licensed the response"),
        ("downgrade", "DIAGNOSTIC_DOWNGRADE_STRENGTHENED", "diagnostic-only downgrade is more strongly supported"),
        ("physical use", "PHYSICAL_USE_BLOCKED", "no insertion, active O, recombination, or parent closure opened"),
    ]
    for label, status, text in ledger:
        emit_line(out, label, status, text)

    header("Case 2: Group 64 status entries")
    for item in entries:
        subheader(item.name)
        emit_line(out, item.name, item.status, f"{item.conclusion}. Boundary: {item.boundary}.")

    header("Case 3: Origin attempt results")
    for item in results:
        subheader(item.name)
        print(f"Result: {item.result}")
        print(f"Meaning: {item.meaning}")
        emit_line(out, item.name, item.status, f"{item.meaning}. Boundary: {item.boundary}.")

    header("Case 4: Open burdens after Group 64")
    for item in burdens:
        subheader(item.name)
        emit_line(out, item.name, item.status, f"{item.burden}. Discipline: {item.discipline}.", obligation=True)

    header("Case 5: Rejected origin routes")
    for item in rejected:
        subheader(item.name)
        print(f"Route: {item.route}")
        emit_line(out, item.name, "REJECTED_ROUTE", item.reason)

    header("Case 6: Safe handoffs")
    for item in handoffs:
        subheader(item.name)
        emit_line(out, item.name, item.status, f"{item.route}. Caution: {item.caution}.")

    header("Case 7: Final interpretation")
    conclusions = [
        ("C1: Group 64 result", "SIMPLE_ORIGIN_FAILED", "simple reduced variational/stress origins did not license the transition response"),
        ("C2: not full no-go", "DEFERRED_WITH_TARGET", "nonlinear, variable-coefficient, tensor, constrained, or covariant origins remain untested"),
        ("C3: downgrade", "DIAGNOSTIC_DOWNGRADE_STRENGTHENED", "diagnostic-only downgrade is now more strongly supported"),
        ("C4: candidate status", "STRESS_ACCOUNTING_NOT_CLOSED", "conditional audit retention is weakened and still burdened"),
        ("C5: physical-use status", "NOT_INSERTABLE", "B_s/F_zeta insertion, active O, recombination, and parent route remain closed"),
    ]
    for label, status, text in conclusions:
        emit_line(out, label, status, text)

    header("Final summary")
    print("Group 64 status summary result:\n")
    print("  Group 64 attempted a real simple reduced variational/stress-origin route.")
    print("  It did not find an origin and did not insert the candidate.")
    print()
    print("  Main reduced results:")
    print("    eta fails a constant-coefficient f''=k f Euler-Lagrange origin test.")
    print("    A linear closure u=a p_r+b p_t reproduces trace/mass tension.")
    print("    p_free remains underived after source, repair, normalization, and zero-response origins fail.")
    print("    Endpoint value/slope silence is real but not a full variational origin.")
    print()
    print("  Status:")
    print("    simple local variational/stress origin failed")
    print("    diagnostic-only downgrade strengthened")
    print("    physical use remains blocked")
    print()
    print("  Not proven:")
    print("    not a full no-go theorem for every possible variational/tensor origin")
    print()
    print("Next honest move:")
    print("  record transition diagnostic-only downgrade, unless a stronger origin route is deliberately attempted.")

    record_governance(ns, entries, results, burdens, rejected, handoffs)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
