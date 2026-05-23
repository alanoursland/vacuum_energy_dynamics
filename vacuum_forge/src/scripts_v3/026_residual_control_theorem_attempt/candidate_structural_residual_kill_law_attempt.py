# Candidate structural residual kill law attempt
#
# Group:
#   26_residual_control_theorem_attempt
#
# Script type:
#   THEOREM ATTEMPT
#
# Purpose
# -------
# Attempt the direct structural residual-kill route.
#
# Locked-door question:
#
#   Can L_double = 0 be derived structurally without naming it zero?
#
# This script does not derive B_s/F_zeta insertion.
# It does not derive active no-overlap O.
# It does not derive parent equation closure.
#
# It tests whether the currently licensed structural constraints are sufficient
# to force the residual double-count load to zero:
#
#   L_double = e_kappa_metric
#            + epsilon_vac_metric
#            + kappa_metric
#            + zeta_residual_metric
#
# The expected conservative result is likely:
#
#   no direct structural residual-kill law is derived under current licensed
#   objects; residual-kill remains provisional / theorem-targeted.
#
# Tiny goblin rule:
#
#   Zero by law, or not zero.

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
        "CONDITIONALLY_REDUCED": StatusMark.INFO,
        "DIAGNOSTIC_ONLY": StatusMark.INFO,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
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
            "g25_problem_dep_26",
            "25_residual_kill_or_no_overlap_theorem__candidate_residual_kill_problem_ledger",
            "residual_kill_problem_ledger_marker_25",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g25_obligation_dep_26",
            "25_residual_kill_or_no_overlap_theorem__candidate_residual_kill_theorem_obligations",
            "residual_kill_theorem_obligations_marker_25",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g24_count_once_dep_26",
            "24_metric_insertion_recovery_retest__candidate_count_once_metric_trace_audit",
            "count_once_metric_trace_marker_24",
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
class KillAttemptLedger:
    zeta_residual_metric: sp.Symbol
    kappa_metric: sp.Symbol
    epsilon_vac_metric: sp.Symbol
    e_kappa_metric: sp.Symbol
    L_double: sp.Expr
    zeta_kill_gap: sp.Symbol
    kappa_kill_gap: sp.Symbol
    epsilon_kill_gap: sp.Symbol
    e_kappa_kill_gap: sp.Symbol
    direct_kill_gap: sp.Expr


@dataclass
class ResidualKillEntry:
    name: str
    residual: str
    candidate_structural_support: str
    kill_status: str
    reason_not_derived: str
    next_reduction: str


@dataclass
class StructuralKillTest:
    name: str
    test: str
    status: str
    passes_if: str
    current_result: str


@dataclass
class RejectedKillShortcut:
    name: str
    shortcut: str
    forbidden_use: str
    status: str
    consequence: str


@dataclass
class KillAttemptConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


# =============================================================================
# Builders
# =============================================================================


def build_ledger() -> KillAttemptLedger:
    (
        zeta_residual_metric,
        kappa_metric,
        epsilon_vac_metric,
        e_kappa_metric,
        zeta_kill_gap,
        kappa_kill_gap,
        epsilon_kill_gap,
        e_kappa_kill_gap,
    ) = sp.symbols(
        "zeta_residual_metric kappa_metric epsilon_vac_metric e_kappa_metric zeta_kill_gap kappa_kill_gap epsilon_kill_gap e_kappa_kill_gap",
        real=True,
    )

    L_double = sp.simplify(
        zeta_residual_metric
        + kappa_metric
        + epsilon_vac_metric
        + e_kappa_metric
    )

    # Direct structural kill would require each gap to vanish by law.
    direct_kill_gap = sp.simplify(
        zeta_kill_gap
        + kappa_kill_gap
        + epsilon_kill_gap
        + e_kappa_kill_gap
    )

    return KillAttemptLedger(
        zeta_residual_metric=zeta_residual_metric,
        kappa_metric=kappa_metric,
        epsilon_vac_metric=epsilon_vac_metric,
        e_kappa_metric=e_kappa_metric,
        L_double=L_double,
        zeta_kill_gap=zeta_kill_gap,
        kappa_kill_gap=kappa_kill_gap,
        epsilon_kill_gap=epsilon_kill_gap,
        e_kappa_kill_gap=e_kappa_kill_gap,
        direct_kill_gap=direct_kill_gap,
    )


def build_kill_entries() -> List[ResidualKillEntry]:
    return [
        ResidualKillEntry(
            name="K1: zeta residual metric trace",
            residual="zeta_residual_metric",
            candidate_structural_support="count-once scalar trace requirement plus B_s/F_zeta insertion target",
            kill_status="NOT_DERIVED",
            reason_not_derived="count-once requirement says zeta residual must not re-enter, but does not by itself derive zeta_residual_metric = 0",
            next_reduction="requires B_s/F_zeta insertion law, coefficient origin, strict non-reentry, or active O",
        ),
        ResidualKillEntry(
            name="K2: kappa metric trace",
            residual="kappa_metric",
            candidate_structural_support="diagnostic-only / areal-kappa guardrail",
            kill_status="NOT_DERIVED",
            reason_not_derived="diagnostic-only status blocks kappa as construction but does not structurally prove kappa_metric = 0",
            next_reduction="requires kappa nonmetric theorem, no-reentry theorem, or active O",
        ),
        ResidualKillEntry(
            name="K3: epsilon_vac metric channel",
            residual="epsilon_vac_metric",
            candidate_structural_support="energy/accounting guardrail",
            kill_status="NOT_DERIVED",
            reason_not_derived="accounting-only discipline forbids source/metric promotion but does not yet prove epsilon_vac_metric = 0 by structural law",
            next_reduction="may reduce to accounting inertness theorem; not direct residual kill",
        ),
        ResidualKillEntry(
            name="K4: e_kappa metric channel",
            residual="e_kappa_metric",
            candidate_structural_support="kappa accounting / no source-channel guardrail",
            kill_status="NOT_DERIVED",
            reason_not_derived="guardrail forbids e_kappa as extra metric/source channel but does not yet derive e_kappa_metric = 0",
            next_reduction="may reduce to kappa accounting inertness theorem; not direct residual kill",
        ),
    ]


def build_tests() -> List[StructuralKillTest]:
    return [
        StructuralKillTest(
            name="T1: zero by structural identity",
            test="does a current structural identity force every L_double entry to zero?",
            status="NOT_DERIVED",
            passes_if="zeta_residual_metric = kappa_metric = epsilon_vac_metric = e_kappa_metric = 0 follows before recovery and without naming",
            current_result="no such identity is currently derived",
        ),
        StructuralKillTest(
            name="T2: zero by count-once alone",
            test="does count-once requirement itself imply L_double = 0?",
            status="NOT_DERIVED",
            passes_if="count-once is a derived recombination theorem rather than a constraint",
            current_result="count-once is a requirement; it does not supply the kill law",
        ),
        StructuralKillTest(
            name="T3: zero by diagnostic-only status",
            test="does diagnostic-only status force kappa/e_kappa residuals to zero?",
            status="NOT_DERIVED",
            passes_if="diagnostic-only is derived as strict nonmetric inertness with no reentry",
            current_result="diagnostic-only status constrains use; it is not a zero theorem",
        ),
        StructuralKillTest(
            name="T4: zero by accounting-only status",
            test="does accounting-only status force epsilon/e_kappa metric channels to zero?",
            status="CONDITIONALLY_REDUCED",
            passes_if="accounting-only is formalized as no metric/source/support/boundary/recovery role",
            current_result="may reduce to inertness theorem, but direct structural kill is not derived",
        ),
        StructuralKillTest(
            name="T5: zero by source no-double-counting",
            test="does source no-double-counting kill residual metric trace?",
            status="NOT_DERIVED",
            passes_if="source routing also proves no metric trace for each residual",
            current_result="source guardrails block source duplication; they do not prove metric residuals zero",
        ),
        StructuralKillTest(
            name="T6: zero by boundary/scalar silence",
            test="does boundary/scalar silence kill residual metric trace?",
            status="NOT_DERIVED",
            passes_if="boundary silence derives interior residual zero, not only exterior/tail constraints",
            current_result="boundary/scalar guardrails block tails/fluxes; they do not prove L_double = 0",
        ),
    ]


def build_rejected_shortcuts() -> List[RejectedKillShortcut]:
    return [
        RejectedKillShortcut(
            name="S1: zeta residual zero by naming",
            shortcut="set zeta_residual_metric = 0",
            forbidden_use="declaring the leftover trace absent",
            status="REJECTED",
            consequence="zeta count-once theorem is smuggled",
        ),
        RejectedKillShortcut(
            name="S2: kappa zero by diagnostic label",
            shortcut="set kappa_metric = 0 because kappa is diagnostic",
            forbidden_use="diagnostic-only label used as zero theorem",
            status="REJECTED",
            consequence="kappa trace may re-enter later",
        ),
        RejectedKillShortcut(
            name="S3: epsilon/e_kappa zero by accounting label",
            shortcut="set epsilon_vac_metric = e_kappa_metric = 0 because they are accounting",
            forbidden_use="accounting label used as inertness theorem",
            status="REJECTED",
            consequence="hidden metric/source channels remain possible",
        ),
        RejectedKillShortcut(
            name="S4: kill by recovery",
            shortcut="choose L_double = 0 because recovery requires it",
            forbidden_use="Schwarzschild/gamma/AB/B=1/A/PPN/areal-kappa target selects kill law",
            status="REJECTED",
            consequence="recovery constructs residual control",
        ),
        RejectedKillShortcut(
            name="S5: kill by boundary/source repair",
            shortcut="choose L_double = 0 to remove tail, flux, shell, source duplication, or support load",
            forbidden_use="boundary/source failure selects kill law",
            status="REJECTED",
            consequence="residual kill becomes repair route",
        ),
        RejectedKillShortcut(
            name="S6: kill by hidden O",
            shortcut="use K_res as an unnamed O eraser",
            forbidden_use="operator-like erasure without O burden",
            status="REJECTED",
            consequence="active O is smuggled",
        ),
        RejectedKillShortcut(
            name="S7: kill licenses insertion",
            shortcut="direct kill attempt licenses B_s/F_zeta insertion",
            forbidden_use="residual kill replaces insertion law and coefficient origin",
            status="REJECTED",
            consequence="metric insertion is smuggled",
        ),
        RejectedKillShortcut(
            name="S8: kill opens parent",
            shortcut="direct kill attempt opens parent equation",
            forbidden_use="residual kill replaces parent identity and divergence closure",
            status="REJECTED",
            consequence="parent equation is smuggled",
        ),
    ]


def build_conclusions() -> List[KillAttemptConclusion]:
    return [
        KillAttemptConclusion(
            name="C1: direct structural residual kill",
            conclusion="not derived under current licensed objects",
            status="NOT_DERIVED",
            meaning="L_double remains open; direct residual kill cannot be claimed from the current ledger",
        ),
        KillAttemptConclusion(
            name="C2: accounting residuals",
            conclusion="epsilon_vac_metric and e_kappa_metric may reduce to an inertness theorem target",
            status="CONDITIONALLY_REDUCED",
            meaning="accounting guardrails suggest a narrower theorem target but do not prove zero",
        ),
        KillAttemptConclusion(
            name="C3: zeta/kappa geometric residuals",
            conclusion="zeta_residual_metric and kappa_metric remain blocked by missing insertion/inertness/no-reentry/O structure",
            status="THEOREM_TARGET",
            meaning="the dangerous geometric trace entries remain unresolved",
        ),
        KillAttemptConclusion(
            name="C4: next route",
            conclusion="the next route should test strict nonmetric inertness rather than claiming direct kill",
            status="SAFE_IF",
            meaning="structural kill attempt points to inertness/no-reentry theorem attempt",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Structural residual-kill law attempt problem")
    print("Question:")
    print()
    print("  Can L_double = 0 be derived structurally without naming it zero?")
    print()
    print("Reference discipline:")
    print()
    print("  A direct kill theorem must force every double-count entry to zero by law.")
    print("  Count-once requirements, diagnostic labels, accounting labels, recovery targets, boundary/source needs, and parent closure do not count as kill laws.")

    with out.governance_assessments():
        out.line(
            "structural residual-kill law attempt opened",
            StatusMark.INFO,
            "testing direct L_double = 0 route without declaration, recovery, repair, or parent shortcuts",
        )


def case_1_kill_ledger(ledger: KillAttemptLedger, out: ScriptOutput) -> None:
    header("Case 1: Direct residual-kill ledger")
    print("Double-count load:")
    print()
    print(f"  L_double = {sp.sstr(ledger.L_double)}")
    print()
    print("Kill gaps:")
    print()
    print(f"  zeta_kill_gap = {sp.sstr(ledger.zeta_kill_gap)}")
    print(f"  kappa_kill_gap = {sp.sstr(ledger.kappa_kill_gap)}")
    print(f"  epsilon_kill_gap = {sp.sstr(ledger.epsilon_kill_gap)}")
    print(f"  e_kappa_kill_gap = {sp.sstr(ledger.e_kappa_kill_gap)}")
    print()
    print("Direct structural kill gap:")
    print()
    print(f"  gap_direct_kill = {sp.sstr(ledger.direct_kill_gap)}")
    print()
    print("Interpretation:")
    print()
    print("  Direct residual kill requires every kill gap to vanish by structural law.")
    print("  No kill gap is closed merely by appearing in this ledger.")

    with out.derived_results():
        out.line(
            "direct residual double-count load restated",
            StatusMark.OBLIGATION,
            f"L_double = {sp.sstr(ledger.L_double)}",
        )
        out.line(
            "direct structural kill gap stated",
            StatusMark.OBLIGATION,
            f"gap_direct_kill = {sp.sstr(ledger.direct_kill_gap)}",
        )


def case_2_residual_entries(entries: List[ResidualKillEntry], out: ScriptOutput) -> None:
    header("Case 2: Residual-entry direct-kill attempt")
    for entry in entries:
        print()
        print("-" * 120)
        print(entry.name)
        print("-" * 120)
        print(f"Residual: {entry.residual}")
        print(f"Candidate structural support: {entry.candidate_structural_support}")
        print(f"[{status_mark(entry.kill_status).value}] {entry.name}: {entry.kill_status}")
        print(f"Reason not derived: {entry.reason_not_derived}")
        print(f"Next reduction: {entry.next_reduction}")

    with out.unresolved_obligations():
        out.line(
            "direct residual-kill entry attempts classified",
            StatusMark.OBLIGATION,
            f"{len(entries)} residual entries tested; no direct kill derived",
        )


def case_3_structural_tests(tests: List[StructuralKillTest], out: ScriptOutput) -> None:
    header("Case 3: Structural kill tests")
    for test in tests:
        print()
        print("-" * 120)
        print(test.name)
        print("-" * 120)
        print(f"Test: {test.test}")
        print(f"[{status_mark(test.status).value}] {test.name}: {test.status}")
        print(f"Passes if: {test.passes_if}")
        print(f"Current result: {test.current_result}")

    with out.governance_assessments():
        out.line(
            "structural residual-kill tests completed",
            StatusMark.PASS,
            f"{len(tests)} tests evaluated; direct kill not derived",
        )


def case_4_rejected_shortcuts(shortcuts: List[RejectedKillShortcut], out: ScriptOutput) -> None:
    header("Case 4: Rejected direct-kill shortcuts")
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
            "direct residual-kill shortcuts rejected",
            StatusMark.FAIL,
            "zero by naming, diagnostic/accounting labels, recovery, repair, hidden O, insertion, and parent shortcuts are rejected",
        )


def case_5_conclusions(conclusions: List[KillAttemptConclusion], out: ScriptOutput) -> None:
    header("Case 5: Direct structural residual-kill conclusions")
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
            "direct structural residual-kill conclusion stated",
            StatusMark.DEFER,
            "direct L_double = 0 not derived; next route is inertness/no-reentry attempt",
        )


def case_6_failure_controls(out: ScriptOutput) -> None:
    header("Case 6: Failure controls")
    print("The structural residual-kill law attempt fails if a later script allows:")
    print()
    print("1. zeta_residual_metric = 0 by declaration")
    print("2. kappa_metric = 0 by diagnostic label")
    print("3. epsilon_vac_metric or e_kappa_metric = 0 by accounting label")
    print("4. count-once requirement treated as kill law")
    print("5. source no-double-counting treated as metric kill law")
    print("6. boundary/scalar silence treated as interior residual kill law")
    print("7. recovery target selects L_double = 0")
    print("8. boundary/source failure selects L_double = 0")
    print("9. K_res becomes hidden O eraser")
    print("10. direct kill attempt licenses insertion or parent closure")

    with out.governance_assessments():
        out.line(
            "structural residual-kill failure controls stated",
            StatusMark.OBLIGATION,
            "future scripts must not convert requirements or labels into direct kill theorem",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Structural residual-kill attempt result:")
    print()
    print("  Direct structural L_double = 0 is not derived under current licensed objects.")
    print("  Count-once, diagnostic-only, accounting-only, source no-double-counting, and boundary/scalar silence are guardrails, not kill laws.")
    print("  epsilon_vac_metric and e_kappa_metric may reduce to an accounting inertness theorem target.")
    print("  zeta_residual_metric and kappa_metric remain unresolved and likely require insertion law, strict no-reentry, or active O.")
    print("  B_s/F_zeta insertion and parent closure remain not ready.")
    print()
    print("Possible next script:")
    print("  candidate_nonmetric_inertness_theorem_attempt.py")
    print()
    print("Tiny goblin label:")
    print("  Zero by law, or not zero.")

    with out.governance_assessments():
        out.line(
            "structural residual-kill law attempt complete",
            StatusMark.PASS,
            "direct kill not derived; inertness/no-reentry route remains next",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, ledger: KillAttemptLedger) -> None:
    ns.record_derivation(
        derivation_id="structural_residual_kill_attempt_gap_26",
        inputs=[
            ledger.zeta_kill_gap,
            ledger.kappa_kill_gap,
            ledger.epsilon_kill_gap,
            ledger.e_kappa_kill_gap,
        ],
        output=ledger.direct_kill_gap,
        method="sum unresolved direct structural kill gaps for L_double entries",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="structural_residual_kill_gap",
        scope="Group 26 residual control theorem attempt",
    )

    ns.record_derivation(
        derivation_id="structural_residual_kill_law_attempt_marker_26",
        inputs=[
            sp.Symbol("zeta_residual_metric"),
            sp.Symbol("kappa_metric"),
            sp.Symbol("epsilon_vac_metric"),
            sp.Symbol("e_kappa_metric"),
            sp.Symbol("direct_kill_tests"),
        ],
        output=sp.Symbol("structural_residual_kill_law_not_derived"),
        method="Group 26 direct structural residual-kill law attempt",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="theorem_attempt_marker",
        scope="Group 26 residual control theorem attempt",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g26_direct_kill_zeta_residual", "Derive direct kill for zeta residual metric trace"),
        ("g26_direct_kill_kappa_metric", "Derive direct kill for kappa metric trace"),
        ("g26_direct_kill_epsilon_metric", "Derive direct kill or inertness reduction for epsilon_vac metric channel"),
        ("g26_direct_kill_e_kappa_metric", "Derive direct kill or inertness reduction for e_kappa metric channel"),
        ("g26_do_not_use_recovery_as_kill", "Do not use recovery as residual-kill law"),
        ("g26_do_not_use_boundary_source_as_kill", "Do not use boundary/source failure as residual-kill law"),
        ("g26_do_not_use_hidden_O_as_kill", "Do not use hidden O as residual-kill law"),
        ("g26_keep_insertion_parent_closed_after_direct_kill_attempt", "Keep insertion and parent gates closed after direct kill attempt"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g26_structural_residual_kill_attempt_route"],
            description=(
                "Direct structural residual kill is not derived here. Future work must derive zero by law or reduce entries to inertness/no-reentry/active-O routes without recovery, repair, insertion, or parent shortcuts."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g26_direct_kill_zeta_residual",
        "g26_direct_kill_kappa_metric",
        "g26_direct_kill_epsilon_metric",
        "g26_direct_kill_e_kappa_metric",
        "g26_do_not_use_recovery_as_kill",
        "g26_do_not_use_boundary_source_as_kill",
        "g26_do_not_use_hidden_O_as_kill",
        "g26_keep_insertion_parent_closed_after_direct_kill_attempt",
    ]

    ns.record_route(RouteRecord(
        route_id="g26_structural_residual_kill_attempt_route",
        script_id=SCRIPT_ID,
        name="Group 26 direct structural residual-kill law attempt",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "L_double entries are killed by structural law",
            "no residual entry is killed by declaration or label",
            "recovery does not select kill law",
            "boundary/source failure does not select kill law",
            "hidden O is not used",
            "insertion and parent gates remain closed",
        ],
    ))

    for branch_id in [
        "zeta_zero_by_naming",
        "kappa_zero_by_diagnostic_label",
        "epsilon_ekappa_zero_by_accounting_label",
        "count_once_as_kill_law",
        "source_guardrail_as_metric_kill",
        "boundary_silence_as_interior_kill",
        "recovery_selected_L_double_zero",
        "boundary_source_selected_L_double_zero",
        "K_res_hidden_O",
        "direct_kill_opens_insertion_parent",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}_26",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; direct residual kill must be structural, not named, repaired, or smuggled.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g26_direct_structural_residual_kill_not_derived",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Direct structural L_double = 0 is not derived under current licensed objects. Count-once, diagnostic-only, accounting-only, "
            "source no-double-counting, and boundary/scalar silence are guardrails, not kill laws. epsilon_vac_metric and e_kappa_metric may reduce "
            "to accounting inertness theorem targets; zeta_residual_metric and kappa_metric remain unresolved. B_s/F_zeta insertion and parent closure remain not ready."
        ),
        derivation_ids=[
            "structural_residual_kill_attempt_gap_26",
            "structural_residual_kill_law_attempt_marker_26",
        ],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Structural Residual Kill Law Attempt")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    ledger = build_ledger()
    entries = build_kill_entries()
    tests = build_tests()
    shortcuts = build_rejected_shortcuts()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_kill_ledger(ledger, out)
    case_2_residual_entries(entries, out)
    case_3_structural_tests(tests, out)
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
