# Candidate source duplicate load ledger
#
# Group:
#   31_source_divergence_coefficient_law
#
# Script type:
#   DUPLICATE SOURCE LOAD LEDGER
#
# Purpose
# -------
# Inventory all ways ordinary source load could be duplicated through coefficient,
# residual, boundary, correction, exchange, curvature, or parent placeholders.
#
# Locked-door question:
#
#   Where can ordinary source load hide or duplicate if B_s/F_zeta coefficient
#   behavior is not source-neutral?
#
# This script does not adopt a new postulate.
# It does not derive source no-double-counting.
# It does not derive divergence-safe coefficient law.
# It does not derive B_s/F_zeta insertion.
# It does not construct active O.
# It does not derive residual control.
# It does not open the parent equation.
#
# Tiny goblin rule:
#
#   Count every pocket before saying the gold is not duplicated.

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


def status_mark(status: str) -> StatusMark:
    return {
        "BLOCKED": StatusMark.FAIL,
        "DUPLICATE_RISK": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "THEOREM_TARGET": StatusMark.OBLIGATION,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g31_problem",
            "31_source_divergence_coefficient_law__candidate_source_divergence_problem_ledger",
            "g31_source_divergence_problem",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g30_summary",
            "30_minimal_coefficient_sector_postulate_inventory__candidate_group_30_status_summary",
            "g30_status_summary",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g29_summary",
            "29_Bs_Fzeta_coefficient_origin__candidate_group_29_status_summary",
            "g29_status_summary",
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


@dataclass
class DuplicateSourceSymbols:
    rho_A: sp.Symbol
    rho_coeff: sp.Symbol
    rho_zeta_res: sp.Symbol
    rho_kappa_res: sp.Symbol
    rho_boundary: sp.Symbol
    rho_support: sp.Symbol
    rho_corr: sp.Symbol
    rho_exchange: sp.Symbol
    rho_curvature: sp.Symbol
    rho_parent: sp.Symbol
    L_dup_core: sp.Expr
    L_dup_extended: sp.Expr


@dataclass
class DuplicateChannel:
    name: str
    channel: str
    status: str
    risk: str
    required_condition: str


@dataclass
class DuplicateTest:
    name: str
    test: str
    status: str
    result: str
    caution: str


@dataclass
class RejectedMove:
    name: str
    move: str
    status: str
    reason: str


@dataclass
class DuplicateObligation:
    name: str
    obligation: str
    status: str
    blocks: str
    discipline: str


@dataclass
class DuplicateConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_symbols() -> DuplicateSourceSymbols:
    (
        rho_A,
        rho_coeff,
        rho_zeta_res,
        rho_kappa_res,
        rho_boundary,
        rho_support,
        rho_corr,
        rho_exchange,
        rho_curvature,
        rho_parent,
    ) = sp.symbols(
        "rho_A rho_coeff rho_zeta_res rho_kappa_res rho_boundary rho_support "
        "rho_corr rho_exchange rho_curvature rho_parent",
        real=True,
    )

    L_dup_core = sp.simplify(
        rho_coeff + rho_zeta_res + rho_kappa_res + rho_boundary + rho_corr
    )

    L_dup_extended = sp.simplify(
        L_dup_core + rho_support + rho_exchange + rho_curvature + rho_parent
    )

    return DuplicateSourceSymbols(
        rho_A=rho_A,
        rho_coeff=rho_coeff,
        rho_zeta_res=rho_zeta_res,
        rho_kappa_res=rho_kappa_res,
        rho_boundary=rho_boundary,
        rho_support=rho_support,
        rho_corr=rho_corr,
        rho_exchange=rho_exchange,
        rho_curvature=rho_curvature,
        rho_parent=rho_parent,
        L_dup_core=L_dup_core,
        L_dup_extended=L_dup_extended,
    )


def build_channels() -> List[DuplicateChannel]:
    return [
        DuplicateChannel(
            name="D1: A-sector protected load",
            channel="rho_A",
            status="REQUIRED",
            risk="ordinary source must be carried once as A-sector mass charge",
            required_condition="rho_A remains the only ordinary source load carrier unless another carrier is independently derived neutral",
        ),
        DuplicateChannel(
            name="D2: coefficient channel",
            channel="rho_coeff",
            status="DUPLICATE_RISK",
            risk="coefficient silently carries ordinary rho/M_enc",
            required_condition="rho_coeff = 0 sector-by-sector or derived source-neutral coefficient law",
        ),
        DuplicateChannel(
            name="D3: zeta residual channel",
            channel="rho_zeta_res",
            status="DUPLICATE_RISK",
            risk="ordinary source hidden in zeta residual",
            required_condition="rho_zeta_res = 0 sector-by-sector or derived neutral residual route",
        ),
        DuplicateChannel(
            name="D4: kappa residual channel",
            channel="rho_kappa_res",
            status="DUPLICATE_RISK",
            risk="ordinary source hidden in kappa residual",
            required_condition="rho_kappa_res = 0 sector-by-sector or derived neutral residual route",
        ),
        DuplicateChannel(
            name="D5: boundary channel",
            channel="rho_boundary",
            status="DUPLICATE_RISK",
            risk="source hidden at boundary/matching layer",
            required_condition="rho_boundary = 0 sector-by-sector or derived boundary neutrality",
        ),
        DuplicateChannel(
            name="D6: support channel",
            channel="rho_support",
            status="DUPLICATE_RISK",
            risk="source hidden in support/compactness/matching assumptions",
            required_condition="rho_support = 0 sector-by-sector or derived support neutrality",
        ),
        DuplicateChannel(
            name="D7: correction channel",
            channel="rho_corr",
            status="DUPLICATE_RISK",
            risk="source hidden in correction/divergence term",
            required_condition="rho_corr = 0 sector-by-sector or derived explicit non-reservoir correction law",
        ),
        DuplicateChannel(
            name="D8: exchange channel",
            channel="rho_exchange",
            status="DUPLICATE_RISK",
            risk="source hidden as exchange between trace/residual/source sectors",
            required_condition="rho_exchange = 0 sector-by-sector or derived exchange-neutral theorem",
        ),
        DuplicateChannel(
            name="D9: curvature channel",
            channel="rho_curvature",
            status="DUPLICATE_RISK",
            risk="ordinary source smuggled as curvature response before coefficient law is derived",
            required_condition="rho_curvature = 0 sector-by-sector or derived geometric identity independent of recovery",
        ),
        DuplicateChannel(
            name="D10: parent placeholder",
            channel="rho_parent",
            status="DUPLICATE_RISK",
            risk="source hidden in parent equation placeholder",
            required_condition="rho_parent = 0; parent gate remains closed",
        ),
    ]


def build_tests(symbols: DuplicateSourceSymbols) -> List[DuplicateTest]:
    return [
        DuplicateTest(
            name="T1: core duplicate source load",
            test=f"L_dup_core = {sp.sstr(symbols.L_dup_core)}",
            status="THEOREM_TARGET",
            result="all core non-A carriers must vanish or be derived neutral sector-by-sector",
            caution="total cancellation is not enough",
        ),
        DuplicateTest(
            name="T2: extended duplicate source load",
            test=f"L_dup_extended = {sp.sstr(symbols.L_dup_extended)}",
            status="THEOREM_TARGET",
            result="extended support/exchange/curvature/parent pockets must also be audited",
            caution="do not let hidden channels escape because they are not in first ledger",
        ),
        DuplicateTest(
            name="T3: A-sector uniqueness",
            test="ordinary source load is carried once by rho_A",
            status="REQUIRED",
            result="rho_A remains protected source carrier",
            caution="this is routing discipline, not parent equation",
        ),
        DuplicateTest(
            name="T4: coefficient neutrality target",
            test="rho_coeff = 0 or coefficient law independently source-neutral",
            status="OPEN",
            result="left for source no-double-counting tests",
            caution="do not choose coefficient by repair",
        ),
        DuplicateTest(
            name="T5: correction neutrality target",
            test="rho_corr = 0 or correction law independently non-reservoir",
            status="OPEN",
            result="left for divergence reservoir obstruction",
            caution="do not hide source in correction",
        ),
    ]


def build_rejected_moves() -> List[RejectedMove]:
    return [
        RejectedMove(
            name="R1: total cancellation",
            move="allow duplicate source pockets because total L_dup cancels",
            status="REJECTED",
            reason="source no-double-counting requires sector-by-sector discipline",
        ),
        RejectedMove(
            name="R2: coefficient repair",
            move="choose coefficient so rho_coeff cancels other source leakage",
            status="REJECTED",
            reason="repair may reject but not select coefficient",
        ),
        RejectedMove(
            name="R3: residual hiding",
            move="hide ordinary source in rho_zeta_res or rho_kappa_res",
            status="REJECTED",
            reason="residuals remain visible and cannot be ordinary source reservoirs",
        ),
        RejectedMove(
            name="R4: boundary hiding",
            move="hide ordinary source at boundary/support/matching layer",
            status="REJECTED",
            reason="guardrail visibility survived only as candidate, not as adopted repair rule",
        ),
        RejectedMove(
            name="R5: correction hiding",
            move="hide ordinary source in divergence/correction term",
            status="REJECTED",
            reason="correction must be explicit and non-reservoir",
        ),
        RejectedMove(
            name="R6: curvature smuggling",
            move="rename ordinary source as curvature response before coefficient law is derived",
            status="REJECTED",
            reason="geometric response cannot be selected by source repair or recovery",
        ),
        RejectedMove(
            name="R7: parent placeholder",
            move="place ordinary source in parent equation placeholder",
            status="REJECTED",
            reason="parent gate remains closed",
        ),
    ]


def build_obligations() -> List[DuplicateObligation]:
    return [
        DuplicateObligation(
            name="O1: sector-by-sector audit",
            obligation="audit every non-A source carrier sector-by-sector",
            status="OPEN",
            blocks="source no-double-counting theorem route",
            discipline="no total cancellation shortcut",
        ),
        DuplicateObligation(
            name="O2: coefficient test",
            obligation="test rho_coeff source neutrality in next source no-double-counting script",
            status="OPEN",
            blocks="coefficient source neutrality",
            discipline="do not choose coefficient by repair",
        ),
        DuplicateObligation(
            name="O3: residual test",
            obligation="ensure zeta/kappa residual channels do not carry ordinary source load",
            status="OPEN",
            blocks="residual visibility",
            discipline="do not hide source in residual labels",
        ),
        DuplicateObligation(
            name="O4: correction test",
            obligation="carry rho_corr into divergence reservoir obstruction",
            status="OPEN",
            blocks="divergence-safe behavior",
            discipline="correction must be non-reservoir",
        ),
        DuplicateObligation(
            name="O5: downstream gates",
            obligation="keep insertion, active O, residual control, and parent equation closed",
            status="NOT_READY",
            blocks="premature closure",
            discipline="duplicate source ledger is not source theorem or insertion",
        ),
    ]


def build_conclusions() -> List[DuplicateConclusion]:
    return [
        DuplicateConclusion(
            name="C1: ledger complete",
            conclusion="duplicate source channels are explicitly inventoried",
            status="REQUIRED",
            meaning="ordinary source can no longer hide without being named",
        ),
        DuplicateConclusion(
            name="C2: no theorem yet",
            conclusion="source no-double-counting is not derived",
            status="NOT_DERIVED",
            meaning="this script only names duplicate-load channels",
        ),
        DuplicateConclusion(
            name="C3: sector discipline",
            conclusion="sector-by-sector zero or derived neutral route is required",
            status="THEOREM_TARGET",
            meaning="total cancellation is rejected",
        ),
        DuplicateConclusion(
            name="C4: no adoption",
            conclusion="no Group 30 candidate postulate is adopted",
            status="NOT_ADOPTED",
            meaning="candidate survival remains non-adoption",
        ),
        DuplicateConclusion(
            name="C5: next",
            conclusion="coefficient source no-double-counting tests should run next",
            status="OPEN",
            meaning="rho_coeff is the central next channel",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Duplicate source load problem")
    print("Question:")
    print()
    print("  Where can ordinary source load hide or duplicate if B_s/F_zeta coefficient behavior is not source-neutral?")
    print()
    print("Discipline:")
    print()
    print("  This script inventories source pockets.")
    print("  It derives no source no-double-counting theorem.")
    print("  It adopts no postulate.")
    print()
    print("Tiny goblin rule:")
    print("  Count every pocket before saying the gold is not duplicated.")

    with out.governance_assessments():
        out.line(
            "duplicate source load ledger opened",
            StatusMark.INFO,
            "inventorying ordinary source duplicate channels",
        )


def case_1_symbolic_ledger(symbols: DuplicateSourceSymbols, out: ScriptOutput) -> None:
    header("Case 1: Duplicate source symbolic ledger")
    print("Duplicate source symbols:")
    print()
    for name in [
        "rho_A",
        "rho_coeff",
        "rho_zeta_res",
        "rho_kappa_res",
        "rho_boundary",
        "rho_support",
        "rho_corr",
        "rho_exchange",
        "rho_curvature",
        "rho_parent",
    ]:
        print(f"  {name} = {sp.sstr(getattr(symbols, name))}")

    print()
    print("Core duplicate source load:")
    print(f"  L_dup_core = {sp.sstr(symbols.L_dup_core)}")
    print()
    print("Extended duplicate source load:")
    print(f"  L_dup_extended = {sp.sstr(symbols.L_dup_extended)}")

    with out.derived_results():
        out.line(
            "duplicate source ledgers stated",
            StatusMark.OBLIGATION,
            f"L_dup_extended = {sp.sstr(symbols.L_dup_extended)}",
        )


def case_2_channels(items: List[DuplicateChannel], out: ScriptOutput) -> None:
    header("Case 2: Duplicate source channels")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Channel: {item.channel}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Risk: {item.risk}")
        print(f"Required condition: {item.required_condition}")

    with out.governance_assessments():
        out.line(
            "duplicate source channels inventoried",
            StatusMark.DEFER,
            f"{len(items)} channels inventoried",
        )


def case_3_tests(items: List[DuplicateTest], out: ScriptOutput) -> None:
    header("Case 3: Duplicate source tests")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Test: {item.test}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Result: {item.result}")
        print(f"Caution: {item.caution}")

    with out.unresolved_obligations():
        out.line(
            "duplicate source tests stated",
            StatusMark.OBLIGATION,
            f"{len(items)} duplicate source tests stated",
        )


def case_4_rejected(items: List[RejectedMove], out: ScriptOutput) -> None:
    header("Case 4: Rejected duplicate-source moves")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Move: {item.move}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Reason: {item.reason}")

    with out.counterexamples():
        out.line(
            "duplicate source hiding moves rejected",
            StatusMark.FAIL,
            "total cancellation, coefficient repair, residual hiding, boundary hiding, correction hiding, curvature smuggling, parent placeholder rejected",
        )


def case_5_obligations(items: List[DuplicateObligation], out: ScriptOutput) -> None:
    header("Case 5: Duplicate source obligations")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Obligation: {item.obligation}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Blocks: {item.blocks}")
        print(f"Discipline: {item.discipline}")

    with out.unresolved_obligations():
        out.line(
            "duplicate source obligations stated",
            StatusMark.OBLIGATION,
            f"{len(items)} obligations remain",
        )


def case_6_conclusions(items: List[DuplicateConclusion], out: ScriptOutput) -> None:
    header("Case 6: Duplicate source conclusions")
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
            "duplicate source ledger conclusion stated",
            StatusMark.PASS,
            "duplicate channels inventoried; source theorem still open",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Duplicate source load ledger result:")
    print()
    print("  Duplicate source channels are explicitly inventoried.")
    print("  Source no-double-counting is not derived yet.")
    print("  Sector-by-sector zero or a derived neutral route is required.")
    print("  Total cancellation is rejected.")
    print("  Coefficient, residual, boundary, support, correction, exchange, curvature, and parent hiding routes are rejected as shortcuts.")
    print("  No postulate is adopted.")
    print("  B_s/F_zeta insertion is not derived.")
    print("  Active O, residual control, and parent equation remain not ready.")
    print()
    print("Possible next script:")
    print("  candidate_coefficient_source_no_double_counting_tests.py")
    print()
    print("Tiny goblin label:")
    print("  Count every pocket before saying the gold is not duplicated.")

    with out.governance_assessments():
        out.line(
            "duplicate source load ledger complete",
            StatusMark.PASS,
            "coefficient source no-double-counting tests should run next",
        )


def record_derivations(ns, symbols: DuplicateSourceSymbols) -> None:
    ns.record_derivation(
        derivation_id="g31_source_duplicate_ledger",
        inputs=[
            symbols.rho_coeff,
            symbols.rho_zeta_res,
            symbols.rho_kappa_res,
            symbols.rho_boundary,
            symbols.rho_support,
            symbols.rho_corr,
            symbols.rho_exchange,
            symbols.rho_curvature,
            symbols.rho_parent,
        ],
        output=symbols.L_dup_extended,
        method="inventory duplicate ordinary source load channels",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="source_duplicate_load_ledger_marker",
        scope="Group 31 source/divergence coefficient law",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g31_dup_sector_audit", "Audit duplicate source channels sector-by-sector"),
        ("g31_dup_coeff_test", "Test coefficient source neutrality next"),
        ("g31_dup_residual_test", "Prevent residual source hiding"),
        ("g31_dup_boundary_support_test", "Prevent boundary/support source hiding"),
        ("g31_dup_correction_test", "Carry correction source hiding into divergence reservoir obstruction"),
        ("g31_dup_no_total_cancellation", "Reject total cancellation shortcut"),
        ("g31_dup_downstream_closed", "Keep insertion/O/residual/parent gates closed"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g31_source_duplicate_route"],
            description=(
                "Duplicate source channels are inventoried. Source no-double-counting is not yet derived."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g31_dup_sector_audit",
        "g31_dup_coeff_test",
        "g31_dup_residual_test",
        "g31_dup_boundary_support_test",
        "g31_dup_correction_test",
        "g31_dup_no_total_cancellation",
        "g31_dup_downstream_closed",
    ]

    ns.record_route(RouteRecord(
        route_id="g31_source_duplicate_route",
        script_id=SCRIPT_ID,
        name="Group 31 duplicate source load ledger route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "duplicate source channels are inventoried",
            "sector-by-sector zero or derived neutral route required",
            "source no-double-counting remains theorem target",
            "no postulate adopted",
            "downstream gates remain closed",
        ],
    ))

    for branch_id in [
        "total_cancellation_shortcut",
        "coefficient_repair_source_cancellation",
        "residual_source_hiding",
        "boundary_support_source_hiding",
        "correction_source_hiding",
        "curvature_source_smuggling",
        "parent_source_placeholder",
        "duplicate_ledger_as_source_theorem",
        "duplicate_ledger_as_insertion",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; duplicate source ledger is not theorem closure.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g31_source_duplicate_ledger_result",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Duplicate source channels are explicitly inventoried. Source no-double-counting is not derived. Sector-by-sector zero or a derived neutral route is required; total cancellation is rejected. "
            "Coefficient, residual, boundary, support, correction, exchange, curvature, and parent hiding routes are rejected as shortcuts. No postulate is adopted. "
            "B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready."
        ),
        derivation_ids=["g31_source_duplicate_ledger"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Source Duplicate Load Ledger")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    channels = build_channels()
    tests = build_tests(symbols)
    rejected = build_rejected_moves()
    obligations = build_obligations()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_symbolic_ledger(symbols, out)
    case_2_channels(channels, out)
    case_3_tests(tests, out)
    case_4_rejected(rejected, out)
    case_5_obligations(obligations, out)
    case_6_conclusions(conclusions, out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns, symbols)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
