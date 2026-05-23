# Candidate sector problem ledger
#
# Group:
#   28_sector_pairing_no_overlap
#
# Human title:
#   Sector Pairing And No-Overlap Geometry
#
# Script type:
#   PROBLEM LEDGER / SECTOR-GEOMETRY TARGET
#
# Purpose
# -------
# Open the sector-pairing/no-overlap geometry group by stating what a
# no-overlap sector geometry must define before it can support kernel/image,
# active-O construction, or residual control.
#
# Locked-door question:
#
#   What exactly must a no-overlap sector geometry define?
#
# This script does not derive a pairing.
# It does not derive active O.
# It does not derive residual control.
# It does not derive B_s/F_zeta insertion.
# It does not derive parent equation closure.
#
# Tiny goblin rule:
#
#   No overlap is not a word.
#   It is a trap with measurements.

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


def status_mark(status: str) -> StatusMark:
    return {
        "BLOCKED": StatusMark.FAIL,
        "CANDIDATE": StatusMark.DEFER,
        "FORBIDDEN": StatusMark.FAIL,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "PRESERVE": StatusMark.OBLIGATION,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "TARGET": StatusMark.DEFER,
        "UNDERDETERMINED": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g27_summary",
            "027_active_O_construction__candidate_group_27_status_summary",
            "g27_status_summary",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g27_ob",
            "027_active_O_construction__candidate_O_obligations",
            "g27_O_obligations",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g27_pair",
            "027_active_O_construction__candidate_O_no_overlap_pairing",
            "g27_O_pairing",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g27_obs",
            "027_active_O_construction__candidate_O_construction_obstruction",
            "g27_O_obstruction",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g26_summary",
            "026_residual_control_theorem_attempt__candidate_group_26_status_summary",
            "g26_status_summary",
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


def ensure_archive_write_dirs(ns) -> None:
    for attr in (
        "routes_path",
        "branch_decisions_path",
        "claims_path",
        "obligations_path",
        "derivations_path",
        "governance_path",
    ):
        path_obj = getattr(ns, attr, None)
        if path_obj is not None:
            path_obj.mkdir(parents=True, exist_ok=True)


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


# =============================================================================
# Data models
# =============================================================================


@dataclass
class SectorProblemSymbols:
    T_zeta: sp.Symbol
    R_zeta: sp.Symbol
    R_kappa: sp.Symbol
    A_eps: sp.Symbol
    A_kappa: sp.Symbol
    S_src: sp.Symbol
    B_bdy: sp.Symbol
    J_cur: sp.Symbol
    M_A: sp.Symbol
    U_sup: sp.Symbol
    D_diag: sp.Symbol
    P_parent: sp.Symbol
    inventory_gap: sp.Symbol
    membership_gap: sp.Symbol
    pairing_gap: sp.Symbol
    incidence_gap: sp.Symbol
    projection_gap: sp.Symbol
    routing_gap: sp.Symbol
    support_gap: sp.Symbol
    divergence_gap: sp.Symbol
    recovery_gap: sp.Symbol
    insertion_gap: sp.Symbol
    parent_gap: sp.Symbol
    geometry_burden: sp.Expr


@dataclass
class GeometryTask:
    name: str
    task: str
    status: str
    needed_for: str
    failure_if: str


@dataclass
class GeometryGuardrail:
    name: str
    preserve: str
    status: str
    reason: str
    violation_if: str


@dataclass
class ForbiddenGeometryUse:
    name: str
    forbidden_use: str
    status: str
    reason: str


@dataclass
class GeometryBoundary:
    name: str
    boundary: str
    status: str
    meaning: str


# =============================================================================
# Builders
# =============================================================================


def build_symbols() -> SectorProblemSymbols:
    (
        T_zeta,
        R_zeta,
        R_kappa,
        A_eps,
        A_kappa,
        S_src,
        B_bdy,
        J_cur,
        M_A,
        U_sup,
        D_diag,
        P_parent,
        inventory_gap,
        membership_gap,
        pairing_gap,
        incidence_gap,
        projection_gap,
        routing_gap,
        support_gap,
        divergence_gap,
        recovery_gap,
        insertion_gap,
        parent_gap,
    ) = sp.symbols(
        "T_zeta R_zeta R_kappa A_eps A_kappa S_src B_bdy J_cur M_A U_sup D_diag P_parent "
        "inventory_gap membership_gap pairing_gap incidence_gap projection_gap routing_gap support_gap "
        "divergence_gap recovery_gap insertion_gap parent_gap",
        real=True,
    )

    geometry_burden = sp.simplify(
        inventory_gap
        + membership_gap
        + pairing_gap
        + incidence_gap
        + projection_gap
        + routing_gap
        + support_gap
        + divergence_gap
        + recovery_gap
        + insertion_gap
        + parent_gap
    )

    return SectorProblemSymbols(
        T_zeta=T_zeta,
        R_zeta=R_zeta,
        R_kappa=R_kappa,
        A_eps=A_eps,
        A_kappa=A_kappa,
        S_src=S_src,
        B_bdy=B_bdy,
        J_cur=J_cur,
        M_A=M_A,
        U_sup=U_sup,
        D_diag=D_diag,
        P_parent=P_parent,
        inventory_gap=inventory_gap,
        membership_gap=membership_gap,
        pairing_gap=pairing_gap,
        incidence_gap=incidence_gap,
        projection_gap=projection_gap,
        routing_gap=routing_gap,
        support_gap=support_gap,
        divergence_gap=divergence_gap,
        recovery_gap=recovery_gap,
        insertion_gap=insertion_gap,
        parent_gap=parent_gap,
        geometry_burden=geometry_burden,
    )


def build_tasks() -> List[GeometryTask]:
    return [
        GeometryTask(
            name="T1: inventory sectors",
            task="identify safe trace, residual, accounting, source, boundary, current, mass, support, diagnostic, and parent sectors",
            status="REQUIRED",
            needed_for="knowing what could overlap",
            failure_if="no-overlap is asserted without defined sectors",
        ),
        GeometryTask(
            name="T2: define membership",
            task="state what makes an object belong to a sector",
            status="REQUIRED",
            needed_for="preventing arbitrary sector assignment",
            failure_if="zeta/kappa/accounting objects are assigned by label only",
        ),
        GeometryTask(
            name="T3: define pairing/incidence",
            task="derive a pairing, incidence matrix, projection criterion, routing graph, or equivalent overlap criterion",
            status="REQUIRED",
            needed_for="turning no-overlap into mathematics",
            failure_if="ordinary orthogonality or sector disjointness is assumed",
        ),
        GeometryTask(
            name="T4: preserve safe trace",
            task="keep zeta_to_Bs / zeta_Bs as the safe scalar trace sector",
            status="REQUIRED",
            needed_for="count-once scalar trace discipline",
            failure_if="residual zeta/kappa re-enter ordinary trace",
        ),
        GeometryTask(
            name="T5: classify residual sectors",
            task="classify zeta_residual_metric and kappa_metric without declaring them killed or inert",
            status="REQUIRED",
            needed_for="future kernel/image and residual-control retest",
            failure_if="residuals are erased by sector naming",
        ),
        GeometryTask(
            name="T6: protect accounting sectors",
            task="prevent epsilon/e_kappa accounting sectors from becoming hidden metric/source reservoirs",
            status="REQUIRED",
            needed_for="accounting no-reservoir discipline",
            failure_if="accounting variables hide residual geometry or source load",
        ),
        GeometryTask(
            name="T7: protect boundary/source/support sectors",
            task="ensure no-overlap is not chosen from boundary/source/current/support failure",
            status="REQUIRED",
            needed_for="guardrail independence",
            failure_if="repair need selects sector geometry",
        ),
        GeometryTask(
            name="T8: audit divergence behavior",
            task="identify whether sector split is derivative/divergence safe",
            status="REQUIRED",
            needed_for="future field-equation use",
            failure_if="sector geometry creates hidden divergence correction source",
        ),
        GeometryTask(
            name="T9: preserve recovery independence",
            task="reject sector geometry selected from AB=1, B=1/A, Schwarzschild, gamma, PPN, kappa=0, or parent-fit success",
            status="REQUIRED",
            needed_for="anti-smuggling discipline",
            failure_if="recovery constructs no-overlap",
        ),
        GeometryTask(
            name="T10: preserve downstream gates",
            task="keep active O, residual control, B_s/F_zeta insertion, and parent equation closed",
            status="REQUIRED",
            needed_for="not overclaiming",
            failure_if="sector geometry is upgraded to O/residual/insertion/parent theorem",
        ),
    ]


def build_guardrails() -> List[GeometryGuardrail]:
    return [
        GeometryGuardrail(
            name="G1: safe trace remains unique",
            preserve="zeta_to_Bs remains the safe scalar trace route",
            status="PRESERVE",
            reason="count-once scalar trace requires no second residual path",
            violation_if="zeta_residual_metric or kappa_metric re-enter ordinary trace",
        ),
        GeometryGuardrail(
            name="G2: residuals not inert by label",
            preserve="zeta/kappa residuals remain unresolved unless no-overlap geometry controls them",
            status="PRESERVE",
            reason="Group 26 did not derive residual non-reentry and Group 27 did not construct O",
            violation_if="sector name makes residuals harmless",
        ),
        GeometryGuardrail(
            name="G3: accounting not reservoir",
            preserve="epsilon/e_kappa accounting sectors cannot hide residual metric/source load",
            status="PRESERVE",
            reason="accounting partial reduction does not solve geometric residuals",
            violation_if="accounting sectors absorb zeta/kappa residual work",
        ),
        GeometryGuardrail(
            name="G4: support/source insufficient alone",
            preserve="support and source routing may assist but cannot be full no-overlap proof alone",
            status="PRESERVE",
            reason="Group 27 found support/source disjointness insufficient by itself",
            violation_if="support or source separation is promoted to full sector geometry",
        ),
        GeometryGuardrail(
            name="G5: recovery audit only",
            preserve="recovery may audit a sector geometry but may not select it",
            status="PRESERVE",
            reason="recovery-selected O and recovery-selected no-overlap are smuggling routes",
            violation_if="AB=1, Schwarzschild, gamma, or weak-field success chooses the pairing",
        ),
        GeometryGuardrail(
            name="G6: insertion separation",
            preserve="sector geometry does not license B_s/F_zeta insertion",
            status="PRESERVE",
            reason="coefficient origin remains separate",
            violation_if="no-overlap geometry is treated as insertion law",
        ),
        GeometryGuardrail(
            name="G7: parent exclusion",
            preserve="parent equation remains excluded from sector-geometry construction",
            status="PRESERVE",
            reason="parent closure remains downstream and not ready",
            violation_if="sector geometry opens parent equation",
        ),
    ]


def build_forbidden_uses() -> List[ForbiddenGeometryUse]:
    return [
        ForbiddenGeometryUse(
            name="F1: orthogonality by habit",
            forbidden_use="ordinary inner-product orthogonality assumed without a derived pairing",
            status="REJECTED",
            reason="the theory has not supplied that structure",
        ),
        ForbiddenGeometryUse(
            name="F2: sector split by naming",
            forbidden_use="trace and residual sectors declared disjoint by label",
            status="REJECTED",
            reason="sector split needs membership and incidence content",
        ),
        ForbiddenGeometryUse(
            name="F3: support disjointness as theorem",
            forbidden_use="support separation treated as full no-overlap",
            status="REJECTED",
            reason="support does not by itself control trace/source/reentry",
        ),
        ForbiddenGeometryUse(
            name="F4: source routing as theorem",
            forbidden_use="source-routing separation treated as full no-overlap",
            status="REJECTED",
            reason="source routing does not by itself control metric trace residuals",
        ),
        ForbiddenGeometryUse(
            name="F5: diagnostic label as inertness",
            forbidden_use="diagnostic sector label makes residuals harmless",
            status="REJECTED",
            reason="diagnostic/inert status requires no-reentry law",
        ),
        ForbiddenGeometryUse(
            name="F6: recovery-selected geometry",
            forbidden_use="sector geometry chosen because recovery works",
            status="REJECTED",
            reason="recovery may audit but not construct",
        ),
        ForbiddenGeometryUse(
            name="F7: repair-selected geometry",
            forbidden_use="sector geometry chosen to fix boundary/source/support failure",
            status="REJECTED",
            reason="failure may reject but not select",
        ),
        ForbiddenGeometryUse(
            name="F8: sector geometry as O",
            forbidden_use="partial sector geometry treated as active O construction",
            status="REJECTED",
            reason="O still needs kernel/image, algebraic law, divergence behavior, and guardrail behavior",
        ),
        ForbiddenGeometryUse(
            name="F9: sector geometry as downstream closure",
            forbidden_use="sector geometry licenses residual control, insertion, or parent equation",
            status="REJECTED",
            reason="downstream gates remain closed",
        ),
    ]


def build_boundaries() -> List[GeometryBoundary]:
    return [
        GeometryBoundary(
            name="B1: candidate sector inventory allowed",
            boundary="it is allowed to propose a sector inventory",
            status="CANDIDATE",
            meaning="only if membership rules remain explicit obligations",
        ),
        GeometryBoundary(
            name="B2: candidate incidence allowed",
            boundary="it is allowed to propose incidence/pairing/projection/routing candidates",
            status="CANDIDATE",
            meaning="only if none are treated as derived by naming",
        ),
        GeometryBoundary(
            name="B3: partial sector geometry allowed",
            boundary="it is allowed to derive partial separation constraints",
            status="CANDIDATE",
            meaning="partial constraints may guide O but do not construct O",
        ),
        GeometryBoundary(
            name="B4: obstruction allowed",
            boundary="it is allowed to conclude current objects do not define no-overlap geometry",
            status="CANDIDATE",
            meaning="controlled underdetermination is useful if missing structure is identified",
        ),
        GeometryBoundary(
            name="B5: new postulate inventory allowed",
            boundary="it is allowed to identify a minimal new choice/postulate needed",
            status="CANDIDATE",
            meaning="a clean choice is better than disguised derivation",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Sector-pairing/no-overlap geometry problem")
    print("Question:")
    print()
    print("  What exactly must a no-overlap sector geometry define?")
    print()
    print("Reference discipline:")
    print()
    print("  No-overlap is not a label.")
    print("  It must be a sector membership rule plus a pairing, incidence, projection, routing, or equivalent criterion.")
    print("  This script states the burden; it does not derive the pairing.")

    with out.governance_assessments():
        out.line(
            "sector-pairing/no-overlap geometry problem ledger opened",
            StatusMark.INFO,
            "stating no-overlap geometry burden without deriving a pairing",
        )


def case_1_symbol_ledger(symbols: SectorProblemSymbols, out: ScriptOutput) -> None:
    header("Case 1: Sector geometry burden ledger")
    print("Candidate sectors:")
    print()
    for name in [
        "T_zeta",
        "R_zeta",
        "R_kappa",
        "A_eps",
        "A_kappa",
        "S_src",
        "B_bdy",
        "J_cur",
        "M_A",
        "U_sup",
        "D_diag",
        "P_parent",
    ]:
        print(f"  {name} = {sp.sstr(getattr(symbols, name))}")
    print()
    print("No-overlap geometry gaps:")
    print()
    for name in [
        "inventory_gap",
        "membership_gap",
        "pairing_gap",
        "incidence_gap",
        "projection_gap",
        "routing_gap",
        "support_gap",
        "divergence_gap",
        "recovery_gap",
        "insertion_gap",
        "parent_gap",
    ]:
        print(f"  {name} = {sp.sstr(getattr(symbols, name))}")
    print()
    print("Total sector geometry burden:")
    print()
    print(f"  L_sector_geometry = {sp.sstr(symbols.geometry_burden)}")
    print()
    print("Interpretation:")
    print()
    print("  No-overlap geometry is not available until these gaps are closed or explicitly classified.")
    print("  Parent sector is listed only to exclude it from construction.")

    with out.derived_results():
        out.line(
            "sector-geometry construction burden stated",
            StatusMark.OBLIGATION,
            f"L_sector_geometry = {sp.sstr(symbols.geometry_burden)}",
        )


def case_2_tasks(tasks: List[GeometryTask], out: ScriptOutput) -> None:
    header("Case 2: Sector geometry construction tasks")
    for task in tasks:
        print()
        print("-" * 120)
        print(task.name)
        print("-" * 120)
        print(f"Task: {task.task}")
        print(f"[{status_mark(task.status).value}] {task.name}: {task.status}")
        print(f"Needed for: {task.needed_for}")
        print(f"Failure if: {task.failure_if}")

    with out.unresolved_obligations():
        out.line(
            "sector-geometry task ledger populated",
            StatusMark.OBLIGATION,
            f"{len(tasks)} construction tasks remain open",
        )


def case_3_guardrails(guardrails: List[GeometryGuardrail], out: ScriptOutput) -> None:
    header("Case 3: Guardrails no-overlap geometry must preserve")
    for guardrail in guardrails:
        print()
        print("-" * 120)
        print(guardrail.name)
        print("-" * 120)
        print(f"Preserve: {guardrail.preserve}")
        print(f"[{status_mark(guardrail.status).value}] {guardrail.name}: {guardrail.status}")
        print(f"Reason: {guardrail.reason}")
        print(f"Violation if: {guardrail.violation_if}")

    with out.governance_assessments():
        out.line(
            "sector-geometry preservation guardrails stated",
            StatusMark.PASS,
            f"{len(guardrails)} guardrails must be preserved by any no-overlap geometry",
        )


def case_4_forbidden_uses(forbidden: List[ForbiddenGeometryUse], out: ScriptOutput) -> None:
    header("Case 4: Forbidden no-overlap geometry uses")
    for item in forbidden:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Forbidden use: {item.forbidden_use}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Reason: {item.reason}")

    with out.counterexamples():
        out.line(
            "sector-geometry shortcuts rejected",
            StatusMark.FAIL,
            "orthogonality by habit, sector split by naming, support/source theorem shortcuts, diagnostic inertness, recovery/repair selection, O upgrade, and downstream closure are rejected",
        )


def case_5_boundaries(boundaries: List[GeometryBoundary], out: ScriptOutput) -> None:
    header("Case 5: Allowed construction boundaries")
    for boundary in boundaries:
        print()
        print("-" * 120)
        print(boundary.name)
        print("-" * 120)
        print(f"Boundary: {boundary.boundary}")
        print(f"[{status_mark(boundary.status).value}] {boundary.name}: {boundary.status}")
        print(f"Meaning: {boundary.meaning}")

    with out.governance_assessments():
        out.line(
            "sector-geometry construction boundaries stated",
            StatusMark.PASS,
            "candidate inventory, candidate incidence, partial geometry, obstruction, and new-postulate inventory are allowed outcomes",
        )


def case_6_failure_controls(out: ScriptOutput) -> None:
    header("Case 6: Failure controls")
    print("The sector-geometry problem ledger fails if a later script allows:")
    print()
    print("1. ordinary orthogonality by habit")
    print("2. sector split by naming")
    print("3. support disjointness as full no-overlap")
    print("4. source-routing disjointness as full no-overlap")
    print("5. diagnostic label as inertness")
    print("6. recovery-selected sector geometry")
    print("7. repair-selected sector geometry")
    print("8. sector geometry treated as active O")
    print("9. sector geometry treated as residual control")
    print("10. sector geometry licensing insertion or parent closure")

    with out.governance_assessments():
        out.line(
            "sector-geometry problem ledger failure controls stated",
            StatusMark.OBLIGATION,
            "future scripts must define no-overlap rather than invoking it",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Sector-pairing/no-overlap geometry opening result:")
    print()
    print("  The no-overlap geometry burden is explicit.")
    print("  Candidate sectors are named, but membership is not derived.")
    print("  Pairing/incidence/projection/routing criteria remain open.")
    print("  Safe trace must remain zeta_to_Bs / zeta_Bs.")
    print("  zeta/kappa residuals are not inert or killed by sector labels.")
    print("  accounting sectors cannot hide residual geometry.")
    print("  support/source disjointness alone is insufficient.")
    print("  recovery and repair may not select sector geometry.")
    print("  sector geometry does not construct O, residual control, insertion, or parent equation.")
    print()
    print("Possible next script:")
    print("  candidate_sector_inventory.py")
    print()
    print("Tiny goblin label:")
    print("  No overlap is not a word. It is a trap with measurements.")

    with out.governance_assessments():
        out.line(
            "sector-pairing/no-overlap geometry problem ledger complete",
            StatusMark.PASS,
            "no-overlap geometry target stated; pairing remains not derived",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, symbols: SectorProblemSymbols) -> None:
    ns.record_derivation(
        derivation_id="g28_sector_problem",
        inputs=[
            symbols.inventory_gap,
            symbols.membership_gap,
            symbols.pairing_gap,
            symbols.incidence_gap,
            symbols.projection_gap,
            symbols.routing_gap,
            symbols.support_gap,
            symbols.divergence_gap,
            symbols.recovery_gap,
            symbols.insertion_gap,
            symbols.parent_gap,
        ],
        output=symbols.geometry_burden,
        method="state sector-pairing/no-overlap geometry construction burden",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="sector_problem_marker",
        scope="Group 28 sector pairing/no-overlap geometry",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g28_sector_inventory", "Inventory candidate sectors"),
        ("g28_sector_membership", "Define sector membership rules"),
        ("g28_pairing", "Define pairing/incidence/projection/routing criterion"),
        ("g28_trace_preserve", "Preserve zeta_to_Bs safe trace sector"),
        ("g28_residual_class", "Classify zeta/kappa residual sectors without label erasure"),
        ("g28_accounting", "Prevent accounting no-overlap reservoir"),
        ("g28_guardrails", "Preserve boundary/source/support independence"),
        ("g28_divergence", "Audit divergence-safe sector split"),
        ("g28_recovery", "Prevent recovery-selected sector geometry"),
        ("g28_downstream", "Keep O/residual/insertion/parent gates closed"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g28_sector_route"],
            description=(
                "No-overlap sector geometry is not derived here. This obligation must be closed before sector geometry can support active O or residual control."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g28_sector_inventory",
        "g28_sector_membership",
        "g28_pairing",
        "g28_trace_preserve",
        "g28_residual_class",
        "g28_accounting",
        "g28_guardrails",
        "g28_divergence",
        "g28_recovery",
        "g28_downstream",
    ]

    ns.record_route(RouteRecord(
        route_id="g28_sector_route",
        script_id=SCRIPT_ID,
        name="Group 28 sector-pairing/no-overlap geometry route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "no-overlap is treated as a geometry construction target, not a label",
            "ordinary orthogonality and projection algebra are not assumed",
            "support/source disjointness is not full proof",
            "recovery and repair do not select sector geometry",
            "O, residual control, insertion, and parent gates remain closed",
        ],
    ))

    for branch_id in [
        "orthogonality_by_habit",
        "sector_split_by_naming",
        "support_as_full_no_overlap",
        "source_as_full_no_overlap",
        "diagnostic_as_inert",
        "recovery_selected_geometry",
        "repair_selected_geometry",
        "geometry_as_O",
        "geometry_as_residual_control",
        "geometry_licenses_insertion",
        "geometry_opens_parent",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; no-overlap geometry must be derived and cannot open downstream gates.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g28_sector_problem_open",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "The sector-pairing/no-overlap geometry burden is explicit, but no pairing or no-overlap criterion is derived. "
            "Candidate sectors are named only as construction targets. Orthogonality by habit, sector split by naming, support/source separation as full proof, "
            "recovery-selected geometry, repair-selected geometry, active-O upgrade, residual-control upgrade, insertion licensing, and parent opening are rejected."
        ),
        derivation_ids=["g28_sector_problem"],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Sector Problem Ledger")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    tasks = build_tasks()
    guardrails = build_guardrails()
    forbidden = build_forbidden_uses()
    boundaries = build_boundaries()

    case_0_problem_statement(out)
    case_1_symbol_ledger(symbols, out)
    case_2_tasks(tasks, out)
    case_3_guardrails(guardrails, out)
    case_4_forbidden_uses(forbidden, out)
    case_5_boundaries(boundaries, out)
    case_6_failure_controls(out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns, symbols)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
