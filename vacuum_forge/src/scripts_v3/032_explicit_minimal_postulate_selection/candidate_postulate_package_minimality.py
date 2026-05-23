# Candidate postulate package minimality
#
# Group:
#   32_explicit_minimal_postulate_selection
#
# Human title:
#   Explicit Minimal Postulate Selection
#
# Script type:
#   MINIMALITY ACCOUNTING / PACKAGE REMOVAL TESTS
#
# Purpose
# -------
# Run minimality accounting after the package sieve classified the Group 32
# package families as insufficient, plausible-to-audit, overstrong, or rejected
# as current shortcut packages.
#
# Locked-door question:
#
#   Under the currently declared trace-anchor audit criteria, is Package B
#   minimal plausible-to-audit, or does it carry removable, missing, or
#   overstrong load?
#
# This script does not adopt a postulate.
# It does not recommend adoption.
# It does not select Package B.
# It does not derive trace normalization.
# It does not derive safe trace membership.
# It does not derive trace/residual incidence.
# It does not derive the complete coefficient law.
# It does not derive B_s/F_zeta insertion.
# It does not derive active O.
# It does not derive residual control.
# It does not open the parent equation.
#
# Tiny goblin rule:
#
#   Weigh each tooth. Still do not bite.

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


def subheader(title: str) -> None:
    print()
    print("-" * 120)
    print(title)
    print("-" * 120)


def status_mark(status: str) -> StatusMark:
    return {
        "ADOPTION_SEPARATE": StatusMark.DEFER,
        "BLOCKED": StatusMark.FAIL,
        "CANDIDATE_ROUTE": StatusMark.DEFER,
        "HIGH_RISK_STRONG_PACKAGE": StatusMark.DEFER,
        "INSUFFICIENT": StatusMark.DEFER,
        "MINIMALITY_ACCOUNTING": StatusMark.INFO,
        "MINIMAL_PLAUSIBLE_TO_AUDIT": StatusMark.INFO,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "OVERSTRONG": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REJECTED_AS_CURRENT_SHORTCUT": StatusMark.FAIL,
        "REMOVAL_BREAKS_AUDIT": StatusMark.OBLIGATION,
        "REQUIRED": StatusMark.OBLIGATION,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g32_package_sieve",
            "032_explicit_minimal_postulate_selection__candidate_postulate_package_sieve",
            "g32_postulate_package_sieve",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g32_dependency_graph",
            "032_explicit_minimal_postulate_selection__candidate_postulate_dependency_graph",
            "g32_postulate_dependency_graph",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g32_candidate_ledger",
            "032_explicit_minimal_postulate_selection__candidate_postulate_candidate_ledger",
            "g32_candidate_postulate_ledger",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g32_problem",
            "032_explicit_minimal_postulate_selection__candidate_explicit_postulate_selection_problem",
            "g32_explicit_selection_problem",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_summary",
            "031_source_divergence_coefficient_law__candidate_group_31_status_summary",
            "g31_status_summary",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_obligations",
            "031_source_divergence_coefficient_law__candidate_source_divergence_obligations",
            "g31_obligations",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g30_summary",
            "030_minimal_coefficient_sector_postulate_inventory__candidate_group_30_status_summary",
            "g30_status_summary",
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
    P_guardrail_visibility: sp.Symbol
    P_div_explicitness: sp.Symbol
    P_source_no_hidden: sp.Symbol
    P_incidence_zero: sp.Symbol
    P_active_O: sp.Symbol
    P_residual_kill: sp.Symbol
    P_insertion: sp.Symbol
    P_parent: sp.Symbol
    L_package_B: sp.Expr
    L_required_trace_anchor: sp.Expr
    L_required_discipline: sp.Expr
    L_downstream_forbidden: sp.Expr
    L_overstrong_additions: sp.Expr
    L_minimality_gap: sp.Expr


@dataclass
class RemovalTest:
    name: str
    removed: str
    status: str
    result: str
    why_required: str
    forbidden_upgrade: str


@dataclass
class PackageAccountingEntry:
    name: str
    package: str
    status: str
    minimality_result: str
    reason: str
    boundary: str


@dataclass
class MinimalityRule:
    name: str
    rule: str
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
        P_guardrail_visibility,
        P_div_explicitness,
        P_source_no_hidden,
        P_incidence_zero,
        P_active_O,
        P_residual_kill,
        P_insertion,
        P_parent,
    ) = sp.symbols(
        "P_trace_norm P_safe_membership P_guardrail_visibility P_div_explicitness "
        "P_source_no_hidden P_incidence_zero P_active_O P_residual_kill P_insertion P_parent",
        real=True,
    )

    L_required_trace_anchor = sp.simplify(P_trace_norm + P_safe_membership)
    L_required_discipline = sp.simplify(P_guardrail_visibility + P_div_explicitness + P_source_no_hidden)
    L_package_B = sp.simplify(L_required_trace_anchor + L_required_discipline)
    L_downstream_forbidden = sp.simplify(P_active_O + P_residual_kill + P_insertion + P_parent)
    L_overstrong_additions = sp.simplify(P_incidence_zero + P_residual_kill)
    L_minimality_gap = sp.simplify(L_package_B + L_downstream_forbidden + P_incidence_zero)

    return MinimalitySymbols(
        P_trace_norm=P_trace_norm,
        P_safe_membership=P_safe_membership,
        P_guardrail_visibility=P_guardrail_visibility,
        P_div_explicitness=P_div_explicitness,
        P_source_no_hidden=P_source_no_hidden,
        P_incidence_zero=P_incidence_zero,
        P_active_O=P_active_O,
        P_residual_kill=P_residual_kill,
        P_insertion=P_insertion,
        P_parent=P_parent,
        L_package_B=L_package_B,
        L_required_trace_anchor=L_required_trace_anchor,
        L_required_discipline=L_required_discipline,
        L_downstream_forbidden=L_downstream_forbidden,
        L_overstrong_additions=L_overstrong_additions,
        L_minimality_gap=L_minimality_gap,
    )


def build_removal_tests() -> List[RemovalTest]:
    return [
        RemovalTest(
            name="R1: remove trace normalization",
            removed="P_trace_norm",
            status="REMOVAL_BREAKS_AUDIT",
            result="Package B becomes membership-plus-discipline only and cannot specify how B_s reads zeta",
            why_required="trace-anchor audit requires the normalization role to be present",
            forbidden_upgrade="safe membership must not choose normalization by implication",
        ),
        RemovalTest(
            name="R2: remove safe membership",
            removed="P_safe_membership",
            status="REMOVAL_BREAKS_AUDIT",
            result="Package B becomes normalization-plus-discipline only and cannot assign zeta_Bs to T_zeta",
            why_required="trace-anchor audit requires membership assignment to be present",
            forbidden_upgrade="trace normalization must not become membership by implication",
        ),
        RemovalTest(
            name="R3: remove guardrail visibility",
            removed="P_guardrail_visibility",
            status="REMOVAL_BREAKS_AUDIT",
            result="boundary/source/current/mass/support loads are no longer required to remain visible and auditable",
            why_required="auditable package accounting requires visible guardrail loads",
            forbidden_upgrade="hidden guardrail load must not be treated as neutrality",
        ),
        RemovalTest(
            name="R4: remove divergence explicitness",
            removed="P_div_explicitness",
            status="REMOVAL_BREAKS_AUDIT",
            result="correction/divergence behavior is no longer required to be explicit and non-reservoir",
            why_required="package accounting must not reopen hidden divergence reservoirs",
            forbidden_upgrade="absence of explicitness must not be patched by divergence-safe-law language",
        ),
        RemovalTest(
            name="R5: remove inherited source-hidden exclusion",
            removed="P_source_no_hidden",
            status="REMOVAL_BREAKS_AUDIT",
            result="ordinary source hidden-pocket exclusions from Group 31 are no longer carried into the package",
            why_required="minimality accounting must preserve inherited anti-smuggling discipline",
            forbidden_upgrade="hidden-pocket exclusion is still not full source no-double-counting theorem",
        ),
    ]


def build_package_accounting() -> List[PackageAccountingEntry]:
    return [
        PackageAccountingEntry(
            name="A: visibility-only package",
            package="P_guardrail_visibility + P_div_explicitness + P_source_no_hidden",
            status="INSUFFICIENT",
            minimality_result="smaller discipline package but missing both trace-anchor candidates",
            reason="fails trace-anchor completeness because P_trace_norm and P_safe_membership are absent",
            boundary="may remain useful discipline, but not a minimal trace-anchor package",
        ),
        PackageAccountingEntry(
            name="B: trace-anchor package",
            package="P_trace_norm + P_safe_membership + P_guardrail_visibility + P_div_explicitness + P_source_no_hidden",
            status="MINIMAL_PLAUSIBLE_TO_AUDIT",
            minimality_result="no listed component can be removed without breaking the current trace-anchor audit criteria",
            reason="contains both fresh trace-anchor candidates and the inherited/discipline guardrails required by the sieve",
            boundary="minimal plausible-to-audit is not selected, not adopted, and not recommended for adoption",
        ),
        PackageAccountingEntry(
            name="C: too-strong no-overlap package",
            package="P_trace_norm + P_safe_membership + P_incidence_zero + P_residual_kill",
            status="OVERSTRONG",
            minimality_result="adds high-risk incidence and residual-kill load while omitting visibility/explicitness/source-hidden guardrails",
            reason="not ordinary minimal package; it mixes trace-anchor choices with downstream residual-control content",
            boundary="may only be studied as high-risk strong package or theorem target",
        ),
        PackageAccountingEntry(
            name="D: parent-closure shortcut package",
            package="P_insertion + P_active_O + P_parent",
            status="REJECTED_AS_CURRENT_SHORTCUT",
            minimality_result="not a prerequisite package; it is a bundle of downstream gates",
            reason="active O, insertion, and parent closure are not ready and not constructed",
            boundary="rejected as current shortcut, not permanent mathematical no-go theorem",
        ),
        PackageAccountingEntry(
            name="E: trace normalization only package",
            package="P_trace_norm + P_guardrail_visibility + P_div_explicitness + P_source_no_hidden",
            status="INSUFFICIENT",
            minimality_result="missing safe membership",
            reason="normalization alone does not assign zeta_Bs to T_zeta",
            boundary="normalization is not membership",
        ),
        PackageAccountingEntry(
            name="F: membership only package",
            package="P_safe_membership + P_guardrail_visibility + P_div_explicitness + P_source_no_hidden",
            status="INSUFFICIENT",
            minimality_result="missing trace normalization",
            reason="membership alone does not specify how B_s reads zeta",
            boundary="membership is not normalization or incidence",
        ),
    ]


def build_rules() -> List[MinimalityRule]:
    return [
        MinimalityRule(
            name="M1: minimal plausible-to-audit is not adoption",
            rule="Package B may be minimal plausible-to-audit under current criteria without being adopted",
            status="POLICY_RULE",
            reason="minimality accounting is weaker than explicit postulate selection",
        ),
        MinimalityRule(
            name="M2: removal test is not theorem proof",
            rule="a removal breaking current audit criteria does not prove the removed postulate is physically true",
            status="POLICY_RULE",
            reason="criteria are governance/audit criteria, not derivation of the postulates",
        ),
        MinimalityRule(
            name="M3: inherited discipline remains inherited",
            rule="P_source_no_hidden contributes to package accounting as inherited discipline unless explicitly restated",
            status="POLICY_RULE",
            reason="Group 31 ruled out hidden pockets but did not derive full no-double-counting theorem",
        ),
        MinimalityRule(
            name="M4: overstrong additions remain outside ordinary minimality",
            rule="P_incidence_zero and P_residual_kill cannot be counted as ordinary minimal requirements",
            status="POLICY_RULE",
            reason="incidence and residual kill are high-risk or not-ready downstream content",
        ),
        MinimalityRule(
            name="M5: downstream gates remain closed",
            rule="minimality accounting cannot license active O, insertion, residual control, or parent closure",
            status="POLICY_RULE",
            reason="package minimality is not downstream theorem closure",
        ),
    ]


def build_obligations() -> List[MinimalityObligation]:
    return [
        MinimalityObligation(
            name="O1: retain no-adoption boundary",
            obligation="record Package B as minimal plausible-to-audit only, not adopted or recommended",
            status="OPEN",
            blocks="adoption drift",
            discipline="minimality accounting is not explicit choice",
        ),
        MinimalityObligation(
            name="O2: preserve removal-test limits",
            obligation="state that each removal test is criterion-based rather than physical proof of the component",
            status="OPEN",
            blocks="theorem overclaim",
            discipline="necessary-for-audit is not derived-as-physics",
        ),
        MinimalityObligation(
            name="O3: carry inherited discipline boundary",
            obligation="keep P_source_no_hidden as inherited discipline unless explicitly restated",
            status="OPEN",
            blocks="false fresh-postulate accounting",
            discipline="partial constraint is not full source theorem",
        ),
        MinimalityObligation(
            name="O4: keep overstrong package separate",
            obligation="keep Package C outside ordinary minimality and record it only as high-risk strong package/theorem target",
            status="OPEN",
            blocks="incidence/residual-control smuggling",
            discipline="high-risk additions are not ordinary requirements",
        ),
        MinimalityObligation(
            name="O5: adoption decision remains separate",
            obligation="handoff to explicit adoption-boundary or status-summary script without adopting Package B",
            status="OPEN",
            blocks="premature adoption",
            discipline="a later explicit user/theory decision is required for adoption",
        ),
        MinimalityObligation(
            name="O6: downstream gates remain closed",
            obligation="keep insertion, active O, residual control, and parent closure closed after minimality accounting",
            status="NOT_READY",
            blocks="downstream overreach",
            discipline="minimality accounting is not insertion or parent closure",
        ),
    ]


def build_conclusions() -> List[MinimalityConclusion]:
    return [
        MinimalityConclusion(
            name="C1: Package B minimality accounting",
            conclusion="Package B is minimal plausible-to-audit under the current trace-anchor criteria",
            status="MINIMAL_PLAUSIBLE_TO_AUDIT",
            meaning="removing any listed component breaks either trace-anchor completeness or required audit discipline",
        ),
        MinimalityConclusion(
            name="C2: no adoption",
            conclusion="this script adopts no postulate and recommends no adoption",
            status="NOT_ADOPTED",
            meaning="minimal plausible-to-audit is not explicit theory choice",
        ),
        MinimalityConclusion(
            name="C3: insufficient packages remain insufficient",
            conclusion="Packages A, E, and F remain insufficient for trace-anchor audit",
            status="INSUFFICIENT",
            meaning="they are missing one or both fresh trace-anchor candidates",
        ),
        MinimalityConclusion(
            name="C4: overstrong packages remain outside ordinary minimality",
            conclusion="Package C and downstream shortcut packages remain high-risk/not-ready/current shortcut exclusions",
            status="NOT_READY",
            meaning="incidence, residual kill, active O, insertion, and parent closure remain outside ordinary minimality",
        ),
        MinimalityConclusion(
            name="C5: next",
            conclusion="adoption boundary / Group 32 status summary should run next",
            status="OPEN",
            meaning="minimality accounting is complete enough to summarize without adopting",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Package minimality problem")
    print("Question:")
    print()
    print("  Under the currently declared trace-anchor audit criteria, is Package B")
    print("  minimal plausible-to-audit, or does it carry removable, missing, or")
    print("  overstrong load?")
    print()
    print("Discipline:")
    print()
    print("  This script performs minimality accounting.")
    print("  It adopts no postulate.")
    print("  It recommends no adoption.")
    print("  It does not select Package B.")
    print("  It derives no coefficient law and no insertion.")
    print("  It keeps active O, residual control, and parent closure closed.")
    print()
    print("Tiny goblin rule:")
    print("  Weigh each tooth. Still do not bite.")

    with out.governance_assessments():
        out.line(
            "package minimality accounting opened",
            StatusMark.INFO,
            "testing minimal plausible-to-audit status after package sieve; no adoption",
        )


def case_1_symbolic_loads(symbols: MinimalitySymbols, out: ScriptOutput) -> None:
    header("Case 1: Minimality symbolic loads")
    print("Candidate symbols:")
    print()
    for name in (
        "P_trace_norm",
        "P_safe_membership",
        "P_guardrail_visibility",
        "P_div_explicitness",
        "P_source_no_hidden",
        "P_incidence_zero",
        "P_active_O",
        "P_residual_kill",
        "P_insertion",
        "P_parent",
    ):
        print(f"  {name} = {getattr(symbols, name)}")

    print()
    print("Package B load:")
    print(f"  L_package_B = {symbols.L_package_B}")
    print()
    print("Required trace-anchor load:")
    print(f"  L_required_trace_anchor = {symbols.L_required_trace_anchor}")
    print()
    print("Required discipline load:")
    print(f"  L_required_discipline = {symbols.L_required_discipline}")
    print()
    print("Downstream forbidden load:")
    print(f"  L_downstream_forbidden = {symbols.L_downstream_forbidden}")
    print()
    print("Overstrong additions load:")
    print(f"  L_overstrong_additions = {symbols.L_overstrong_additions}")
    print()
    print("Minimality gap:")
    print(f"  L_minimality_gap = {symbols.L_minimality_gap}")

    with out.derived_results():
        out.line(
            "minimality symbolic loads stated",
            StatusMark.OBLIGATION,
            f"L_package_B = {symbols.L_package_B}; L_downstream_forbidden = {symbols.L_downstream_forbidden}",
        )


def case_2_removal_tests(tests: List[RemovalTest], out: ScriptOutput) -> None:
    header("Case 2: Package B removal tests")

    for item in tests:
        subheader(item.name)
        print(f"Removed: {item.removed}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Result: {item.result}")
        print(f"Why required: {item.why_required}")
        print(f"Forbidden upgrade: {item.forbidden_upgrade}")

    with out.governance_assessments():
        out.line(
            "Package B removal tests stated",
            StatusMark.OBLIGATION,
            f"{len(tests)} removal tests show criteria-based minimality; no adoption",
        )


def case_3_package_accounting(entries: List[PackageAccountingEntry], out: ScriptOutput) -> None:
    header("Case 3: Package minimality accounting")

    for item in entries:
        subheader(item.name)
        print(f"Package: {item.package}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Minimality result: {item.minimality_result}")
        print(f"Reason: {item.reason}")
        print(f"Boundary: {item.boundary}")

    with out.governance_assessments():
        out.line(
            "package minimality accounting stated",
            StatusMark.DEFER,
            f"{len(entries)} package accounting entries stated; Package B not selected or adopted",
        )


def case_4_rules(rules: List[MinimalityRule], out: ScriptOutput) -> None:
    header("Case 4: Minimality no-overclaim rules")

    for item in rules:
        subheader(item.name)
        print(f"Rule: {item.rule}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Reason: {item.reason}")

    with out.governance_assessments():
        out.line(
            "minimality no-overclaim rules stated",
            StatusMark.OBLIGATION,
            f"{len(rules)} rules stated",
        )


def case_5_obligations(obligations: List[MinimalityObligation], out: ScriptOutput) -> None:
    header("Case 5: Minimality obligations")

    for item in obligations:
        subheader(item.name)
        print(f"Obligation: {item.obligation}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Blocks: {item.blocks}")
        print(f"Discipline: {item.discipline}")

    with out.unresolved_obligations():
        out.line(
            "minimality obligations opened",
            StatusMark.OBLIGATION,
            f"{len(obligations)} obligations stated",
        )


def case_6_conclusions(conclusions: List[MinimalityConclusion], out: ScriptOutput) -> None:
    header("Case 6: Minimality conclusions")

    for item in conclusions:
        subheader(item.name)
        print(f"Conclusion: {item.conclusion}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Meaning: {item.meaning}")

    with out.governance_assessments():
        out.line(
            "minimality accounting conclusion stated",
            StatusMark.PASS,
            "Package B minimal plausible-to-audit under current criteria; no postulate adopted; adoption boundary remains separate",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Package minimality accounting result:")
    print()
    print("  Package B is minimal plausible-to-audit under the current trace-anchor criteria.")
    print("  This means each listed component is required for the current audit role.")
    print("  It does not mean any component has been derived as physics.")
    print("  It does not mean Package B is selected, adopted, or recommended for adoption.")
    print("  Packages A, E, and F remain insufficient for trace-anchor audit.")
    print("  Package C remains high-risk/overstrong.")
    print("  Package D remains rejected as a current downstream shortcut.")
    print("  Active O, residual kill, B_s/F_zeta insertion, and parent closure remain not ready.")
    print("  No postulate is adopted by this minimality accounting.")
    print()
    print("Possible next script:")
    print("  candidate_group_32_status_summary.py")
    print()
    print("Tiny goblin label:")
    print("  Weigh each tooth. Still do not bite.")

    with out.governance_assessments():
        out.line(
            "candidate package minimality accounting complete",
            StatusMark.PASS,
            "Group 32 status summary or adoption-boundary record should run next; adoption remains separate",
        )


def record_inventory_marker(ns, symbols: MinimalitySymbols) -> None:
    ns.record_derivation(
        derivation_id="g32_postulate_package_minimality",
        inputs=[
            symbols.P_trace_norm,
            symbols.P_safe_membership,
            symbols.P_guardrail_visibility,
            symbols.P_div_explicitness,
            symbols.P_source_no_hidden,
            symbols.P_incidence_zero,
            symbols.P_active_O,
            symbols.P_residual_kill,
            symbols.P_insertion,
            symbols.P_parent,
        ],
        output=symbols.L_minimality_gap,
        method="minimality accounting for Group 32 package families; Package B removal tests under current trace-anchor audit criteria",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="postulate_package_minimality_marker",
        scope="Group 32 explicit minimal postulate selection",
        is_placeholder=True,
    )


def record_obligations(ns, obligations: List[MinimalityObligation]) -> None:
    obligation_id_map = {
        "O1: retain no-adoption boundary": "g32_minimality_no_adoption_boundary",
        "O2: preserve removal-test limits": "g32_minimality_removal_test_limits",
        "O3: carry inherited discipline boundary": "g32_minimality_inherited_discipline_boundary",
        "O4: keep overstrong package separate": "g32_minimality_overstrong_package_separate",
        "O5: adoption decision remains separate": "g32_minimality_adoption_decision_separate",
        "O6: downstream gates remain closed": "g32_minimality_downstream_gates_closed",
    }

    for item in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id_map[item.name],
            script_id=SCRIPT_ID,
            title=item.obligation,
            status=ObligationStatus.OPEN,
            required_by=["g32_postulate_package_minimality"],
            description=f"{item.discipline} Blocks: {item.blocks}.",
        ))


def record_governance(
    ns,
    removal_tests: List[RemovalTest],
    package_entries: List[PackageAccountingEntry],
    rules: List[MinimalityRule],
) -> None:
    obligation_ids = [
        "g32_minimality_no_adoption_boundary",
        "g32_minimality_removal_test_limits",
        "g32_minimality_inherited_discipline_boundary",
        "g32_minimality_overstrong_package_separate",
        "g32_minimality_adoption_decision_separate",
        "g32_minimality_downstream_gates_closed",
    ]

    ns.record_route(RouteRecord(
        route_id="g32_postulate_package_minimality_route",
        script_id=SCRIPT_ID,
        name="Group 32 postulate package minimality accounting route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "package sieve completed",
            "dependency graph completed",
            "minimality accounting remains separate from adoption",
            "downstream gates remain closed",
        ],
    ))

    for item in removal_tests:
        ns.record_claim(ClaimRecord(
            claim_id=f"g32_removal_test_{item.name.split(':')[0].lower()}",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.POLICY_RULE,
            statement=(
                f"{item.name}: removing {item.removed} breaks the current audit criteria. "
                f"Result: {item.result}. Forbidden upgrade: {item.forbidden_upgrade}."
            ),
            derivation_ids=["g32_postulate_package_minimality"],
            obligation_ids=obligation_ids,
        ))

    for item in package_entries:
        status = GovernanceStatus.CANDIDATE_ROUTE
        if item.status in {"INSUFFICIENT", "OVERSTRONG"}:
            status = GovernanceStatus.DEFERRED_PENDING_PREREQUISITES
        elif item.status == "REJECTED_AS_CURRENT_SHORTCUT":
            status = GovernanceStatus.POLICY_RULE

        ns.record_claim(ClaimRecord(
            claim_id=f"g32_minimality_package_{item.name.split(':')[0].lower()}",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=status,
            statement=(
                f"{item.name}: {item.minimality_result}. Reason: {item.reason}. "
                f"Boundary: {item.boundary}."
            ),
            derivation_ids=["g32_postulate_package_minimality"],
            obligation_ids=obligation_ids,
        ))

    for item in rules:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"g32_minimality_rule_{item.name.split(':')[0].lower()}",
            script_id=SCRIPT_ID,
            branch_id=item.rule,
            status=GovernanceStatus.POLICY_RULE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"{item.rule}. Reason: {item.reason}.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g32_postulate_package_minimality_complete",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Group 32 package minimality accounting is complete. Package B is minimal plausible-to-audit under the current trace-anchor criteria, "
            "but is not selected, adopted, or recommended for adoption. Removal tests are audit-criteria tests, not physical derivations. "
            "Downstream gates remain closed."
        ),
        derivation_ids=["g32_postulate_package_minimality"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Postulate Package Minimality")
    archive, ns, invalidated = prepare_archive()
    ensure_archive_write_dirs(ns)
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    removal_tests = build_removal_tests()
    package_entries = build_package_accounting()
    rules = build_rules()
    obligations = build_obligations()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_symbolic_loads(symbols, out)
    case_2_removal_tests(removal_tests, out)
    case_3_package_accounting(package_entries, out)
    case_4_rules(rules, out)
    case_5_obligations(obligations, out)
    case_6_conclusions(conclusions, out)
    final_interpretation(out)

    record_inventory_marker(ns, symbols)
    record_obligations(ns, obligations)
    record_governance(ns, removal_tests, package_entries, rules)

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
