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
SCRIPT_LABEL = "Candidate Group 59 Status Summary"
MARKER_ID = "g59_summary"

DEPENDENCIES = [
    ("g58_summary", "058_weighted_neutral_layer__candidate_group_58_status_summary", "g58_summary"),
    ("g59_problem", "059_transition_term_audit__candidate_transition_problem", "g59_problem"),
    ("g59_inv", "059_transition_term_audit__candidate_residue_inventory", "g59_inv"),
    ("g59_loc", "059_transition_term_audit__candidate_locality_filter", "g59_loc"),
    ("g59_neu", "059_transition_term_audit__candidate_weighted_neutralizer", "g59_neu"),
    ("g59_src", "059_transition_term_audit__candidate_source_trace_filter", "g59_src"),
    ("g59_div", "059_transition_term_audit__candidate_divergence_filter", "g59_div"),
    ("g59_class", "059_transition_term_audit__candidate_transition_route_classifier", "g59_class"),
    ("g59_reconcile", "059_transition_term_audit__candidate_transition_batch_reconcile", "g59_reconcile"),
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
            "G59-1: transition audit",
            "TRANSITION_AUDIT_OPENED",
            "Group 59 opened a candidate transition-term audit using finite-layer residues and weighted-neutral shapes",
            "not insertion",
        ),
        StatusEntry(
            "G59-2: candidate surface",
            "CANDIDATE_TERM_SURFACE_OPENED",
            "transition-response candidate surfaces were generated and filtered",
            "not adopted terms",
        ),
        StatusEntry(
            "G59-3: survivor",
            "TRANSITION_TERM_SURVIVES_CONDITIONALLY",
            "a narrow localized weighted-neutral closure-supported transition response survives conditionally",
            "not insertable",
        ),
        StatusEntry(
            "G59-4: physical use",
            "PHYSICAL_USE_BLOCKED",
            "candidate remains audit-only and blocked for physical use",
            "not parent-ready",
        ),
    ]


def build_result_entries() -> List[ResultEntry]:
    return [
        ResultEntry(
            "C1: residue inventory",
            "RESIDUE_INVENTORY_DERIVED",
            "R1=(F_out-F_in)s' and R2=(F_out-F_in)s''+2(F_out'-F_in')s'",
            "blend residues are candidate clues, not inserted terms",
            "not parent equation",
        ),
        ResultEntry(
            "C2: weighted layer basis",
            "WEIGHTED_NEUTRALITY_CONFIRMED",
            "eta=w(y)*(y-c*) and eta^2 were inventoried as scalar/stress-like bases",
            "Group 58 shape seeds candidate surfaces",
            "reduced",
        ),
        ResultEntry(
            "C3: locality",
            "LOCALITY_FILTER_APPLIED",
            "w, eta, and eta^2 vanish with zero derivative at endpoints; constant term rejected",
            "candidate layer terms must be endpoint-localized",
            "not covariant compact support",
        ),
        ResultEntry(
            "C4: weighted neutralizer",
            "WEIGHTED_NEUTRALIZER_DERIVED",
            "N_w[f]=w(f-mu_w[f]) with mu_w[f]=int r^2wf/int r^2w",
            "weighted-neutral candidate profiles can be generated systematically",
            "not active O",
        ),
        ResultEntry(
            "C5: Group 58 recovery",
            "WEIGHTED_NEUTRALITY_CONFIRMED",
            "mu_w[y]=2Rell/(7R^2+ell^2) and int r^2N_w[y]dy=0",
            "neutralizer reproduces Group 58 skew and weighted charge zero",
            "not source safety",
        ),
        ResultEntry(
            "C6: source/trace filter",
            "SOURCE_TRACE_FILTER_APPLIED",
            "source-carrying and trace-double-counting transition terms were rejected",
            "ordinary source and trace count are protected conditionally",
            "not full theorem",
        ),
        ResultEntry(
            "C7: divergence filter",
            "DIVERGENCE_FILTER_APPLIED",
            "radial-only stress failed; p_t=p_r+r p_r'/2 closure gives D=0",
            "candidate stress needs tangential closure",
            "not Bianchi proof",
        ),
        ResultEntry(
            "C8: surviving candidate family",
            "TRANSITION_TERM_SURVIVES_CONDITIONALLY",
            "localized weighted-neutral closure-supported transition response",
            "narrow candidate family survives the reduced filters",
            "not insertable",
        ),
    ]


def build_burdens() -> List[BurdenEntry]:
    return [
        BurdenEntry(
            "B1: source safety",
            "SOURCE_SAFETY_REQUIRED",
            "prove surviving transition response does not duplicate ordinary source load",
            "protect A-sector source routing",
        ),
        BurdenEntry(
            "B2: covariant lift",
            "COVARIANT_LIFT_REQUIRED",
            "lift neutralizer, locality, weighted measure, and closure to geometric layer formalism",
            "avoid radial-only proof",
        ),
        BurdenEntry(
            "B3: candidate-equation sieve",
            "DEFERRED_WITH_TARGET",
            "apply stricter candidate-equation exclusion sieve before any insertion",
            "avoid repair terms",
        ),
        BurdenEntry(
            "B4: divergence identity",
            "DIVERGENCE_IDENTITY_REQUIRED",
            "lift reduced D=0 closure to covariant identity structure",
            "avoid parent overclaim",
        ),
        BurdenEntry(
            "B5: energy/stress accounting",
            "ENERGY_ACCOUNTING_REQUIRED",
            "connect closure-supported candidate response to admissible energy/stress accounting",
            "avoid free transition response",
        ),
        BurdenEntry(
            "B6: physical-use block",
            "NOT_INSERTABLE",
            "keep insertion, active O, recombination, and parent closure closed",
            "avoid status inflation",
        ),
    ]


def build_rejected() -> List[RejectedUpgrade]:
    return [
        RejectedUpgrade("R1: residue repair", "insert R1/R2 directly as correction tensors", "residues are clues only"),
        RejectedUpgrade("R2: nonlocal layer term", "allow constant transition term", "constant term leaks outside layer endpoints"),
        RejectedUpgrade("R3: neutralizer as active O", "rename N_w as full no-overlap operator", "N_w is only a reduced scalar neutralizer"),
        RejectedUpgrade("R4: Q=0 as source safety", "claim weighted charge zero proves no source duplication", "source safety remains separate"),
        RejectedUpgrade("R5: source-carrying transition", "let transition term carry ordinary source load", "ordinary source duplication is forbidden"),
        RejectedUpgrade("R6: trace double-count", "let transition term add trace payload with B_s", "trace double-counting is forbidden"),
        RejectedUpgrade("R7: radial-only stress", "accept p_r without tangential closure", "reduced divergence fails"),
        RejectedUpgrade("R8: reduced D=0 as parent identity", "treat closure route as Bianchi proof", "covariant lift remains required"),
    ]


def build_handoffs() -> List[HandoffEntry]:
    return [
        HandoffEntry(
            "H1: candidate-equation exclusion sieve",
            "DEFERRED_WITH_TARGET",
            "run a stricter sieve on the surviving localized weighted-neutral closure-supported transition response",
            "do not insert it first",
        ),
        HandoffEntry(
            "H2: source safety audit",
            "SOURCE_SAFETY_REQUIRED",
            "test whether the surviving transition response duplicates ordinary source load",
            "do not treat Q=0 as source role-purity",
        ),
        HandoffEntry(
            "H3: covariant layer lift",
            "COVARIANT_LIFT_REQUIRED",
            "replace reduced N_w/locality/closure with geometric layer objects",
            "do not treat reduced construction as covariant",
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
        "G59_transition_audit_summary",
        "Group 59 transition-term audit summary; no physical insertion",
    )

    for idx, item in enumerate(entries, 1):
        record_claim(ns, f"{MARKER_ID}_entry_{idx}", MARKER_ID, item.status, f"{item.name}: {item.conclusion}. Boundary: {item.boundary}.")
    for idx, item in enumerate(results, 1):
        record_claim(ns, f"{MARKER_ID}_result_{idx}", MARKER_ID, item.status, f"{item.name}: {item.result}. Meaning: {item.meaning}. Boundary: {item.boundary}.")
    for idx, item in enumerate(burdens, 1):
        record_obligation(ns, f"{MARKER_ID}_burden_{idx}", f"{item.name}: {item.burden}. Discipline: {item.discipline}.", item.status)
    for idx, item in enumerate(rejected, 1):
        record_claim(ns, f"{MARKER_ID}_rejected_{idx}", MARKER_ID, "REJECTED_ROUTE", f"Rejected upgrade: {item.upgrade}. Reason: {item.reason}.")
    for idx, item in enumerate(handoffs, 1):
        record_obligation(ns, f"{MARKER_ID}_handoff_{idx}", f"{item.name}: {item.route}. Caution: {item.caution}.", item.status)


def case_0(out: ScriptOutput) -> None:
    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  What did Group 59 establish about transition-term candidate surfaces?\n")
    print("Discipline:\n")
    print("  This summary must preserve candidate-surface progress, rejected repair/source/trace/divergence routes,")
    print("  reduced-only scope, and blocked physical use.")
    emit_line(out, "Group 59 status summary opened", "PASS", "closing transition-term audit without insertion")


def case_1(out: ScriptOutput) -> None:
    header("Case 1: Group 59 compact result ledger")
    ledger = [
        ("transition audit", "TRANSITION_AUDIT_OPENED", "candidate transition-term audit opened"),
        ("residue inventory", "RESIDUE_INVENTORY_DERIVED", "R1/R2 residues inventoried as clues"),
        ("locality", "LOCALITY_FILTER_APPLIED", "localized bases retained and constant term rejected"),
        ("neutralizer", "WEIGHTED_NEUTRALIZER_DERIVED", "N_w[f] derived and Group 58 skew recovered"),
        ("weighted charge", "WEIGHTED_NEUTRALITY_CONFIRMED", "N_w[y] has zero weighted charge"),
        ("source/trace", "SOURCE_TRACE_FILTER_APPLIED", "source-carrying and trace-double-counting routes rejected"),
        ("divergence", "DIVERGENCE_FILTER_APPLIED", "radial-only stress rejected; closure route survives"),
        ("candidate survivor", "TRANSITION_TERM_SURVIVES_CONDITIONALLY", "localized weighted-neutral closure-supported response survives conditionally"),
        ("physical use", "PHYSICAL_USE_BLOCKED", "no insertion, active O, recombination, or parent closure opened"),
    ]
    for label, status, text in ledger:
        emit_line(out, label, status, text)


def case_2(out: ScriptOutput, entries: List[StatusEntry]) -> None:
    header("Case 2: Group 59 status entries")
    for item in entries:
        subheader(item.name)
        emit_line(out, item.name, item.status, f"{item.conclusion}. Boundary: {item.boundary}.")
    emit_line(out, "Group 59 status entries stated", "PASS", f"{len(entries)} status entries stated")


def case_3(out: ScriptOutput, results: List[ResultEntry]) -> None:
    header("Case 3: Transition-term audit results")
    for item in results:
        subheader(item.name)
        print(f"Result: {item.result}")
        print(f"Meaning: {item.meaning}")
        emit_line(out, item.name, item.status, f"{item.meaning}. Boundary: {item.boundary}.")
    emit_line(out, "Group 59 results preserved", "PASS", f"{len(results)} transition audit results preserved")


def case_4(out: ScriptOutput, burdens: List[BurdenEntry]) -> None:
    header("Case 4: Open burdens after Group 59")
    for item in burdens:
        subheader(item.name)
        emit_line(out, item.name, item.status, f"{item.burden}. Discipline: {item.discipline}.", obligation=True)
    emit_line(out, "Group 59 burdens preserved", "PASS", f"{len(burdens)} burdens remain explicit", obligation=True)


def case_5(out: ScriptOutput, rejected: List[RejectedUpgrade]) -> None:
    header("Case 5: Rejected summary upgrades and term families")
    for item in rejected:
        subheader(item.name)
        print(f"Upgrade: {item.upgrade}")
        emit_line(out, item.name, "REJECTED_ROUTE", item.reason)
    emit_line(out, "Group 59 rejected routes preserved", "PASS", f"{len(rejected)} rejected routes preserved")


def case_6(out: ScriptOutput, handoffs: List[HandoffEntry]) -> None:
    header("Case 6: Safe handoffs")
    for item in handoffs:
        subheader(item.name)
        emit_line(out, item.name, item.status, f"{item.route}. Caution: {item.caution}.")
    emit_line(out, "Group 59 handoffs stated", "DEFERRED_WITH_TARGET", f"{len(handoffs)} handoff routes stated without opening physical use")


def case_7(out: ScriptOutput) -> None:
    header("Case 7: Final interpretation")
    conclusions = [
        ("C1: Group 59 result", "TRANSITION_TERM_SURVIVES_CONDITIONALLY", "a narrow localized weighted-neutral closure-supported transition response survives conditionally"),
        ("C2: neutralizer status", "WEIGHTED_NEUTRALIZER_DERIVED", "N_w generalizes the Group 58 weighted-neutral construction"),
        ("C3: rejected routes", "REJECTED_ROUTE", "nonlocal, repair, source-carrying, trace-double-counting, and divergence-failing routes were rejected"),
        ("C4: theorem gap", "COVARIANT_LIFT_REQUIRED", "source safety, covariant lift, candidate-equation sieve, and divergence identity remain required"),
        ("C5: physical-use status", "NOT_INSERTABLE", "B_s/F_zeta insertion, active O, recombination, and parent route remain closed"),
    ]
    for label, status, text in conclusions:
        emit_line(out, label, status, text)

    header("Final summary")
    print("Group 59 status summary result:\n")
    print("  Group 59 opened and filtered a transition-term candidate surface.")
    print("  It did not insert B_s/F_zeta or open a parent equation.")
    print()
    print("  Main reduced results:")
    print("    R1=(F_out-F_in)s' and R2=(F_out-F_in)s''+2(F_out'-F_in')s' are clues, not inserted terms.")
    print("    w, eta, and eta^2 are endpoint-local; constant terms are rejected.")
    print("    N_w[f]=w(f-mu_w[f]) generates weighted-neutral scalar layer candidates.")
    print("    mu_w[y]=2Rell/(7R^2+ell^2), reproducing Group 58 skew.")
    print("    Source-carrying and trace-double-counting terms are rejected.")
    print("    Radial-only stress is rejected; closure p_t=p_r+r p_r'/2 gives reduced D=0.")
    print()
    print("  Surviving candidate family:")
    print("    localized weighted-neutral closure-supported transition response")
    print()
    print("Still required:")
    print("  source safety")
    print("  covariant layer lift")
    print("  stricter candidate-equation exclusion sieve")
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
