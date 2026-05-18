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
SCRIPT_LABEL = "Candidate Group 61 Status Summary"
MARKER_ID = "g61_summary"

DEPENDENCIES = [
    ("g60_summary", "60_term_exclusion_sieve__candidate_group_60_status_summary", "g60_summary"),
    ("g61_problem", "61_source_safety_audit__candidate_source_problem", "g61_problem"),
    ("g61_role", "61_source_safety_audit__candidate_role_separation", "g61_role"),
    ("g61_coupling", "61_source_safety_audit__candidate_source_coupling", "g61_coupling"),
    ("g61_mass", "61_source_safety_audit__candidate_mass_moment", "g61_mass"),
    ("g61_tension", "61_source_safety_audit__candidate_trace_mass_tension", "g61_tension"),
    ("g61_exchange", "61_source_safety_audit__candidate_conservation_exchange", "g61_exchange"),
    ("g61_class", "61_source_safety_audit__candidate_source_route_classifier", "g61_class"),
    ("g61_reconcile", "61_source_safety_audit__candidate_source_batch_reconcile", "g61_reconcile"),
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
        "SOURCE_AUDIT_OPENED": StatusMark.INFO,
        "ROLE_SEPARATION_APPLIED": StatusMark.PASS,
        "SOURCE_CARRYING_TERM_REJECTED": StatusMark.FAIL,
        "SOURCE_REPAIR_REJECTED": StatusMark.FAIL,
        "TRACE_CARRYING_TERM_REJECTED": StatusMark.FAIL,
        "RESIDUAL_REENTRY_REJECTED": StatusMark.FAIL,
        "SOURCE_COUPLING_REJECTED": StatusMark.FAIL,
        "SOURCE_NEUTRAL_AMPLITUDE_CONDITIONAL": StatusMark.INFO,
        "MASS_MOMENT_BURDEN_FOUND": StatusMark.OBLIGATION,
        "MASS_COUPLED_ROUTE_UNSAFE": StatusMark.FAIL,
        "TRACE_MASS_TENSION_FOUND": StatusMark.OBLIGATION,
        "TRACE_FREE_CLOSURE_CONDITIONAL": StatusMark.INFO,
        "ACTIVE_MASS_NEUTRAL_CLOSURE_CONDITIONAL": StatusMark.INFO,
        "CONSERVATION_EXCHANGE_FILTER_APPLIED": StatusMark.PASS,
        "REDUCED_EXCHANGE_SILENCE_CONDITIONAL": StatusMark.INFO,
        "SOURCE_SAFETY_NOT_CLOSED": StatusMark.OBLIGATION,
        "AUDIT_CANDIDATE_RETAINED": StatusMark.INFO,
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
        "SOURCE_CARRYING_TERM_REJECTED",
        "SOURCE_REPAIR_REJECTED",
        "TRACE_CARRYING_TERM_REJECTED",
        "RESIDUAL_REENTRY_REJECTED",
        "SOURCE_COUPLING_REJECTED",
        "MASS_COUPLED_ROUTE_UNSAFE",
        "REJECTED_ROUTE",
    }:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {
        "MASS_MOMENT_BURDEN_FOUND",
        "TRACE_MASS_TENSION_FOUND",
        "SOURCE_SAFETY_NOT_CLOSED",
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
        StatusEntry("G61-1: source audit", "SOURCE_AUDIT_OPENED", "Group 61 audited the narrowed stress-only transition response for source/mass role safety", "not insertion"),
        StatusEntry("G61-2: source safety", "SOURCE_SAFETY_NOT_CLOSED", "source safety was sharpened but not proven", "theorem still required"),
        StatusEntry("G61-3: audit survivor", "AUDIT_CANDIDATE_RETAINED", "only a source-independent stress-only transition response remains as audit material", "not physical use"),
        StatusEntry("G61-4: physical use", "PHYSICAL_USE_BLOCKED", "candidate remains blocked for physical use", "not parent-ready"),
    ]


def build_result_entries() -> List[ResultEntry]:
    return [
        ResultEntry("C1: role separation", "ROLE_SEPARATION_APPLIED", "source carrying, source repair, trace carrying, and residual reentry remain rejected", "ordinary source and trace roles remain separated by incidence", "not source theorem"),
        ResultEntry("C2: source coupling", "SOURCE_COUPLING_REJECTED", "p0=p_free+lambda*rho_M gives d(p_r)/d(rho_M)=eta^2*lambda", "direct rho_M amplitude is hidden source dependence unless lambda=0", "rejected unless zero"),
        ResultEntry("C3: source-independent amplitude", "SOURCE_NEUTRAL_AMPLITUDE_CONDITIONAL", "lambda=0 leaves p0=p_free", "source-independent amplitude remains possible but underived", "audit-only"),
        ResultEntry("C4: mass moment", "MASS_MOMENT_BURDEN_FOUND", "E_layer=256*ell*p0*(49R^4+58R^2ell^2+ell^4)/(3465*(7R^2+ell^2)^2)", "stress-only response has nonzero reduced layer moment", "not mass theorem"),
        ResultEntry("C5: mass-coupled route", "MASS_COUPLED_ROUTE_UNSAFE", "Delta_M=beta*E_layer", "beta != 0 shifts the mass diagnostic", "blocked without theorem"),
        ResultEntry("C6: trace/mass tension", "TRACE_MASS_TENSION_FOUND", "trace-free requires u=p_r+2p_t while active-mass-neutral requires u=-(p_r+2p_t)", "both require p_r+2p_t=0, which is not generic", "open burden"),
        ResultEntry("C7: conservation exchange", "CONSERVATION_EXCHANGE_FILTER_APPLIED", "D_total=D_A+D_layer+J_exchange; D_layer=0 alone leaves D_A", "reduced layer silence is internal balance only, not source safety", "not covariant conservation"),
        ResultEntry("C8: route status", "SOURCE_SAFETY_NOT_CLOSED", "source safety remains unclosed", "candidate remains audit-only", "not insertable"),
    ]


def build_burdens() -> List[BurdenEntry]:
    return [
        BurdenEntry("B1: source safety theorem", "SOURCE_SAFETY_REQUIRED", "prove or reject ordinary-source neutrality of the narrowed stress-only response", "protect A-sector source routing"),
        BurdenEntry("B2: mass/trace closure", "SAFETY_THEOREMS_REQUIRED", "resolve trace-free versus active-mass-neutral closure tension", "avoid hidden trace or mass load"),
        BurdenEntry("B3: energy/stress accounting", "ENERGY_ACCOUNTING_REQUIRED", "derive admissible u, p_r, p_t, and amplitude relation", "avoid arbitrary stress closure"),
        BurdenEntry("B4: covariant conservation", "DIVERGENCE_IDENTITY_REQUIRED", "lift reduced exchange accounting to covariant divergence identity", "avoid parent overclaim"),
        BurdenEntry("B5: covariant layer lift", "COVARIANT_LIFT_REQUIRED", "lift the source/mass/trace/exchange diagnostics to geometric layer formalism", "avoid radial-only proof"),
        BurdenEntry("B6: physical-use block", "NOT_INSERTABLE", "keep insertion, active O, recombination, and parent closure closed", "avoid status inflation"),
    ]


def build_rejected() -> List[RejectedRoute]:
    return [
        RejectedRoute("R1: source carrying", "transition carries ordinary source load", "duplicates the A-sector source route"),
        RejectedRoute("R2: source repair", "transition replaces A-sector source", "role-purity violation even when incidence residual is zero"),
        RejectedRoute("R3: trace carrying", "transition carries trace payload", "adds trace count"),
        RejectedRoute("R4: residual reentry", "transition permits residual trace/source reentry", "reopens rejected residual route"),
        RejectedRoute("R5: direct source amplitude", "p0 depends directly on rho_M", "hidden ordinary-source dependence"),
        RejectedRoute("R6: mass-coupled route", "Delta_M=beta*E_layer with beta != 0", "mass shift diagnostic appears"),
        RejectedRoute("R7: exchange repair", "choose J_exchange to cancel D_A+D_layer", "repair, not theorem"),
        RejectedRoute("R8: D_layer as source safety", "treat reduced D_layer=0 as full source/conservation proof", "A-sector and exchange terms remain"),
    ]


def build_handoffs() -> List[HandoffEntry]:
    return [
        HandoffEntry("H1: energy/stress accounting", "ENERGY_ACCOUNTING_REQUIRED", "derive or reject an admissible stress-energy role for the source-independent transition response", "do not choose u by convenience"),
        HandoffEntry("H2: trace/mass closure audit", "SAFETY_THEOREMS_REQUIRED", "resolve whether trace-free and active-mass-neutral conditions can coexist", "do not claim both from one arbitrary energy density"),
        HandoffEntry("H3: covariant layer lift", "COVARIANT_LIFT_REQUIRED", "lift source/mass/trace/exchange diagnostics to geometric layer objects", "do not treat reduced results as covariant"),
    ]


def record_governance(ns, entries, results, burdens, rejected, handoffs) -> None:
    record_marker(ns, MARKER_ID, "G61_source_safety_summary", "Group 61 source-safety audit summary; no physical insertion")
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
    print("  What did Group 61 establish about source safety for the narrowed transition response?\n")
    print("Discipline:\n")
    print("  Preserve rejected unsafe routes, sharpened mass/trace burdens, retained audit-only status, and blocked physical use.")
    emit_line(out, "Group 61 status summary opened", "PASS", "closing source-safety audit without proving source safety or insertion")

    header("Case 1: Group 61 compact result ledger")
    ledger = [
        ("source audit opened", "SOURCE_AUDIT_OPENED", "narrowed stress-only transition response was audited for source/mass role safety"),
        ("role separation", "ROLE_SEPARATION_APPLIED", "source carrying/repair and trace/reentry routes rejected"),
        ("source coupling", "SOURCE_COUPLING_REJECTED", "direct rho_M amplitude rejected unless lambda=0"),
        ("source-independent amplitude", "SOURCE_NEUTRAL_AMPLITUDE_CONDITIONAL", "p_free route remains audit-only and underived"),
        ("mass moment", "MASS_MOMENT_BURDEN_FOUND", "stress-only response has nonzero reduced layer moment"),
        ("mass-coupled route", "MASS_COUPLED_ROUTE_UNSAFE", "beta != 0 shifts mass diagnostic"),
        ("trace mass tension", "TRACE_MASS_TENSION_FOUND", "trace-free and active-mass-neutral closures conflict generically"),
        ("exchange audit", "CONSERVATION_EXCHANGE_FILTER_APPLIED", "D_layer=0 is not source safety or covariant conservation"),
        ("source safety", "SOURCE_SAFETY_NOT_CLOSED", "source safety remains an open theorem target"),
        ("audit candidate", "AUDIT_CANDIDATE_RETAINED", "source-independent stress-only response remains audit material"),
        ("physical use", "PHYSICAL_USE_BLOCKED", "no insertion, active O, recombination, or parent closure opened"),
    ]
    for label, status, text in ledger:
        emit_line(out, label, status, text)

    header("Case 2: Group 61 status entries")
    for item in entries:
        subheader(item.name)
        emit_line(out, item.name, item.status, f"{item.conclusion}. Boundary: {item.boundary}.")

    header("Case 3: Source-safety audit results")
    for item in results:
        subheader(item.name)
        print(f"Result: {item.result}")
        print(f"Meaning: {item.meaning}")
        emit_line(out, item.name, item.status, f"{item.meaning}. Boundary: {item.boundary}.")

    header("Case 4: Open burdens after Group 61")
    for item in burdens:
        subheader(item.name)
        emit_line(out, item.name, item.status, f"{item.burden}. Discipline: {item.discipline}.", obligation=True)

    header("Case 5: Rejected source-safety routes")
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
        ("C1: Group 61 result", "SOURCE_SAFETY_NOT_CLOSED", "source safety was sharpened but not proven"),
        ("C2: unsafe routes", "REJECTED_ROUTE", "source-coupled, source-repair, source-carrying, trace/reentry, exchange repair, and mass-coupled routes were rejected or blocked"),
        ("C3: audit survivor", "AUDIT_CANDIDATE_RETAINED", "only source-independent stress-only transition response remains as audit material"),
        ("C4: hard burdens", "TRACE_MASS_TENSION_FOUND", "mass/trace closure tension and mass moment burden remain"),
        ("C5: physical-use status", "NOT_INSERTABLE", "B_s/F_zeta insertion, active O, recombination, and parent route remain closed"),
    ]
    for label, status, text in conclusions:
        emit_line(out, label, status, text)

    header("Final summary")
    print("Group 61 status summary result:\n")
    print("  Group 61 audited source safety for the narrowed stress-only transition response.")
    print("  It did not prove source safety and did not insert the candidate.")
    print()
    print("  Main reduced results:")
    print("    Source carrying, source repair, trace carrying, and residual reentry remain rejected.")
    print("    Direct rho_M amplitude p0=p_free+lambda*rho_M is rejected unless lambda=0.")
    print("    Source-independent p_free remains possible but underived.")
    print("    The stress-only response has a nonzero reduced layer energy/mass moment.")
    print("    A mass-coupled route Delta_M=beta*E_layer is unsafe for beta != 0.")
    print("    Trace-free and active-mass-neutral closures require opposite u choices.")
    print("    Reduced D_layer=0 is internal balance only, not source safety or covariant conservation.")
    print()
    print("  Retained candidate:")
    print("    source-independent stress-only transition response as audit material")
    print()
    print("Still required:")
    print("  source-safety theorem")
    print("  mass/trace closure theorem or obstruction")
    print("  energy/stress accounting")
    print("  covariant conservation / layer lift")
    print()
    print("Forbidden immediate next step:")
    print("  B_s/F_zeta insertion, transition response insertion, active O construction, recombination, or parent closure")

    record_governance(ns, entries, results, burdens, rejected, handoffs)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
