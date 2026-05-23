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
SCRIPT_LABEL = "Candidate Group 58 Status Summary"
MARKER_ID = "g58_summary"

DEPENDENCIES = [
    ("g57_summary", "057_layer_unify_probe__candidate_group_57_status_summary", "g57_summary"),
    ("g58_problem", "058_weighted_neutral_layer__candidate_weighted_problem", "g58_problem"),
    ("g58_profile", "058_weighted_neutral_layer__candidate_weighted_profile", "g58_profile"),
    ("g58_compare", "058_weighted_neutral_layer__candidate_flat_vs_weighted", "g58_compare"),
    ("g58_energy", "058_weighted_neutral_layer__candidate_weighted_energy", "g58_energy"),
    ("g58_tailmass", "058_weighted_neutral_layer__candidate_tail_mass_zero", "g58_tailmass"),
    ("g58_div", "058_weighted_neutral_layer__candidate_weighted_divergence", "g58_div"),
    ("g58_class", "058_weighted_neutral_layer__candidate_weighted_route_classifier", "g58_class"),
    ("g58_reconcile", "058_weighted_neutral_layer__candidate_weighted_batch_reconcile", "g58_reconcile"),
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
        "WEIGHTED_LAYER_PROBLEM_OPENED": StatusMark.INFO,
        "WEIGHTED_NEUTRAL_PROFILE_DERIVED": StatusMark.PASS,
        "GEOMETRIC_SKEW_DERIVED": StatusMark.PASS,
        "FLAT_NEUTRALITY_REJECTED": StatusMark.FAIL,
        "WEIGHTED_NEUTRALITY_CONFIRMED": StatusMark.PASS,
        "LOCALIZED_LAYER_PROFILE_DERIVED": StatusMark.PASS,
        "WEIGHTED_ENERGY_CONDITION_DERIVED": StatusMark.PASS,
        "TAIL_MASS_ZERO_CONFIRMED": StatusMark.PASS,
        "WEIGHTED_DIVERGENCE_CLOSURE_DERIVED": StatusMark.PASS,
        "WEIGHTED_LAYER_ROUTE_SURVIVES_CONDITIONALLY": StatusMark.INFO,
        "UNIFICATION_PROBE_SURVIVES_CONDITIONALLY": StatusMark.INFO,
        "CANDIDATE_TERM_SURFACE_OPENED": StatusMark.INFO,
        "COVARIANT_LIFT_REQUIRED": StatusMark.OBLIGATION,
        "ENERGY_ACCOUNTING_REQUIRED": StatusMark.OBLIGATION,
        "CHARGE_NEUTRALITY_REQUIRED": StatusMark.OBLIGATION,
        "DIVERGENCE_IDENTITY_REQUIRED": StatusMark.OBLIGATION,
        "SAFETY_THEOREMS_REQUIRED": StatusMark.OBLIGATION,
        "SOURCE_SAFETY_REQUIRED": StatusMark.OBLIGATION,
        "PHYSICAL_USE_BLOCKED": StatusMark.DEFER,
        "NOT_INSERTABLE": StatusMark.DEFER,
        "ACTIVE_O_NECESSITY_NOT_ESTABLISHED": StatusMark.DEFER,
        "DEFERRED_WITH_TARGET": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REJECTED_ROUTE": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
    }.get(status, StatusMark.INFO)


def governance_status(status: str) -> GovernanceStatus:
    if status in {"REJECTED_ROUTE", "FORBIDDEN_SHORTCUT", "FLAT_NEUTRALITY_REJECTED"}:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {
        "COVARIANT_LIFT_REQUIRED",
        "ENERGY_ACCOUNTING_REQUIRED",
        "CHARGE_NEUTRALITY_REQUIRED",
        "DIVERGENCE_IDENTITY_REQUIRED",
        "SAFETY_THEOREMS_REQUIRED",
        "SOURCE_SAFETY_REQUIRED",
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
            "G58-1: weighted-neutral construction",
            "WEIGHTED_LAYER_PROBLEM_OPENED",
            "Group 58 directly attacked the weighted layer-neutrality blocker from Group 57",
            "not parent equation",
        ),
        StatusEntry(
            "G58-2: route status",
            "WEIGHTED_LAYER_ROUTE_SURVIVES_CONDITIONALLY",
            "the weighted-neutral finite-layer route survives conditionally as a reduced theorem surface",
            "not insertable",
        ),
        StatusEntry(
            "G58-3: flat neutrality",
            "FLAT_NEUTRALITY_REJECTED",
            "flat odd cancellation remains rejected as a sufficient neutrality condition",
            "rejected shortcut",
        ),
        StatusEntry(
            "G58-4: physical use",
            "PHYSICAL_USE_BLOCKED",
            "candidate remains audit-only and blocked for physical use",
            "not parent-ready",
        ),
    ]


def build_result_entries() -> List[ResultEntry]:
    return [
        ResultEntry(
            "C1: weighted-neutral profile",
            "WEIGHTED_NEUTRAL_PROFILE_DERIVED",
            "rho=rho0*(1-y^2)^2*(y-c*) with c*=2Rell/(7R^2+ell^2)",
            "nontrivial localized profile has exactly zero weighted charge",
            "reduced theorem surface",
        ),
        ResultEntry(
            "C2: geometric skew",
            "GEOMETRIC_SKEW_DERIVED",
            "c*=2Rell/(7R^2+ell^2)",
            "profile asymmetry is forced by spherical weighting, not arbitrary tuning",
            "radial/reduced",
        ),
        ResultEntry(
            "C3: flat comparison",
            "FLAT_NEUTRALITY_REJECTED",
            "rho_odd=rho1*y has Q_flat=0 but Q_weighted=4Rell*rho1/3",
            "flat neutrality is not the physical reduced target",
            "rejected shortcut",
        ),
        ResultEntry(
            "C4: weighted target",
            "WEIGHTED_NEUTRALITY_CONFIRMED",
            "weighted profile has Q_weighted=0 even though its flat charge need not vanish",
            "spherical weighted charge is the correct target",
            "reduced",
        ),
        ResultEntry(
            "C5: energy",
            "WEIGHTED_ENERGY_CONDITION_DERIVED",
            "E=256*rho0^2*(49R^4+26R^2ell^2+ell^4)/(315ell*(7R^2+ell^2)^2)",
            "neutrality is finite-energy for finite ell but nonfree",
            "not stress theorem",
        ),
        ResultEntry(
            "C6: tail and mass",
            "TAIL_MASS_ZERO_CONFIRMED",
            "Q_weighted=0 gives phi_ext=C0 and Delta_M=0; with C0=0, phi_ext=0",
            "reduced Q-driven tail and mass diagnostics vanish conditionally",
            "not full theorem",
        ),
        ResultEntry(
            "C7: divergence closure",
            "WEIGHTED_DIVERGENCE_CLOSURE_DERIVED",
            "p_r proportional to weighted shape squared with p_t=p_r+r*p_r'/2 gives D=0",
            "weighted-neutral layer can be reduced-divergence silent",
            "not Bianchi proof",
        ),
    ]


def build_burdens() -> List[BurdenEntry]:
    return [
        BurdenEntry(
            "B1: source safety",
            "SOURCE_SAFETY_REQUIRED",
            "prove weighted-neutral layer does not duplicate ordinary source load",
            "protect A-sector source routing",
        ),
        BurdenEntry(
            "B2: candidate transition-term audit",
            "DEFERRED_WITH_TARGET",
            "test whether weighted layer shape/residues define admissible transition response terms",
            "avoid repair insertion",
        ),
        BurdenEntry(
            "B3: covariant lift",
            "COVARIANT_LIFT_REQUIRED",
            "lift weighted measure and skew to geometric layer formalism",
            "avoid radial-only proof",
        ),
        BurdenEntry(
            "B4: covariant divergence identity",
            "DIVERGENCE_IDENTITY_REQUIRED",
            "lift reduced D=0 closure to covariant identity structure",
            "avoid parent overclaim",
        ),
        BurdenEntry(
            "B5: energy/stress accounting",
            "ENERGY_ACCOUNTING_REQUIRED",
            "lift finite reduced profile energy to admissible stress accounting",
            "avoid free neutral profile",
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
        RejectedUpgrade("R1: weighted profile as insertion", "insert B_s/F_zeta because Q_weighted=0", "no insertion occurred"),
        RejectedUpgrade("R2: weighted neutrality as full safety", "write Q_weighted=0 as all boundary/source/covariant safety closed", "source safety and covariant lift remain"),
        RejectedUpgrade("R3: radial profile as covariant theorem", "write the reduced profile as covariant layer theory", "lift remains required"),
        RejectedUpgrade("R4: reduced D=0 as parent closure", "use reduced D=0 to open parent equation", "not a Bianchi proof"),
        RejectedUpgrade("R5: flat odd neutrality", "treat Q_flat=0 as physical neutrality", "spherical weighted charge is the target"),
    ]


def build_handoffs() -> List[HandoffEntry]:
    return [
        HandoffEntry(
            "H1: candidate transition-term audit",
            "DEFERRED_WITH_TARGET",
            "use the weighted-neutral shape and earlier blend residues to test admissible layer response terms",
            "do not insert residues as repairs",
        ),
        HandoffEntry(
            "H2: covariant weighted-layer lift",
            "COVARIANT_LIFT_REQUIRED",
            "replace r=R+ell*y and weighted measure with geometric layer/area-measure formalism",
            "do not treat the reduced construction as already covariant",
        ),
        HandoffEntry(
            "H3: source safety audit",
            "SOURCE_SAFETY_REQUIRED",
            "test whether weighted-neutral layer response duplicates ordinary source load",
            "do not treat Q=0 as source role-purity",
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
        "G58_weighted_neutral_summary",
        "Group 58 weighted-neutral finite-layer route summary; no physical insertion",
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
    print("  What did Group 58 establish about weighted-neutral finite transition layers?\n")
    print("Discipline:\n")
    print("  This summary must preserve constructive weighted-neutral progress, rejected flat neutrality,")
    print("  reduced-only scope, source/covariant gaps, and blocked physical use.")
    emit_line(out, "Group 58 status summary opened", "PASS", "closing weighted-neutral finite-layer construction group without insertion")


def case_1(out: ScriptOutput) -> None:
    header("Case 1: Group 58 compact result ledger")
    ledger = [
        ("weighted problem", "WEIGHTED_LAYER_PROBLEM_OPENED", "Group 58 directly attacked the Group 57 weighted-neutrality blocker"),
        ("profile", "WEIGHTED_NEUTRAL_PROFILE_DERIVED", "nontrivial localized weighted-neutral profile exists"),
        ("geometric skew", "GEOMETRIC_SKEW_DERIVED", "c*=2Rell/(7R^2+ell^2) is forced by spherical weighting"),
        ("flat rejection", "FLAT_NEUTRALITY_REJECTED", "flat odd cancellation remains insufficient"),
        ("energy", "WEIGHTED_ENERGY_CONDITION_DERIVED", "weighted-neutral profile has finite explicit reduced energy"),
        ("tail/mass", "TAIL_MASS_ZERO_CONFIRMED", "Q=0 kills reduced Q-driven tail and mass diagnostics"),
        ("divergence", "WEIGHTED_DIVERGENCE_CLOSURE_DERIVED", "weighted shape supports reduced D=0 closure"),
        ("route status", "WEIGHTED_LAYER_ROUTE_SURVIVES_CONDITIONALLY", "weighted-neutral route survives conditionally"),
        ("physical use", "PHYSICAL_USE_BLOCKED", "no insertion, active O, recombination, or parent closure opened"),
    ]
    for label, status, text in ledger:
        emit_line(out, label, status, text)


def case_2(out: ScriptOutput, entries: List[StatusEntry]) -> None:
    header("Case 2: Group 58 status entries")
    for item in entries:
        subheader(item.name)
        emit_line(out, item.name, item.status, f"{item.conclusion}. Boundary: {item.boundary}.")
    emit_line(out, "Group 58 status entries stated", "PASS", f"{len(entries)} status entries stated")


def case_3(out: ScriptOutput, results: List[ResultEntry]) -> None:
    header("Case 3: Weighted-neutral finite-layer results")
    for item in results:
        subheader(item.name)
        print(f"Result: {item.result}")
        print(f"Meaning: {item.meaning}")
        emit_line(out, item.name, item.status, f"{item.meaning}. Boundary: {item.boundary}.")
    emit_line(out, "Group 58 results preserved", "PASS", f"{len(results)} weighted-layer results preserved")


def case_4(out: ScriptOutput, burdens: List[BurdenEntry]) -> None:
    header("Case 4: Open burdens after Group 58")
    for item in burdens:
        subheader(item.name)
        emit_line(out, item.name, item.status, f"{item.burden}. Discipline: {item.discipline}.", obligation=True)
    emit_line(out, "Group 58 burdens preserved", "PASS", f"{len(burdens)} burdens remain explicit", obligation=True)


def case_5(out: ScriptOutput, rejected: List[RejectedUpgrade]) -> None:
    header("Case 5: Rejected summary upgrades")
    for item in rejected:
        subheader(item.name)
        print(f"Upgrade: {item.upgrade}")
        emit_line(out, item.name, "REJECTED_ROUTE", item.reason)
    emit_line(out, "Group 58 rejected upgrades preserved", "PASS", f"{len(rejected)} upgrade shortcuts rejected")


def case_6(out: ScriptOutput, handoffs: List[HandoffEntry]) -> None:
    header("Case 6: Safe handoffs")
    for item in handoffs:
        subheader(item.name)
        emit_line(out, item.name, item.status, f"{item.route}. Caution: {item.caution}.")
    emit_line(out, "Group 58 handoffs stated", "DEFERRED_WITH_TARGET", f"{len(handoffs)} handoff routes stated without opening physical use")


def case_7(out: ScriptOutput) -> None:
    header("Case 7: Final interpretation")
    conclusions = [
        ("C1: Group 58 result", "WEIGHTED_LAYER_ROUTE_SURVIVES_CONDITIONALLY", "weighted-neutral finite-layer route survives conditionally as a reduced theorem surface"),
        ("C2: blocker status", "PASS", "the Group 57 weighted-neutrality blocker has a constructive reduced answer"),
        ("C3: flat neutrality", "FLAT_NEUTRALITY_REJECTED", "flat odd cancellation remains rejected"),
        ("C4: theorem gap", "COVARIANT_LIFT_REQUIRED", "source safety, candidate-term audit, and covariant lift remain required"),
        ("C5: physical-use status", "NOT_INSERTABLE", "B_s/F_zeta insertion, active O, recombination, and parent route remain closed"),
    ]
    for label, status, text in conclusions:
        emit_line(out, label, status, text)

    header("Final summary")
    print("Group 58 status summary result:\n")
    print("  Group 58 constructed a nontrivial weighted-neutral finite-layer profile.")
    print("  It did not insert B_s/F_zeta or open a parent equation.")
    print()
    print("  Main reduced results:")
    print("    rho=rho0*(1-y^2)^2*(y-c*)")
    print("    c*=2Rell/(7R^2+ell^2)")
    print("    integral (R+ell*y)^2 rho dy = 0")
    print("    flat odd cancellation remains rejected")
    print("    weighted profile energy is finite for finite ell")
    print("    Q=0 kills reduced Q-driven exterior tail and mass diagnostics")
    print("    weighted shape supports reduced D=0 closure")
    print()
    print("  The weighted-neutral route survives conditionally as a reduced theorem surface.")
    print("  It still requires source safety, candidate transition-term audit, covariant lift,")
    print("  covariant divergence identity support, and energy/stress accounting.")
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
