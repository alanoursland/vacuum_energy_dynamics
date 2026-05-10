# Candidate pure wind neutrality test
#
# Group:
#   18_vacuum_current_split
#
# Script type:
#   DERIVATION
#
# Purpose
# -------
# The vacuum current split inventory found:
#
#   J_V remains unresolved.
#   J_sub/J_exch split is useful as role-level bookkeeping, not operator-level law.
#   Pure wind neutrality is the central safety requirement for J_sub.
#   J_exch requires real source/relaxation sides and cannot be repair.
#   Zero-net-exchange / zero-creation branches should stay live for ordinary sector.
#
# This script tests whether a pure substrate vacuum flow can exist without
# ordinary gravitational effect.
#
# Locked-door question:
#
#   Can pure vacuum substrate flow exist without ordinary gravitational effect?
#
# Core rule:
#
#   pure wind does not gravitate merely because it flows.
#
# This is a neutrality test, not a J_sub definition.


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


@dataclass
class PureWindNeutralityEntry:
    name: str
    neutrality_rule: str
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
        dependency_id="vacuum_current_split_inventory_marker",
        upstream_script_id="18_vacuum_current_split__candidate_vacuum_current_split_inventory",
        upstream_derivation_id="vacuum_current_split_inventory_marker",
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


def build_entries() -> List[PureWindNeutralityEntry]:
    return [
        PureWindNeutralityEntry(
            name="PW1: pure wind neutrality target",
            neutrality_rule="pure substrate flow has no ordinary gravitational effect by existence alone",
            role="core J_sub safety theorem target",
            allowed_if="neutrality is structural, not imposed after force/mass leakage appears",
            forbidden_if="pure wind is treated as mass source, scalar charge, or preferred-frame force",
            status="THEOREM_TARGET",
            missing="pure wind neutrality theorem",
            consequence="decides whether J_sub can represent harmless substrate flow",
        ),
        PureWindNeutralityEntry(
            name="PW2: no divergence condition",
            neutrality_rule="nabla_mu J_sub^mu = 0 in ordinary sector",
            role="candidate substrate conservation condition",
            allowed_if="divergence-free status follows from substrate law",
            forbidden_if="imposed to cancel exchange/source leakage",
            status="CANDIDATE",
            missing="J_sub definition and divergence theorem",
            consequence="candidate route to no creation/destruction for substrate flow",
        ),
        PureWindNeutralityEntry(
            name="PW3: no exchange condition",
            neutrality_rule="Sigma_sub = R_sub = 0 for pure substrate wind",
            role="zero-creation substrate condition",
            allowed_if="pure wind is not exchange/current-source channel",
            forbidden_if="Sigma/R are hidden inside substrate flow",
            status="CANDIDATE",
            missing="Sigma_sub/R_sub definitions or absence theorem",
            consequence="separates substrate flow from active exchange",
        ),
        PureWindNeutralityEntry(
            name="PW4: no endpoints condition",
            neutrality_rule="pure wind has no sources/sinks/endpoints in ordinary domain",
            role="ordinary-domain neutrality condition",
            allowed_if="support/topology prevents source/sink behavior",
            forbidden_if="endpoints become mass, scalar charge, or boundary repair",
            status="CANDIDATE",
            missing="domain/support topology",
            consequence="prevents pure wind from becoming active exchange by endpoints",
        ),
        PureWindNeutralityEntry(
            name="PW5: no boundary flux condition",
            neutrality_rule="pure wind has zero exterior flux or purely tangential boundary flow",
            role="boundary safety condition",
            allowed_if="boundary behavior follows from substrate law",
            forbidden_if="boundary flux is chosen to hide leakage or mass shift",
            status="CANDIDATE",
            missing="boundary/support law",
            consequence="protects exterior sector from substrate-flow leakage",
        ),
        PureWindNeutralityEntry(
            name="PW6: no M_ext shift",
            neutrality_rule="delta M_ext|J_sub = 0",
            role="mass neutrality requirement",
            allowed_if="J_sub is exterior mass-neutral by structure",
            forbidden_if="pure wind changes measured exterior mass",
            status="REQUIRED",
            missing="mass neutrality theorem",
            consequence="protects strongest A-sector result",
        ),
        PureWindNeutralityEntry(
            name="PW7: no scalar trace",
            neutrality_rule="J_sub does not source B_s, zeta residual metric trace, or scalar charge",
            role="metric-insertion guard",
            allowed_if="J_sub is decoupled from ordinary metric scalar trace",
            forbidden_if="pure wind reopens B_s/F_zeta or residual trace",
            status="REQUIRED",
            missing="no scalar-trace theorem",
            consequence="preserves Group 16 count-once guardrails",
        ),
        PureWindNeutralityEntry(
            name="PW8: no ordinary matter coupling",
            neutrality_rule="J_sub does not enter ordinary T_mu_nu routing or push matter",
            role="matter decoupling requirement",
            allowed_if="matter coupling remains in established ordinary sectors",
            forbidden_if="pure wind becomes fifth-force-like matter coupling",
            status="REQUIRED",
            missing="ordinary matter decoupling theorem",
            consequence="prevents pure wind from becoming matter repair mechanism",
        ),
        PureWindNeutralityEntry(
            name="PW9: no recovery role",
            neutrality_rule="J_sub is not chosen to pass gamma_like, AB, or exterior matching",
            role="anti-smuggling guard",
            allowed_if="recovery remains downstream test",
            forbidden_if="pure wind properties are recovery-tuned",
            status="REQUIRED",
            missing="not a mechanism",
            consequence="keeps recovery downstream",
        ),
        PureWindNeutralityEntry(
            name="PW10: no boundary repair",
            neutrality_rule="J_sub does not cancel boundary leakage, shell source, or scalar tail",
            role="boundary repair rejection",
            allowed_if="J_sub boundary behavior is neutral, not repair",
            forbidden_if="J_sub hides boundary failure",
            status="REQUIRED",
            missing="boundary neutrality theorem",
            consequence="prevents substrate flow from becoming repair current",
        ),
        PureWindNeutralityEntry(
            name="PW11: frame neutrality requirement",
            neutrality_rule="J_sub is not an arbitrary preferred-frame wind",
            role="frame safety guard",
            allowed_if="frame or frame-free definition is ontology-derived",
            forbidden_if="wind direction is arbitrary preferred frame",
            status="REQUIRED",
            missing="vacuum frame or frame-free substrate law",
            consequence="prevents arbitrary frame physics",
        ),
        PureWindNeutralityEntry(
            name="PW12: relation to u_vac deferred",
            neutrality_rule="J_sub cannot define u_vac circularly or depend on undefined u_vac",
            role="u_vac circularity guard",
            allowed_if="u_vac derived from real current or frame law later",
            forbidden_if="J_sub = n_vac u_vac with u_vac undefined",
            status="DEFER",
            missing="u_vac definition",
            consequence="keeps vacuum rest frame unresolved honestly",
        ),
        PureWindNeutralityEntry(
            name="PW13: relation to J_exch separation",
            neutrality_rule="J_sub is not whatever remains after J_exch is removed unless split criterion exists",
            role="split-definition guard",
            allowed_if="J_sub/J_exch split criterion is defined",
            forbidden_if="residual bookkeeping is treated as current definition",
            status="REQUIRED",
            missing="split criterion",
            consequence="prevents remainder-current fake definition",
        ),
        PureWindNeutralityEntry(
            name="PW14: pure wind as mass source rejection",
            neutrality_rule="pure wind contributes directly to mass/energy source",
            role="forbidden mass-source branch",
            allowed_if="never under pure wind status",
            forbidden_if="accepted as substrate current effect",
            status="REJECTED",
            missing="not pursued",
            consequence="protects mass neutrality",
        ),
        PureWindNeutralityEntry(
            name="PW15: pure wind as preferred-frame force rejection",
            neutrality_rule="pure wind exerts force because it defines a preferred direction/frame",
            role="forbidden preferred-frame branch",
            allowed_if="never without derived coupling and frame law",
            forbidden_if="accepted as ordinary-sector force",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents arbitrary wind force",
        ),
        PureWindNeutralityEntry(
            name="PW16: pure wind as scalar charge rejection",
            neutrality_rule="pure wind sources zeta/kappa/B_s scalar charge",
            role="forbidden scalar-charge branch",
            allowed_if="never under pure wind neutrality",
            forbidden_if="accepted as substrate effect",
            status="REJECTED",
            missing="not pursued",
            consequence="preserves no ordinary scalar radiation/charge",
        ),
        PureWindNeutralityEntry(
            name="PW17: pure wind as recovery repair rejection",
            neutrality_rule="pure wind adjusted to recover gamma_like, AB, or exterior behavior",
            role="forbidden recovery repair branch",
            allowed_if="never as mechanism",
            forbidden_if="accepted as neutral wind",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents recovery-shaped wind",
        ),
        PureWindNeutralityEntry(
            name="PW18: pure wind as boundary patch rejection",
            neutrality_rule="pure wind chosen to cancel boundary leakage or shell source",
            role="forbidden boundary patch branch",
            allowed_if="never as mechanism",
            forbidden_if="accepted as boundary-neutral substrate",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents painted boundary neutrality",
        ),
        PureWindNeutralityEntry(
            name="PW19: zero-net ordinary exchange compatibility",
            neutrality_rule="pure wind is compatible with Sigma_V - R_V = 0 ordinary-sector branch",
            role="ordinary-sector exchange neutrality candidate",
            allowed_if="wind flow is redistribution/transport, not net creation",
            forbidden_if="zero-net branch still claims active sourcing from wind",
            status="CANDIDATE",
            missing="ordinary-sector exchange neutrality theorem",
            consequence="keeps zero-net exchange live",
        ),
        PureWindNeutralityEntry(
            name="PW20: zero-creation ordinary branch compatibility",
            neutrality_rule="pure wind is compatible with Sigma_V = R_V = 0 ordinary-sector branch",
            role="strong ordinary-sector neutrality candidate",
            allowed_if="curvature changes arise from warping/constraint, not creation/destruction",
            forbidden_if="creation/destruction is invoked as ordinary active source",
            status="CANDIDATE",
            missing="zero-creation sector theorem",
            consequence="keeps clean no-exchange branch live",
        ),
        PureWindNeutralityEntry(
            name="PW21: neutrality failure",
            neutrality_rule="pure wind shifts mass, sources scalar trace, couples matter, or repairs boundary",
            role="branch failure condition",
            allowed_if="used to reject J_sub as ordinary-sector neutral substrate",
            forbidden_if="patched with labels",
            status="BRANCH_KILLED",
            missing="applies if failure demonstrated",
            consequence="J_sub cannot enter ordinary sector as pure wind",
        ),
        PureWindNeutralityEntry(
            name="PW22: recommended next move",
            neutrality_rule="if pure wind neutrality survives, define J_sub requirements next",
            role="next local bottleneck",
            allowed_if="J_sub remains theorem target after neutrality constraints",
            forbidden_if="jumping to J_exch before J_sub burden is stated",
            status="RECOMMENDED",
            missing="J_sub definition requirements",
            consequence="next script should be candidate_J_sub_definition_requirements.py",
        ),
    ]


def print_entry(e: PureWindNeutralityEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Neutrality rule: {e.neutrality_rule}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: Pure wind neutrality problem")

    print("Question:")
    print()
    print("  Can pure vacuum substrate flow exist without ordinary gravitational effect?")
    print()
    print("Core rule:")
    print()
    print("  pure wind does not gravitate merely because it flows")
    print()
    print("Goal:")
    print()
    print("  test J_sub safety before trying to define J_sub")
    print()
    print("Discipline:")
    print()
    print("  no M_ext shift")
    print("  no scalar trace")
    print("  no ordinary matter coupling")
    print("  no boundary repair")
    print("  no preferred-frame force")
    print("  no recovery role")
    print("  no circular u_vac")
    print("  preserve zero-net/zero-creation branches")

    status_line("pure wind neutrality problem posed", "REQUIRED")


def case_1_inventory(entries: List[PureWindNeutralityEntry]):
    header("Case 1: Pure wind neutrality inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[PureWindNeutralityEntry]):
    header("Case 2: Compact pure wind neutrality ledger")

    print("| Entry | Neutrality rule | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.neutrality_rule.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    status_line("compact pure wind neutrality ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[PureWindNeutralityEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Pure wind neutrality is required but not derived.")
    print("  J_sub can survive only as neutral substrate-current theorem target.")
    print("  No M_ext shift, scalar trace, matter coupling, boundary repair, preferred-frame force, or recovery role is allowed.")
    print("  Zero-net-exchange and zero-creation branches remain compatible and live.")
    print("  u_vac remains deferred.")
    print("  Next gate is J_sub definition requirements.")

    status_line("pure wind neutrality status count produced", "STRUCTURAL")


def case_4_neutrality_conditions():
    header("Case 4: Candidate neutrality conditions")

    print("Candidate neutrality conditions:")
    print()
    print("1. divergence-free substrate flow")
    print("2. no exchange: Sigma_sub = R_sub = 0")
    print("3. no endpoints / no ordinary sources or sinks")
    print("4. zero exterior flux or tangential boundary flow")
    print("5. no M_ext shift")
    print("6. no B_s/zeta/kappa scalar trace")
    print("7. no ordinary matter coupling")
    print("8. no recovery role")
    print("9. no boundary repair")
    print("10. no arbitrary preferred frame")

    status_line("pure wind neutrality conditions listed", "RECOMMENDED")


def case_4b_sample_pure_wind_field(ns):
    header("Case 4b: Sample divergence-free tangential pure wind")

    x, y, R = sp.symbols("x y R", positive=True)
    J_sub = sp.Matrix([-y, x])
    divergence = sp.simplify(sp.diff(J_sub[0], x) + sp.diff(J_sub[1], y))
    boundary_normal_flux = sp.simplify((x * J_sub[0] + y * J_sub[1]) / R)

    print("Sample field:")
    print(f"  J_sub(x, y) = {J_sub}")
    print()
    print(f"div J_sub = {divergence}")
    print(f"radial boundary flux on r=R = {boundary_normal_flux}")
    print()
    print("Interpretation:")
    print("  this sample shows a divergence-free tangential flow can satisfy")
    print("  no local source/sink and zero boundary-normal flux simultaneously.")
    print("  It is a compatibility example, not a J_sub theorem.")

    if divergence == 0 and boundary_normal_flux == 0:
        status_line(
            "sample pure-wind compatibility check",
            "DERIVED_REDUCED",
            "div J_sub = 0 and n·J_sub = 0 for the tangential sample field",
        )
    else:
        status_line(
            "sample pure-wind compatibility check",
            "UNRESOLVED",
            "sample field failed neutrality compatibility conditions",
        )

    ns.record_derivation(
        derivation_id="pure_wind_tangential_sample",
        inputs=[J_sub],
        output=sp.Tuple(divergence, boundary_normal_flux),
        method="sample_tangential_flow_compatibility",
        status=Status.DERIVED,
    )


def case_5_decision_tree():
    header("Case 5: Pure wind neutrality decision tree")

    print("Decision tree:")
    print()
    print("1. Pure wind satisfies no mass/scalar/matter/boundary effects:")
    print("   J_sub may proceed as theorem target.")
    print()
    print("2. Pure wind has divergence but no exchange:")
    print("   needs substrate conservation/support law.")
    print()
    print("3. Pure wind has endpoints/sources:")
    print("   it is not pure wind; reroute to J_exch candidate.")
    print()
    print("4. Pure wind shifts M_ext or scalar trace:")
    print("   J_sub branch killed for ordinary sector.")
    print()
    print("5. Pure wind depends on undefined u_vac:")
    print("   defer until frame/current law exists.")
    print()
    print("6. Pure wind passes only by boundary/recovery repair:")
    print("   rejected.")

    status_line("pure wind neutrality decision tree stated", "RECOMMENDED")


def case_6_good_failure():
    header("Case 6: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  pure wind cannot be neutral because it shifts mass, sources scalar trace,")
    print("  couples ordinary matter, or repairs boundary behavior.")
    print()
    print("Consequence:")
    print()
    print("  reject J_sub as ordinary-sector pure wind.")
    print("  move active effects to J_exch only if source sides are real.")
    print()
    print("Bad failure:")
    print()
    print("  claim pure wind is neutral while letting it gravitate or repair boundaries.")

    status_line("pure wind neutrality good failure stated", "DEFER")


def case_7_failure_controls():
    header("Case 7: Failure controls")

    print("Pure wind neutrality fails if:")
    print()
    print("1. J_sub shifts M_ext")
    print("2. J_sub sources B_s/zeta/kappa scalar trace")
    print("3. J_sub couples to ordinary matter")
    print("4. J_sub creates boundary leakage or repair")
    print("5. J_sub defines preferred-frame force")
    print("6. J_sub is recovery-tuned")
    print("7. J_sub is defined circularly from u_vac")
    print("8. J_sub hides Sigma/R exchange")
    print("9. J_sub is whatever remains after J_exch")
    print("10. pure wind claims active creation/destruction")

    status_line("pure wind neutrality failure controls stated", "RISK")


def case_8_next_tests():
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_pure_wind_neutrality_test.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_J_sub_definition_requirements.py")
    print("   Define what J_sub must be after neutrality constraints.")
    print()
    print("3. candidate_pure_wind_failure_summary.py")
    print("   Use if pure wind neutrality fails.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_J_sub_definition_requirements.py")
    print()
    print("Reason:")
    print("  If pure wind is allowed only under strict neutrality,")
    print("  J_sub must next be burdened with domain, frame, direction, measure, boundary, and decoupling requirements.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("Pure wind neutrality is required but not derived.")
    print()
    print("J_sub survives only as neutral substrate-current theorem target.")
    print()
    print("Required:")
    print()
    print("  no M_ext shift")
    print("  no scalar trace")
    print("  no ordinary matter coupling")
    print("  no boundary repair")
    print("  no preferred-frame force")
    print("  no recovery role")
    print()
    print("Best next script:")
    print()
    print("  candidate_J_sub_definition_requirements.py")

    status_line("pure wind neutrality audit complete", "CLOSED")


def main():
    header("Candidate Pure Wind Neutrality Test")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_neutrality_conditions()
    case_4b_sample_pure_wind_field(ns)
    case_5_decision_tree()
    case_6_good_failure()
    case_7_failure_controls()
    case_8_next_tests()
    final_interpretation()

    with archive:
        ns.record_obligation(ProofObligationRecord(
            obligation_id="prove_pure_wind_mass_neutrality_in_18_pure_wind",
            script_id=SCRIPT_ID,
            status=ObligationStatus.OPEN,
            statement="Mass neutrality theorem: delta M_ext|J_sub = 0. Pure wind must not change measured exterior mass.",
        ))
        ns.record_obligation(ProofObligationRecord(
            obligation_id="prove_pure_wind_scalar_trace_neutrality_in_18_pure_wind",
            script_id=SCRIPT_ID,
            status=ObligationStatus.OPEN,
            statement="Scalar trace neutrality theorem: J_sub must not source B_s, zeta residual metric trace, or scalar charge.",
        ))
        ns.record_obligation(ProofObligationRecord(
            obligation_id="prove_pure_wind_matter_decoupling_in_18_pure_wind",
            script_id=SCRIPT_ID,
            status=ObligationStatus.OPEN,
            statement="Ordinary matter decoupling theorem: J_sub must not enter ordinary T_mu_nu routing or push matter.",
        ))
        ns.record_claim(ClaimRecord(
            claim_id="pure_wind_neutrality_theorem_target_in_18",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.CANDIDATE_ROUTE,
            statement="Pure wind neutrality is required but not derived. J_sub survives only as neutral substrate-current theorem target. The tangential-flow sample confirms compatibility but is not a J_sub theorem.",
        ))
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id="reject_pure_wind_mass_source_in_18_pure_wind",
            script_id=SCRIPT_ID,
            branch_name="pure_wind_as_mass_source",
            status=GovernanceStatus.REJECTED_ROUTE,
            rationale="Pure wind contributing directly to mass/energy source is forbidden under pure wind neutrality.",
        ))
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id="reject_pure_wind_preferred_frame_force_in_18_pure_wind",
            script_id=SCRIPT_ID,
            branch_name="pure_wind_as_preferred_frame_force",
            status=GovernanceStatus.REJECTED_ROUTE,
            rationale="Pure wind exerting ordinary force because it defines a preferred direction/frame is forbidden.",
        ))
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id="reject_pure_wind_boundary_patch_in_18_pure_wind",
            script_id=SCRIPT_ID,
            branch_name="pure_wind_as_boundary_patch",
            status=GovernanceStatus.REJECTED_ROUTE,
            rationale="Pure wind chosen to cancel boundary leakage or shell source is a forbidden boundary patch.",
        ))
        ns.record_derivation(
            derivation_id="pure_wind_neutrality_test_marker",
            inputs=[],
            output=sp.Symbol("pure_wind_neutrality_test_complete"),
            method="pure_wind_neutrality_test",
            status=Status.DERIVED,
        )
        ns.write_run_metadata()


if __name__ == "__main__":
    main()
