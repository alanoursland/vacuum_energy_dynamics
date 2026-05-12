# Candidate sector inventory
#
# Group:
#   28_sector_pairing_no_overlap
#
# Script type:
#   SECTOR INVENTORY
#
# Purpose
# -------
# Inventory the candidate sectors needed before no-overlap can be meaningful.
#
# Locked-door question:
#
#   What sectors must the theory distinguish before no-overlap can be meaningful?
#
# This script does not derive sector membership rules.
# It does not derive a pairing or incidence relation.
# It does not derive active O.
# It does not derive residual control.
# It does not derive B_s/F_zeta insertion.
# It does not derive parent equation closure.
#
# Tiny goblin rule:
#
#   Name the rooms before drawing the doors.

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
        "ADMISSIBLE_CANDIDATE": StatusMark.INFO,
        "AUXILIARY_CANDIDATE": StatusMark.INFO,
        "CANDIDATE": StatusMark.DEFER,
        "DIAGNOSTIC_CANDIDATE": StatusMark.INFO,
        "EXCLUDED": StatusMark.FAIL,
        "FORBIDDEN": StatusMark.FAIL,
        "NOT_DERIVED": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "PARENT_EXCLUDED": StatusMark.FAIL,
        "PRESERVE": StatusMark.OBLIGATION,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "UNDERDETERMINED": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g28_sector_problem",
            "28_sector_pairing_no_overlap__candidate_sector_problem_ledger",
            "g28_sector_problem",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g27_summary",
            "27_active_O_construction__candidate_group_27_status_summary",
            "g27_status_summary",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g27_ob",
            "27_active_O_construction__candidate_O_obligations",
            "g27_O_obligations",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g26_summary",
            "26_residual_control_theorem_attempt__candidate_group_26_status_summary",
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
class SectorInventorySymbols:
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
    sector_tuple: sp.Tuple
    admissible_tuple: sp.Tuple
    excluded_tuple: sp.Tuple
    inventory_gap: sp.Symbol
    membership_gap: sp.Symbol
    inventory_load: sp.Expr


@dataclass
class SectorCandidate:
    name: str
    symbol: str
    meaning: str
    status: str
    allowed_role: str
    hazard: str


@dataclass
class SectorBoundary:
    name: str
    boundary: str
    status: str
    meaning: str


@dataclass
class InventoryTest:
    name: str
    test: str
    status: str
    result: str
    implication: str


@dataclass
class RejectedInventoryShortcut:
    name: str
    shortcut: str
    status: str
    reason: str


@dataclass
class InventoryConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


# =============================================================================
# Builders
# =============================================================================


def build_symbols() -> SectorInventorySymbols:
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
    ) = sp.symbols(
        "T_zeta R_zeta R_kappa A_eps A_kappa S_src B_bdy J_cur M_A U_sup D_diag P_parent inventory_gap membership_gap",
        real=True,
    )

    sector_tuple = sp.Tuple(
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
    )

    admissible_tuple = sp.Tuple(
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
    )

    excluded_tuple = sp.Tuple(P_parent)
    inventory_load = sp.simplify(inventory_gap + membership_gap)

    return SectorInventorySymbols(
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
        sector_tuple=sector_tuple,
        admissible_tuple=admissible_tuple,
        excluded_tuple=excluded_tuple,
        inventory_gap=inventory_gap,
        membership_gap=membership_gap,
        inventory_load=inventory_load,
    )


def build_sector_candidates() -> List[SectorCandidate]:
    return [
        SectorCandidate(
            name="S1: safe scalar trace sector",
            symbol="T_zeta",
            meaning="zeta_to_Bs / zeta_Bs safe trace route",
            status="ADMISSIBLE_CANDIDATE",
            allowed_role="candidate safe ordinary scalar trace sector",
            hazard="safe trace sector accidentally admits residual zeta/kappa reentry",
        ),
        SectorCandidate(
            name="S2: zeta residual sector",
            symbol="R_zeta",
            meaning="zeta_residual_metric sector",
            status="ADMISSIBLE_CANDIDATE",
            allowed_role="candidate residual sector requiring classification",
            hazard="residual zeta is declared inert/killed by naming",
        ),
        SectorCandidate(
            name="S3: kappa residual sector",
            symbol="R_kappa",
            meaning="kappa_metric residual sector",
            status="ADMISSIBLE_CANDIDATE",
            allowed_role="candidate residual sector requiring classification",
            hazard="kappa residual is declared diagnostic or harmless by naming",
        ),
        SectorCandidate(
            name="S4: epsilon accounting sector",
            symbol="A_eps",
            meaning="epsilon_vac accounting sector",
            status="AUXILIARY_CANDIDATE",
            allowed_role="accounting sector if non-reservoir discipline is preserved",
            hazard="epsilon accounting hides residual metric/source load",
        ),
        SectorCandidate(
            name="S5: e_kappa accounting sector",
            symbol="A_kappa",
            meaning="e_kappa accounting sector",
            status="AUXILIARY_CANDIDATE",
            allowed_role="accounting sector if non-reservoir discipline is preserved",
            hazard="e_kappa accounting hides kappa/zeta residual geometry",
        ),
        SectorCandidate(
            name="S6: ordinary source sector",
            symbol="S_src",
            meaning="ordinary source / source-routing sector",
            status="AUXILIARY_CANDIDATE",
            allowed_role="source audit sector",
            hazard="source routing treated as full no-overlap proof",
        ),
        SectorCandidate(
            name="S7: boundary sector",
            symbol="B_bdy",
            meaning="boundary scalar-tail, shell, or boundary-load sector",
            status="AUXILIARY_CANDIDATE",
            allowed_role="boundary audit sector",
            hazard="boundary failure selects sector geometry",
        ),
        SectorCandidate(
            name="S8: current sector",
            symbol="J_cur",
            meaning="current-flux sector",
            status="AUXILIARY_CANDIDATE",
            allowed_role="current-flux audit sector",
            hazard="current leakage hidden by sector split",
        ),
        SectorCandidate(
            name="S9: A-sector mass",
            symbol="M_A",
            meaning="A-sector mass / mass accounting sector",
            status="AUXILIARY_CANDIDATE",
            allowed_role="mass audit sector",
            hazard="mass shift hidden as residual cleanup",
        ),
        SectorCandidate(
            name="S10: support/matching sector",
            symbol="U_sup",
            meaning="support, smoothing, transition, seam, and matching data",
            status="AUXILIARY_CANDIDATE",
            allowed_role="support/matching audit sector",
            hazard="support disjointness treated as full no-overlap proof",
        ),
        SectorCandidate(
            name="S11: diagnostic sector",
            symbol="D_diag",
            meaning="diagnostic-only bookkeeping sector",
            status="DIAGNOSTIC_CANDIDATE",
            allowed_role="audit-only sector if no constructive role is derived",
            hazard="diagnostic label is upgraded to inertness theorem",
        ),
        SectorCandidate(
            name="S12: parent sector",
            symbol="P_parent",
            meaning="parent field-equation sector",
            status="PARENT_EXCLUDED",
            allowed_role="listed only for explicit exclusion",
            hazard="sector inventory opens parent equation",
        ),
    ]


def build_boundaries() -> List[SectorBoundary]:
    return [
        SectorBoundary(
            name="B1: inventory not membership",
            boundary="naming a sector does not define membership",
            status="REQUIRED",
            meaning="membership rules must be derived next",
        ),
        SectorBoundary(
            name="B2: inventory not pairing",
            boundary="naming sectors does not define overlap",
            status="REQUIRED",
            meaning="pairing/incidence/projection/routing criterion remains open",
        ),
        SectorBoundary(
            name="B3: inventory not O",
            boundary="sector inventory does not construct active O",
            status="REQUIRED",
            meaning="O still needs kernel/image, algebraic law, divergence, and guardrails",
        ),
        SectorBoundary(
            name="B4: inventory not residual control",
            boundary="sector inventory does not close residual control",
            status="REQUIRED",
            meaning="residual non-reentry and count-once recombination remain open",
        ),
        SectorBoundary(
            name="B5: parent sector excluded",
            boundary="parent sector is explicitly excluded from construction",
            status="REQUIRED",
            meaning="parent equation remains closed",
        ),
    ]


def build_tests() -> List[InventoryTest]:
    return [
        InventoryTest(
            name="T1: inventory completeness",
            test="does the inventory include trace, residual, accounting, source, boundary, current, mass, support, diagnostic, and parent-exclusion sectors?",
            status="CANDIDATE",
            result="yes, as candidate labels",
            implication="inventory is broad enough for next membership audit",
        ),
        InventoryTest(
            name="T2: safe trace uniqueness",
            test="does T_zeta preserve zeta_to_Bs as the safe trace candidate?",
            status="CANDIDATE",
            result="yes, as inventory label only",
            implication="safe trace sector still needs membership rule",
        ),
        InventoryTest(
            name="T3: residual sector classification",
            test="are R_zeta and R_kappa classified as inert or killed?",
            status="NOT_DERIVED",
            result="no; they are candidate residual sectors only",
            implication="no residual control is gained from inventory",
        ),
        InventoryTest(
            name="T4: accounting reservoir test",
            test="do A_eps and A_kappa absorb residual geometry?",
            status="REJECTED",
            result="no; accounting sectors are listed only with non-reservoir guardrail",
            implication="accounting cannot solve zeta/kappa geometry",
        ),
        InventoryTest(
            name="T5: support/source sufficiency test",
            test="do source/support sectors define no-overlap by themselves?",
            status="REJECTED",
            result="no; they are auxiliary audit sectors",
            implication="source/support disjointness is insufficient alone",
        ),
        InventoryTest(
            name="T6: parent sector test",
            test="is P_parent an admissible construction sector?",
            status="PARENT_EXCLUDED",
            result="no; it is included only for exclusion",
            implication="parent equation remains closed",
        ),
    ]


def build_shortcuts() -> List[RejectedInventoryShortcut]:
    return [
        RejectedInventoryShortcut(
            name="F1: sector label as membership",
            shortcut="named sector treated as derived membership rule",
            status="REJECTED",
            reason="membership rules remain open",
        ),
        RejectedInventoryShortcut(
            name="F2: inventory as pairing",
            shortcut="sector inventory treated as no-overlap pairing",
            status="REJECTED",
            reason="pairing/incidence criterion remains open",
        ),
        RejectedInventoryShortcut(
            name="F3: residual sector as inertness",
            shortcut="R_zeta or R_kappa label makes residuals inert",
            status="REJECTED",
            reason="residual non-reentry is not derived",
        ),
        RejectedInventoryShortcut(
            name="F4: diagnostic sector as theorem",
            shortcut="D_diag label makes diagnostic data non-constructive by theorem",
            status="REJECTED",
            reason="diagnostic-only status must be controlled by a rule",
        ),
        RejectedInventoryShortcut(
            name="F5: support/source as full proof",
            shortcut="S_src or U_sup disjointness treated as full no-overlap",
            status="REJECTED",
            reason="source/support separation is insufficient alone",
        ),
        RejectedInventoryShortcut(
            name="F6: parent sector admitted",
            shortcut="P_parent used as active construction sector",
            status="REJECTED",
            reason="parent equation remains excluded",
        ),
    ]


def build_conclusions() -> List[InventoryConclusion]:
    return [
        InventoryConclusion(
            name="C1: sector inventory",
            conclusion="candidate sector inventory is available",
            status="CANDIDATE",
            meaning="the theory has a named list of sectors to test",
        ),
        InventoryConclusion(
            name="C2: membership",
            conclusion="sector membership rules are not derived",
            status="NOT_DERIVED",
            meaning="membership is the next target",
        ),
        InventoryConclusion(
            name="C3: no-overlap",
            conclusion="no-overlap pairing/incidence is not derived",
            status="NOT_DERIVED",
            meaning="inventory does not define overlap",
        ),
        InventoryConclusion(
            name="C4: residual control",
            conclusion="residual control is not advanced to closure",
            status="NOT_DERIVED",
            meaning="R_zeta and R_kappa remain unresolved",
        ),
        InventoryConclusion(
            name="C5: parent",
            conclusion="parent sector is excluded",
            status="PARENT_EXCLUDED",
            meaning="parent equation remains not ready",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Sector inventory problem")
    print("Question:")
    print()
    print("  What sectors must the theory distinguish before no-overlap can be meaningful?")
    print()
    print("Reference discipline:")
    print()
    print("  Sector names are not sector membership rules.")
    print("  Sector inventory is not no-overlap pairing.")
    print("  Parent sector is included only to exclude it.")

    with out.governance_assessments():
        out.line(
            "sector inventory opened",
            StatusMark.INFO,
            "inventorying candidate sectors without deriving membership or pairing",
        )


def case_1_symbol_ledger(symbols: SectorInventorySymbols, out: ScriptOutput) -> None:
    header("Case 1: Sector inventory symbolic ledger")
    print("Full candidate sector tuple:")
    print()
    print(f"  sectors = {sp.sstr(symbols.sector_tuple)}")
    print()
    print("Admissible candidate sector tuple:")
    print()
    print(f"  admissible = {sp.sstr(symbols.admissible_tuple)}")
    print()
    print("Excluded sector tuple:")
    print()
    print(f"  excluded = {sp.sstr(symbols.excluded_tuple)}")
    print()
    print("Inventory load:")
    print()
    print(f"  L_sector_inventory = {sp.sstr(symbols.inventory_load)}")
    print()
    print("Interpretation:")
    print()
    print("  Inventory and membership remain distinct.")
    print("  Parent sector is excluded from construction.")

    with out.derived_results():
        out.line(
            "sector inventory candidate ledger stated",
            StatusMark.OBLIGATION,
            f"sectors = {sp.sstr(symbols.sector_tuple)}",
        )


def case_2_sector_candidates(items: List[SectorCandidate], out: ScriptOutput) -> None:
    header("Case 2: Candidate sector inventory")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Symbol: {item.symbol}")
        print(f"Meaning: {item.meaning}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Allowed role: {item.allowed_role}")
        print(f"Hazard: {item.hazard}")

    with out.governance_assessments():
        out.line(
            "candidate sector inventory classified",
            StatusMark.PASS,
            f"{len(items)} sector candidates classified",
        )


def case_3_boundaries(items: List[SectorBoundary], out: ScriptOutput) -> None:
    header("Case 3: Inventory boundaries")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Boundary: {item.boundary}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Meaning: {item.meaning}")

    with out.governance_assessments():
        out.line(
            "sector inventory boundaries stated",
            StatusMark.PASS,
            "inventory is not membership, pairing, active O, residual control, or parent closure",
        )


def case_4_tests(items: List[InventoryTest], out: ScriptOutput) -> None:
    header("Case 4: Inventory tests")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Test: {item.test}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Result: {item.result}")
        print(f"Implication: {item.implication}")

    with out.governance_assessments():
        out.line(
            "sector inventory tests completed",
            StatusMark.DEFER,
            "candidate inventory exists; membership and pairing remain open",
        )


def case_5_shortcuts(items: List[RejectedInventoryShortcut], out: ScriptOutput) -> None:
    header("Case 5: Rejected inventory shortcuts")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Shortcut: {item.shortcut}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Reason: {item.reason}")

    with out.counterexamples():
        out.line(
            "sector inventory shortcuts rejected",
            StatusMark.FAIL,
            "sector label as membership, inventory as pairing, residual sector as inertness, diagnostic theorem, support/source proof, and parent admission are rejected",
        )


def case_6_conclusions(items: List[InventoryConclusion], out: ScriptOutput) -> None:
    header("Case 6: Sector inventory conclusions")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Conclusion: {item.conclusion}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Meaning: {item.meaning}")

    with out.governance_assessments():
        out.line(
            "sector inventory conclusion stated",
            StatusMark.DEFER,
            "candidate inventory available; membership rules are next",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Sector inventory result:")
    print()
    print("  Candidate sector inventory is available.")
    print("  T_zeta is the candidate safe scalar trace sector.")
    print("  R_zeta and R_kappa are candidate residual sectors, not inert/killed sectors.")
    print("  A_eps and A_kappa are accounting sectors only if no-reservoir discipline is preserved.")
    print("  source, boundary, current, mass, and support sectors are audit sectors, not full no-overlap proof.")
    print("  diagnostic sector is audit-only unless a rule is derived.")
    print("  parent sector is excluded.")
    print("  Sector membership rules are not derived.")
    print("  No-overlap pairing/incidence is not derived.")
    print()
    print("Possible next script:")
    print("  candidate_sector_membership_rules.py")
    print()
    print("Tiny goblin label:")
    print("  Name the rooms before drawing the doors.")

    with out.governance_assessments():
        out.line(
            "sector inventory complete",
            StatusMark.PASS,
            "candidate sectors classified; membership rules remain next",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, symbols: SectorInventorySymbols) -> None:
    ns.record_derivation(
        derivation_id="g28_sector_inventory",
        inputs=[
            symbols.T_zeta,
            symbols.R_zeta,
            symbols.R_kappa,
            symbols.A_eps,
            symbols.A_kappa,
            symbols.S_src,
            symbols.B_bdy,
            symbols.J_cur,
            symbols.M_A,
            symbols.U_sup,
            symbols.D_diag,
            symbols.P_parent,
        ],
        output=sp.Tuple(symbols.admissible_tuple, symbols.excluded_tuple),
        method="inventory candidate sectors for no-overlap geometry and exclude parent sector",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="sector_inventory_marker",
        scope="Group 28 sector pairing/no-overlap geometry",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g28_inv_membership", "Derive sector membership rules"),
        ("g28_inv_pairing", "Derive pairing/incidence criterion"),
        ("g28_inv_trace", "Preserve T_zeta safe trace sector"),
        ("g28_inv_residual", "Classify R_zeta/R_kappa without inertness by label"),
        ("g28_inv_accounting", "Prevent accounting reservoir"),
        ("g28_inv_audit", "Keep source/boundary/current/mass/support sectors as audit sectors"),
        ("g28_inv_diag", "Control diagnostic-only sector"),
        ("g28_inv_parent", "Keep parent sector excluded"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g28_inv_route"],
            description=(
                "Candidate sector inventory is available, but membership and no-overlap pairing are not derived."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g28_inv_membership",
        "g28_inv_pairing",
        "g28_inv_trace",
        "g28_inv_residual",
        "g28_inv_accounting",
        "g28_inv_audit",
        "g28_inv_diag",
        "g28_inv_parent",
    ]

    ns.record_route(RouteRecord(
        route_id="g28_inv_route",
        script_id=SCRIPT_ID,
        name="Group 28 sector inventory route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "sector inventory is not treated as membership rule",
            "sector inventory is not treated as no-overlap pairing",
            "R_zeta/R_kappa are not inert by label",
            "parent sector remains excluded",
        ],
    ))

    for branch_id in [
        "sector_label_as_membership",
        "inventory_as_pairing",
        "residual_sector_as_inertness",
        "diagnostic_sector_as_theorem",
        "support_source_as_full_proof",
        "parent_sector_admitted",
        "inventory_as_active_O",
        "inventory_as_residual_control",
        "inventory_as_parent_closure",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; sector inventory does not derive membership, no-overlap, O, residual control, or parent closure.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g28_inventory_not_pairing",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Candidate sector inventory is available: T_zeta, R_zeta, R_kappa, A_eps, A_kappa, S_src, B_bdy, J_cur, M_A, U_sup, D_diag, with P_parent excluded. "
            "This inventory does not derive sector membership or no-overlap pairing. Residual sectors are not inert by label; accounting cannot be reservoir; "
            "source/boundary/current/mass/support are audit sectors; parent equation remains closed."
        ),
        derivation_ids=["g28_sector_inventory"],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Sector Inventory")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    sectors = build_sector_candidates()
    boundaries = build_boundaries()
    tests = build_tests()
    shortcuts = build_shortcuts()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_symbol_ledger(symbols, out)
    case_2_sector_candidates(sectors, out)
    case_3_boundaries(boundaries, out)
    case_4_tests(tests, out)
    case_5_shortcuts(shortcuts, out)
    case_6_conclusions(conclusions, out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns, symbols)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
