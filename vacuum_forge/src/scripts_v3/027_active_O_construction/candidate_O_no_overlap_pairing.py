# Candidate O no overlap pairing
#
# Group:
#   27_active_O_construction
#
# Script type:
#   NO-OVERLAP CRITERION INVENTORY
#
# Purpose
# -------
# Test candidate meanings of "no overlap" for active O.
#
# Locked-door question:
#
#   What does no-overlap mean mathematically?
#
# This script does not derive active O.
# It does not prove kernel/image closure.
# It does not prove O is a projection.
# It does not derive residual control.
# It does not derive B_s/F_zeta insertion.
# It does not open parent equation closure.
#
# Tiny goblin rule:
#
#   No overlap is not a spell. It needs teeth.

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
        "BLOCKED": StatusMark.FAIL,
        "CANDIDATE": StatusMark.DEFER,
        "INSUFFICIENT": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "PARTIAL": StatusMark.INFO,
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
            "g27_O_problem",
            "27_active_O_construction__candidate_O_problem_ledger",
            "g27_O_problem",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g27_dc",
            "27_active_O_construction__candidate_O_domain_codomain",
            "g27_O_domain_codomain",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g27_ki",
            "27_active_O_construction__candidate_O_kernel_image",
            "g27_O_kernel_image",
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
class PairingSymbols:
    zeta_Bs: sp.Symbol
    zeta_res: sp.Symbol
    kappa_res: sp.Symbol
    eps_acc: sp.Symbol
    ekappa_acc: sp.Symbol
    P_trace: sp.Symbol
    P_res: sp.Symbol
    P_acc: sp.Symbol
    P_src: sp.Symbol
    P_bdy: sp.Symbol
    pairing_gap: sp.Symbol
    sector_gap: sp.Symbol
    support_gap: sp.Symbol
    routing_gap: sp.Symbol
    criterion_gap: sp.Symbol
    no_overlap_gap: sp.Expr


@dataclass
class PairingCandidate:
    name: str
    candidate: str
    status: str
    works_if: str
    hazard: str


@dataclass
class NoOverlapCriterion:
    name: str
    criterion: str
    status: str
    required_for: str
    fails_if: str


@dataclass
class PairingTest:
    name: str
    test: str
    status: str
    result: str
    implication: str


@dataclass
class RejectedPairingShortcut:
    name: str
    shortcut: str
    status: str
    reason: str


@dataclass
class PairingConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


# =============================================================================
# Builders
# =============================================================================


def build_symbols() -> PairingSymbols:
    (
        zeta_Bs,
        zeta_res,
        kappa_res,
        eps_acc,
        ekappa_acc,
        P_trace,
        P_res,
        P_acc,
        P_src,
        P_bdy,
        pairing_gap,
        sector_gap,
        support_gap,
        routing_gap,
        criterion_gap,
    ) = sp.symbols(
        "zeta_Bs zeta_res kappa_res eps_acc ekappa_acc P_trace P_res P_acc P_src P_bdy "
        "pairing_gap sector_gap support_gap routing_gap criterion_gap",
        real=True,
    )

    no_overlap_gap = sp.simplify(pairing_gap + sector_gap + support_gap + routing_gap + criterion_gap)

    return PairingSymbols(
        zeta_Bs=zeta_Bs,
        zeta_res=zeta_res,
        kappa_res=kappa_res,
        eps_acc=eps_acc,
        ekappa_acc=ekappa_acc,
        P_trace=P_trace,
        P_res=P_res,
        P_acc=P_acc,
        P_src=P_src,
        P_bdy=P_bdy,
        pairing_gap=pairing_gap,
        sector_gap=sector_gap,
        support_gap=support_gap,
        routing_gap=routing_gap,
        criterion_gap=criterion_gap,
        no_overlap_gap=no_overlap_gap,
    )


def build_pairing_candidates() -> List[PairingCandidate]:
    return [
        PairingCandidate(
            name="P1: algebraic pairing",
            candidate="<trace, residual> = 0",
            status="UNDERDETERMINED",
            works_if="the theory supplies a bilinear or compatible pairing on trace/residual sectors",
            hazard="ordinary Hilbert orthogonality is assumed without structure",
        ),
        PairingCandidate(
            name="P2: sector projection split",
            candidate="P_trace P_res = 0 with complementary sectors",
            status="CANDIDATE",
            works_if="trace and residual sectors are structurally defined and composition is meaningful",
            hazard="projection algebra is assumed before deriving O law",
        ),
        PairingCandidate(
            name="P3: support disjointness",
            candidate="safe trace and residual sectors have disjoint support",
            status="INSUFFICIENT",
            works_if="support split is structural and survives smoothing/matching",
            hazard="support disjointness fails in transition layers or hides boundary terms",
        ),
        PairingCandidate(
            name="P4: source-routing disjointness",
            candidate="safe trace and residual/source channels route to disjoint source roles",
            status="INSUFFICIENT",
            works_if="source-routing split is derived and prevents source duplication",
            hazard="source routing protects sources but not necessarily metric trace",
        ),
        PairingCandidate(
            name="P5: trace/inert-sector separation",
            candidate="safe trace sector and inert sector have no reentry map",
            status="CANDIDATE",
            works_if="inert sector is proven no metric/source/boundary/support/recovery/parent role",
            hazard="inert sector exists by label only",
        ),
        PairingCandidate(
            name="P6: recovery-defined orthogonality",
            candidate="choose no-overlap because recovery works",
            status="REJECTED",
            works_if="never allowed",
            hazard="recovery constructs O",
        ),
    ]


def build_criteria() -> List[NoOverlapCriterion]:
    return [
        NoOverlapCriterion(
            name="C1: no double trace",
            criterion="zeta_Bs may enter safe trace sector, while zeta_res/kappa_res do not enter ordinary metric trace",
            status="REQUIRED",
            required_for="count-once scalar trace",
            fails_if="zeta or kappa residuals re-enter safe trace sector",
        ),
        NoOverlapCriterion(
            name="C2: no source duplication",
            criterion="residual separation must not create or hide ordinary source load",
            status="REQUIRED",
            required_for="source no-double-counting",
            fails_if="O maps residuals into source role or removes source evidence",
        ),
        NoOverlapCriterion(
            name="C3: no boundary/support repair",
            criterion="no-overlap must not be chosen from boundary, current, tail, shell, or support failure",
            status="REQUIRED",
            required_for="boundary/source/support guardrail preservation",
            fails_if="O is selected by repair need",
        ),
        NoOverlapCriterion(
            name="C4: no accounting reservoir",
            criterion="epsilon/e_kappa cannot receive hidden residual metric/source load",
            status="REQUIRED",
            required_for="accounting discipline",
            fails_if="accounting sector hides zeta/kappa residual geometry",
        ),
        NoOverlapCriterion(
            name="C5: no recovery selection",
            criterion="AB=1, B=1/A, Schwarzschild, gamma, PPN, or weak-field success cannot define no-overlap",
            status="REQUIRED",
            required_for="recovery independence",
            fails_if="recovery target chooses pairing or sectors",
        ),
        NoOverlapCriterion(
            name="C6: no parent gate",
            criterion="no-overlap does not imply parent equation readiness",
            status="REQUIRED",
            required_for="parent-gate closure",
            fails_if="pairing/criterion opens parent equation",
        ),
    ]


def build_tests() -> List[PairingTest]:
    return [
        PairingTest(
            name="T1: can a pairing be named now?",
            test="does current structure provide a mathematical pairing <.,.>?",
            status="NOT_DERIVED",
            result="no explicit pairing is derived in this script",
            implication="orthogonality cannot be claimed yet",
        ),
        PairingTest(
            name="T2: can sector projection be used now?",
            test="do current sectors define P_trace and P_res with P_trace P_res = 0?",
            status="UNDERDETERMINED",
            result="sector split is plausible but composition law is missing",
            implication="projection law must be tested next",
        ),
        PairingTest(
            name="T3: is support disjointness enough?",
            test="would support disjointness alone define no-overlap?",
            status="INSUFFICIENT",
            result="no; support disjointness does not by itself control trace/source/reentry behavior",
            implication="support split may assist but cannot close O",
        ),
        PairingTest(
            name="T4: is source-routing disjointness enough?",
            test="would source-routing disjointness alone define no-overlap?",
            status="INSUFFICIENT",
            result="no; source routing does not by itself control metric trace residuals",
            implication="source routing may assist but cannot define full O",
        ),
        PairingTest(
            name="T5: is inert-sector separation enough?",
            test="can residuals be mapped to inert sector now?",
            status="UNDERDETERMINED",
            result="not yet; inert sector safety requires no-reentry theorem",
            implication="inert-sector image remains candidate only",
        ),
        PairingTest(
            name="T6: does no-overlap derive kernel/image closure?",
            test="does this script close kernel/image?",
            status="NOT_DERIVED",
            result="no; it inventories criteria and leaves operator law open",
            implication="projection/replacement law must be tested next",
        ),
    ]


def build_shortcuts() -> List[RejectedPairingShortcut]:
    return [
        RejectedPairingShortcut(
            name="S1: orthogonality by habit",
            shortcut="assume ordinary inner-product orthogonality",
            status="REJECTED",
            reason="the theory has not supplied that pairing",
        ),
        RejectedPairingShortcut(
            name="S2: sector split by naming",
            shortcut="call trace and residual sectors disjoint",
            status="REJECTED",
            reason="sector split must have composition/no-reentry content",
        ),
        RejectedPairingShortcut(
            name="S3: support disjointness as full O",
            shortcut="use disjoint support as full no-overlap operator",
            status="REJECTED",
            reason="support does not by itself control trace/source/reentry",
        ),
        RejectedPairingShortcut(
            name="S4: source disjointness as full O",
            shortcut="use source-routing separation as full no-overlap operator",
            status="REJECTED",
            reason="source routing does not by itself control metric trace",
        ),
        RejectedPairingShortcut(
            name="S5: inert by label",
            shortcut="map residuals to inert sector by vocabulary",
            status="REJECTED",
            reason="inertness requires no-reentry theorem",
        ),
        RejectedPairingShortcut(
            name="S6: recovery-defined pairing",
            shortcut="choose pairing because recovery works",
            status="REJECTED",
            reason="recovery may audit but not construct O",
        ),
        RejectedPairingShortcut(
            name="S7: pairing licenses insertion",
            shortcut="no-overlap pairing licenses B_s/F_zeta insertion",
            status="REJECTED",
            reason="insertion law remains separate",
        ),
        RejectedPairingShortcut(
            name="S8: pairing opens parent",
            shortcut="no-overlap pairing opens parent equation",
            status="REJECTED",
            reason="parent gate remains closed",
        ),
    ]


def build_conclusions() -> List[PairingConclusion]:
    return [
        PairingConclusion(
            name="K1: pairing",
            conclusion="no explicit mathematical pairing is derived",
            status="NOT_DERIVED",
            meaning="orthogonality cannot yet be claimed",
        ),
        PairingConclusion(
            name="K2: sector projection split",
            conclusion="sector-projection no-overlap remains the best candidate structure",
            status="CANDIDATE",
            meaning="requires projection/replacement law next",
        ),
        PairingConclusion(
            name="K3: support/source disjointness",
            conclusion="support and source disjointness are insufficient alone",
            status="INSUFFICIENT",
            meaning="they may be guardrail aids but not full no-overlap criterion",
        ),
        PairingConclusion(
            name="K4: inert-sector separation",
            conclusion="inert-sector image remains underdetermined",
            status="UNDERDETERMINED",
            meaning="requires no-reentry theorem or operator law",
        ),
        PairingConclusion(
            name="K5: next route",
            conclusion="test projection/replacement law for O",
            status="OPEN",
            meaning="no-overlap criterion points to algebraic operator law as next target",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: O no-overlap pairing problem")
    print("Question:")
    print()
    print("  What does no-overlap mean mathematically?")
    print()
    print("Reference discipline:")
    print()
    print("  No-overlap cannot mean 'looks separate'.")
    print("  It must be a pairing, sector split, support/source rule, or no-reentry law with actual content.")
    print("  This script inventories candidates; it does not derive O.")

    with out.governance_assessments():
        out.line(
            "O no-overlap pairing inventory opened",
            StatusMark.INFO,
            "testing candidate meanings of no-overlap without deriving O",
        )


def case_1_symbol_ledger(symbols: PairingSymbols, out: ScriptOutput) -> None:
    header("Case 1: No-overlap symbolic ledger")
    print("Candidate sector projectors / roles:")
    print()
    print(f"  P_trace = {sp.sstr(symbols.P_trace)}")
    print(f"  P_res   = {sp.sstr(symbols.P_res)}")
    print(f"  P_acc   = {sp.sstr(symbols.P_acc)}")
    print(f"  P_src   = {sp.sstr(symbols.P_src)}")
    print(f"  P_bdy   = {sp.sstr(symbols.P_bdy)}")
    print()
    print("No-overlap gap:")
    print()
    print(f"  L_no_overlap_gap = {sp.sstr(symbols.no_overlap_gap)}")
    print()
    print("Interpretation:")
    print()
    print("  Pairing, sector split, support split, routing split, and criterion gaps remain open.")
    print("  No-overlap cannot close until at least one criterion has real operator content.")

    with out.derived_results():
        out.line(
            "O no-overlap candidate ledger stated",
            StatusMark.OBLIGATION,
            f"L_no_overlap_gap = {sp.sstr(symbols.no_overlap_gap)}",
        )


def case_2_pairing_candidates(items: List[PairingCandidate], out: ScriptOutput) -> None:
    header("Case 2: Candidate no-overlap structures")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Candidate: {item.candidate}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Works if: {item.works_if}")
        print(f"Hazard: {item.hazard}")

    with out.governance_assessments():
        out.line(
            "O no-overlap candidates classified",
            StatusMark.PASS,
            f"{len(items)} no-overlap candidates classified",
        )


def case_3_criteria(items: List[NoOverlapCriterion], out: ScriptOutput) -> None:
    header("Case 3: Required no-overlap criteria")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Criterion: {item.criterion}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Required for: {item.required_for}")
        print(f"Fails if: {item.fails_if}")

    with out.unresolved_obligations():
        out.line(
            "O no-overlap criteria stated",
            StatusMark.OBLIGATION,
            f"{len(items)} criteria must be preserved by any no-overlap law",
        )


def case_4_tests(items: List[PairingTest], out: ScriptOutput) -> None:
    header("Case 4: No-overlap tests")
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
            "O no-overlap tests completed",
            StatusMark.DEFER,
            "no explicit pairing derived; sector projection split remains candidate",
        )


def case_5_shortcuts(items: List[RejectedPairingShortcut], out: ScriptOutput) -> None:
    header("Case 5: Rejected no-overlap shortcuts")
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
            "O no-overlap shortcuts rejected",
            StatusMark.FAIL,
            "orthogonality by habit, sector split by naming, support/source disjointness as full O, inert by label, recovery-defined pairing, insertion, and parent shortcuts are rejected",
        )


def case_6_conclusions(items: List[PairingConclusion], out: ScriptOutput) -> None:
    header("Case 6: No-overlap conclusions")
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
            "O no-overlap conclusion stated",
            StatusMark.DEFER,
            "pairing not derived; sector projection split remains candidate; projection/replacement law is next",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("O no-overlap pairing result:")
    print()
    print("  No explicit mathematical pairing is derived.")
    print("  Orthogonality cannot yet be claimed.")
    print("  Sector-projection no-overlap is the best current candidate structure.")
    print("  Support disjointness and source-routing disjointness are insufficient by themselves.")
    print("  Inert-sector image remains underdetermined.")
    print("  No-overlap does not license insertion or parent closure.")
    print("  Projection/replacement law should be tested next.")
    print("  O is not derived by this script.")
    print()
    print("Possible next script:")
    print("  candidate_O_projection_law.py")
    print()
    print("Tiny goblin label:")
    print("  No overlap is not a spell. It needs teeth.")

    with out.governance_assessments():
        out.line(
            "O no-overlap pairing inventory complete",
            StatusMark.PASS,
            "no explicit pairing derived; sector-projection law remains next candidate",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, symbols: PairingSymbols) -> None:
    ns.record_derivation(
        derivation_id="g27_O_pairing",
        inputs=[
            symbols.pairing_gap,
            symbols.sector_gap,
            symbols.support_gap,
            symbols.routing_gap,
            symbols.criterion_gap,
        ],
        output=symbols.no_overlap_gap,
        method="state candidate no-overlap pairing/criterion gaps",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="O_pairing_marker",
        scope="Group 27 active O construction",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g27_pair_define", "Define mathematical pairing or no-overlap criterion"),
        ("g27_pair_sector", "Test sector projection split"),
        ("g27_pair_support", "Classify support disjointness as insufficient or auxiliary"),
        ("g27_pair_source", "Classify source-routing disjointness as insufficient or auxiliary"),
        ("g27_pair_inert", "Derive inert-sector no-reentry if used"),
        ("g27_pair_no_recovery", "Prevent recovery-defined pairing"),
        ("g27_pair_no_downstream", "Keep insertion and parent gates closed"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g27_pair_route"],
            description=(
                "No explicit no-overlap pairing is derived here. Sector projection remains candidate and must be tested as an operator law."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g27_pair_define",
        "g27_pair_sector",
        "g27_pair_support",
        "g27_pair_source",
        "g27_pair_inert",
        "g27_pair_no_recovery",
        "g27_pair_no_downstream",
    ]

    ns.record_route(RouteRecord(
        route_id="g27_pair_route",
        script_id=SCRIPT_ID,
        name="Group 27 O no-overlap pairing route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "no-overlap criterion is treated as open",
            "ordinary orthogonality is not assumed",
            "support/source disjointness is not treated as full O",
            "recovery does not define pairing",
            "insertion and parent gates remain closed",
        ],
    ))

    for branch_id in [
        "orthogonality_by_habit",
        "sector_split_by_naming",
        "support_as_full_O",
        "source_as_full_O",
        "inert_by_label",
        "recovery_defined_pairing",
        "pairing_licenses_insertion",
        "pairing_opens_parent",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; no-overlap criterion must have real mathematical content.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g27_pair_not_derived",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "No explicit mathematical no-overlap pairing is derived. Orthogonality cannot yet be claimed. "
            "Sector-projection no-overlap is the best current candidate structure; support/source disjointness are insufficient alone; "
            "inert-sector image remains underdetermined. No-overlap does not license insertion or parent closure."
        ),
        derivation_ids=["g27_O_pairing"],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate O No Overlap Pairing")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    candidates = build_pairing_candidates()
    criteria = build_criteria()
    tests = build_tests()
    shortcuts = build_shortcuts()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_symbol_ledger(symbols, out)
    case_2_pairing_candidates(candidates, out)
    case_3_criteria(criteria, out)
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
