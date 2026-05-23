# Candidate curvature anti-singularity claim audit
#
# Group:
#   17_curvature_energy_and_finite_admissibility
#
# Script type:
#   AUDIT
#
# Purpose
# -------
# The curvature boundary/mass neutrality audit found:
#
#   Boundary/mass neutrality is required but not derived.
#
# Safest fallback:
#
#   curvature admissibility remains interior diagnostic / branch-filter only.
#
# Candidate safe routes:
#
#   compact support,
#   smooth transition,
#   exterior-neutral J_curv,
#   boundary diagnostic only.
#
# Rejected:
#
#   e_curv mass reservoir,
#   J_curv boundary repair,
#   boundary counterterm singularity avoidance,
#   recovery-tuned smoothing.
#
# This script audits what anti-singularity claim, if any, is currently licensed.
#
# Locked-door question:
#
#   What anti-singularity claim, if any, is currently licensed?
#
# This is a claim-level audit, not an anti-singularity theorem.


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


@dataclass
class AntiSingularityClaimEntry:
    name: str
    claim: str
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
        dependency_id="curvature_boundary_and_mass_neutrality_marker",
        upstream_script_id="017_curvature_energy_and_finite_admissibility__candidate_curvature_boundary_and_mass_neutrality",
        upstream_derivation_id="curvature_boundary_and_mass_neutrality_marker",
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


def build_entries() -> List[AntiSingularityClaimEntry]:
    return [
        AntiSingularityClaimEntry(
            name="AS1: anti-singularity claim target",
            claim="claim level must not exceed the derived admissibility object, dynamics, and solution support",
            role="core overclaim guard",
            allowed_if="claim strength is matched to what has been derived",
            forbidden_if="diagnostic condition is advertised as dynamical singularity resolution",
            status="REQUIRED",
            missing="claim classification",
            consequence="prevents anti-singularity overclaim",
        ),
        AntiSingularityClaimEntry(
            name="AS2: diagnostic claim",
            claim="finite-admissibility diagnostic flags singular or high-curvature configurations",
            role="currently safest licensed claim",
            allowed_if="diagnostic object/condition is stated before branch test",
            forbidden_if="flagging is called physical avoidance",
            status="SAFE_IF",
            missing="specific diagnostic functional still needed",
            consequence="allowed as current modest claim",
        ),
        AntiSingularityClaimEntry(
            name="AS3: branch-kill claim",
            claim="branches violating finite admissibility are outside the candidate solution class",
            role="safe theorem-target claim",
            allowed_if="finite-admissibility condition and branch-kill rule are stated beforehand",
            forbidden_if="used selectively after a branch looks bad",
            status="CANDIDATE",
            missing="formal A_curv condition and branch-kill theorem",
            consequence="stronger than diagnostic but still not dynamics",
        ),
        AntiSingularityClaimEntry(
            name="AS4: bounded-invariant claim",
            claim="chosen curvature invariant or invariant set remains finite on admissible branches",
            role="diagnostic/branch-filter theorem target",
            allowed_if="invariant set and domain are specified before solution",
            forbidden_if="invariant set is tailored to avoid divergence",
            status="CANDIDATE",
            missing="invariant set, domain, solutions",
            consequence="can support finite-admissibility branch tests",
        ),
        AntiSingularityClaimEntry(
            name="AS5: integrable-curvature claim",
            claim="integral curvature measure remains finite over defined domain",
            role="diagnostic/branch-filter theorem target",
            allowed_if="domain and measure are structural and cutoff-free",
            forbidden_if="cutoff removes singular region",
            status="CANDIDATE",
            missing="I_curv, D_curv, dV_phys",
            consequence="can support finite total admissibility without local dynamics",
        ),
        AntiSingularityClaimEntry(
            name="AS6: dynamical avoidance claim",
            claim="equations force evolution away from singularity",
            role="strong dynamical claim",
            allowed_if="field equations, evolution law, and proof are derived",
            forbidden_if="claimed from diagnostic, e_curv, or balance target alone",
            status="REJECTED",
            missing="dynamics/evolution theorem",
            consequence="not currently licensed",
        ),
        AntiSingularityClaimEntry(
            name="AS7: bounce claim",
            claim="collapse reverses, saturates, or bounces because of curvature admissibility",
            role="strong solution/evolution claim",
            allowed_if="dynamical equations and explicit solution/proof show bounce",
            forbidden_if="claimed from e_curv, boundary condition, or finite-admissibility slogan",
            status="REJECTED",
            missing="dynamics and solution",
            consequence="not currently licensed",
        ),
        AntiSingularityClaimEntry(
            name="AS8: regular-core claim",
            claim="interior solution remains finite / regular core replaces singularity",
            role="strong solution claim",
            allowed_if="explicit interior solution satisfies admissibility, boundary, and mass neutrality",
            forbidden_if="claimed without solution or by boundary/core tuning",
            status="REJECTED",
            missing="regular solution and matching theorem",
            consequence="not currently licensed",
        ),
        AntiSingularityClaimEntry(
            name="AS9: current-based anti-singularity claim",
            claim="J_curv transports/redistributes curvature to prevent singular behavior",
            role="future current claim",
            allowed_if="J_curv, direction, balance, neutrality, and dynamics are derived",
            forbidden_if="claimed from current name or decorative balance",
            status="DEFER",
            missing="J_curv definition and balance law",
            consequence="deferred until current exists",
        ),
        AntiSingularityClaimEntry(
            name="AS10: energy-based anti-singularity claim",
            claim="e_curv supplies energy/pressure/negative contribution that prevents singularity",
            role="forbidden source-reservoir claim under current status",
            allowed_if="only after source law and dynamics are derived, not now",
            forbidden_if="claimed from diagnostic/accounting e_curv",
            status="REJECTED",
            missing="source law and dynamics",
            consequence="prevents curvature energy bounce money",
        ),
        AntiSingularityClaimEntry(
            name="AS11: boundary-based anti-singularity claim",
            claim="boundary flux/counterterm/support condition prevents singularity",
            role="high-risk boundary claim",
            allowed_if="boundary behavior is structural, neutral, and not repair",
            forbidden_if="boundary term cancels singularity or hides mass shift",
            status="REJECTED",
            missing="boundary theorem and neutrality",
            consequence="not currently licensed",
        ),
        AntiSingularityClaimEntry(
            name="AS12: volume-response anti-singularity claim",
            claim="zeta/volume response prevents curvature blowup",
            role="curvature-volume bridge claim",
            allowed_if="B_s/F_zeta insertion, count-once, no-overlap, and boundary safety are derived",
            forbidden_if="zeta becomes hidden scalar source or residual trace",
            status="DEFER",
            missing="Group 16 bottlenecks and dynamics",
            consequence="deferred until metric insertion/no-overlap is solved",
        ),
        AntiSingularityClaimEntry(
            name="AS13: H_curv anti-singularity claim",
            claim="parent correction tensor H_curv enforces finite admissibility",
            role="future Group 19 claim",
            allowed_if="H_curv is divergence-safe and sourced by defined curvature object/current",
            forbidden_if="H_curv introduced as repair tensor",
            status="DEFER",
            missing="H_curv divergence-safe audit",
            consequence="deferred until parent correction tensor audit",
        ),
        AntiSingularityClaimEntry(
            name="AS14: ordinary-sector neutrality requirement",
            claim="any anti-singularity claim preserves no M_ext shift, no scalar leakage, no matter rerouting",
            role="ordinary exterior guard",
            allowed_if="neutrality is derived or claim remains interior diagnostic",
            forbidden_if="claim relies on exterior mass/charge/flux changes",
            status="REQUIRED",
            missing="neutrality theorem if stronger than diagnostic",
            consequence="keeps ordinary sector safe",
        ),
        AntiSingularityClaimEntry(
            name="AS15: no repair mechanism requirement",
            claim="anti-singularity cannot be obtained by boundary repair, e_curv reservoir, J_curv repair, or H_curv patch",
            role="anti-repair guard",
            allowed_if="mechanism is derived before claim",
            forbidden_if="repair terms are renamed as avoidance",
            status="REQUIRED",
            missing="mechanism if any",
            consequence="prevents painted singularity escape",
        ),
        AntiSingularityClaimEntry(
            name="AS16: no recovery construction requirement",
            claim="anti-singularity claim cannot be chosen to preserve gamma_like, AB, or exterior matching",
            role="anti-smuggling guard",
            allowed_if="recovery remains downstream",
            forbidden_if="anti-singularity mechanism is recovery-tuned",
            status="REQUIRED",
            missing="not a mechanism",
            consequence="keeps recovery downstream",
        ),
        AntiSingularityClaimEntry(
            name="AS17: claim failure",
            claim="no anti-singularity claim beyond diagnostic/branch-filter is currently licensed",
            role="safe closure condition",
            allowed_if="used to close Group 17 honestly",
            forbidden_if="patched by stronger wording",
            status="SAFE_IF",
            missing="dynamics/current/solution for stronger claims",
            consequence="keeps theory honest",
        ),
        AntiSingularityClaimEntry(
            name="AS18: recommended next move",
            claim="close Group 17 with status summary if no stronger claim is licensed",
            role="next local bottleneck",
            allowed_if="claim audit licenses diagnostic/branch-filter only",
            forbidden_if="jumping to Group 18 before summarizing handoff",
            status="RECOMMENDED",
            missing="Group 17 status summary",
            consequence="next script should be candidate_curvature_energy_group_status_summary.py",
        ),
    ]


def print_entry(e: AntiSingularityClaimEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Claim: {e.claim}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: Curvature anti-singularity claim problem")

    print("Question:")
    print()
    print("  What anti-singularity claim, if any, is currently licensed?")
    print()
    print("Goal:")
    print()
    print("  prevent overclaim after object, condition, energy, current, balance, and neutrality audits")
    print()
    print("Discipline:")
    print()
    print("  diagnostic claim is not dynamics")
    print("  branch-kill claim is not bounce")
    print("  bounded invariant is not regular core")
    print("  no e_curv bounce money")
    print("  no J_curv repair courier")
    print("  no boundary counterterm escape")
    print("  no H_curv patch")
    print("  no volume-response shortcut")
    print("  no recovery-tuned anti-singularity")

    status_line("curvature anti-singularity claim problem posed", "REQUIRED")


def case_1_inventory(entries: List[AntiSingularityClaimEntry]):
    header("Case 1: Curvature anti-singularity claim inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[AntiSingularityClaimEntry]):
    header("Case 2: Compact anti-singularity claim ledger")

    print("| Entry | Claim | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.claim.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    status_line("compact anti-singularity claim ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[AntiSingularityClaimEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Diagnostic claim is currently licensed if the diagnostic is stated beforehand.")
    print("  Branch-kill, bounded-invariant, and integrable-curvature claims remain candidates/theorem targets.")
    print("  Dynamical avoidance, bounce, regular core, energy-based, and boundary-based claims are rejected under current status.")
    print("  J_curv, volume-response, and H_curv claims are deferred.")
    print("  Group 17 should close with status summary rather than strengthen the claim.")

    status_line("anti-singularity claim status count produced", "STRUCTURAL")


def case_4_claim_ladder():
    header("Case 4: Claim ladder")

    print("Claim ladder:")
    print()
    print("1. diagnostic flag:")
    print("   currently allowed if diagnostic is defined.")
    print()
    print("2. branch-kill theorem target:")
    print("   candidate if finite-admissibility condition is formalized.")
    print()
    print("3. bounded invariant / integrable curvature theorem target:")
    print("   candidate if domain/measure/invariants are fixed.")
    print()
    print("4. dynamical avoidance:")
    print("   rejected for now; requires equations.")
    print()
    print("5. bounce:")
    print("   rejected for now; requires dynamics and solution.")
    print()
    print("6. regular core:")
    print("   rejected for now; requires explicit interior solution and matching.")
    print()
    print("7. H_curv correction:")
    print("   deferred to parent correction tensor audit.")

    status_line("anti-singularity claim ladder listed", "RECOMMENDED")


def case_5_decision_tree():
    header("Case 5: Anti-singularity claim decision tree")

    print("Decision tree:")
    print()
    print("1. Diagnostic object only:")
    print("   diagnostic claim only.")
    print()
    print("2. Finite-admissibility condition with branch-kill rule:")
    print("   branch-filter claim candidate.")
    print()
    print("3. Current/balance undefined:")
    print("   no dynamical avoidance claim.")
    print()
    print("4. No explicit solution:")
    print("   no bounce or regular-core claim.")
    print()
    print("5. Boundary/mass neutrality not derived:")
    print("   no exterior-safe strong claim.")
    print()
    print("6. H_curv not audited:")
    print("   no parent-correction anti-singularity claim.")
    print()
    print("7. Stronger wording appears:")
    print("   reject as overclaim.")

    status_line("anti-singularity claim decision tree stated", "RECOMMENDED")


def case_6_good_failure():
    header("Case 6: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  no anti-singularity claim beyond diagnostic / branch-filter is licensed.")
    print()
    print("Consequence:")
    print()
    print("  close Group 17 honestly.")
    print("  carry anti-singularity as theorem target into future current/correction work.")
    print()
    print("Bad failure:")
    print()
    print("  use words like bounce, regular core, or singularity avoidance because the diagnostics look promising.")

    status_line("anti-singularity claim good failure stated", "DEFER")


def case_7_failure_controls():
    header("Case 7: Failure controls")

    print("Anti-singularity claim audit fails if:")
    print()
    print("1. diagnostic flag is called dynamics")
    print("2. branch-kill is called bounce")
    print("3. bounded invariant is called regular core")
    print("4. e_curv is used as source/bounce money")
    print("5. J_curv is used before definition")
    print("6. balance law is used decoratively")
    print("7. boundary counterterm is used as avoidance")
    print("8. zeta/volume response reopens metric insertion")
    print("9. H_curv is introduced as patch")
    print("10. recovery targets shape the anti-singularity mechanism")
    print("11. ordinary exterior neutrality is ignored")

    status_line("anti-singularity claim failure controls stated", "RISK")


def case_8_next_tests():
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_curvature_anti_singularity_claim_audit.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_curvature_energy_group_status_summary.py")
    print("   Close Group 17 with status summary and handoff.")
    print()
    print("3. candidate_curvature_claim_overreach_failure_summary.py")
    print("   Use if a stronger claim is attempted but unsupported.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_curvature_energy_group_status_summary.py")
    print()
    print("Reason:")
    print("  The group has audited object, condition, energy, current, balance, neutrality, and claim level.")
    print("  No dynamical anti-singularity claim is licensed, so the group should close.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("Currently licensed:")
    print()
    print("  diagnostic claim")
    print("  branch-filter / theorem-target claim")
    print()
    print("Not currently licensed:")
    print()
    print("  dynamical singularity avoidance")
    print("  bounce")
    print("  regular core")
    print("  current-based avoidance")
    print("  energy-based avoidance")
    print("  boundary-based avoidance")
    print("  H_curv correction avoidance")
    print()
    print("Best next script:")
    print()
    print("  candidate_curvature_energy_group_status_summary.py")

    status_line("curvature anti-singularity claim audit complete", "CLOSED")


def main():
    header("Candidate Curvature Anti-Singularity Claim Audit")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_claim_ladder()
    case_5_decision_tree()
    case_6_good_failure()
    case_7_failure_controls()
    case_8_next_tests()
    final_interpretation()

    ns.record_obligation(ProofObligationRecord(
        obligation_id="formalize_A_curv_branch_kill_in_17_claim_audit",
        script_id=SCRIPT_ID,
        title="Formalize A_curv branch-kill rule",
        status=ObligationStatus.OPEN,
        description="Formal finite-admissibility condition and branch-kill rule are required before any branch-filter anti-singularity claim can be made.",
    ))
    # AS17: diagnostic only is best (SAFE_IF, no claim beyond diagnostic) ->
    # Per special rule: anti-singularity claim -> ClaimRecord(DEFERRED_PENDING_PREREQUISITES)
    ns.record_claim(ClaimRecord(
        claim_id="anti_singularity_diagnostic_only_in_17",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        statement="The anti-singularity claim is currently limited to diagnostic/branch-filter level only; no dynamical avoidance, bounce, or regular-core claim is licensed pending derivation of J_curv, balance law, boundary neutrality, and explicit solutions.",
    ))
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_dynamical_avoidance_in_17_claim_audit",
        script_id=SCRIPT_ID,
        branch_id="curvature_dynamical_singularity_avoidance",
        status=GovernanceStatus.REJECTED_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=[],
    ))
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_bounce_in_17_claim_audit",
        script_id=SCRIPT_ID,
        branch_id="curvature_bounce",
        status=GovernanceStatus.REJECTED_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=[],
    ))
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_regular_core_in_17_claim_audit",
        script_id=SCRIPT_ID,
        branch_id="curvature_regular_core",
        status=GovernanceStatus.REJECTED_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=[],
    ))
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_J_curv_anti_singularity_in_17_claim_audit",
        script_id=SCRIPT_ID,
        branch_id="J_curv_anti_singularity",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=["formalize_A_curv_branch_kill_in_17_claim_audit"],
    ))
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_H_curv_anti_singularity_in_17_claim_audit",
        script_id=SCRIPT_ID,
        branch_id="H_curv_anti_singularity",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=["formalize_A_curv_branch_kill_in_17_claim_audit"],
    ))
    ns.record_derivation(
        derivation_id="curvature_anti_singularity_claim_audit_marker",
        inputs=[],
        output=sp.Symbol("curvature_anti_singularity_claim_audit_complete"),
        method="curvature_anti_singularity_claim_audit",
        status=Status.DERIVED,
    )
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
