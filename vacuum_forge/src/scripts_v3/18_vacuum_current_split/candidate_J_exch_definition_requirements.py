# Candidate J_exch definition requirements
#
# Group:
#   18_vacuum_current_split
#
# Script type:
#   REQUIREMENTS
#
# Purpose
# -------
# The J_sub definition requirements audit found:
#
#   J_sub is not defined yet.
#
# It survives only as a theorem target requiring:
#
#   domain,
#   frame or frame-free law,
#   direction,
#   measure,
#   divergence status,
#   boundary behavior,
#   matter decoupling,
#   mass neutrality,
#   scalar trace neutrality.
#
# Rejected:
#
#   arbitrary preferred-frame wind,
#   circular u_vac,
#   remainder-current definition,
#   pure wind gravitating by existence,
#   dark-sector convenience.
#
# This script defines what J_exch must be to be more than repair current.
#
# Locked-door question:
#
#   What must J_exch be to be more than repair current?
#
# This is a requirements audit, not an exchange-current derivation.


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


@dataclass
class JExchRequirementEntry:
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
        dependency_id="J_sub_definition_requirements_marker",
        upstream_script_id="18_vacuum_current_split__candidate_J_sub_definition_requirements",
        upstream_derivation_id="J_sub_definition_requirements_marker",
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


def build_entries() -> List[JExchRequirementEntry]:
    return [
        JExchRequirementEntry(
            name="JE1: J_exch definition target",
            requirement="J_exch has source side, relaxation side, divergence/balance role, domain, direction, boundary behavior, matter decoupling, and mass neutrality",
            role="core active-exchange theorem target",
            allowed_if="all requirements are explicit before J_exch is used",
            forbidden_if="J_exch is named active exchange without source/relaxation structure",
            status="THEOREM_TARGET",
            missing="actual J_exch definition",
            consequence="decides whether active exchange language can become technical",
        ),
        JExchRequirementEntry(
            name="JE2: source side requirement",
            requirement="Sigma_exch or equivalent source side is defined",
            role="source prerequisite",
            allowed_if="source has domain, sign/strength rule, and physical meaning",
            forbidden_if="source is whatever creates desired curvature or fixes leakage",
            status="REQUIRED",
            missing="Sigma_exch operator",
            consequence="prevents source side from becoming repair label",
        ),
        JExchRequirementEntry(
            name="JE3: relaxation side requirement",
            requirement="R_exch or equivalent relaxation/sink side is defined",
            role="relaxation prerequisite",
            allowed_if="relaxation mechanism is distinct from source and not tuned",
            forbidden_if="R_exch is chosen to cancel source, divergence, boundary leakage, or recovery mismatch",
            status="REQUIRED",
            missing="R_exch operator",
            consequence="prevents relaxation from becoming cancellation knob",
        ),
        JExchRequirementEntry(
            name="JE4: Sigma/R distinction requirement",
            requirement="Sigma_exch and R_exch are not two names for one hidden tuning mechanism",
            role="double-counting guard",
            allowed_if="source and relaxation have independent definitions",
            forbidden_if="Sigma/R are adjusted against each other to pass checks",
            status="REQUIRED",
            missing="Sigma/R separation theorem",
            consequence="preserves exchange accounting honesty",
        ),
        JExchRequirementEntry(
            name="JE5: divergence / balance role requirement",
            requirement="possible balance form is stated only after current/source sides are defined",
            role="balance guard",
            allowed_if="nabla_mu J_exch^mu = Sigma_exch - R_exch is theorem target only",
            forbidden_if="balance law defines all symbols decoratively",
            status="REQUIRED",
            missing="J_exch, Sigma_exch, R_exch definitions",
            consequence="prevents decorative exchange continuity",
        ),
        JExchRequirementEntry(
            name="JE6: domain requirement",
            requirement="domain D_exch where exchange is active is specified",
            role="definition prerequisite",
            allowed_if="domain follows from source/admissibility/support law",
            forbidden_if="domain is chosen to hide leakage or boundary failure",
            status="REQUIRED",
            missing="D_exch",
            consequence="prevents convenient active region",
        ),
        JExchRequirementEntry(
            name="JE7: direction / orientation requirement",
            requirement="J_exch direction follows from source gradient, transport law, support, or admissibility structure",
            role="orientation prerequisite",
            allowed_if="direction is defined before recovery/boundary checks",
            forbidden_if="direction is chosen to cancel leakage or singular behavior",
            status="REQUIRED",
            missing="direction law",
            consequence="prevents repair-current behavior",
        ),
        JExchRequirementEntry(
            name="JE8: boundary behavior requirement",
            requirement="J_exch has no boundary repair flux, hidden exterior charge, or mass-shift leakage",
            role="boundary safety guard",
            allowed_if="boundary behavior follows from exchange law",
            forbidden_if="J_exch is chosen to repair boundary failure",
            status="REQUIRED",
            missing="boundary neutrality theorem",
            consequence="protects exterior sector",
        ),
        JExchRequirementEntry(
            name="JE9: ordinary matter decoupling requirement",
            requirement="J_exch does not reroute ordinary matter or double-count T_mu_nu",
            role="matter-sector guard",
            allowed_if="ordinary matter coupling remains independently routed",
            forbidden_if="J_exch fixes curvature/boundary behavior by changing matter coupling",
            status="REQUIRED",
            missing="ordinary matter decoupling theorem",
            consequence="prevents exchange from becoming matter repair",
        ),
        JExchRequirementEntry(
            name="JE10: mass neutrality requirement",
            requirement="delta M_ext|J_exch = 0 unless derived through A-sector source law",
            role="mass protection guard",
            allowed_if="exchange is exterior-neutral or source-coupled only by theorem",
            forbidden_if="J_exch changes measured exterior mass",
            status="REQUIRED",
            missing="mass neutrality theorem",
            consequence="protects strongest A-sector result",
        ),
        JExchRequirementEntry(
            name="JE11: scalar trace neutrality requirement",
            requirement="J_exch does not reopen B_s/F_zeta, residual trace, kappa, or ordinary scalar charge unless derived",
            role="metric-insertion guard",
            allowed_if="exchange stays outside ordinary scalar trace or has explicit insertion theorem",
            forbidden_if="J_exch becomes hidden B_s/zeta source",
            status="REQUIRED",
            missing="scalar trace / insertion theorem",
            consequence="preserves Group 16 guardrails",
        ),
        JExchRequirementEntry(
            name="JE12: relation to curvature admissibility",
            requirement="J_exch may couple to curvature admissibility only as theorem target, not dynamics",
            role="Group 17 preservation guard",
            allowed_if="A_curv remains diagnostic/branch-filter unless dynamics are derived",
            forbidden_if="J_exch turns curvature admissibility into active repair",
            status="RISK",
            missing="A_curv dynamics / J_curv absent",
            consequence="prevents curvature-admissibility overclaim",
        ),
        JExchRequirementEntry(
            name="JE13: relation to e_curv",
            requirement="J_exch is not e_curv source reservoir or bounce money",
            role="curvature-energy guard",
            allowed_if="e_curv remains diagnostic/accounting",
            forbidden_if="J_exch transports free curvature energy to force finite behavior",
            status="REJECTED",
            missing="not pursued",
            consequence="preserves Group 17 e_curv fence",
        ),
        JExchRequirementEntry(
            name="JE14: relation to J_sub",
            requirement="J_exch is distinguished from J_sub by source/support/divergence/coupling criterion",
            role="split criterion guard",
            allowed_if="criterion distinguishes active exchange from pure substrate wind",
            forbidden_if="J_exch is whatever is not J_sub",
            status="REQUIRED",
            missing="J_sub/J_exch split criterion",
            consequence="prevents role complement from becoming operator definition",
        ),
        JExchRequirementEntry(
            name="JE15: zero-net exchange branch",
            requirement="ordinary sector may have Sigma_exch - R_exch = 0",
            role="ordinary-sector neutrality candidate",
            allowed_if="ordinary curvature comes from warping/constraint or balanced exchange",
            forbidden_if="zero-net branch still claims active net exchange source",
            status="CANDIDATE",
            missing="ordinary-sector zero-net theorem",
            consequence="keeps zero-net ordinary branch live",
        ),
        JExchRequirementEntry(
            name="JE16: zero-creation branch",
            requirement="ordinary sector may have Sigma_exch = R_exch = 0",
            role="strong ordinary-sector neutrality candidate",
            allowed_if="J_exch inactive in ordinary sector and curvature arises otherwise",
            forbidden_if="creation/destruction is still used as ordinary active source",
            status="CANDIDATE",
            missing="ordinary-sector zero-creation theorem",
            consequence="keeps no-exchange ordinary branch live",
        ),
        JExchRequirementEntry(
            name="JE17: active-only domain candidate",
            requirement="J_exch active only where explicit exchange source is nonzero",
            role="candidate exchange-support rule",
            allowed_if="source side is independently defined",
            forbidden_if="support is chosen to hide boundary/exterior effects",
            status="CANDIDATE",
            missing="source support law",
            consequence="possible route to separating exchange from substrate",
        ),
        JExchRequirementEntry(
            name="JE18: endpoint/admissibility-domain candidate",
            requirement="J_exch active only at endpoints / boundaries of admissibility domain",
            role="high-risk candidate",
            allowed_if="endpoints are structural and not boundary repair",
            forbidden_if="endpoints repair singularity or leakage",
            status="RISK",
            missing="endpoint/admissibility domain theorem",
            consequence="possible but dangerous exchange localization route",
        ),
        JExchRequirementEntry(
            name="JE19: boundary repair rejection",
            requirement="J_exch chosen to cancel boundary leakage, shell source, scalar tail, or mass shift",
            role="forbidden repair-current branch",
            allowed_if="never as mechanism",
            forbidden_if="accepted as exchange current",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents painted exchange pipe",
        ),
        JExchRequirementEntry(
            name="JE20: recovery repair rejection",
            requirement="J_exch chosen to pass gamma_like, AB, exterior matching, or boundary recovery",
            role="forbidden recovery-smuggling branch",
            allowed_if="never as mechanism",
            forbidden_if="accepted as exchange law",
            status="REJECTED",
            missing="not pursued",
            consequence="keeps recovery downstream",
        ),
        JExchRequirementEntry(
            name="JE21: matter repair rejection",
            requirement="J_exch reroutes ordinary matter to fix curvature or boundary problems",
            role="forbidden matter repair branch",
            allowed_if="never without source theorem",
            forbidden_if="accepted as exchange coupling",
            status="REJECTED",
            missing="not pursued",
            consequence="preserves ordinary matter decoupling",
        ),
        JExchRequirementEntry(
            name="JE22: H_exch premature use rejection",
            requirement="J_exch immediately justifies H_exch or parent correction tensor",
            role="forbidden parent-correction shortcut",
            allowed_if="deferred to Group 19",
            forbidden_if="accepted as divergence closure",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents decorative correction tensor",
        ),
        JExchRequirementEntry(
            name="JE23: dark-sector deferral",
            requirement="dark-sector coupling to J_exch remains optional and separated",
            role="future optional branch",
            allowed_if="ordinary matter decoupling and neutrality are preserved",
            forbidden_if="dark sector patches ordinary failure",
            status="DEFER",
            missing="dark-sector coupling rule",
            consequence="keeps speculative coupling downstream",
        ),
        JExchRequirementEntry(
            name="JE24: J_exch failure",
            requirement="J_exch cannot meet source, relaxation, boundary, matter, mass, and split requirements",
            role="branch failure condition",
            allowed_if="used to keep exchange current role-level only",
            forbidden_if="patched with decorative continuity or repair current",
            status="BRANCH_KILLED",
            missing="applies if failure demonstrated",
            consequence="active exchange current cannot be used",
        ),
        JExchRequirementEntry(
            name="JE25: recommended next move",
            requirement="after J_sub/J_exch burdens are stated, audit ordinary matter decoupling for vacuum currents",
            role="next local bottleneck",
            allowed_if="both current branches remain theorem targets",
            forbidden_if="proceeding to source inventory before matter decoupling guard",
            status="RECOMMENDED",
            missing="ordinary matter decoupling audit",
            consequence="next script should be candidate_ordinary_matter_decoupling_for_vacuum_currents.py",
        ),
    ]


def print_entry(e: JExchRequirementEntry) -> None:
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
    header("Case 0: J_exch definition requirements problem")

    print("Question:")
    print()
    print("  What must J_exch be to be more than repair current?")
    print()
    print("Goal:")
    print()
    print("  state minimum active-exchange burden after J_sub has been fenced")
    print()
    print("Discipline:")
    print()
    print("  no undefined Sigma/R")
    print("  no decorative balance law")
    print("  no boundary repair")
    print("  no recovery repair")
    print("  no matter repair")
    print("  no e_curv source reservoir")
    print("  no H_exch patch")
    print("  no hidden scalar trace")
    print("  preserve zero-net / zero-creation ordinary branches")

    status_line("J_exch definition requirements problem posed", "REQUIRED")


def case_1_inventory(entries: List[JExchRequirementEntry]):
    header("Case 1: J_exch definition requirements inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[JExchRequirementEntry]):
    header("Case 2: Compact J_exch requirements ledger")

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

    status_line("compact J_exch requirements ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[JExchRequirementEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  J_exch is not defined yet.")
    print("  A real J_exch requires source side, relaxation side, balance role, domain, direction, boundary behavior, matter decoupling, mass neutrality, scalar-trace guard, and split criterion.")
    print("  Sigma/R double-counting remains the central danger.")
    print("  Curvature admissibility and e_curv cannot be used as repair reservoirs.")
    print("  Zero-net and zero-creation ordinary-sector branches remain live.")
    print("  Next gate is ordinary matter decoupling for both J_sub and J_exch.")

    status_line("J_exch requirements status count produced", "STRUCTURAL")


def case_4_required_fields():
    header("Case 4: Required J_exch fields")

    print("Required J_exch fields:")
    print()
    print("1. source side")
    print("2. relaxation side")
    print("3. Sigma/R distinction")
    print("4. divergence / balance role")
    print("5. domain")
    print("6. direction / orientation")
    print("7. boundary behavior")
    print("8. ordinary matter decoupling")
    print("9. mass neutrality")
    print("10. scalar trace guard")
    print("11. relation to curvature admissibility")
    print("12. relation to e_curv")
    print("13. relation to J_sub")
    print("14. zero-net / zero-creation ordinary-sector condition")

    status_line("required J_exch fields listed", "RECOMMENDED")


def case_5_decision_tree():
    header("Case 5: J_exch definition decision tree")

    print("Decision tree:")
    print()
    print("1. J_exch has source/relaxation sides:")
    print("   exchange-current theorem target survives.")
    print()
    print("2. Sigma/R are undefined:")
    print("   J_exch remains role-level only.")
    print()
    print("3. J_exch repairs boundary/recovery/matter:")
    print("   rejected.")
    print()
    print("4. J_exch uses e_curv as reservoir:")
    print("   rejected.")
    print()
    print("5. J_exch is inactive in ordinary sector:")
    print("   zero-net or zero-creation branch stays live.")
    print()
    print("6. J_exch cannot meet requirements:")
    print("   active exchange branch killed or remains bookkeeping.")

    status_line("J_exch definition decision tree stated", "RECOMMENDED")


def case_6_good_failure():
    header("Case 6: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  J_exch cannot be defined without undefined Sigma/R,")
    print("  repair behavior, matter rerouting, source reservoir, or boundary patch.")
    print()
    print("Consequence:")
    print()
    print("  do not use J_exch as current.")
    print("  preserve zero-net/zero-creation ordinary-sector branches.")
    print()
    print("Bad failure:")
    print()
    print("  write nabla_mu J_exch^mu = Sigma_exch - R_exch")
    print("  while all three objects are labels.")

    status_line("J_exch definition good failure stated", "DEFER")


def case_7_failure_controls():
    header("Case 7: Failure controls")

    print("J_exch definition fails if:")
    print()
    print("1. Sigma_exch is undefined")
    print("2. R_exch is undefined")
    print("3. Sigma/R are tuning knobs")
    print("4. balance law defines symbols decoratively")
    print("5. domain hides leakage/failure")
    print("6. direction cancels leakage or singularity")
    print("7. boundary behavior repairs failure")
    print("8. matter coupling is rerouted")
    print("9. M_ext shifts")
    print("10. scalar trace reopens")
    print("11. e_curv becomes source reservoir")
    print("12. H_exch is introduced early")
    print("13. dark sector patches ordinary failure")

    status_line("J_exch definition failure controls stated", "RISK")


def case_8_next_tests():
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_J_exch_definition_requirements.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_ordinary_matter_decoupling_for_vacuum_currents.py")
    print("   Audit whether J_sub/J_exch avoid changing ordinary matter coupling.")
    print()
    print("3. candidate_J_exch_failure_summary.py")
    print("   Use if J_exch cannot meet exchange-current requirements.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_ordinary_matter_decoupling_for_vacuum_currents.py")
    print()
    print("Reason:")
    print("  Both J_sub and J_exch are now constrained theorem targets.")
    print("  The next shared safety gate is ordinary matter decoupling.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("J_exch is not defined yet.")
    print()
    print("It survives only as a theorem target requiring:")
    print()
    print("  source side")
    print("  relaxation side")
    print("  Sigma/R distinction")
    print("  divergence/balance role")
    print("  domain")
    print("  direction")
    print("  boundary behavior")
    print("  ordinary matter decoupling")
    print("  mass neutrality")
    print("  scalar trace guard")
    print()
    print("Rejected:")
    print()
    print("  boundary repair")
    print("  recovery repair")
    print("  matter repair")
    print("  e_curv source reservoir")
    print("  H_exch shortcut")
    print()
    print("Best next script:")
    print()
    print("  candidate_ordinary_matter_decoupling_for_vacuum_currents.py")

    status_line("J_exch definition requirements audit complete", "CLOSED")


def main():
    header("Candidate J_exch Definition Requirements")
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

    ns.record_obligation(ProofObligationRecord(
        obligation_id="define_Sigma_exch_in_18_J_exch_requirements",
        script_id=SCRIPT_ID,
        status=ObligationStatus.OPEN,
        statement="Sigma_exch or equivalent source side must be defined with domain, sign/strength rule, and physical meaning before J_exch is used.",
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="define_R_exch_in_18_J_exch_requirements",
        script_id=SCRIPT_ID,
        status=ObligationStatus.OPEN,
        statement="R_exch or equivalent relaxation/sink side must be defined, distinct from source, and not chosen to cancel divergence or leakage.",
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="prove_Sigma_R_distinction_in_18_J_exch_requirements",
        script_id=SCRIPT_ID,
        status=ObligationStatus.OPEN,
        statement="Sigma_exch and R_exch must have independent definitions. They must not be two names for one hidden tuning mechanism.",
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="prove_J_exch_boundary_neutrality_in_18_J_exch_requirements",
        script_id=SCRIPT_ID,
        status=ObligationStatus.OPEN,
        statement="J_exch must have no boundary repair flux, hidden exterior charge, or mass-shift leakage. Boundary behavior must follow from exchange law.",
    ))
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_J_exch_boundary_repair_in_18_J_exch_requirements",
        script_id=SCRIPT_ID,
        branch_name="J_exch_boundary_repair",
        status=GovernanceStatus.REJECTED_ROUTE,
        rationale="J_exch chosen to cancel boundary leakage, shell source, scalar tail, or mass shift is forbidden as repair-current behavior.",
    ))
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_J_exch_recovery_repair_in_18_J_exch_requirements",
        script_id=SCRIPT_ID,
        branch_name="J_exch_recovery_repair",
        status=GovernanceStatus.REJECTED_ROUTE,
        rationale="J_exch chosen to pass gamma_like, AB, or exterior matching is forbidden recovery-smuggling.",
    ))
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_J_exch_e_curv_reservoir_in_18_J_exch_requirements",
        script_id=SCRIPT_ID,
        branch_name="J_exch_e_curv_reservoir",
        status=GovernanceStatus.REJECTED_ROUTE,
        rationale="J_exch transporting free curvature energy (e_curv) as source reservoir is forbidden. Preserves Group 17 e_curv fence.",
    ))
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_J_exch_dark_sector_in_18_J_exch_requirements",
        script_id=SCRIPT_ID,
        branch_name="J_exch_dark_sector_coupling",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        rationale="Dark-sector coupling to J_exch remains optional and separated. Must not patch ordinary failure. Deferred pending dark-sector coupling rule.",
    ))
    ns.record_derivation(
        derivation_id="J_exch_definition_requirements_marker",
        inputs=[],
        output=sp.Symbol("J_exch_definition_requirements_complete"),
        method="J_exch_definition_requirements",
        status=Status.DERIVED,
    )
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
