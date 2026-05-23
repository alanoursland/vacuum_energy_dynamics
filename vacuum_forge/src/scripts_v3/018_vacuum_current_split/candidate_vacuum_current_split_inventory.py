# Candidate vacuum current split inventory
#
# Group:
#   18_vacuum_current_split
#
# Script type:
#   INVENTORY
#
# Purpose
# -------
# Group 18 starts from the unresolved vacuum current bottleneck:
#
#   J_V is unresolved.
#   u_vac is unresolved because J_V is unresolved.
#   Sigma_V / R_V are role-level only.
#   Exchange continuity is theorem target, not law.
#
# The previous group also found:
#
#   Curvature admissibility is diagnostic / branch-filter only.
#   e_curv is diagnostic/accounting only, not source.
#   J_curv is not defined.
#
# This first script inventories whether J_V should remain one unresolved
# umbrella current or split into role-level candidates:
#
#   J_sub:
#     substrate / background / pure vacuum transport candidate
#
#   J_exch:
#     active exchange / source-relaxation current candidate
#
# Locked-door question:
#
#   What distinct roles are being hidden inside J_V?
#
# This is a role inventory, not an operator-level current definition.

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
)


ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def status_line(label: str, status: str, detail: str = "") -> None:
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
class VacuumCurrentSplitEntry:
    name: str
    split_role: str
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
        dependency_id="curvature_energy_group_status_summary_marker",
        upstream_script_id="017_curvature_energy_and_finite_admissibility__candidate_curvature_energy_group_status_summary",
        upstream_derivation_id="curvature_energy_group_status_summary_marker",
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


def build_entries() -> List[VacuumCurrentSplitEntry]:
    return [
        VacuumCurrentSplitEntry(
            name="VS1: vacuum current split target",
            split_role="J_V may contain distinct substrate-flow and active-exchange roles",
            role="core Group 18 target",
            allowed_if="split remains role-level until operators are defined",
            forbidden_if="split is treated as a physical decomposition by naming it",
            status="THEOREM_TARGET",
            missing="operator-level definitions of J_sub and J_exch",
            consequence="decides whether J_V can be decomposed without fake closure",
        ),
        VacuumCurrentSplitEntry(
            name="VS2: single unresolved J_V",
            split_role="J_V remains umbrella notation for unresolved vacuum current",
            role="safe fallback",
            allowed_if="no split criterion is derived",
            forbidden_if="J_V is used as a repair current or recovery tool",
            status="SAFE_IF",
            missing="physical J_V law",
            consequence="keeps vacuum-current branch honest if split is premature",
        ),
        VacuumCurrentSplitEntry(
            name="VS3: J_sub substrate-flow role",
            split_role="J_sub as pure substrate / background / vacuum transport candidate",
            role="candidate pure wind branch",
            allowed_if="pure wind neutrality, matter decoupling, and mass neutrality are preserved",
            forbidden_if="J_sub gravitates merely because it exists or shifts M_ext",
            status="CANDIDATE",
            missing="J_sub definition, frame/measure/support law, neutrality theorem",
            consequence="could represent vacuum substance flow without ordinary gravitational effect",
        ),
        VacuumCurrentSplitEntry(
            name="VS4: J_exch active-exchange role",
            split_role="J_exch as exchange/source-relaxation current candidate",
            role="candidate active exchange branch",
            allowed_if="source/relaxation sides are explicit and not repair mechanisms",
            forbidden_if="J_exch cancels boundary leakage, singularity behavior, or recovery mismatch",
            status="CANDIDATE",
            missing="J_exch definition, Sigma/R source sides, boundary/matter neutrality",
            consequence="could carry active exchange if source side becomes real",
        ),
        VacuumCurrentSplitEntry(
            name="VS5: role-level decomposition",
            split_role="J_V = J_sub + J_exch as bookkeeping only",
            role="provisional split notation",
            allowed_if="explicitly marked role-level and not field law",
            forbidden_if="used as operator identity or balance closure",
            status="SAFE_IF",
            missing="operator split criterion",
            consequence="lets later scripts test roles without pretending the split is derived",
        ),
        VacuumCurrentSplitEntry(
            name="VS6: operator-level decomposition",
            split_role="J_V = J_sub + J_exch with real projection/support/divergence criterion",
            role="future theorem target",
            allowed_if="split criterion is non-decorative and source/boundary behavior is defined",
            forbidden_if="operator split is asserted from vocabulary alone",
            status="THEOREM_TARGET",
            missing="split criterion and current definitions",
            consequence="stronger future target if role-level split survives",
        ),
        VacuumCurrentSplitEntry(
            name="VS7: pure wind neutrality requirement",
            split_role="pure substrate flow has no ordinary gravitational effect by existence alone",
            role="central J_sub safety rule",
            allowed_if="no M_ext shift, no scalar trace, no ordinary matter coupling, no boundary leakage",
            forbidden_if="pure wind becomes mass source, scalar charge, or preferred-frame force",
            status="REQUIRED",
            missing="pure wind neutrality theorem",
            consequence="decides whether J_sub can be harmless in ordinary sector",
        ),
        VacuumCurrentSplitEntry(
            name="VS8: ordinary matter decoupling requirement",
            split_role="J_sub/J_exch do not alter ordinary matter routing unless theorem derives it",
            role="matter-sector guard",
            allowed_if="rho/T_mu_nu remain routed through established ordinary sectors",
            forbidden_if="vacuum current split reroutes matter to fix curvature or boundary failures",
            status="REQUIRED",
            missing="ordinary matter decoupling theorem",
            consequence="prevents current split from becoming matter repair mechanism",
        ),
        VacuumCurrentSplitEntry(
            name="VS9: exterior mass neutrality requirement",
            split_role="J_sub/J_exch do not shift M_ext independently of A-sector",
            role="mass protection guard",
            allowed_if="current roles are exterior-neutral or coupled only through derived source law",
            forbidden_if="vacuum current changes measured exterior mass",
            status="REQUIRED",
            missing="mass neutrality theorem",
            consequence="protects strongest reduced A-sector result",
        ),
        VacuumCurrentSplitEntry(
            name="VS10: Sigma/R double-counting guard",
            split_role="Sigma_V and R_V cannot be two names for one tuning mechanism",
            role="exchange-source guard",
            allowed_if="source and relaxation sides have distinct definitions",
            forbidden_if="Sigma/R are adjusted to pass recovery or cancel leakage",
            status="REQUIRED",
            missing="Sigma_V and R_V operators",
            consequence="prevents exchange current from hiding a tuning knob",
        ),
        VacuumCurrentSplitEntry(
            name="VS11: zero-net-exchange branch",
            split_role="Sigma_V - R_V = 0 in ordinary sector",
            role="ordinary-sector neutral exchange candidate",
            allowed_if="ordinary curvature can arise from warping/constraint rather than net creation",
            forbidden_if="used to avoid defining active exchange while still claiming it sources curvature",
            status="CANDIDATE",
            missing="ordinary-sector exchange neutrality theorem",
            consequence="keeps vacuum-substance ontology while ordinary net creation is zero",
        ),
        VacuumCurrentSplitEntry(
            name="VS12: zero-creation branch",
            split_role="Sigma_V = R_V = 0 in ordinary sector",
            role="strong ordinary-sector neutrality candidate",
            allowed_if="curvature changes are attributed to constrained time/space warping",
            forbidden_if="creation/destruction language is still used as active source",
            status="CANDIDATE",
            missing="zero-creation theorem or sector condition",
            consequence="cleanest ordinary-sector no-exchange branch",
        ),
        VacuumCurrentSplitEntry(
            name="VS13: curvature-from-warping branch",
            split_role="curvature change arises from constrained spatial/time warping, not net vacuum creation/destruction",
            role="non-exchange curvature branch",
            allowed_if="does not reopen B_s/F_zeta or recovery construction",
            forbidden_if="warping relation is copied from GR or tuned by recovery",
            status="CANDIDATE",
            missing="warping constraint / parent relation",
            consequence="important alternative to active exchange in ordinary sector",
        ),
        VacuumCurrentSplitEntry(
            name="VS14: latent-exchange branch",
            split_role="Sigma/R exist as ontology/accounting but vanish or balance in ordinary sector",
            role="ontology/accounting candidate",
            allowed_if="latent exchange does not source ordinary metric or matter",
            forbidden_if="latent exchange becomes hidden source reservoir",
            status="CANDIDATE",
            missing="regime condition separating ordinary/active exchange",
            consequence="preserves substance language without forcing ordinary creation/destruction",
        ),
        VacuumCurrentSplitEntry(
            name="VS15: J_curv-related branch deferred",
            split_role="J_curv participates in vacuum current split",
            role="deferred curvature-current branch",
            allowed_if="J_curv is later defined",
            forbidden_if="Group 18 assumes J_curv is already real",
            status="DEFER",
            missing="J_curv definition",
            consequence="preserves Group 17 closure",
        ),
        VacuumCurrentSplitEntry(
            name="VS16: dark-sector branch optional",
            split_role="dark-sector coupling attaches to J_exch or vacuum current split",
            role="optional future branch",
            allowed_if="ordinary matter decoupling is preserved and not used as repair",
            forbidden_if="dark coupling patches ordinary-sector failure",
            status="DEFER",
            missing="dark-sector coupling rule and ordinary decoupling",
            consequence="keeps dark-sector speculation downstream",
        ),
        VacuumCurrentSplitEntry(
            name="VS17: preferred-frame wind rejection",
            split_role="J_sub as arbitrary preferred-frame wind",
            role="forbidden substrate shortcut",
            allowed_if="never unless ontology defines frame and neutrality",
            forbidden_if="accepted as J_sub definition",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents arbitrary-frame current",
        ),
        VacuumCurrentSplitEntry(
            name="VS18: repair-current rejection",
            split_role="J_exch or J_V chosen to cancel boundary leakage, singularity behavior, or recovery mismatch",
            role="forbidden repair branch",
            allowed_if="never as mechanism",
            forbidden_if="accepted as exchange current",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents vacuum current from becoming painted repair pipe",
        ),
        VacuumCurrentSplitEntry(
            name="VS19: H_exch/H_curv premature use rejection",
            split_role="J_sub/J_exch used to justify H_exch or H_curv immediately",
            role="forbidden parent-correction shortcut",
            allowed_if="deferred to Group 19",
            forbidden_if="correction tensor introduced before source/current objects are real",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents decorative correction tensor",
        ),
        VacuumCurrentSplitEntry(
            name="VS20: recovery downstream guard",
            split_role="gamma_like, AB, exterior recovery do not choose current split",
            role="anti-smuggling guard",
            allowed_if="recovery remains downstream test",
            forbidden_if="current split is chosen to pass recovery",
            status="REQUIRED",
            missing="not a mechanism",
            consequence="prevents recovery-shaped current split",
        ),
        VacuumCurrentSplitEntry(
            name="VS21: recommended next move",
            split_role="test pure wind neutrality before defining J_sub",
            role="next local bottleneck",
            allowed_if="role-level split is useful but not derived",
            forbidden_if="jumping to J_sub definition before neutrality rule",
            status="RECOMMENDED",
            missing="pure wind neutrality test",
            consequence="next script should be candidate_pure_wind_neutrality_test.py",
        ),
    ]


def print_entry(e: VacuumCurrentSplitEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Split role: {e.split_role}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: Vacuum current split inventory problem")

    print("Question:")
    print()
    print("  What distinct roles are being hidden inside J_V?")
    print()
    print("Goal:")
    print()
    print("  inventory whether J_V should remain unresolved umbrella current")
    print("  or split into role-level J_sub / J_exch candidates")
    print()
    print("Discipline:")
    print()
    print("  do not assume J_V is defined")
    print("  do not define J_sub or J_exch by naming them")
    print("  do not let pure wind gravitate by existence")
    print("  do not let exchange become repair")
    print("  do not let Sigma/R become hidden tuning")
    print("  do not use dark sector as ordinary repair")
    print("  do not introduce H_exch/H_curv")
    print("  keep recovery downstream")

    status_line("vacuum current split inventory problem posed", "REQUIRED")


def case_1_inventory(entries: List[VacuumCurrentSplitEntry]):
    header("Case 1: Vacuum current split inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[VacuumCurrentSplitEntry]):
    header("Case 2: Compact vacuum current split ledger")

    print("| Entry | Split role | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.split_role.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    status_line("compact vacuum current split ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[VacuumCurrentSplitEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  J_V remains unresolved.")
    print("  J_sub/J_exch split is useful as role-level bookkeeping, not operator-level law.")
    print("  Pure wind neutrality is the central safety requirement for J_sub.")
    print("  J_exch requires real source/relaxation sides and cannot be repair.")
    print("  Zero-net-exchange / zero-creation branches should stay live for ordinary sector.")
    print("  J_curv and dark-sector branches remain deferred.")
    print("  Next gate is pure wind neutrality.")

    status_line("vacuum current split inventory status count produced", "STRUCTURAL")


def case_4_split_roles():
    header("Case 4: Split role distinctions")

    print("Candidate role distinctions:")
    print()
    print("1. unresolved umbrella J_V")
    print("2. J_sub as pure substrate / background transport")
    print("3. J_exch as active exchange / source-relaxation current")
    print("4. zero-net exchange in ordinary sector")
    print("5. zero creation in ordinary sector")
    print("6. curvature-from-warping rather than net creation")
    print("7. latent exchange as ontology/accounting only")
    print()
    print("Deferred:")
    print()
    print("  J_curv-related branch")
    print("  dark-sector branch")
    print("  H_exch/H_curv branch")

    status_line("vacuum current split roles distinguished", "RECOMMENDED")


def case_5_decision_tree():
    header("Case 5: Vacuum current split decision tree")

    print("Decision tree:")
    print()
    print("1. No split criterion:")
    print("   J_V remains unresolved umbrella notation.")
    print()
    print("2. Role-level split useful:")
    print("   write J_sub/J_exch as bookkeeping only.")
    print()
    print("3. J_sub candidate:")
    print("   must pass pure wind neutrality before definition.")
    print()
    print("4. J_exch candidate:")
    print("   must have real source/relaxation sides and cannot be repair.")
    print()
    print("5. Ordinary sector:")
    print("   preserve zero-net-exchange / zero-creation branches.")
    print()
    print("6. Dark sector:")
    print("   deferred and optional.")
    print()
    print("7. Parent correction tensor:")
    print("   deferred to Group 19.")

    status_line("vacuum current split decision tree stated", "RECOMMENDED")


def case_6_good_failure():
    header("Case 6: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  J_sub/J_exch split cannot be made operator-level.")
    print()
    print("Consequence:")
    print()
    print("  keep split as role-level bookkeeping only.")
    print("  preserve pure wind neutrality and ordinary matter decoupling as theorem targets.")
    print("  keep zero-net-exchange / zero-creation branches alive in ordinary sector.")
    print()
    print("Bad failure:")
    print()
    print("  name J_sub/J_exch and use them as currents, sources, or correction-tensor inputs.")

    status_line("vacuum current split inventory good failure stated", "DEFER")


def case_7_failure_controls():
    header("Case 7: Failure controls")

    print("Vacuum current split fails if:")
    print()
    print("1. J_V is assumed defined")
    print("2. J_sub is arbitrary preferred-frame wind")
    print("3. J_sub gravitates by existence")
    print("4. J_sub shifts M_ext")
    print("5. J_sub couples to ordinary matter")
    print("6. J_exch is repair current")
    print("7. Sigma/R become tuning knobs")
    print("8. dark sector patches ordinary failure")
    print("9. current split reopens zeta metric trace")
    print("10. H_exch/H_curv introduced early")
    print("11. recovery chooses the split")

    status_line("vacuum current split inventory failure controls stated", "RISK")


def case_8_next_tests():
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_vacuum_current_split_inventory.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_pure_wind_neutrality_test.py")
    print("   Test whether pure vacuum substrate flow can exist without ordinary gravitational effect.")
    print()
    print("3. candidate_vacuum_current_split_early_failure_summary.py")
    print("   Use if split language immediately collapses into fake operators.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_pure_wind_neutrality_test.py")
    print()
    print("Reason:")
    print("  Before J_sub can be defined, pure wind must be shown harmless:")
    print("  no M_ext shift, no scalar trace, no ordinary matter coupling, no boundary repair.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("J_V remains unresolved.")
    print()
    print("J_sub/J_exch split is useful as role-level bookkeeping only.")
    print()
    print("Core live branches:")
    print()
    print("  J_sub pure substrate / pure wind candidate")
    print("  J_exch active exchange candidate")
    print("  zero-net-exchange ordinary sector")
    print("  zero-creation ordinary sector")
    print("  curvature-from-warping branch")
    print("  latent-exchange accounting branch")
    print()
    print("Best next script:")
    print()
    print("  candidate_pure_wind_neutrality_test.py")

    status_line("vacuum current split inventory complete", "CLOSED")


def main():
    header("Candidate Vacuum Current Split Inventory")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_split_roles()
    case_5_decision_tree()
    case_6_good_failure()
    case_7_failure_controls()
    case_8_next_tests()
    final_interpretation()

    ns.record_obligation(ProofObligationRecord(
        obligation_id="prove_pure_wind_neutrality_in_18_inventory",
        script_id=SCRIPT_ID,
        title="Prove pure wind neutrality",
        status=ObligationStatus.OPEN,
        description="Pure wind neutrality theorem: J_sub must have no M_ext shift, no scalar trace, no ordinary matter coupling, no boundary leakage.",
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="prove_ordinary_matter_decoupling_in_18_inventory",
        script_id=SCRIPT_ID,
        title="Prove ordinary matter decoupling",
        status=ObligationStatus.OPEN,
        description="Ordinary matter decoupling theorem: J_sub/J_exch must not alter ordinary matter routing unless a theorem derives it.",
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="prove_exterior_mass_neutrality_in_18_inventory",
        script_id=SCRIPT_ID,
        title="Prove exterior mass neutrality",
        status=ObligationStatus.OPEN,
        description="Exterior mass neutrality theorem: J_sub/J_exch must not shift M_ext independently of A-sector.",
    ))
    ns.record_claim(ClaimRecord(
        claim_id="vacuum_current_split_role_level_only_in_18",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement="J_V = J_sub + J_exch is role-level bookkeeping only. No operator-level split criterion is derived. J_sub/J_exch are useful labels for role distinctions pending real definitions.",
    ))
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_preferred_frame_wind_in_18_inventory",
        script_id=SCRIPT_ID,
        branch_id="preferred_frame_wind",
        status=GovernanceStatus.REJECTED_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        description="J_sub as arbitrary preferred-frame wind is forbidden. Frame must follow from vacuum ontology or substrate law.",
    ))
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_repair_current_in_18_inventory",
        script_id=SCRIPT_ID,
        branch_id="repair_current",
        status=GovernanceStatus.REJECTED_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        description="J_exch or J_V chosen to cancel boundary leakage, singularity behavior, or recovery mismatch is forbidden.",
    ))
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_premature_H_exch_in_18_inventory",
        script_id=SCRIPT_ID,
        branch_id="premature_H_exch_H_curv",
        status=GovernanceStatus.REJECTED_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        description="J_sub/J_exch must not be used to justify H_exch or H_curv before source/current objects are real. Deferred to Group 19.",
    ))
    ns.record_derivation(
        derivation_id="vacuum_current_split_inventory_marker",
        inputs=[],
        output=sp.Symbol("vacuum_current_split_inventory_complete"),
        method="vacuum_current_split_inventory",
        status=Status.DERIVED,
    )
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
