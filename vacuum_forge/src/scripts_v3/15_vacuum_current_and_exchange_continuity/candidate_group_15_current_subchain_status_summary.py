# Group:
#   15_vacuum_current_and_exchange_continuity
#
# Script type:
#   SUMMARY
#
# Candidate Group 15 current subchain status summary
#
# Purpose
# -------
# The current subchain began with the Group 14 bottleneck:
#
#   J_V / u_vac
#
# Group 15 opened the exchange-continuity route:
#
#   nabla_mu J_V^mu = Sigma_V - R_V
#
# The current subchain has now tested:
#
#   Sigma/R split,
#   flux direction,
#   timelike/nonzero domain,
#   static-source neutrality,
#   boundary/no-overlap,
#   no-overlap operator.
#
# The result is a useful status closure, not a field equation.
#
# This script summarizes the current-subchain result.
#
# It is not a new derivation.

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
class SubchainStatusEntry:
    name: str
    result: str
    status: str
    consequence: str
    handoff: str


def build_entries() -> List[SubchainStatusEntry]:
    return [
        SubchainStatusEntry(
            name="G15C-1: exchange continuity target",
            result="nabla_mu J_V^mu = Sigma_V - R_V is the right theorem target, not yet a law",
            status="THEOREM_TARGET",
            consequence="J_V requires independent flux direction and Sigma/R definitions",
            handoff="do not call continuity a current definition",
        ),
        SubchainStatusEntry(
            name="G15C-2: Sigma/R role-level split",
            result="Sigma_V is source/creation/destruction side; R_V is relaxation/reconfiguration/return side",
            status="STRUCTURAL",
            consequence="role split exists, but neither operator is derived",
            handoff="preserve SR10 double-counting guard: Sigma/R must not be two names for one tuning mechanism",
        ),
        SubchainStatusEntry(
            name="G15C-3: flux-direction result",
            result="Sigma_V - R_V supplies divergence strength, not vector direction",
            status="REQUIRED",
            consequence="J_V still needs independent physical flux / transport law",
            handoff="distinguish physical flux law from diagnostic elliptic completion and forbidden repair current",
        ),
        SubchainStatusEntry(
            name="G15C-4: candidate direction families",
            result="exchange-potential and causal transport currents remain candidates; zeta/source/relaxation gradients are risky",
            status="CANDIDATE",
            consequence="direction candidates exist but none is derived",
            handoff="causal transport must not become Box zeta or ordinary scalar radiation",
        ),
        SubchainStatusEntry(
            name="G15C-5: timelike/nonzero domain",
            result="u_vac from J_V exists only on D_V = {J_V^2 < 0, J_V != 0}",
            status="THEOREM_TARGET",
            consequence="no global u_vac follows from a domain-limited or zero current",
            handoff="separate active exchange domains from static/equilibrium domains",
        ),
        SubchainStatusEntry(
            name="G15C-6: static-source neutrality",
            result="static zero-current or compact/balanced exchange may be safe; exterior scalar charge kills the family",
            status="REQUIRED",
            consequence="ordinary static mass must not awaken a scalar volume tail",
            handoff="do not patch scalar charge with R_V tuning or boundary repair",
        ),
        SubchainStatusEntry(
            name="G15C-7: boundary neutrality",
            result="surviving current must have zero exterior flux, zero zeta/kappa charge, no far-zone scalar flux, and no M_ext shift",
            status="REQUIRED",
            consequence="volume current cannot leak into ordinary exterior scalar gravity",
            handoff="diagnostic elliptic boundary completion is not physical flux ontology",
        ),
        SubchainStatusEntry(
            name="G15C-8: no-overlap bottleneck",
            result="O[B_s, zeta_residual/kappa_residual, J_V] = 0 remains unresolved",
            status="UNRESOLVED",
            consequence="count-once recombination remains the central missing theorem",
            handoff="do not proceed to field equations with unresolved double-counting",
        ),
        SubchainStatusEntry(
            name="G15C-9: safest recombination convention",
            result="residual-kill / non-metric residual is the cleanest safe branch",
            status="SAFE_IF",
            consequence="zeta/kappa residual metric trace is demoted if J_V-driven zeta enters B_s",
            handoff="use as provisional convention only, not derivation",
        ),
        SubchainStatusEntry(
            name="G15C-10: neutral residual branch",
            result="neutral residual branch remains possible but theorem-heavy",
            status="RISK",
            consequence="requires orthogonality, boundary neutrality, no A-sector mass overlap, and no scalar charge",
            handoff="do not use neutral residual unless O is made real",
        ),
        SubchainStatusEntry(
            name="G15C-11: forbidden zeta-both branch",
            result="zeta/J_V cannot change B_s and remain independent residual metric trace",
            status="REJECTED",
            consequence="kills double-counting branch",
            handoff="preserve from Group 14 through all future recombination scripts",
        ),
        SubchainStatusEntry(
            name="G15C-12: kappa safety",
            result="kappa remains diagnostic / non-metric / separately neutral unless derived",
            status="REQUIRED",
            consequence="kappa must not restore killed zeta residual trace",
            handoff="kappa cleanup remains necessary if residual branch is reopened",
        ),
        SubchainStatusEntry(
            name="G15C-13: recovery downstream",
            result="gamma_like and AB remain recovery checks only",
            status="RECOVERY_TARGET",
            consequence="recovery cannot choose flux, domain, boundary, or overlap mechanism",
            handoff="keep recovery tests downstream of mechanism",
        ),
        SubchainStatusEntry(
            name="G15C-14: current-subchain closure",
            result="current subchain should close with J_V/O as unresolved bottleneck unless a real O or flux law is introduced",
            status="RECOMMENDED",
            consequence="prevents another loop of renamed missing mechanisms",
            handoff="next move should be either a real operator attempt or a Group 15 status update",
        ),
    ]


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="no_overlap_operator_for_volume_current_marker",
        upstream_script_id="15_vacuum_current_and_exchange_continuity__candidate_no_overlap_operator_for_volume_current",
        upstream_derivation_id="no_overlap_operator_for_volume_current_marker",
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


def print_entry(e: SubchainStatusEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Result: {e.result}")
    print(f"Status: {e.status}")
    print(f"Consequence: {e.consequence}")
    print(f"Handoff: {e.handoff}")


def case_0_problem_statement():
    header("Case 0: Current-subchain status problem")

    print("Question:")
    print()
    print("  What has the J_V current subchain actually established,")
    print("  and where should it stop?")
    print()
    print("Goal:")
    print()
    print("  summarize the J_V / exchange-continuity subchain without pretending field equations are derived")
    print()
    print("Discipline:")
    print()
    print("  do not promote theorem targets to laws")
    print("  do not hide no-overlap behind words")
    print("  do not continue mechanism-relocation loops")
    print("  preserve recovery downstream")
    print("  name the surviving bottleneck clearly")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("current-subchain status problem posed", StatusMark.OBLIGATION, "requires honest closure of J_V subchain")
    out.print()


def case_1_status_ledger(entries: List[SubchainStatusEntry]):
    header("Case 1: Current-subchain status ledger")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[SubchainStatusEntry]):
    header("Case 2: Compact current-subchain table")

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
        out.line("compact current-subchain table produced", StatusMark.INFO, "summary only")
    out.print()


def case_3_status_counts(entries: List[SubchainStatusEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  The subchain narrowed J_V but did not define it.")
    print("  It separated Sigma/R roles but did not derive Sigma_V or R_V.")
    print("  It identified flux direction, timelike domain, static neutrality, boundary neutrality, and no-overlap as gates.")
    print("  The no-overlap operator remains unresolved.")
    print("  Residual-kill / non-metric residual is the safest provisional convention.")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("current-subchain status count produced", StatusMark.INFO, "summary only")
    out.print()


def case_4_surviving_bottlenecks():
    header("Case 4: Surviving bottlenecks")

    print("Surviving bottlenecks:")
    print()
    print("1. J_V physical flux / transport law")
    print("2. Sigma_V and R_V operator definitions")
    print("3. timelike / nonzero domain for u_vac")
    print("4. static-source neutrality theorem")
    print("5. boundary neutrality theorem")
    print("6. no-overlap operator O")
    print("7. residual-kill or non-metric residual theorem")
    print("8. kappa cleanup")
    print()
    print("Most central bottleneck:")
    print()
    print("  O[B_s, zeta_residual/kappa_residual, J_V] = 0")
    print()
    print("because without count-once recombination, J_V-driven zeta cannot safely enter the ordinary metric sector.")

    out = ScriptOutput()
    with out.unresolved_obligations():
        out.line("no-overlap operator O unresolved", StatusMark.OBLIGATION, "central missing theorem for recombination safety")
        out.line("J_V physical flux law unresolved", StatusMark.OBLIGATION, "open proof obligation")
        out.line("Sigma_V operator unresolved", StatusMark.OBLIGATION, "open proof obligation")
        out.line("R_V operator unresolved", StatusMark.OBLIGATION, "open proof obligation")
    out.print()


def case_5_rejected_regressions():
    header("Case 5: Rejected regressions to preserve")

    regressions = [
        "treat div J_V = Sigma_V - R_V as definition of J_V",
        "treat Sigma_V - R_V as vector direction",
        "promote diagnostic elliptic completion to physical current",
        "use acausal repair current to cancel boundary charge",
        "tune R_V to erase static scalar charge",
        "normalize J_V where it is spacelike, null, or zero",
        "claim global u_vac from domain-limited current",
        "let static mass create exterior zeta/kappa/J_V scalar charge",
        "let J_V shift M_ext independently of A-sector",
        "let zeta enter both B_s and residual metric trace",
        "let kappa restore killed residual trace",
        "use recovery targets to choose flux/domain/boundary/overlap",
    ]

    for idx, item in enumerate(regressions, 1):
        print(f"{idx}. {item}")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("rejected regressions preserved", StatusMark.INFO, "policy rules recorded")
    out.print()


def case_6_next_options():
    header("Case 6: Next options")

    print("Option A: Close current subchain now")
    print("  candidate_group_15_current_subchain_status_summary.md")
    print("  Use if we want a durable checkpoint before trying new mechanisms.")
    print()
    print("Option B: Try residual-kill rule")
    print("  candidate_residual_kill_rule_for_volume_current.py")
    print("  Use if choosing the cleanest safe branch for further testing.")
    print()
    print("Option C: Try physical flux law")
    print("  candidate_physical_flux_law_for_J_V.py")
    print("  Use only if a concrete flux mechanism is proposed.")
    print()
    print("Recommended:")
    print("  candidate_residual_kill_rule_for_volume_current.py")
    print()
    print("Reason:")
    print("  The status summary has closed the audit. The next constructive narrow step, if continuing, is to test the cleanest safe convention: residual-kill / non-metric residual.")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("next option selected", StatusMark.INFO, "candidate_residual_kill_rule_for_volume_current.py")
    out.print()


def final_interpretation():
    header("Final interpretation")

    print("The J_V current subchain is not a failure.")
    print()
    print("It narrowed the problem to a hard bottleneck:")
    print()
    print("  define a real current and a no-overlap mechanism,")
    print("  or keep J_V-driven zeta out of the ordinary metric scalar sector.")
    print()
    print("Current best provisional convention:")
    print()
    print("  residual-kill / non-metric residual if J_V-driven zeta enters B_s.")
    print()
    print("Best next script if continuing:")
    print()
    print("  candidate_residual_kill_rule_for_volume_current.py")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("current-subchain status summary complete", StatusMark.INFO, "closed with unresolved bottleneck recorded")
    out.print()


def main():
    header("Candidate Group 15 Current Subchain Status Summary")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    entries = build_entries()
    case_1_status_ledger(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_surviving_bottlenecks()
    case_5_rejected_regressions()
    case_6_next_options()
    final_interpretation()

    with archive:
        ns.record_claim(ClaimRecord(
            claim_id="g15c_J_V_subchain_unresolved_bottleneck",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.SUMMARY_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
            statement=(
                "The J_V / exchange-continuity current subchain narrowed the problem to: "
                "J_V physical flux law, Sigma_V/R_V operators, timelike domain, static "
                "neutrality, boundary neutrality, and no-overlap operator O. None has been "
                "derived. The central missing theorem is O[B_s, zeta_residual/kappa_residual, J_V] = 0."
            ),
            obligation_ids=[
                "derive_J_V_physical_flux_law_in_15",
                "derive_Sigma_V_operator_in_15",
                "derive_R_V_operator_in_15",
                "derive_J_V_timelike_domain_theorem_in_15",
                "derive_static_source_neutrality_theorem_in_15",
                "derive_boundary_neutrality_theorem_in_15",
                "derive_no_overlap_operator_or_residual_kill_in_15",
            ],
        ))
        ns.record_claim(ClaimRecord(
            claim_id="g15c_residual_kill_provisional_convention",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.CANDIDATE_ROUTE,
            statement=(
                "Residual-kill / non-metric residual is the safest provisional count-once "
                "convention if J_V-driven zeta enters B_s. It is not derived. It is revisitable "
                "if O is later derived or if neutral residual becomes structurally safe."
            ),
        ))
        ns.record_handoff_import(HandoffImportRecord(
            handoff_id="group_15_current_subchain_handoff",
            script_id=SCRIPT_ID,
            imported_as=RecordKind.SUMMARY_CLAIM,
            status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
            imported_record_refs=[
                "claim:g15c_J_V_subchain_unresolved_bottleneck",
                "claim:g15c_residual_kill_provisional_convention",
                "obligation:derive_J_V_physical_flux_law_in_15",
                "obligation:derive_no_overlap_operator_or_residual_kill_in_15",
                "obligation:derive_boundary_neutrality_theorem_in_15",
                "obligation:derive_static_source_neutrality_theorem_in_15",
                "obligation:derive_J_V_timelike_domain_theorem_in_15",
                "route:no4_residual_kill_safe_route",
            ],
            description=(
                "What the residual-kill and final Group 15 summary scripts may import from "
                "the current subchain: the unresolved J_V/O bottleneck, the residual-kill "
                "provisional convention, and all open proof obligations."
            ),
        ))
        ns.record_derivation(
            derivation_id="group_15_current_subchain_status_summary_marker",
            inputs=[],
            output=sp.Symbol("group_15_current_subchain_status_summary_audited"),
            method="group_15_current_subchain_status_summary_audit",
            status=Status.DERIVED,
            record_kind=RecordKind.INVENTORY_MARKER,
            is_placeholder=True,
        )
        ns.write_run_metadata()


if __name__ == "__main__":
    main()
