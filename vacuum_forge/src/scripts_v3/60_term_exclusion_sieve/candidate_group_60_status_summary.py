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
SCRIPT_LABEL = "Candidate Group 60 Status Summary"
MARKER_ID = "g60_summary"

DEPENDENCIES = [
    ("g59_summary", "59_transition_term_audit__candidate_group_59_status_summary", "g59_summary"),
    ("g60_problem", "60_term_exclusion_sieve__candidate_sieve_problem", "g60_problem"),
    ("g60_repair", "60_term_exclusion_sieve__candidate_repair_sieve", "g60_repair"),
    ("g60_der", "60_term_exclusion_sieve__candidate_derivative_sieve", "g60_der"),
    ("g60_neu", "60_term_exclusion_sieve__candidate_neutrality_sieve", "g60_neu"),
    ("g60_tune", "60_term_exclusion_sieve__candidate_tuning_sieve", "g60_tune"),
    ("g60_src", "60_term_exclusion_sieve__candidate_source_trace_sieve", "g60_src"),
    ("g60_div", "60_term_exclusion_sieve__candidate_div_energy_sieve", "g60_divE"),
    ("g60_class", "60_term_exclusion_sieve__candidate_sieve_classifier", "g60_class"),
    ("g60_reconcile", "60_term_exclusion_sieve__candidate_sieve_reconcile", "g60_reconcile"),
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
class RejectedUpgrade:
    name: str
    upgrade: str
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
        StatusEntry(
            "G60-1: exclusion sieve",
            "SIEVE_OPENED",
            "Group 60 applied a stricter exclusion sieve to the Group 59 transition-response survivor",
            "not insertion",
        ),
        StatusEntry(
            "G60-2: candidate narrowed",
            "TERM_SURVIVES_NARROWLY",
            "the survivor was narrowed to a stress-only localized weighted-neutral-generated closure-supported response",
            "audit-only",
        ),
        StatusEntry(
            "G60-3: physical use",
            "PHYSICAL_USE_BLOCKED",
            "candidate remains blocked for physical use",
            "not parent-ready",
        ),
    ]


def build_result_entries() -> List[ResultEntry]:
    return [
        ResultEntry(
            "C1: repair rejection",
            "REPAIR_TERM_REJECTED",
            "raw R1/R2 insertion and arbitrary counterterm repair were rejected",
            "residues remain clues only",
            "not inserted",
        ),
        ResultEntry(
            "C2: derivative narrowing",
            "DERIVATIVE_BURDEN_FOUND",
            "w and eta have nonzero endpoint second derivatives, while eta^2 is silent through second derivative",
            "scalar route is burdened and stress-like squared basis is safer",
            "reduced",
        ),
        ResultEntry(
            "C3: scalar neutrality",
            "SCALAR_CHARGE_TERM_REJECTED",
            "Q[eta]=0 but Q[eta^2] and Q[constant] are nonzero",
            "eta^2 cannot be scalar response and can survive only as stress-like basis",
            "rejected as scalar",
        ),
        ResultEntry(
            "C4: tuning rejection",
            "TUNING_ROUTE_REJECTED",
            "candidate=a*eta+b has Q proportional to b and endpoints equal b",
            "constant admixture survives only by b=0, so the constant basis is rejected",
            "rejected",
        ),
        ResultEntry(
            "C5: source/trace sieve",
            "SOURCE_TRACE_SIEVE_APPLIED",
            "source-carrying, source-repair, trace-carrying, and residual-reentry routes were rejected",
            "incidence guardrails preserved",
            "not full theorem",
        ),
        ResultEntry(
            "C6: divergence/energy sieve",
            "CLOSURE_SUPPORTED_TERM_SURVIVES",
            "radial-only stress failed; p_t=p_r+r*p_r'/2 gives reduced D=0",
            "closure-supported route survives with energy/stress burden",
            "not Bianchi proof",
        ),
        ResultEntry(
            "C7: energy burden",
            "ENERGY_ACCOUNTING_REQUIRED",
            "E_layer=256*ell*p0*(49R^4+58R^2ell^2+ell^4)/(3465*(7R^2+ell^2)^2)",
            "the surviving response is nonfree and needs accounting",
            "open",
        ),
        ResultEntry(
            "C8: narrowed survivor",
            "TERM_SURVIVES_NARROWLY",
            "stress-only localized weighted-neutral-generated closure-supported transition response",
            "the candidate survives only as audit material",
            "not insertable",
        ),
    ]


def build_burdens() -> List[BurdenEntry]:
    return [
        BurdenEntry(
            "B1: source safety",
            "SOURCE_SAFETY_REQUIRED",
            "prove surviving stress-only transition response does not duplicate ordinary source load",
            "protect A-sector source routing",
        ),
        BurdenEntry(
            "B2: covariant lift",
            "COVARIANT_LIFT_REQUIRED",
            "lift derivative locality, weighted neutralizer, and closure to geometric layer formalism",
            "avoid radial-only proof",
        ),
        BurdenEntry(
            "B3: divergence identity",
            "DIVERGENCE_IDENTITY_REQUIRED",
            "lift reduced D=0 closure to covariant identity structure",
            "avoid parent overclaim",
        ),
        BurdenEntry(
            "B4: energy/stress accounting",
            "ENERGY_ACCOUNTING_REQUIRED",
            "derive admissible energy/stress role for the narrowed survivor",
            "avoid free transition response",
        ),
        BurdenEntry(
            "B5: physical-use block",
            "NOT_INSERTABLE",
            "keep insertion, active O, recombination, and parent closure closed",
            "avoid status inflation",
        ),
    ]


def build_rejected() -> List[RejectedUpgrade]:
    return [
        RejectedUpgrade("R1: raw residue repair", "insert R1/R2 or counterterm", "residues remain clues only"),
        RejectedUpgrade("R2: eta as unrestricted scalar insertion", "ignore second-derivative endpoint burden", "curvature/derivative burden remains"),
        RejectedUpgrade("R3: eta^2 scalar response", "use eta^2 as scalar charge/source profile", "weighted charge is nonzero"),
        RejectedUpgrade("R4: constant admixture", "keep constant term by forcing coefficient to zero", "zero coefficient means rejected basis"),
        RejectedUpgrade("R5: source repair", "let transition response replace A-sector source", "source role-purity is violated"),
        RejectedUpgrade("R6: source carrying", "let transition response carry ordinary source load", "ordinary source duplication is forbidden"),
        RejectedUpgrade("R7: trace double-count", "let transition response carry trace or residual reentry", "trace count must remain exact once"),
        RejectedUpgrade("R8: radial-only stress", "accept p_r without tangential closure", "reduced divergence fails"),
        RejectedUpgrade("R9: active O by disguise", "promote N_w to active O", "operator burdens remain"),
        RejectedUpgrade("R10: reduced closure as Bianchi proof", "treat reduced D=0 as covariant identity", "covariant lift remains required"),
    ]


def build_handoffs() -> List[HandoffEntry]:
    return [
        HandoffEntry(
            "H1: source safety audit",
            "SOURCE_SAFETY_REQUIRED",
            "test whether the narrowed stress-only transition response duplicates ordinary source load",
            "do not treat incidence filtering as a theorem",
        ),
        HandoffEntry(
            "H2: covariant layer lift",
            "COVARIANT_LIFT_REQUIRED",
            "lift derivative locality, weighted neutralizer, and closure to geometric objects",
            "do not treat the reduced construction as covariant",
        ),
        HandoffEntry(
            "H3: energy/stress accounting",
            "ENERGY_ACCOUNTING_REQUIRED",
            "derive or reject the energy/stress role of the narrowed survivor",
            "do not treat the response as free",
        ),
    ]


def record_governance(
    ns,
    entries: List[StatusEntry],
    results: List[ResultEntry],
    burdens: List[BurdenEntry],
    rejected: List[RejectedUpgrade],
    handoffs: List[HandoffEntry],
) -> None:
    record_marker(
        ns,
        MARKER_ID,
        "G60_term_sieve_summary",
        "Group 60 stricter term exclusion sieve summary; no physical insertion",
    )

    for idx, item in enumerate(entries, 1):
        record_claim(ns, f"{MARKER_ID}_entry_{idx}", MARKER_ID, item.status, f"{item.name}: {item.conclusion}. Boundary: {item.boundary}.")
    for idx, item in enumerate(results, 1):
        record_claim(ns, f"{MARKER_ID}_result_{idx}", MARKER_ID, item.status, f"{item.name}: {item.result}. Meaning: {item.meaning}. Boundary: {item.boundary}.")
    for idx, item in enumerate(burdens, 1):
        record_obligation(ns, f"{MARKER_ID}_burden_{idx}", f"{item.name}: {item.burden}. Discipline: {item.discipline}.", item.status)
    for idx, item in enumerate(rejected, 1):
        record_claim(ns, f"{MARKER_ID}_rejected_{idx}", MARKER_ID, "REJECTED_ROUTE", f"Rejected route: {item.upgrade}. Reason: {item.reason}.")
    for idx, item in enumerate(handoffs, 1):
        record_obligation(ns, f"{MARKER_ID}_handoff_{idx}", f"{item.name}: {item.route}. Caution: {item.caution}.", item.status)


def case_0(out: ScriptOutput) -> None:
    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  What did Group 60 establish after the stricter term exclusion sieve?\n")
    print("Discipline:\n")
    print("  This summary must preserve rejected families, narrowed survivor status, theorem gaps, and blocked physical use.")
    emit_line(out, "Group 60 status summary opened", "PASS", "closing stricter term exclusion sieve without insertion")


def case_1(out: ScriptOutput) -> None:
    header("Case 1: Group 60 compact result ledger")
    ledger = [
        ("sieve opened", "SIEVE_OPENED", "Group 60 attacked the Group 59 survivor before lift or insertion"),
        ("repair rejection", "REPAIR_TERM_REJECTED", "raw residues and counterterms rejected"),
        ("derivative narrowing", "DERIVATIVE_BURDEN_FOUND", "eta has second-derivative endpoint burden; eta^2 has stronger silence"),
        ("scalar charge rejection", "SCALAR_CHARGE_TERM_REJECTED", "eta^2 rejected as scalar response"),
        ("stress-only burden", "STRESS_ONLY_INTERPRETATION_REQUIRED", "eta^2 may survive only as stress-like closure basis"),
        ("tuning rejection", "TUNING_ROUTE_REJECTED", "constant admixture rejected"),
        ("source trace sieve", "SOURCE_TRACE_SIEVE_APPLIED", "source repair/carrying and trace double-count rejected"),
        ("closure survivor", "CLOSURE_SUPPORTED_TERM_SURVIVES", "closure-supported route survives reduced D=0"),
        ("energy burden", "ENERGY_ACCOUNTING_REQUIRED", "survivor is nonfree and needs energy/stress accounting"),
        ("narrow survivor", "TERM_SURVIVES_NARROWLY", "stress-only localized weighted-neutral-generated closure-supported response survives narrowly"),
        ("physical use", "PHYSICAL_USE_BLOCKED", "no insertion, active O, recombination, or parent closure opened"),
    ]
    for label, status, text in ledger:
        emit_line(out, label, status, text)


def case_2(out: ScriptOutput, entries: List[StatusEntry]) -> None:
    header("Case 2: Group 60 status entries")
    for item in entries:
        subheader(item.name)
        emit_line(out, item.name, item.status, f"{item.conclusion}. Boundary: {item.boundary}.")
    emit_line(out, "Group 60 status entries stated", "PASS", f"{len(entries)} status entries stated")


def case_3(out: ScriptOutput, results: List[ResultEntry]) -> None:
    header("Case 3: Exclusion sieve results")
    for item in results:
        subheader(item.name)
        print(f"Result: {item.result}")
        print(f"Meaning: {item.meaning}")
        emit_line(out, item.name, item.status, f"{item.meaning}. Boundary: {item.boundary}.")
    emit_line(out, "Group 60 results preserved", "PASS", f"{len(results)} sieve results preserved")


def case_4(out: ScriptOutput, burdens: List[BurdenEntry]) -> None:
    header("Case 4: Open burdens after Group 60")
    for item in burdens:
        subheader(item.name)
        emit_line(out, item.name, item.status, f"{item.burden}. Discipline: {item.discipline}.", obligation=True)
    emit_line(out, "Group 60 burdens preserved", "PASS", f"{len(burdens)} burdens remain explicit", obligation=True)


def case_5(out: ScriptOutput, rejected: List[RejectedUpgrade]) -> None:
    header("Case 5: Rejected term families and upgrades")
    for item in rejected:
        subheader(item.name)
        print(f"Route: {item.upgrade}")
        emit_line(out, item.name, "REJECTED_ROUTE", item.reason)
    emit_line(out, "Group 60 rejected routes preserved", "PASS", f"{len(rejected)} rejected routes preserved")


def case_6(out: ScriptOutput, handoffs: List[HandoffEntry]) -> None:
    header("Case 6: Safe handoffs")
    for item in handoffs:
        subheader(item.name)
        emit_line(out, item.name, item.status, f"{item.route}. Caution: {item.caution}.")
    emit_line(out, "Group 60 handoffs stated", "DEFERRED_WITH_TARGET", f"{len(handoffs)} handoff routes stated without opening physical use")


def case_7(out: ScriptOutput) -> None:
    header("Case 7: Final interpretation")
    conclusions = [
        ("C1: Group 60 result", "TERM_SURVIVES_NARROWLY", "candidate survived only as stress-only localized weighted-neutral-generated closure-supported response"),
        ("C2: scalar route narrowed", "STRESS_ONLY_INTERPRETATION_REQUIRED", "eta^2 is stronger at endpoints but cannot be scalar response"),
        ("C3: bad routes rejected", "REJECTED_ROUTE", "repair, scalar-charge, tuning, source/trace, radial-only, and O-disguise routes were rejected"),
        ("C4: theorem gaps", "COVARIANT_LIFT_REQUIRED", "source safety, covariant lift, divergence identity, and energy/stress accounting remain required"),
        ("C5: physical-use status", "NOT_INSERTABLE", "B_s/F_zeta insertion, active O, recombination, and parent route remain closed"),
    ]
    for label, status, text in conclusions:
        emit_line(out, label, status, text)

    header("Final summary")
    print("Group 60 status summary result:\n")
    print("  Group 60 applied a stricter exclusion sieve to the Group 59 survivor.")
    print("  It did not insert B_s/F_zeta or open a parent equation.")
    print()
    print("  Main reduced results:")
    print("    Raw R1/R2 insertion and arbitrary counterterm repair are rejected.")
    print("    w and eta have second-derivative endpoint burdens; eta^2 has stronger endpoint silence.")
    print("    eta is weighted-neutral as scalar; eta^2 is not scalar-neutral and is rejected as scalar response.")
    print("    constant admixture is rejected; b must be zero for locality/neutrality.")
    print("    source repair/carrying and trace double-counting routes are rejected.")
    print("    radial-only stress is rejected; p_t=p_r+r*p_r'/2 gives reduced D=0.")
    print("    layer stress/energy is nonfree and requires accounting.")
    print()
    print("  Narrow survivor:")
    print("    stress-only localized weighted-neutral-generated closure-supported transition response")
    print()
    print("Still required:")
    print("  source safety")
    print("  covariant layer lift")
    print("  covariant divergence identity")
    print("  energy/stress accounting")
    print()
    print("Forbidden immediate next step:")
    print("  B_s/F_zeta insertion, residue insertion, active O construction, recombination, or parent closure")


def main() -> None:
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    entries = build_status_entries()
    results = build_result_entries()
    burdens = build_burdens()
    rejected = build_rejected()
    handoffs = build_handoffs()

    case_0(out)
    case_1(out)
    case_2(out, entries)
    case_3(out, results)
    case_4(out, burdens)
    case_5(out, rejected)
    case_6(out, handoffs)
    case_7(out)

    record_governance(ns, entries, results, burdens, rejected, handoffs)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
