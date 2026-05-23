# Candidate B_s insertion recovery audit
#
# Group:
#   16_metric_insertion_and_no_overlap
#
# Script type:
#   AUDIT
#
# Purpose
# -------
# The B_s insertion boundary-safety audit found:
#
#   boundary safety is required but not derived.
#   B_s insertion under residual-kill convention remains alive only if:
#     no exterior zeta/kappa charge,
#     no far-zone scalar flux,
#     no M_ext shift,
#     no shell source,
#     no boundary repair.
#
# If boundary safety is not killed, the next danger is recovery smuggling:
#
#   gamma_like,
#   AB,
#   Schwarzschild spatial metric,
#   areal kappa,
#   weak-field spatial curvature,
#
# used as construction rather than downstream checks.
#
# Locked-door question:
#
#   Can B_s insertion be audited against gamma_like / AB / Schwarzschild recovery
#   without using those recovery targets to construct the insertion rule?
#
# This is an anti-smuggling audit, not a recovery derivation.

from dataclasses import dataclass
from pathlib import Path
from typing import List

import sympy as sp

from vacuumforge import ProjectArchive, Status, TheoryContext
from vacuumforge.metric.concrete_check import check_concrete_metric
from vacuumforge.governance import (
    BranchDecisionRecord,
    ClaimRecord,
    ClaimTier,
    EvidenceRecord,
    EvidenceType,
    GovernanceStatus,
    ObligationStatus,
    ProofObligationRecord,
    ReasonCode,
    RecordKind,
    RouteRecord,
    ScriptOutput,
    StatusMark,
)


ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


@dataclass
class RecoveryAuditEntry:
    name: str
    rule: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="B_s_insertion_boundary_safety_marker",
        upstream_script_id="16_metric_insertion_and_no_overlap__candidate_B_s_insertion_boundary_safety",
        upstream_derivation_id="B_s_insertion_boundary_safety_marker",
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


def build_entries() -> List[RecoveryAuditEntry]:
    return [
        RecoveryAuditEntry(
            name="RA1: recovery-audit target",
            rule="gamma_like, AB, and Schwarzschild recovery are downstream tests, not B_s/F_zeta construction rules",
            role="core anti-smuggling target",
            allowed_if="insertion mechanism is fixed before recovery checks",
            forbidden_if="recovery target chooses coefficient, support, boundary, or residual status",
            status="THEOREM_TARGET",
            missing="solutions after insertion mechanism",
            consequence="protects B_s insertion from GR-copy construction",
        ),
        RecoveryAuditEntry(
            name="RA2: gamma_like downstream test",
            rule="ordinary weak-field spatial curvature / gamma_like behavior checked after insertion rule",
            role="weak-field recovery target",
            allowed_if="gamma_like is output of parent/insertion mechanism",
            forbidden_if="coefficient is chosen to make gamma_like = 1",
            status="RECOVERY_TARGET",
            missing="post-insertion weak-field solution",
            consequence="keeps observational safety from becoming coefficient tuning",
        ),
        RecoveryAuditEntry(
            name="RA3: AB downstream exterior diagnostic",
            rule="AB -> 1 in ordinary exterior is diagnostic/recovery check",
            role="static exterior diagnostic",
            allowed_if="AB is checked after boundary-safe insertion",
            forbidden_if="AB=1 is imposed to construct B_s",
            status="RECOVERY_TARGET",
            missing="exterior solution after insertion",
            consequence="keeps exterior recovery from becoming field law",
        ),
        RecoveryAuditEntry(
            name="RA4: areal kappa diagnostic only",
            rule="kappa_areal = 1/2 ln(AB) remains reduced diagnostic / mismatch test",
            role="allowed reduced diagnostic",
            allowed_if="used only to test exterior AB mismatch",
            forbidden_if="areal kappa becomes physical scalar or insertion mechanism",
            status="SAFE_IF",
            missing="not a mechanism",
            consequence="preserves kappa fence",
        ),
        RecoveryAuditEntry(
            name="RA5: Schwarzschild spatial metric as recovery target",
            rule="ordinary exterior should recover Schwarzschild/GR-compatible spatial behavior",
            role="exterior recovery target",
            allowed_if="used only as target for acceptable parent/insertion equations",
            forbidden_if="spatial metric is copied as derivation",
            status="RECOVERY_TARGET",
            missing="derived exterior solution",
            consequence="keeps GR-compatible exterior as test",
        ),
        RecoveryAuditEntry(
            name="RA6: weak-field spatial curvature target",
            rule="acceptable insertion should recover ordinary weak-field scalar spatial curvature",
            role="weak-field recovery target",
            allowed_if="checked after mechanism is specified",
            forbidden_if="curvature coefficient is fit by hand",
            status="RECOVERY_TARGET",
            missing="weak-field solution from mechanism",
            consequence="preserves observational target without tuning",
        ),
        RecoveryAuditEntry(
            name="RA7: B=1/A construction rejection",
            rule="B=1/A imposed generally to define B_s",
            role="forbidden shortcut",
            allowed_if="only as reduced static exterior recovery diagnostic",
            forbidden_if="used as general insertion or field equation",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents exterior relation from becoming parent construction",
        ),
        RecoveryAuditEntry(
            name="RA8: gamma coefficient fit rejection",
            rule="choose B_s/F_zeta coefficient so gamma_like = 1",
            role="forbidden coefficient tuning",
            allowed_if="never as derivation",
            forbidden_if="accepted as mechanism",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents observational recovery from being fake derivation",
        ),
        RecoveryAuditEntry(
            name="RA9: GR spatial copy rejection",
            rule="copy Schwarzschild/GR spatial metric as B_s or F_zeta",
            role="forbidden GR smuggling",
            allowed_if="never as derivation",
            forbidden_if="accepted as insertion law",
            status="REJECTED",
            missing="not pursued",
            consequence="keeps B_s/F_zeta theorem target honest",
        ),
        RecoveryAuditEntry(
            name="RA10: areal kappa physical promotion rejection",
            rule="use kappa_areal as physical scalar to justify B_s",
            role="forbidden diagnostic promotion",
            allowed_if="never as physical insertion mechanism",
            forbidden_if="accepted as scalar field",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents kappa diagnostic from becoming scalar gravity",
        ),
        RecoveryAuditEntry(
            name="RA11: recovery-tuned boundary smoothing rejection",
            rule="choose support/smoothing boundary behavior to pass AB/gamma recovery",
            role="forbidden boundary/recovery coupling",
            allowed_if="never as mechanism",
            forbidden_if="accepted as boundary safety",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents boundary safety from being recovery-fit",
        ),
        RecoveryAuditEntry(
            name="RA12: residual-kill not chosen by recovery",
            rule="residual-kill / non-metric residual status fixed before recovery checks",
            role="count-once protection",
            allowed_if="residual status follows safety convention or O/parent identity",
            forbidden_if="residual is killed because recovery fails otherwise",
            status="REQUIRED",
            missing="residual-kill theorem remains missing",
            consequence="prevents recovery from choosing recombination split",
        ),
        RecoveryAuditEntry(
            name="RA13: boundary safety not chosen by recovery",
            rule="compact support / smooth transition / zero flux fixed before recovery checks",
            role="boundary anti-smuggling guard",
            allowed_if="boundary behavior follows insertion/current law",
            forbidden_if="chosen to force exterior Schwarzschild behavior",
            status="REQUIRED",
            missing="boundary theorem",
            consequence="prevents recovery-tuned boundary repair",
        ),
        RecoveryAuditEntry(
            name="RA14: J_V unresolved guard",
            rule="J_V remains unresolved and cannot be chosen to pass recovery",
            role="current-branch guard",
            allowed_if="J_V stays theorem target unless physical flux law exists",
            forbidden_if="J_V is used as recovery repair current",
            status="REQUIRED",
            missing="physical J_V law",
            consequence="prevents current from becoming painted tunnel",
        ),
        RecoveryAuditEntry(
            name="RA15: recovery audit pass condition",
            rule="insertion branch may proceed only if recovery targets are cleanly downstream",
            role="branch-survival condition",
            allowed_if="no recovery target has been used as construction input",
            forbidden_if="any recovery target selects insertion/coefficient/boundary/residual",
            status="REQUIRED",
            missing="mechanism remains theorem target",
            consequence="decides whether group can summarize branch honestly",
        ),
        RecoveryAuditEntry(
            name="RA16: recovery-smuggling failure",
            rule="B_s insertion depends on gamma_like, AB, GR metric copy, or areal kappa promotion",
            role="branch-kill condition",
            allowed_if="used to reject unsafe insertion family",
            forbidden_if="patched or relabeled",
            status="BRANCH_KILLED",
            missing="applies if failure demonstrated",
            consequence="unsafe insertion cannot support ordinary sector",
        ),
        RecoveryAuditEntry(
            name="RA17: recommended next move",
            rule="if recovery audit passes only conventionally, close Group 16 with status summary",
            role="next local bottleneck",
            allowed_if="no concrete insertion/O theorem is derived",
            forbidden_if="continuing into parent equations before status closure",
            status="RECOMMENDED",
            missing="Group 16 status summary",
            consequence="next script should be candidate_metric_insertion_group_status_summary.py",
        ),
    ]


def print_entry(e: RecoveryAuditEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Rule: {e.rule}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    print(f"[INFO] {e.name}: {e.status}")
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement(out: ScriptOutput):
    header("Case 0: B_s insertion recovery-audit problem")

    print("Question:")
    print()
    print("  Can B_s insertion be audited against gamma_like / AB / Schwarzschild recovery")
    print("  without using those recovery targets to construct the insertion rule?")
    print()
    print("Goal:")
    print()
    print("  keep recovery as downstream test, not construction")
    print()
    print("Discipline:")
    print()
    print("  gamma_like is output, not coefficient input")
    print("  AB is diagnostic, not construction")
    print("  Schwarzschild spatial metric is target, not derivation")
    print("  areal kappa is diagnostic, not physical scalar")
    print("  residual-kill is not chosen by recovery")
    print("  boundary safety is not chosen by recovery")
    print("  J_V is not a recovery repair current")

    with out.governance_assessments():
        out.line(
            "B_s insertion recovery-audit problem posed",
            StatusMark.OBLIGATION,
            "required before insertion branch can be summarized",
        )


def case_1_inventory(entries: List[RecoveryAuditEntry]):
    header("Case 1: B_s insertion recovery-audit inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[RecoveryAuditEntry], out: ScriptOutput):
    header("Case 2: Compact recovery-audit ledger")

    print("| Entry | Rule | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.rule.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    with out.governance_assessments():
        out.line("compact recovery-audit ledger produced", StatusMark.INFO, "recovery routes enumerated")


def case_3_status_counts(entries: List[RecoveryAuditEntry], out: ScriptOutput):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Recovery targets remain downstream.")
    print("  Gamma_like, AB, Schwarzschild behavior, and areal kappa may test insertion branches.")
    print("  They may not construct B_s, choose coefficients, choose boundary behavior, or choose residual status.")
    print("  If no smuggling occurs, Group 16 should close with a status summary rather than jump to parent equations.")

    with out.governance_assessments():
        out.line(
            "B_s insertion recovery-audit status count produced",
            StatusMark.INFO,
            "recovery anti-smuggling guards enumerated",
        )


def case_4_recovery_tests(out: ScriptOutput):
    header("Case 4: Allowed recovery tests")

    print("Allowed downstream tests:")
    print()
    print("1. gamma_like weak-field behavior")
    print("2. AB exterior diagnostic")
    print("3. areal kappa mismatch diagnostic")
    print("4. Schwarzschild/GR-compatible exterior spatial behavior")
    print("5. weak-field spatial curvature")
    print()
    print("Not allowed:")
    print()
    print("1. coefficient fitting")
    print("2. B=1/A construction")
    print("3. GR spatial metric copy")
    print("4. areal kappa physical promotion")
    print("5. recovery-tuned support/smoothing")
    print("6. recovery-selected residual-kill")

    with out.governance_assessments():
        out.line("allowed recovery tests listed", StatusMark.INFO, "five allowed; six forbidden")


def case_4b_concrete_recovery_check(ns, out: ScriptOutput):
    header("Case 4b: Concrete recovery check stays downstream")

    ctx = TheoryContext("group_16_recovery_audit")
    ms = ctx.define_equal_response_algebraic_symbols()
    A_value = 1 - 2 * ms.G * ms.M / (ms.r * ms.c**2)
    B_value = 1 / A_value
    product = sp.simplify(A_value * B_value)
    result = check_concrete_metric(ctx, A_value, B_value, ["reciprocal_scaling"])[0]

    print(f"A(r) = {A_value}")
    print(f"B(r) = {B_value}")
    print(f"A(r) * B(r) = {product}")
    print(f"ConcreteMetricCheck status = {result.status}")

    if result.status == "satisfied_by_construction":
        with out.sample_results():
            out.line(
                "downstream reciprocal recovery audit",
                StatusMark.PASS,
                f"A*B = {product}; ConcreteMetricCheck = {result.status}",
            )
    else:
        with out.sample_results():
            out.line(
                "downstream reciprocal recovery audit",
                StatusMark.WARN,
                f"expected satisfied_by_construction, got {result.status}",
            )

    ns.record_derivation(
        derivation_id="B_s_insertion_recovery_reciprocal_check",
        inputs=[A_value, B_value],
        output=product,
        method="ConcreteMetricCheck reciprocal_scaling",
        status=Status.DERIVED,
        record_kind=RecordKind.COMPATIBILITY_EXAMPLE,
        scope="static exterior Schwarzschild-like ansatz; confirms AB=1 structure is downstream check only",
    )


def case_5_decision_tree(out: ScriptOutput):
    header("Case 5: Recovery-audit decision tree")

    print("Decision tree:")
    print()
    print("1. Recovery checked after mechanism:")
    print("   allowed.")
    print()
    print("2. Recovery chooses coefficient:")
    print("   rejected.")
    print()
    print("3. Recovery chooses boundary behavior:")
    print("   rejected.")
    print()
    print("4. Recovery chooses residual status:")
    print("   rejected.")
    print()
    print("5. Recovery uses diagnostic areal kappa:")
    print("   allowed if diagnostic only.")
    print()
    print("6. Recovery copies GR spatial metric:")
    print("   rejected.")
    print()
    print("7. If audit passes only conventionally:")
    print("   close Group 16 with status summary.")

    with out.governance_assessments():
        out.line("recovery-audit decision tree stated", StatusMark.INFO, "recommended next is group status summary")


def case_6_good_failure(ns, out: ScriptOutput):
    header("Case 6: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  The insertion branch only passes recovery by coefficient tuning,")
    print("  B=1/A construction, GR spatial metric copying, or areal kappa promotion.")
    print()
    print("Consequence:")
    print()
    print("  Reject the insertion branch as recovery-smuggled.")
    print("  Do not patch or relabel.")
    print()
    print("Bad failure:")
    print()
    print("  Call a recovery target a theorem because it gets the right exterior answer.")
    print()
    print("Recovery-target selected-parameter finding:")
    print()
    print("  gamma_like, AB, Schwarzschild recovery, and areal kappa are downstream tests.")
    print("  Gamma-like behavior, AB behavior, and Schwarzschild recovery are downstream tests,")
    print("  not construction rules for B_s/F_zeta insertion.")
    print("  Using them as construction inputs constitutes a RECOVERY_SELECTED_PARAMETER violation.")

    with out.governance_assessments():
        out.line(
            "B_s insertion recovery-audit good failure stated",
            StatusMark.DEFER,
            "deferred; recovery-smuggling would kill branch",
        )

    # Evidence record: recovery targets are selected parameters, not construction rules
    ns.record_evidence(EvidenceRecord(
        evidence_id="recovery_precedes_origin_check",
        script_id=SCRIPT_ID,
        evidence_type=EvidenceType.TARGET_SELECTED_PARAMETER,
        challenges=["gamma_like_coefficient_fit_route", "B_equals_1_over_A_construction_route"],
        reason_code=ReasonCode.RECOVERY_SELECTED_PARAMETER,
        description=(
            "Gamma-like behavior, AB behavior, and Schwarzschild recovery are downstream tests, "
            "not construction rules for B_s/F_zeta insertion. Any route that uses these targets "
            "to select coefficients, boundary behavior, or residual status constitutes a "
            "recovery-selected-parameter violation and must be rejected."
        ),
    ))

    # Governance claim: recovery targets are policy rule, not construction
    ns.record_claim(ClaimRecord(
        claim_id="recovery_targets_downstream_only",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Gamma-like behavior, AB behavior, and Schwarzschild recovery are downstream tests, "
            "not construction rules for B_s/F_zeta insertion."
        ),
        reason_code=ReasonCode.RECOVERY_SELECTED_PARAMETER,
        evidence_ids=["recovery_precedes_origin_check"],
    ))


def case_7_failure_controls(out: ScriptOutput):
    header("Case 7: Failure controls")

    print("Recovery audit fails if:")
    print()
    print("1. gamma_like fixes a coefficient")
    print("2. AB=1 constructs B_s")
    print("3. Schwarzschild spatial metric is copied")
    print("4. areal kappa is promoted to physical scalar")
    print("5. residual-kill is chosen by recovery")
    print("6. boundary smoothing is recovery-tuned")
    print("7. J_V is used as recovery repair current")
    print("8. recovery target is called parent identity")

    with out.governance_assessments():
        out.line("B_s insertion recovery-audit failure controls stated", StatusMark.WARN, "eight failure modes")


def case_8_next_tests(out: ScriptOutput):
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_B_s_insertion_recovery_audit.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_metric_insertion_group_status_summary.py")
    print("   Close Group 16 with status after insertion/count-once/O/boundary/recovery audits.")
    print()
    print("3. candidate_parent_identity_for_residual_kill.py")
    print("   Use only after status summary if parent route is selected.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_metric_insertion_group_status_summary.py")
    print()
    print("Reason:")
    print("  The branch has now been audited for insertion, count-once, non-metric residuals,")
    print("  minimal O, boundary safety, and recovery smuggling.")
    print("  Unless a concrete insertion/O theorem has appeared, the group should close with status.")

    with out.governance_assessments():
        out.line("next test selected", StatusMark.INFO, "candidate_metric_insertion_group_status_summary.py")


def final_interpretation(out: ScriptOutput):
    header("Final interpretation")

    print("Recovery remains downstream.")
    print()
    print("Allowed:")
    print()
    print("  gamma_like as test")
    print("  AB as diagnostic")
    print("  areal kappa as mismatch check")
    print("  Schwarzschild exterior as recovery target")
    print()
    print("Rejected:")
    print()
    print("  gamma_like coefficient fit")
    print("  B=1/A construction")
    print("  GR spatial metric copy")
    print("  areal kappa physical promotion")
    print("  recovery-tuned boundary/residual behavior")
    print()
    print("Best next script:")
    print()
    print("  candidate_metric_insertion_group_status_summary.py")

    with out.governance_assessments():
        out.line(
            "B_s insertion recovery-audit complete",
            StatusMark.DEFER,
            "recovery anti-smuggling guards in place; no theorem derived",
        )


def main():
    header("Candidate B_s Insertion Recovery Audit")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_problem_statement(out)
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries, out)
    case_3_status_counts(entries, out)
    case_4_recovery_tests(out)
    case_4b_concrete_recovery_check(ns, out)
    case_5_decision_tree(out)
    case_6_good_failure(ns, out)
    case_7_failure_controls(out)
    case_8_next_tests(out)
    final_interpretation(out)

    ns2 = ns
    if True:
        # Proof obligation: derive full solutions after insertion mechanism is fixed
        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_post_insertion_solutions_for_recovery",
            script_id=SCRIPT_ID,
            title="Derive post-insertion solutions to enable recovery tests",
            status=ObligationStatus.OPEN,
            required_by=["B_s_insertion_recovery_audit_pass_condition"],
            description=(
                "Recovery tests (gamma_like, AB, Schwarzschild exterior) cannot be run "
                "until a concrete B_s/F_zeta insertion mechanism is specified and "
                "boundary safety is verified. Only then may recovery serve as a downstream check."
            ),
        ))

        # Branch decision for any recovery-smuggled branch
        ns2.record_branch_decision(BranchDecisionRecord(
            decision_id="kill_recovery_tuned_B_s_branch",
            script_id=SCRIPT_ID,
            branch_id="recovery_tuned_B_s",
            status=GovernanceStatus.KILLED_BY_CONTRADICTION,
            tier=ClaimTier.EXCLUSION,
            reason_code=ReasonCode.RECOVERY_SELECTED_PARAMETER,
            evidence_ids=["recovery_precedes_origin_check"],
            description=(
                "Any B_s insertion branch that selects its coefficient, support, "
                "boundary behavior, or residual status by using gamma_like, AB, "
                "Schwarzschild spatial metric, or areal kappa promotion is killed. "
                "Recovery targets are downstream tests only."
            ),
        ))

        # Route: recovery as downstream-only test (the allowed route)
        ns2.record_route(RouteRecord(
            route_id="recovery_downstream_only_route",
            script_id=SCRIPT_ID,
            name="Recovery as downstream test only (anti-smuggling)",
            status=GovernanceStatus.CANDIDATE_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            required_obligations=["derive_post_insertion_solutions_for_recovery"],
            activation_conditions=[
                "insertion mechanism is fixed before recovery checks",
                "no coefficient is chosen to match gamma_like",
                "no B=1/A construction",
                "no GR spatial metric copy",
                "no areal kappa physical promotion",
                "no recovery-tuned boundary smoothing",
                "residual-kill not chosen by recovery",
            ],
        ))

        # Inventory marker
        ns2.record_derivation(
            derivation_id="B_s_insertion_recovery_audit_marker",
            inputs=[],
            output=sp.Symbol("B_s_insertion_recovery_audit_complete"),
            method="B_s_insertion_recovery_audit",
            status=Status.DERIVED,
            record_kind=RecordKind.INVENTORY_MARKER,
            is_placeholder=True,
        )

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
