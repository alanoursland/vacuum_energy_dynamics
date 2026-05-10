# Candidate J_sub definition requirements
#
# Group:
#   18_vacuum_current_split
#
# Script type:
#   REQUIREMENTS
#
# Purpose
# -------
# The pure wind neutrality test found:
#
#   Pure wind neutrality is required but not derived.
#   J_sub can survive only as neutral substrate-current theorem target.
#
# Required:
#
#   no M_ext shift,
#   no scalar trace,
#   no ordinary matter coupling,
#   no boundary repair,
#   no preferred-frame force,
#   no recovery role.
#
# This script defines what J_sub must be after neutrality constraints.
#
# Locked-door question:
#
#   What must J_sub be to be more than preferred-frame wind?
#
# This is a requirements audit, not a substrate-current derivation.


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
    HandoffImportRecord,
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
class JSubRequirementEntry:
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
        dependency_id="pure_wind_neutrality_test_marker",
        upstream_script_id="18_vacuum_current_split__candidate_pure_wind_neutrality_test",
        upstream_derivation_id="pure_wind_neutrality_test_marker",
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


def build_entries() -> List[JSubRequirementEntry]:
    return [
        JSubRequirementEntry(
            name="JS1: J_sub definition target",
            requirement="J_sub has domain, frame/frame-free law, direction, measure, divergence status, boundary behavior, matter decoupling, and mass neutrality",
            role="core substrate-current theorem target",
            allowed_if="all requirements are explicit before J_sub is used",
            forbidden_if="J_sub is named as substrate current without structure",
            status="THEOREM_TARGET",
            missing="actual J_sub definition",
            consequence="decides whether substrate-current language can become technical",
        ),
        JSubRequirementEntry(
            name="JS2: domain requirement",
            requirement="ordinary-sector domain D_sub where J_sub is defined is specified",
            role="definition prerequisite",
            allowed_if="domain is structural and not selected after leakage/failure",
            forbidden_if="domain excludes problematic regions by cutoff",
            status="REQUIRED",
            missing="D_sub",
            consequence="prevents convenient-domain wind",
        ),
        JSubRequirementEntry(
            name="JS3: frame or frame-free definition requirement",
            requirement="J_sub has an ontology-derived frame, or is defined frame-free",
            role="preferred-frame guard",
            allowed_if="frame follows from vacuum ontology / substrate law",
            forbidden_if="wind direction is arbitrary preferred frame",
            status="REQUIRED",
            missing="vacuum frame or frame-free substrate law",
            consequence="prevents arbitrary-frame physics",
        ),
        JSubRequirementEntry(
            name="JS4: direction / orientation requirement",
            requirement="J_sub direction is defined by substrate law, topology, support, or frame-free structure",
            role="orientation prerequisite",
            allowed_if="direction is not chosen by boundary/recovery behavior",
            forbidden_if="direction is chosen to cancel mass/scalar/boundary leakage",
            status="REQUIRED",
            missing="direction law",
            consequence="prevents repair wind",
        ),
        JSubRequirementEntry(
            name="JS5: measure requirement",
            requirement="substrate amount/current measure is specified",
            role="substance/accounting prerequisite",
            allowed_if="measure is ontology-native and does not shift M_ext",
            forbidden_if="measure is chosen to make flux vanish or mass neutral after the fact",
            status="REQUIRED",
            missing="substrate density/measure",
            consequence="prevents fake neutral accounting",
        ),
        JSubRequirementEntry(
            name="JS6: divergence status requirement",
            requirement="divergence-free, zero-creation, or other divergence status is specified",
            role="substrate conservation guard",
            allowed_if="divergence status follows from substrate law",
            forbidden_if="nabla_mu J_sub^mu = 0 is imposed to hide exchange",
            status="REQUIRED",
            missing="substrate conservation/divergence theorem",
            consequence="separates pure substrate from active exchange",
        ),
        JSubRequirementEntry(
            name="JS7: boundary behavior requirement",
            requirement="J_sub has zero exterior flux, tangential flow, compact support, or other neutral boundary law",
            role="boundary neutrality guard",
            allowed_if="boundary behavior follows structurally",
            forbidden_if="boundary behavior is repair or recovery-tuned",
            status="REQUIRED",
            missing="boundary law",
            consequence="protects exterior sector",
        ),
        JSubRequirementEntry(
            name="JS8: matter decoupling requirement",
            requirement="J_sub does not enter ordinary T_mu_nu routing or produce fifth-force-like coupling",
            role="ordinary matter guard",
            allowed_if="ordinary matter remains routed through established sectors",
            forbidden_if="J_sub pushes matter or repairs matter coupling",
            status="REQUIRED",
            missing="ordinary matter decoupling theorem",
            consequence="prevents substrate wind from becoming matter mechanism",
        ),
        JSubRequirementEntry(
            name="JS9: mass neutrality requirement",
            requirement="delta M_ext|J_sub = 0",
            role="mass protection guard",
            allowed_if="J_sub is exterior-mass-neutral structurally",
            forbidden_if="J_sub changes measured exterior mass",
            status="REQUIRED",
            missing="mass neutrality theorem",
            consequence="protects strongest A-sector result",
        ),
        JSubRequirementEntry(
            name="JS10: scalar trace neutrality requirement",
            requirement="J_sub does not source B_s, zeta residual metric trace, kappa, or exterior scalar charge",
            role="metric-insertion guard",
            allowed_if="J_sub is decoupled from ordinary metric scalar trace",
            forbidden_if="J_sub reopens B_s/F_zeta, residual trace, or O",
            status="REQUIRED",
            missing="scalar trace neutrality theorem",
            consequence="preserves Group 16 guardrails",
        ),
        JSubRequirementEntry(
            name="JS11: relation to u_vac",
            requirement="J_sub may define or use u_vac only non-circularly",
            role="vacuum-frame guard",
            allowed_if="u_vac follows from real current/frame law",
            forbidden_if="J_sub = n_vac u_vac with u_vac undefined",
            status="DEFER",
            missing="u_vac definition",
            consequence="keeps vacuum frame unresolved honestly",
        ),
        JSubRequirementEntry(
            name="JS12: relation to J_V",
            requirement="J_sub relation to J_V is bookkeeping unless operator split criterion exists",
            role="umbrella-current guard",
            allowed_if="J_V = J_sub + J_exch is marked role-level only",
            forbidden_if="treated as operator identity now",
            status="SAFE_IF",
            missing="operator split criterion",
            consequence="preserves role-level status",
        ),
        JSubRequirementEntry(
            name="JS13: relation to J_exch",
            requirement="J_sub is not whatever remains after J_exch is removed",
            role="remainder-current rejection guard",
            allowed_if="split criterion distinguishes substrate from exchange",
            forbidden_if="residual bookkeeping becomes current definition",
            status="REQUIRED",
            missing="J_sub/J_exch split criterion",
            consequence="prevents fake substrate current",
        ),
        JSubRequirementEntry(
            name="JS14: relation to zeta / B_s",
            requirement="J_sub does not drive zeta/B_s insertion or residual metric trace",
            role="metric-sector guard",
            allowed_if="J_sub remains pure wind and scalar-trace neutral",
            forbidden_if="J_sub becomes hidden B_s/F_zeta source",
            status="REQUIRED",
            missing="no scalar trace theorem",
            consequence="keeps pure wind from re-entering metric insertion",
        ),
        JSubRequirementEntry(
            name="JS15: zero-net exchange compatibility",
            requirement="J_sub compatible with Sigma_V - R_V = 0 in ordinary sector",
            role="ordinary-sector neutral exchange candidate",
            allowed_if="substrate flow is redistribution/transport, not net creation",
            forbidden_if="J_sub claims active ordinary sourcing",
            status="CANDIDATE",
            missing="zero-net exchange theorem",
            consequence="keeps ordinary zero-net branch live",
        ),
        JSubRequirementEntry(
            name="JS16: zero-creation compatibility",
            requirement="J_sub compatible with Sigma_V = R_V = 0 in ordinary sector",
            role="strong ordinary-sector neutrality candidate",
            allowed_if="curvature changes are warping/constraint rather than creation/destruction",
            forbidden_if="J_sub is active creation/destruction source",
            status="CANDIDATE",
            missing="zero-creation theorem",
            consequence="keeps ordinary no-creation branch live",
        ),
        JSubRequirementEntry(
            name="JS17: arbitrary preferred-frame rejection",
            requirement="J_sub = arbitrary preferred-frame wind",
            role="forbidden definition",
            allowed_if="never without ontology-derived frame and neutrality",
            forbidden_if="accepted as substrate current",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents arbitrary frame current",
        ),
        JSubRequirementEntry(
            name="JS18: circular u_vac rejection",
            requirement="J_sub = n_vac u_vac with u_vac undefined",
            role="forbidden circular definition",
            allowed_if="never as definition",
            forbidden_if="accepted as substrate current",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents circular vacuum rest frame",
        ),
        JSubRequirementEntry(
            name="JS19: remainder-current rejection",
            requirement="J_sub = J_V - J_exch with no split criterion",
            role="forbidden bookkeeping-to-current branch",
            allowed_if="never as operator definition",
            forbidden_if="accepted as J_sub definition",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents leftover current from becoming ontology",
        ),
        JSubRequirementEntry(
            name="JS20: pure wind gravitating rejection",
            requirement="J_sub has gravitational effect merely because substrate flows",
            role="forbidden pure-wind effect",
            allowed_if="never under pure wind neutrality",
            forbidden_if="accepted as substrate current behavior",
            status="REJECTED",
            missing="not pursued",
            consequence="preserves pure wind neutrality",
        ),
        JSubRequirementEntry(
            name="JS21: dark-sector convenience rejection",
            requirement="J_sub becomes dark-sector current by convenience",
            role="forbidden speculative shortcut",
            allowed_if="dark branch remains deferred and separated",
            forbidden_if="used to patch ordinary-sector current failure",
            status="REJECTED",
            missing="not pursued",
            consequence="keeps dark sector optional/downstream",
        ),
        JSubRequirementEntry(
            name="JS22: J_sub failure",
            requirement="J_sub cannot meet neutrality, frame, domain, measure, and split requirements",
            role="branch failure condition",
            allowed_if="used to reject J_sub as current",
            forbidden_if="patched with preferred frame or remainder notation",
            status="BRANCH_KILLED",
            missing="applies if failure demonstrated",
            consequence="vacuum current split must proceed without substrate current",
        ),
        JSubRequirementEntry(
            name="JS23: recommended next move",
            requirement="after J_sub burden is stated, define J_exch requirements next",
            role="next local bottleneck",
            allowed_if="J_sub remains theorem target or constrained candidate",
            forbidden_if="assuming J_exch is easier before auditing it",
            status="RECOMMENDED",
            missing="J_exch definition requirements",
            consequence="next script should be candidate_J_exch_definition_requirements.py",
        ),
    ]


def print_entry(e: JSubRequirementEntry) -> None:
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
    header("Case 0: J_sub definition requirements problem")

    print("Question:")
    print()
    print("  What must J_sub be to be more than preferred-frame wind?")
    print()
    print("Goal:")
    print()
    print("  state minimum substrate-current burden after pure wind neutrality")
    print()
    print("Discipline:")
    print()
    print("  no arbitrary preferred frame")
    print("  no circular u_vac")
    print("  no remainder-current definition")
    print("  no pure-wind gravity by existence")
    print("  no dark-sector convenience")
    print("  no scalar trace")
    print("  no matter coupling")
    print("  no M_ext shift")
    print("  no boundary repair")

    status_line("J_sub definition requirements problem posed", "REQUIRED")


def case_1_inventory(entries: List[JSubRequirementEntry]):
    header("Case 1: J_sub definition requirements inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[JSubRequirementEntry]):
    header("Case 2: Compact J_sub requirements ledger")

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

    status_line("compact J_sub requirements ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[JSubRequirementEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  J_sub is not defined yet.")
    print("  A real J_sub requires domain, frame/frame-free law, direction, measure, divergence status, boundary behavior, matter decoupling, mass neutrality, and scalar-trace neutrality.")
    print("  u_vac remains deferred.")
    print("  J_V = J_sub + J_exch remains role-level only.")
    print("  Zero-net and zero-creation ordinary-sector branches remain live.")
    print("  Next gate is J_exch definition requirements.")

    status_line("J_sub requirements status count produced", "STRUCTURAL")


def case_4_required_fields():
    header("Case 4: Required J_sub fields")

    print("Required J_sub fields:")
    print()
    print("1. domain")
    print("2. frame or frame-free definition")
    print("3. direction / orientation")
    print("4. substrate measure")
    print("5. divergence status")
    print("6. boundary behavior")
    print("7. matter decoupling")
    print("8. mass neutrality")
    print("9. scalar trace neutrality")
    print("10. relation to u_vac")
    print("11. relation to J_V")
    print("12. relation to J_exch")
    print("13. relation to zeta / B_s")

    status_line("required J_sub fields listed", "RECOMMENDED")


def case_5_decision_tree():
    header("Case 5: J_sub definition decision tree")

    print("Decision tree:")
    print()
    print("1. J_sub has domain/frame/direction/measure and neutrality:")
    print("   substrate-current theorem target survives.")
    print()
    print("2. J_sub depends on undefined u_vac:")
    print("   defer until u_vac/frame law exists.")
    print()
    print("3. J_sub is arbitrary preferred-frame wind:")
    print("   rejected.")
    print()
    print("4. J_sub is leftover after J_exch:")
    print("   rejected unless split criterion exists.")
    print()
    print("5. J_sub gravitates by existence:")
    print("   rejected under pure wind neutrality.")
    print()
    print("6. J_sub cannot meet requirements:")
    print("   substrate-current branch killed or remains only metaphor/bookkeeping.")

    status_line("J_sub definition decision tree stated", "RECOMMENDED")


def case_6_good_failure():
    header("Case 6: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  J_sub cannot be defined without arbitrary frame, circular u_vac,")
    print("  remainder-current bookkeeping, mass shift, scalar trace, or matter coupling.")
    print()
    print("Consequence:")
    print()
    print("  do not use J_sub as current.")
    print("  keep pure substrate flow as unresolved ontology/bookkeeping only.")
    print()
    print("Bad failure:")
    print()
    print("  call J_sub substrate current because the theory wants pure wind.")

    status_line("J_sub definition good failure stated", "DEFER")


def case_7_failure_controls():
    header("Case 7: Failure controls")

    print("J_sub definition fails if:")
    print()
    print("1. domain is chosen after leakage/failure")
    print("2. frame is arbitrary")
    print("3. direction is boundary/recovery repair")
    print("4. measure is chosen to make flux neutral")
    print("5. divergence-free status hides exchange")
    print("6. boundary behavior repairs leakage")
    print("7. matter coupling appears")
    print("8. M_ext shifts")
    print("9. scalar trace appears")
    print("10. u_vac is circular")
    print("11. J_sub is role-level remainder")
    print("12. J_sub becomes dark-sector patch")

    status_line("J_sub definition failure controls stated", "RISK")


def case_8_next_tests():
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_J_sub_definition_requirements.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_J_exch_definition_requirements.py")
    print("   Define what J_exch must be to be more than repair current.")
    print()
    print("3. candidate_J_sub_failure_summary.py")
    print("   Use if J_sub cannot meet substrate-current requirements.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_J_exch_definition_requirements.py")
    print()
    print("Reason:")
    print("  J_sub has now been burdened as pure neutral substrate flow.")
    print("  The active branch J_exch must next be fenced against repair-current behavior.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("J_sub is not defined yet.")
    print()
    print("It survives only as a theorem target requiring:")
    print()
    print("  domain")
    print("  frame or frame-free law")
    print("  direction")
    print("  measure")
    print("  divergence status")
    print("  boundary behavior")
    print("  matter decoupling")
    print("  mass neutrality")
    print("  scalar trace neutrality")
    print()
    print("Rejected:")
    print()
    print("  arbitrary preferred-frame wind")
    print("  circular u_vac")
    print("  remainder-current definition")
    print("  pure wind gravitating by existence")
    print("  dark-sector convenience")
    print()
    print("Best next script:")
    print()
    print("  candidate_J_exch_definition_requirements.py")

    status_line("J_sub definition requirements audit complete", "CLOSED")


def main():
    header("Candidate J_sub Definition Requirements")
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
            obligation_id="define_J_sub_domain_in_18_J_sub_requirements",
            script_id=SCRIPT_ID,
            status=ObligationStatus.OPEN,
            statement="J_sub domain D_sub must be specified structurally before J_sub is used.",
        ))
        ns.record_obligation(ProofObligationRecord(
            obligation_id="define_J_sub_frame_or_frame_free_in_18_J_sub_requirements",
            script_id=SCRIPT_ID,
            status=ObligationStatus.OPEN,
            statement="J_sub must have an ontology-derived frame or be defined frame-free. Arbitrary preferred frame is forbidden.",
        ))
        ns.record_obligation(ProofObligationRecord(
            obligation_id="define_J_sub_measure_in_18_J_sub_requirements",
            script_id=SCRIPT_ID,
            status=ObligationStatus.OPEN,
            statement="Substrate amount/current measure must be specified; must not shift M_ext.",
        ))
        ns.record_obligation(ProofObligationRecord(
            obligation_id="define_J_sub_divergence_status_in_18_J_sub_requirements",
            script_id=SCRIPT_ID,
            status=ObligationStatus.OPEN,
            statement="Divergence-free, zero-creation, or other divergence status must be specified from substrate law, not imposed to hide exchange.",
        ))
        ns.record_obligation(ProofObligationRecord(
            obligation_id="define_J_sub_boundary_behavior_in_18_J_sub_requirements",
            script_id=SCRIPT_ID,
            status=ObligationStatus.OPEN,
            statement="J_sub boundary behavior (zero exterior flux, tangential flow, compact support) must follow structurally, not be repair or recovery-tuned.",
        ))
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id="reject_arbitrary_frame_J_sub_in_18_J_sub_requirements",
            script_id=SCRIPT_ID,
            branch_name="arbitrary_preferred_frame_J_sub",
            status=GovernanceStatus.REJECTED_ROUTE,
            rationale="J_sub = arbitrary preferred-frame wind is forbidden. Frame must follow from vacuum ontology.",
        ))
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id="reject_circular_u_vac_J_sub_in_18_J_sub_requirements",
            script_id=SCRIPT_ID,
            branch_name="circular_u_vac_J_sub",
            status=GovernanceStatus.REJECTED_ROUTE,
            rationale="J_sub = n_vac u_vac with u_vac undefined is a circular definition. Deferred until u_vac is resolved.",
        ))
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id="reject_remainder_current_J_sub_in_18_J_sub_requirements",
            script_id=SCRIPT_ID,
            branch_name="remainder_current_J_sub",
            status=GovernanceStatus.REJECTED_ROUTE,
            rationale="J_sub = J_V - J_exch with no split criterion is forbidden. Residual bookkeeping cannot become current definition.",
        ))
        ns.record_derivation(
            derivation_id="J_sub_definition_requirements_marker",
            inputs=[],
            output=sp.Symbol("J_sub_definition_requirements_complete"),
            method="J_sub_definition_requirements",
            status=Status.DERIVED,
        )
        ns.write_run_metadata()


if __name__ == "__main__":
    main()
