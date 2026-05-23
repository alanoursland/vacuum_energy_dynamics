# Candidate gamma AB recovery diagnostics
#
# Group:
#   24_metric_insertion_recovery_retest
#
# Script type:
#   DIAGNOSTIC / REQUIREMENTS
#
# Purpose
# -------
# Audit gamma-like and AB diagnostics after anti-smuggling and count-once
# constraints.
#
# Locked-door question:
#
#   What do gamma-like and AB diagnostics say after anti-smuggling constraints?
#
# This script does not derive B_s/F_zeta insertion.
# It does not prove gamma-like recovery.
# It does not prove AB=1 as a parent law.
# It does not prove B=1/A as a construction rule.
# It does not promote areal kappa to a physical scalar.
# It does not open the parent field equation.
#
# It runs reduced recovery diagnostics without using them as construction rules.

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
        "ALLOWED_AUDIT": StatusMark.INFO,
        "BLOCKED": StatusMark.FAIL,
        "CLOSED_DIAGNOSTIC": StatusMark.PASS,
        "DIAGNOSTIC_ONLY": StatusMark.INFO,
        "NOT_READY": StatusMark.DEFER,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "SAFE_IF": StatusMark.INFO,
        "THEOREM_TARGET": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "metric_retest_dep_24",
            "24_metric_insertion_recovery_retest__candidate_metric_insertion_retest_ledger",
            "metric_insertion_retest_ledger_marker_24",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "recovery_antismuggle_dep_24",
            "24_metric_insertion_recovery_retest__candidate_recovery_target_anti_smuggling_audit",
            "recovery_target_anti_smuggling_marker_24",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "count_once_dep_24",
            "24_metric_insertion_recovery_retest__candidate_count_once_metric_trace_audit",
            "count_once_metric_trace_marker_24",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g23_summary_dep_24",
            "23_smooth_support_and_matching_laws__candidate_group_23_matching_laws_status_summary",
            "group23_matching_laws_status_summary_marker_23",
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
class GammaABDiagnostic:
    A_weak: sp.Expr
    B_candidate: sp.Expr
    AB_product: sp.Expr
    kappa_areal: sp.Expr
    gamma_like: sp.Expr
    AB_deviation: sp.Expr
    gamma_deviation: sp.Expr


@dataclass
class RecoveryDiagnosticCase:
    name: str
    candidate_description: str
    status: str
    diagnostic_result: str
    allowed_interpretation: str
    forbidden_interpretation: str


@dataclass
class RecoveryDiagnosticRule:
    name: str
    rule: str
    status: str
    failure_if: str


@dataclass
class RejectedRecoveryUpgrade:
    name: str
    rejected_upgrade: str
    status: str
    reason: str


# =============================================================================
# Builders
# =============================================================================


def build_reduced_diagnostic_expressions() -> GammaABDiagnostic:
    x, gamma_s, beta_AB = sp.symbols("x gamma_s beta_AB", real=True)

    # Reduced weak-field placeholder:
    # A = 1 - 2x.
    # Candidate B = 1 + 2 gamma_s x + beta_AB x**2.
    #
    # gamma_s = 1 gives the GR weak-field spatial coefficient diagnostically.
    # beta_AB controls higher-order/product deviation diagnostically.
    A_weak = sp.simplify(1 - 2 * x)
    B_candidate = sp.simplify(1 + 2 * gamma_s * x + beta_AB * x**2)
    AB_product = sp.series(sp.expand(A_weak * B_candidate), x, 0, 3).removeO()
    kappa_areal = sp.series(sp.Rational(1, 2) * sp.log(AB_product), x, 0, 3).removeO()

    gamma_like = gamma_s
    AB_deviation = sp.simplify(AB_product - 1)
    gamma_deviation = sp.simplify(gamma_like - 1)

    return GammaABDiagnostic(
        A_weak=A_weak,
        B_candidate=B_candidate,
        AB_product=sp.simplify(AB_product),
        kappa_areal=sp.simplify(kappa_areal),
        gamma_like=gamma_like,
        AB_deviation=AB_deviation,
        gamma_deviation=gamma_deviation,
    )


def build_cases() -> List[RecoveryDiagnosticCase]:
    return [
        RecoveryDiagnosticCase(
            name="D1: gamma-like diagnostic",
            candidate_description="weak-field B_candidate = 1 + 2 gamma_s x + beta_AB x^2",
            status="CLOSED_DIAGNOSTIC",
            diagnostic_result="gamma_like = gamma_s; gamma_deviation = gamma_s - 1",
            allowed_interpretation="may classify whether a structurally fixed candidate has GR-like weak-field spatial response",
            forbidden_interpretation="must not choose gamma_s from desired recovery",
        ),
        RecoveryDiagnosticCase(
            name="D2: AB product diagnostic",
            candidate_description="AB = (1 - 2x)(1 + 2 gamma_s x + beta_AB x^2)",
            status="CLOSED_DIAGNOSTIC",
            diagnostic_result="AB_deviation begins at 2x(gamma_s - 1) plus second-order product terms",
            allowed_interpretation="may classify reduced exterior product behavior after candidate is fixed",
            forbidden_interpretation="must not impose AB=1 as parent insertion law",
        ),
        RecoveryDiagnosticCase(
            name="D3: areal kappa diagnostic",
            candidate_description="kappa_areal = 1/2 ln(AB)",
            status="DIAGNOSTIC_ONLY",
            diagnostic_result="kappa_areal measures reduced AB deviation diagnostically",
            allowed_interpretation="may audit areal-gauge product behavior",
            forbidden_interpretation="must not promote areal kappa to physical scalar dynamics",
        ),
        RecoveryDiagnosticCase(
            name="D4: B=1/A static exterior check",
            candidate_description="B=1/A in reduced static exterior",
            status="ALLOWED_AUDIT",
            diagnostic_result="valid as reduced exterior check when branch data are already fixed",
            allowed_interpretation="may confirm a branch matches known exterior relation",
            forbidden_interpretation="must not construct B_s generally by inverse A",
        ),
        RecoveryDiagnosticCase(
            name="D5: count-once recovery check",
            candidate_description="gamma/AB diagnostics with residual trace load already killed or inert",
            status="SAFE_IF",
            diagnostic_result="diagnostic is meaningful only after double-count load is absent",
            allowed_interpretation="may test fixed branch under count-once convention",
            forbidden_interpretation="must not select residual-kill/nonmetric status to pass diagnostics",
        ),
    ]


def build_rules() -> List[RecoveryDiagnosticRule]:
    return [
        RecoveryDiagnosticRule(
            name="R1: diagnostic after structure",
            rule="gamma-like and AB diagnostics may be evaluated only after F_zeta form and coefficients are fixed structurally or left theorem-targeted",
            status="REQUIRED",
            failure_if="diagnostic target chooses coefficient",
        ),
        RecoveryDiagnosticRule(
            name="R2: AB diagnostic not parent law",
            rule="AB=1 is a reduced exterior diagnostic, not a general insertion law",
            status="REQUIRED",
            failure_if="AB=1 is used to derive B_s",
        ),
        RecoveryDiagnosticRule(
            name="R3: B inverse A diagnostic not construction",
            rule="B=1/A is a static exterior check, not a general B_s construction rule",
            status="REQUIRED",
            failure_if="B_s is set by inverse A outside a derived theorem",
        ),
        RecoveryDiagnosticRule(
            name="R4: kappa areal diagnostic only",
            rule="kappa_areal = 1/2 ln(AB) remains gauge/reduced diagnostic unless separately derived",
            status="REQUIRED",
            failure_if="kappa_areal becomes physical scalar insertion route",
        ),
        RecoveryDiagnosticRule(
            name="R5: count-once before recovery interpretation",
            rule="residual zeta/kappa metric trace must be killed, inert, or theorem-routed before recovery diagnostics license insertion",
            status="REQUIRED",
            failure_if="recovery success hides residual double-counting",
        ),
        RecoveryDiagnosticRule(
            name="R6: parent gate remains closed",
            rule="successful gamma-like or AB diagnostic does not open the parent equation",
            status="REQUIRED",
            failure_if="parent closure is inferred from reduced recovery",
        ),
    ]


def build_rejected_upgrades() -> List[RejectedRecoveryUpgrade]:
    return [
        RejectedRecoveryUpgrade(
            name="U1: gamma diagnostic becomes coefficient law",
            rejected_upgrade="setting gamma_s from the desired recovery target",
            status="REJECTED",
            reason="gamma-like behavior may audit but not construct the branch",
        ),
        RejectedRecoveryUpgrade(
            name="U2: AB diagnostic becomes parent equation",
            rejected_upgrade="using AB=1 as parent insertion law",
            status="REJECTED",
            reason="AB product behavior is reduced diagnostic unless derived generally",
        ),
        RejectedRecoveryUpgrade(
            name="U3: B=1/A becomes construction rule",
            rejected_upgrade="setting B_s = 1/A by exterior recovery",
            status="REJECTED",
            reason="static exterior relation cannot construct general scalar spatial response",
        ),
        RejectedRecoveryUpgrade(
            name="U4: areal kappa becomes scalar source",
            rejected_upgrade="promoting kappa_areal to physical scalar dynamics",
            status="REJECTED",
            reason="kappa_areal remains reduced/gauge diagnostic unless derived",
        ),
        RejectedRecoveryUpgrade(
            name="U5: count-once burden hidden by recovery",
            rejected_upgrade="using successful recovery diagnostic to ignore residual double-count load",
            status="REJECTED",
            reason="recovery cannot hide residual trace overlap",
        ),
        RejectedRecoveryUpgrade(
            name="U6: parent gate opens from diagnostics",
            rejected_upgrade="opening parent equation from gamma/AB diagnostic success",
            status="REJECTED",
            reason="parent closure requires insertion, source, boundary, support, no-overlap, and divergence theorems",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Gamma / AB recovery diagnostics problem")
    print("Question:")
    print()
    print("  What do gamma-like and AB diagnostics say after anti-smuggling constraints?")
    print()
    print("Reference discipline:")
    print()
    print("  Recovery diagnostics may classify fixed candidates.")
    print("  They may not choose insertion coefficients.")
    print("  AB=1 and B=1/A remain reduced diagnostics, not parent laws.")
    print("  Count-once residual discipline must be preserved.")

    with out.governance_assessments():
        out.line(
            "gamma / AB recovery diagnostics audit opened",
            StatusMark.INFO,
            "running reduced recovery diagnostics without turning them into construction rules",
        )


def case_1_symbolic_diagnostics(diag: GammaABDiagnostic, out: ScriptOutput) -> None:
    header("Case 1: Symbolic gamma / AB diagnostics")
    print("Reduced weak-field placeholder:")
    print()
    print(f"  A_weak = {sp.sstr(diag.A_weak)}")
    print(f"  B_candidate = {sp.sstr(diag.B_candidate)}")
    print()
    print("Diagnostics:")
    print()
    print(f"  AB_product = {sp.sstr(diag.AB_product)}")
    print(f"  AB_deviation = {sp.sstr(diag.AB_deviation)}")
    print(f"  kappa_areal = {sp.sstr(diag.kappa_areal)}")
    print(f"  gamma_like = {sp.sstr(diag.gamma_like)}")
    print(f"  gamma_deviation = {sp.sstr(diag.gamma_deviation)}")
    print()
    print("Interpretation:")
    print()
    print("  gamma_s and beta_AB are diagnostic placeholders.")
    print("  They must be structurally fixed before this diagnostic is interpreted.")
    print("  Setting them from recovery would be smuggling.")

    with out.derived_results():
        out.line(
            "gamma-like diagnostic stated",
            StatusMark.PASS,
            f"gamma_like = {sp.sstr(diag.gamma_like)}, deviation = {sp.sstr(diag.gamma_deviation)}",
        )
        out.line(
            "AB product diagnostic stated",
            StatusMark.PASS,
            f"AB_product = {sp.sstr(diag.AB_product)}, deviation = {sp.sstr(diag.AB_deviation)}",
        )
        out.line(
            "areal kappa diagnostic stated",
            StatusMark.PASS,
            f"kappa_areal = {sp.sstr(diag.kappa_areal)}",
        )


def case_2_diagnostic_cases(cases: List[RecoveryDiagnosticCase], out: ScriptOutput) -> None:
    header("Case 2: Recovery diagnostic cases")
    for case in cases:
        print()
        print("-" * 120)
        print(case.name)
        print("-" * 120)
        print(f"Candidate: {case.candidate_description}")
        print(f"[{status_mark(case.status).value}] {case.name}: {case.status}")
        print(f"Diagnostic result: {case.diagnostic_result}")
        print(f"Allowed interpretation: {case.allowed_interpretation}")
        print(f"Forbidden interpretation: {case.forbidden_interpretation}")

    with out.governance_assessments():
        out.line(
            "gamma / AB diagnostic cases populated",
            StatusMark.PASS,
            f"{len(cases)} reduced recovery diagnostic cases classified",
        )


def case_3_rules(rules: List[RecoveryDiagnosticRule], out: ScriptOutput) -> None:
    header("Case 3: Recovery diagnostic rules")
    for rule in rules:
        print()
        print("-" * 120)
        print(rule.name)
        print("-" * 120)
        print(f"Rule: {rule.rule}")
        print(f"[{status_mark(rule.status).value}] {rule.name}: {rule.status}")
        print(f"Failure if: {rule.failure_if}")

    with out.unresolved_obligations():
        out.line(
            "gamma / AB diagnostic rules populated",
            StatusMark.OBLIGATION,
            f"{len(rules)} recovery diagnostic rules constrain interpretation",
        )


def case_4_rejected_upgrades(upgrades: List[RejectedRecoveryUpgrade], out: ScriptOutput) -> None:
    header("Case 4: Rejected diagnostic upgrades")
    for upgrade in upgrades:
        print()
        print("-" * 120)
        print(upgrade.name)
        print("-" * 120)
        print(f"Rejected upgrade: {upgrade.rejected_upgrade}")
        print(f"[{status_mark(upgrade.status).value}] {upgrade.name}: {upgrade.status}")
        print(f"Reason: {upgrade.reason}")

    with out.counterexamples():
        out.line(
            "gamma / AB diagnostic upgrades rejected",
            StatusMark.FAIL,
            "gamma, AB, B=1/A, areal kappa, residual hiding, and parent closure upgrades remain rejected",
        )


def case_5_failure_controls(out: ScriptOutput) -> None:
    header("Case 5: Failure controls")
    print("The gamma / AB recovery diagnostic audit fails if a later script allows:")
    print()
    print("1. gamma_s chosen from desired PPN/gamma_like recovery")
    print("2. beta_AB chosen to enforce AB=1")
    print("3. AB=1 used as parent insertion law")
    print("4. B=1/A used as general construction rule")
    print("5. kappa_areal promoted to physical scalar")
    print("6. recovery success hides residual double-count load")
    print("7. support/smoothing/boundary data selected from gamma/AB diagnostics")
    print("8. parent equation opened from reduced recovery diagnostics")

    with out.governance_assessments():
        out.line(
            "gamma / AB diagnostic failure controls stated",
            StatusMark.OBLIGATION,
            "future scripts must not convert reduced recovery diagnostics into construction or parent closure",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Gamma / AB diagnostic result:")
    print()
    print("  gamma_like, AB, B=1/A, and kappa_areal are useful reduced diagnostics.")
    print("  They may classify a candidate after the candidate is structurally fixed.")
    print("  They may not choose F_zeta coefficients, seam data, residual status, or parent closure.")
    print("  Successful diagnostics do not derive metric insertion.")
    print("  Failed diagnostics may reject or flag a candidate, not tune it.")
    print()
    print("Possible next script:")
    print("  candidate_metric_insertion_boundary_support_compatibility.py")
    print()
    print("Tiny goblin label:")
    print("  The mirror may frown. It may not sculpt.")

    with out.governance_assessments():
        out.line(
            "gamma / AB recovery diagnostics audit complete",
            StatusMark.PASS,
            "reduced recovery diagnostics classified; metric insertion theorem remains open",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, diag: GammaABDiagnostic) -> None:
    ns.record_derivation(
        derivation_id="gamma_AB_recovery_diagnostic_24",
        inputs=[diag.A_weak, diag.B_candidate],
        output=sp.Tuple(diag.gamma_like, diag.AB_product, diag.kappa_areal),
        method="evaluate reduced weak-field gamma-like, AB, and kappa_areal diagnostics",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="gamma_AB_recovery_diagnostic",
        scope="Group 24 metric insertion recovery retest",
    )

    ns.record_derivation(
        derivation_id="gamma_AB_recovery_diagnostics_marker_24",
        inputs=[
            sp.Symbol("gamma_like"),
            sp.Symbol("AB_product"),
            sp.Symbol("B_inverse_A"),
            sp.Symbol("kappa_areal"),
            sp.Symbol("count_once_trace"),
        ],
        output=sp.Symbol("gamma_AB_recovery_diagnostics_stated"),
        method="Group 24 gamma / AB recovery diagnostics ledger",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="requirements_marker",
        scope="Group 24 metric insertion recovery retest",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g24_derive_gamma_coeff_origin", "Derive gamma-like coefficient origin before recovery"),
        ("g24_derive_AB_behavior_without_tuning", "Derive AB behavior without AB-product tuning"),
        ("g24_keep_B_inverse_A_diagnostic", "Keep B=1/A diagnostic unless derived generally"),
        ("g24_keep_kappa_areal_diagnostic", "Keep areal kappa diagnostic unless derived physically"),
        ("g24_preserve_count_once_during_recovery", "Preserve count-once trace discipline during recovery audit"),
        ("g24_keep_parent_closed_after_gamma_AB", "Keep parent gate closed after gamma/AB diagnostics"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g24_gamma_AB_diag_route"],
            description=(
                "Gamma-like and AB diagnostics may classify fixed candidates but may not choose coefficients, "
                "promote areal kappa, hide residual double-counting, or open parent closure."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g24_derive_gamma_coeff_origin",
        "g24_derive_AB_behavior_without_tuning",
        "g24_keep_B_inverse_A_diagnostic",
        "g24_keep_kappa_areal_diagnostic",
        "g24_preserve_count_once_during_recovery",
        "g24_keep_parent_closed_after_gamma_AB",
    ]

    ns.record_route(RouteRecord(
        route_id="g24_gamma_AB_diag_route",
        script_id=SCRIPT_ID,
        name="Group 24 gamma / AB recovery diagnostic route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "candidate insertion data are structurally fixed before diagnostics",
            "gamma/AB diagnostics do not choose coefficients",
            "B=1/A remains reduced exterior diagnostic unless derived",
            "areal kappa remains diagnostic unless derived",
            "count-once trace discipline is preserved",
            "parent equation remains closed",
        ],
    ))

    for branch_id in [
        "gamma_coefficient_from_recovery",
        "AB_product_parent_law",
        "B_inverse_A_construction",
        "areal_kappa_physical_scalar",
        "recovery_hides_double_count",
        "parent_from_gamma_AB_success",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}_24",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; gamma/AB diagnostics cannot construct metric insertion.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g24_gamma_AB_diagnostics_not_construction",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "gamma-like, AB, B=1/A, and areal-kappa diagnostics may classify fixed metric-insertion candidates. "
            "They may not choose coefficients, construct B_s/F_zeta, promote kappa, hide count-once failure, or open parent closure."
        ),
        derivation_ids=[
            "gamma_AB_recovery_diagnostic_24",
            "gamma_AB_recovery_diagnostics_marker_24",
        ],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Gamma AB Recovery Diagnostics")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    diagnostics = build_reduced_diagnostic_expressions()
    cases = build_cases()
    rules = build_rules()
    upgrades = build_rejected_upgrades()

    case_0_problem_statement(out)
    case_1_symbolic_diagnostics(diagnostics, out)
    case_2_diagnostic_cases(cases, out)
    case_3_rules(rules, out)
    case_4_rejected_upgrades(upgrades, out)
    case_5_failure_controls(out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns, diagnostics)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
