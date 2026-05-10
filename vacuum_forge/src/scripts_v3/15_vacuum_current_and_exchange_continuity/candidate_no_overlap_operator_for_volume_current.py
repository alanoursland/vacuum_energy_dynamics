# Group:
#   15_vacuum_current_and_exchange_continuity
#
# Script type:
#   INVENTORY
#
# Candidate no-overlap operator for volume current
#
# Purpose
# -------
# The boundary/no-overlap audit found:
#
#   J_V-driven zeta is allowed only if it has no exterior leakage
#   and does not double-count B_s / residual trace.
#
# The central missing theorem is:
#
#   O[B_s, zeta_residual/kappa_residual, J_V] = 0
#
# This script inventories possible meanings of the no-overlap operator O.
#
# It is not a derivation of O.

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
class NoOverlapEntry:
    name: str
    operator_form: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def build_entries() -> List[NoOverlapEntry]:
    return [
        NoOverlapEntry(
            name="NO1: no-overlap theorem target",
            operator_form="O[B_s, zeta_residual/kappa_residual, J_V] = 0",
            role="core count-once theorem for volume-current recombination",
            allowed_if="O is derived or residual metric trace is killed",
            forbidden_if="overlap is asserted without mechanism",
            status="THEOREM_TARGET",
            missing="definition of O",
            consequence="decides whether volume current can recombine safely",
        ),
        NoOverlapEntry(
            name="NO2: orthogonality condition",
            operator_form="<B_s, zeta_residual/kappa_residual>_trace = 0",
            role="mathematical no-overlap candidate",
            allowed_if="inner product / trace pairing is defined by theory",
            forbidden_if="orthogonality is coordinate/gauge artifact",
            status="CANDIDATE",
            missing="trace pairing and domain",
            consequence="could express count-once if pairing is real",
        ),
        NoOverlapEntry(
            name="NO3: projector split",
            operator_form="P_comp zeta enters B_s, P_res zeta is non-metric or killed, P_comp P_res = 0",
            role="projector-based no-overlap candidate",
            allowed_if="projectors are explicit and not requirement bundles only",
            forbidden_if="projectors are named to hide double-counting",
            status="CANDIDATE",
            missing="P_comp, P_res, and composition law",
            consequence="natural but risks reopening projector bundle problem",
        ),
        NoOverlapEntry(
            name="NO4: residual-kill rule",
            operator_form="zeta_residual_metric = 0 and kappa_residual_metric = 0 after B_s insertion",
            role="hard no-overlap branch",
            allowed_if="residual becomes diagnostic/non-metric or belongs to P_relax only",
            forbidden_if="residual trace remains metric-active",
            status="SAFE_IF",
            missing="residual-kill theorem and accounting update",
            consequence="simplest count-once route but demotes residual zeta/kappa",
        ),
        NoOverlapEntry(
            name="NO5: metric insertion rule",
            operator_form="metric scalar trace receives J_V-driven zeta only through B_s / A_spatial channel",
            role="recombination-rule candidate",
            allowed_if="F_zeta-to-B_s map is explicit and residual metric insertion is forbidden",
            forbidden_if="same zeta variation appears again as residual trace",
            status="CANDIDATE",
            missing="F_zeta/B_s insertion law",
            consequence="keeps volume current alive only as companion source",
        ),
        NoOverlapEntry(
            name="NO6: energy/accounting no-overlap",
            operator_form="epsilon_vac_config / e_kappa do not count the same scalar response as B_s",
            role="prevents energy/accounting double-counting",
            allowed_if="configuration energy is bookkeeping or enters once through recombination",
            forbidden_if="energy terms are used as extra source reservoir",
            status="REQUIRED",
            missing="energy recombination rule",
            consequence="protects against coefficient reservoir behavior",
        ),
        NoOverlapEntry(
            name="NO7: kappa diagnostic branch",
            operator_form="kappa remains reduced diagnostic / non-metric residual unless separately derived",
            role="post-Group-14 kappa safety branch",
            allowed_if="kappa does not restore killed zeta residual trace",
            forbidden_if="kappa becomes substitute scalar metric trace",
            status="REQUIRED",
            missing="kappa cleanup theorem",
            consequence="prevents kappa from undoing residual kill",
        ),
        NoOverlapEntry(
            name="NO8: B_s-only branch",
            operator_form="Trace[g_ij^scalar] = Trace_A/B_s only, residual trace = 0",
            role="strong count-once branch",
            allowed_if="B_s/A_spatial accounts for scalar spatial trace and residual is non-metric",
            forbidden_if="residual trace is retained for metric corrections",
            status="CANDIDATE",
            missing="A_spatial/B_s derivation",
            consequence="may close zeta-residual metric branch",
        ),
        NoOverlapEntry(
            name="NO9: neutral residual branch",
            operator_form="Trace[g_ij^scalar] = Trace_B_s + Trace_residual_neutral with O=0",
            role="weaker count-once branch",
            allowed_if="residual trace is orthogonal, boundary-neutral, and not A-sector mass",
            forbidden_if="residual overlaps B_s or carries exterior charge",
            status="RISK",
            missing="orthogonality and boundary theorem",
            consequence="keeps residual alive but highest double-counting burden",
        ),
        NoOverlapEntry(
            name="NO10: forbidden overlap",
            operator_form="zeta/J_V changes B_s and also remains independent residual metric trace",
            role="rejected double-counting branch",
            allowed_if="never in ordinary branch",
            forbidden_if="accepted as recombination",
            status="REJECTED",
            missing="not pursued",
            consequence="kills branches where zeta is both companion and residual",
        ),
        NoOverlapEntry(
            name="NO11: boundary-coupled overlap risk",
            operator_form="boundary terms hide overlap by moving residual trace into surface contribution",
            role="failure mode",
            allowed_if="only as diagnostic risk",
            forbidden_if="used as no-overlap mechanism",
            status="RISK",
            missing="surface accounting theorem",
            consequence="can disguise double-counting as boundary neutrality",
        ),
        NoOverlapEntry(
            name="NO12: diagnostic elliptic overlap audit",
            operator_form="use diagnostic solve to measure overlap, not define O",
            role="diagnostic tool",
            allowed_if="clearly non-ontological",
            forbidden_if="diagnostic projection becomes physical operator",
            status="SAFE_IF",
            missing="physical no-overlap mechanism",
            consequence="useful audit but cannot derive O",
        ),
        NoOverlapEntry(
            name="NO13: recovery downstream",
            operator_form="gamma_like and AB checked only after O or residual-kill is fixed",
            role="ordinary-regime recovery target",
            allowed_if="kept downstream",
            forbidden_if="used to choose overlap split",
            status="RECOVERY_TARGET",
            missing="solutions after safe recombination",
            consequence="keeps recovery from defining O",
        ),
        NoOverlapEntry(
            name="NO14: no-overlap failure",
            operator_form="O cannot be defined and residual trace cannot be killed/non-metric",
            role="branch failure condition",
            allowed_if="used to close current subchain",
            forbidden_if="patched by relabeling residuals",
            status="BRANCH_KILLED",
            missing="applies if no safe branch survives",
            consequence="J_V-driven zeta cannot enter ordinary metric sector",
        ),
        NoOverlapEntry(
            name="NO15: recommended next move",
            operator_form="if O remains theorem target, close current subchain with unresolved no-overlap / J_V status",
            role="best next bottleneck",
            allowed_if="no explicit O is derived in this audit",
            forbidden_if="continuing into field equations with unresolved double-counting",
            status="RECOMMENDED",
            missing="current-subchain status summary",
            consequence="next script should summarize Group 15 status unless O becomes explicit",
        ),
    ]


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="boundary_no_overlap_for_volume_current_marker",
        upstream_script_id="15_vacuum_current_and_exchange_continuity__candidate_boundary_no_overlap_for_volume_current",
        upstream_derivation_id="boundary_no_overlap_for_volume_current_marker",
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


def print_entry(e: NoOverlapEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Operator form: {e.operator_form}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    print(f"Status: {e.status}")
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: No-overlap operator problem")

    print("Question:")
    print()
    print("  Can O[B_s, zeta_residual/kappa_residual, J_V] = 0 be made real,")
    print("  or must residual metric trace be killed?")
    print()
    print("Goal:")
    print()
    print("  inventory possible meanings of the no-overlap operator")
    print()
    print("Discipline:")
    print()
    print("  do not assert orthogonality without a defined pairing")
    print("  do not name projectors without action")
    print("  do not let kappa restore killed residual trace")
    print("  do not use boundary terms to hide overlap")
    print("  keep recovery downstream")
    print("  close subchain if no-overlap remains only a theorem target")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("no-overlap operator problem posed", StatusMark.OBLIGATION, "requires O derivation or residual-kill")
    out.print()


def case_1_inventory(entries: List[NoOverlapEntry]):
    header("Case 1: No-overlap operator inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[NoOverlapEntry]):
    header("Case 2: Compact no-overlap ledger")

    print("| Entry | Operator form | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.operator_form.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("compact no-overlap ledger produced", StatusMark.INFO, "inventory only")
    out.print()


def case_3_status_counts(entries: List[NoOverlapEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Several no-overlap forms can be named, but none is derived.")
    print("  Residual-kill is the cleanest safe branch.")
    print("  Neutral residual branch remains risky because it has the largest theorem burden.")
    print("  Kappa must not restore killed residual trace.")
    print("  If O is not made explicit, close the current subchain with no-overlap as unresolved bottleneck.")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("no-overlap status count produced", StatusMark.INFO, "inventory only")
    out.print()


def case_4_decision_tree():
    header("Case 4: No-overlap decision tree")

    print("Decision tree:")
    print()
    print("1. Orthogonality condition:")
    print("   possible if trace pairing is defined.")
    print()
    print("2. Projector split:")
    print("   possible if projectors become real operators, not bundles.")
    print()
    print("3. Residual-kill rule:")
    print("   cleanest safe route; demotes residual metric trace.")
    print()
    print("4. B_s-only insertion:")
    print("   allowed if F_zeta/B_s map is explicit.")
    print()
    print("5. Neutral residual:")
    print("   risky; requires orthogonality, neutrality, and no A-sector overlap.")
    print()
    print("6. If overlap persists:")
    print("   J_V-driven zeta cannot enter ordinary metric sector.")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("no-overlap decision tree stated", StatusMark.INFO, "decision tree recorded")
    out.print()


def case_5_good_failure():
    header("Case 5: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  no overlap operator can be defined, and residual zeta/kappa trace")
    print("  cannot be killed or made non-metric.")
    print()
    print("Consequence:")
    print()
    print("  J_V-driven zeta cannot enter ordinary metric scalar sector.")
    print("  Keep volume-current route as theorem target or non-metric bookkeeping only.")
    print()
    print("Bad failure:")
    print("  rename overlap as orthogonality without defining the pairing.")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("no-overlap good failure stated", StatusMark.DEFER, "deferred pending O derivation or residual-kill theorem")
    out.print()


def case_6_failure_controls():
    header("Case 6: Failure controls")

    print("No-overlap operator fails if:")
    print()
    print("1. orthogonality pairing is undefined")
    print("2. projectors are named but not operators")
    print("3. zeta enters metric through both B_s and residual trace")
    print("4. kappa restores killed residual trace")
    print("5. boundary terms hide overlap")
    print("6. energy/accounting counts same response twice")
    print("7. diagnostic projection is promoted to physical O")
    print("8. recovery checks choose overlap split")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("no-overlap failure controls stated", StatusMark.INFO, "guardrails recorded")
    out.print()


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_no_overlap_operator_for_volume_current.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_group_15_current_subchain_status_summary.py")
    print("   Summarize J_V current subchain and unresolved no-overlap/J_V bottlenecks.")
    print()
    print("3. candidate_residual_kill_rule_for_volume_current.py")
    print("   Use only if choosing the clean residual-kill branch for further testing.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_group_15_current_subchain_status_summary.py")
    print()
    print("Reason:")
    print("  If O remains a theorem target and no explicit operator is derived, the current subchain should close with no-overlap/J_V status rather than continue into field equations.")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("next test selected", StatusMark.INFO, "candidate_group_15_current_subchain_status_summary.py")
    out.print()


def final_interpretation():
    header("Final interpretation")

    print("No-overlap remains the central recombination bottleneck.")
    print()
    print("Best current interpretation:")
    print()
    print("  safest branch is residual-kill / non-metric residual.")
    print("  neutral residual remains possible but theorem-heavy.")
    print("  forbidden branch is zeta as both B_s companion and residual metric trace.")
    print()
    print("Best next test:")
    print("  candidate_group_15_current_subchain_status_summary.py")


def main():
    header("Candidate No-Overlap Operator For Volume Current")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_decision_tree()
    case_5_good_failure()
    case_6_failure_controls()
    case_7_next_tests()
    final_interpretation()

    with archive:
        ns.record_obligation(ProofObligationRecord(
            obligation_id="derive_no_overlap_operator_or_residual_kill_in_15",
            script_id=SCRIPT_ID,
            title="Derive no-overlap operator O or establish residual-kill theorem",
            status=ObligationStatus.OPEN,
            description=(
                "Either O[B_s, zeta_residual/kappa_residual, J_V] = 0 must be derived with "
                "an explicit mechanism (orthogonality pairing, projector split, or B_s-only "
                "insertion law), or residual zeta/kappa metric trace must be killed/made "
                "non-metric with a derivation or parent identity."
            ),
        ))
        ns.record_claim(ClaimRecord(
            claim_id="no10_forbidden_zeta_both_B_s_and_residual",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.POLICY_RULE,
            statement=(
                "zeta/J_V cannot simultaneously change B_s and remain as an independent residual "
                "metric trace. The double-counting branch is rejected in the ordinary sector."
            ),
        ))
        ns.record_claim(ClaimRecord(
            claim_id="no7_kappa_must_not_restore_residual_trace",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.POLICY_RULE,
            statement=(
                "kappa must remain a reduced diagnostic / non-metric residual unless separately "
                "derived. It must not restore killed zeta residual trace."
            ),
        ))
        ns.record_claim(ClaimRecord(
            claim_id="no13_recovery_downstream_no_overlap",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.POLICY_RULE,
            statement=(
                "gamma_like and AB recovery tests must be performed only after O or residual-kill "
                "is fixed; they must not be used to choose the overlap split."
            ),
        ))
        ns.record_route(RouteRecord(
            route_id="no4_residual_kill_safe_route",
            script_id=SCRIPT_ID,
            name="Residual-kill / non-metric residual (provisional count-once convention)",
            status=GovernanceStatus.CANDIDATE_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            required_obligations=["derive_no_overlap_operator_or_residual_kill_in_15"],
            activation_conditions=[
                "zeta_residual_metric = 0 after B_s insertion",
                "kappa_residual_metric = 0 or kappa remains non-metric/diagnostic",
                "residual-kill or non-metric transition is explicit",
            ],
        ))
        # NO14 branch kill applies only when demonstrated; no demonstration here.
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id="defer_no_overlap_operator_branch",
            script_id=SCRIPT_ID,
            branch_id="no_overlap_operator_O_definition",
            status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=["derive_no_overlap_operator_or_residual_kill_in_15"],
            description=(
                "The no-overlap operator O has not been derived and residual-kill has not been "
                "established from a theorem. The branch is deferred pending O derivation or "
                "residual-kill theorem."
            ),
        ))
        ns.record_derivation(
            derivation_id="no_overlap_operator_for_volume_current_marker",
            inputs=[],
            output=sp.Symbol("no_overlap_operator_for_volume_current_audited"),
            method="no_overlap_operator_for_volume_current_audit",
            status=Status.DERIVED,
            record_kind=RecordKind.INVENTORY_MARKER,
            is_placeholder=True,
        )
        ns.write_run_metadata()


if __name__ == "__main__":
    main()
