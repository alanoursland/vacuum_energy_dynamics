# Group:
#   15_vacuum_current_and_exchange_continuity
#
# Script type:
#   INVENTORY
#
# Candidate static-source neutrality for J_V
#
# Purpose
# -------
# The timelike-domain script found:
#
#   u_vac = J_V / sqrt(-J_V^2)
#
# can only be defined on a domain where:
#
#   J_V^2 < 0
#   J_V != 0
#
# It also found that zero-flux equilibrium may protect neutrality but cannot
# define u_vac from J_V.
#
# The next ordinary-sector gate is static-source neutrality:
#
#   Does candidate J_V / Sigma_V / R_V structure create exterior scalar charge
#   around ordinary static sources?
#
# This script inventories static-source neutrality conditions.
#
# It is not a derivation of J_V.

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
class StaticNeutralityEntry:
    name: str
    neutrality_test: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def build_entries() -> List[StaticNeutralityEntry]:
    return [
        StaticNeutralityEntry(
            name="SN1: static-source neutrality target",
            neutrality_test="ordinary static sources create no independent exterior J_V/zeta/kappa scalar charge",
            role="core ordinary-sector safety condition for exchange continuity",
            allowed_if="static equilibrium has zero net volume charge, zero far-zone scalar flux, and no M_ext shift",
            forbidden_if="static mass creates exterior scalar volume tail",
            status="THEOREM_TARGET",
            missing="static neutrality theorem",
            consequence="decides whether J_V/Sigma/R can survive ordinary static gravity",
        ),
        StaticNeutralityEntry(
            name="SN2: static zero-current equilibrium",
            neutrality_test="J_V = 0 in static equilibrium with no exterior flux",
            role="strongest neutral static branch",
            allowed_if="u_vac is not required from J_V in the static region or has separate equilibrium fallback",
            forbidden_if="J_V=0 is normalized to define u_vac",
            status="SAFE_IF",
            missing="equilibrium-frame fallback if frame is needed",
            consequence="protects neutrality but does not define current-based u_vac",
        ),
        StaticNeutralityEntry(
            name="SN3: pointwise Sigma/R balance",
            neutrality_test="Sigma_V = R_V pointwise in static equilibrium",
            role="local no-net-source branch",
            allowed_if="balance follows from equilibrium law, not tuning",
            forbidden_if="R_V is chosen to cancel Sigma_V by hand",
            status="CANDIDATE",
            missing="equilibrium balance law and sign convention",
            consequence="can prevent static volume charge if not decorative",
        ),
        StaticNeutralityEntry(
            name="SN4: compact-support current",
            neutrality_test="J_V nonzero only inside source/interior, with zero boundary flux",
            role="interior redistribution branch",
            allowed_if="support theorem and boundary flux cancellation are explicit",
            forbidden_if="compactness is imposed after seeing exterior charge",
            status="CANDIDATE",
            missing="support law and interior flux direction",
            consequence="may allow internal exchange without exterior scalar charge",
        ),
        StaticNeutralityEntry(
            name="SN5: zeta-gradient static risk",
            neutrality_test="J_V ~ -D_z grad zeta around static source",
            role="danger check for zeta-gradient flux",
            allowed_if="grad zeta has compact support or no exterior scalar tail",
            forbidden_if="static zeta gradient produces 1/r-like exterior charge",
            status="RISK",
            missing="zeta boundary theorem",
            consequence="likely rejects unrestricted zeta-gradient current in ordinary static gravity",
        ),
        StaticNeutralityEntry(
            name="SN6: source-gradient static risk",
            neutrality_test="J_V follows source/support gradient near static matter boundary",
            role="danger check for source-gradient flux",
            allowed_if="boundary smoothing creates no M_ext shift and no scalar tail",
            forbidden_if="source boundary becomes scalar shell charge",
            status="RISK",
            missing="shell-source avoidance theorem",
            consequence="can become boundary repair or shell source if uncontrolled",
        ),
        StaticNeutralityEntry(
            name="SN7: acceleration-gradient static safety",
            neutrality_test="Sigma_V ~ chi rho a^mu nabla_mu A is zero or neutral for static equilibrium",
            role="static safety test for inherited source candidate",
            allowed_if="supported/static acceleration does not create independent scalar volume charge",
            forbidden_if="static support acceleration sources exterior zeta/kappa field",
            status="RISK",
            missing="static support / acceleration interpretation",
            consequence="may kill acceleration-gradient source in ordinary static branch if unsafe",
        ),
        StaticNeutralityEntry(
            name="SN8: exterior scalar charge rejection",
            neutrality_test="Q_V = integral_static (Sigma_V - R_V) with boundary terms gives no exterior scalar charge",
            role="forbidden outcome guard",
            allowed_if="Q_V = 0 by structure, not tuning",
            forbidden_if="Q_V != 0 or is canceled by fitted R_V",
            status="REQUIRED",
            missing="definition of Q_V and proof of zero charge",
            consequence="kills any static law that makes independent scalar gravity",
        ),
        StaticNeutralityEntry(
            name="SN9: no far-zone scalar flux",
            neutrality_test="F_scalar_far[J_V,zeta,kappa] = 0 for ordinary static sources",
            role="ordinary-sector radiation/exterior guard",
            allowed_if="far-zone scalar flux vanishes structurally",
            forbidden_if="static source leaks scalar volume flux",
            status="REQUIRED",
            missing="far-zone flux theorem",
            consequence="prevents J_V from becoming observable scalar field",
        ),
        StaticNeutralityEntry(
            name="SN10: no exterior mass shift",
            neutrality_test="delta M_ext|volume = 0 for static volume exchange",
            role="A-sector mass protection",
            allowed_if="volume exchange recombines without changing A-sector exterior mass",
            forbidden_if="J_V/Sigma/R changes measured exterior mass independently",
            status="REQUIRED",
            missing="mass-accounting theorem",
            consequence="kills current laws that alter A-sector mass",
        ),
        StaticNeutralityEntry(
            name="SN11: no-overlap / residual-kill",
            neutrality_test="static J_V-driven zeta enters metric only through B_s, or residual trace killed/non-metric",
            role="count-once recombination guard",
            allowed_if="static no-overlap theorem is explicit",
            forbidden_if="static volume exchange creates independent residual metric trace",
            status="REQUIRED",
            missing="static no-overlap theorem",
            consequence="prevents static current from reviving zeta/kappa scalar duplicate",
        ),
        StaticNeutralityEntry(
            name="SN12: R_V cancellation patch rejection",
            neutrality_test="R_V tuned to cancel static exterior charge",
            role="rejected shortcut",
            allowed_if="only as no-go diagnostic",
            forbidden_if="accepted as neutrality mechanism",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents relaxation from becoming scalar-charge eraser",
        ),
        StaticNeutralityEntry(
            name="SN13: recovery downstream",
            neutrality_test="gamma_like and AB checked only after static neutrality is structural",
            role="ordinary-regime recovery target",
            allowed_if="checked after neutrality is established",
            forbidden_if="used to tune static balance",
            status="RECOVERY_TARGET",
            missing="solutions after static-neutral law",
            consequence="keeps recovery from selecting neutrality mechanism",
        ),
        StaticNeutralityEntry(
            name="SN14: static neutrality failure",
            neutrality_test="candidate J_V/Sigma/R produces exterior scalar charge around static sources",
            role="branch-kill condition",
            allowed_if="used to reject unsafe current family",
            forbidden_if="patched by R_V tuning or boundary repair",
            status="BRANCH_KILLED",
            missing="only applies if charge is demonstrated",
            consequence="unsafe current family cannot support ordinary gravity",
        ),
        StaticNeutralityEntry(
            name="SN15: recommended next move",
            neutrality_test="if static neutrality survives, test boundary/no-overlap for volume current",
            role="best next bottleneck",
            allowed_if="neutrality is structural or reduced to clear theorem target",
            forbidden_if="jumping to boundary/no-overlap while scalar charge remains unresolved",
            status="RECOMMENDED",
            missing="boundary/no-overlap current test",
            consequence="next script should test whether the current double-counts B_s/residual trace or leaks through boundary",
        ),
    ]


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="timelike_domain_for_volume_current_marker",
        upstream_script_id="015_vacuum_current_and_exchange_continuity__candidate_timelike_domain_for_volume_current",
        upstream_derivation_id="timelike_domain_for_volume_current_marker",
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


def print_entry(e: StaticNeutralityEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Neutrality test: {e.neutrality_test}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    print(f"Status: {e.status}")
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: Static-source neutrality problem")

    print("Question:")
    print()
    print("  Does the proposed J_V / Sigma_V / R_V structure create exterior scalar charge around static sources?")
    print()
    print("Goal:")
    print()
    print("  protect ordinary static gravity from scalar volume charge")
    print()
    print("Discipline:")
    print()
    print("  do not allow static mass to create independent zeta/kappa exterior charge")
    print("  do not use R_V as scalar-charge cancellation patch")
    print("  do not let J_V alter M_ext independently of A-sector")
    print("  preserve no far-zone scalar flux")
    print("  preserve no-overlap / residual-kill")
    print("  keep gamma/AB recovery downstream")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("static-source neutrality problem posed", StatusMark.OBLIGATION, "requires static neutrality theorem")


def case_1_inventory(entries: List[StaticNeutralityEntry]):
    header("Case 1: Static-source neutrality inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[StaticNeutralityEntry]):
    header("Case 2: Compact static-neutrality ledger")

    print("| Entry | Neutrality test | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.neutrality_test.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("compact static-neutrality ledger produced", StatusMark.INFO, "inventory only")


def case_3_status_counts(entries: List[StaticNeutralityEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Static zero-current equilibrium is safe if u_vac is not required from J_V there.")
    print("  Pointwise Sigma/R balance and compact-support current are candidate safety routes.")
    print("  Zeta-gradient, source-gradient, and acceleration-gradient branches are risky in static ordinary gravity.")
    print("  No exterior scalar charge, no far-zone scalar flux, no M_ext shift, and no-overlap are mandatory.")
    print("  If static neutrality survives, boundary/no-overlap becomes the next gate.")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("static-neutrality status count produced", StatusMark.INFO, "inventory only")


def case_4_static_decision_tree():
    header("Case 4: Static-neutrality decision tree")

    print("Decision tree:")
    print()
    print("1. Static zero-current equilibrium:")
    print("   safest for exterior neutrality, but cannot define u_vac from J_V.")
    print()
    print("2. Pointwise Sigma/R balance:")
    print("   candidate if balance follows from equilibrium law, not tuning.")
    print()
    print("3. Compact-support current:")
    print("   candidate if boundary flux is structurally zero.")
    print()
    print("4. Gradient currents around static sources:")
    print("   risky because exterior gradients can create scalar tails.")
    print()
    print("5. R_V cancellation:")
    print("   rejected if used to erase scalar charge after the fact.")
    print()
    print("6. If exterior scalar charge appears:")
    print("   branch killed for ordinary static gravity.")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("static-neutrality decision tree stated", StatusMark.INFO, "decision tree recorded")


def case_5_good_failure():
    header("Case 5: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  a candidate J_V / Sigma_V / R_V family produces exterior scalar charge")
    print("  around ordinary static sources.")
    print()
    print("Consequence:")
    print()
    print("  reject that current family for ordinary gravity.")
    print("  Do not patch with R_V tuning or boundary repair.")
    print()
    print("Bad failure:")
    print("  allow static scalar charge and hope recovery checks hide it.")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("static-neutrality good failure stated", StatusMark.DEFER, "deferred pending static neutrality theorem")


def case_6_failure_controls():
    header("Case 6: Failure controls")

    print("Static-source neutrality fails if:")
    print()
    print("1. static mass creates independent zeta/kappa exterior charge")
    print("2. R_V is tuned to cancel that charge")
    print("3. source-gradient creates shell scalar charge at boundary")
    print("4. zeta-gradient current produces far-zone scalar tail")
    print("5. acceleration-gradient source treats static support as scalar source without neutrality theorem")
    print("6. J_V changes M_ext independently of A-sector")
    print("7. static current creates residual metric trace outside B_s")
    print("8. gamma_like or AB is used to select neutrality mechanism")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("static-neutrality failure controls stated", StatusMark.INFO, "guardrails recorded")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_static_source_neutrality_for_J_V.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_boundary_no_overlap_for_volume_current.py")
    print("   Test boundary neutrality and no-overlap for surviving current families.")
    print()
    print("3. candidate_static_neutrality_failure_summary.py")
    print("   Use if static scalar charge kills current families.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_boundary_no_overlap_for_volume_current.py")
    print()
    print("Reason:")
    print("  If ordinary static neutrality survives, the next gate is whether J_V-driven zeta leaks through the boundary or double-counts B_s/residual trace.")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("next test selected", StatusMark.INFO, "candidate_boundary_no_overlap_for_volume_current.py")


def final_interpretation():
    header("Final interpretation")

    print("Static-source neutrality is mandatory for ordinary gravity.")
    print()
    print("Best current interpretation:")
    print()
    print("  static zero-current or compact/balanced exchange may be safe,")
    print("  but any exterior scalar charge kills the current family.")
    print()
    print("Best next test:")
    print("  candidate_boundary_no_overlap_for_volume_current.py")


def main():
    header("Candidate Static-Source Neutrality For J_V")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_static_decision_tree()
    case_5_good_failure()
    case_6_failure_controls()
    case_7_next_tests()
    final_interpretation()

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_static_source_neutrality_theorem_in_15",
        script_id=SCRIPT_ID,
        title="Derive static-source neutrality theorem for J_V/Sigma/R",
        status=ObligationStatus.OPEN,
        description=(
            "Show that the candidate J_V/Sigma_V/R_V structure creates no exterior scalar "
            "volume charge, no far-zone scalar flux, and no M_ext shift for ordinary static "
            "sources. Q_V = 0 must hold by structure, not by R_V tuning."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="sn8_exterior_scalar_charge_mandatory_zero",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Q_V (net volume charge around static source) must be zero by structure. "
            "Any static law that makes independent exterior scalar gravity is rejected."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="sn12_R_V_cancellation_patch_rejected",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "R_V tuned to cancel static exterior scalar charge is rejected as a neutrality "
            "mechanism. Relaxation cannot serve as a scalar-charge eraser."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="sn13_recovery_downstream_static_neutrality",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "gamma_like and AB recovery tests must be performed only after static neutrality "
            "is structural; they must not be used to tune the static balance."
        ),
    ))
    ns.record_route(RouteRecord(
        route_id="sn2_static_zero_current_safe_route",
        script_id=SCRIPT_ID,
        name="Static zero-current equilibrium (J_V = 0 in static region)",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=["derive_static_source_neutrality_theorem_in_15"],
        activation_conditions=[
            "J_V = 0 in static equilibrium with no exterior flux",
            "u_vac is not required from J_V in the static region",
            "separate equilibrium-frame fallback exists if frame is needed",
        ],
    ))
    # SN14 is a BRANCH_KILLED entry but only "applies if charge is demonstrated".
    # No exterior scalar charge has been demonstrated yet, so this is recorded
    # as a conditional deferred branch, not a kill.
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_static_neutrality_unsafe_current_branch",
        script_id=SCRIPT_ID,
        branch_id="J_V_Sigma_R_static_neutrality_check",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=["derive_static_source_neutrality_theorem_in_15"],
        description=(
            "Static neutrality has not been demonstrated. Current families that produce "
            "exterior scalar charge around ordinary static sources will be killed. "
            "The branch is deferred pending the static neutrality theorem."
        ),
    ))
    ns.record_derivation(
        derivation_id="static_source_neutrality_for_J_V_marker",
        inputs=[],
        output=sp.Symbol("static_source_neutrality_for_J_V_audited"),
        method="static_source_neutrality_for_J_V_audit",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
