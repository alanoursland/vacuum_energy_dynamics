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
SCRIPT_LABEL = "Candidate Group 62 Status Summary"
MARKER_ID = "g62_summary"

DEPENDENCIES = [
    ("g61_summary", "061_source_safety_audit__candidate_group_61_status_summary", "g61_summary"),
    ("g62_problem", "062_stress_energy_accounting__candidate_stress_problem", "g62_problem"),
    ("g62_inv", "062_stress_energy_accounting__candidate_closure_inventory", "g62_inv"),
    ("g62_closure", "062_stress_energy_accounting__candidate_trace_mass_closure_sieve", "g62_closure"),
    ("g62_P", "062_stress_energy_accounting__candidate_pressure_sum_obstruction", "g62_P"),
    ("g62_int", "062_stress_energy_accounting__candidate_integral_accounting", "g62_int"),
    ("g62_sign", "062_stress_energy_accounting__candidate_energy_sign_sieve", "g62_sign"),
    ("g62_amp", "062_stress_energy_accounting__candidate_amplitude_origin_sieve", "g62_amp"),
    ("g62_class", "062_stress_energy_accounting__candidate_stress_route_classifier", "g62_class"),
    ("g62_reconcile", "062_stress_energy_accounting__candidate_stress_batch_reconcile", "g62_reconcile"),
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
        "STRESS_AUDIT_OPENED": StatusMark.INFO,
        "CLOSURE_INVENTORY_DERIVED": StatusMark.PASS,
        "TRACE_CLOSURE_IDENTIFIED": StatusMark.INFO,
        "ACTIVE_MASS_CLOSURE_IDENTIFIED": StatusMark.INFO,
        "TRACE_MASS_TENSION_CONFIRMED": StatusMark.OBLIGATION,
        "PRESSURE_SUM_OBSTRUCTION_FOUND": StatusMark.OBLIGATION,
        "INTEGRAL_ACCOUNTING_DERIVED": StatusMark.PASS,
        "ACTIVE_MASS_BURDEN_FOUND": StatusMark.OBLIGATION,
        "TRACE_BURDEN_FOUND": StatusMark.OBLIGATION,
        "ENERGY_SIGN_BURDEN_FOUND": StatusMark.OBLIGATION,
        "ARBITRARY_CLOSURE_REJECTED": StatusMark.FAIL,
        "ZERO_RESPONSE_REJECTED_AS_TRIVIAL": StatusMark.FAIL,
        "AMPLITUDE_UNDERIVED": StatusMark.OBLIGATION,
        "SOURCE_COUPLING_REJECTED": StatusMark.FAIL,
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
    }.get(status, StatusMark.INFO)


def governance_status(status: str) -> GovernanceStatus:
    if status in {
        "ARBITRARY_CLOSURE_REJECTED",
        "ZERO_RESPONSE_REJECTED_AS_TRIVIAL",
        "SOURCE_COUPLING_REJECTED",
        "REJECTED_ROUTE",
    }:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {
        "TRACE_MASS_TENSION_CONFIRMED",
        "PRESSURE_SUM_OBSTRUCTION_FOUND",
        "ACTIVE_MASS_BURDEN_FOUND",
        "TRACE_BURDEN_FOUND",
        "ENERGY_SIGN_BURDEN_FOUND",
        "AMPLITUDE_UNDERIVED",
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
        StatusEntry("G62-1: stress audit", "STRESS_AUDIT_OPENED", "Group 62 audited stress-energy accounting for the source-independent transition response", "not insertion"),
        StatusEntry("G62-2: accounting status", "STRESS_ACCOUNTING_NOT_CLOSED", "stress-energy accounting was clarified but not closed", "theorem still required"),
        StatusEntry("G62-3: audit survivor", "AUDIT_CANDIDATE_RETAINED", "source-independent stress-only route remains only as audit material", "possible downgrade"),
        StatusEntry("G62-4: physical use", "PHYSICAL_USE_BLOCKED", "candidate remains blocked for physical use", "not parent-ready"),
    ]


def build_result_entries() -> List[ResultEntry]:
    return [
        ResultEntry("C1: closure inventory", "CLOSURE_INVENTORY_DERIVED", "p_r, p_t, P=p_r+2p_t, T=-u+P, and A=u+P were made explicit", "stress accounting variables are visible", "reduced"),
        ResultEntry("C2: closure algebra", "TRACE_MASS_TENSION_CONFIRMED", "u=gamma*P gives gamma=1 for trace and gamma=-1 for active mass", "both diagnostics require P=0 to close together", "open obstruction"),
        ResultEntry("C3: pressure obstruction", "PRESSURE_SUM_OBSTRUCTION_FOUND", "P is not generically zero for the closure-supported layer", "simultaneous trace/mass closure is obstructed", "reduced witness"),
        ResultEntry("C4: integral accounting", "INTEGRAL_ACCOUNTING_DERIVED", "I_P=2*E_pr", "pressure-sum burden is tied directly to layer stress energy", "reduced"),
        ResultEntry("C5: trace-free burden", "ACTIVE_MASS_BURDEN_FOUND", "u=P closes trace but leaves active diagnostic 2P", "trace-free closure is not active-mass-neutral", "open"),
        ResultEntry("C6: active-neutral burden", "TRACE_BURDEN_FOUND", "u=-P closes active mass but leaves trace diagnostic 2P", "active-mass-neutral closure is not trace-free", "open"),
        ResultEntry("C7: sign/simple closure", "ENERGY_SIGN_BURDEN_FOUND", "u=0 fails both diagnostics and u=±P carry sign/admissibility burden", "no simple closure licenses the response", "open"),
        ResultEntry("C8: amplitude origin", "AMPLITUDE_UNDERIVED", "source-coupled, diagnostic-repair, and zero-response amplitude origins were rejected", "p_free remains underived", "open"),
        ResultEntry("C9: route status", "STRESS_ACCOUNTING_NOT_CLOSED", "stress accounting remains unclosed", "candidate remains audit-only / possible diagnostic-only downgrade", "not insertable"),
    ]


def build_burdens() -> List[BurdenEntry]:
    return [
        BurdenEntry("B1: stress-energy principle", "ENERGY_ACCOUNTING_REQUIRED", "derive admissible u/p_r/p_t/p_free relation or reject the candidate", "avoid arbitrary stress"),
        BurdenEntry("B2: trace/mass theorem", "SAFETY_THEOREMS_REQUIRED", "resolve trace/mass closure tension or record obstruction", "avoid hidden load"),
        BurdenEntry("B3: source safety", "SOURCE_SAFETY_REQUIRED", "connect stress-energy accounting to ordinary-source neutrality", "avoid hidden source"),
        BurdenEntry("B4: covariant lift", "COVARIANT_LIFT_REQUIRED", "lift reduced stress accounting to geometric layer formalism", "avoid reduced-only proof"),
        BurdenEntry("B5: divergence identity", "DIVERGENCE_IDENTITY_REQUIRED", "lift reduced closure to covariant conservation/identity structure", "avoid parent overclaim"),
        BurdenEntry("B6: physical-use block", "NOT_INSERTABLE", "keep insertion, active O, recombination, and parent closure closed", "avoid status inflation"),
    ]


def build_rejected() -> List[RejectedRoute]:
    return [
        RejectedRoute("R1: arbitrary u", "choose u only to pass one diagnostic", "closure must be derived"),
        RejectedRoute("R2: trace-free as full closure", "adopt u=P and claim mass safety", "active-mass burden remains"),
        RejectedRoute("R3: active-neutral as full closure", "adopt u=-P and claim trace safety", "trace burden remains"),
        RejectedRoute("R4: zero energy", "adopt u=0", "both diagnostics remain open"),
        RejectedRoute("R5: pressure sum by fiat", "declare P=0", "reduced witness is nonzero"),
        RejectedRoute("R6: source amplitude", "derive p_free from rho_M", "hidden ordinary-source dependence"),
        RejectedRoute("R7: repair amplitude", "choose p_free to cancel trace or mass diagnostics", "repair, not derivation"),
        RejectedRoute("R8: zero amplitude", "set p_free=0 and call candidate licensed", "trivial no-response"),
        RejectedRoute("R9: insertion anyway", "insert the audit candidate", "not licensed"),
    ]


def build_handoffs() -> List[HandoffEntry]:
    return [
        HandoffEntry("H1: obstruction decision", "DEFERRED_WITH_TARGET", "decide whether trace/mass closure tension downgrades the transition response to diagnostic-only", "do not silently keep a failed candidate"),
        HandoffEntry("H2: variational stress origin", "ENERGY_ACCOUNTING_REQUIRED", "attempt to derive u, p_r, p_t, and p_free from a principle", "do not choose closures by convenience"),
        HandoffEntry("H3: covariant layer lift", "COVARIANT_LIFT_REQUIRED", "lift the reduced accounting to geometric layer objects", "do not treat reduced accounting as covariant"),
    ]


def record_governance(ns, entries, results, burdens, rejected, handoffs) -> None:
    record_marker(ns, MARKER_ID, "G62_stress_accounting_summary", "Group 62 stress-energy accounting summary; no physical insertion")
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
    print("  What did Group 62 establish about stress-energy accounting for the source-independent transition response?\n")
    print("Discipline:\n")
    print("  Preserve closure obstruction, underived amplitude, audit-only status, and blocked physical use.")
    emit_line(out, "Group 62 status summary opened", "PASS", "closing stress-energy audit without deriving a closure or insertion")

    header("Case 1: Group 62 compact result ledger")
    ledger = [
        ("stress audit opened", "STRESS_AUDIT_OPENED", "source-independent stress-only route was audited for stress-energy accounting"),
        ("closure inventory", "CLOSURE_INVENTORY_DERIVED", "p_r, p_t, P, T, and A made explicit"),
        ("trace mass tension", "TRACE_MASS_TENSION_CONFIRMED", "u=P and u=-P satisfy opposite diagnostics"),
        ("pressure obstruction", "PRESSURE_SUM_OBSTRUCTION_FOUND", "P is not generically zero"),
        ("integral accounting", "INTEGRAL_ACCOUNTING_DERIVED", "I_P=2*E_pr"),
        ("trace-free burden", "ACTIVE_MASS_BURDEN_FOUND", "u=P leaves active-mass diagnostic"),
        ("active-neutral burden", "TRACE_BURDEN_FOUND", "u=-P leaves trace diagnostic"),
        ("energy sign burden", "ENERGY_SIGN_BURDEN_FOUND", "simple closures do not give full admissibility"),
        ("amplitude", "AMPLITUDE_UNDERIVED", "p_free remains underived after rejecting bad origins"),
        ("stress accounting", "STRESS_ACCOUNTING_NOT_CLOSED", "stress-energy accounting remains open"),
        ("audit candidate", "AUDIT_CANDIDATE_RETAINED", "candidate remains audit-only / possible downgrade"),
        ("physical use", "PHYSICAL_USE_BLOCKED", "no insertion, active O, recombination, or parent closure opened"),
    ]
    for label, status, text in ledger:
        emit_line(out, label, status, text)

    header("Case 2: Group 62 status entries")
    for item in entries:
        subheader(item.name)
        emit_line(out, item.name, item.status, f"{item.conclusion}. Boundary: {item.boundary}.")

    header("Case 3: Stress accounting audit results")
    for item in results:
        subheader(item.name)
        print(f"Result: {item.result}")
        print(f"Meaning: {item.meaning}")
        emit_line(out, item.name, item.status, f"{item.meaning}. Boundary: {item.boundary}.")

    header("Case 4: Open burdens after Group 62")
    for item in burdens:
        subheader(item.name)
        emit_line(out, item.name, item.status, f"{item.burden}. Discipline: {item.discipline}.", obligation=True)

    header("Case 5: Rejected stress-accounting routes")
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
        ("C1: Group 62 result", "STRESS_ACCOUNTING_NOT_CLOSED", "stress-energy accounting was clarified but not closed"),
        ("C2: obstruction", "TRACE_MASS_TENSION_CONFIRMED", "trace-free and active-mass-neutral closures conflict unless P=0"),
        ("C3: pressure burden", "PRESSURE_SUM_OBSTRUCTION_FOUND", "P is not generically zero and I_P=2*E_pr"),
        ("C4: amplitude burden", "AMPLITUDE_UNDERIVED", "p_free remains underived after source/repair/zero origins fail"),
        ("C5: candidate status", "AUDIT_CANDIDATE_RETAINED", "source-independent stress-only response remains audit-only, with diagnostic-only downgrade possible"),
        ("C6: physical-use status", "NOT_INSERTABLE", "B_s/F_zeta insertion, active O, recombination, and parent route remain closed"),
    ]
    for label, status, text in conclusions:
        emit_line(out, label, status, text)

    header("Final summary")
    print("Group 62 status summary result:\n")
    print("  Group 62 audited stress-energy accounting for the source-independent stress-only transition response.")
    print("  It did not derive an admissible closure and did not insert the candidate.")
    print()
    print("  Main reduced results:")
    print("    Stress diagnostics are T=-u+P and A=u+P with P=p_r+2p_t.")
    print("    u=gamma*P gives gamma=1 for trace-free and gamma=-1 for active-mass-neutral.")
    print("    Both diagnostics close together only if P=0.")
    print("    P is not generically zero for the closure-supported layer.")
    print("    Integrated accounting gives I_P=2*E_pr.")
    print("    u=P leaves active-mass burden; u=-P leaves trace burden; u=0 fails both.")
    print("    p_free remains underived after source-coupled, diagnostic-repair, and zero-response origins are rejected.")
    print()
    print("  Retained candidate:")
    print("    source-independent stress-only transition response as audit material")
    print()
    print("Possible downgrade:")
    print("    diagnostic-only if no stress-energy principle is found")
    print()
    print("Still required:")
    print("  stress-energy principle")
    print("  trace/mass closure theorem or obstruction decision")
    print("  source safety")
    print("  covariant conservation / layer lift")
    print()
    print("Forbidden immediate next step:")
    print("  B_s/F_zeta insertion, transition response insertion, active O construction, recombination, or parent closure")

    record_governance(ns, entries, results, burdens, rejected, handoffs)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
