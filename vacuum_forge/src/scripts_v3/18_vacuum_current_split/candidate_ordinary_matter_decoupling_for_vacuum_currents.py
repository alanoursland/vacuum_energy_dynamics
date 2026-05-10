# Candidate ordinary matter decoupling for vacuum currents
#
# Group:
#   18_vacuum_current_split
#
# Script type:
#   AUDIT
#
# Purpose
# -------
# The J_exch definition requirements audit found:
#
#   J_exch is not defined yet.
#
# It survives only as a theorem target requiring:
#
#   source side,
#   relaxation side,
#   Sigma/R distinction,
#   divergence/balance role,
#   domain,
#   direction,
#   boundary behavior,
#   ordinary matter decoupling,
#   mass neutrality,
#   scalar trace guard.
#
# Rejected:
#
#   boundary repair,
#   recovery repair,
#   matter repair,
#   e_curv source reservoir,
#   H_exch shortcut.
#
# This script audits whether J_sub/J_exch avoid changing ordinary matter coupling.
#
# Locked-door question:
#
#   Can J_sub and J_exch avoid changing ordinary matter coupling?
#
# This is a decoupling audit, not a current definition.


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
class MatterDecouplingEntry:
    name: str
    decoupling_rule: str
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
        dependency_id="J_exch_definition_requirements_marker",
        upstream_script_id="18_vacuum_current_split__candidate_J_exch_definition_requirements",
        upstream_derivation_id="J_exch_definition_requirements_marker",
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


def build_entries() -> List[MatterDecouplingEntry]:
    return [
        MatterDecouplingEntry(
            name="OM1: ordinary matter decoupling target",
            decoupling_rule="J_sub and J_exch do not change ordinary matter coupling or source routing",
            role="core ordinary-sector safety theorem target",
            allowed_if="decoupling follows structurally before current split is used",
            forbidden_if="vacuum currents reroute matter to fix curvature, boundary, or recovery problems",
            status="THEOREM_TARGET",
            missing="ordinary matter decoupling theorem",
            consequence="decides whether vacuum-current split is safe for ordinary sector",
        ),
        MatterDecouplingEntry(
            name="OM2: rho routes to A-sector",
            decoupling_rule="ordinary rho / scalar charge remains routed to A-sector",
            role="A-sector protection rule",
            allowed_if="vacuum currents do not replace or supplement ordinary mass source",
            forbidden_if="J_sub/J_exch alter scalar charge sourcing",
            status="REQUIRED",
            missing="source-routing theorem",
            consequence="protects strongest reduced A-sector result",
        ),
        MatterDecouplingEntry(
            name="OM3: no T_mu_nu double-count",
            decoupling_rule="ordinary T_mu_nu is not counted again in J_sub, J_exch, Sigma_exch, or R_exch",
            role="source accounting guard",
            allowed_if="matter source and vacuum-current source are distinct",
            forbidden_if="ordinary matter appears twice under different names",
            status="REQUIRED",
            missing="source separation theorem",
            consequence="prevents hidden strengthening/tuning of matter source",
        ),
        MatterDecouplingEntry(
            name="OM4: J_sub matter silence",
            decoupling_rule="J_sub does not push, drag, accelerate, or otherwise couple to ordinary matter",
            role="pure wind matter guard",
            allowed_if="J_sub remains neutral substrate flow",
            forbidden_if="pure wind becomes fifth-force-like matter coupling",
            status="REQUIRED",
            missing="J_sub matter decoupling theorem",
            consequence="preserves pure wind neutrality",
        ),
        MatterDecouplingEntry(
            name="OM5: J_exch no matter repair",
            decoupling_rule="J_exch does not reroute ordinary matter to fix curvature, boundary, or exchange failure",
            role="active exchange matter guard",
            allowed_if="J_exch source side is independent of ordinary matter unless theorem derives coupling",
            forbidden_if="exchange current solves problems by changing matter coupling",
            status="REQUIRED",
            missing="J_exch matter decoupling theorem",
            consequence="prevents matter-sector repair behavior",
        ),
        MatterDecouplingEntry(
            name="OM6: no fifth-force-like coupling",
            decoupling_rule="vacuum currents do not produce new ordinary force channel without theorem",
            role="phenomenology guard",
            allowed_if="ordinary matter equations remain unchanged",
            forbidden_if="J_sub/J_exch generate force on matter by existence",
            status="REQUIRED",
            missing="force-decoupling theorem",
            consequence="prevents hidden preferred-frame or exchange force",
        ),
        MatterDecouplingEntry(
            name="OM7: no hidden scalar charge",
            decoupling_rule="vacuum currents do not create ordinary scalar charge through B_s/zeta/kappa",
            role="scalar-sector guard",
            allowed_if="B_s/F_zeta and residual trace remain closed",
            forbidden_if="matter feels vacuum current through hidden scalar trace",
            status="REQUIRED",
            missing="scalar charge neutrality theorem",
            consequence="preserves Group 16 guardrails",
        ),
        MatterDecouplingEntry(
            name="OM8: no M_ext shift independent of A",
            decoupling_rule="vacuum currents do not shift exterior mass independently of A-sector",
            role="mass neutrality guard",
            allowed_if="any mass effect is derived through A-sector source law",
            forbidden_if="J_sub/J_exch alter measured exterior mass directly",
            status="REQUIRED",
            missing="mass neutrality theorem",
            consequence="protects ordinary exterior sector",
        ),
        MatterDecouplingEntry(
            name="OM9: no boundary matter repair",
            decoupling_rule="vacuum currents do not modify matter behavior at boundary to avoid shell/source/leakage",
            role="boundary/matter guard",
            allowed_if="boundary behavior is structural and matter-independent",
            forbidden_if="matter coupling is adjusted at boundary",
            status="REQUIRED",
            missing="boundary matter decoupling theorem",
            consequence="prevents boundary repair via matter coupling",
        ),
        MatterDecouplingEntry(
            name="OM10: no recovery-tuned matter coupling",
            decoupling_rule="ordinary matter coupling is not adjusted to pass gamma_like, AB, or exterior matching",
            role="anti-smuggling guard",
            allowed_if="recovery remains downstream",
            forbidden_if="vacuum-current matter coupling is selected by recovery behavior",
            status="REQUIRED",
            missing="not a mechanism",
            consequence="keeps recovery downstream",
        ),
        MatterDecouplingEntry(
            name="OM11: matter-induced exchange branch",
            decoupling_rule="ordinary matter may source J_exch only if explicit theorem derives it",
            role="high-risk candidate",
            allowed_if="source theorem exists and no double-counting occurs",
            forbidden_if="ordinary matter is used as exchange source by convenience",
            status="RISK",
            missing="matter-to-exchange source theorem",
            consequence="possible future branch but unsafe now",
        ),
        MatterDecouplingEntry(
            name="OM12: zero-net ordinary exchange",
            decoupling_rule="ordinary sector may require Sigma_exch - R_exch = 0",
            role="ordinary-sector neutral branch",
            allowed_if="matter coupling remains unchanged and curvature arises by warping/constraint or balanced exchange",
            forbidden_if="zero-net branch still uses matter to drive net exchange",
            status="CANDIDATE",
            missing="ordinary-sector zero-net theorem",
            consequence="keeps ordinary matter decoupled from net exchange",
        ),
        MatterDecouplingEntry(
            name="OM13: zero-creation ordinary branch",
            decoupling_rule="ordinary sector may require Sigma_exch = R_exch = 0",
            role="strong ordinary-sector neutrality branch",
            allowed_if="J_exch inactive for ordinary matter",
            forbidden_if="creation/destruction language remains active ordinary source",
            status="CANDIDATE",
            missing="ordinary-sector zero-creation theorem",
            consequence="cleanest decoupling branch",
        ),
        MatterDecouplingEntry(
            name="OM14: dark-sector separation",
            decoupling_rule="dark-sector coupling remains optional and separated from ordinary matter",
            role="future optional branch guard",
            allowed_if="dark coupling does not patch ordinary-sector failure",
            forbidden_if="dark sector used to explain ordinary matter coupling leak",
            status="DEFER",
            missing="dark-sector coupling rule",
            consequence="keeps speculative coupling downstream",
        ),
        MatterDecouplingEntry(
            name="OM15: J_sub matter coupling rejection",
            decoupling_rule="J_sub directly pushes or drags ordinary matter",
            role="forbidden pure-wind matter branch",
            allowed_if="never under pure wind neutrality",
            forbidden_if="accepted as substrate-current behavior",
            status="REJECTED",
            missing="not pursued",
            consequence="preserves pure wind neutrality",
        ),
        MatterDecouplingEntry(
            name="OM16: J_exch matter repair rejection",
            decoupling_rule="J_exch reroutes matter to fix curvature, boundary, or recovery behavior",
            role="forbidden exchange repair branch",
            allowed_if="never without source theorem",
            forbidden_if="accepted as exchange coupling",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents matter repair",
        ),
        MatterDecouplingEntry(
            name="OM17: ordinary T as Sigma_exch by fiat rejection",
            decoupling_rule="Sigma_exch = function(T_mu_nu) by convenience",
            role="forbidden source shortcut",
            allowed_if="never without derivation",
            forbidden_if="accepted as source side",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents matter double-counting",
        ),
        MatterDecouplingEntry(
            name="OM18: scalar charge leak rejection",
            decoupling_rule="vacuum current creates ordinary scalar charge through hidden B_s/zeta channel",
            role="forbidden scalar coupling branch",
            allowed_if="never without insertion theorem",
            forbidden_if="accepted as matter coupling",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents hidden scalar fifth force",
        ),
        MatterDecouplingEntry(
            name="OM19: decoupling failure",
            decoupling_rule="J_sub/J_exch cannot avoid changing ordinary matter coupling",
            role="branch failure condition",
            allowed_if="used to reject ordinary-sector vacuum-current split",
            forbidden_if="patched with dark sector, recovery, or source relabeling",
            status="BRANCH_KILLED",
            missing="applies if failure demonstrated",
            consequence="vacuum current split cannot enter ordinary matter sector",
        ),
        MatterDecouplingEntry(
            name="OM20: recommended next move",
            decoupling_rule="after ordinary matter decoupling, inventory possible J_exch source sides",
            role="next local bottleneck",
            allowed_if="decoupling remains theorem target and guards are clear",
            forbidden_if="source inventory before decoupling guard",
            status="RECOMMENDED",
            missing="exchange source-side inventory",
            consequence="next script should be candidate_exchange_current_source_side_inventory.py",
        ),
    ]


def print_entry(e: MatterDecouplingEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Decoupling rule: {e.decoupling_rule}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: Ordinary matter decoupling problem")

    print("Question:")
    print()
    print("  Can J_sub and J_exch avoid changing ordinary matter coupling?")
    print()
    print("Goal:")
    print()
    print("  prevent vacuum-current split from becoming ordinary matter repair mechanism")
    print()
    print("Discipline:")
    print()
    print("  rho/scalar charge stays routed to A-sector")
    print("  no T_mu_nu double-count")
    print("  J_sub does not push ordinary matter")
    print("  J_exch does not reroute matter")
    print("  no fifth-force-like coupling")
    print("  no hidden scalar charge")
    print("  no M_ext shift independent of A")
    print("  dark-sector coupling remains optional and separated")

    status_line("ordinary matter decoupling problem posed", "REQUIRED")


def case_1_inventory(entries: List[MatterDecouplingEntry]):
    header("Case 1: Ordinary matter decoupling inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[MatterDecouplingEntry]):
    header("Case 2: Compact ordinary matter decoupling ledger")

    print("| Entry | Decoupling rule | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.decoupling_rule.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    status_line("compact ordinary matter decoupling ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[MatterDecouplingEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Ordinary matter decoupling is required but not derived.")
    print("  rho/scalar charge must remain routed to A-sector.")
    print("  J_sub cannot push matter; J_exch cannot reroute matter.")
    print("  No fifth force, hidden scalar charge, M_ext shift, boundary matter repair, or recovery-tuned coupling is allowed.")
    print("  Zero-net and zero-creation ordinary-sector branches remain the safest current-compatible branches.")
    print("  Next gate is J_exch source-side inventory.")

    status_line("ordinary matter decoupling status count produced", "STRUCTURAL")


def case_4_decoupling_rules():
    header("Case 4: Required decoupling rules")

    print("Required decoupling rules:")
    print()
    print("1. rho / scalar charge routes to A-sector")
    print("2. ordinary T_mu_nu is not double-counted")
    print("3. J_sub does not push ordinary matter")
    print("4. J_exch does not reroute ordinary matter")
    print("5. no fifth-force-like coupling")
    print("6. no hidden scalar charge")
    print("7. no M_ext shift independent of A")
    print("8. no boundary matter repair")
    print("9. no recovery-tuned matter coupling")
    print("10. dark-sector branch remains optional and separated")

    status_line("ordinary matter decoupling rules listed", "RECOMMENDED")


def case_5_decision_tree():
    header("Case 5: Ordinary matter decoupling decision tree")

    print("Decision tree:")
    print()
    print("1. Ordinary matter stays routed to A-sector:")
    print("   decoupling theorem target survives.")
    print()
    print("2. J_sub pushes matter:")
    print("   pure wind branch rejected.")
    print()
    print("3. J_exch reroutes matter:")
    print("   exchange branch rejected unless explicit theorem exists.")
    print()
    print("4. Matter appears inside Sigma_exch by convenience:")
    print("   rejected as double-counting.")
    print()
    print("5. Hidden scalar charge appears:")
    print("   rejected unless B_s/F_zeta insertion theorem exists.")
    print()
    print("6. Ordinary sector remains zero-net/zero-creation:")
    print("   safest branch.")
    print()
    print("7. Dark-sector coupling appears:")
    print("   defer and keep separated.")

    status_line("ordinary matter decoupling decision tree stated", "RECOMMENDED")


def case_6_good_failure():
    header("Case 6: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  vacuum-current split cannot decouple from ordinary matter.")
    print()
    print("Consequence:")
    print()
    print("  do not use J_sub/J_exch in ordinary matter sector.")
    print("  preserve zero-net/zero-creation ordinary-sector branch.")
    print()
    print("Bad failure:")
    print()
    print("  hide ordinary matter coupling inside Sigma_exch or dark-sector language.")

    status_line("ordinary matter decoupling good failure stated", "DEFER")


def case_7_failure_controls():
    header("Case 7: Failure controls")

    print("Ordinary matter decoupling fails if:")
    print()
    print("1. rho does not route to A-sector")
    print("2. T_mu_nu is double-counted")
    print("3. J_sub pushes matter")
    print("4. J_exch reroutes matter")
    print("5. fifth-force-like coupling appears")
    print("6. hidden scalar charge appears")
    print("7. M_ext shifts independently of A")
    print("8. boundary matter repair appears")
    print("9. recovery tunes matter coupling")
    print("10. dark sector patches ordinary failure")
    print("11. Sigma_exch is defined from ordinary T by convenience")

    status_line("ordinary matter decoupling failure controls stated", "RISK")


def case_8_next_tests():
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_ordinary_matter_decoupling_for_vacuum_currents.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_exchange_current_source_side_inventory.py")
    print("   Inventory possible source sides for J_exch.")
    print()
    print("3. candidate_matter_decoupling_failure_summary.py")
    print("   Use if decoupling fails.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_exchange_current_source_side_inventory.py")
    print()
    print("Reason:")
    print("  With ordinary matter decoupling fenced, the next question is what source side")
    print("  could make J_exch real without ordinary-sector repair.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("Ordinary matter decoupling is required but not derived.")
    print()
    print("Required:")
    print()
    print("  rho/scalar charge stays in A-sector")
    print("  no T_mu_nu double-count")
    print("  J_sub does not push matter")
    print("  J_exch does not reroute matter")
    print("  no fifth-force-like coupling")
    print("  no hidden scalar charge")
    print("  no M_ext shift independent of A")
    print()
    print("Safest ordinary-sector branches:")
    print()
    print("  zero-net exchange")
    print("  zero creation")
    print()
    print("Best next script:")
    print()
    print("  candidate_exchange_current_source_side_inventory.py")

    status_line("ordinary matter decoupling audit complete", "CLOSED")


def main():
    header("Candidate Ordinary Matter Decoupling For Vacuum Currents")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_decoupling_rules()
    case_5_decision_tree()
    case_6_good_failure()
    case_7_failure_controls()
    case_8_next_tests()
    final_interpretation()

    with archive:
        ns.record_obligation(ProofObligationRecord(
            obligation_id="prove_rho_routes_to_A_sector_in_18_matter_decoupling",
            script_id=SCRIPT_ID,
            status=ObligationStatus.OPEN,
            statement="Ordinary rho/scalar charge must remain routed to A-sector. Vacuum currents must not replace or supplement ordinary mass source.",
        ))
        ns.record_obligation(ProofObligationRecord(
            obligation_id="prove_J_sub_matter_silence_in_18_matter_decoupling",
            script_id=SCRIPT_ID,
            status=ObligationStatus.OPEN,
            statement="J_sub matter decoupling theorem: J_sub must not push, drag, accelerate, or otherwise couple to ordinary matter.",
        ))
        ns.record_obligation(ProofObligationRecord(
            obligation_id="prove_J_exch_no_matter_repair_in_18_matter_decoupling",
            script_id=SCRIPT_ID,
            status=ObligationStatus.OPEN,
            statement="J_exch matter decoupling theorem: J_exch must not reroute ordinary matter to fix curvature, boundary, or exchange failure.",
        ))
        ns.record_claim(ClaimRecord(
            claim_id="ordinary_matter_decoupling_theorem_target_in_18",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.CANDIDATE_ROUTE,
            statement="Ordinary matter decoupling is required but not derived. Zero-net and zero-creation ordinary-sector branches remain the safest current-compatible branches.",
        ))
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id="reject_J_sub_matter_coupling_in_18_matter_decoupling",
            script_id=SCRIPT_ID,
            branch_name="J_sub_matter_coupling",
            status=GovernanceStatus.REJECTED_ROUTE,
            rationale="J_sub directly pushing or dragging ordinary matter is forbidden under pure wind neutrality.",
        ))
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id="reject_J_exch_matter_repair_in_18_matter_decoupling",
            script_id=SCRIPT_ID,
            branch_name="J_exch_matter_repair",
            status=GovernanceStatus.REJECTED_ROUTE,
            rationale="J_exch rerouting ordinary matter to fix curvature, boundary, or recovery behavior is forbidden.",
        ))
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id="reject_ordinary_T_as_Sigma_exch_in_18_matter_decoupling",
            script_id=SCRIPT_ID,
            branch_name="ordinary_T_as_Sigma_exch",
            status=GovernanceStatus.REJECTED_ROUTE,
            rationale="Sigma_exch = function(T_mu_nu) by convenience is forbidden as matter double-counting.",
        ))
        ns.record_derivation(
            derivation_id="ordinary_matter_decoupling_for_vacuum_currents_marker",
            inputs=[],
            output=sp.Symbol("ordinary_matter_decoupling_for_vacuum_currents_complete"),
            method="ordinary_matter_decoupling_for_vacuum_currents",
            status=Status.DERIVED,
        )
        ns.write_run_metadata()


if __name__ == "__main__":
    main()
