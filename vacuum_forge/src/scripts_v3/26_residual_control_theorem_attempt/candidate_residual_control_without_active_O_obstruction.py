# Candidate residual control without active O obstruction
#
# Group:
#   26_residual_control_theorem_attempt
#
# Script type:
#   THEOREM ATTEMPT / CONTROLLED OBSTRUCTION
#
# Purpose
# -------
# Test whether any non-O residual-control route closes under current licensed
# objects.
#
# Locked-door question:
#
#   Can residual control close without active O?
#
# This script does not derive residual kill.
# It does not derive strict non-metric inertness.
# It does not derive zeta/kappa non-reentry.
# It does not derive epsilon/e_kappa accounting inertness.
# It does not derive active no-overlap O.
# It does not derive B_s/F_zeta insertion.
# It does not open parent equation closure.
#
# It asks whether the non-O routes already tested are enough:
#
#   direct residual kill,
#   strict inertness,
#   zeta/kappa geometric non-reentry,
#   epsilon/e_kappa accounting inertness,
#   source/boundary/support guardrails.
#
# Conservative expected result:
#
#   Under current licensed objects, no non-O residual-control route closes.
#   This is a controlled obstruction, not a proof of mathematical impossibility.
#
# Tiny goblin rule:
#
#   No O, no shortcut.

from dataclasses import dataclass
from pathlib import Path
from typing import List

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    BranchDecisionRecord,
    ClaimRecord,
    ClaimTier,
    GovernanceStatus,
    ObligationStatus,
    ProofObligationRecord,
    RecordKind,
    RouteRecord,
    ScriptOutput,
    StatusMark,
)


ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"


# =============================================================================
# Utilities
# =============================================================================


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def status_mark(status: str) -> StatusMark:
    return {
        "BLOCKED": StatusMark.FAIL,
        "CONTROLLED_OBSTRUCTION": StatusMark.DEFER,
        "CONDITIONALLY_REDUCED": StatusMark.INFO,
        "DEFERRED": StatusMark.DEFER,
        "DIAGNOSTIC_ONLY": StatusMark.INFO,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "PARTIAL_REDUCTION": StatusMark.INFO,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "SAFE_IF": StatusMark.INFO,
        "THEOREM_ATTEMPT": StatusMark.DEFER,
        "THEOREM_TARGET": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "problem_ledger_dep_26",
            "26_residual_control_theorem_attempt__candidate_residual_control_theorem_problem_ledger",
            "residual_control_theorem_problem_marker_26",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "structural_kill_dep_26",
            "26_residual_control_theorem_attempt__candidate_structural_residual_kill_law_attempt",
            "structural_residual_kill_law_attempt_marker_26",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "inertness_attempt_dep_26",
            "26_residual_control_theorem_attempt__candidate_nonmetric_inertness_theorem_attempt",
            "nonmetric_inertness_theorem_attempt_marker_26",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "zeta_kappa_dep_26",
            "26_residual_control_theorem_attempt__candidate_zeta_kappa_nonreentry_theorem_attempt",
            "zeta_kappa_nonreentry_theorem_attempt_marker_26",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "epsilon_ekappa_dep_26",
            "26_residual_control_theorem_attempt__candidate_epsilon_ekappa_inertness_theorem_attempt",
            "epsilon_ekappa_inertness_theorem_attempt_marker_26",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g25_O_burden_dep_26",
            "25_residual_kill_or_no_overlap_theorem__candidate_no_overlap_operator_minimum_burden",
            "no_overlap_operator_minimum_burden_marker_25",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g25_summary_dep_26",
            "25_residual_kill_or_no_overlap_theorem__candidate_group_25_residual_kill_status_summary",
            "group25_residual_kill_status_summary_marker_25",
            RecordKind.INVENTORY_MARKER,
        ),
    ]

    for dependency_id, upstream_script_id, upstream_derivation_id, expected_record_kind in dependencies:
        ns.declare_dependency(
            dependency_id=dependency_id,
            upstream_script_id=upstream_script_id,
            upstream_derivation_id=upstream_derivation_id,
            expected_record_kind=expected_record_kind,
        )

    return archive, ns, invalidated


def ensure_archive_write_dirs(ns) -> None:
    for attr in (
        "routes_path",
        "branch_decisions_path",
        "claims_path",
        "obligations_path",
        "derivations_path",
        "governance_path",
    ):
        path_obj = getattr(ns, attr, None)
        if path_obj is not None:
            path_obj.mkdir(parents=True, exist_ok=True)


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


# =============================================================================
# Data models
# =============================================================================


@dataclass
class NonOClosureLedger:
    direct_kill_gap: sp.Symbol
    full_inertness_gap: sp.Symbol
    zeta_kappa_nonreentry_gap: sp.Symbol
    accounting_inertness_gap: sp.Symbol
    boundary_source_guardrail_gap: sp.Symbol
    insertion_law_gap: sp.Symbol
    coefficient_origin_gap: sp.Symbol
    nonO_obstruction_load: sp.Expr


@dataclass
class NonORouteStatus:
    name: str
    route: str
    status: str
    evidence: str
    blocker: str


@dataclass
class ObstructionTest:
    name: str
    test: str
    status: str
    result: str
    implication: str


@dataclass
class RejectedNonOShortcut:
    name: str
    shortcut: str
    forbidden_use: str
    status: str
    consequence: str


@dataclass
class NonOConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


# =============================================================================
# Builders
# =============================================================================


def build_ledger() -> NonOClosureLedger:
    (
        direct_kill_gap,
        full_inertness_gap,
        zeta_kappa_nonreentry_gap,
        accounting_inertness_gap,
        boundary_source_guardrail_gap,
        insertion_law_gap,
        coefficient_origin_gap,
    ) = sp.symbols(
        "direct_kill_gap full_inertness_gap zeta_kappa_nonreentry_gap accounting_inertness_gap boundary_source_guardrail_gap insertion_law_gap coefficient_origin_gap",
        real=True,
    )

    nonO_obstruction_load = sp.simplify(
        direct_kill_gap
        + full_inertness_gap
        + zeta_kappa_nonreentry_gap
        + accounting_inertness_gap
        + boundary_source_guardrail_gap
        + insertion_law_gap
        + coefficient_origin_gap
    )

    return NonOClosureLedger(
        direct_kill_gap=direct_kill_gap,
        full_inertness_gap=full_inertness_gap,
        zeta_kappa_nonreentry_gap=zeta_kappa_nonreentry_gap,
        accounting_inertness_gap=accounting_inertness_gap,
        boundary_source_guardrail_gap=boundary_source_guardrail_gap,
        insertion_law_gap=insertion_law_gap,
        coefficient_origin_gap=coefficient_origin_gap,
        nonO_obstruction_load=nonO_obstruction_load,
    )


def build_route_statuses() -> List[NonORouteStatus]:
    return [
        NonORouteStatus(
            name="R1: direct residual kill",
            route="derive L_double = 0 structurally",
            status="NOT_DERIVED",
            evidence="direct structural residual kill attempt did not derive L_double = 0",
            blocker="no structural law kills zeta_residual_metric, kappa_metric, epsilon_vac_metric, and e_kappa_metric",
        ),
        NonORouteStatus(
            name="R2: strict non-metric inertness",
            route="derive every L_double entry strictly inert / non-metric / non-reentering",
            status="NOT_DERIVED",
            evidence="full strict inertness was not derived for all L_double entries",
            blocker="zeta_residual_metric and kappa_metric remain unresolved; accounting pair is only partially reduced",
        ),
        NonORouteStatus(
            name="R3: zeta/kappa geometric non-reentry",
            route="derive zeta and kappa residuals cannot re-enter sector-by-sector",
            status="NOT_DERIVED",
            evidence="zeta/kappa non-reentry attempt left both geometric residuals open",
            blocker="missing insertion law, coefficient origin, sector-by-sector non-reentry, or active O",
        ),
        NonORouteStatus(
            name="R4: epsilon/e_kappa accounting inertness",
            route="derive accounting-only inertness for epsilon_vac_metric and e_kappa_metric",
            status="PARTIAL_REDUCTION",
            evidence="accounting pair was partially reduced but not fully derived",
            blocker="even full accounting inertness would not close zeta/kappa geometric non-reentry",
        ),
        NonORouteStatus(
            name="R5: source/boundary/support guardrails",
            route="use source, boundary, scalar, current, mass, shell, and support guardrails to close residual control",
            status="NOT_DERIVED",
            evidence="guardrails reject repair routes but do not derive residual-control theorem",
            blocker="guardrails are constraints, not kill/inertness/non-reentry laws",
        ),
        NonORouteStatus(
            name="R6: B_s/F_zeta insertion-independent closure",
            route="close residual control without needing insertion law or coefficient origin",
            status="NOT_DERIVED",
            evidence="zeta residual non-reentry remains blocked by missing insertion law/coefficient origin or active O",
            blocker="safe zeta_to_Bs trace target is known, but insertion law is not derived",
        ),
    ]


def build_obstruction_tests() -> List[ObstructionTest]:
    return [
        ObstructionTest(
            name="T1: all non-O theorem routes close",
            test="do direct kill, strict inertness, zeta/kappa non-reentry, and accounting inertness all close?",
            status="BLOCKED",
            result="no; none is fully derived and the accounting pair only partially reduces",
            implication="non-O residual control is not closed",
        ),
        ObstructionTest(
            name="T2: accounting route closes residual control",
            test="does epsilon/e_kappa accounting inertness close L_double?",
            status="BLOCKED",
            result="no; even full accounting inertness would not close zeta/kappa geometric non-reentry",
            implication="accounting route cannot be the whole residual-control theorem",
        ),
        ObstructionTest(
            name="T3: guardrails close residual control",
            test="do source/boundary/support guardrails become residual-control theorem?",
            status="BLOCKED",
            result="no; they reject repair paths but do not prove residual kill or non-reentry",
            implication="guardrails are necessary but insufficient",
        ),
        ObstructionTest(
            name="T4: insertion-independent zeta closure",
            test="can zeta residual non-reentry close without B_s/F_zeta insertion law or coefficient origin?",
            status="NOT_DERIVED",
            result="not under current licensed objects",
            implication="zeta route likely depends on insertion details or active O",
        ),
        ObstructionTest(
            name="T5: active-O-free geometric separator",
            test="can zeta/kappa be separated without an O-like operator?",
            status="NOT_DERIVED",
            result="not under current licensed objects",
            implication="active O may be required, optional, or deferred; classification remains next",
        ),
        ObstructionTest(
            name="T6: no-go theorem",
            test="does this prove active O is mathematically necessary?",
            status="NOT_DERIVED",
            result="no; this is only a controlled obstruction under current licensed objects",
            implication="next script must classify O required / optional / deferred without overclaiming",
        ),
    ]


def build_rejected_shortcuts() -> List[RejectedNonOShortcut]:
    return [
        RejectedNonOShortcut(
            name="S1: non-O closure by summary",
            shortcut="declare non-O residual control closed because all audits are listed",
            forbidden_use="summary replaces theorem",
            status="REJECTED",
            consequence="requirements are mistaken for proof",
        ),
        RejectedNonOShortcut(
            name="S2: accounting closes geometry",
            shortcut="use epsilon/e_kappa accounting reduction to close zeta/kappa geometric residuals",
            forbidden_use="accounting pair repairs geometric residuals",
            status="REJECTED",
            consequence="geometric non-reentry remains hidden",
        ),
        RejectedNonOShortcut(
            name="S3: guardrail as theorem",
            shortcut="source/boundary/support guardrails become residual-control theorem",
            forbidden_use="constraints are upgraded into kill/inertness/non-reentry laws",
            status="REJECTED",
            consequence="repair-route closure is smuggled",
        ),
        RejectedNonOShortcut(
            name="S4: insertion law assumed",
            shortcut="assume B_s/F_zeta insertion law to close zeta residual",
            forbidden_use="missing insertion theorem is treated as available",
            status="REJECTED",
            consequence="metric recombination is smuggled",
        ),
        RejectedNonOShortcut(
            name="S5: coefficient origin assumed",
            shortcut="assume coefficient origin resolves residual split",
            forbidden_use="missing coefficient theorem is treated as available",
            status="REJECTED",
            consequence="zeta residual control is selected by coefficient choice",
        ),
        RejectedNonOShortcut(
            name="S6: hidden O in non-O route",
            shortcut="use projection-like separator while claiming no active O",
            forbidden_use="O burden is renamed and bypassed",
            status="REJECTED",
            consequence="active O is smuggled",
        ),
        RejectedNonOShortcut(
            name="S7: no-go overclaim",
            shortcut="claim active O is mathematically necessary from incomplete non-O tests",
            forbidden_use="controlled obstruction upgraded to impossibility theorem",
            status="REJECTED",
            consequence="the theorem attempt overclaims",
        ),
        RejectedNonOShortcut(
            name="S8: non-O closure opens insertion or parent",
            shortcut="controlled obstruction opens B_s/F_zeta insertion or parent equation",
            forbidden_use="obstruction result replaces insertion/parent theorems",
            status="REJECTED",
            consequence="downstream gates are smuggled",
        ),
    ]


def build_conclusions() -> List[NonOConclusion]:
    return [
        NonOConclusion(
            name="C1: non-O residual control",
            conclusion="not closed under current licensed objects",
            status="CONTROLLED_OBSTRUCTION",
            meaning="direct kill, full inertness, zeta/kappa non-reentry, and accounting inertness do not currently close residual control",
        ),
        NonOConclusion(
            name="C2: accounting route",
            conclusion="partially reduced but insufficient",
            status="PARTIAL_REDUCTION",
            meaning="epsilon/e_kappa accounting work may be useful, but cannot close zeta/kappa geometric residuals by itself",
        ),
        NonOConclusion(
            name="C3: zeta/kappa obstruction",
            conclusion="dominant non-O blocker",
            status="THEOREM_TARGET",
            meaning="the unresolved geometric residuals are the sharp obstruction",
        ),
        NonOConclusion(
            name="C4: active O status",
            conclusion="not proven necessary, but now a live classification target",
            status="DEFERRED",
            meaning="next script should classify active O as required, optional, deferred, or rejected as shortcut",
        ),
        NonOConclusion(
            name="C5: insertion and parent gates",
            conclusion="remain closed",
            status="NOT_READY",
            meaning="controlled obstruction does not license B_s/F_zeta insertion or parent equation",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Residual control without active O obstruction problem")
    print("Question:")
    print()
    print("  Can residual control close without active O?")
    print()
    print("Reference discipline:")
    print()
    print("  This is a controlled obstruction test, not an impossibility theorem.")
    print("  Non-O closure must come from a real theorem route, not a summary of guardrails.")
    print("  Active O may become required, optional, or deferred, but is not derived here.")

    with out.governance_assessments():
        out.line(
            "non-O residual-control obstruction test opened",
            StatusMark.INFO,
            "testing whether current non-O routes close residual control without active O",
        )


def case_1_obstruction_ledger(ledger: NonOClosureLedger, out: ScriptOutput) -> None:
    header("Case 1: Non-O residual-control obstruction ledger")
    print("Obstruction gaps:")
    print()
    for name in [
        "direct_kill_gap",
        "full_inertness_gap",
        "zeta_kappa_nonreentry_gap",
        "accounting_inertness_gap",
        "boundary_source_guardrail_gap",
        "insertion_law_gap",
        "coefficient_origin_gap",
    ]:
        print(f"  {name} = {sp.sstr(getattr(ledger, name))}")
    print()
    print("Non-O obstruction load:")
    print()
    print(f"  L_nonO_obstruction = {sp.sstr(ledger.nonO_obstruction_load)}")
    print()
    print("Interpretation:")
    print()
    print("  Non-O residual control closes only if every relevant gap is closed by theorem.")
    print("  Under current licensed objects, these gaps remain open or only partially reduced.")

    with out.derived_results():
        out.line(
            "non-O residual-control obstruction load stated",
            StatusMark.OBLIGATION,
            f"L_nonO_obstruction = {sp.sstr(ledger.nonO_obstruction_load)}",
        )


def case_2_route_statuses(routes: List[NonORouteStatus], out: ScriptOutput) -> None:
    header("Case 2: Non-O route status ledger")
    for route in routes:
        print()
        print("-" * 120)
        print(route.name)
        print("-" * 120)
        print(f"Route: {route.route}")
        print(f"[{status_mark(route.status).value}] {route.name}: {route.status}")
        print(f"Evidence: {route.evidence}")
        print(f"Blocker: {route.blocker}")

    with out.unresolved_obligations():
        out.line(
            "non-O residual-control route statuses classified",
            StatusMark.OBLIGATION,
            f"{len(routes)} non-O routes tested; no closure route derived",
        )


def case_3_obstruction_tests(tests: List[ObstructionTest], out: ScriptOutput) -> None:
    header("Case 3: Controlled obstruction tests")
    for test in tests:
        print()
        print("-" * 120)
        print(test.name)
        print("-" * 120)
        print(f"Test: {test.test}")
        print(f"[{status_mark(test.status).value}] {test.name}: {test.status}")
        print(f"Result: {test.result}")
        print(f"Implication: {test.implication}")

    with out.governance_assessments():
        out.line(
            "controlled obstruction tests completed",
            StatusMark.PASS,
            f"{len(tests)} obstruction tests evaluated; non-O closure not derived",
        )


def case_4_rejected_shortcuts(shortcuts: List[RejectedNonOShortcut], out: ScriptOutput) -> None:
    header("Case 4: Rejected non-O closure shortcuts")
    for shortcut in shortcuts:
        print()
        print("-" * 120)
        print(shortcut.name)
        print("-" * 120)
        print(f"Shortcut: {shortcut.shortcut}")
        print(f"Forbidden use: {shortcut.forbidden_use}")
        print(f"[{status_mark(shortcut.status).value}] {shortcut.name}: {shortcut.status}")
        print(f"Consequence: {shortcut.consequence}")

    with out.counterexamples():
        out.line(
            "non-O closure shortcuts rejected",
            StatusMark.FAIL,
            "summary closure, accounting-to-geometry, guardrail theorem, assumed insertion/coefficient, hidden O, no-go overclaim, and downstream gate shortcuts are rejected",
        )


def case_5_conclusions(conclusions: List[NonOConclusion], out: ScriptOutput) -> None:
    header("Case 5: Non-O residual-control conclusions")
    for conclusion in conclusions:
        print()
        print("-" * 120)
        print(conclusion.name)
        print("-" * 120)
        print(f"Conclusion: {conclusion.conclusion}")
        print(f"[{status_mark(conclusion.status).value}] {conclusion.name}: {conclusion.status}")
        print(f"Meaning: {conclusion.meaning}")

    with out.governance_assessments():
        out.line(
            "non-O residual-control conclusion stated",
            StatusMark.DEFER,
            "non-O closure not derived; active O necessity/deferral classification remains next",
        )


def case_6_failure_controls(out: ScriptOutput) -> None:
    header("Case 6: Failure controls")
    print("The residual-control without active O obstruction test fails if a later script allows:")
    print()
    print("1. non-O closure by summary of audits")
    print("2. accounting reduction closes zeta/kappa geometry")
    print("3. guardrails treated as residual-control theorem")
    print("4. B_s/F_zeta insertion law assumed")
    print("5. coefficient origin assumed")
    print("6. hidden O used inside a non-O route")
    print("7. controlled obstruction upgraded to mathematical impossibility")
    print("8. active O declared necessary without classification")
    print("9. non-O obstruction licenses insertion")
    print("10. non-O obstruction opens parent equation")

    with out.governance_assessments():
        out.line(
            "non-O residual-control failure controls stated",
            StatusMark.OBLIGATION,
            "future scripts must not overclaim obstruction or smuggle active O, insertion, or parent closure",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Residual control without active O obstruction result:")
    print()
    print("  Under current licensed objects, no non-O residual-control route closes.")
    print("  Direct residual kill is not derived.")
    print("  Full strict inertness is not derived.")
    print("  Zeta/kappa geometric non-reentry is not derived.")
    print("  epsilon/e_kappa accounting inertness is only partially reduced and does not close zeta/kappa geometry.")
    print("  Source/boundary/support guardrails are necessary but insufficient.")
    print("  This is a controlled obstruction, not a mathematical no-go theorem.")
    print("  Active O is now a live classification target: required, optional, deferred, or rejected as shortcut.")
    print("  B_s/F_zeta insertion and parent closure remain not ready.")
    print()
    print("Possible next script:")
    print("  candidate_minimal_O_necessity_or_deferral.py")
    print()
    print("Tiny goblin label:")
    print("  No O, no shortcut.")

    with out.governance_assessments():
        out.line(
            "residual control without active O obstruction test complete",
            StatusMark.PASS,
            "non-O closure not derived; active-O necessity/deferral route remains next",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, ledger: NonOClosureLedger) -> None:
    ns.record_derivation(
        derivation_id="nonO_residual_control_obstruction_load_26",
        inputs=[
            ledger.direct_kill_gap,
            ledger.full_inertness_gap,
            ledger.zeta_kappa_nonreentry_gap,
            ledger.accounting_inertness_gap,
            ledger.boundary_source_guardrail_gap,
            ledger.insertion_law_gap,
            ledger.coefficient_origin_gap,
        ],
        output=ledger.nonO_obstruction_load,
        method="sum open/partial non-O residual-control route gaps under current licensed objects",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="nonO_residual_control_obstruction_ledger",
        scope="Group 26 residual control theorem attempt",
    )

    ns.record_derivation(
        derivation_id="residual_control_without_active_O_obstruction_marker_26",
        inputs=[
            sp.Symbol("direct_kill_not_derived"),
            sp.Symbol("full_inertness_not_derived"),
            sp.Symbol("zeta_kappa_nonreentry_not_derived"),
            sp.Symbol("accounting_partial_only"),
            sp.Symbol("guardrails_insufficient"),
        ],
        output=sp.Symbol("nonO_residual_control_not_closed_under_current_objects"),
        method="Group 26 controlled obstruction test for non-O residual control",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="controlled_obstruction_marker",
        scope="Group 26 residual control theorem attempt",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g26_close_or_block_direct_kill", "Close or block direct residual kill"),
        ("g26_close_or_block_full_inertness", "Close or block full strict inertness"),
        ("g26_close_or_block_zeta_kappa_nonreentry", "Close or block zeta/kappa geometric non-reentry"),
        ("g26_close_or_block_accounting_inertness", "Close or block epsilon/e_kappa accounting inertness"),
        ("g26_classify_guardrails_as_insufficient_or_theorem", "Classify whether guardrails are insufficient or theorem-producing"),
        ("g26_classify_insertion_law_dependency", "Classify B_s/F_zeta insertion-law dependency"),
        ("g26_classify_coefficient_origin_dependency", "Classify coefficient-origin dependency"),
        ("g26_classify_active_O_required_optional_deferred", "Classify active O as required, optional, deferred, or rejected as shortcut"),
        ("g26_keep_insertion_parent_closed_after_nonO_obstruction", "Keep insertion and parent gates closed after non-O obstruction"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g26_nonO_residual_control_obstruction_route"],
            description=(
                "Non-O residual control is not closed here. This is a controlled obstruction under current licensed objects, not a mathematical no-go theorem."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g26_close_or_block_direct_kill",
        "g26_close_or_block_full_inertness",
        "g26_close_or_block_zeta_kappa_nonreentry",
        "g26_close_or_block_accounting_inertness",
        "g26_classify_guardrails_as_insufficient_or_theorem",
        "g26_classify_insertion_law_dependency",
        "g26_classify_coefficient_origin_dependency",
        "g26_classify_active_O_required_optional_deferred",
        "g26_keep_insertion_parent_closed_after_nonO_obstruction",
    ]

    ns.record_route(RouteRecord(
        route_id="g26_nonO_residual_control_obstruction_route",
        script_id=SCRIPT_ID,
        name="Group 26 residual control without active O obstruction test",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "non-O routes are tested without active O",
            "direct kill, inertness, zeta/kappa non-reentry, accounting inertness, and guardrails are separately classified",
            "controlled obstruction is not upgraded to impossibility theorem",
            "active O is classified only in the next step",
            "insertion and parent gates remain closed",
        ],
    ))

    for branch_id in [
        "nonO_closure_by_summary",
        "accounting_closes_geometric_residuals",
        "guardrail_as_residual_control_theorem",
        "insertion_law_assumed",
        "coefficient_origin_assumed",
        "hidden_O_inside_nonO_route",
        "no_go_overclaim",
        "active_O_declared_necessary_without_classification",
        "nonO_obstruction_licenses_insertion",
        "nonO_obstruction_opens_parent",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}_26",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; non-O obstruction must not smuggle closure, O, insertion, or parent readiness.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g26_nonO_residual_control_not_closed_under_current_objects",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Under current licensed objects, no non-O residual-control route closes. Direct kill, full strict inertness, and zeta/kappa geometric non-reentry are not derived; "
            "epsilon/e_kappa accounting inertness is only partially reduced and does not close zeta/kappa geometry; guardrails are necessary but insufficient. "
            "This is a controlled obstruction, not a mathematical no-go theorem. Active O must be classified next, and insertion/parent gates remain closed."
        ),
        derivation_ids=[
            "nonO_residual_control_obstruction_load_26",
            "residual_control_without_active_O_obstruction_marker_26",
        ],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Residual Control Without Active O Obstruction")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    ledger = build_ledger()
    routes = build_route_statuses()
    tests = build_obstruction_tests()
    shortcuts = build_rejected_shortcuts()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_obstruction_ledger(ledger, out)
    case_2_route_statuses(routes, out)
    case_3_obstruction_tests(tests, out)
    case_4_rejected_shortcuts(shortcuts, out)
    case_5_conclusions(conclusions, out)
    case_6_failure_controls(out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns, ledger)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
