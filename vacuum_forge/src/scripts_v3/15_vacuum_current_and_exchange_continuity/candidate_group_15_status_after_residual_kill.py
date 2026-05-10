# Group:
#   15_vacuum_current_and_exchange_continuity
#
# Script type:
#   SUMMARY
#
# Candidate Group 15 status after residual-kill
#
# Purpose
# -------
# The residual-kill audit found:
#
#   residual-kill / non-metric residual is the cleanest safe convention
#   if J_V-driven zeta enters B_s.
#
# But it remains provisional.
#
# This script updates the Group 15 status after that audit.
#
# It is not a derivation and not a field-equation proposal.

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
    ObligationStatus,
    ProofObligationRecord,
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
class Group15StatusEntry:
    name: str
    result: str
    status: str
    consequence: str
    handoff: str


def build_entries() -> List[Group15StatusEntry]:
    return [
        Group15StatusEntry(
            name="G15R-1: J_V status",
            result="J_V remains undefined as a physical flux / transport current",
            status="UNRESOLVED",
            consequence="u_vac cannot be globally defined from J_V",
            handoff="do not promote J_V to field-equation ingredient",
        ),
        Group15StatusEntry(
            name="G15R-2: exchange continuity status",
            result="nabla_mu J_V^mu = Sigma_V - R_V remains a theorem target, not a law",
            status="THEOREM_TARGET",
            consequence="continuity constrains but does not define current",
            handoff="requires independent J_V, Sigma_V, and R_V operators",
        ),
        Group15StatusEntry(
            name="G15R-3: Sigma/R status",
            result="Sigma_V and R_V have been split at role-level only",
            status="STRUCTURAL",
            consequence="source and relaxation jobs are separated, but no operators are derived",
            handoff="preserve double-counting guard between Sigma_V and R_V",
        ),
        Group15StatusEntry(
            name="G15R-4: flux direction status",
            result="Sigma_V - R_V supplies divergence strength, not vector direction",
            status="REQUIRED",
            consequence="J_V requires an independent physical flux / transport law",
            handoff="do not promote elliptic completion or repair current",
        ),
        Group15StatusEntry(
            name="G15R-5: u_vac domain status",
            result="u_vac from J_V exists only on D_V = {J_V^2 < 0, J_V != 0}",
            status="THEOREM_TARGET",
            consequence="domain-limited current does not give global vacuum clock",
            handoff="static/equilibrium regions need separate treatment if frame is required",
        ),
        Group15StatusEntry(
            name="G15R-6: ordinary static safety",
            result="static zero-current or compact/balanced exchange may be safe; exterior scalar charge kills current family",
            status="REQUIRED",
            consequence="ordinary static mass must not create zeta/kappa/J_V scalar tail",
            handoff="do not patch scalar charge with R_V or boundary repair",
        ),
        Group15StatusEntry(
            name="G15R-7: boundary safety",
            result="surviving current requires zero exterior flux, zero scalar charge, no far-zone scalar flux, and no M_ext shift",
            status="REQUIRED",
            consequence="volume current cannot become scalar exterior gravity",
            handoff="boundary elliptic completion remains diagnostic only",
        ),
        Group15StatusEntry(
            name="G15R-8: no-overlap status",
            result="O[B_s, zeta_residual/kappa_residual, J_V] = 0 remains unresolved",
            status="UNRESOLVED",
            consequence="count-once recombination remains missing theorem",
            handoff="do not insert J_V-driven zeta into ordinary metric sector without residual-kill convention or O",
        ),
        Group15StatusEntry(
            name="G15R-9: residual-kill convention",
            result="if J_V-driven zeta enters B_s, residual zeta/kappa metric trace is killed or made non-metric",
            status="SAFE_IF",
            consequence="cleanest provisional count-once convention",
            handoff="use only as provisional safety convention, not derivation",
        ),
        Group15StatusEntry(
            name="G15R-10: non-metric residual branch",
            result="zeta/kappa residual may remain as bookkeeping or first-order non-radiative relaxation, not direct metric trace",
            status="CANDIDATE",
            consequence="preserves residual variables without scalar-gravity behavior if guarded",
            handoff="requires non-metric bookkeeping or P_relax mechanism",
        ),
        Group15StatusEntry(
            name="G15R-11: neutral residual branch",
            result="neutral residual metric trace remains possible only if O, boundary neutrality, and no mass overlap are derived",
            status="RISK",
            consequence="highest theorem burden",
            handoff="do not use neutral residual as escape from residual-kill",
        ),
        Group15StatusEntry(
            name="G15R-12: kappa status",
            result="kappa remains diagnostic / non-metric / separately neutral unless derived",
            status="REQUIRED",
            consequence="kappa must not restore killed zeta residual trace",
            handoff="kappa cleanup remains a standing guardrail",
        ),
        Group15StatusEntry(
            name="G15R-13: energy/accounting status",
            result="epsilon_vac_config / e_kappa cannot count killed residual as extra source energy",
            status="REQUIRED",
            consequence="prevents hidden coefficient reservoir",
            handoff="energy/accounting is diagnostic unless recombined once",
        ),
        Group15StatusEntry(
            name="G15R-14: recovery status",
            result="gamma_like and AB remain recovery checks only",
            status="RECOVERY_TARGET",
            consequence="recovery cannot choose residual-kill, flux law, domain, or overlap split",
            handoff="keep observational/GR-compatible targets downstream",
        ),
        Group15StatusEntry(
            name="G15R-15: Group 15 status decision",
            result="Group 15 has narrowed the current/exchange path but has not derived a field equation",
            status="CLOSED",
            consequence="next document should update field-equation status rather than continue the same subchain",
            handoff="recommended next: update field-equation status after Group 15",
        ),
    ]


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="residual_kill_rule_for_volume_current_marker",
        upstream_script_id="15_vacuum_current_and_exchange_continuity__candidate_residual_kill_rule_for_volume_current",
        upstream_derivation_id="residual_kill_rule_for_volume_current_marker",
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


def print_entry(e: Group15StatusEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Result: {e.result}")
    print(f"Status: {e.status}")
    print(f"Consequence: {e.consequence}")
    print(f"Handoff: {e.handoff}")


def case_0_problem_statement():
    header("Case 0: Group 15 status-after-residual-kill problem")

    print("Question:")
    print()
    print("  What is the Group 15 status after adopting residual-kill as provisional convention?")
    print()
    print("Goal:")
    print()
    print("  update the current/exchange-continuity status without claiming a derivation")
    print()
    print("Discipline:")
    print()
    print("  do not treat residual-kill as derived")
    print("  do not promote J_V or exchange continuity to field equation")
    print("  preserve no-overlap as unresolved")
    print("  preserve recovery downstream")
    print("  prepare field-equation status update")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("Group 15 status-after-residual-kill problem posed", StatusMark.OBLIGATION, "requires honest Group 15 closure")


def case_1_status_ledger(entries: List[Group15StatusEntry]):
    header("Case 1: Group 15 status ledger after residual-kill")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[Group15StatusEntry]):
    header("Case 2: Compact Group 15 status table")

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

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("compact Group 15 status table produced", StatusMark.INFO, "summary only")


def case_3_status_counts(entries: List[Group15StatusEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  J_V and O remain unresolved.")
    print("  Exchange continuity remains theorem target.")
    print("  Residual-kill is the safest provisional convention.")
    print("  Group 15 narrowed the field-equation search but did not derive a field equation.")
    print("  Next step should update field-equation status after Group 15.")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("Group 15 status count produced", StatusMark.INFO, "summary only")


def case_4_surviving_bottlenecks():
    header("Case 4: Surviving bottlenecks after residual-kill")

    bottlenecks = [
        "J_V physical flux / transport law",
        "Sigma_V source operator",
        "R_V relaxation / return operator",
        "timelike/nonzero active domain for u_vac",
        "equilibrium-frame fallback if J_V = 0 but frame needed",
        "static-source neutrality theorem",
        "boundary neutrality theorem",
        "no-overlap operator O",
        "residual-kill derivation or parent identity",
        "kappa cleanup",
        "B_s / F_zeta insertion law",
    ]

    for idx, item in enumerate(bottlenecks, 1):
        print(f"{idx}. {item}")

    print()
    print("Central surviving bottleneck:")
    print()
    print("  real J_V + no-overlap/residual-kill mechanism")

    out = ScriptOutput()
    with out.unresolved_obligations():
        out.line("real J_V + no-overlap/residual-kill mechanism", StatusMark.OBLIGATION, "central surviving bottleneck after Group 15")


def case_5_current_convention():
    header("Case 5: Current working convention")

    print("Working convention:")
    print()
    print("  If J_V-driven zeta enters B_s,")
    print("  residual zeta/kappa metric trace is killed or made non-metric.")
    print()
    print("Status:")
    print()
    print("  provisional safety convention")
    print("  not derived")
    print("  revisitable if O is derived")
    print("  mandatory if no neutral-residual theorem exists")
    print()
    print("Revisit triggers:")
    print()
    print("1. explicit no-overlap operator O is derived")
    print("2. neutral residual branch becomes structurally safe")
    print("3. B_s/F_zeta insertion law changes")
    print("4. kappa obtains separately derived non-overlap status")
    print("5. parent identity derives residual-kill or residual survival")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("working convention recorded", StatusMark.WARN, "provisional only; not derived")


def case_6_rejected_regressions():
    header("Case 6: Rejected regressions to preserve")

    regressions = [
        "residual-kill treated as derived",
        "J_V promoted without physical flux law",
        "continuity treated as current definition",
        "Sigma/R roles treated as operators",
        "zeta enters both B_s and residual metric trace",
        "kappa restores killed residual trace",
        "killed residual reappears as energy/source reservoir",
        "neutral residual assumed without O",
        "P_relax becomes Box zeta / Box kappa",
        "boundary repair hides exterior scalar charge",
        "recovery checks choose residual status",
    ]

    for idx, item in enumerate(regressions, 1):
        print(f"{idx}. {item}")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("rejected regressions preserved", StatusMark.INFO, "policy rules recorded")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts/documents:")
    print()
    print("1. candidate_group_15_status_after_residual_kill.md")
    print("   Artifact for this script.")
    print()
    print("2. field_equation_status_after_group_15.md")
    print("   Update the larger field-equation status document.")
    print()
    print("3. candidate_B_s_F_zeta_insertion_law.py")
    print("   Use only if continuing narrowly on metric insertion.")
    print()
    print("Recommended next document:")
    print()
    print("  field_equation_status_after_group_15.md")
    print()
    print("Reason:")
    print("  Group 15 has produced a durable status update. The larger field-equation status should now be revised before opening another mechanism search.")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("next document selected", StatusMark.INFO, "field_equation_status_after_group_15.md")


def final_interpretation():
    header("Final interpretation")

    print("Group 15 has not produced a field equation.")
    print()
    print("It has produced a sharper working boundary:")
    print()
    print("  J_V-driven zeta may enter ordinary metric trace only through B_s,")
    print("  with residual zeta/kappa metric trace killed or non-metric,")
    print("  unless a real no-overlap operator O is later derived.")
    print()
    print("Best next document:")
    print()
    print("  field_equation_status_after_group_15.md")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("Group 15 status after residual-kill complete", StatusMark.PASS, "closed")


def main():
    header("Candidate Group 15 Status After Residual-Kill")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    entries = build_entries()
    case_1_status_ledger(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_surviving_bottlenecks()
    case_5_current_convention()
    case_6_rejected_regressions()
    case_7_next_tests()
    final_interpretation()

    # Final group-level summary claims
    ns.record_claim(ClaimRecord(
        claim_id="g15_J_V_unresolved_final",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.SUMMARY_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        statement=(
            "Group 15 did not derive a field equation. J_V as a physical flux/transport "
            "current remains undefined. Exchange continuity nabla_mu J_V^mu = Sigma_V - R_V "
            "remains a theorem target."
        ),
        obligation_ids=[
            "derive_J_V_physical_flux_law_in_15",
            "derive_Sigma_V_operator_in_15",
            "derive_R_V_operator_in_15",
            "derive_exchange_continuity_law_in_15",
        ],
    ))
    ns.record_claim(ClaimRecord(
        claim_id="g15_residual_kill_working_boundary",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.SUMMARY_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement=(
            "Group 15 established the working boundary: J_V-driven zeta may enter ordinary "
            "metric trace only through B_s, with residual zeta/kappa metric trace killed or "
            "non-metric, unless O is later derived. This is provisional."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="g15_no_overlap_O_unresolved_final",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.SUMMARY_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        statement=(
            "O[B_s, zeta_residual/kappa_residual, J_V] = 0 remains unresolved. "
            "Count-once recombination is the central missing theorem carried out of Group 15."
        ),
        obligation_ids=[
            "derive_no_overlap_operator_or_residual_kill_in_15",
            "derive_residual_kill_theorem_or_parent_identity_in_15",
        ],
    ))
    ns.record_claim(ClaimRecord(
        claim_id="g15_policy_no_regression_list",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Group 15 rejected regressions must be preserved in all downstream groups: "
            "no treating residual-kill as derived; no J_V without flux law; no continuity "
            "as current definition; no zeta in both B_s and residual trace; no kappa "
            "restoring killed trace; no recovery checks choosing residual status."
        ),
    ))
    # HandoffImportRecord for Group 16 - the final group handoff
    ns.record_handoff_import(HandoffImportRecord(
        handoff_id="group_16_handoff_from_15",
        script_id=SCRIPT_ID,
        imported_as=RecordKind.SUMMARY_CLAIM,
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        imported_record_refs=[
            "claim:g15_J_V_unresolved_final",
            "claim:g15_residual_kill_working_boundary",
            "claim:g15_no_overlap_O_unresolved_final",
            "claim:g15_policy_no_regression_list",
            "obligation:derive_J_V_physical_flux_law_in_15",
            "obligation:derive_exchange_continuity_law_in_15",
            "obligation:derive_no_overlap_operator_or_residual_kill_in_15",
            "obligation:derive_boundary_neutrality_theorem_in_15",
            "obligation:derive_static_source_neutrality_theorem_in_15",
            "obligation:derive_J_V_timelike_domain_theorem_in_15",
            "obligation:derive_residual_kill_theorem_or_parent_identity_in_15",
            "obligation:derive_Sigma_V_operator_in_15",
            "obligation:derive_R_V_operator_in_15",
            "route:g15c_residual_kill_provisional_convention",
            "route:no4_residual_kill_safe_route",
            "route:bo6_B_s_only_metric_insertion_candidate_route",
        ],
        description=(
            "What Group 16 may import from Group 15: the J_V/exchange-continuity unresolved "
            "status, the residual-kill provisional convention as the working boundary for "
            "ordinary metric entry, the no-overlap bottleneck, all Group 15 open proof "
            "obligations, and the Group 15 rejection list. Group 16 must not treat any of "
            "these as resolved without new derivation."
        ),
    ))
    ns.record_derivation(
        derivation_id="group_15_status_after_residual_kill_marker",
        inputs=[],
        output=sp.Symbol("group_15_status_after_residual_kill_audited"),
        method="group_15_status_after_residual_kill_audit",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
