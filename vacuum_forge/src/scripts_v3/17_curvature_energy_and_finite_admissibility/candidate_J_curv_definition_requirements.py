# Candidate J_curv definition requirements
#
# Group:
#   17_curvature_energy_and_finite_admissibility
#
# Script type:
#   REQUIREMENTS
#
# Purpose
# -------
# The curvature energy density role audit found:
#
#   e_curv can survive only as diagnostic/accounting or finite-admissibility measure.
#   Source, bounce, regular-core, mass-shift, boundary-repair, and recovery-tuning roles are rejected.
#   e_curv may seed future H_curv only after divergence-safe source structure is known.
#   e_curv does not define J_curv by itself.
#
# This script defines the minimum requirements for J_curv to be more than a name.
#
# Locked-door question:
#
#   What must J_curv be to be more than a name?
#
# This is a requirements audit, not a curvature-current derivation.


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
    ProofObligationRecord,
    ObligationStatus,
    RecordKind,
    ScriptOutput,
)


ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def status_line(label: str, status: str, detail: str = "") -> ScriptOutput:
    marks = {
        "SAFE_IF": "WARN",
        "CANDIDATE": "WARN",
        "STRUCTURAL": "WARN",
        "CONSTRAINED": "WARN",
        "RECOMMENDED": "PASS",
        "REQUIRED": "WARN",
        "MISSING": "FAIL",
        "UNRESOLVED": "FAIL",
        "RISK": "WARN",
        "FORBIDDEN": "PASS",
        "REJECTED": "WARN",
        "DANGER": "FAIL",
        "THEOREM_TARGET": "WARN",
        "RECOVERY_TARGET": "WARN",
        "BRANCH_KILLED": "FAIL",
        "DEFER": "WARN",
        "CLOSED": "PASS",
    }
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")
    return ScriptOutput(label=label, status=mark, detail=detail or status)


@dataclass
class JCurvRequirementEntry:
    name: str
    requirement: str
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
        dependency_id="curvature_energy_density_role_marker",
        upstream_script_id="17_curvature_energy_and_finite_admissibility__candidate_curvature_energy_density_role",
        upstream_derivation_id="curvature_energy_density_role_marker",
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


def build_entries() -> List[JCurvRequirementEntry]:
    return [
        JCurvRequirementEntry(
            name="JC1: J_curv definition target",
            requirement="J_curv^mu has domain, orientation, measure, balance role, boundary behavior, and source separation",
            role="core curvature-current theorem target",
            allowed_if="all minimum requirements are stated before any balance law is proposed",
            forbidden_if="J_curv is named to carry whatever curvature admissibility needs",
            status="THEOREM_TARGET",
            missing="actual J_curv definition",
            consequence="decides whether curvature current language can become technical",
        ),
        JCurvRequirementEntry(
            name="JC2: domain requirement",
            requirement="domain D_curv where J_curv is defined is specified",
            role="definition prerequisite",
            allowed_if="domain is geometric/physical and not selected after failure",
            forbidden_if="domain excludes divergence or singularity by cutoff",
            status="REQUIRED",
            missing="D_curv",
            consequence="prevents current from existing only where convenient",
        ),
        JCurvRequirementEntry(
            name="JC3: orientation requirement",
            requirement="direction/orientation of J_curv is defined by transport/admissibility structure",
            role="direction prerequisite",
            allowed_if="orientation is derived or structurally assigned before solutions",
            forbidden_if="direction is chosen to cancel blowup, flux, or boundary leakage",
            status="REQUIRED",
            missing="orientation law",
            consequence="prevents repair-current behavior",
        ),
        JCurvRequirementEntry(
            name="JC4: measure requirement",
            requirement="physical measure for flux/integral is defined",
            role="integration / covariance prerequisite",
            allowed_if="measure is compatible with geometry and not cutoff repair",
            forbidden_if="measure chosen to make flux finite after the fact",
            status="REQUIRED",
            missing="measure and hypersurface/boundary convention",
            consequence="prevents fake finite flux",
        ),
        JCurvRequirementEntry(
            name="JC5: covariance status requirement",
            requirement="J_curv is classified as spacetime vector, hypersurface current, projected current, or diagnostic current",
            role="covariance honesty guard",
            allowed_if="covariance level is explicit and not overclaimed",
            forbidden_if="hypersurface diagnostic is advertised as covariant current",
            status="REQUIRED",
            missing="covariance/projection status",
            consequence="prevents fake covariant-enough claims",
        ),
        JCurvRequirementEntry(
            name="JC6: balance role requirement",
            requirement="possible divergence/balance role is stated but not imposed as definition",
            role="pre-balance guard",
            allowed_if="source/relaxation sides are identified before balance law",
            forbidden_if="nabla_mu J_curv^mu is written to define J_curv decoratively",
            status="REQUIRED",
            missing="source/balance sides",
            consequence="prevents decorative continuity law",
        ),
        JCurvRequirementEntry(
            name="JC7: finite-admissibility relation",
            requirement="J_curv connects to A_curv only through defined admissibility condition",
            role="admissibility link",
            allowed_if="current carries a specific finite-admissibility role",
            forbidden_if="J_curv is added because anti-singularity needs a current",
            status="REQUIRED",
            missing="relation to A_curv",
            consequence="keeps current tied to prior condition",
        ),
        JCurvRequirementEntry(
            name="JC8: relation to e_curv",
            requirement="e_curv does not define J_curv by itself",
            role="energy/current separation guard",
            allowed_if="J_curv has independent transport/orientation law",
            forbidden_if="J_curv is declared as grad(e_curv) or flux of e_curv without law",
            status="REQUIRED",
            missing="transport law if related to e_curv",
            consequence="prevents scalar diagnostic from becoming current by fiat",
        ),
        JCurvRequirementEntry(
            name="JC9: relation to zeta / volume",
            requirement="J_curv may couple to zeta/volume only if count-once and metric insertion issues stay closed",
            role="curvature-volume bridge guard",
            allowed_if="does not reopen B_s/F_zeta, residual trace, or O problems",
            forbidden_if="zeta becomes hidden scalar source through J_curv",
            status="RISK",
            missing="zeta-volume coupling and no-overlap theorem",
            consequence="keeps Group 16 bottlenecks from reappearing",
        ),
        JCurvRequirementEntry(
            name="JC10: boundary behavior requirement",
            requirement="J_curv has no boundary repair flux, hidden exterior charge, or mass-shift leakage",
            role="boundary safety guard",
            allowed_if="boundary behavior is structural and neutral",
            forbidden_if="J_curv cancels boundary leakage or hides singularity",
            status="REQUIRED",
            missing="boundary neutrality theorem",
            consequence="protects ordinary exterior sector",
        ),
        JCurvRequirementEntry(
            name="JC11: matter separation requirement",
            requirement="J_curv does not double-count T_mu_nu or modify ordinary matter coupling",
            role="source separation guard",
            allowed_if="matter source remains routed independently",
            forbidden_if="J_curv reroutes matter to fix finite admissibility",
            status="REQUIRED",
            missing="matter separation theorem",
            consequence="prevents matter repair behavior",
        ),
        JCurvRequirementEntry(
            name="JC12: no M_ext shift",
            requirement="J_curv does not shift M_ext independently of A-sector source law",
            role="mass neutrality guard",
            allowed_if="curvature current is exterior-neutral or diagnostic",
            forbidden_if="J_curv changes measured exterior mass",
            status="REQUIRED",
            missing="mass neutrality theorem",
            consequence="protects strongest reduced A-sector result",
        ),
        JCurvRequirementEntry(
            name="JC13: relation to future H_curv",
            requirement="J_curv may inform H_curv only after divergence-safe correction structure is audited",
            role="future parent-correction handoff",
            allowed_if="H_curv remains deferred",
            forbidden_if="H_curv is introduced because J_curv is named",
            status="DEFER",
            missing="H_curv divergence-safe audit",
            consequence="prevents premature parent correction tensor",
        ),
        JCurvRequirementEntry(
            name="JC14: repair-current rejection",
            requirement="J_curv = whatever cancels divergence, singularity, or boundary leakage",
            role="forbidden current definition",
            allowed_if="never as mechanism",
            forbidden_if="accepted as curvature current",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents painted anti-singularity current",
        ),
        JCurvRequirementEntry(
            name="JC15: gradient-by-fiat rejection",
            requirement="J_curv^mu = grad^mu I_curv or grad^mu e_curv without transport law",
            role="forbidden scalar-to-current shortcut",
            allowed_if="only as candidate if transport/orientation law is later derived",
            forbidden_if="accepted as current definition now",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents scalar diagnostic from being renamed current",
        ),
        JCurvRequirementEntry(
            name="JC16: source-reservoir rejection",
            requirement="J_curv carries free positive/negative curvature energy to force finite behavior",
            role="forbidden reservoir current",
            allowed_if="never as mechanism",
            forbidden_if="accepted as anti-singularity current",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents curvature-current bounce money",
        ),
        JCurvRequirementEntry(
            name="JC17: current overclaim guard",
            requirement="J_curv candidate does not license bounce, regular core, or dynamical avoidance without equations",
            role="anti-overclaim guard",
            allowed_if="claim remains diagnostic/branch-filter until dynamics are derived",
            forbidden_if="strong anti-singularity claim made from current name alone",
            status="REQUIRED",
            missing="claim audit",
            consequence="keeps anti-singularity claims honest",
        ),
        JCurvRequirementEntry(
            name="JC18: J_curv failure",
            requirement="J_curv cannot meet domain/orientation/measure/boundary/source-separation requirements",
            role="branch failure condition",
            allowed_if="used to demote J_curv to deferred/nonexistent",
            forbidden_if="patched with decorative continuity language",
            status="BRANCH_KILLED",
            missing="applies if failure demonstrated",
            consequence="curvature admissibility remains diagnostic/branch-filter only",
        ),
        JCurvRequirementEntry(
            name="JC19: recommended next move",
            requirement="after requirements are stated, test whether a curvature balance law can be non-decorative",
            role="next local bottleneck",
            allowed_if="J_curv remains theorem target but requirements are clear",
            forbidden_if="jumping to H_curv before balance law audit",
            status="RECOMMENDED",
            missing="curvature balance law audit",
            consequence="next script should be candidate_curvature_balance_law.py",
        ),
    ]


def print_entry(e: JCurvRequirementEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Requirement: {e.requirement}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: J_curv definition requirements problem")

    print("Question:")
    print()
    print("  What must J_curv be to be more than a name?")
    print()
    print("Goal:")
    print()
    print("  define minimum requirements before proposing a curvature balance law")
    print()
    print("Discipline:")
    print()
    print("  no J_curv by renaming e_curv")
    print("  no gradient-by-fiat")
    print("  no repair current")
    print("  no source reservoir")
    print("  no boundary repair")
    print("  no M_ext shift")
    print("  no ordinary matter rerouting")
    print("  no H_curv yet")
    print("  no bounce/regular-core claim yet")

    status_line("J_curv definition requirements problem posed", "REQUIRED")


def case_1_inventory(entries: List[JCurvRequirementEntry]):
    header("Case 1: J_curv definition requirements inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[JCurvRequirementEntry]):
    header("Case 2: Compact J_curv requirements ledger")

    print("| Entry | Requirement | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.requirement.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    status_line("compact J_curv requirements ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[JCurvRequirementEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  J_curv is not defined yet.")
    print("  A real J_curv requires domain, orientation, measure, covariance status, admissibility role, boundary behavior, matter separation, and mass neutrality.")
    print("  e_curv does not define J_curv.")
    print("  zeta/volume coupling remains risky until no-overlap and insertion issues are solved.")
    print("  H_curv remains deferred.")
    print("  Next gate is whether a curvature balance law can be non-decorative.")

    status_line("J_curv requirements status count produced", "STRUCTURAL")


def case_4_required_fields():
    header("Case 4: Required J_curv fields")

    print("Required fields:")
    print()
    print("1. domain")
    print("2. orientation / direction law")
    print("3. measure")
    print("4. covariance status")
    print("5. admissibility relation")
    print("6. balance/source role")
    print("7. relation to e_curv")
    print("8. relation to zeta / volume")
    print("9. boundary behavior")
    print("10. matter separation")
    print("11. mass neutrality")
    print("12. future H_curv handoff")

    status_line("required J_curv fields listed", "RECOMMENDED")


def case_5_decision_tree():
    header("Case 5: J_curv requirements decision tree")

    print("Decision tree:")
    print()
    print("1. J_curv has domain/direction/measure:")
    print("   candidate can proceed to balance-law audit.")
    print()
    print("2. J_curv is only gradient of scalar:")
    print("   rejected unless transport law appears.")
    print()
    print("3. J_curv is boundary repair:")
    print("   rejected.")
    print()
    print("4. J_curv is curvature energy flux by name:")
    print("   rejected unless independent law exists.")
    print()
    print("5. J_curv modifies matter or M_ext:")
    print("   rejected unless source theorem exists.")
    print()
    print("6. J_curv cannot meet requirements:")
    print("   curvature admissibility remains diagnostic/branch-filter only.")

    status_line("J_curv requirements decision tree stated", "RECOMMENDED")


def case_6_good_failure():
    header("Case 6: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  J_curv cannot be defined without repair, gradient-by-fiat,")
    print("  boundary leakage, mass shift, or source-reservoir behavior.")
    print()
    print("Consequence:")
    print()
    print("  do not use J_curv.")
    print("  keep curvature admissibility diagnostic / branch-filter only.")
    print()
    print("Bad failure:")
    print()
    print("  call a scalar gradient or repair flux J_curv and proceed to balance equations.")

    status_line("J_curv definition good failure stated", "DEFER")


def case_7_failure_controls():
    header("Case 7: Failure controls")

    print("J_curv definition fails if:")
    print()
    print("1. domain is selected after failure")
    print("2. direction cancels blowup or leakage")
    print("3. measure hides divergence")
    print("4. covariance status is overclaimed")
    print("5. balance law defines current decoratively")
    print("6. e_curv is renamed as current")
    print("7. zeta coupling reopens metric insertion/no-overlap problem")
    print("8. boundary repair appears")
    print("9. ordinary matter coupling is rerouted")
    print("10. M_ext shifts independently of A")
    print("11. H_curv is introduced early")
    print("12. bounce or regular core is claimed")

    status_line("J_curv definition failure controls stated", "RISK")


def case_8_next_tests():
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_J_curv_definition_requirements.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_curvature_balance_law.py")
    print("   Test whether curvature admissibility can be expressed as a non-decorative balance law.")
    print()
    print("3. candidate_curvature_admissibility_current_failure_summary.py")
    print("   Use if J_curv cannot meet requirements.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_curvature_balance_law.py")
    print()
    print("Reason:")
    print("  With J_curv requirements stated, the next question is whether any balance law")
    print("  can be written without becoming decorative continuity language.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("J_curv is not defined yet.")
    print()
    print("Minimum requirements:")
    print()
    print("  domain")
    print("  orientation")
    print("  measure")
    print("  covariance status")
    print("  admissibility relation")
    print("  balance role")
    print("  boundary behavior")
    print("  matter separation")
    print("  mass neutrality")
    print()
    print("Rejected:")
    print()
    print("  repair current")
    print("  gradient-by-fiat")
    print("  source-reservoir current")
    print("  J_curv by renaming e_curv")
    print()
    print("Best next script:")
    print()
    print("  candidate_curvature_balance_law.py")

    status_line("J_curv definition requirements audit complete", "CLOSED")


def main():
    header("Candidate J_curv Definition Requirements")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_required_fields()
    case_5_decision_tree()
    case_6_good_failure()
    case_7_failure_controls()
    case_8_next_tests()
    final_interpretation()

    with archive:
        ns.record_obligation(ProofObligationRecord(
            obligation_id="define_J_curv_domain_in_17_J_curv_requirements",
            script_id=SCRIPT_ID,
            title="Define J_curv domain D_curv",
            status=ObligationStatus.OPEN,
            description="D_curv must be geometric/physical and not selected after failure to exclude singularity.",
        ))
        ns.record_obligation(ProofObligationRecord(
            obligation_id="define_J_curv_orientation_in_17_J_curv_requirements",
            script_id=SCRIPT_ID,
            title="Define J_curv orientation law",
            status=ObligationStatus.OPEN,
            description="Direction/orientation of J_curv must follow from transport/admissibility structure, not be chosen to cancel blowup or leakage.",
        ))
        ns.record_obligation(ProofObligationRecord(
            obligation_id="define_J_curv_measure_in_17_J_curv_requirements",
            script_id=SCRIPT_ID,
            title="Define J_curv physical measure",
            status=ObligationStatus.OPEN,
            description="Physical measure for flux/integral must be structurally compatible with geometry, not chosen to make flux finite after the fact.",
        ))
        ns.record_obligation(ProofObligationRecord(
            obligation_id="prove_J_curv_boundary_neutrality_in_17_J_curv_requirements",
            script_id=SCRIPT_ID,
            title="Prove J_curv boundary neutrality",
            status=ObligationStatus.OPEN,
            description="J_curv must have no boundary repair flux, hidden exterior charge, or mass-shift leakage.",
        ))
        ns.record_obligation(ProofObligationRecord(
            obligation_id="prove_J_curv_matter_separation_in_17_J_curv_requirements",
            script_id=SCRIPT_ID,
            title="Prove J_curv matter separation",
            status=ObligationStatus.OPEN,
            description="J_curv must not double-count T_mu_nu or modify ordinary matter coupling.",
        ))
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id="reject_J_curv_repair_current_in_17",
            script_id=SCRIPT_ID,
            branch_id="J_curv_repair_current",
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=[],
        ))
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id="reject_J_curv_gradient_by_fiat_in_17",
            script_id=SCRIPT_ID,
            branch_id="J_curv_gradient_by_fiat",
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=[],
        ))
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id="reject_J_curv_source_reservoir_in_17",
            script_id=SCRIPT_ID,
            branch_id="J_curv_source_reservoir",
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=[],
        ))
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id="defer_J_curv_H_curv_handoff_in_17",
            script_id=SCRIPT_ID,
            branch_id="J_curv_informs_H_curv",
            status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=[
                "define_J_curv_domain_in_17_J_curv_requirements",
                "define_J_curv_orientation_in_17_J_curv_requirements",
            ],
        ))
        ns.record_derivation(
            derivation_id="J_curv_definition_requirements_marker",
            inputs=[],
            output=sp.Symbol("J_curv_definition_requirements_complete"),
            method="J_curv_definition_requirements",
            status=Status.DERIVED,
        )
        ns.write_run_metadata()


if __name__ == "__main__":
    main()
