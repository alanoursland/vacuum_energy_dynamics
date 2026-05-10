# Candidate vacuum current split group status summary
#
# Group:
#   18_vacuum_current_split
#
# Script type:
#   SUMMARY
#
# Purpose
# -------
# Group 18 audited:
#
#   vacuum current split inventory,
#   pure wind neutrality,
#   J_sub definition requirements,
#   J_exch definition requirements,
#   ordinary matter decoupling,
#   exchange current source-side inventory,
#   dark-sector optional coupling.
#
# It did not derive J_V, J_sub, J_exch, u_vac, Sigma/R operators,
# ordinary matter decoupling, pure wind neutrality, dark-sector coupling,
# or H_exch/H_curv.
#
# This script closes Group 18 as a status summary.
#
# It is not a field equation, not a current law, not a source law,
# and not a parent correction tensor.


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
class Group18StatusEntry:
    name: str
    result: str
    status: str
    consequence: str
    handoff: str


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="dark_sector_coupling_optional_branch_marker",
        upstream_script_id="18_vacuum_current_split__candidate_dark_sector_coupling_optional_branch",
        upstream_derivation_id="dark_sector_coupling_optional_branch_marker",
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


def build_entries() -> List[Group18StatusEntry]:
    return [
        Group18StatusEntry(
            name="G18-1: J_V",
            result="J_V remains unresolved umbrella notation",
            status="UNRESOLVED",
            consequence="u_vac remains unresolved because no real vacuum current has been defined",
            handoff="do not assume J_V is physical current in Group 19",
        ),
        Group18StatusEntry(
            name="G18-2: J_sub/J_exch split",
            result="J_sub/J_exch split is useful as role-level bookkeeping only",
            status="SAFE_IF",
            consequence="split is not operator-level decomposition",
            handoff="do not use J_V = J_sub + J_exch as field law",
        ),
        Group18StatusEntry(
            name="G18-3: J_sub",
            result="J_sub survives only as neutral substrate-current theorem target",
            status="THEOREM_TARGET",
            consequence="requires pure wind neutrality, domain, frame/frame-free law, measure, boundary behavior, matter decoupling, mass neutrality, scalar-trace neutrality",
            handoff="pure wind is not ordinary gravity",
        ),
        Group18StatusEntry(
            name="G18-4: pure wind neutrality",
            result="pure wind neutrality is required but not derived",
            status="THEOREM_TARGET",
            consequence="J_sub cannot shift M_ext, source scalar trace, push matter, repair boundary, or tune recovery",
            handoff="preserve pure wind neutrality as required future theorem",
        ),
        Group18StatusEntry(
            name="G18-5: J_exch",
            result="J_exch survives only as active-exchange theorem target",
            status="THEOREM_TARGET",
            consequence="requires source side, relaxation side, Sigma/R distinction, balance role, domain, direction, boundary behavior, matter decoupling, mass neutrality, scalar trace guard",
            handoff="exchange is not repair",
        ),
        Group18StatusEntry(
            name="G18-6: Sigma/R",
            result="Sigma/R remain role-level unless distinct operators and strength laws are found",
            status="UNRESOLVED",
            consequence="no exchange continuity law is derived",
            handoff="do not write decorative nabla_mu J_exch^mu = Sigma_exch - R_exch",
        ),
        Group18StatusEntry(
            name="G18-7: ordinary matter decoupling",
            result="ordinary matter decoupling is required but not derived",
            status="THEOREM_TARGET",
            consequence="rho/scalar charge remains routed to A-sector; no T_mu_nu double-count; no fifth force; no hidden scalar charge; no M_ext shift independent of A",
            handoff="ordinary matter must stay in A's lane unless theorem derives otherwise",
        ),
        Group18StatusEntry(
            name="G18-8: J_exch source side",
            result="no active ordinary-sector source side for J_exch is derived",
            status="UNRESOLVED",
            consequence="curvature admissibility, volume response, matter-induced exchange, and boundary exchange are high risk",
            handoff="ordinary-sector J_exch should stay inactive/role-level unless source side is derived",
        ),
        Group18StatusEntry(
            name="G18-9: safest ordinary-sector branches",
            result="zero-net exchange, zero creation, curvature-from-warping, and latent exchange survive",
            status="CANDIDATE",
            consequence="ordinary curvature need not imply net vacuum creation/destruction",
            handoff="preserve zero-net / zero-creation branches in field-equation snapshot",
        ),
        Group18StatusEntry(
            name="G18-10: dark-sector coupling",
            result="no dark-sector coupling is required",
            status="SAFE_IF",
            consequence="safest default is no dark-sector coupling in Group 18",
            handoff="dark coupling to J_exch only may remain future candidate if ordinary separation and source law exist",
        ),
        Group18StatusEntry(
            name="G18-11: forbidden dark uses",
            result="dark patch for ordinary failure, M_ext shift, scalar leak, boundary repair, recovery repair, and H_exch shortcut are rejected",
            status="REJECTED",
            consequence="dark sector cannot rescue failed ordinary source/current branches",
            handoff="carry no-dark-patch rule into Group 19",
        ),
        Group18StatusEntry(
            name="G18-12: H_exch/H_curv",
            result="H_exch/H_curv remain deferred",
            status="DEFER",
            consequence="parent correction tensors cannot be justified by role-level currents or dark labels",
            handoff="Group 19 may audit correction tensors only as divergence-safe non-decorative targets",
        ),
        Group18StatusEntry(
            name="G18-13: final Group 18 closure",
            result="Group 18 closes at role-level split / theorem-target strength",
            status="CLOSED",
            consequence="vacuum-current split is disciplined but not operator-level",
            handoff="update field-equation snapshot before opening Group 19 if needed",
        ),
    ]


def print_entry(e: Group18StatusEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Result: {e.result}")
    status_line(e.name, e.status)
    print(f"Consequence: {e.consequence}")
    print(f"Handoff: {e.handoff}")


def case_0_problem_statement():
    header("Case 0: Group 18 status problem")

    print("Question:")
    print()
    print("  What is the current status of the vacuum-current split after Group 18 audits?")
    print()
    print("Goal:")
    print()
    print("  close the group without promoting role-level current language to operator-level law")
    print()
    print("Discipline:")
    print()
    print("  no J_V as defined current")
    print("  no J_sub physical wind without neutrality")
    print("  no J_exch source law without source sides")
    print("  no ordinary matter rerouting")
    print("  no M_ext shift")
    print("  no hidden scalar charge")
    print("  no dark-sector patch")
    print("  no H_exch/H_curv shortcut")
    print("  preserve zero-net / zero-creation branches")

    status_line("Group 18 status problem posed", "REQUIRED")


def case_1_status_ledger(entries: List[Group18StatusEntry]):
    header("Case 1: Group 18 status ledger")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[Group18StatusEntry]):
    header("Case 2: Compact Group 18 status table")

    print("| Entry | Result | Status | Handoff |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.result.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.handoff.replace("|", "/")
            + " |"
        )

    status_line("compact Group 18 status table produced", "STRUCTURAL")


def case_3_status_counts(entries: List[Group18StatusEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Group 18 disciplined vacuum-current language but did not derive operators.")
    print("  J_V, Sigma/R, and ordinary-sector J_exch source side remain unresolved.")
    print("  J_sub and J_exch survive as theorem targets only.")
    print("  Pure wind neutrality and ordinary matter decoupling are required but not derived.")
    print("  Zero-net exchange, zero creation, curvature-from-warping, and latent exchange remain safest ordinary-sector branches.")
    print("  No dark-sector coupling is required.")
    print("  H_exch/H_curv remain deferred.")

    status_line("Group 18 status count produced", "STRUCTURAL")


def case_4_current_working_rule():
    header("Case 4: Current working rule")

    print("Current working rule:")
    print()
    print("  Vacuum-current split is role-level only.")
    print("  Pure wind is not gravity.")
    print("  Exchange is not repair.")
    print("  Matter stays in A's lane.")
    print("  Dark sector does not patch ordinary failure.")
    print()
    print("Currently licensed:")
    print()
    print("  role-level J_sub/J_exch bookkeeping")
    print("  zero-net exchange branch")
    print("  zero-creation branch")
    print("  curvature-from-warping branch")
    print("  latent exchange accounting branch")
    print()
    print("Not currently licensed:")
    print()
    print("  physical J_V current")
    print("  physical J_sub substrate current")
    print("  physical J_exch active current")
    print("  ordinary-sector exchange source")
    print("  dark-sector coupling")
    print("  H_exch/H_curv correction closure")

    status_line("Group 18 working rule recorded", "SAFE_IF")


def case_5_surviving_bottlenecks():
    header("Case 5: Surviving bottlenecks")

    bottlenecks = [
        "J_V definition",
        "u_vac definition",
        "J_sub domain/frame/measure/direction law",
        "pure wind neutrality theorem",
        "J_exch source side",
        "J_exch relaxation side",
        "Sigma/R distinction and strength laws",
        "ordinary matter decoupling theorem",
        "mass neutrality theorem",
        "scalar trace neutrality theorem",
        "boundary neutrality theorem",
        "zero-net exchange ordinary-sector condition",
        "zero-creation ordinary-sector condition",
        "curvature-from-warping parent relation",
        "latent vs active exchange regime condition",
        "dark-sector source separation if reopened",
        "H_exch/H_curv divergence-safe audit in Group 19",
    ]

    for idx, item in enumerate(bottlenecks, 1):
        print(f"{idx}. {item}")

    print()
    print("Central bottleneck:")
    print()
    print("  define a real vacuum current/source structure,")
    print("  or keep the split role-level and ordinary-sector neutral.")

    status_line("surviving bottlenecks recorded", "UNRESOLVED")


def case_6_rejected_regressions():
    header("Case 6: Rejected regressions to preserve")

    regressions = [
        "J_V assumed defined",
        "J_sub as arbitrary preferred-frame wind",
        "J_sub gravitating by existence",
        "J_sub pushing ordinary matter",
        "J_sub shifting M_ext",
        "J_sub sourcing scalar trace",
        "J_sub as remainder current",
        "J_exch as repair current",
        "Sigma/R as tuning knobs",
        "decorative exchange continuity law",
        "ordinary T as Sigma_exch by fiat",
        "matter-induced exchange by convenience",
        "boundary exchange as repair",
        "curvature admissibility as active repair source",
        "e_curv as source reservoir",
        "dark sector patching ordinary failure",
        "dark sector shifting ordinary M_ext",
        "dark scalar charge leak",
        "H_exch/H_curv shortcut",
        "recovery-tuned current/source/coupling",
    ]

    for idx, item in enumerate(regressions, 1):
        print(f"{idx}. {item}")

    status_line("rejected regressions preserved", "REJECTED")


def case_7_next_options():
    header("Case 7: Next options")

    print("Possible next documents/scripts:")
    print()
    print("1. candidate_vacuum_current_split_group_status_summary.md")
    print("   Artifact for this script.")
    print()
    print("2. field_equation_status_after_group_18.md")
    print("   Update current field-equation snapshot after Group 18.")
    print()
    print("3. Group 19 first script:")
    print("   candidate_parent_correction_tensor_role_inventory.py")
    print()
    print("Recommended next document:")
    print()
    print("  field_equation_status_after_group_18.md")
    print()
    print("Reason:")
    print("  Group 18 is a status closure. The field-equation snapshot should be updated")
    print("  before opening the parent correction tensor audit.")

    status_line("next document selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("Group 18 did not derive J_V, J_sub, J_exch, u_vac, Sigma/R operators, ordinary matter decoupling, pure wind neutrality, dark-sector coupling, or H_exch/H_curv.")
    print()
    print("It produced a sharper vacuum-current boundary:")
    print()
    print("  vacuum-current split is role-level only;")
    print("  J_sub is pure-wind theorem target only;")
    print("  J_exch is active-exchange theorem target only;")
    print("  ordinary matter decoupling is required;")
    print("  no ordinary-sector source side for J_exch is derived;")
    print("  zero-net / zero-creation / curvature-from-warping / latent exchange remain safest;")
    print("  no dark-sector coupling is required;")
    print("  H_exch/H_curv remain deferred.")
    print()
    print("Best next document:")
    print()
    print("  field_equation_status_after_group_18.md")

    status_line("Group 18 vacuum current split status complete", "CLOSED")


def main():
    header("Candidate Vacuum Current Split Group Status Summary")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    entries = build_entries()
    case_1_status_ledger(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_current_working_rule()
    case_5_surviving_bottlenecks()
    case_6_rejected_regressions()
    case_7_next_options()
    final_interpretation()

    with archive:
        ns.record_handoff_import(HandoffImportRecord(
            handoff_id="group_19_handoff",
            script_id=SCRIPT_ID,
            imported_as=RecordKind.SUMMARY_CLAIM,
            status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
            imported_record_refs=[
                "obligation:prove_pure_wind_neutrality_in_18_inventory",
                "obligation:prove_ordinary_matter_decoupling_in_18_inventory",
                "obligation:prove_exterior_mass_neutrality_in_18_inventory",
                "obligation:prove_pure_wind_mass_neutrality_in_18_pure_wind",
                "obligation:define_J_sub_domain_in_18_J_sub_requirements",
                "obligation:define_Sigma_exch_in_18_J_exch_requirements",
                "obligation:define_R_exch_in_18_J_exch_requirements",
                "claim:vacuum_current_split_role_level_only_in_18",
                "claim:pure_wind_neutrality_theorem_target_in_18",
                "claim:no_active_ordinary_source_side_for_J_exch_in_18",
                "claim:dark_sector_no_coupling_default_in_18",
            ],
            description="Group 19 may import: J_V unresolved, J_sub/J_exch role-level only, pure wind neutrality required but not derived, no ordinary-sector J_exch source side, ordinary matter decoupling required, no dark-sector coupling, H_exch/H_curv remain deferred. Group 19 should audit correction tensors only as divergence-safe non-decorative targets after source/current objects are real.",
        ))
        ns.record_derivation(
            derivation_id="vacuum_current_split_group_status_summary_marker",
            inputs=[],
            output=sp.Symbol("vacuum_current_split_group_status_summary_complete"),
            method="vacuum_current_split_group_status_summary",
            status=Status.DERIVED,
        )
        ns.write_run_metadata()


if __name__ == "__main__":
    main()
