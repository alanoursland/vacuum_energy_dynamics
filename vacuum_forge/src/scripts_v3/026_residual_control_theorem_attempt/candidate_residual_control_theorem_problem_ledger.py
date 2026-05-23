# Candidate residual control theorem problem ledger
#
# Group:
#   26_residual_control_theorem_attempt
#
# Script type:
#   THEOREM ATTEMPT / PROBLEM LEDGER
#
# Purpose
# -------
# Open Group 26 by separating what would count as an actual residual-control
# theorem from labels, diagnostics, placeholders, and repair routes.
#
# Locked-door question:
#
#   What exactly would count as a residual-control theorem?
#
# This script does not derive residual kill.
# It does not derive strict non-metric inertness.
# It does not derive active no-overlap O.
# It does not derive count-once recombination.
# It does not derive B_s/F_zeta insertion.
# It does not open parent equation closure.
#
# It defines the theorem-attempt target:
#
#   L_double = e_kappa_metric
#            + epsilon_vac_metric
#            + kappa_metric
#            + zeta_residual_metric
#
# must be killed by structural law, made strictly inert/non-metric/
# non-reentering sector-by-sector, or shown to require a real active
# no-overlap operator.
#
# Tiny goblin rule:
#
#   Try the key.
#   Do not paint the door open.

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
        "ADMISSIBLE_TARGET": StatusMark.OBLIGATION,
        "BLOCKED": StatusMark.FAIL,
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
            "g25_problem_dep_26",
            "025_residual_kill_or_no_overlap_theorem__candidate_residual_kill_problem_ledger",
            "residual_kill_problem_ledger_marker_25",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g25_theorem_obligation_dep_26",
            "025_residual_kill_or_no_overlap_theorem__candidate_residual_kill_theorem_obligations",
            "residual_kill_theorem_obligations_marker_25",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g25_summary_dep_26",
            "025_residual_kill_or_no_overlap_theorem__candidate_group_25_residual_kill_status_summary",
            "group25_residual_kill_status_summary_marker_25",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g24_summary_dep_26",
            "024_metric_insertion_recovery_retest__candidate_group_24_metric_insertion_status_summary",
            "group24_metric_insertion_status_summary_marker_24",
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
class ResidualControlTheoremLedger:
    zeta_residual_metric: sp.Symbol
    kappa_metric: sp.Symbol
    epsilon_vac_metric: sp.Symbol
    e_kappa_metric: sp.Symbol
    zeta_to_Bs: sp.Symbol
    L_double: sp.Expr
    T_total: sp.Expr
    K_res: sp.Symbol
    I_res: sp.Symbol
    R_res: sp.Symbol
    O_active: sp.Symbol
    theorem_gap: sp.Expr


@dataclass
class TheoremCandidateRoute:
    name: str
    route: str
    status: str
    would_count_if: str
    fails_if: str


@dataclass
class AdmissibilityCondition:
    name: str
    condition: str
    status: str
    theorem_use: str
    failure_if: str


@dataclass
class RejectedPseudoTheorem:
    name: str
    pseudo_theorem: str
    forbidden_use: str
    status: str
    consequence: str


@dataclass
class TheoremAttemptBoundary:
    name: str
    boundary: str
    status: str
    reason: str


# =============================================================================
# Builders
# =============================================================================


def build_ledger() -> ResidualControlTheoremLedger:
    (
        zeta_residual_metric,
        kappa_metric,
        epsilon_vac_metric,
        e_kappa_metric,
        zeta_to_Bs,
        K_res,
        I_res,
        R_res,
        O_active,
    ) = sp.symbols(
        "zeta_residual_metric kappa_metric epsilon_vac_metric e_kappa_metric zeta_to_Bs K_res I_res R_res O_active",
        real=True,
    )

    L_double = sp.simplify(
        zeta_residual_metric
        + kappa_metric
        + epsilon_vac_metric
        + e_kappa_metric
    )

    T_total = sp.simplify(zeta_to_Bs + L_double)

    # Theorem gap:
    #   K_res, I_res, R_res, and O_active are possible theorem mechanisms,
    #   but none is assumed active. The gap remains until one route is derived.
    theorem_gap = sp.simplify(L_double - K_res - I_res - R_res - O_active)

    return ResidualControlTheoremLedger(
        zeta_residual_metric=zeta_residual_metric,
        kappa_metric=kappa_metric,
        epsilon_vac_metric=epsilon_vac_metric,
        e_kappa_metric=e_kappa_metric,
        zeta_to_Bs=zeta_to_Bs,
        L_double=L_double,
        T_total=T_total,
        K_res=K_res,
        I_res=I_res,
        R_res=R_res,
        O_active=O_active,
        theorem_gap=theorem_gap,
    )


def build_candidate_routes() -> List[TheoremCandidateRoute]:
    return [
        TheoremCandidateRoute(
            name="T1: structural residual kill",
            route="derive L_double = 0 by a structural residual-kill law",
            status="THEOREM_ATTEMPT",
            would_count_if="zeta_residual_metric, kappa_metric, epsilon_vac_metric, and e_kappa_metric are killed by derived law before recovery",
            fails_if="any entry is set to zero by declaration, naming, recovery, boundary/source failure, or parent fit",
        ),
        TheoremCandidateRoute(
            name="T2: strict inertness / non-metric theorem",
            route="derive each L_double entry strictly inert, non-metric, non-sourcing, and non-reentering",
            status="THEOREM_ATTEMPT",
            would_count_if="every residual entry has no metric/source/boundary/support/recovery/repair/parent role sector-by-sector",
            fails_if="non-metric or inert labels substitute for no-reentry proof",
        ),
        TheoremCandidateRoute(
            name="T3: sector-by-sector non-reentry theorem",
            route="derive residual reentry load vanishes through every known channel",
            status="THEOREM_ATTEMPT",
            would_count_if="metric, source, boundary, support, recovery, repair, and parent reentry vanish separately",
            fails_if="unsafe channels cancel only in total",
        ),
        TheoremCandidateRoute(
            name="T4: controlled obstruction theorem",
            route="show no current non-O route closes under licensed objects",
            status="THEOREM_ATTEMPT",
            would_count_if="a specific missing object blocks every non-O route without claiming mathematical impossibility beyond the audited assumptions",
            fails_if="obstruction is asserted without testing direct kill, inertness, and non-reentry routes",
        ),
        TheoremCandidateRoute(
            name="T5: active-O necessity or deferral result",
            route="show active O is required, optional, or deferred",
            status="THEOREM_ATTEMPT",
            would_count_if="the status follows from the tested theorem routes and does not invoke O as eraser by name",
            fails_if="active O is used before domain/codomain/kernel/image/divergence/boundary/source structure is derived",
        ),
        TheoremCandidateRoute(
            name="T6: coefficient-origin dependency result",
            route="show residual control depends on B_s/F_zeta insertion law or coefficient origin",
            status="THEOREM_ATTEMPT",
            would_count_if="the dependency is identified without licensing insertion",
            fails_if="missing coefficient origin is treated as solved insertion",
        ),
    ]


def build_admissibility_conditions() -> List[AdmissibilityCondition]:
    return [
        AdmissibilityCondition(
            name="A1: structural origin",
            condition="the residual-control mechanism has a structural origin",
            status="REQUIRED",
            theorem_use="required for kill, inertness, non-reentry, or obstruction claims",
            failure_if="mechanism is introduced as a label or bookkeeping preference",
        ),
        AdmissibilityCondition(
            name="A2: recovery independence",
            condition="residual status is fixed before recovery diagnostics",
            status="REQUIRED",
            theorem_use="prevents recovery from constructing the theorem",
            failure_if="Schwarzschild, AB=1, B=1/A, gamma_like, PPN, or areal kappa selects status",
        ),
        AdmissibilityCondition(
            name="A3: sector-by-sector no-reentry",
            condition="metric/source/boundary/support/recovery/repair/parent reentry channels vanish separately",
            status="REQUIRED",
            theorem_use="required for inertness and non-reentry claims",
            failure_if="total cancellation is used as non-reentry",
        ),
        AdmissibilityCondition(
            name="A4: boundary/source independence",
            condition="residual control is not selected from tail, flux, shell, mass shift, support load, or source duplication",
            status="REQUIRED",
            theorem_use="prevents residual cleanup from becoming a repair route",
            failure_if="boundary/source failure chooses residual status",
        ),
        AdmissibilityCondition(
            name="A5: active O discipline",
            condition="active O is unavailable unless real operator structure is derived",
            status="REQUIRED",
            theorem_use="prevents O from erasing overlap by name",
            failure_if="O acts without domain, codomain, kernel, image, composition, pairing, divergence, boundary, source, mass, scalar/current/support behavior, and recovery independence",
        ),
        AdmissibilityCondition(
            name="A6: no insertion license",
            condition="residual control does not by itself license B_s/F_zeta insertion",
            status="REQUIRED",
            theorem_use="keeps residual control separate from insertion law and coefficient origin",
            failure_if="residual cleanup is treated as metric insertion theorem",
        ),
        AdmissibilityCondition(
            name="A7: no parent closure",
            condition="residual control does not open parent field equation",
            status="REQUIRED",
            theorem_use="prevents parent identity from being smuggled",
            failure_if="parent closure follows from residual cleanup alone",
        ),
    ]


def build_rejected_pseudo_theorems() -> List[RejectedPseudoTheorem]:
    return [
        RejectedPseudoTheorem(
            name="P1: kill by declaration",
            pseudo_theorem="declare L_double = 0",
            forbidden_use="turning zero-by-statement into residual-kill theorem",
            status="REJECTED",
            consequence="count-once recombination is smuggled",
        ),
        RejectedPseudoTheorem(
            name="P2: nonmetric by vocabulary",
            pseudo_theorem="call residuals non-metric or inert",
            forbidden_use="using a label instead of no-reentry proof",
            status="REJECTED",
            consequence="residuals may still re-enter",
        ),
        RejectedPseudoTheorem(
            name="P3: diagnostic-only becomes construction",
            pseudo_theorem="diagnostic residual status later supplies insertion, source, boundary, support, or recovery data",
            forbidden_use="diagnostic label used as construction mechanism",
            status="REJECTED",
            consequence="diagnostic/inert distinction collapses",
        ),
        RejectedPseudoTheorem(
            name="P4: O by another name",
            pseudo_theorem="K_res, I_res, R_res, or another symbol erases residuals like O without operator burden",
            forbidden_use="renaming active O to avoid O obligations",
            status="REJECTED",
            consequence="fake operator eraser returns",
        ),
        RejectedPseudoTheorem(
            name="P5: recovery-selected theorem",
            pseudo_theorem="choose residual status because recovery works only if it is chosen",
            forbidden_use="Schwarzschild/gamma/AB/B=1/A/PPN/areal-kappa recovery selects residual control",
            status="REJECTED",
            consequence="recovery constructs theorem",
        ),
        RejectedPseudoTheorem(
            name="P6: repair-selected theorem",
            pseudo_theorem="choose residual status to remove boundary, source, support, or mass failure",
            forbidden_use="tail, flux, shell, source duplication, or support load selects residual control",
            status="REJECTED",
            consequence="residual theorem becomes repair patch",
        ),
        RejectedPseudoTheorem(
            name="P7: insertion from cleanup",
            pseudo_theorem="residual cleanup licenses B_s/F_zeta insertion",
            forbidden_use="residual theorem replaces insertion law and coefficient origin",
            status="REJECTED",
            consequence="metric insertion is smuggled",
        ),
        RejectedPseudoTheorem(
            name="P8: parent from cleanup",
            pseudo_theorem="residual cleanup opens parent equation",
            forbidden_use="residual theorem replaces parent identity and divergence closure",
            status="REJECTED",
            consequence="parent equation is smuggled",
        ),
    ]


def build_attempt_boundaries() -> List[TheoremAttemptBoundary]:
    return [
        TheoremAttemptBoundary(
            name="B1: theorem attempt may close no route",
            boundary="it is admissible to conclude no residual-control route is derived under current licensed objects",
            status="SAFE_IF",
            reason="negative closure localizes the obstruction without overclaiming",
        ),
        TheoremAttemptBoundary(
            name="B2: theorem attempt may close a partial route",
            boundary="it is admissible to control epsilon/e_kappa or diagnostic residues while leaving zeta/kappa open",
            status="SAFE_IF",
            reason="partial residual control is useful if exact controlled entries are named",
        ),
        TheoremAttemptBoundary(
            name="B3: theorem attempt may require active O",
            boundary="it is admissible to hand off to active O construction if non-O routes do not close",
            status="SAFE_IF",
            reason="O necessity/deferral is a valid theorem-attempt outcome if not used as proof",
        ),
        TheoremAttemptBoundary(
            name="B4: theorem attempt may depend on B_s/F_zeta coefficient origin",
            boundary="it is admissible to identify coefficient-origin as the sharper missing object",
            status="SAFE_IF",
            reason="residual control may be underdetermined until insertion law is specified",
        ),
        TheoremAttemptBoundary(
            name="B5: theorem attempt may not open parent closure",
            boundary="it is never admissible to open parent equation from residual-control attempt alone",
            status="REJECTED",
            reason="parent closure requires separate identity, divergence, source, boundary, support, and insertion theorems",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Residual-control theorem attempt problem")
    print("Question:")
    print()
    print("  What exactly would count as a residual-control theorem?")
    print()
    print("Reference discipline:")
    print()
    print("  This group is a theorem attempt, not another requirements restatement.")
    print("  A theorem route must actually close L_double, prove strict inertness/no-reentry, or identify a controlled obstruction.")
    print("  Labels, recovery success, boundary/source repair, O by name, and parent-looking closure do not count.")

    with out.governance_assessments():
        out.line(
            "residual-control theorem attempt opened",
            StatusMark.INFO,
            "separating admissible theorem targets from labels and pseudo-theorems",
        )


def case_1_theorem_target_ledger(ledger: ResidualControlTheoremLedger, out: ScriptOutput) -> None:
    header("Case 1: Residual-control theorem target ledger")
    print("Safe scalar trace target:")
    print()
    print(f"  zeta_to_Bs = {sp.sstr(ledger.zeta_to_Bs)}")
    print()
    print("Residual double-count entries:")
    print()
    print(f"  zeta_residual_metric = {sp.sstr(ledger.zeta_residual_metric)}")
    print(f"  kappa_metric = {sp.sstr(ledger.kappa_metric)}")
    print(f"  epsilon_vac_metric = {sp.sstr(ledger.epsilon_vac_metric)}")
    print(f"  e_kappa_metric = {sp.sstr(ledger.e_kappa_metric)}")
    print()
    print("Total scalar metric-trace ledger:")
    print()
    print(f"  T_total = {sp.sstr(ledger.T_total)}")
    print()
    print("Double-count load:")
    print()
    print(f"  L_double = {sp.sstr(ledger.L_double)}")
    print()
    print("Possible theorem mechanism placeholders:")
    print()
    print(f"  K_res = {sp.sstr(ledger.K_res)}")
    print(f"  I_res = {sp.sstr(ledger.I_res)}")
    print(f"  R_res = {sp.sstr(ledger.R_res)}")
    print(f"  O_active = {sp.sstr(ledger.O_active)}")
    print()
    print("Theorem gap:")
    print()
    print(f"  gap_theorem = {sp.sstr(ledger.theorem_gap)}")
    print()
    print("Interpretation:")
    print()
    print("  K_res, I_res, R_res, and O_active are not active by name.")
    print("  One route must be structurally derived before L_double is controlled.")

    with out.derived_results():
        out.line(
            "residual-control theorem target total trace stated",
            StatusMark.PASS,
            f"T_total = {sp.sstr(ledger.T_total)}",
        )
        out.line(
            "residual-control double-count load stated",
            StatusMark.OBLIGATION,
            f"L_double = {sp.sstr(ledger.L_double)}",
        )
        out.line(
            "residual-control theorem gap stated",
            StatusMark.OBLIGATION,
            f"gap_theorem = {sp.sstr(ledger.theorem_gap)}",
        )


def case_2_candidate_routes(routes: List[TheoremCandidateRoute], out: ScriptOutput) -> None:
    header("Case 2: Candidate residual-control theorem routes")
    for route in routes:
        print()
        print("-" * 120)
        print(route.name)
        print("-" * 120)
        print(f"Route: {route.route}")
        print(f"[{status_mark(route.status).value}] {route.name}: {route.status}")
        print(f"Would count if: {route.would_count_if}")
        print(f"Fails if: {route.fails_if}")

    with out.governance_assessments():
        out.line(
            "candidate residual-control theorem routes classified",
            StatusMark.PASS,
            f"{len(routes)} theorem-attempt routes classified",
        )


def case_3_admissibility_conditions(conditions: List[AdmissibilityCondition], out: ScriptOutput) -> None:
    header("Case 3: Theorem admissibility conditions")
    for condition in conditions:
        print()
        print("-" * 120)
        print(condition.name)
        print("-" * 120)
        print(f"Condition: {condition.condition}")
        print(f"[{status_mark(condition.status).value}] {condition.name}: {condition.status}")
        print(f"Theorem use: {condition.theorem_use}")
        print(f"Failure if: {condition.failure_if}")

    with out.unresolved_obligations():
        out.line(
            "residual-control theorem admissibility conditions populated",
            StatusMark.OBLIGATION,
            f"{len(conditions)} admissibility conditions constrain Group 26 theorem attempts",
        )


def case_4_rejected_pseudo_theorems(pseudo_theorems: List[RejectedPseudoTheorem], out: ScriptOutput) -> None:
    header("Case 4: Rejected residual-control pseudo-theorems")
    for item in pseudo_theorems:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Pseudo-theorem: {item.pseudo_theorem}")
        print(f"Forbidden use: {item.forbidden_use}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Consequence: {item.consequence}")

    with out.counterexamples():
        out.line(
            "residual-control pseudo-theorems rejected",
            StatusMark.FAIL,
            "declaration, vocabulary, diagnostic construction, fake O, recovery/repair selection, insertion, and parent shortcuts are rejected",
        )


def case_5_attempt_boundaries(boundaries: List[TheoremAttemptBoundary], out: ScriptOutput) -> None:
    header("Case 5: Theorem-attempt boundaries")
    for boundary in boundaries:
        print()
        print("-" * 120)
        print(boundary.name)
        print("-" * 120)
        print(f"Boundary: {boundary.boundary}")
        print(f"[{status_mark(boundary.status).value}] {boundary.name}: {boundary.status}")
        print(f"Reason: {boundary.reason}")

    with out.governance_assessments():
        out.line(
            "residual-control theorem-attempt boundaries stated",
            StatusMark.PASS,
            "partial success, controlled obstruction, O handoff, or coefficient-origin dependency are admissible; parent closure is not",
        )


def case_6_failure_controls(out: ScriptOutput) -> None:
    header("Case 6: Failure controls")
    print("The residual-control theorem problem ledger fails if a later script allows:")
    print()
    print("1. L_double killed by declaration")
    print("2. zeta_residual_metric, kappa_metric, epsilon_vac_metric, or e_kappa_metric set zero by naming")
    print("3. nonmetric or inert status used without no-reentry proof")
    print("4. diagnostic-only status used as construction data")
    print("5. total cancellation treated as no-reentry")
    print("6. K_res, I_res, R_res, or O_active erases residuals by name")
    print("7. residual status selected from recovery")
    print("8. residual status selected from boundary/source/support failure")
    print("9. residual cleanup licenses B_s/F_zeta insertion")
    print("10. residual cleanup opens parent equation")

    with out.governance_assessments():
        out.line(
            "residual-control theorem attempt failure controls stated",
            StatusMark.OBLIGATION,
            "future scripts must actually attempt theorem routes without painting the door open",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Group 26 opening result:")
    print()
    print("  A residual-control theorem must actually control L_double.")
    print("  Allowed theorem-attempt routes are structural kill, strict inertness/no-reentry, controlled obstruction, active-O necessity/deferral, or coefficient-origin dependency.")
    print("  Labels, diagnostics, recovery success, boundary/source repair, fake O, insertion licensing, and parent closure do not count.")
    print("  This script does not derive residual control.")
    print()
    print("Possible next script:")
    print("  candidate_structural_residual_kill_law_attempt.py")
    print()
    print("Tiny goblin label:")
    print("  Try the key. Do not paint the door open.")

    with out.governance_assessments():
        out.line(
            "residual-control theorem problem ledger complete",
            StatusMark.PASS,
            "admissible theorem-attempt routes defined; residual control remains open",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, ledger: ResidualControlTheoremLedger) -> None:
    ns.record_derivation(
        derivation_id="residual_control_theorem_attempt_target_26",
        inputs=[
            ledger.zeta_to_Bs,
            ledger.zeta_residual_metric,
            ledger.kappa_metric,
            ledger.epsilon_vac_metric,
            ledger.e_kappa_metric,
        ],
        output=sp.Tuple(ledger.T_total, ledger.L_double),
        method="state scalar trace target and residual double-count load for theorem attempt",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="residual_control_theorem_target",
        scope="Group 26 residual control theorem attempt",
    )

    ns.record_derivation(
        derivation_id="residual_control_theorem_gap_26",
        inputs=[
            ledger.L_double,
            ledger.K_res,
            ledger.I_res,
            ledger.R_res,
            ledger.O_active,
        ],
        output=ledger.theorem_gap,
        method="state theorem-control gap without activating any placeholder mechanism",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="residual_control_theorem_gap",
        scope="Group 26 residual control theorem attempt",
    )

    ns.record_derivation(
        derivation_id="residual_control_theorem_problem_marker_26",
        inputs=[
            sp.Symbol("L_double"),
            sp.Symbol("structural_kill"),
            sp.Symbol("strict_inertness"),
            sp.Symbol("sector_by_sector_nonreentry"),
            sp.Symbol("active_O_necessity"),
            sp.Symbol("coefficient_origin_dependency"),
        ],
        output=sp.Symbol("residual_control_theorem_problem_stated"),
        method="Group 26 residual-control theorem problem ledger",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="theorem_attempt_marker",
        scope="Group 26 residual control theorem attempt",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g26_attempt_structural_residual_kill", "Attempt structural residual-kill law"),
        ("g26_attempt_strict_inertness", "Attempt strict non-metric inertness law"),
        ("g26_attempt_sector_nonreentry", "Attempt sector-by-sector residual non-reentry"),
        ("g26_test_nonO_obstruction", "Test whether non-O residual control is obstructed"),
        ("g26_classify_active_O_need", "Classify active-O necessity, optionality, or deferral"),
        ("g26_test_coefficient_origin_dependency", "Test B_s/F_zeta coefficient-origin dependency"),
        ("g26_preserve_recovery_independence", "Preserve recovery independence"),
        ("g26_preserve_boundary_source_independence", "Preserve boundary/source independence"),
        ("g26_keep_insertion_parent_closed", "Keep insertion and parent gates closed"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g26_residual_control_theorem_attempt_route"],
            description=(
                "Group 26 is a theorem attempt. Residual control remains open until a structural kill, strict inertness, "
                "sector-by-sector non-reentry, controlled obstruction, active-O classification, or coefficient-origin dependency is derived without recovery, repair, insertion, or parent smuggling."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g26_attempt_structural_residual_kill",
        "g26_attempt_strict_inertness",
        "g26_attempt_sector_nonreentry",
        "g26_test_nonO_obstruction",
        "g26_classify_active_O_need",
        "g26_test_coefficient_origin_dependency",
        "g26_preserve_recovery_independence",
        "g26_preserve_boundary_source_independence",
        "g26_keep_insertion_parent_closed",
    ]

    ns.record_route(RouteRecord(
        route_id="g26_residual_control_theorem_attempt_route",
        script_id=SCRIPT_ID,
        name="Group 26 residual-control theorem attempt route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "L_double is actually controlled or a controlled obstruction is derived",
            "labels are not used as proof",
            "recovery does not select residual status",
            "boundary/source failure does not select residual cleanup",
            "O is not used by name",
            "insertion and parent gates remain closed unless separately derived",
        ],
    ))

    for branch_id in [
        "L_double_zero_by_declaration",
        "nonmetric_label_as_theorem",
        "diagnostic_status_as_construction",
        "fake_O_by_renaming",
        "recovery_selected_residual_theorem",
        "boundary_source_repair_residual_theorem",
        "residual_cleanup_licenses_Bs_Fzeta",
        "residual_cleanup_opens_parent",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}_26",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; Group 26 theorem attempt must not replace proof with labels, repair, insertion, or parent shortcuts.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g26_residual_control_theorem_attempt_defined_not_solved",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "A residual-control theorem must structurally control L_double, prove strict sector-by-sector inertness/non-reentry, "
            "derive a controlled obstruction, classify active-O necessity/deferral, or identify coefficient-origin dependency. "
            "Declarations, labels, diagnostics, recovery selection, boundary/source repair, fake O, insertion licensing, and parent closure do not count. "
            "This opening script does not solve residual control."
        ),
        derivation_ids=[
            "residual_control_theorem_attempt_target_26",
            "residual_control_theorem_gap_26",
            "residual_control_theorem_problem_marker_26",
        ],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Residual Control Theorem Problem Ledger")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    ledger = build_ledger()
    routes = build_candidate_routes()
    conditions = build_admissibility_conditions()
    pseudo_theorems = build_rejected_pseudo_theorems()
    boundaries = build_attempt_boundaries()

    case_0_problem_statement(out)
    case_1_theorem_target_ledger(ledger, out)
    case_2_candidate_routes(routes, out)
    case_3_admissibility_conditions(conditions, out)
    case_4_rejected_pseudo_theorems(pseudo_theorems, out)
    case_5_attempt_boundaries(boundaries, out)
    case_6_failure_controls(out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns, ledger)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
