# Candidate source divergence coefficient law classifier
#
# Group:
#   31_source_divergence_coefficient_law
#
# Script type:
#   SOURCE / DIVERGENCE COEFFICIENT-LAW CLASSIFIER
#
# Purpose
# -------
# Classify whether source/divergence constraints derive a coefficient law,
# partially constrain it, or leave it underdetermined/blocked.
#
# Locked-door question:
#
#   Did the source/divergence theorem route derive the coefficient law,
#   only partially constrain it, or expose an obstruction?
#
# This script does not adopt a new postulate.
# It does not derive B_s/F_zeta insertion.
# It does not derive active O.
# It does not derive residual control.
# It does not open the parent equation.
#
# Tiny goblin rule:
#
#   A clean channel is not yet a river map.

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
        "DERIVED": StatusMark.PASS,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "PARTIAL_CONSTRAINT": StatusMark.INFO,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "THEOREM_TARGET": StatusMark.OBLIGATION,
        "UNDERDETERMINED": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g31_explicitness",
            "31_source_divergence_coefficient_law__candidate_nonreservoir_divergence_explicitness",
            "g31_nonreservoir_explicitness",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_div_res",
            "31_source_divergence_coefficient_law__candidate_divergence_reservoir_obstruction",
            "g31_divergence_reservoir",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_coeff",
            "31_source_divergence_coefficient_law__candidate_coefficient_source_no_double_counting_tests",
            "g31_coeff_source_tests",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_dup",
            "31_source_divergence_coefficient_law__candidate_source_duplicate_load_ledger",
            "g31_source_duplicate_ledger",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_problem",
            "31_source_divergence_coefficient_law__candidate_source_divergence_problem_ledger",
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
class ClassifierSymbols:
    L_source_dup: sp.Symbol
    L_coeff_source: sp.Symbol
    L_div_reservoir: sp.Symbol
    L_explicitness: sp.Symbol
    N_trace: sp.Symbol
    M_safe: sp.Symbol
    I_residual: sp.Symbol
    C_law: sp.Symbol
    insertion_gap: sp.Symbol
    theorem_gap: sp.Expr


@dataclass
class ClassifierItem:
    name: str
    item: str
    status: str
    result: str
    blocker: str


@dataclass
class RouteClassification:
    name: str
    route: str
    status: str
    meaning: str


@dataclass
class RejectedUpgrade:
    name: str
    upgrade: str
    status: str
    reason: str


@dataclass
class ClassifierObligation:
    name: str
    obligation: str
    status: str
    blocks: str
    discipline: str


@dataclass
class ClassifierConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_symbols() -> ClassifierSymbols:
    (
        L_source_dup,
        L_coeff_source,
        L_div_reservoir,
        L_explicitness,
        N_trace,
        M_safe,
        I_residual,
        C_law,
        insertion_gap,
    ) = sp.symbols(
        "L_source_dup L_coeff_source L_div_reservoir L_explicitness "
        "N_trace M_safe I_residual C_law insertion_gap",
        real=True,
    )

    theorem_gap = sp.simplify(
        L_source_dup
        + L_coeff_source
        + L_div_reservoir
        + L_explicitness
        + N_trace
        + M_safe
        + I_residual
        + insertion_gap
    )

    return ClassifierSymbols(
        L_source_dup=L_source_dup,
        L_coeff_source=L_coeff_source,
        L_div_reservoir=L_div_reservoir,
        L_explicitness=L_explicitness,
        N_trace=N_trace,
        M_safe=M_safe,
        I_residual=I_residual,
        C_law=C_law,
        insertion_gap=insertion_gap,
        theorem_gap=theorem_gap,
    )


def build_items() -> List[ClassifierItem]:
    return [
        ClassifierItem(
            name="K1: duplicate source ledger",
            item="ordinary source cannot hide in coefficient/residual/boundary/support/correction/exchange/curvature/parent pockets",
            status="PARTIAL_CONSTRAINT",
            result="source pockets are named and forbidden as shortcuts",
            blocker="sector-by-sector zero or neutral route still not fully derived",
        ),
        ClassifierItem(
            name="K2: coefficient source neutrality",
            item="coefficient-side ordinary source load must vanish or be neutral",
            status="PARTIAL_CONSTRAINT",
            result="coefficient cannot carry ordinary rho/M_enc",
            blocker="full coefficient law not derived",
        ),
        ClassifierItem(
            name="K3: divergence reservoir obstruction",
            item="correction cannot hide source/boundary/current/mass/support/residual/parent loads",
            status="PARTIAL_CONSTRAINT",
            result="reservoir routes rejected",
            blocker="divergence-safe coefficient law not derived",
        ),
        ClassifierItem(
            name="K4: non-reservoir explicitness",
            item="correction must be visible, auditable, and non-reservoir",
            status="PARTIAL_CONSTRAINT",
            result="explicitness admissible as discipline",
            blocker="explicitness is weaker than divergence safety",
        ),
        ClassifierItem(
            name="K5: trace normalization",
            item="how B_s reads zeta",
            status="OPEN",
            result="not fixed by source/divergence route so far",
            blocker="N_trace remains open theorem target/candidate",
        ),
        ClassifierItem(
            name="K6: safe membership",
            item="zeta_Bs -> T_zeta",
            status="OPEN",
            result="not fixed by source/divergence route so far",
            blocker="M_safe remains open theorem target/candidate",
        ),
        ClassifierItem(
            name="K7: trace/residual incidence",
            item="I(T_zeta,R_zeta)=0 and I(T_zeta,R_kappa)=0",
            status="UNDERDETERMINED",
            result="not derived and remains high-risk",
            blocker="too close to no-overlap/residual-control smuggling",
        ),
        ClassifierItem(
            name="K8: coefficient law",
            item="complete B_s/F_zeta coefficient law",
            status="NOT_DERIVED",
            result="source/divergence gives constraints, not full law",
            blocker="normalization, membership, incidence, and insertion gaps remain",
        ),
    ]


def build_classifications() -> List[RouteClassification]:
    return [
        RouteClassification(
            name="R1: full derivation route",
            route="source/divergence constraints derive complete coefficient law",
            status="NOT_DERIVED",
            meaning="not achieved; constraints do not fix normalization/membership/incidence/insertion",
        ),
        RouteClassification(
            name="R2: partial constraint route",
            route="source/divergence constraints rule out hidden source and hidden reservoir behavior",
            status="PARTIAL_CONSTRAINT",
            meaning="achieved as necessary discipline",
        ),
        RouteClassification(
            name="R3: obstruction route",
            route="source/divergence route cannot close coefficient law without additional theorem or explicit choice",
            status="UNDERDETERMINED",
            meaning="current route remains incomplete rather than fully blocked",
        ),
        RouteClassification(
            name="R4: postulate route",
            route="adopt Group 30 candidate postulates to close law",
            status="REJECTED",
            meaning="forbidden without explicit user/theory decision",
        ),
        RouteClassification(
            name="R5: insertion route",
            route="use partial constraints as B_s/F_zeta insertion",
            status="REJECTED",
            meaning="constraints are not insertion",
        ),
    ]


def build_rejected() -> List[RejectedUpgrade]:
    return [
        RejectedUpgrade(
            name="U1: partial constraint as law",
            upgrade="source/divergence partial constraints treated as complete coefficient law",
            status="REJECTED",
            reason="normalization, membership, incidence, and insertion gaps remain",
        ),
        RejectedUpgrade(
            name="U2: explicitness as divergence safety",
            upgrade="non-reservoir explicitness treated as divergence-safe coefficient law",
            status="REJECTED",
            reason="explicitness is weaker than safety theorem",
        ),
        RejectedUpgrade(
            name="U3: source neutrality as no-double-counting theorem",
            upgrade="coefficient source neutrality treated as full source no-double-counting",
            status="REJECTED",
            reason="residual/boundary/support/correction/exchange/curvature/parent channels remain obligations",
        ),
        RejectedUpgrade(
            name="U4: source/divergence as insertion",
            upgrade="source/divergence constraints treated as B_s/F_zeta insertion",
            status="REJECTED",
            reason="insertion gap remains",
        ),
        RejectedUpgrade(
            name="U5: classifier as postulate adoption",
            upgrade="classifier result treated as adoption of Group 30 candidates",
            status="REJECTED",
            reason="candidate survival and classification are not adoption",
        ),
        RejectedUpgrade(
            name="U6: classifier as parent readiness",
            upgrade="source/divergence classifier opens parent equation",
            status="REJECTED",
            reason="parent gate remains closed",
        ),
    ]


def build_obligations() -> List[ClassifierObligation]:
    return [
        ClassifierObligation(
            name="O1: trace normalization fork",
            obligation="test whether source/divergence constraints force trace normalization or leave it open",
            status="OPEN",
            blocks="coefficient normalization",
            discipline="do not select from recovery",
        ),
        ClassifierObligation(
            name="O2: membership fork",
            obligation="keep safe trace membership separate unless derived",
            status="OPEN",
            blocks="sector membership",
            discipline="do not smuggle no-overlap",
        ),
        ClassifierObligation(
            name="O3: incidence caution",
            obligation="keep trace/residual incidence high-risk and unadopted",
            status="REQUIRED",
            blocks="residual-control honesty",
            discipline="do not hide residuals",
        ),
        ClassifierObligation(
            name="O4: source/divergence summary",
            obligation="summarize partial constraints and unresolved gaps",
            status="OPEN",
            blocks="Group 31 closure",
            discipline="partial constraint is not law",
        ),
        ClassifierObligation(
            name="O5: downstream gates",
            obligation="keep insertion, active O, residual control, and parent equation closed",
            status="NOT_READY",
            blocks="premature closure",
            discipline="classifier is not insertion",
        ),
    ]


def build_conclusions() -> List[ClassifierConclusion]:
    return [
        ClassifierConclusion(
            name="C1: theorem-route status",
            conclusion="source/divergence route gives partial constraints but not complete coefficient law",
            status="PARTIAL_CONSTRAINT",
            meaning="hidden source and reservoir routes are constrained/rejected",
        ),
        ClassifierConclusion(
            name="C2: no law",
            conclusion="complete B_s/F_zeta coefficient law is not derived",
            status="NOT_DERIVED",
            meaning="normalization, membership, incidence, and insertion gaps remain",
        ),
        ClassifierConclusion(
            name="C3: no adoption",
            conclusion="no Group 30 candidate postulate is adopted",
            status="NOT_ADOPTED",
            meaning="theorem-route failure/partiality does not select postulates",
        ),
        ClassifierConclusion(
            name="C4: no insertion",
            conclusion="B_s/F_zeta insertion is not derived",
            status="NOT_READY",
            meaning="partial constraints are not insertion",
        ),
        ClassifierConclusion(
            name="C5: next",
            conclusion="trace-normalization from source/divergence should be tested next",
            status="OPEN",
            meaning="the next fork is whether source/divergence fixes normalization or leaves it open",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Source/divergence coefficient-law classifier problem")
    print("Question:")
    print()
    print("  Did the source/divergence theorem route derive the coefficient law, only partially constrain it, or expose an obstruction?")
    print()
    print("Discipline:")
    print()
    print("  This script classifies theorem-route status.")
    print("  It adopts no postulate.")
    print("  It derives no insertion.")
    print()
    print("Tiny goblin rule:")
    print("  A clean channel is not yet a river map.")

    with out.governance_assessments():
        out.line(
            "source/divergence coefficient-law classifier opened",
            StatusMark.INFO,
            "classifying source/divergence route status",
        )


def case_1_symbolic_ledger(symbols: ClassifierSymbols, out: ScriptOutput) -> None:
    header("Case 1: Source/divergence classifier symbolic ledger")
    print("Classifier symbols:")
    print()
    for name in [
        "L_source_dup",
        "L_coeff_source",
        "L_div_reservoir",
        "L_explicitness",
        "N_trace",
        "M_safe",
        "I_residual",
        "C_law",
        "insertion_gap",
    ]:
        print(f"  {name} = {sp.sstr(getattr(symbols, name))}")

    print()
    print("Source/divergence theorem gap:")
    print(f"  G_source_divergence = {sp.sstr(symbols.theorem_gap)}")

    with out.derived_results():
        out.line(
            "source/divergence theorem gap stated",
            StatusMark.OBLIGATION,
            f"G_source_divergence = {sp.sstr(symbols.theorem_gap)}",
        )


def case_2_items(items: List[ClassifierItem], out: ScriptOutput) -> None:
    header("Case 2: Source/divergence classifier items")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Item: {item.item}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Result: {item.result}")
        print(f"Blocker: {item.blocker}")

    with out.governance_assessments():
        out.line(
            "source/divergence classifier items stated",
            StatusMark.DEFER,
            f"{len(items)} classifier items stated",
        )


def case_3_classifications(items: List[RouteClassification], out: ScriptOutput) -> None:
    header("Case 3: Route classifications")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Route: {item.route}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Meaning: {item.meaning}")

    with out.governance_assessments():
        out.line(
            "source/divergence route classification stated",
            StatusMark.PASS,
            "route classified as partial constraint, not full law",
        )


def case_4_rejected(items: List[RejectedUpgrade], out: ScriptOutput) -> None:
    header("Case 4: Rejected classifier upgrades")
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
            "source/divergence classifier upgrades rejected",
            StatusMark.FAIL,
            "law, divergence safety, source theorem, insertion, postulate adoption, and parent readiness upgrades rejected",
        )


def case_5_obligations(items: List[ClassifierObligation], out: ScriptOutput) -> None:
    header("Case 5: Classifier obligations")
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
            "source/divergence classifier obligations stated",
            StatusMark.OBLIGATION,
            f"{len(items)} obligations remain",
        )


def case_6_conclusions(items: List[ClassifierConclusion], out: ScriptOutput) -> None:
    header("Case 6: Classifier conclusions")
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
            "source/divergence classifier conclusion stated",
            StatusMark.PASS,
            "partial constraints only; trace-normalization fork next",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Source/divergence coefficient-law classifier result:")
    print()
    print("  The source/divergence route gives partial constraints but does not derive the complete coefficient law.")
    print("  It rules out hidden ordinary source carriers and hidden divergence reservoirs as admissible shortcuts.")
    print("  It does not fix trace normalization.")
    print("  It does not derive safe trace membership.")
    print("  It does not derive trace/residual incidence.")
    print("  It does not derive B_s/F_zeta insertion.")
    print("  No Group 30 candidate postulate is adopted.")
    print("  Active O, residual control, and parent equation remain not ready.")
    print()
    print("Possible next script:")
    print("  candidate_trace_normalization_from_source_divergence.py")
    print()
    print("Tiny goblin label:")
    print("  A clean channel is not yet a river map.")

    with out.governance_assessments():
        out.line(
            "source/divergence coefficient-law classifier complete",
            StatusMark.PASS,
            "trace-normalization from source/divergence should run next",
        )


def record_derivations(ns, symbols: ClassifierSymbols) -> None:
    ns.record_derivation(
        derivation_id="g31_source_divergence_classifier",
        inputs=[
            symbols.L_source_dup,
            symbols.L_coeff_source,
            symbols.L_div_reservoir,
            symbols.L_explicitness,
            symbols.N_trace,
            symbols.M_safe,
            symbols.I_residual,
            symbols.insertion_gap,
        ],
        output=symbols.theorem_gap,
        method="classify source/divergence theorem route as partial constraint, not full coefficient law",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="source_divergence_coefficient_law_classifier_marker",
        scope="Group 31 source/divergence coefficient law",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g31_cls_trace_norm_next", "Test trace normalization from source/divergence next"),
        ("g31_cls_membership_open", "Keep safe trace membership open unless derived"),
        ("g31_cls_incidence_high_risk", "Keep trace/residual incidence high-risk"),
        ("g31_cls_no_law_overclaim", "Do not treat partial constraints as coefficient law"),
        ("g31_cls_no_postulate", "Do not adopt Group 30 candidates"),
        ("g31_cls_no_insertion", "Do not treat classifier as insertion"),
        ("g31_cls_downstream_closed", "Keep insertion/O/residual/parent gates closed"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g31_classifier_route"],
            description=(
                "Source/divergence constraints partially constrain coefficient behavior but do not derive the full coefficient law or insertion."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g31_cls_trace_norm_next",
        "g31_cls_membership_open",
        "g31_cls_incidence_high_risk",
        "g31_cls_no_law_overclaim",
        "g31_cls_no_postulate",
        "g31_cls_no_insertion",
        "g31_cls_downstream_closed",
    ]

    ns.record_route(RouteRecord(
        route_id="g31_classifier_route",
        script_id=SCRIPT_ID,
        name="Group 31 source/divergence coefficient-law classifier route",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "source/divergence constraints are partial constraints",
            "complete coefficient law is not derived",
            "trace normalization remains open",
            "safe membership remains open",
            "trace/residual incidence remains high-risk",
            "no postulate adopted",
            "downstream gates remain closed",
        ],
    ))

    for branch_id in [
        "partial_constraint_as_full_law",
        "explicitness_as_divergence_safety",
        "source_neutrality_as_full_source_theorem",
        "source_divergence_as_insertion",
        "classifier_as_postulate_adoption",
        "classifier_as_parent_readiness",
        "classifier_as_active_O_readiness",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; classifier is not theorem closure or postulate adoption.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g31_source_divergence_partial_constraint",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "The source/divergence route gives partial constraints but does not derive the complete coefficient law. "
            "It rules out hidden ordinary source carriers and hidden divergence reservoirs as admissible shortcuts. "
            "It does not fix trace normalization, derive safe trace membership, derive trace/residual incidence, or derive B_s/F_zeta insertion. "
            "No Group 30 candidate postulate is adopted. Active O, residual control, and parent equation remain not ready."
        ),
        derivation_ids=["g31_source_divergence_classifier"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Source Divergence Coefficient Law Classifier")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    items = build_items()
    classifications = build_classifications()
    rejected = build_rejected()
    obligations = build_obligations()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_symbolic_ledger(symbols, out)
    case_2_items(items, out)
    case_3_classifications(classifications, out)
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
