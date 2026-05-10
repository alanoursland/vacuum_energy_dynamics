# Candidate curvature energy density role
#
# Group:
#   17_curvature_energy_and_finite_admissibility
#
# Script type:
#   SIEVE
#
# Purpose
# -------
# The finite-admissibility condition audit found:
#
#   finite admissibility can currently be stated only as a theorem target / branch filter.
#
# Safest candidate forms:
#
#   bounded scalar diagnostic,
#   bounded invariant set,
#   integrable curvature measure.
#
# Still not licensed:
#
#   dynamical singularity avoidance,
#   bounce,
#   regular core,
#   curvature current,
#   curvature source energy.
#
# This script tests the next risk:
#
#   Can curvature energy be defined as diagnostic/accounting
#   without becoming a hidden source reservoir?
#
# It is not a source law and not a curvature-current derivation.


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
        "DERIVED_REDUCED": "PASS",
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
class CurvatureEnergyRoleEntry:
    name: str
    role_rule: str
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
        dependency_id="finite_admissibility_condition_marker",
        upstream_script_id="17_curvature_energy_and_finite_admissibility__candidate_finite_admissibility_condition",
        upstream_derivation_id="finite_admissibility_condition_marker",
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


def build_entries() -> List[CurvatureEnergyRoleEntry]:
    return [
        CurvatureEnergyRoleEntry(
            name="CE1: curvature energy role target",
            role_rule="e_curv is diagnostic/accounting only unless a recombination/source law is derived",
            role="core curvature-energy fence",
            allowed_if="e_curv has domain, measure, invariant content, and no source behavior",
            forbidden_if="e_curv is used as free source reservoir or repair energy",
            status="THEOREM_TARGET",
            missing="definition of e_curv and accounting rule",
            consequence="decides whether curvature energy language can be kept safe",
        ),
        CurvatureEnergyRoleEntry(
            name="CE2: e_curv diagnostic only",
            role_rule="e_curv flags curvature intensity / admissibility cost but does not source equations",
            role="safest curvature-energy role",
            allowed_if="diagnostic output is not inserted into metric/source equations",
            forbidden_if="diagnostic becomes hidden force/source",
            status="SAFE_IF",
            missing="diagnostic definition and invariant choice",
            consequence="allows curvature energy language without dynamics claim",
        ),
        CurvatureEnergyRoleEntry(
            name="CE3: e_curv finite-admissibility measure",
            role_rule="Integral_D e_curv dV_phys finite as branch-filter condition",
            role="finite-admissibility accounting candidate",
            allowed_if="domain/measure are fixed and e_curv is not a source",
            forbidden_if="finite bound is used as bounce energy or cutoff repair",
            status="CANDIDATE",
            missing="e_curv functional, D, dV_phys, threshold",
            consequence="supports diagnostic/branch-filter anti-singularity language only",
        ),
        CurvatureEnergyRoleEntry(
            name="CE4: e_curv configuration accounting",
            role_rule="e_curv records curvature configuration cost without independent exterior mass contribution",
            role="accounting candidate",
            allowed_if="does not shift M_ext and does not double-count matter/vacuum energy",
            forbidden_if="configuration accounting becomes source reservoir",
            status="CANDIDATE",
            missing="accounting ledger and recombination rule",
            consequence="could support finite-admissibility bookkeeping if fenced",
        ),
        CurvatureEnergyRoleEntry(
            name="CE5: e_curv as H_curv seed",
            role_rule="e_curv may seed future H_curv only after divergence-safe source structure is defined",
            role="future parent-correction handoff",
            allowed_if="deferred until H_curv audit and source/divergence safety exist",
            forbidden_if="H_curv introduced now to make e_curv source-like",
            status="DEFER",
            missing="H_curv divergence-safe source structure",
            consequence="prevents premature parent correction tensor",
        ),
        CurvatureEnergyRoleEntry(
            name="CE6: e_curv source term deferred",
            role_rule="e_curv does not enter field equations as source in current group",
            role="source-role quarantine",
            allowed_if="source role waits for recombination/source law",
            forbidden_if="e_curv is inserted into A, B_s, H_curv, or J_curv equations now",
            status="REQUIRED",
            missing="source/recombination theorem",
            consequence="blocks curvature energy from becoming repair mechanism",
        ),
        CurvatureEnergyRoleEntry(
            name="CE7: no M_ext shift",
            role_rule="delta M_ext|e_curv = 0 unless derived through A-sector source law",
            role="mass neutrality guard",
            allowed_if="curvature energy remains diagnostic/accounting",
            forbidden_if="e_curv changes measured exterior mass independently",
            status="REQUIRED",
            missing="mass neutrality theorem",
            consequence="protects strongest reduced A-sector result",
        ),
        CurvatureEnergyRoleEntry(
            name="CE8: no ordinary matter double-count",
            role_rule="e_curv does not double-count T_mu_nu or reroute ordinary matter coupling",
            role="source separation guard",
            allowed_if="ordinary matter remains in its own source channel",
            forbidden_if="curvature energy modifies ordinary matter coupling",
            status="REQUIRED",
            missing="matter/source separation theorem",
            consequence="prevents matter-sector repair behavior",
        ),
        CurvatureEnergyRoleEntry(
            name="CE9: no boundary repair energy",
            role_rule="e_curv cannot hide blowup, leakage, or mass shift in boundary contribution",
            role="boundary safety guard",
            allowed_if="boundary energy is diagnostic or structurally neutral",
            forbidden_if="boundary term cancels singularity or exterior leakage",
            status="REQUIRED",
            missing="boundary neutrality theorem",
            consequence="prevents curvature energy from patching boundary failure",
        ),
        CurvatureEnergyRoleEntry(
            name="CE10: no recovery tuning",
            role_rule="e_curv cannot tune gamma_like, AB, boundary smoothing, or B_s/F_zeta behavior",
            role="anti-smuggling guard",
            allowed_if="recovery remains downstream",
            forbidden_if="curvature energy chosen to pass recovery target",
            status="REQUIRED",
            missing="not a mechanism",
            consequence="prevents curvature energy from becoming coefficient knob",
        ),
        CurvatureEnergyRoleEntry(
            name="CE11: source-reservoir rejection",
            role_rule="e_curv inserted as free positive/negative source to force finite behavior",
            role="forbidden reservoir branch",
            allowed_if="never in current status",
            forbidden_if="used to tune bounce, mass, boundary, or recovery",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents repair-money behavior",
        ),
        CurvatureEnergyRoleEntry(
            name="CE12: bounce-energy rejection",
            role_rule="e_curv becomes repulsive/negative/positive energy chosen to produce bounce",
            role="forbidden anti-singularity shortcut",
            allowed_if="never without derived dynamics",
            forbidden_if="bounce claimed from e_curv diagnostic/accounting alone",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents dynamical overclaim",
        ),
        CurvatureEnergyRoleEntry(
            name="CE13: regular-core tuning rejection",
            role_rule="e_curv coefficient or cutoff chosen to make regular core finite",
            role="forbidden solution-after-the-fact tuning",
            allowed_if="never as mechanism",
            forbidden_if="chosen after target solution",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents regular core by diagnostic cherry-pick",
        ),
        CurvatureEnergyRoleEntry(
            name="CE14: relation to zeta / volume",
            role_rule="e_curv may couple to volume response only if count-once and metric insertion issues remain closed",
            role="curvature-volume bridge risk",
            allowed_if="does not reopen B_s insertion, residual trace, or O problems",
            forbidden_if="zeta becomes hidden scalar source or metric trace again",
            status="RISK",
            missing="zeta coupling rule and no-overlap theorem",
            consequence="promising but dangerous until Group 16 bottlenecks are solved",
        ),
        CurvatureEnergyRoleEntry(
            name="CE15: relation to J_curv",
            role_rule="e_curv does not define J_curv by itself",
            role="current-definition guard",
            allowed_if="J_curv waits for domain, orientation, balance, and boundary law",
            forbidden_if="J_curv is declared as gradient/flux of e_curv without transport law",
            status="REQUIRED",
            missing="J_curv definition requirements",
            consequence="prevents scalar diagnostic from being renamed current",
        ),
        CurvatureEnergyRoleEntry(
            name="CE16: admissibility claim level",
            role_rule="e_curv diagnostic licenses diagnostic/branch-filter claim only",
            role="anti-overclaim guard",
            allowed_if="claim strength matches diagnostic/accounting role",
            forbidden_if="dynamical avoidance, bounce, or regular core claimed from e_curv alone",
            status="REQUIRED",
            missing="claim audit",
            consequence="keeps anti-singularity claims honest",
        ),
        CurvatureEnergyRoleEntry(
            name="CE17: curvature energy failure",
            role_rule="e_curv cannot be fenced from source-reservoir, mass-shift, or repair behavior",
            role="branch failure condition",
            allowed_if="used to demote e_curv to forbidden/local diagnostic only",
            forbidden_if="patched with labels",
            status="BRANCH_KILLED",
            missing="applies if failure demonstrated",
            consequence="curvature energy cannot be used in future current/correction work",
        ),
        CurvatureEnergyRoleEntry(
            name="CE18: recommended next move",
            role_rule="after e_curv is fenced, define J_curv requirements before any current is proposed",
            role="next local bottleneck",
            allowed_if="e_curv remains diagnostic/accounting only",
            forbidden_if="jumping to curvature balance law before J_curv requirements",
            status="RECOMMENDED",
            missing="J_curv definition requirements",
            consequence="next script should be candidate_J_curv_definition_requirements.py",
        ),
    ]


def print_entry(e: CurvatureEnergyRoleEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Role rule: {e.role_rule}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: Curvature energy density role problem")

    print("Question:")
    print()
    print("  Can curvature energy be defined as diagnostic/accounting")
    print("  without becoming a hidden source reservoir?")
    print()
    print("Goal:")
    print()
    print("  fence e_curv before any source, current, or correction-tensor role")
    print()
    print("Discipline:")
    print()
    print("  diagnostic/accounting only")
    print("  no field-equation source role")
    print("  no M_ext shift")
    print("  no ordinary matter double-count")
    print("  no boundary repair")
    print("  no recovery tuning")
    print("  no bounce or regular-core claim")
    print("  no J_curv by renaming e_curv")

    status_line("curvature energy density role problem posed", "REQUIRED")


def case_1_inventory(entries: List[CurvatureEnergyRoleEntry]):
    header("Case 1: Curvature energy density role inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[CurvatureEnergyRoleEntry]):
    header("Case 2: Compact curvature energy role ledger")

    print("| Entry | Role rule | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.role_rule.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    status_line("compact curvature energy role ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[CurvatureEnergyRoleEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  e_curv can survive only as diagnostic/accounting or finite-admissibility measure.")
    print("  Source, bounce, regular-core, mass-shift, boundary-repair, and recovery-tuning roles are rejected.")
    print("  e_curv may seed future H_curv only after divergence-safe source structure is known.")
    print("  e_curv does not define J_curv by itself.")
    print("  Next gate is J_curv definition requirements.")

    status_line("curvature energy role status count produced", "STRUCTURAL")


def case_4_allowed_roles():
    header("Case 4: Allowed e_curv roles")

    print("Allowed e_curv roles if fenced:")
    print()
    print("1. diagnostic curvature intensity")
    print("2. finite-admissibility measure")
    print("3. configuration accounting")
    print("4. deferred H_curv seed")
    print()
    print("Not allowed:")
    print()
    print("1. source term")
    print("2. bounce energy")
    print("3. regular-core tuning coefficient")
    print("4. M_ext shift")
    print("5. boundary repair")
    print("6. recovery tuning")
    print("7. J_curv definition by fiat")

    status_line("allowed e_curv roles listed", "RECOMMENDED")


def case_4b_sample_diagnostic_density(ns):
    header("Case 4b: Sample diagnostic curvature density")

    I_curv = sp.symbols("I_curv", real=True)
    e_curv = sp.simplify(I_curv**2)

    print(f"Sample diagnostic choice: e_curv = {e_curv}")
    print("For real I_curv, e_curv is manifestly nonnegative.")

    status_line(
        "sample diagnostic e_curv density",
        "DERIVED_REDUCED",
        f"e_curv = {e_curv} >= 0 for real I_curv",
    )

    ns.record_derivation(
        derivation_id="curvature_energy_sample_nonnegative_density",
        inputs=[I_curv],
        output=e_curv,
        method="symbolic sample diagnostic density",
        status=Status.DERIVED,
    )


def case_5_decision_tree():
    header("Case 5: Curvature energy decision tree")

    print("Decision tree:")
    print()
    print("1. e_curv diagnostic:")
    print("   safest.")
    print()
    print("2. e_curv finite-admissibility measure:")
    print("   candidate if domain/measure are fixed.")
    print()
    print("3. e_curv configuration accounting:")
    print("   candidate if no M_ext shift or matter double-count.")
    print()
    print("4. e_curv as source:")
    print("   deferred until recombination/source law exists.")
    print()
    print("5. e_curv as bounce / regular core mechanism:")
    print("   rejected.")
    print()
    print("6. e_curv to J_curv:")
    print("   requires separate current-definition requirements.")

    status_line("curvature energy decision tree stated", "RECOMMENDED")


def case_6_good_failure():
    header("Case 6: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  curvature energy cannot be kept from becoming source reservoir,")
    print("  mass shift, boundary repair, or bounce-tuning device.")
    print()
    print("Consequence:")
    print()
    print("  e_curv remains diagnostic-only or is removed from future current/correction work.")
    print()
    print("Bad failure:")
    print()
    print("  call e_curv diagnostic, then let it source equations or tune a regular core.")

    status_line("curvature energy good failure stated", "DEFER")


def case_7_failure_controls():
    header("Case 7: Failure controls")

    print("Curvature energy role fails if:")
    print()
    print("1. e_curv enters field equations as source")
    print("2. e_curv shifts M_ext independently of A")
    print("3. e_curv double-counts ordinary matter")
    print("4. e_curv hides boundary repair")
    print("5. e_curv tunes gamma_like / AB / recovery")
    print("6. e_curv is used as bounce energy")
    print("7. e_curv is used to tune a regular core")
    print("8. J_curv is declared as flux/gradient of e_curv without transport law")

    status_line("curvature energy role failure controls stated", "RISK")


def case_8_next_tests():
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_curvature_energy_density_role.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_J_curv_definition_requirements.py")
    print("   Define the minimum requirements for J_curv to be more than a name.")
    print()
    print("3. candidate_curvature_energy_early_failure_summary.py")
    print("   Use if e_curv cannot be fenced from source-reservoir behavior.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_J_curv_definition_requirements.py")
    print()
    print("Reason:")
    print("  e_curv does not define J_curv by itself.")
    print("  Before a curvature balance law, J_curv needs domain, direction, balance, measure, and boundary requirements.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("Curvature energy can survive only as diagnostic/accounting for now.")
    print()
    print("Allowed:")
    print()
    print("  diagnostic curvature intensity")
    print("  finite-admissibility measure")
    print("  configuration accounting")
    print("  deferred H_curv seed")
    print()
    print("Rejected:")
    print()
    print("  source reservoir")
    print("  bounce energy")
    print("  regular-core tuning")
    print("  M_ext shift")
    print("  boundary repair")
    print("  recovery tuning")
    print("  J_curv by fiat")
    print()
    print("Best next script:")
    print()
    print("  candidate_J_curv_definition_requirements.py")

    status_line("curvature energy density role audit complete", "CLOSED")


def main():
    header("Candidate Curvature Energy Density Role")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_allowed_roles()
    case_4b_sample_diagnostic_density(ns)
    case_5_decision_tree()
    case_6_good_failure()
    case_7_failure_controls()
    case_8_next_tests()
    final_interpretation()

    with archive:
        ns.record_obligation(ProofObligationRecord(
            obligation_id="prove_e_curv_source_quarantine_in_17_curvature_energy",
            script_id=SCRIPT_ID,
            title="Prove e_curv source quarantine",
            status=ObligationStatus.OPEN,
            description="e_curv must be shown to be diagnostic/accounting only, not a field-equation source, until a recombination/source law is derived.",
        ))
        ns.record_obligation(ProofObligationRecord(
            obligation_id="prove_e_curv_mass_neutrality_in_17_curvature_energy",
            script_id=SCRIPT_ID,
            title="Prove e_curv exterior mass neutrality",
            status=ObligationStatus.OPEN,
            description="delta M_ext|e_curv = 0 must be derived to protect the A-sector result.",
        ))
        ns.record_claim(ClaimRecord(
            claim_id="e_curv_diagnostic_accounting_only_in_17",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.CANDIDATE_ROUTE,
            statement="e_curv can function as diagnostic curvature intensity or finite-admissibility accounting measure only, with no source, bounce, or regular-core role in the current group.",
        ))
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id="reject_e_curv_source_reservoir_in_17_curvature_energy",
            script_id=SCRIPT_ID,
            branch_id="curvature_energy_source_reservoir",
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=[],
        ))
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id="reject_e_curv_bounce_energy_in_17_curvature_energy",
            script_id=SCRIPT_ID,
            branch_id="curvature_energy_bounce_energy",
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=[],
        ))
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id="defer_e_curv_H_curv_seed_in_17_curvature_energy",
            script_id=SCRIPT_ID,
            branch_id="e_curv_as_H_curv_seed",
            status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=["prove_e_curv_source_quarantine_in_17_curvature_energy"],
        ))
        ns.record_derivation(
            derivation_id="curvature_energy_density_role_marker",
            inputs=[],
            output=sp.Symbol("curvature_energy_density_role_complete"),
            method="curvature_energy_density_role",
            status=Status.DERIVED,
        )
        ns.write_run_metadata()


if __name__ == "__main__":
    main()
