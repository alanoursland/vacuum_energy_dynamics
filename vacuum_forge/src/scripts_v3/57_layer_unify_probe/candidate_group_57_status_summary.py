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
SCRIPT_LABEL = "Candidate Group 57 Status Summary"
MARKER_ID = "g57_summary"

DEPENDENCIES = [
    ("g56_summary", "56_silent_insert_law__candidate_group_56_status_summary", "g56_summary"),
    ("g57_problem", "57_layer_unify_probe__candidate_layer_problem", "g57_problem"),
    ("g57_s", "57_layer_unify_probe__candidate_smoothstep_profile", "g57_s"),
    ("g57_res", "57_layer_unify_probe__candidate_blend_residue", "g57_res"),
    ("g57_energy", "57_layer_unify_probe__candidate_layer_energy", "g57_energy"),
    ("g57_qm", "57_layer_unify_probe__candidate_layer_charge_mass", "g57_qm"),
    ("g57_div", "57_layer_unify_probe__candidate_layer_divergence", "g57_div"),
    ("g57_class", "57_layer_unify_probe__candidate_layer_route_classifier", "g57_class"),
    ("g57_reconcile", "57_layer_unify_probe__candidate_layer_batch_reconcile", "g57_reconcile"),
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
        "LAYER_PROBE_OPENED": StatusMark.INFO,
        "SMOOTHSTEP_PROFILE_DERIVED": StatusMark.PASS,
        "BLEND_RESIDUE_DERIVED": StatusMark.PASS,
        "LAYER_RESIDUE_LOCALIZED": StatusMark.INFO,
        "LAYER_ENERGY_CONDITION_DERIVED": StatusMark.PASS,
        "LAYER_CHARGE_CONDITION_DERIVED": StatusMark.PASS,
        "LAYER_MASS_SHIFT_CONDITION_DERIVED": StatusMark.PASS,
        "LAYER_DIVERGENCE_CLOSURE_DERIVED": StatusMark.PASS,
        "LAYER_ROUTE_SURVIVES_CONDITIONALLY": StatusMark.INFO,
        "UNIFICATION_PROBE_SURVIVES_CONDITIONALLY": StatusMark.INFO,
        "CANDIDATE_TERM_SURFACE_OPENED": StatusMark.INFO,
        "COVARIANT_LIFT_REQUIRED": StatusMark.OBLIGATION,
        "ENERGY_ACCOUNTING_REQUIRED": StatusMark.OBLIGATION,
        "CHARGE_NEUTRALITY_REQUIRED": StatusMark.OBLIGATION,
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
    if status in {"REJECTED_ROUTE", "FORBIDDEN_SHORTCUT"}:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {
        "COVARIANT_LIFT_REQUIRED",
        "ENERGY_ACCOUNTING_REQUIRED",
        "CHARGE_NEUTRALITY_REQUIRED",
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
            "G57-1: finite layer probe",
            "LAYER_PROBE_OPENED",
            "Group 57 replaced the hard-boundary-only picture with a finite transition-layer unification probe",
            "not parent equation",
        ),
        StatusEntry(
            "G57-2: route status",
            "UNIFICATION_PROBE_SURVIVES_CONDITIONALLY",
            "the finite-layer route survives conditionally as a diagnostic unification probe",
            "not insertable",
        ),
        StatusEntry(
            "G57-3: candidate term status",
            "CANDIDATE_TERM_SURFACE_OPENED",
            "blend residues can guide candidate transition terms",
            "not adopted field-equation terms",
        ),
        StatusEntry(
            "G57-4: physical use",
            "PHYSICAL_USE_BLOCKED",
            "candidate remains audit-only and blocked for physical use",
            "not parent-ready",
        ),
    ]


def build_result_entries() -> List[ResultEntry]:
    return [
        ResultEntry(
            "C1: smoothstep layer",
            "SMOOTHSTEP_PROFILE_DERIVED",
            "s(x)=10x^3-15x^4+6x^5 with endpoint value/slope/curvature control",
            "finite layer can match interior/exterior smoothly in the reduced model",
            "not physical law",
        ),
        ResultEntry(
            "C2: blend residues",
            "BLEND_RESIDUE_DERIVED",
            "R1=(F_out-F_in)s' and R2=(F_out-F_in)s''+2(F_out'-F_in')s'",
            "transition residues expose the terms a unified rule must explain",
            "not inserted",
        ),
        ResultEntry(
            "C3: layer energy",
            "LAYER_ENERGY_CONDITION_DERIVED",
            "E_layer=5*A^2/(7*ell)",
            "finite layer has explicit cost and hard-shell limit is costly",
            "not full stress theorem",
        ),
        ResultEntry(
            "C4: charge/mass warning",
            "LAYER_CHARGE_CONDITION_DERIVED",
            "odd flat profile gives Q_flat=0 but weighted Q=4*R*ell^2*rho1/3",
            "spherical weighting can spoil naive layer neutrality",
            "neutrality not closed",
        ),
        ResultEntry(
            "C5: mass shift diagnostic",
            "LAYER_MASS_SHIFT_CONDITION_DERIVED",
            "Delta_M_layer=4*R*alpha*ell^2*rho1/3",
            "net layer charge can shift mass unless neutralized",
            "conditional",
        ),
        ResultEntry(
            "C6: layer divergence",
            "LAYER_DIVERGENCE_CLOSURE_DERIVED",
            "p_r proportional to [s(1-s)]^2 with p_t=p_r+r*p_r'/2 gives D=0",
            "layer-local stress can be reduced-divergence silent",
            "not Bianchi proof",
        ),
    ]


def build_burdens() -> List[BurdenEntry]:
    return [
        BurdenEntry(
            "B1: weighted neutrality",
            "CHARGE_NEUTRALITY_REQUIRED",
            "construct or derive a weighted zero-charge finite-layer profile",
            "avoid exterior scalar tail and mass shift",
        ),
        BurdenEntry(
            "B2: layer candidate terms",
            "DEFERRED_WITH_TARGET",
            "audit whether blend residues define admissible transition candidate terms",
            "avoid repair insertion",
        ),
        BurdenEntry(
            "B3: energy/stress accounting",
            "ENERGY_ACCOUNTING_REQUIRED",
            "lift reduced layer energy cost into admissible stress/response accounting",
            "avoid free blending",
        ),
        BurdenEntry(
            "B4: covariant lift",
            "COVARIANT_LIFT_REQUIRED",
            "lift finite-layer coordinate, profile, residues, and stress closure to geometric form",
            "avoid reduced overclaim",
        ),
        BurdenEntry(
            "B5: divergence identity",
            "DIVERGENCE_IDENTITY_REQUIRED",
            "lift reduced D=0 closure to covariant identity structure",
            "avoid parent overclaim",
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
        RejectedUpgrade("R1: layer as parent equation", "write finite-layer probe as parent equation", "no parent equation was opened"),
        RejectedUpgrade("R2: residues as insertion", "insert blend residues as B_s/F_zeta terms or repair tensors", "residues are diagnostics"),
        RejectedUpgrade("R3: smoothness as neutrality", "treat endpoint smoothness as charge/mass neutrality", "weighted neutrality remains required"),
        RejectedUpgrade("R4: reduced D=0 as Bianchi proof", "read reduced radial divergence closure as covariant identity", "covariant lift remains required"),
        RejectedUpgrade("R5: odd profile as neutrality", "claim flat odd cancellation proves spherical neutrality", "r^2 weighting can spoil cancellation"),
    ]


def build_handoffs() -> List[HandoffEntry]:
    return [
        HandoffEntry(
            "H1: weighted-neutral layer construction",
            "DEFERRED_WITH_TARGET",
            "construct a finite-layer profile with weighted Q_layer=0 while remaining nontrivial",
            "do not assume odd flat symmetry is sufficient",
        ),
        HandoffEntry(
            "H2: candidate transition term audit",
            "DEFERRED_WITH_TARGET",
            "test whether blend residues can be organized into admissible transition response terms",
            "do not insert residues as repair tensors",
        ),
        HandoffEntry(
            "H3: covariant layer lift",
            "COVARIANT_LIFT_REQUIRED",
            "replace radial layer coordinate with geometric distance-to-boundary or transition scalar structure",
            "do not treat the reduced layer as already covariant",
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
        "G57_layer_unify_summary",
        "Group 57 finite-layer unification probe summary; no physical insertion",
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
    print("  What did Group 57 establish about finite transition-layer unification diagnostics?\n")
    print("Discipline:\n")
    print("  This summary must preserve finite-layer diagnostic progress, the weighted-neutrality warning,")
    print("  candidate-term status, covariant-lift burden, and blocked physical use.")
    emit_line(out, "Group 57 status summary opened", "PASS", "closing finite transition-layer unification probe without insertion")


def case_1(out: ScriptOutput) -> None:
    header("Case 1: Group 57 compact result ledger")
    ledger = [
        ("finite layer probe", "LAYER_PROBE_OPENED", "finite transition layer replaced hard-boundary-only diagnostics"),
        ("smoothstep", "SMOOTHSTEP_PROFILE_DERIVED", "quintic smoothstep gives endpoint value/slope/curvature control"),
        ("blend residues", "BLEND_RESIDUE_DERIVED", "derivative residues expose transition terms"),
        ("layer energy", "LAYER_ENERGY_CONDITION_DERIVED", "finite layer energy cost is explicit"),
        ("charge warning", "CHARGE_NEUTRALITY_REQUIRED", "spherical weighting can spoil odd-profile neutrality"),
        ("mass warning", "LAYER_MASS_SHIFT_CONDITION_DERIVED", "layer charge can create mass shift"),
        ("divergence", "LAYER_DIVERGENCE_CLOSURE_DERIVED", "layer-local reduced D=0 closure exists"),
        ("route status", "UNIFICATION_PROBE_SURVIVES_CONDITIONALLY", "finite-layer unification probe survives conditionally"),
        ("physical use", "PHYSICAL_USE_BLOCKED", "no insertion, active O, recombination, or parent closure opened"),
    ]
    for label, status, text in ledger:
        emit_line(out, label, status, text)


def case_2(out: ScriptOutput, entries: List[StatusEntry]) -> None:
    header("Case 2: Group 57 status entries")
    for item in entries:
        subheader(item.name)
        emit_line(out, item.name, item.status, f"{item.conclusion}. Boundary: {item.boundary}.")
    emit_line(out, "Group 57 status entries stated", "PASS", f"{len(entries)} status entries stated")


def case_3(out: ScriptOutput, results: List[ResultEntry]) -> None:
    header("Case 3: Finite-layer diagnostic results")
    for item in results:
        subheader(item.name)
        print(f"Result: {item.result}")
        print(f"Meaning: {item.meaning}")
        emit_line(out, item.name, item.status, f"{item.meaning}. Boundary: {item.boundary}.")
    emit_line(out, "Group 57 diagnostic results preserved", "PASS", f"{len(results)} diagnostic results preserved")


def case_4(out: ScriptOutput, burdens: List[BurdenEntry]) -> None:
    header("Case 4: Open burdens after Group 57")
    for item in burdens:
        subheader(item.name)
        emit_line(out, item.name, item.status, f"{item.burden}. Discipline: {item.discipline}.", obligation=True)
    emit_line(out, "Group 57 burdens preserved", "PASS", f"{len(burdens)} burdens remain explicit", obligation=True)


def case_5(out: ScriptOutput, rejected: List[RejectedUpgrade]) -> None:
    header("Case 5: Rejected summary upgrades")
    for item in rejected:
        subheader(item.name)
        print(f"Upgrade: {item.upgrade}")
        emit_line(out, item.name, "REJECTED_ROUTE", item.reason)
    emit_line(out, "Group 57 rejected upgrades preserved", "PASS", f"{len(rejected)} upgrade shortcuts rejected")


def case_6(out: ScriptOutput, handoffs: List[HandoffEntry]) -> None:
    header("Case 6: Safe handoffs")
    for item in handoffs:
        subheader(item.name)
        emit_line(out, item.name, item.status, f"{item.route}. Caution: {item.caution}.")
    emit_line(out, "Group 57 handoffs stated", "DEFERRED_WITH_TARGET", f"{len(handoffs)} handoff routes stated without opening physical use")


def case_7(out: ScriptOutput) -> None:
    header("Case 7: Final interpretation")
    conclusions = [
        ("C1: Group 57 result", "UNIFICATION_PROBE_SURVIVES_CONDITIONALLY", "finite transition-layer route survives conditionally as a diagnostic unification probe"),
        ("C2: residue status", "CANDIDATE_TERM_SURFACE_OPENED", "blend residues are candidate clues, not adopted terms"),
        ("C3: charge warning", "CHARGE_NEUTRALITY_REQUIRED", "weighted layer neutrality remains the sharpest immediate blocker"),
        ("C4: covariant gap", "COVARIANT_LIFT_REQUIRED", "finite radial layer must be lifted before physical use"),
        ("C5: physical-use status", "NOT_INSERTABLE", "B_s/F_zeta insertion, active O, recombination, and parent route remain closed"),
    ]
    for label, status, text in conclusions:
        emit_line(out, label, status, text)

    header("Final summary")
    print("Group 57 status summary result:\n")
    print("  Group 57 turned the boundary-layer idea into a finite transition-layer unification probe.")
    print("  It did not insert B_s/F_zeta or open a parent equation.")
    print()
    print("  Main reduced results:")
    print("    s(x)=10x^3-15x^4+6x^5 gives smooth endpoint value/slope/curvature behavior.")
    print("    Blend residues are R1=(F_out-F_in)s' and R2=(F_out-F_in)s''+2(F_out'-F_in')s'.")
    print("    Reduced layer energy scales as E_layer=5*A^2/(7*ell).")
    print("    Odd flat layer charge cancels, but spherical weighted charge is 4*R*ell^2*rho1/3.")
    print("    Delta_M_layer=4*R*alpha*ell^2*rho1/3.")
    print("    Layer-local stress with p_t=p_r+r*p_r'/2 gives reduced D=0.")
    print()
    print("  The finite-layer unification probe survives conditionally.")
    print("  The sharpest new warning is weighted layer neutrality: flat odd cancellation is not enough.")
    print()
    print("Still required:")
    print("  weighted-neutral finite-layer profile")
    print("  candidate transition-term audit")
    print("  covariant layer lift")
    print("  energy/stress accounting")
    print("  divergence identity support")
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
