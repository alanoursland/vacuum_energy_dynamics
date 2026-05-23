# Candidate recovery smuggling filter
#
# Group:
#   29_Bs_Fzeta_coefficient_origin
#
# Script type:
#   RECOVERY-SMUGGLING FILTER
#
# Purpose
# -------
# Reject coefficient normalizations selected from AB=1, B=1/A,
# Schwarzschild, gamma/PPN, weak-field success, kappa=0, active O convenience,
# residual cleanup, repair, or parent-fit closure.
#
# Locked-door question:
#
#   Which apparent coefficient-origin routes are only recovery or repair smuggling?
#
# This script does not derive B_s/F_zeta insertion.
# It does not derive no-overlap sector geometry.
# It does not construct active O.
# It does not derive residual control.
# It does not open the parent equation.
#
# Tiny goblin rule:
#
#   Do not paint the key after seeing the lock.

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
        "AUDIT_ONLY": StatusMark.INFO,
        "FILTERED": StatusMark.FAIL,
        "FORBIDDEN": StatusMark.FAIL,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "SAFE_IF": StatusMark.INFO,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g29_volume_trace",
            "29_Bs_Fzeta_coefficient_origin__candidate_volume_trace_coefficient_origin",
            "g29_volume_trace",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g29_problem",
            "29_Bs_Fzeta_coefficient_origin__candidate_coefficient_origin_problem_ledger",
            "g29_coeff_problem",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g28_summary",
            "28_sector_pairing_no_overlap__candidate_group_28_status_summary",
            "g28_status_summary",
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
class SmugglingSymbols:
    c_Bs: sp.Symbol
    c_vol: sp.Symbol
    c_rec: sp.Symbol
    AB1: sp.Symbol
    BinvA: sp.Symbol
    Schw: sp.Symbol
    gamma_ppn: sp.Symbol
    weak: sp.Symbol
    kappa0: sp.Symbol
    O_active: sp.Symbol
    parent_fit: sp.Symbol
    recovery_gap: sp.Symbol
    repair_gap: sp.Symbol
    residual_gap: sp.Symbol
    parent_gap: sp.Symbol
    insertion_gap: sp.Symbol
    smuggling_load: sp.Expr


@dataclass
class SmugglingCandidate:
    name: str
    route: str
    status: str
    reason: str
    allowed_use: str


@dataclass
class FilterTest:
    name: str
    test: str
    status: str
    result: str
    implication: str


@dataclass
class FilterRequirement:
    name: str
    requirement: str
    status: str
    needed_for: str
    fails_if: str


@dataclass
class FilterConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_symbols() -> SmugglingSymbols:
    (
        c_Bs,
        c_vol,
        c_rec,
        AB1,
        BinvA,
        Schw,
        gamma_ppn,
        weak,
        kappa0,
        O_active,
        parent_fit,
        recovery_gap,
        repair_gap,
        residual_gap,
        parent_gap,
        insertion_gap,
    ) = sp.symbols(
        "c_Bs c_vol c_rec AB1 BinvA Schw gamma_ppn weak kappa0 O_active parent_fit "
        "recovery_gap repair_gap residual_gap parent_gap insertion_gap",
        real=True,
    )

    smuggling_load = sp.simplify(recovery_gap + repair_gap + residual_gap + parent_gap + insertion_gap)

    return SmugglingSymbols(
        c_Bs=c_Bs,
        c_vol=c_vol,
        c_rec=c_rec,
        AB1=AB1,
        BinvA=BinvA,
        Schw=Schw,
        gamma_ppn=gamma_ppn,
        weak=weak,
        kappa0=kappa0,
        O_active=O_active,
        parent_fit=parent_fit,
        recovery_gap=recovery_gap,
        repair_gap=repair_gap,
        residual_gap=residual_gap,
        parent_gap=parent_gap,
        insertion_gap=insertion_gap,
        smuggling_load=smuggling_load,
    )


def build_candidates() -> List[SmugglingCandidate]:
    return [
        SmugglingCandidate(
            name="S1: AB=1-selected coefficient",
            route="choose c_Bs so AB=1",
            status="REJECTED",
            reason="AB=1 is downstream recovery audit, not coefficient origin",
            allowed_use="audit after construction only",
        ),
        SmugglingCandidate(
            name="S2: B=1/A-selected coefficient",
            route="choose c_Bs so B=1/A",
            status="REJECTED",
            reason="reciprocal exterior factor is recovery target, not origin law",
            allowed_use="audit after construction only",
        ),
        SmugglingCandidate(
            name="S3: Schwarzschild-selected coefficient",
            route="choose c_Bs from Schwarzschild exterior success",
            status="REJECTED",
            reason="Schwarzschild recovery may validate but not construct coefficient",
            allowed_use="phenomenological audit only",
        ),
        SmugglingCandidate(
            name="S4: gamma/PPN-selected coefficient",
            route="choose c_Bs so gamma/PPN works",
            status="REJECTED",
            reason="PPN recovery cannot define coefficient origin",
            allowed_use="weak-field/phenomenology audit only",
        ),
        SmugglingCandidate(
            name="S5: weak-field-only coefficient",
            route="choose c_Bs from weak-field success alone",
            status="REJECTED",
            reason="weak-field success without structural origin is recovery smuggling",
            allowed_use="audit only after structural origin",
        ),
        SmugglingCandidate(
            name="S6: kappa=0-selected coefficient",
            route="choose c_Bs to force kappa_areal=0",
            status="REJECTED",
            reason="kappa diagnostic cannot define residual-sector or coefficient origin",
            allowed_use="diagnostic audit only",
        ),
        SmugglingCandidate(
            name="S7: residual-cleanup coefficient",
            route="choose c_Bs to hide zeta/kappa residual trace",
            status="REJECTED",
            reason="coefficient cannot perform residual control by repair",
            allowed_use="none as construction",
        ),
        SmugglingCandidate(
            name="S8: source/boundary repair coefficient",
            route="choose c_Bs to repair source, boundary, current, mass, or support failure",
            status="REJECTED",
            reason="guardrail failure may reject a coefficient but cannot select it",
            allowed_use="failure audit only",
        ),
        SmugglingCandidate(
            name="S9: active-O-selected coefficient",
            route="choose c_Bs to make active O possible",
            status="REJECTED",
            reason="active O is not constructed and cannot choose coefficient",
            allowed_use="none as construction",
        ),
        SmugglingCandidate(
            name="S10: parent-fit-selected coefficient",
            route="choose c_Bs so parent equation closes",
            status="REJECTED",
            reason="parent equation remains closed",
            allowed_use="none",
        ),
        SmugglingCandidate(
            name="S11: volume/trace structural coefficient",
            route="use volume/trace algebra as candidate source",
            status="SAFE_IF",
            reason="allowed only if normalization is not chosen from recovery",
            allowed_use="candidate origin to be tested further",
        ),
    ]


def build_tests() -> List[FilterTest]:
    return [
        FilterTest(
            name="T1: recovery-selection test",
            test="does route choose coefficient from recovery target?",
            status="FILTERED",
            result="AB=1, B=1/A, Schwarzschild, gamma/PPN, weak-field, and kappa=0 routes are rejected",
            implication="recovery may audit only after coefficient origin exists",
        ),
        FilterTest(
            name="T2: repair-selection test",
            test="does route choose coefficient to fix source/boundary/current/mass/support failure?",
            status="FILTERED",
            result="repair-selected coefficients are rejected",
            implication="guardrails may reject but cannot construct",
        ),
        FilterTest(
            name="T3: residual-cleanup test",
            test="does route choose coefficient to hide residual zeta/kappa trace?",
            status="FILTERED",
            result="residual-cleanup coefficient is rejected",
            implication="coefficient origin is not residual control",
        ),
        FilterTest(
            name="T4: active-O convenience test",
            test="does route choose coefficient to make active O possible?",
            status="FILTERED",
            result="active-O-selected coefficient is rejected",
            implication="O cannot select what O needs",
        ),
        FilterTest(
            name="T5: parent-fit test",
            test="does route choose coefficient to close parent field equation?",
            status="FILTERED",
            result="parent-fit-selected coefficient is rejected",
            implication="parent gate remains closed",
        ),
        FilterTest(
            name="T6: structural survival test",
            test="does volume/trace route survive the filter?",
            status="SAFE_IF",
            result="yes, as candidate only",
            implication="volume/trace candidate may proceed to membership bridge audit",
        ),
    ]


def build_requirements() -> List[FilterRequirement]:
    return [
        FilterRequirement(
            name="R1: origin-before-recovery",
            requirement="derive coefficient origin before applying recovery audits",
            status="REQUIRED",
            needed_for="anti-smuggling",
            fails_if="coefficient is chosen from AB=1 or Schwarzschild",
        ),
        FilterRequirement(
            name="R2: no repair selection",
            requirement="guardrail failure may reject but not select coefficient",
            status="REQUIRED",
            needed_for="source/boundary/current/mass/support discipline",
            fails_if="coefficient repairs leakage by definition",
        ),
        FilterRequirement(
            name="R3: no residual cleanup",
            requirement="coefficient must not erase residual zeta/kappa trace",
            status="REQUIRED",
            needed_for="residual-control honesty",
            fails_if="coefficient becomes hidden residual operator",
        ),
        FilterRequirement(
            name="R4: no O selection",
            requirement="active O cannot select coefficient",
            status="REQUIRED",
            needed_for="operator discipline",
            fails_if="coefficient chosen to make O possible",
        ),
        FilterRequirement(
            name="R5: no parent selection",
            requirement="parent-fit closure cannot select coefficient",
            status="REQUIRED",
            needed_for="parent gate closure",
            fails_if="coefficient chosen from parent identity or closure",
        ),
    ]


def build_conclusions() -> List[FilterConclusion]:
    return [
        FilterConclusion(
            name="C1: recovery routes",
            conclusion="recovery-selected coefficients are rejected",
            status="REJECTED",
            meaning="AB=1, B=1/A, Schwarzschild, gamma/PPN, weak-field, and kappa=0 cannot fix coefficient",
        ),
        FilterConclusion(
            name="C2: repair routes",
            conclusion="repair-selected coefficients are rejected",
            status="REJECTED",
            meaning="source/boundary/current/mass/support failure cannot choose coefficient",
        ),
        FilterConclusion(
            name="C3: residual cleanup",
            conclusion="residual-cleanup coefficients are rejected",
            status="REJECTED",
            meaning="coefficient origin is not residual control",
        ),
        FilterConclusion(
            name="C4: structural survivor",
            conclusion="volume/trace route survives as candidate only",
            status="SAFE_IF",
            meaning="it can be tested as structural origin but not upgraded to insertion",
        ),
        FilterConclusion(
            name="C5: next route",
            conclusion="coefficient membership bridge should be audited next",
            status="OPEN",
            meaning="test whether surviving coefficient origin improves zeta_Bs -> T_zeta",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Recovery-smuggling filter problem")
    print("Question:")
    print()
    print("  Which apparent coefficient-origin routes are only recovery or repair smuggling?")
    print()
    print("Discipline:")
    print()
    print("  Recovery may audit only after construction.")
    print("  Repair may reject but not select.")
    print("  Parent-fit closure may not choose coefficient.")
    print()
    print("Tiny goblin rule:")
    print("  Do not paint the key after seeing the lock.")

    with out.governance_assessments():
        out.line(
            "recovery-smuggling filter opened",
            StatusMark.INFO,
            "filtering coefficient-origin routes against recovery, repair, residual-cleanup, active-O, and parent smuggling",
        )


def case_1_symbolic_ledger(symbols: SmugglingSymbols, out: ScriptOutput) -> None:
    header("Case 1: Smuggling-filter symbolic ledger")
    print("Smuggling-filter symbols:")
    print()
    for name in [
        "c_Bs",
        "c_vol",
        "c_rec",
        "AB1",
        "BinvA",
        "Schw",
        "gamma_ppn",
        "weak",
        "kappa0",
        "O_active",
        "parent_fit",
    ]:
        print(f"  {name} = {sp.sstr(getattr(symbols, name))}")
    print()
    print("Smuggling-filter load:")
    print()
    print(f"  L_smuggling_filter = {sp.sstr(symbols.smuggling_load)}")

    with out.derived_results():
        out.line(
            "smuggling-filter load stated",
            StatusMark.OBLIGATION,
            f"L_smuggling_filter = {sp.sstr(symbols.smuggling_load)}",
        )


def case_2_candidates(items: List[SmugglingCandidate], out: ScriptOutput) -> None:
    header("Case 2: Coefficient-origin route filter")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Route: {item.route}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Reason: {item.reason}")
        print(f"Allowed use: {item.allowed_use}")

    with out.governance_assessments():
        out.line(
            "coefficient-origin routes filtered",
            StatusMark.PASS,
            f"{len(items)} coefficient-origin routes filtered",
        )


def case_3_tests(items: List[FilterTest], out: ScriptOutput) -> None:
    header("Case 3: Smuggling-filter tests")
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
            "smuggling-filter tests completed",
            StatusMark.PASS,
            "recovery/repair/residual/O/parent selected coefficients rejected; volume/trace survives as candidate",
        )


def case_4_requirements(items: List[FilterRequirement], out: ScriptOutput) -> None:
    header("Case 4: Smuggling-filter requirements")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Requirement: {item.requirement}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Needed for: {item.needed_for}")
        print(f"Fails if: {item.fails_if}")

    with out.unresolved_obligations():
        out.line(
            "smuggling-filter requirements stated",
            StatusMark.OBLIGATION,
            f"{len(items)} anti-smuggling requirements remain active",
        )


def case_5_conclusions(items: List[FilterConclusion], out: ScriptOutput) -> None:
    header("Case 5: Smuggling-filter conclusions")
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
            "smuggling-filter conclusion stated",
            StatusMark.PASS,
            "coefficient membership bridge should be audited next",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Recovery-smuggling filter result:")
    print()
    print("  Recovery-selected coefficients are rejected.")
    print("  AB=1, B=1/A, Schwarzschild, gamma/PPN, weak-field, and kappa=0 cannot fix coefficient.")
    print("  Repair-selected coefficients are rejected.")
    print("  Residual-cleanup coefficients are rejected.")
    print("  Active-O-selected coefficients are rejected.")
    print("  Parent-fit-selected coefficients are rejected.")
    print("  Volume/trace route survives as candidate only.")
    print("  B_s/F_zeta insertion is not derived.")
    print("  Active O, residual control, and parent equation remain not ready.")
    print()
    print("Possible next script:")
    print("  candidate_coefficient_membership_bridge.py")
    print()
    print("Tiny goblin label:")
    print("  Do not paint the key after seeing the lock.")

    with out.governance_assessments():
        out.line(
            "recovery-smuggling filter complete",
            StatusMark.PASS,
            "volume/trace survives as candidate; membership bridge should be audited next",
        )


def record_derivations(ns, symbols: SmugglingSymbols) -> None:
    ns.record_derivation(
        derivation_id="g29_recovery_filter",
        inputs=[
            symbols.recovery_gap,
            symbols.repair_gap,
            symbols.residual_gap,
            symbols.parent_gap,
            symbols.insertion_gap,
        ],
        output=symbols.smuggling_load,
        method="filter coefficient-origin routes against recovery, repair, residual-cleanup, active-O, and parent-fit smuggling",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="recovery_smuggling_filter_marker",
        scope="Group 29 B_s/F_zeta coefficient origin",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g29_filter_origin_first", "Derive coefficient origin before recovery audit"),
        ("g29_filter_no_repair", "Prevent repair-selected coefficient"),
        ("g29_filter_no_residual", "Prevent residual-cleanup coefficient"),
        ("g29_filter_no_O", "Prevent active-O-selected coefficient"),
        ("g29_filter_no_parent", "Prevent parent-fit-selected coefficient"),
        ("g29_filter_membership_next", "Audit coefficient membership bridge next"),
        ("g29_filter_downstream", "Keep insertion/O/residual/parent gates closed"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g29_filter_route"],
            description=(
                "Recovery, repair, residual-cleanup, active-O, and parent-fit selected coefficients are rejected. Volume/trace survives as candidate only."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g29_filter_origin_first",
        "g29_filter_no_repair",
        "g29_filter_no_residual",
        "g29_filter_no_O",
        "g29_filter_no_parent",
        "g29_filter_membership_next",
        "g29_filter_downstream",
    ]

    ns.record_route(RouteRecord(
        route_id="g29_filter_route",
        script_id=SCRIPT_ID,
        name="Group 29 recovery-smuggling filter route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "recovery may audit only after construction",
            "repair may reject but not select",
            "residual cleanup cannot select coefficient",
            "active O cannot select coefficient",
            "parent fit cannot select coefficient",
            "volume/trace candidate proceeds only as candidate",
        ],
    ))

    for branch_id in [
        "AB1_selected_coefficient",
        "B_inverse_A_selected_coefficient",
        "Schwarzschild_selected_coefficient",
        "gamma_PPN_selected_coefficient",
        "weak_field_selected_coefficient",
        "kappa0_selected_coefficient",
        "repair_selected_coefficient",
        "residual_cleanup_coefficient",
        "active_O_selected_coefficient",
        "parent_fit_selected_coefficient",
        "filter_as_insertion",
        "filter_as_residual_control",
        "filter_as_parent_closure",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; coefficient origin cannot be selected by recovery, repair, residual cleanup, active O, or parent fit.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g29_recovery_filter_result",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Recovery-selected coefficients are rejected: AB=1, B=1/A, Schwarzschild, gamma/PPN, weak-field, and kappa=0 cannot fix coefficient. "
            "Repair-selected, residual-cleanup, active-O-selected, and parent-fit-selected coefficients are rejected. Volume/trace route survives as candidate only. "
            "B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready."
        ),
        derivation_ids=["g29_recovery_filter"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Recovery Smuggling Filter")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    candidates = build_candidates()
    tests = build_tests()
    requirements = build_requirements()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_symbolic_ledger(symbols, out)
    case_2_candidates(candidates, out)
    case_3_tests(tests, out)
    case_4_requirements(requirements, out)
    case_5_conclusions(conclusions, out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns, symbols)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
