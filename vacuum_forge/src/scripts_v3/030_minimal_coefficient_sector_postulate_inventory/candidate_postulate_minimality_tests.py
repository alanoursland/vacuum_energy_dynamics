# Candidate postulate minimality tests
#
# Group:
#   30_minimal_coefficient_sector_postulate_inventory
#
# Script type:
#   MINIMALITY / INDEPENDENCE TEST LEDGER
#
# Purpose
# -------
# Test which candidate postulates are independent, minimal, and not redundant.
#
# Locked-door question:
#
#   Which candidate postulates are minimal independent choices rather than bundled theorem closure?
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
#   A tooth that opens three locks is probably a crowbar.

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
        "BUNDLED": StatusMark.FAIL,
        "CANDIDATE_POSTULATE": StatusMark.OBLIGATION,
        "CONDITIONAL_CANDIDATE": StatusMark.DEFER,
        "HIGH_RISK": StatusMark.DEFER,
        "INDEPENDENT_CANDIDATE": StatusMark.INFO,
        "MINIMAL_CANDIDATE": StatusMark.INFO,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "THEOREM_ROUTE_PREFERRED": StatusMark.INFO,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g30_problem",
            "30_minimal_coefficient_sector_postulate_inventory__candidate_minimal_postulate_problem_ledger",
            "g30_postulate_problem",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g29_summary",
            "29_Bs_Fzeta_coefficient_origin__candidate_group_29_status_summary",
            "g29_status_summary",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g29_obligations",
            "29_Bs_Fzeta_coefficient_origin__candidate_coefficient_origin_obligations",
            "g29_obligations",
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
class MinimalitySymbols:
    P_trace_norm: sp.Symbol
    P_safe_membership: sp.Symbol
    P_incidence: sp.Symbol
    P_source_once: sp.Symbol
    P_guardrail_visibility: sp.Symbol
    P_divergence_explicit: sp.Symbol
    bundle_penalty: sp.Symbol
    dependency_penalty: sp.Symbol
    smuggling_penalty: sp.Symbol
    downstream_penalty: sp.Symbol
    minimality_load: sp.Expr


@dataclass
class MinimalityTest:
    name: str
    candidate: str
    independence: str
    minimality_status: str
    reason: str
    risk: str


@dataclass
class DependencyRelation:
    name: str
    relation: str
    status: str
    meaning: str


@dataclass
class OverlargeBundle:
    name: str
    bundle: str
    status: str
    reason: str


@dataclass
class MinimalityObligation:
    name: str
    obligation: str
    status: str
    blocks: str
    discipline: str


@dataclass
class MinimalityConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_symbols() -> MinimalitySymbols:
    (
        P_trace_norm,
        P_safe_membership,
        P_incidence,
        P_source_once,
        P_guardrail_visibility,
        P_divergence_explicit,
        bundle_penalty,
        dependency_penalty,
        smuggling_penalty,
        downstream_penalty,
    ) = sp.symbols(
        "P_trace_norm P_safe_membership P_incidence P_source_once "
        "P_guardrail_visibility P_divergence_explicit "
        "bundle_penalty dependency_penalty smuggling_penalty downstream_penalty",
        real=True,
    )

    minimality_load = sp.simplify(
        P_trace_norm
        + P_safe_membership
        + P_incidence
        + P_source_once
        + P_guardrail_visibility
        + P_divergence_explicit
        + bundle_penalty
        + dependency_penalty
        + smuggling_penalty
        + downstream_penalty
    )

    return MinimalitySymbols(
        P_trace_norm=P_trace_norm,
        P_safe_membership=P_safe_membership,
        P_incidence=P_incidence,
        P_source_once=P_source_once,
        P_guardrail_visibility=P_guardrail_visibility,
        P_divergence_explicit=P_divergence_explicit,
        bundle_penalty=bundle_penalty,
        dependency_penalty=dependency_penalty,
        smuggling_penalty=smuggling_penalty,
        downstream_penalty=downstream_penalty,
        minimality_load=minimality_load,
    )


def build_tests() -> List[MinimalityTest]:
    return [
        MinimalityTest(
            name="T1: trace-normalization",
            candidate="B_s reads the volume-trace scalar through a fixed normalization rule",
            independence="independent of membership, incidence, source routing, and divergence",
            minimality_status="MINIMAL_CANDIDATE",
            reason="closes only the normalization gap if stated narrowly",
            risk="chosen from recovery rather than structural role",
        ),
        MinimalityTest(
            name="T2: safe-trace membership",
            candidate="zeta_Bs is assigned to T_zeta as safe trace membership",
            independence="independent of normalization and zero incidence",
            minimality_status="MINIMAL_CANDIDATE",
            reason="turns constrained candidate into explicit membership only",
            risk="may be mistaken for no-overlap or residual control",
        ),
        MinimalityTest(
            name="T3: trace/residual incidence",
            candidate="I(T_zeta,R_zeta)=0 and/or I(T_zeta,R_kappa)=0",
            independence="depends on membership but not on source routing",
            minimality_status="HIGH_RISK",
            reason="minimal if stated only as incidence, but very close to residual-control/no-overlap theorem",
            risk="smuggles residual kill or hides residuals",
        ),
        MinimalityTest(
            name="T4: source no-double-counting",
            candidate="ordinary source load enters once and is not duplicated through coefficient/accounting sectors",
            independence="independent from trace normalization and membership",
            minimality_status="CONDITIONAL_CANDIDATE",
            reason="could be a minimal postulate, but source/divergence theorem route may be preferred",
            risk="chosen by repair or used as insertion shortcut",
        ),
        MinimalityTest(
            name="T5: guardrail visibility",
            candidate="boundary/current/mass/support loads remain visible and non-reservoir",
            independence="independent from neutrality theorem",
            minimality_status="MINIMAL_CANDIDATE",
            reason="visibility is weaker than neutrality and only forbids hiding",
            risk="mistaken for boundary/current/mass/support neutralities",
        ),
        MinimalityTest(
            name="T6: divergence explicitness",
            candidate="any divergence correction must be explicit, auditable, and non-reservoir",
            independence="independent from divergence-safe theorem",
            minimality_status="MINIMAL_CANDIDATE",
            reason="requires visibility of correction without asserting divergence closure",
            risk="correction becomes hidden parent-fit reservoir",
        ),
    ]


def build_dependencies() -> List[DependencyRelation]:
    return [
        DependencyRelation(
            name="D1: normalization versus membership",
            relation="trace-normalization does not imply zeta_Bs -> T_zeta membership",
            status="INDEPENDENT_CANDIDATE",
            meaning="P_trace_norm and P_safe_membership are separable",
        ),
        DependencyRelation(
            name="D2: membership versus incidence",
            relation="safe trace membership does not imply I(T_zeta,R_zeta)=0 or I(T_zeta,R_kappa)=0",
            status="INDEPENDENT_CANDIDATE",
            meaning="P_incidence is separate and higher risk",
        ),
        DependencyRelation(
            name="D3: incidence versus residual control",
            relation="zero incidence must not be upgraded to residual kill or inertness",
            status="REQUIRED",
            meaning="incidence candidate must remain narrow if retained",
        ),
        DependencyRelation(
            name="D4: source versus divergence",
            relation="source no-double-counting and divergence explicitness are related but not identical",
            status="CONDITIONAL_CANDIDATE",
            meaning="source/divergence theorem route may handle both without postulating both",
        ),
        DependencyRelation(
            name="D5: visibility versus neutrality",
            relation="guardrail visibility does not imply boundary/current/mass/support neutralities",
            status="INDEPENDENT_CANDIDATE",
            meaning="P_guardrail_visibility is weaker and more minimal than neutrality",
        ),
        DependencyRelation(
            name="D6: postulate inventory versus insertion",
            relation="no candidate postulate alone derives B_s/F_zeta insertion",
            status="REQUIRED",
            meaning="insertion gate remains closed",
        ),
    ]


def build_bundles() -> List[OverlargeBundle]:
    return [
        OverlargeBundle(
            name="B1: insertion bundle",
            bundle="postulate trace normalization + membership + incidence + source + divergence as B_s/F_zeta insertion",
            status="REJECTED",
            reason="collapses all missing laws into one endpoint-selected package",
        ),
        OverlargeBundle(
            name="B2: no-overlap bundle",
            bundle="postulate membership and zero incidence as complete no-overlap geometry",
            status="REJECTED",
            reason="too strong; hides sector geometry obligations",
        ),
        OverlargeBundle(
            name="B3: residual-control bundle",
            bundle="postulate incidence plus residual inertness/kill",
            status="REJECTED",
            reason="residual control remains not derived and cannot be chosen by bundle",
        ),
        OverlargeBundle(
            name="B4: guardrail-neutrality bundle",
            bundle="postulate visibility plus boundary/current/mass/support neutralities",
            status="REJECTED",
            reason="visibility is admissible candidate; neutrality theorem is not derived",
        ),
        OverlargeBundle(
            name="B5: parent-closure bundle",
            bundle="postulate source/divergence behavior so parent equation closes",
            status="REJECTED",
            reason="parent fit cannot select postulates",
        ),
    ]


def build_obligations() -> List[MinimalityObligation]:
    return [
        MinimalityObligation(
            name="O1: anti-smuggling filter next",
            obligation="run postulate smuggling filter against all surviving candidates",
            status="REQUIRED",
            blocks="admissible postulate inventory",
            discipline="recovery, repair, active O, residual cleanup, and parent fit may not select",
        ),
        MinimalityObligation(
            name="O2: keep candidates narrow",
            obligation="state each candidate as only one missing tooth",
            status="REQUIRED",
            blocks="minimality",
            discipline="reject bundled theorem closure",
        ),
        MinimalityObligation(
            name="O3: incidence caution",
            obligation="treat trace/residual incidence as high-risk candidate",
            status="REQUIRED",
            blocks="residual-control honesty",
            discipline="do not hide residuals or claim no-overlap theorem",
        ),
        MinimalityObligation(
            name="O4: source/divergence fork",
            obligation="decide whether source no-double-counting and divergence explicitness should be theorem route or postulate candidates",
            status="OPEN",
            blocks="field-equation usability",
            discipline="do not hide source or correction load",
        ),
        MinimalityObligation(
            name="O5: downstream gates",
            obligation="keep insertion, active O, residual control, and parent equation closed",
            status="NOT_READY",
            blocks="premature closure",
            discipline="minimality is not adoption or theorem closure",
        ),
    ]


def build_conclusions() -> List[MinimalityConclusion]:
    return [
        MinimalityConclusion(
            name="C1: narrow candidates",
            conclusion="trace normalization, safe membership, guardrail visibility, and divergence explicitness survive as narrow minimal candidates",
            status="MINIMAL_CANDIDATE",
            meaning="subject to anti-smuggling filter and no adoption yet",
        ),
        MinimalityConclusion(
            name="C2: source candidate",
            conclusion="source no-double-counting is conditional",
            status="CONDITIONAL_CANDIDATE",
            meaning="may be better pursued as source/divergence theorem route",
        ),
        MinimalityConclusion(
            name="C3: incidence candidate",
            conclusion="trace/residual incidence is high-risk",
            status="HIGH_RISK",
            meaning="may be too close to postulating no-overlap/residual control",
        ),
        MinimalityConclusion(
            name="C4: bundles",
            conclusion="overlarge insertion/no-overlap/residual/parent bundles are rejected",
            status="REJECTED",
            meaning="postulates must not collapse theorem targets",
        ),
        MinimalityConclusion(
            name="C5: adoption",
            conclusion="no postulate is adopted",
            status="NOT_ADOPTED",
            meaning="minimality tests classify candidates only",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Postulate minimality problem")
    print("Question:")
    print()
    print("  Which candidate postulates are minimal independent choices rather than bundled theorem closure?")
    print()
    print("Discipline:")
    print()
    print("  This script classifies minimality.")
    print("  It adopts no postulate.")
    print("  It derives no insertion.")
    print()
    print("Tiny goblin rule:")
    print("  A tooth that opens three locks is probably a crowbar.")

    with out.governance_assessments():
        out.line(
            "postulate minimality tests opened",
            StatusMark.INFO,
            "testing independence and minimality of candidate postulate families",
        )


def case_1_symbolic_ledger(symbols: MinimalitySymbols, out: ScriptOutput) -> None:
    header("Case 1: Postulate minimality symbolic ledger")
    print("Minimality symbols:")
    print()
    for name in [
        "P_trace_norm",
        "P_safe_membership",
        "P_incidence",
        "P_source_once",
        "P_guardrail_visibility",
        "P_divergence_explicit",
        "bundle_penalty",
        "dependency_penalty",
        "smuggling_penalty",
        "downstream_penalty",
    ]:
        print(f"  {name} = {sp.sstr(getattr(symbols, name))}")
    print()
    print("Minimality load:")
    print()
    print(f"  L_postulate_minimality = {sp.sstr(symbols.minimality_load)}")

    with out.derived_results():
        out.line(
            "postulate minimality load stated",
            StatusMark.OBLIGATION,
            f"L_postulate_minimality = {sp.sstr(symbols.minimality_load)}",
        )


def case_2_tests(items: List[MinimalityTest], out: ScriptOutput) -> None:
    header("Case 2: Candidate postulate minimality tests")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Candidate: {item.candidate}")
        print(f"Independence: {item.independence}")
        print(f"[{status_mark(item.minimality_status).value}] {item.name}: {item.minimality_status}")
        print(f"Reason: {item.reason}")
        print(f"Risk: {item.risk}")

    with out.governance_assessments():
        out.line(
            "candidate postulate minimality tests completed",
            StatusMark.DEFER,
            f"{len(items)} candidate postulates tested for minimality",
        )


def case_3_dependencies(items: List[DependencyRelation], out: ScriptOutput) -> None:
    header("Case 3: Candidate postulate dependency relations")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Relation: {item.relation}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Meaning: {item.meaning}")

    with out.governance_assessments():
        out.line(
            "candidate postulate dependencies classified",
            StatusMark.DEFER,
            f"{len(items)} dependency relations classified",
        )


def case_4_bundles(items: List[OverlargeBundle], out: ScriptOutput) -> None:
    header("Case 4: Rejected overlarge bundles")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Bundle: {item.bundle}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Reason: {item.reason}")

    with out.counterexamples():
        out.line(
            "overlarge postulate bundles rejected",
            StatusMark.FAIL,
            "insertion/no-overlap/residual-control/guardrail-neutrality/parent bundles rejected",
        )


def case_5_obligations(items: List[MinimalityObligation], out: ScriptOutput) -> None:
    header("Case 5: Minimality obligations")
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
            "minimality obligations stated",
            StatusMark.OBLIGATION,
            f"{len(items)} minimality obligations remain",
        )


def case_6_conclusions(items: List[MinimalityConclusion], out: ScriptOutput) -> None:
    header("Case 6: Minimality conclusions")
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
            "postulate minimality conclusions stated",
            StatusMark.PASS,
            "narrow candidates classified; overlarge bundles rejected; no postulate adopted",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Postulate minimality result:")
    print()
    print("  Trace normalization survives as a narrow minimal candidate.")
    print("  Safe trace membership survives as a narrow minimal candidate.")
    print("  Guardrail visibility survives as a narrow minimal candidate.")
    print("  Divergence explicitness survives as a narrow minimal candidate.")
    print("  Source no-double-counting is conditional; theorem route may be preferred.")
    print("  Trace/residual incidence is high-risk because it may smuggle no-overlap or residual control.")
    print("  Overlarge insertion, no-overlap, residual-control, guardrail-neutrality, and parent bundles are rejected.")
    print("  No postulate is adopted.")
    print("  B_s/F_zeta insertion is not derived.")
    print("  Active O, residual control, and parent equation remain not ready.")
    print()
    print("Possible next script:")
    print("  candidate_postulate_smuggling_filter.py")
    print()
    print("Tiny goblin label:")
    print("  A tooth that opens three locks is probably a crowbar.")

    with out.governance_assessments():
        out.line(
            "postulate minimality tests complete",
            StatusMark.PASS,
            "postulate smuggling filter should run next",
        )


def record_derivations(ns, symbols: MinimalitySymbols) -> None:
    ns.record_derivation(
        derivation_id="g30_postulate_minimality",
        inputs=[
            symbols.P_trace_norm,
            symbols.P_safe_membership,
            symbols.P_incidence,
            symbols.P_source_once,
            symbols.P_guardrail_visibility,
            symbols.P_divergence_explicit,
            symbols.bundle_penalty,
            symbols.dependency_penalty,
            symbols.smuggling_penalty,
            symbols.downstream_penalty,
        ],
        output=symbols.minimality_load,
        method="test candidate postulates for independence and minimality without adopting them",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="postulate_minimality_marker",
        scope="Group 30 minimal coefficient/sector postulate inventory",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g30_min_filter_next", "Run postulate smuggling filter next"),
        ("g30_min_narrowness", "Keep postulates narrow and independent"),
        ("g30_min_incidence_caution", "Treat trace/residual incidence as high-risk"),
        ("g30_min_source_div_fork", "Resolve source/divergence theorem route versus postulate route"),
        ("g30_min_no_bundles", "Reject overlarge theorem-closure bundles"),
        ("g30_min_downstream", "Keep insertion/O/residual/parent gates closed"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g30_minimality_route"],
            description=(
                "Candidate postulates are classified for minimality only. No postulate is adopted and no downstream theorem is derived."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g30_min_filter_next",
        "g30_min_narrowness",
        "g30_min_incidence_caution",
        "g30_min_source_div_fork",
        "g30_min_no_bundles",
        "g30_min_downstream",
    ]

    ns.record_route(RouteRecord(
        route_id="g30_minimality_route",
        script_id=SCRIPT_ID,
        name="Group 30 postulate minimality route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "candidate postulates remain unadopted",
            "trace normalization, safe membership, guardrail visibility, and divergence explicitness survive as narrow candidates",
            "source no-double-counting is conditional",
            "trace/residual incidence is high-risk",
            "overlarge bundles are rejected",
            "downstream gates remain closed",
        ],
    ))

    for branch_id in [
        "insertion_bundle",
        "no_overlap_bundle",
        "residual_control_bundle",
        "guardrail_neutrality_bundle",
        "parent_closure_bundle",
        "minimality_as_adoption",
        "minimality_as_insertion",
        "minimality_as_parent_readiness",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; minimality classification is not adoption or theorem closure.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g30_postulate_minimality_result",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Trace normalization, safe trace membership, guardrail visibility, and divergence explicitness survive as narrow minimal candidates. "
            "Source no-double-counting is conditional and may be better pursued as theorem route. Trace/residual incidence is high-risk because it may smuggle no-overlap or residual control. "
            "Overlarge insertion, no-overlap, residual-control, guardrail-neutrality, and parent bundles are rejected. No postulate is adopted. "
            "B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready."
        ),
        derivation_ids=["g30_postulate_minimality"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Postulate Minimality Tests")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    tests = build_tests()
    dependencies = build_dependencies()
    bundles = build_bundles()
    obligations = build_obligations()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_symbolic_ledger(symbols, out)
    case_2_tests(tests, out)
    case_3_dependencies(dependencies, out)
    case_4_bundles(bundles, out)
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
