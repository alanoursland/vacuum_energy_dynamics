# Candidate incidence source divergence postulate inventory
#
# Group:
#   30_minimal_coefficient_sector_postulate_inventory
#
# Script type:
#   INCIDENCE / SOURCE / DIVERGENCE POSTULATE INVENTORY
#
# Purpose
# -------
# Inventory whether trace/residual incidence, source no-double-counting,
# and divergence explicitness require independent postulates or theorem routes.
#
# Locked-door question:
#
#   Which of incidence, source no-double-counting, and divergence explicitness
#   should be postulate candidates, and which should remain theorem routes?
#
# This script does not adopt a new postulate.
# It does not derive B_s/F_zeta insertion.
# It does not derive no-overlap sector geometry.
# It does not construct active O.
# It does not derive residual control.
# It does not open the parent equation.
#
# Tiny goblin rule:
#
#   Do not call the fence a wall, and do not call the drain a river.

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
        "ADMISSIBLE_CANDIDATE": StatusMark.INFO,
        "CANDIDATE_POSTULATE": StatusMark.OBLIGATION,
        "CONDITIONAL_CANDIDATE": StatusMark.DEFER,
        "HIGH_RISK": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "THEOREM_ROUTE_PREFERRED": StatusMark.INFO,
        "THEOREM_TARGET": StatusMark.OBLIGATION,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g30_safe_membership",
            "030_minimal_coefficient_sector_postulate_inventory__candidate_safe_trace_membership_postulate",
            "g30_safe_membership",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g30_trace_norm",
            "030_minimal_coefficient_sector_postulate_inventory__candidate_trace_normalization_postulate",
            "g30_trace_normalization",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g30_filter",
            "030_minimal_coefficient_sector_postulate_inventory__candidate_postulate_smuggling_filter",
            "g30_postulate_smuggling_filter",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g30_minimality",
            "030_minimal_coefficient_sector_postulate_inventory__candidate_postulate_minimality_tests",
            "g30_postulate_minimality",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g30_problem",
            "030_minimal_coefficient_sector_postulate_inventory__candidate_minimal_postulate_problem_ledger",
            "g30_postulate_problem",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g29_summary",
            "029_Bs_Fzeta_coefficient_origin__candidate_group_29_status_summary",
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
class InventorySymbols:
    I_TRz: sp.Symbol
    I_TRk: sp.Symbol
    S_once: sp.Symbol
    D_explicit: sp.Symbol
    C_div: sp.Symbol
    T_zeta: sp.Symbol
    R_zeta: sp.Symbol
    R_kappa: sp.Symbol
    incidence_gap: sp.Symbol
    source_gap: sp.Symbol
    divergence_gap: sp.Symbol
    residual_gap: sp.Symbol
    insertion_gap: sp.Symbol
    parent_gap: sp.Symbol
    inventory_load: sp.Expr


@dataclass
class InventoryItem:
    name: str
    item: str
    status: str
    recommendation: str
    risk: str


@dataclass
class CouplingTest:
    name: str
    coupling: str
    status: str
    result: str
    implication: str


@dataclass
class ForbiddenUpgrade:
    name: str
    upgrade: str
    status: str
    reason: str


@dataclass
class InventoryObligation:
    name: str
    obligation: str
    status: str
    blocks: str
    discipline: str


@dataclass
class InventoryConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_symbols() -> InventorySymbols:
    (
        I_TRz,
        I_TRk,
        S_once,
        D_explicit,
        C_div,
        T_zeta,
        R_zeta,
        R_kappa,
        incidence_gap,
        source_gap,
        divergence_gap,
        residual_gap,
        insertion_gap,
        parent_gap,
    ) = sp.symbols(
        "I_TRz I_TRk S_once D_explicit C_div T_zeta R_zeta R_kappa "
        "incidence_gap source_gap divergence_gap residual_gap insertion_gap parent_gap",
        real=True,
    )

    inventory_load = sp.simplify(
        incidence_gap + source_gap + divergence_gap + residual_gap + insertion_gap + parent_gap
    )

    return InventorySymbols(
        I_TRz=I_TRz,
        I_TRk=I_TRk,
        S_once=S_once,
        D_explicit=D_explicit,
        C_div=C_div,
        T_zeta=T_zeta,
        R_zeta=R_zeta,
        R_kappa=R_kappa,
        incidence_gap=incidence_gap,
        source_gap=source_gap,
        divergence_gap=divergence_gap,
        residual_gap=residual_gap,
        insertion_gap=insertion_gap,
        parent_gap=parent_gap,
        inventory_load=inventory_load,
    )


def build_inventory_items() -> List[InventoryItem]:
    return [
        InventoryItem(
            name="I1: trace/residual incidence",
            item="I(T_zeta,R_zeta)=0 and/or I(T_zeta,R_kappa)=0",
            status="HIGH_RISK",
            recommendation="do not adopt directly in this group; retain as high-risk candidate/theorem target",
            risk="too close to no-overlap geometry and residual-control smuggling",
        ),
        InventoryItem(
            name="I2: source no-double-counting",
            item="ordinary source load enters once and is not duplicated through coefficient/accounting sectors",
            status="THEOREM_ROUTE_PREFERRED",
            recommendation="prefer source/divergence law route over direct postulate",
            risk="may be chosen by source repair or used as insertion shortcut",
        ),
        InventoryItem(
            name="I3: divergence explicitness",
            item="any divergence correction is explicit, auditable, and non-reservoir",
            status="ADMISSIBLE_CANDIDATE",
            recommendation="retain as narrow candidate postulate or theorem constraint",
            risk="correction may become hidden source/boundary/current/mass/support reservoir",
        ),
        InventoryItem(
            name="I4: divergence-safe coefficient law",
            item="coefficient law has explicit divergence behavior compatible with source discipline",
            status="THEOREM_TARGET",
            recommendation="pursue as theorem route if possible",
            risk="too large as postulate if it silently includes insertion",
        ),
        InventoryItem(
            name="I5: incidence/source/divergence bundle",
            item="postulate incidence + source once + divergence safety as insertion-ready package",
            status="REJECTED",
            recommendation="reject bundle",
            risk="collapses missing theorem targets into endpoint-selected closure",
        ),
    ]


def build_couplings() -> List[CouplingTest]:
    return [
        CouplingTest(
            name="C1: incidence versus membership",
            coupling="safe membership does not imply trace/residual zero incidence",
            status="REQUIRED",
            result="incidence remains separate",
            implication="membership candidate cannot be treated as no-overlap",
        ),
        CouplingTest(
            name="C2: incidence versus residual control",
            coupling="zero incidence must not imply residual kill or inertness",
            status="REQUIRED",
            result="residual control remains not derived",
            implication="incidence candidate remains high-risk",
        ),
        CouplingTest(
            name="C3: source versus divergence",
            coupling="source no-double-counting and divergence explicitness are related but separable",
            status="OPEN",
            result="source/divergence theorem route remains preferred",
            implication="do not postulate both unless theorem route fails",
        ),
        CouplingTest(
            name="C4: divergence explicitness versus divergence safety",
            coupling="explicit correction is weaker than divergence-safe coefficient law",
            status="ADMISSIBLE_CANDIDATE",
            result="D_explicit can survive as narrow candidate",
            implication="does not derive divergence-safe theorem",
        ),
        CouplingTest(
            name="C5: source/divergence versus insertion",
            coupling="source/divergence discipline does not derive B_s/F_zeta insertion by itself",
            status="REQUIRED",
            result="insertion gate remains closed",
            implication="no endpoint shortcut",
        ),
    ]


def build_forbidden_upgrades() -> List[ForbiddenUpgrade]:
    return [
        ForbiddenUpgrade(
            name="F1: incidence as no-overlap theorem",
            upgrade="I(T_zeta,R_zeta)=0 treated as complete sector geometry",
            status="REJECTED",
            reason="no-overlap geometry remains not derived",
        ),
        ForbiddenUpgrade(
            name="F2: incidence as residual control",
            upgrade="zero incidence treated as residual kill or inertness",
            status="REJECTED",
            reason="residual control remains not derived",
        ),
        ForbiddenUpgrade(
            name="F3: source once as insertion",
            upgrade="source no-double-counting treated as B_s/F_zeta insertion",
            status="REJECTED",
            reason="source discipline is not insertion",
        ),
        ForbiddenUpgrade(
            name="F4: divergence explicitness as divergence safety",
            upgrade="explicit correction treated as divergence-safe coefficient law",
            status="REJECTED",
            reason="explicitness is weaker than safety theorem",
        ),
        ForbiddenUpgrade(
            name="F5: correction as reservoir",
            upgrade="C_div absorbs source/boundary/current/mass/support load",
            status="REJECTED",
            reason="correction must remain explicit and auditable",
        ),
        ForbiddenUpgrade(
            name="F6: bundle as closure",
            upgrade="incidence/source/divergence package treated as insertion or parent readiness",
            status="REJECTED",
            reason="bundle closure is endpoint smuggling",
        ),
    ]


def build_obligations() -> List[InventoryObligation]:
    return [
        InventoryObligation(
            name="O1: incidence caution",
            obligation="keep trace/residual incidence high-risk and separate",
            status="REQUIRED",
            blocks="no-overlap/residual-control honesty",
            discipline="do not adopt directly without further obstruction analysis",
        ),
        InventoryObligation(
            name="O2: source/divergence theorem route",
            obligation="prefer theorem route for source no-double-counting and divergence-safe coefficient law",
            status="OPEN",
            blocks="field-equation usability",
            discipline="do not hide source or correction load",
        ),
        InventoryObligation(
            name="O3: divergence explicitness narrowness",
            obligation="retain divergence explicitness only as visibility/correction rule",
            status="REQUIRED",
            blocks="minimality",
            discipline="do not upgrade to divergence-safe theorem",
        ),
        InventoryObligation(
            name="O4: next obstruction classifier",
            obligation="classify whether minimal postulate set is identified, underdetermined, overlarge, or blocked",
            status="OPEN",
            blocks="Group 30 closure",
            discipline="do not adopt yet",
        ),
        InventoryObligation(
            name="O5: downstream gates",
            obligation="keep insertion, active O, residual control, and parent equation closed",
            status="NOT_READY",
            blocks="premature closure",
            discipline="inventory is not theorem closure",
        ),
    ]


def build_conclusions() -> List[InventoryConclusion]:
    return [
        InventoryConclusion(
            name="R1: incidence",
            conclusion="trace/residual incidence remains high-risk and not adopted",
            status="HIGH_RISK",
            meaning="too close to no-overlap/residual-control smuggling",
        ),
        InventoryConclusion(
            name="R2: source",
            conclusion="source no-double-counting should remain theorem-route preferred",
            status="THEOREM_ROUTE_PREFERRED",
            meaning="source/divergence law may be cleaner than postulate",
        ),
        InventoryConclusion(
            name="R3: divergence explicitness",
            conclusion="divergence explicitness survives as admissible narrow candidate",
            status="ADMISSIBLE_CANDIDATE",
            meaning="explicit correction visibility only; not divergence-safe theorem",
        ),
        InventoryConclusion(
            name="R4: bundle",
            conclusion="incidence/source/divergence insertion-ready bundle is rejected",
            status="REJECTED",
            meaning="too large; endpoint closure smuggling",
        ),
        InventoryConclusion(
            name="R5: adoption",
            conclusion="no incidence/source/divergence postulate is adopted",
            status="NOT_ADOPTED",
            meaning="inventory classification only",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Incidence/source/divergence inventory problem")
    print("Question:")
    print()
    print("  Which of incidence, source no-double-counting, and divergence explicitness should be postulate candidates, and which should remain theorem routes?")
    print()
    print("Discipline:")
    print()
    print("  This inventory adopts no postulate.")
    print("  It derives no insertion.")
    print("  It opens no parent gate.")
    print()
    print("Tiny goblin rule:")
    print("  Do not call the fence a wall, and do not call the drain a river.")

    with out.governance_assessments():
        out.line(
            "incidence/source/divergence postulate inventory opened",
            StatusMark.INFO,
            "classifying high-risk incidence, source theorem route, and divergence explicitness candidate",
        )


def case_1_symbolic_ledger(symbols: InventorySymbols, out: ScriptOutput) -> None:
    header("Case 1: Incidence/source/divergence symbolic ledger")
    print("Inventory symbols:")
    print()
    for name in [
        "I_TRz",
        "I_TRk",
        "S_once",
        "D_explicit",
        "C_div",
        "T_zeta",
        "R_zeta",
        "R_kappa",
        "incidence_gap",
        "source_gap",
        "divergence_gap",
        "residual_gap",
        "insertion_gap",
        "parent_gap",
    ]:
        print(f"  {name} = {sp.sstr(getattr(symbols, name))}")
    print()
    print("Incidence/source/divergence inventory load:")
    print()
    print(f"  L_incidence_source_divergence = {sp.sstr(symbols.inventory_load)}")

    with out.derived_results():
        out.line(
            "incidence/source/divergence inventory load stated",
            StatusMark.OBLIGATION,
            f"L_incidence_source_divergence = {sp.sstr(symbols.inventory_load)}",
        )


def case_2_inventory(items: List[InventoryItem], out: ScriptOutput) -> None:
    header("Case 2: Incidence/source/divergence inventory items")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Item: {item.item}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Recommendation: {item.recommendation}")
        print(f"Risk: {item.risk}")

    with out.governance_assessments():
        out.line(
            "incidence/source/divergence inventory classified",
            StatusMark.DEFER,
            f"{len(items)} inventory items classified",
        )


def case_3_couplings(items: List[CouplingTest], out: ScriptOutput) -> None:
    header("Case 3: Coupling tests")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Coupling: {item.coupling}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Result: {item.result}")
        print(f"Implication: {item.implication}")

    with out.governance_assessments():
        out.line(
            "incidence/source/divergence couplings tested",
            StatusMark.DEFER,
            f"{len(items)} coupling tests completed",
        )


def case_4_forbidden(items: List[ForbiddenUpgrade], out: ScriptOutput) -> None:
    header("Case 4: Forbidden incidence/source/divergence upgrades")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Upgrade: {item.upgrade}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Reason: {item.reason}")

    with out.counterexamples():
        out.line(
            "incidence/source/divergence forbidden upgrades rejected",
            StatusMark.FAIL,
            "no-overlap, residual control, insertion, divergence safety, reservoir, and bundle closure upgrades rejected",
        )


def case_5_obligations(items: List[InventoryObligation], out: ScriptOutput) -> None:
    header("Case 5: Incidence/source/divergence obligations")
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
            "incidence/source/divergence obligations stated",
            StatusMark.OBLIGATION,
            f"{len(items)} obligations remain",
        )


def case_6_conclusions(items: List[InventoryConclusion], out: ScriptOutput) -> None:
    header("Case 6: Incidence/source/divergence conclusions")
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
            "incidence/source/divergence conclusion stated",
            StatusMark.PASS,
            "inventory classified; no postulate adopted",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Incidence/source/divergence postulate inventory result:")
    print()
    print("  Trace/residual incidence remains high-risk and is not adopted.")
    print("  Source no-double-counting should remain theorem-route preferred.")
    print("  Divergence explicitness survives as an admissible narrow candidate.")
    print("  Divergence-safe coefficient law remains theorem target.")
    print("  Incidence/source/divergence insertion-ready bundle is rejected.")
    print("  No incidence, source, or divergence postulate is adopted.")
    print("  B_s/F_zeta insertion is not derived.")
    print("  Active O, residual control, and parent equation remain not ready.")
    print()
    print("Possible next script:")
    print("  candidate_minimal_postulate_set_obstruction.py")
    print()
    print("Tiny goblin label:")
    print("  Do not call the fence a wall, and do not call the drain a river.")

    with out.governance_assessments():
        out.line(
            "incidence/source/divergence postulate inventory complete",
            StatusMark.PASS,
            "minimal postulate set obstruction classifier should run next",
        )


def record_derivations(ns, symbols: InventorySymbols) -> None:
    ns.record_derivation(
        derivation_id="g30_incidence_source_divergence",
        inputs=[
            symbols.incidence_gap,
            symbols.source_gap,
            symbols.divergence_gap,
            symbols.residual_gap,
            symbols.insertion_gap,
            symbols.parent_gap,
        ],
        output=symbols.inventory_load,
        method="inventory incidence, source no-double-counting, and divergence explicitness postulate/theorem split",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="incidence_source_divergence_inventory_marker",
        scope="Group 30 minimal coefficient/sector postulate inventory",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g30_isd_incidence_caution", "Keep trace/residual incidence high-risk"),
        ("g30_isd_source_theorem", "Prefer source no-double-counting theorem route"),
        ("g30_isd_divergence_candidate", "Retain divergence explicitness as narrow candidate"),
        ("g30_isd_divergence_theorem", "Keep divergence-safe coefficient law as theorem target"),
        ("g30_isd_no_bundle", "Reject incidence/source/divergence closure bundle"),
        ("g30_isd_next_obstruction", "Run minimal postulate set obstruction classifier next"),
        ("g30_isd_downstream", "Keep insertion/O/residual/parent gates closed"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g30_isd_route"],
            description=(
                "Incidence/source/divergence structures are classified only. No postulate is adopted and no downstream theorem is derived."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g30_isd_incidence_caution",
        "g30_isd_source_theorem",
        "g30_isd_divergence_candidate",
        "g30_isd_divergence_theorem",
        "g30_isd_no_bundle",
        "g30_isd_next_obstruction",
        "g30_isd_downstream",
    ]

    ns.record_route(RouteRecord(
        route_id="g30_isd_route",
        script_id=SCRIPT_ID,
        name="Group 30 incidence/source/divergence postulate inventory route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "trace/residual incidence remains high-risk",
            "source no-double-counting theorem route preferred",
            "divergence explicitness survives as narrow candidate",
            "divergence-safe coefficient law remains theorem target",
            "no incidence/source/divergence postulate adopted",
            "downstream gates remain closed",
        ],
    ))

    for branch_id in [
        "incidence_as_no_overlap",
        "incidence_as_residual_control",
        "source_once_as_insertion",
        "divergence_explicit_as_divergence_safety",
        "correction_as_reservoir",
        "isd_bundle_as_closure",
        "isd_inventory_as_adoption",
        "isd_inventory_as_parent_readiness",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; incidence/source/divergence inventory is not adoption or theorem closure.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g30_incidence_source_divergence_inventory",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Trace/residual incidence remains high-risk and is not adopted. Source no-double-counting should remain theorem-route preferred. "
            "Divergence explicitness survives as an admissible narrow candidate, while divergence-safe coefficient law remains theorem target. "
            "The incidence/source/divergence insertion-ready bundle is rejected. No incidence, source, or divergence postulate is adopted. "
            "B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready."
        ),
        derivation_ids=["g30_incidence_source_divergence"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Incidence Source Divergence Postulate Inventory")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    inventory = build_inventory_items()
    couplings = build_couplings()
    forbidden = build_forbidden_upgrades()
    obligations = build_obligations()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_symbolic_ledger(symbols, out)
    case_2_inventory(inventory, out)
    case_3_couplings(couplings, out)
    case_4_forbidden(forbidden, out)
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
