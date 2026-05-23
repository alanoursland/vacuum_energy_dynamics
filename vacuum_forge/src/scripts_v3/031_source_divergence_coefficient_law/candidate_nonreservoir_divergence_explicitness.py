# Candidate nonreservoir divergence explicitness
#
# Group:
#   31_source_divergence_coefficient_law
#
# Script type:
#   NON-RESERVOIR DIVERGENCE EXPLICITNESS CLASSIFIER
#
# Purpose
# -------
# Classify explicit divergence behavior that is weaker than divergence-safe
# coefficient law but strong enough to prevent hidden reservoirs.
#
# Locked-door question:
#
#   What can divergence explicitness honestly say without becoming a postulate
#   or a full divergence-safe coefficient theorem?
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
#   A labeled drain is safer, but it still does not build the mill.

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
        "ADMISSIBLE_DISCIPLINE": StatusMark.INFO,
        "BLOCKED": StatusMark.FAIL,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "PARTIAL_CONSTRAINT": StatusMark.INFO,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "THEOREM_TARGET": StatusMark.OBLIGATION,
        "WEAKER_THAN_THEOREM": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g31_div_res",
            "031_source_divergence_coefficient_law__candidate_divergence_reservoir_obstruction",
            "g31_divergence_reservoir",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_coeff",
            "031_source_divergence_coefficient_law__candidate_coefficient_source_no_double_counting_tests",
            "g31_coeff_source_tests",
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
class ExplicitnessSymbols:
    C_div: sp.Symbol
    E_div: sp.Symbol
    R_div: sp.Symbol
    H_div: sp.Symbol
    D_safe: sp.Symbol
    source_load: sp.Symbol
    boundary_load: sp.Symbol
    residual_load: sp.Symbol
    parent_load: sp.Symbol
    explicitness_burden: sp.Expr
    divergence_safety_gap: sp.Expr


@dataclass
class ExplicitnessCriterion:
    name: str
    criterion: str
    status: str
    result: str
    caveat: str


@dataclass
class Boundary:
    name: str
    boundary: str
    status: str
    reason: str


@dataclass
class ExplicitnessObligation:
    name: str
    obligation: str
    status: str
    blocks: str
    discipline: str


@dataclass
class ExplicitnessConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_symbols() -> ExplicitnessSymbols:
    (
        C_div,
        E_div,
        R_div,
        H_div,
        D_safe,
        source_load,
        boundary_load,
        residual_load,
        parent_load,
    ) = sp.symbols(
        "C_div E_div R_div H_div D_safe source_load boundary_load residual_load parent_load",
        real=True,
    )

    explicitness_burden = sp.simplify(C_div - E_div + R_div + H_div)
    divergence_safety_gap = sp.simplify(
        D_safe - E_div + source_load + boundary_load + residual_load + parent_load
    )

    return ExplicitnessSymbols(
        C_div=C_div,
        E_div=E_div,
        R_div=R_div,
        H_div=H_div,
        D_safe=D_safe,
        source_load=source_load,
        boundary_load=boundary_load,
        residual_load=residual_load,
        parent_load=parent_load,
        explicitness_burden=explicitness_burden,
        divergence_safety_gap=divergence_safety_gap,
    )


def build_criteria() -> List[ExplicitnessCriterion]:
    return [
        ExplicitnessCriterion(
            name="E1: explicit correction identity",
            criterion="C_div must be decomposed into visible E_div plus no hidden reservoir remainder",
            status="ADMISSIBLE_DISCIPLINE",
            result="explicitness can demand C_div = E_div only after R_div and H_div vanish or are derived neutral",
            caveat="does not specify the complete coefficient law",
        ),
        ExplicitnessCriterion(
            name="E2: auditability",
            criterion="every correction contribution must be named, typed, and assigned to a visible channel",
            status="ADMISSIBLE_DISCIPLINE",
            result="prevents hidden pockets",
            caveat="visibility is not neutrality",
        ),
        ExplicitnessCriterion(
            name="E3: non-reservoir condition",
            criterion="R_div = 0 and H_div = 0 sector-by-sector or by derived neutral route",
            status="THEOREM_TARGET",
            result="correction may not carry source/boundary/current/mass/support/residual/parent load",
            caveat="not derived by this classifier",
        ),
        ExplicitnessCriterion(
            name="E4: weaker-than-safety",
            criterion="explicitness is weaker than divergence-safe coefficient law",
            status="WEAKER_THAN_THEOREM",
            result="D_safe remains theorem target",
            caveat="do not upgrade explicitness to full divergence theorem",
        ),
        ExplicitnessCriterion(
            name="E5: no postulate adoption",
            criterion="divergence explicitness remains unadopted candidate discipline",
            status="NOT_ADOPTED",
            result="Group 30 candidate is not adopted",
            caveat="explicitness classifier is not explicitness postulate",
        ),
        ExplicitnessCriterion(
            name="E6: no insertion",
            criterion="non-reservoir explicitness does not derive B_s/F_zeta insertion",
            status="NOT_READY",
            result="insertion gate remains closed",
            caveat="do not use explicit correction as coefficient law",
        ),
    ]


def build_boundaries() -> List[Boundary]:
    return [
        Boundary(
            name="B1: no divergence-safe theorem",
            boundary="explicitness classifier treated as divergence-safe coefficient law",
            status="REJECTED",
            reason="explicitness is necessary discipline, not full divergence theorem",
        ),
        Boundary(
            name="B2: no neutrality theorem",
            boundary="visible channel treated as neutral channel",
            status="REJECTED",
            reason="visibility is not neutrality",
        ),
        Boundary(
            name="B3: no source no-double-counting theorem",
            boundary="non-reservoir correction treated as full source no-double-counting",
            status="REJECTED",
            reason="coefficient/residual/source channels still need theorem route",
        ),
        Boundary(
            name="B4: no residual control",
            boundary="explicit correction used to clean residuals",
            status="REJECTED",
            reason="residual control remains not derived",
        ),
        Boundary(
            name="B5: no parent readiness",
            boundary="explicit divergence behavior used to open parent equation",
            status="REJECTED",
            reason="parent gate remains closed",
        ),
        Boundary(
            name="B6: no postulate adoption",
            boundary="classifier treated as adoption of divergence explicitness postulate",
            status="REJECTED",
            reason="candidate survival and classification are not adoption",
        ),
    ]


def build_obligations() -> List[ExplicitnessObligation]:
    return [
        ExplicitnessObligation(
            name="O1: non-reservoir proof burden",
            obligation="derive or retain as open R_div = H_div = 0 sector-by-sector",
            status="OPEN",
            blocks="divergence-safe coefficient behavior",
            discipline="no hidden reservoir remainder",
        ),
        ExplicitnessObligation(
            name="O2: divergence-safe law classifier next",
            obligation="classify whether source/divergence constraints derive, partially constrain, or fail to derive coefficient law",
            status="OPEN",
            blocks="Group 31 theorem-route status",
            discipline="do not overclaim explicitness",
        ),
        ExplicitnessObligation(
            name="O3: source carryover",
            obligation="carry source_load back into source no-double-counting route",
            status="OPEN",
            blocks="source discipline",
            discipline="explicitness does not remove source burden",
        ),
        ExplicitnessObligation(
            name="O4: residual carryover",
            obligation="carry residual_load forward as residual visibility obligation",
            status="OPEN",
            blocks="residual-control honesty",
            discipline="do not clean residuals through explicitness",
        ),
        ExplicitnessObligation(
            name="O5: downstream gates",
            obligation="keep insertion, active O, residual control, and parent equation closed",
            status="NOT_READY",
            blocks="premature closure",
            discipline="explicitness classifier is not theorem closure",
        ),
    ]


def build_conclusions() -> List[ExplicitnessConclusion]:
    return [
        ExplicitnessConclusion(
            name="C1: admissible discipline",
            conclusion="non-reservoir divergence explicitness is admissible as discipline",
            status="ADMISSIBLE_DISCIPLINE",
            meaning="it can require visible correction accounting without becoming a postulate",
        ),
        ExplicitnessConclusion(
            name="C2: partial constraint",
            conclusion="explicitness constrains correction behavior but does not derive divergence-safe coefficient law",
            status="PARTIAL_CONSTRAINT",
            meaning="necessary but not sufficient",
        ),
        ExplicitnessConclusion(
            name="C3: no adoption",
            conclusion="divergence explicitness candidate is not adopted",
            status="NOT_ADOPTED",
            meaning="classification is not postulate selection",
        ),
        ExplicitnessConclusion(
            name="C4: no insertion",
            conclusion="B_s/F_zeta insertion is not derived",
            status="NOT_READY",
            meaning="visible correction is not coefficient insertion",
        ),
        ExplicitnessConclusion(
            name="C5: next",
            conclusion="source/divergence coefficient-law classifier should run next",
            status="OPEN",
            meaning="classify whether the theorem route produced derivation, partial constraint, or obstruction",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Non-reservoir divergence explicitness problem")
    print("Question:")
    print()
    print("  What can divergence explicitness honestly say without becoming a postulate or a full divergence-safe coefficient theorem?")
    print()
    print("Discipline:")
    print()
    print("  This script classifies explicitness discipline.")
    print("  It does not adopt a postulate.")
    print("  It does not derive divergence-safe law or insertion.")
    print()
    print("Tiny goblin rule:")
    print("  A labeled drain is safer, but it still does not build the mill.")

    with out.governance_assessments():
        out.line(
            "non-reservoir divergence explicitness classifier opened",
            StatusMark.INFO,
            "classifying explicit correction discipline without postulate adoption",
        )


def case_1_symbolic_ledger(symbols: ExplicitnessSymbols, out: ScriptOutput) -> None:
    header("Case 1: Non-reservoir explicitness symbolic ledger")
    print("Explicitness symbols:")
    print()
    for name in [
        "C_div",
        "E_div",
        "R_div",
        "H_div",
        "D_safe",
        "source_load",
        "boundary_load",
        "residual_load",
        "parent_load",
    ]:
        print(f"  {name} = {sp.sstr(getattr(symbols, name))}")

    print()
    print("Explicitness burden:")
    print(f"  L_explicitness = {sp.sstr(symbols.explicitness_burden)}")
    print()
    print("Divergence safety gap:")
    print(f"  G_divergence_safety = {sp.sstr(symbols.divergence_safety_gap)}")

    with out.derived_results():
        out.line(
            "non-reservoir explicitness burden stated",
            StatusMark.OBLIGATION,
            f"L_explicitness = {sp.sstr(symbols.explicitness_burden)}",
        )


def case_2_criteria(items: List[ExplicitnessCriterion], out: ScriptOutput) -> None:
    header("Case 2: Explicitness criteria")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Criterion: {item.criterion}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Result: {item.result}")
        print(f"Caveat: {item.caveat}")

    with out.governance_assessments():
        out.line(
            "non-reservoir explicitness criteria stated",
            StatusMark.DEFER,
            f"{len(items)} explicitness criteria stated",
        )


def case_3_boundaries(items: List[Boundary], out: ScriptOutput) -> None:
    header("Case 3: Explicitness forbidden upgrades")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Boundary: {item.boundary}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Reason: {item.reason}")

    with out.counterexamples():
        out.line(
            "explicitness forbidden upgrades rejected",
            StatusMark.FAIL,
            "divergence-safe theorem, neutrality, source theorem, residual control, parent readiness, and postulate adoption upgrades rejected",
        )


def case_4_obligations(items: List[ExplicitnessObligation], out: ScriptOutput) -> None:
    header("Case 4: Explicitness obligations")
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
            "non-reservoir explicitness obligations stated",
            StatusMark.OBLIGATION,
            f"{len(items)} obligations remain",
        )


def case_5_conclusions(items: List[ExplicitnessConclusion], out: ScriptOutput) -> None:
    header("Case 5: Explicitness conclusions")
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
            "non-reservoir explicitness conclusion stated",
            StatusMark.PASS,
            "explicitness classified as admissible discipline; no theorem closure",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Non-reservoir divergence explicitness result:")
    print()
    print("  Non-reservoir divergence explicitness is admissible as discipline.")
    print("  It requires visible, auditable correction accounting.")
    print("  It can demand no hidden reservoir remainder, but this remains a proof burden unless derived.")
    print("  It is weaker than divergence-safe coefficient law.")
    print("  It does not derive source no-double-counting.")
    print("  It does not adopt the Group 30 divergence explicitness candidate as a postulate.")
    print("  B_s/F_zeta insertion is not derived.")
    print("  Active O, residual control, and parent equation remain not ready.")
    print()
    print("Possible next script:")
    print("  candidate_source_divergence_coefficient_law_classifier.py")
    print()
    print("Tiny goblin label:")
    print("  A labeled drain is safer, but it still does not build the mill.")

    with out.governance_assessments():
        out.line(
            "non-reservoir divergence explicitness complete",
            StatusMark.PASS,
            "source/divergence coefficient-law classifier should run next",
        )


def record_derivations(ns, symbols: ExplicitnessSymbols) -> None:
    ns.record_derivation(
        derivation_id="g31_nonreservoir_explicitness",
        inputs=[
            symbols.C_div,
            symbols.E_div,
            symbols.R_div,
            symbols.H_div,
        ],
        output=symbols.explicitness_burden,
        method="classify non-reservoir divergence explicitness as discipline weaker than divergence-safe law",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="nonreservoir_divergence_explicitness_marker",
        scope="Group 31 source/divergence coefficient law",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g31_explicit_reservoir_zero", "Derive or leave open R_div = H_div = 0 sector-by-sector"),
        ("g31_explicit_classifier_next", "Run source/divergence coefficient-law classifier next"),
        ("g31_explicit_source_carryover", "Carry source load to source no-double-counting"),
        ("g31_explicit_residual_carryover", "Carry residual load as visible residual obligation"),
        ("g31_explicit_no_postulate", "Do not treat explicitness classification as postulate adoption"),
        ("g31_explicit_no_divsafe", "Do not treat explicitness as divergence-safe law"),
        ("g31_explicit_downstream_closed", "Keep insertion/O/residual/parent gates closed"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g31_explicitness_route"],
            description=(
                "Non-reservoir divergence explicitness is classified as admissible discipline. It is not adopted as postulate and does not derive divergence-safe coefficient law."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g31_explicit_reservoir_zero",
        "g31_explicit_classifier_next",
        "g31_explicit_source_carryover",
        "g31_explicit_residual_carryover",
        "g31_explicit_no_postulate",
        "g31_explicit_no_divsafe",
        "g31_explicit_downstream_closed",
    ]

    ns.record_route(RouteRecord(
        route_id="g31_explicitness_route",
        script_id=SCRIPT_ID,
        name="Group 31 non-reservoir divergence explicitness route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "explicitness is admissible discipline",
            "hidden reservoir remainder remains proof burden",
            "explicitness is weaker than divergence-safe coefficient law",
            "no postulate adopted",
            "downstream gates remain closed",
        ],
    ))

    for branch_id in [
        "explicitness_as_divergence_safe_theorem",
        "visible_channel_as_neutrality_theorem",
        "explicitness_as_source_no_double_counting",
        "explicitness_as_residual_control",
        "explicitness_as_parent_readiness",
        "explicitness_as_postulate_adoption",
        "explicitness_as_insertion",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; explicitness classifier is not theorem closure or postulate adoption.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g31_nonreservoir_explicitness_result",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Non-reservoir divergence explicitness is admissible as discipline requiring visible, auditable correction accounting. It can demand no hidden reservoir remainder, but this remains a proof burden unless derived. "
            "It is weaker than divergence-safe coefficient law and does not derive source no-double-counting. It does not adopt the Group 30 divergence explicitness candidate as a postulate. "
            "B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready."
        ),
        derivation_ids=["g31_nonreservoir_explicitness"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Nonreservoir Divergence Explicitness")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    criteria = build_criteria()
    boundaries = build_boundaries()
    obligations = build_obligations()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_symbolic_ledger(symbols, out)
    case_2_criteria(criteria, out)
    case_3_boundaries(boundaries, out)
    case_4_obligations(obligations, out)
    case_5_conclusions(conclusions, out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns, symbols)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
