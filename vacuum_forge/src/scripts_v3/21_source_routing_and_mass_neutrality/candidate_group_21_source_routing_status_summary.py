# Candidate group 21 source routing status summary
#
# Group:
#   21_source_routing_and_mass_neutrality
#
# Script type:
#   SUMMARY
#
# Purpose
# -------
# Close Group 21 by summarizing the source-routing and mass-neutrality status:
#
#   A-sector mass charge definition,
#   non-A mass-neutrality inventory,
#   residual scalar tail flux audit,
#   boundary flux mass preservation,
#   zeta/kappa residual neutrality,
#   J_V/J_sub/J_exch neutrality,
#   curvature accounting neutrality,
#   correction tensor guard,
#   ordinary source routing and no-double-counting.
#
# This script is not a parent field equation, not a mass-neutrality theorem,
# not a boundary theorem, not a source projector, and not a closure proof.
#
# Locked-door question:
#
#   What did Group 21 actually establish, and what remains theorem-targeted?

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


# =============================================================================
# Utilities
# =============================================================================


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


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


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "A_sector_mass_definition_dependency_21",
            "21_source_routing_and_mass_neutrality__candidate_A_sector_mass_charge_definition",
            "A_sector_mass_definition_21",
            RecordKind.DERIVATION,
        ),
        (
            "A_sector_schwarzschild_mass_residual_dependency_21",
            "21_source_routing_and_mass_neutrality__candidate_A_sector_mass_charge_definition",
            "A_sector_schwarzschild_mass_residual_21",
            RecordKind.DERIVATION,
        ),
        (
            "non_A_inventory_dependency_21",
            "21_source_routing_and_mass_neutrality__candidate_non_A_sector_mass_neutrality_inventory",
            "non_A_sector_mass_neutrality_inventory_marker_21",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "residual_scalar_tail_flux_dependency_21",
            "21_source_routing_and_mass_neutrality__candidate_residual_scalar_tail_flux_audit",
            "residual_scalar_tail_flux_1_over_r_21",
            RecordKind.DERIVATION,
        ),
        (
            "boundary_flux_inventory_dependency_21",
            "21_source_routing_and_mass_neutrality__candidate_boundary_flux_mass_preservation",
            "boundary_flux_mass_preservation_inventory_marker_21",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "zeta_kappa_inventory_dependency_21",
            "21_source_routing_and_mass_neutrality__candidate_zeta_kappa_mass_neutrality_conditions",
            "zeta_kappa_mass_neutrality_inventory_marker_21",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "JV_inventory_dependency_21",
            "21_source_routing_and_mass_neutrality__candidate_JV_mass_neutrality_conditions",
            "JV_mass_neutrality_inventory_marker_21",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "curvature_accounting_dependency_21",
            "21_source_routing_and_mass_neutrality__candidate_curvature_accounting_mass_neutrality",
            "curvature_accounting_mass_neutrality_inventory_marker_21",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "correction_tensor_guard_dependency_21",
            "21_source_routing_and_mass_neutrality__candidate_correction_tensor_mass_neutrality_guard",
            "correction_tensor_mass_neutrality_guard_marker_21",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "source_routing_no_double_counting_dependency_21",
            "21_source_routing_and_mass_neutrality__candidate_source_routing_no_double_counting",
            "source_routing_no_double_counting_marker_21",
            RecordKind.INVENTORY_MARKER,
        ),
    ]

    for dependency_id, upstream_script_id, upstream_derivation_id, expected_record_kind in dependencies:
        ns.declare_dependency(
            dependency_id=dependency_id,
            upstream_script_id=upstream_script_id,
            upstream_derivation_id=upstream_derivation_id,
            expected_record_kind=expected_record_kind,
        )

    return archive, ns, invalidated


def status_mark(status: str) -> StatusMark:
    return {
        "ACCOUNTING_ONLY": StatusMark.INFO,
        "CANDIDATE": StatusMark.INFO,
        "CLOSED_REDUCED": StatusMark.PASS,
        "DEFER": StatusMark.DEFER,
        "DIAGNOSTIC_ONLY": StatusMark.INFO,
        "NOT_INSERTABLE": StatusMark.FAIL,
        "OBLIGATION": StatusMark.OBLIGATION,
        "PROTECTED": StatusMark.PASS,
        "PROVISIONAL": StatusMark.INFO,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "RISK": StatusMark.WARN,
        "ROLE_LEVEL": StatusMark.INFO,
        "SAFE_IF": StatusMark.INFO,
        "SUMMARY": StatusMark.PASS,
        "THEOREM_TARGET": StatusMark.DEFER,
        "UNRESOLVED": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


# =============================================================================
# Data models
# =============================================================================


@dataclass
class Group21StatusEntry:
    name: str
    result: str
    status: str
    consequence: str
    handoff: str


@dataclass
class Group21ClosureOutcome:
    name: str
    statement: str
    status: str
    consequence: str


@dataclass
class Group21HandoffOption:
    name: str
    route: str
    allowed_if: str
    caution: str
    status: str


# =============================================================================
# Builders
# =============================================================================


def build_status_entries() -> List[Group21StatusEntry]:
    return [
        Group21StatusEntry(
            name="G21-1: A-sector mass charge",
            result="M_A = c^2 F_A/(8*pi*G) is the current reduced ordinary-exterior reference charge; for A = 1 - 2GM/(c^2 r), M_A = M",
            status="CLOSED_REDUCED",
            consequence="A carries the ordinary exterior mass coin in the current reduced branch",
            handoff="all non-A sectors are audited against delta M_A = 0 unless a future parent identity redefines mass",
        ),
        Group21StatusEntry(
            name="G21-2: non-A mass-neutrality inventory",
            result="18 non-A sectors were audited for possible exterior mass leakage",
            status="SUMMARY",
            consequence="no non-A sector is licensed as an independent ordinary exterior mass carrier",
            handoff="non-A sectors remain diagnostic, non-metric, role-level, deferred, non-insertable, or theorem-targeted",
        ),
        Group21StatusEntry(
            name="G21-3: residual scalar tail rule",
            result="a residual tail C/r carries F = -4*pi*C and is neutral only when C = 0 or non-metric/diagnostic",
            status="CLOSED_REDUCED",
            consequence="ordinary residual 1/r scalar tails are mass-dangerous",
            handoff="future residual sectors must prove vanishing exterior 1/r coefficients or a no-double-counting parent route",
        ),
        Group21StatusEntry(
            name="G21-4: boundary mass preservation",
            result="a non-A boundary A-tail q/r shifts delta_M_A = -c^2 q/(2G)",
            status="THEOREM_TARGET",
            consequence="boundary mass preservation remains required but not derived",
            handoff="no shell source, counterterm, recovery-tuned smoothing, sharp-support patch, or boundary purse is licensed",
        ),
        Group21StatusEntry(
            name="G21-5: zeta/kappa neutrality",
            result="zeta_tail = C_zeta/r and kappa_tail = C_kappa/r carry independent scalar fluxes unless C_zeta = C_kappa = 0",
            status="THEOREM_TARGET",
            consequence="residual-kill / non-metric residual remains the safest current convention",
            handoff="zeta/kappa cancellation by hand, Box zeta/kappa, residual repair, and recovery-chosen residual status remain rejected",
        ),
        Group21StatusEntry(
            name="G21-6: vacuum-current neutrality",
            result="J_V scalar residue, far-zone current flux, and Sigma/R zero-net language were audited as diagnostics",
            status="UNRESOLVED",
            consequence="J_V remains unresolved; J_sub/J_exch remain role-level",
            handoff="pure wind is not gravity; exchange is not repair; zero-net exchange needs real operators",
        ),
        Group21StatusEntry(
            name="G21-7: curvature accounting neutrality",
            result="A_curv/e_curv/J_curv were audited for scalar residue, source-reservoir behavior, far-zone flux, and boundary repair danger",
            status="DIAGNOSTIC_ONLY",
            consequence="curvature remains diagnostic/accounting/branch-filter; mass neutrality is required and not derived",
            handoff="e_curv source reservoir, curvature balance repair, J_curv by fiat, branch-kill bounce, and H_curv rescue remain rejected",
        ),
        Group21StatusEntry(
            name="G21-8: correction tensor guard",
            result="H_curv/H_exch were audited for trace leakage, A-tail correction, far-zone flux, divergence/source gap, and boundary repair danger",
            status="NOT_INSERTABLE",
            consequence="no correction tensor is insertable",
            handoff="future H requires tensor definition, source side, divergence safety, scalar trace neutrality, boundary neutrality, far-zone neutrality, and delta_M_A = 0",
        ),
        Group21StatusEntry(
            name="G21-9: ordinary source routing",
            result="rho/M_enc remains routed to A-sector; non-A duplicate source channels are forbidden, diagnostic, role-level, or theorem-targeted",
            status="PROTECTED",
            consequence="ordinary matter remains routed through protected channels without duplicate source counting",
            handoff="pressure/trace, longitudinal current, transverse current, TT stress, exchange, curvature, H, dark, and accounting routes need separate no-double-counting discipline",
        ),
        Group21StatusEntry(
            name="G21-10: no-double-counting guardrails",
            result="duplicate scalar tail, duplicate A-tail, and extra source-load ledger witnesses were recorded",
            status="SUMMARY",
            consequence="source cancellation ledgers do not count as sector neutrality",
            handoff="each non-A pocket must be empty, diagnostic, non-metric, role-level, or theorem-routed",
        ),
        Group21StatusEntry(
            name="G21-11: parent equation status",
            result="Group 21 sharpened mass-routing obligations but did not define a parent field equation",
            status="THEOREM_TARGET",
            consequence="parent equation remains not ready",
            handoff="do not insert O, H, J_V, Sigma/R, zeta/kappa scalar routes, curvature currents, or dark labels into a parent equation from this group alone",
        ),
    ]


def build_closure_outcomes() -> List[Group21ClosureOutcome]:
    return [
        Group21ClosureOutcome(
            name="Outcome A: A-sector charge protected",
            statement="M_A = c^2 F_A/(8*pi*G) is the only currently derived reduced ordinary exterior mass charge",
            status="CLOSED_REDUCED",
            consequence="A-sector mass coin remains protected",
        ),
        Group21ClosureOutcome(
            name="Outcome B: non-A sectors neutral or deferred",
            statement="All non-A sectors must satisfy delta_M_A = 0 or remain diagnostic, non-metric, role-level, deferred, or theorem-targeted",
            status="REQUIRED",
            consequence="no non-A exterior mass carrier is licensed",
        ),
        Group21ClosureOutcome(
            name="Outcome C: scalar-tail rule",
            statement="Any residual 1/r scalar tail carries nonzero surface flux unless its coefficient vanishes",
            status="CLOSED_REDUCED",
            consequence="ordinary residual exterior scalar tails must vanish or be non-metric/diagnostic",
        ),
        Group21ClosureOutcome(
            name="Outcome D: boundary neutrality still target",
            statement="Boundary mass preservation and exterior scalar silence are required but not derived",
            status="THEOREM_TARGET",
            consequence="boundary repair mechanisms remain rejected",
        ),
        Group21ClosureOutcome(
            name="Outcome E: parent equation not ready",
            statement="Mass-neutrality requirements sharpen future parent identity but do not make it available",
            status="THEOREM_TARGET",
            consequence="next group must choose a narrower follow-up path",
        ),
    ]


def build_handoff_options() -> List[Group21HandoffOption]:
    return [
        Group21HandoffOption(
            name="Handoff 1: boundary neutrality and scalar silence",
            route="22_boundary_neutrality_and_scalar_silence",
            allowed_if="the next step should attack the remaining boundary/scalar-tail theorem burden directly",
            caution="do not use smoothing, O, H, or recovery tuning as a shortcut",
            status="RECOMMENDED",
        ),
        Group21HandoffOption(
            name="Handoff 2: metric insertion recovery retest",
            route="22_metric_insertion_recovery_retest",
            allowed_if="the next step wants to re-test B_s/F_zeta insertion under the Group 21 mass-neutrality guardrails",
            caution="B_s/F_zeta insertion remains theorem-targeted; do not treat residual-kill as derived",
            status="CANDIDATE",
        ),
        Group21HandoffOption(
            name="Handoff 3: role-specific source projectors",
            route="22_role_specific_source_projectors",
            allowed_if="a real source-projector route is attempted with explicit domain, kernel, image, source side, and boundary law",
            caution="Group 20 already rejected universal O and projection-by-name",
            status="CANDIDATE",
        ),
        Group21HandoffOption(
            name="Handoff 4: reduced observational audit",
            route="22_reduced_observational_audit",
            allowed_if="the A-sector reduced mass charge is stable enough for downstream observational bookkeeping",
            caution="observational checks must not choose non-A mass routes or boundary conditions",
            status="CANDIDATE",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Group 21 status summary problem")
    print("Question:")
    print()
    print("  What did Group 21 actually establish, and what remains theorem-targeted?")
    print()
    print("Discipline:")
    print()
    print("  This is a group summary, not a closure proof.")
    print("  Summary claims must not outrank the archived derivations and obligations.")
    print("  A-sector mass charge remains protected.")
    print("  Non-A mass neutrality remains required unless explicitly derived.")
    print("  Parent equation remains not ready.")

    with out.governance_assessments():
        out.line(
            "Group 21 summary opened",
            StatusMark.INFO,
            "summarizing archive-backed source-routing and mass-neutrality status",
        )


def case_1_status_entries(entries: List[Group21StatusEntry], out: ScriptOutput) -> None:
    header("Case 1: Group 21 status entries")
    for entry in entries:
        print()
        print("-" * 120)
        print(entry.name)
        print("-" * 120)
        print(f"Result: {entry.result}")
        print(f"[{status_mark(entry.status).value}] {entry.name}: {entry.status}")
        print(f"Consequence: {entry.consequence}")
        print(f"Handoff: {entry.handoff}")

    with out.governance_assessments():
        out.line(
            "Group 21 status ledger populated",
            StatusMark.PASS,
            f"{len(entries)} status entries summarized from the Group 21 script chain",
        )


def case_2_closure_outcomes(outcomes: List[Group21ClosureOutcome], out: ScriptOutput) -> None:
    header("Case 2: Closure outcomes")
    for outcome in outcomes:
        print()
        print("-" * 120)
        print(outcome.name)
        print("-" * 120)
        print(f"Statement: {outcome.statement}")
        print(f"[{status_mark(outcome.status).value}] {outcome.name}: {outcome.status}")
        print(f"Consequence: {outcome.consequence}")

    with out.governance_assessments():
        out.line(
            "Group 21 closure outcomes stated",
            StatusMark.PASS,
            "A-sector charge protected; non-A neutrality remains required/theorem-targeted",
        )


def case_3_preserved_unknowns(out: ScriptOutput) -> None:
    header("Case 3: Known unknowns preserved")
    unknowns = [
        "boundary mass preservation theorem",
        "static-source neutrality theorem",
        "ordinary matter decoupling theorem",
        "B_s/F_zeta insertion law",
        "residual-kill derivation",
        "O no-overlap",
        "J_V definition",
        "J_sub/J_exch definition",
        "Sigma/R operators",
        "curvature admissibility functional",
        "J_curv",
        "H_curv/H_exch tensor definitions",
        "correction tensor divergence safety",
        "source separation",
        "parent identity",
    ]

    for item in unknowns:
        print(f"  - {item}")

    with out.unresolved_obligations():
        out.line(
            "Group 21 known unknowns preserved",
            StatusMark.OBLIGATION,
            "mass-routing audit did not close parent, boundary, current, projection, curvature, or correction-tensor obligations",
        )


def case_4_handoff_options(options: List[Group21HandoffOption], out: ScriptOutput) -> None:
    header("Case 4: Handoff options")
    for option in options:
        print()
        print("-" * 120)
        print(option.name)
        print("-" * 120)
        print(f"Route: {option.route}")
        print(f"Allowed if: {option.allowed_if}")
        print(f"Caution: {option.caution}")
        print(f"[{status_mark(option.status).value}] {option.name}: {option.status}")

    with out.governance_assessments():
        out.line(
            "Group 21 handoff options recorded",
            StatusMark.PASS,
            "boundary neutrality/scalar silence is the most direct next target; other routes remain candidates",
        )


def case_5_failure_controls(out: ScriptOutput) -> None:
    header("Case 5: Failure controls")
    print("The Group 21 summary fails if a later script treats it as proving:")
    print()
    print("1. mass neutrality is solved")
    print("2. boundary neutrality is solved")
    print("3. ordinary matter decoupling is solved")
    print("4. J_V is defined")
    print("5. J_sub/J_exch are real currents")
    print("6. O exists")
    print("7. B_s/F_zeta insertion is derived")
    print("8. H_curv/H_exch are insertable")
    print("9. curvature dynamics are derived")
    print("10. a parent field equation is ready")
    print()
    print("The summary only licenses this reduced governance result:")
    print()
    print("  A carries the ordinary exterior mass coin.")
    print("  Every other sector must show empty pockets.")

    with out.governance_assessments():
        out.line(
            "Group 21 overclaim controls stated",
            StatusMark.OBLIGATION,
            "summary must not upgrade theorem targets into solved claims",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Group 21 result:")
    print()
    print("  A-sector mass charge is protected as the current reduced ordinary exterior mass reference.")
    print("  Non-A sectors are not proven mass-neutral.")
    print("  Instead, Group 21 records the sector-by-sector theorem burden and rejected repair routes.")
    print()
    print("Current closed-reduced rule:")
    print()
    print("  M_A = c^2 F_A/(8*pi*G)")
    print()
    print("Current governance rule:")
    print()
    print("  non-A sectors must satisfy delta_M_A = 0, remain diagnostic, remain non-metric,")
    print("  stay role-level, be non-insertable, or remain theorem-targeted.")
    print()
    print("Recommended next group:")
    print()
    print("  22_boundary_neutrality_and_scalar_silence")
    print()
    print("Tiny goblin label:")
    print()
    print("  A carries the coin. Everyone else shows empty pockets.")

    with out.governance_assessments():
        out.line(
            "Group 21 source-routing status summary complete",
            StatusMark.PASS,
            "A-sector mass protected; non-A neutrality sharpened but not solved; parent equation still not ready",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_inventory_marker(ns, entries: List[Group21StatusEntry]) -> None:
    symbols = [sp.Symbol(entry.name.split(":", 1)[0].replace("-", "_").replace(" ", "_")) for entry in entries]
    ns.record_derivation(
        derivation_id="group21_source_routing_status_summary_marker_21",
        inputs=symbols,
        output=sp.Symbol("group21_source_routing_status_summary_stated"),
        method="Group 21 source-routing and mass-neutrality status summary",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="summary_marker",
        scope="Group 21 source routing and mass neutrality",
        is_placeholder=True,
    )


def record_obligations(ns, entries: List[Group21StatusEntry], outcomes: List[Group21ClosureOutcome]) -> None:
    obligations = [
        (
            "derive_ordinary_closed_regime_mass_neutrality_theorem_21",
            "Derive ordinary closed-regime mass-neutrality theorem",
            "Show M_ext = M_A and delta_M_A|non-A = 0 for zeta, kappa, J_V, J_sub, J_exch, curvature diagnostics, correction tensor candidates, boundary behavior, and dark labels.",
        ),
        (
            "derive_boundary_neutrality_and_scalar_silence_21",
            "Derive boundary neutrality and scalar silence",
            "Show no non-A boundary behavior changes exterior A-flux, creates shell source, or leaves residual 1/r scalar tails.",
        ),
        (
            "derive_source_routing_no_double_counting_parent_theorem_21",
            "Derive source-routing no-double-counting parent theorem",
            "Show ordinary rho/T_mu_nu is not duplicated into kappa, zeta, curvature, H, exchange, dark, or accounting source channels.",
        ),
        (
            "derive_parent_identity_after_mass_neutrality_21",
            "Derive parent identity after mass-neutrality prerequisites",
            "Only after mass, boundary, scalar, source, divergence, and insertion obligations are met may a parent equation be attempted.",
        ),
    ]

    for obligation_id, title, description in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["group21_source_routing_status_summary_21"],
            description=description,
        ))

    for entry in entries:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=f"preserve_{entry.name.split(':', 1)[0].replace('-', '_').replace(' ', '_').lower()}_status_21",
            script_id=SCRIPT_ID,
            title=f"Preserve Group 21 status: {entry.name}",
            status=ObligationStatus.OPEN,
            required_by=["group21_source_routing_status_summary_21"],
            description=(
                f"Result: {entry.result}. Status: {entry.status}. "
                f"Consequence: {entry.consequence}. Handoff: {entry.handoff}."
            ),
        ))

    for outcome in outcomes:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=f"preserve_{outcome.name.split(':', 1)[0].replace('-', '_').replace(' ', '_').lower()}_21",
            script_id=SCRIPT_ID,
            title=f"Preserve closure outcome: {outcome.name}",
            status=ObligationStatus.OPEN,
            required_by=["group21_source_routing_status_summary_21"],
            description=(
                f"Statement: {outcome.statement}. Status: {outcome.status}. Consequence: {outcome.consequence}."
            ),
        ))


def record_governance(
    ns,
    entries: List[Group21StatusEntry],
    outcomes: List[Group21ClosureOutcome],
    options: List[Group21HandoffOption],
) -> None:
    obligation_ids = [
        "derive_ordinary_closed_regime_mass_neutrality_theorem_21",
        "derive_boundary_neutrality_and_scalar_silence_21",
        "derive_source_routing_no_double_counting_parent_theorem_21",
        "derive_parent_identity_after_mass_neutrality_21",
    ]

    ns.record_route(RouteRecord(
        route_id="group21_source_routing_status_summary_21",
        script_id=SCRIPT_ID,
        name="Group 21 source-routing and mass-neutrality status summary",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "A-sector mass charge remains the reduced ordinary exterior reference",
            "non-A sectors are not treated as exterior mass carriers without delta_M_A = 0",
            "boundary neutrality and scalar silence remain theorem-targeted",
            "parent equation remains not ready",
        ],
    ))

    ns.record_route(RouteRecord(
        route_id="recommended_next_group_boundary_neutrality_scalar_silence_22",
        script_id=SCRIPT_ID,
        name="Recommended next group: boundary neutrality and scalar silence",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=[
            "derive_boundary_neutrality_and_scalar_silence_21",
            "derive_ordinary_closed_regime_mass_neutrality_theorem_21",
        ],
        activation_conditions=[
            "attack boundary mass preservation and residual scalar-tail silence directly",
            "do not use smoothing, O, H, dark labels, or recovery tuning as repairs",
        ],
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="protect_A_sector_mass_coin_after_group21",
        script_id=SCRIPT_ID,
        branch_id="A_sector_mass_charge_reference",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=["derive_ordinary_closed_regime_mass_neutrality_theorem_21"],
        description=(
            "A-sector mass charge remains the current reduced ordinary exterior reference. "
            "Non-A sectors must remain neutral, diagnostic, non-metric, role-level, non-insertable, or theorem-targeted."
        ),
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_parent_equation_after_group21",
        script_id=SCRIPT_ID,
        branch_id="parent_field_equation_route",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=obligation_ids,
        description=(
            "Group 21 sharpens source-routing and mass-neutrality requirements but does not make the parent field equation ready."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="group21_A_sector_mass_charge_protected_claim",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.LICENSING,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "In the reduced ordinary exterior, M_A = c^2 F_A/(8*pi*G) remains the current reference mass charge; "
            "Group 21 licenses it as the audit anchor, not as a final covariant parent mass definition."
        ),
        derivation_ids=[
            "A_sector_mass_definition_21",
            "A_sector_schwarzschild_mass_residual_21",
        ],
        obligation_ids=["derive_ordinary_closed_regime_mass_neutrality_theorem_21"],
    ))

    ns.record_claim(ClaimRecord(
        claim_id="group21_non_A_mass_neutrality_not_solved_claim",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Group 21 does not solve non-A mass neutrality. It records that non-A sectors must satisfy delta_M_A = 0, remain diagnostic, "
            "remain non-metric, stay role-level, be non-insertable, or remain theorem-targeted."
        ),
        derivation_ids=[
            "non_A_sector_mass_neutrality_inventory_marker_21",
            "source_routing_no_double_counting_marker_21",
        ],
        obligation_ids=obligation_ids,
    ))

    ns.record_claim(ClaimRecord(
        claim_id="group21_parent_equation_not_ready_claim",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "The parent field equation remains not ready after Group 21. Boundary neutrality, scalar silence, source separation, "
            "current definitions, curvature-current definitions, correction-tensor definitions, and no-double-counting obligations remain open."
        ),
        derivation_ids=["group21_source_routing_status_summary_marker_21"],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Group 21 Source Routing Status Summary")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    entries = build_status_entries()
    outcomes = build_closure_outcomes()
    options = build_handoff_options()

    case_0_problem_statement(out)
    case_1_status_entries(entries, out)
    case_2_closure_outcomes(outcomes, out)
    case_3_preserved_unknowns(out)
    case_4_handoff_options(options, out)
    case_5_failure_controls(out)
    final_interpretation(out)

    record_inventory_marker(ns, entries)
    record_obligations(ns, entries, outcomes)
    record_governance(ns, entries, outcomes, options)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
