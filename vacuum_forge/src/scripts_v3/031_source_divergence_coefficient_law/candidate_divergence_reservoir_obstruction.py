# Candidate divergence reservoir obstruction
#
# Group:
#   31_source_divergence_coefficient_law
#
# Script type:
#   DIVERGENCE RESERVOIR OBSTRUCTION
#
# Purpose
# -------
# Test whether correction/divergence terms become hidden source, boundary,
# current, mass, or support reservoirs.
#
# Locked-door question:
#
#   Can a divergence correction be explicit without becoming a hidden reservoir?
#
# This script does not adopt a new postulate.
# It does not derive divergence-safe coefficient law.
# It does not derive source no-double-counting.
# It does not derive B_s/F_zeta insertion.
# It does not construct active O.
# It does not derive residual control.
# It does not open the parent equation.
#
# Tiny goblin rule:
#
#   A drain is not a treasure chest.

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
        "DIVERGENCE_RISK": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "PARTIAL_CONSTRAINT": StatusMark.INFO,
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
            "g31_coeff",
            "031_source_divergence_coefficient_law__candidate_coefficient_source_no_double_counting_tests",
            "g31_coeff_source_tests",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_dup",
            "031_source_divergence_coefficient_law__candidate_source_duplicate_load_ledger",
            "g31_source_duplicate_ledger",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_problem",
            "031_source_divergence_coefficient_law__candidate_source_divergence_problem_ledger",
            "g31_source_divergence_problem",
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
class DivergenceSymbols:
    C_div: sp.Symbol
    R_div: sp.Symbol
    hidden_source: sp.Symbol
    hidden_boundary: sp.Symbol
    hidden_current: sp.Symbol
    hidden_mass: sp.Symbol
    hidden_support: sp.Symbol
    hidden_residual: sp.Symbol
    hidden_parent: sp.Symbol
    explicit_part: sp.Symbol
    reservoir_load: sp.Expr
    explicitness_gap: sp.Expr


@dataclass
class ReservoirChannel:
    name: str
    channel: str
    status: str
    risk: str
    required_condition: str


@dataclass
class ReservoirTest:
    name: str
    test: str
    status: str
    result: str
    caution: str


@dataclass
class RejectedReservoir:
    name: str
    move: str
    status: str
    reason: str


@dataclass
class ReservoirObligation:
    name: str
    obligation: str
    status: str
    blocks: str
    discipline: str


@dataclass
class ReservoirConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_symbols() -> DivergenceSymbols:
    (
        C_div,
        R_div,
        hidden_source,
        hidden_boundary,
        hidden_current,
        hidden_mass,
        hidden_support,
        hidden_residual,
        hidden_parent,
        explicit_part,
    ) = sp.symbols(
        "C_div R_div hidden_source hidden_boundary hidden_current hidden_mass "
        "hidden_support hidden_residual hidden_parent explicit_part",
        real=True,
    )

    reservoir_load = sp.simplify(
        R_div + hidden_source + hidden_boundary + hidden_current + hidden_mass
        + hidden_support + hidden_residual + hidden_parent
    )

    explicitness_gap = sp.simplify(C_div - explicit_part + reservoir_load)

    return DivergenceSymbols(
        C_div=C_div,
        R_div=R_div,
        hidden_source=hidden_source,
        hidden_boundary=hidden_boundary,
        hidden_current=hidden_current,
        hidden_mass=hidden_mass,
        hidden_support=hidden_support,
        hidden_residual=hidden_residual,
        hidden_parent=hidden_parent,
        explicit_part=explicit_part,
        reservoir_load=reservoir_load,
        explicitness_gap=explicitness_gap,
    )


def build_channels() -> List[ReservoirChannel]:
    return [
        ReservoirChannel(
            name="D1: reservoir remainder",
            channel="R_div",
            status="DIVERGENCE_RISK",
            risk="unaccounted correction remainder becomes hidden reservoir",
            required_condition="R_div = 0 or explicitly derived neutral",
        ),
        ReservoirChannel(
            name="D2: hidden source",
            channel="hidden_source",
            status="DIVERGENCE_RISK",
            risk="ordinary source hidden inside divergence correction",
            required_condition="hidden_source = 0 sector-by-sector",
        ),
        ReservoirChannel(
            name="D3: hidden boundary",
            channel="hidden_boundary",
            status="DIVERGENCE_RISK",
            risk="boundary or matching load hidden inside correction",
            required_condition="hidden_boundary = 0 sector-by-sector",
        ),
        ReservoirChannel(
            name="D4: hidden current",
            channel="hidden_current",
            status="DIVERGENCE_RISK",
            risk="current/flux load hidden inside correction",
            required_condition="hidden_current = 0 sector-by-sector",
        ),
        ReservoirChannel(
            name="D5: hidden mass",
            channel="hidden_mass",
            status="DIVERGENCE_RISK",
            risk="A-sector mass load hidden inside correction",
            required_condition="hidden_mass = 0 sector-by-sector",
        ),
        ReservoirChannel(
            name="D6: hidden support",
            channel="hidden_support",
            status="DIVERGENCE_RISK",
            risk="support/compactness/matching condition hidden inside correction",
            required_condition="hidden_support = 0 sector-by-sector",
        ),
        ReservoirChannel(
            name="D7: hidden residual",
            channel="hidden_residual",
            status="DIVERGENCE_RISK",
            risk="zeta/kappa residual hidden inside correction",
            required_condition="hidden_residual = 0 or visibly carried as residual, not correction",
        ),
        ReservoirChannel(
            name="D8: hidden parent",
            channel="hidden_parent",
            status="DIVERGENCE_RISK",
            risk="parent equation obligation hidden inside correction",
            required_condition="hidden_parent = 0; parent gate remains closed",
        ),
    ]


def build_tests(symbols: DivergenceSymbols) -> List[ReservoirTest]:
    return [
        ReservoirTest(
            name="T1: reservoir load",
            test=f"L_div_reservoir = {sp.sstr(symbols.reservoir_load)}",
            status="THEOREM_TARGET",
            result="all reservoir pockets must vanish or be explicitly derived neutral",
            caution="does not derive divergence-safe coefficient law",
        ),
        ReservoirTest(
            name="T2: explicitness gap",
            test=f"G_explicitness = {sp.sstr(symbols.explicitness_gap)}",
            status="THEOREM_TARGET",
            result="correction must be explicit_part plus no reservoir load",
            caution="explicitness is weaker than divergence safety",
        ),
        ReservoirTest(
            name="T3: non-source correction",
            test="hidden_source = hidden_mass = 0",
            status="REQUIRED",
            result="correction cannot carry ordinary source or A-sector mass charge",
            caution="source discipline is not insertion",
        ),
        ReservoirTest(
            name="T4: non-boundary/current correction",
            test="hidden_boundary = hidden_current = hidden_support = 0",
            status="REQUIRED",
            result="correction cannot absorb guardrail loads",
            caution="guardrail visibility candidate is not adopted neutrality theorem",
        ),
        ReservoirTest(
            name="T5: parent closure exclusion",
            test="hidden_parent = 0",
            status="REQUIRED",
            result="correction cannot carry parent equation obligation",
            caution="parent gate remains closed",
        ),
    ]


def build_rejected() -> List[RejectedReservoir]:
    return [
        RejectedReservoir(
            name="R1: correction as source reservoir",
            move="use C_div to store ordinary source load",
            status="REJECTED",
            reason="ordinary source already has protected A-sector routing",
        ),
        RejectedReservoir(
            name="R2: correction as boundary reservoir",
            move="use C_div to absorb boundary/support/matching failure",
            status="REJECTED",
            reason="boundary/support loads must remain visible",
        ),
        RejectedReservoir(
            name="R3: correction as current reservoir",
            move="use C_div to absorb current/flux failure",
            status="REJECTED",
            reason="current/flux load must remain visible",
        ),
        RejectedReservoir(
            name="R4: correction as residual cleanup",
            move="use C_div to hide zeta/kappa residuals",
            status="REJECTED",
            reason="residual control remains not derived",
        ),
        RejectedReservoir(
            name="R5: correction as coefficient repair",
            move="choose correction to repair coefficient source leakage",
            status="REJECTED",
            reason="repair may reject but not select",
        ),
        RejectedReservoir(
            name="R6: correction as insertion",
            move="treat explicit correction as B_s/F_zeta insertion",
            status="REJECTED",
            reason="explicit correction is not insertion",
        ),
        RejectedReservoir(
            name="R7: correction as parent closure",
            move="use correction to close parent equation",
            status="REJECTED",
            reason="parent fit cannot select correction law",
        ),
    ]


def build_obligations() -> List[ReservoirObligation]:
    return [
        ReservoirObligation(
            name="O1: reservoir zero",
            obligation="derive or retain as open L_div_reservoir = 0 sector-by-sector",
            status="OPEN",
            blocks="divergence-safe coefficient behavior",
            discipline="no hidden correction pockets",
        ),
        ReservoirObligation(
            name="O2: explicitness criterion next",
            obligation="classify non-reservoir divergence explicitness next",
            status="OPEN",
            blocks="non-reservoir correction rule",
            discipline="explicitness is not full divergence safety",
        ),
        ReservoirObligation(
            name="O3: source carryover",
            obligation="carry hidden_source and hidden_mass back to source no-double-counting",
            status="OPEN",
            blocks="source discipline",
            discipline="correction cannot carry ordinary source",
        ),
        ReservoirObligation(
            name="O4: residual carryover",
            obligation="keep hidden_residual visible as residual obligation, not correction payload",
            status="OPEN",
            blocks="residual visibility",
            discipline="do not clean residuals by correction",
        ),
        ReservoirObligation(
            name="O5: downstream gates",
            obligation="keep insertion, active O, residual control, and parent equation closed",
            status="NOT_READY",
            blocks="premature closure",
            discipline="divergence obstruction is not divergence-safe theorem",
        ),
    ]


def build_conclusions() -> List[ReservoirConclusion]:
    return [
        ReservoirConclusion(
            name="C1: reservoir obstruction",
            conclusion="divergence correction cannot be a hidden reservoir",
            status="THEOREM_TARGET",
            meaning="all reservoir channels must vanish or be explicitly derived neutral",
        ),
        ReservoirConclusion(
            name="C2: partial constraint",
            conclusion="reservoir obstruction constrains correction behavior but does not derive divergence-safe coefficient law",
            status="PARTIAL_CONSTRAINT",
            meaning="necessary condition only",
        ),
        ReservoirConclusion(
            name="C3: no adoption",
            conclusion="no Group 30 candidate postulate is adopted",
            status="NOT_ADOPTED",
            meaning="divergence explicitness candidate remains unadopted",
        ),
        ReservoirConclusion(
            name="C4: no insertion",
            conclusion="B_s/F_zeta insertion is not derived",
            status="NOT_READY",
            meaning="explicit correction is not insertion",
        ),
        ReservoirConclusion(
            name="C5: next",
            conclusion="non-reservoir divergence explicitness classifier should run next",
            status="OPEN",
            meaning="explicitness criterion must be stated without overclaim",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Divergence reservoir obstruction problem")
    print("Question:")
    print()
    print("  Can a divergence correction be explicit without becoming a hidden reservoir?")
    print()
    print("Discipline:")
    print()
    print("  This script tests reservoir obstruction.")
    print("  It does not derive divergence-safe coefficient law.")
    print("  It does not derive insertion.")
    print()
    print("Tiny goblin rule:")
    print("  A drain is not a treasure chest.")

    with out.governance_assessments():
        out.line(
            "divergence reservoir obstruction opened",
            StatusMark.INFO,
            "testing correction/divergence hidden reservoir channels",
        )


def case_1_symbolic_ledger(symbols: DivergenceSymbols, out: ScriptOutput) -> None:
    header("Case 1: Divergence reservoir symbolic ledger")
    print("Divergence reservoir symbols:")
    print()
    for name in [
        "C_div",
        "R_div",
        "hidden_source",
        "hidden_boundary",
        "hidden_current",
        "hidden_mass",
        "hidden_support",
        "hidden_residual",
        "hidden_parent",
        "explicit_part",
    ]:
        print(f"  {name} = {sp.sstr(getattr(symbols, name))}")

    print()
    print("Reservoir load:")
    print(f"  L_div_reservoir = {sp.sstr(symbols.reservoir_load)}")
    print()
    print("Explicitness gap:")
    print(f"  G_explicitness = {sp.sstr(symbols.explicitness_gap)}")

    with out.derived_results():
        out.line(
            "divergence reservoir load stated",
            StatusMark.OBLIGATION,
            f"L_div_reservoir = {sp.sstr(symbols.reservoir_load)}",
        )


def case_2_channels(items: List[ReservoirChannel], out: ScriptOutput) -> None:
    header("Case 2: Divergence reservoir channels")
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
            "divergence reservoir channels inventoried",
            StatusMark.DEFER,
            f"{len(items)} reservoir channels inventoried",
        )


def case_3_tests(items: List[ReservoirTest], out: ScriptOutput) -> None:
    header("Case 3: Divergence reservoir tests")
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
            "divergence reservoir tests stated",
            StatusMark.OBLIGATION,
            f"{len(items)} reservoir tests stated",
        )


def case_4_rejected(items: List[RejectedReservoir], out: ScriptOutput) -> None:
    header("Case 4: Rejected divergence reservoir moves")
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
            "divergence reservoir moves rejected",
            StatusMark.FAIL,
            "source, boundary, current, residual, repair, insertion, and parent correction reservoirs rejected",
        )


def case_5_obligations(items: List[ReservoirObligation], out: ScriptOutput) -> None:
    header("Case 5: Divergence reservoir obligations")
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
            "divergence reservoir obligations stated",
            StatusMark.OBLIGATION,
            f"{len(items)} obligations remain",
        )


def case_6_conclusions(items: List[ReservoirConclusion], out: ScriptOutput) -> None:
    header("Case 6: Divergence reservoir conclusions")
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
            "divergence reservoir conclusion stated",
            StatusMark.PASS,
            "reservoir obstruction constrained; no divergence-safe theorem or insertion",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Divergence reservoir obstruction result:")
    print()
    print("  Divergence correction cannot be a hidden reservoir.")
    print("  Source, boundary, current, mass, support, residual, and parent loads may not be hidden inside C_div.")
    print("  Reservoir obstruction constrains correction behavior but does not derive divergence-safe coefficient law.")
    print("  Divergence explicitness remains unadopted candidate discipline, not a postulate.")
    print("  No Group 30 candidate postulate is adopted.")
    print("  Full source no-double-counting is not yet derived.")
    print("  B_s/F_zeta insertion is not derived.")
    print("  Active O, residual control, and parent equation remain not ready.")
    print()
    print("Possible next script:")
    print("  candidate_nonreservoir_divergence_explicitness.py")
    print()
    print("Tiny goblin label:")
    print("  A drain is not a treasure chest.")

    with out.governance_assessments():
        out.line(
            "divergence reservoir obstruction complete",
            StatusMark.PASS,
            "non-reservoir divergence explicitness classifier should run next",
        )


def record_derivations(ns, symbols: DivergenceSymbols) -> None:
    ns.record_derivation(
        derivation_id="g31_divergence_reservoir",
        inputs=[
            symbols.R_div,
            symbols.hidden_source,
            symbols.hidden_boundary,
            symbols.hidden_current,
            symbols.hidden_mass,
            symbols.hidden_support,
            symbols.hidden_residual,
            symbols.hidden_parent,
        ],
        output=symbols.reservoir_load,
        method="test divergence correction reservoir obstruction",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="divergence_reservoir_obstruction_marker",
        scope="Group 31 source/divergence coefficient law",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g31_div_reservoir_zero", "Derive or leave open L_div_reservoir = 0 sector-by-sector"),
        ("g31_div_explicitness_next", "Classify non-reservoir divergence explicitness next"),
        ("g31_div_no_source_pocket", "Prevent source/mass hiding in correction"),
        ("g31_div_no_guardrail_pocket", "Prevent boundary/current/support hiding in correction"),
        ("g31_div_no_residual_cleanup", "Prevent residual cleanup through correction"),
        ("g31_div_no_parent", "Prevent parent closure through correction"),
        ("g31_div_downstream_closed", "Keep insertion/O/residual/parent gates closed"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g31_div_reservoir_route"],
            description=(
                "Divergence reservoir obstruction constrains correction behavior. Divergence-safe coefficient law and insertion are not derived."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g31_div_reservoir_zero",
        "g31_div_explicitness_next",
        "g31_div_no_source_pocket",
        "g31_div_no_guardrail_pocket",
        "g31_div_no_residual_cleanup",
        "g31_div_no_parent",
        "g31_div_downstream_closed",
    ]

    ns.record_route(RouteRecord(
        route_id="g31_div_reservoir_route",
        script_id=SCRIPT_ID,
        name="Group 31 divergence reservoir obstruction route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "divergence correction cannot be hidden reservoir",
            "source/boundary/current/mass/support/residual/parent pockets rejected",
            "explicitness remains weaker than divergence-safe coefficient law",
            "no postulate adopted",
            "downstream gates remain closed",
        ],
    ))

    for branch_id in [
        "correction_as_source_reservoir",
        "correction_as_boundary_reservoir",
        "correction_as_current_reservoir",
        "correction_as_residual_cleanup",
        "correction_as_coefficient_repair",
        "correction_as_insertion",
        "correction_as_parent_closure",
        "reservoir_obstruction_as_divergence_safe_law",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; divergence reservoir obstruction is not theorem closure.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g31_divergence_reservoir_obstruction",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Divergence correction cannot be a hidden reservoir. Source, boundary, current, mass, support, residual, and parent loads may not be hidden inside C_div. "
            "Reservoir obstruction constrains correction behavior but does not derive divergence-safe coefficient law. Divergence explicitness remains unadopted candidate discipline, not a postulate. "
            "No Group 30 candidate postulate is adopted. Full source no-double-counting, B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready."
        ),
        derivation_ids=["g31_divergence_reservoir"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Divergence Reservoir Obstruction")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    channels = build_channels()
    tests = build_tests(symbols)
    rejected = build_rejected()
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
