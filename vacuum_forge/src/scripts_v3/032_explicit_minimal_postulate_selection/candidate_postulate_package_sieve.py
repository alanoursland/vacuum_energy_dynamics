# Candidate postulate package sieve
#
# Group:
#   32_explicit_minimal_postulate_selection
#
# Human title:
#   Explicit Minimal Postulate Selection
#
# Script type:
#   PACKAGE SIEVE / SUFFICIENCY-OVERREACH CLASSIFIER
#
# Purpose
# -------
# Classify Group 32 candidate postulate packages after the candidate ledger and
# dependency graph have separated fresh candidates, inherited discipline, and
# forbidden implication edges.
#
# Locked-door question:
#
#   Which candidate packages are insufficient, plausible-to-audit, overstrong,
#   or forbidden as current shortcut packages before any explicit adoption
#   decision is made?
#
# This script does not adopt a postulate.
# It does not recommend adoption.
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
#   Sift the teeth. Do not bite yet.

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
        "CANDIDATE_ROUTE": StatusMark.DEFER,
        "FORBIDDEN_CURRENT_SHORTCUT": StatusMark.FAIL,
        "GATE_CLOSED": StatusMark.DEFER,
        "HIGH_RISK_STRONG_PACKAGE": StatusMark.DEFER,
        "INSUFFICIENT": StatusMark.DEFER,
        "LEADING_PACKAGE_TO_AUDIT": StatusMark.INFO,
        "LIKELY_INSUFFICIENT": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "NOT_SELECTED": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "PLAUSIBLE_TO_AUDIT": StatusMark.INFO,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REJECTED_AS_CURRENT_MINIMAL_PACKAGE": StatusMark.FAIL,
        "REJECTED_AS_SHORTCUT": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g32_dependency_graph",
            "32_explicit_minimal_postulate_selection__candidate_postulate_dependency_graph",
            "g32_postulate_dependency_graph",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g32_candidate_ledger",
            "32_explicit_minimal_postulate_selection__candidate_postulate_candidate_ledger",
            "g32_candidate_postulate_ledger",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g32_problem",
            "32_explicit_minimal_postulate_selection__candidate_explicit_postulate_selection_problem",
            "g32_explicit_selection_problem",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_summary",
            "31_source_divergence_coefficient_law__candidate_group_31_status_summary",
            "g31_status_summary",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_obligations",
            "31_source_divergence_coefficient_law__candidate_source_divergence_obligations",
            "g31_obligations",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g30_summary",
            "30_minimal_coefficient_sector_postulate_inventory__candidate_group_30_status_summary",
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
class PackageSymbols:
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
    L_visibility_only: sp.Expr
    L_trace_anchor: sp.Expr
    L_too_strong: sp.Expr
    L_parent_closure: sp.Expr
    L_missing_trace_anchor: sp.Expr
    L_downstream_gate: sp.Expr
    L_sieve_gap: sp.Expr


@dataclass
class PackageEntry:
    name: str
    package: str
    status: str
    classification: str
    result: str
    passes: str
    fails: str
    forbidden_upgrade: str


@dataclass
class SieveTest:
    name: str
    test: str
    status: str
    result: str
    failure_mode: str


@dataclass
class SieveRule:
    name: str
    rule: str
    status: str
    reason: str


@dataclass
class SieveObligation:
    name: str
    obligation: str
    status: str
    blocks: str
    discipline: str


@dataclass
class SieveConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_symbols() -> PackageSymbols:
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

    L_visibility_only = sp.simplify(
        P_guardrail_visibility + P_div_explicitness + P_source_no_hidden
    )
    L_trace_anchor = sp.simplify(
        L_visibility_only + P_trace_norm + P_safe_membership
    )
    L_too_strong = sp.simplify(
        P_trace_norm + P_safe_membership + P_incidence_zero + P_residual_kill
    )
    L_parent_closure = sp.simplify(P_insertion + P_active_O + P_parent)
    L_missing_trace_anchor = sp.simplify(P_trace_norm + P_safe_membership)
    L_downstream_gate = sp.simplify(P_incidence_zero + P_active_O + P_residual_kill + P_insertion + P_parent)
    L_sieve_gap = sp.simplify(L_trace_anchor + L_downstream_gate)

    return PackageSymbols(
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
        L_visibility_only=L_visibility_only,
        L_trace_anchor=L_trace_anchor,
        L_too_strong=L_too_strong,
        L_parent_closure=L_parent_closure,
        L_missing_trace_anchor=L_missing_trace_anchor,
        L_downstream_gate=L_downstream_gate,
        L_sieve_gap=L_sieve_gap,
    )


def build_package_entries() -> List[PackageEntry]:
    return [
        PackageEntry(
            name="Package A: Visibility Only",
            package="P_guardrail_visibility + P_div_explicitness + P_source_no_hidden",
            status="LIKELY_INSUFFICIENT",
            classification="safe discipline package but incomplete trace anchor",
            result="keeps guardrails visible and non-reservoir but does not choose trace normalization or safe membership",
            passes="anti-hidden-pocket discipline and auditable correction discipline",
            fails="trace-anchor sufficiency because P_trace_norm and P_safe_membership are absent",
            forbidden_upgrade="must not be treated as trace normalization, membership, coefficient law, insertion, or parent readiness",
        ),
        PackageEntry(
            name="Package B: Trace Anchor",
            package="P_trace_norm + P_safe_membership + P_guardrail_visibility + P_div_explicitness + P_source_no_hidden",
            status="PLAUSIBLE_TO_AUDIT",
            classification="leading package to audit for minimal plausibility",
            result="contains the fresh trace-anchor candidates plus inherited/discipline guardrails",
            passes="candidate completeness for trace-anchor precondition audit",
            fails="does not derive the candidates and does not license downstream gates",
            forbidden_upgrade="not selected, not adopted, not insertion, not residual control, not active O, not parent closure",
        ),
        PackageEntry(
            name="Package C: Too-Strong No-Overlap",
            package="P_trace_norm + P_safe_membership + P_incidence_zero + P_residual_kill",
            status="HIGH_RISK_STRONG_PACKAGE",
            classification="overstrong warning package",
            result="adds incidence and residual kill to trace-anchor candidates",
            passes="shows what a stronger no-overlap-like package would try to include",
            fails="smuggles high-risk residual-control/no-overlap content into package testing",
            forbidden_upgrade="must not be accepted unless separately adopted as strong postulate with explicit warning or derived by theorem",
        ),
        PackageEntry(
            name="Package D: Parent Closure",
            package="P_insertion + P_active_O + P_parent",
            status="REJECTED_AS_CURRENT_MINIMAL_PACKAGE",
            classification="forbidden current shortcut package",
            result="tries to combine downstream gates rather than prepare prerequisites",
            passes="none for current minimal package role",
            fails="active O, insertion, and parent closure are not ready and not constructed",
            forbidden_upgrade="cannot be adopted as current minimal package; rejection is current-governance, not permanent mathematical no-go",
        ),
        PackageEntry(
            name="Package E: Trace Normalization Only",
            package="P_trace_norm + P_guardrail_visibility + P_div_explicitness + P_source_no_hidden",
            status="INSUFFICIENT",
            classification="normalization without membership",
            result="chooses or audits how B_s reads zeta but does not assign zeta_Bs to T_zeta",
            passes="normalization side of trace anchor is present",
            fails="safe trace membership remains absent",
            forbidden_upgrade="normalization must not become membership by implication",
        ),
        PackageEntry(
            name="Package F: Membership Only",
            package="P_safe_membership + P_guardrail_visibility + P_div_explicitness + P_source_no_hidden",
            status="INSUFFICIENT",
            classification="membership without normalization",
            result="assigns zeta_Bs to T_zeta but does not specify how B_s reads zeta",
            passes="membership side of trace anchor is present",
            fails="trace normalization remains absent",
            forbidden_upgrade="membership must not choose normalization or incidence by implication",
        ),
    ]


def build_sieve_tests() -> List[SieveTest]:
    return [
        SieveTest(
            name="T1: trace-anchor completeness",
            test="package contains both P_trace_norm and P_safe_membership",
            status="REQUIRED",
            result="required before a package can be called plausible for trace-anchor precondition audit",
            failure_mode="visibility-only, normalization-only, or membership-only package is insufficient",
        ),
        SieveTest(
            name="T2: inherited discipline visibility",
            test="package carries P_guardrail_visibility, P_div_explicitness, and inherited P_source_no_hidden discipline",
            status="REQUIRED",
            result="required for auditable package accounting",
            failure_mode="package hides source, correction, boundary, current, mass, or support loads",
        ),
        SieveTest(
            name="T3: no incidence smuggling",
            test="package does not include P_incidence_zero unless explicitly classified as high-risk strong package",
            status="REQUIRED",
            result="zero incidence remains separate from safe membership",
            failure_mode="membership becomes residual control/no-overlap by implication",
        ),
        SieveTest(
            name="T4: no residual-kill smuggling",
            test="package does not include P_residual_kill as a minimal-package consequence",
            status="REQUIRED",
            result="residual kill remains not ready or separate strong-postulate/theorem target",
            failure_mode="package kills residual trace by declaration",
        ),
        SieveTest(
            name="T5: no active-O smuggling",
            test="package does not include P_active_O or imply an active no-overlap operator",
            status="REQUIRED",
            result="active O remains construction target",
            failure_mode="operator is adopted by naming a package",
        ),
        SieveTest(
            name="T6: no insertion or parent closure",
            test="package does not include P_insertion or P_parent as consequence",
            status="REQUIRED",
            result="insertion and parent gates remain closed",
            failure_mode="package testing becomes downstream closure",
        ),
    ]


def build_sieve_rules() -> List[SieveRule]:
    return [
        SieveRule(
            name="R1: plausible to audit is not selected",
            rule="Package B may be classified as leading package to audit without being selected",
            status="POLICY_RULE",
            reason="sieve classification is not adoption or recommendation for adoption",
        ),
        SieveRule(
            name="R2: insufficient is not impossible forever",
            rule="Package A/E/F insufficiency means insufficient for current trace-anchor audit, not permanently useless",
            status="POLICY_RULE",
            reason="a discipline package may still be useful even if it does not choose the trace anchor",
        ),
        SieveRule(
            name="R3: high-risk is not ordinary minimal",
            rule="Package C may be studied only as high-risk strong package or theorem target, not normal minimal package",
            status="POLICY_RULE",
            reason="incidence and residual kill are too close to no-overlap/residual-control smuggling",
        ),
        SieveRule(
            name="R4: rejected current shortcut is not permanent no-go theorem",
            rule="Package D is rejected as current minimal package, not proved mathematically impossible forever",
            status="POLICY_RULE",
            reason="active O, insertion, and parent closure may become future theorem/construction targets after prerequisites",
        ),
        SieveRule(
            name="R5: sieve is not minimality proof",
            rule="package sieve classifies packages before a later minimality accounting script",
            status="POLICY_RULE",
            reason="sufficiency/overreach classification precedes minimality and adoption decisions",
        ),
    ]


def build_obligations() -> List[SieveObligation]:
    return [
        SieveObligation(
            name="O1: package B audit boundary",
            obligation="audit Package B for minimal plausibility without selecting or adopting it",
            status="OPEN",
            blocks="package recommendation and adoption boundary",
            discipline="plausible to audit is not selected",
        ),
        SieveObligation(
            name="O2: package insufficiency record",
            obligation="record why visibility-only, normalization-only, and membership-only packages are insufficient for trace-anchor audit",
            status="OPEN",
            blocks="minimality accounting",
            discipline="insufficient for trace anchor does not mean useless forever",
        ),
        SieveObligation(
            name="O3: high-risk package fence",
            obligation="keep Package C as high-risk strong package or theorem target, not ordinary minimal package",
            status="OPEN",
            blocks="overstrength control",
            discipline="incidence and residual kill are not hidden inside safe membership",
        ),
        SieveObligation(
            name="O4: downstream shortcut exclusion",
            obligation="keep active O, insertion, residual control, and parent closure outside current package consequences",
            status="NOT_READY",
            blocks="downstream overreach",
            discipline="package sieve is not insertion or parent closure",
        ),
        SieveObligation(
            name="O5: next minimality accounting",
            obligation="run explicit package minimality accounting after sieve classification",
            status="OPEN",
            blocks="minimal package recommendation",
            discipline="minimality test remains separate from adoption",
        ),
    ]


def build_conclusions() -> List[SieveConclusion]:
    return [
        SieveConclusion(
            name="C1: visibility-only package classified",
            conclusion="Package A is safe discipline but likely insufficient for trace-anchor package role",
            status="LIKELY_INSUFFICIENT",
            meaning="it lacks trace normalization and safe membership",
        ),
        SieveConclusion(
            name="C2: trace-anchor package classified",
            conclusion="Package B is the leading package to audit for minimal plausibility",
            status="PLAUSIBLE_TO_AUDIT",
            meaning="it is not selected, not adopted, and does not license downstream gates",
        ),
        SieveConclusion(
            name="C3: too-strong package classified",
            conclusion="Package C is high-risk because it adds incidence and residual kill",
            status="HIGH_RISK_STRONG_PACKAGE",
            meaning="it must not be treated as ordinary minimal package",
        ),
        SieveConclusion(
            name="C4: parent-closure shortcut classified",
            conclusion="Package D is rejected as current minimal package shortcut",
            status="REJECTED_AS_CURRENT_MINIMAL_PACKAGE",
            meaning="active O, insertion, and parent closure are not ready now; this is not permanent no-go theorem",
        ),
        SieveConclusion(
            name="C5: no adoption",
            conclusion="this sieve adopts no postulate and recommends no adoption",
            status="NOT_ADOPTED",
            meaning="package classification is not explicit theory choice",
        ),
        SieveConclusion(
            name="C6: next",
            conclusion="package minimality accounting should run next",
            status="OPEN",
            meaning="sieve classification enables minimality tests, but adoption remains separate",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Candidate package sieve problem")
    print("Question:")
    print()
    print("  Which candidate packages are insufficient, plausible-to-audit, overstrong,")
    print("  or forbidden as current shortcut packages before any explicit adoption")
    print("  decision is made?")
    print()
    print("Discipline:")
    print()
    print("  This script classifies packages.")
    print("  It adopts no postulate.")
    print("  It recommends no adoption.")
    print("  It derives no coefficient law and no insertion.")
    print("  It keeps active O, residual control, and parent closure closed.")
    print()
    print("Tiny goblin rule:")
    print("  Sift the teeth. Do not bite yet.")

    with out.governance_assessments():
        out.line(
            "candidate package sieve opened",
            StatusMark.INFO,
            "classifying packages after dependency graph and before minimality/adoption tests",
        )


def case_1_symbolic_packages(symbols: PackageSymbols, out: ScriptOutput) -> None:
    header("Case 1: Package sieve symbolic loads")
    print("Candidate symbols:")
    print()
    for item in (
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
    ):
        print(f"  {item} = {item}")

    print()
    print("Visibility-only package load:")
    print(f"  L_visibility_only = {symbols.L_visibility_only}")
    print()
    print("Trace-anchor package load:")
    print(f"  L_trace_anchor = {symbols.L_trace_anchor}")
    print()
    print("Too-strong package load:")
    print(f"  L_too_strong = {symbols.L_too_strong}")
    print()
    print("Parent-closure shortcut load:")
    print(f"  L_parent_closure = {symbols.L_parent_closure}")
    print()
    print("Missing trace-anchor load:")
    print(f"  L_missing_trace_anchor = {symbols.L_missing_trace_anchor}")
    print()
    print("Downstream gate load:")
    print(f"  L_downstream_gate = {symbols.L_downstream_gate}")
    print()
    print("Sieve gap:")
    print(f"  L_sieve_gap = {symbols.L_sieve_gap}")

    with out.derived_results():
        out.line(
            "package sieve symbolic loads stated",
            StatusMark.OBLIGATION,
            f"L_trace_anchor = {symbols.L_trace_anchor}; L_downstream_gate = {symbols.L_downstream_gate}",
        )


def case_2_package_entries(packages: List[PackageEntry], out: ScriptOutput) -> None:
    header("Case 2: Candidate package family sieve")

    for item in packages:
        subheader(item.name)
        print(f"Package: {item.package}")
        print(f"Classification: {item.classification}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Result: {item.result}")
        print(f"Passes: {item.passes}")
        print(f"Fails: {item.fails}")
        print(f"Forbidden upgrade: {item.forbidden_upgrade}")

    with out.governance_assessments():
        out.line(
            "candidate package families classified",
            StatusMark.DEFER,
            f"{len(packages)} package families classified; none selected or adopted",
        )


def case_3_sieve_tests(tests: List[SieveTest], out: ScriptOutput) -> None:
    header("Case 3: Package sieve tests")

    for item in tests:
        subheader(item.name)
        print(f"Test: {item.test}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Result: {item.result}")
        print(f"Failure mode: {item.failure_mode}")

    with out.governance_assessments():
        out.line(
            "package sieve tests stated",
            StatusMark.OBLIGATION,
            f"{len(tests)} tests stated before minimality accounting",
        )


def case_4_sieve_rules(rules: List[SieveRule], out: ScriptOutput) -> None:
    header("Case 4: Sieve no-overclaim rules")

    for item in rules:
        subheader(item.name)
        print(f"Rule: {item.rule}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Reason: {item.reason}")

    with out.governance_assessments():
        out.line(
            "package-sieve no-overclaim rules stated",
            StatusMark.OBLIGATION,
            f"{len(rules)} rules stated",
        )


def case_5_obligations(obligations: List[SieveObligation], out: ScriptOutput) -> None:
    header("Case 5: Package-sieve obligations")

    for item in obligations:
        subheader(item.name)
        print(f"Obligation: {item.obligation}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Blocks: {item.blocks}")
        print(f"Discipline: {item.discipline}")

    with out.unresolved_obligations():
        out.line(
            "package-sieve obligations opened",
            StatusMark.OBLIGATION,
            f"{len(obligations)} obligations stated",
        )


def case_6_conclusions(conclusions: List[SieveConclusion], out: ScriptOutput) -> None:
    header("Case 6: Package-sieve conclusions")

    for item in conclusions:
        subheader(item.name)
        print(f"Conclusion: {item.conclusion}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Meaning: {item.meaning}")

    with out.governance_assessments():
        out.line(
            "package sieve conclusion stated",
            StatusMark.PASS,
            "Package B plausible to audit; no package selected or adopted; package minimality accounting should run next",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Candidate package sieve result:")
    print()
    print("  Package A is safe discipline but likely insufficient for trace-anchor audit.")
    print("  Package B is the leading package to audit for minimal plausibility.")
    print("  Package B is not selected, not adopted, and not recommended for adoption.")
    print("  Package C is high-risk because it includes incidence and residual kill.")
    print("  Package D is rejected as a current minimal-package shortcut, not as permanent no-go theorem.")
    print("  Normalization-only and membership-only packages are insufficient for trace-anchor audit.")
    print("  Active O, residual kill, B_s/F_zeta insertion, and parent closure remain not ready.")
    print("  No postulate is adopted by this sieve.")
    print()
    print("Possible next script:")
    print("  candidate_postulate_package_minimality.py")
    print()
    print("Tiny goblin label:")
    print("  Sift the teeth. Do not bite yet.")

    with out.governance_assessments():
        out.line(
            "candidate package sieve complete",
            StatusMark.PASS,
            "package minimality accounting should run next; adoption remains separate",
        )


def record_inventory_marker(ns, symbols: PackageSymbols) -> None:
    ns.record_derivation(
        derivation_id="g32_postulate_package_sieve",
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
        output=symbols.L_sieve_gap,
        method="classify candidate packages as insufficient, plausible-to-audit, overstrong, or forbidden current shortcuts without adoption",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="postulate_package_sieve_marker",
        scope="Group 32 explicit minimal postulate selection",
        is_placeholder=True,
    )


def record_obligations(ns, obligations: List[SieveObligation]) -> None:
    obligation_id_map = {
        "O1: package B audit boundary": "g32_package_b_audit_boundary",
        "O2: package insufficiency record": "g32_package_insufficiency_record",
        "O3: high-risk package fence": "g32_high_risk_package_fence",
        "O4: downstream shortcut exclusion": "g32_downstream_shortcut_exclusion",
        "O5: next minimality accounting": "g32_next_minimality_accounting",
    }

    for item in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id_map[item.name],
            script_id=SCRIPT_ID,
            title=item.obligation,
            status=ObligationStatus.OPEN,
            required_by=["g32_postulate_package_sieve"],
            description=f"{item.discipline} Blocks: {item.blocks}.",
        ))


def record_governance(
    ns,
    packages: List[PackageEntry],
    tests: List[SieveTest],
    rules: List[SieveRule],
) -> None:
    obligation_ids = [
        "g32_package_b_audit_boundary",
        "g32_package_insufficiency_record",
        "g32_high_risk_package_fence",
        "g32_downstream_shortcut_exclusion",
        "g32_next_minimality_accounting",
    ]

    ns.record_route(RouteRecord(
        route_id="g32_postulate_package_sieve_route",
        script_id=SCRIPT_ID,
        name="Group 32 postulate package sieve route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "candidate postulate ledger completed",
            "dependency graph completed",
            "package sieve classifies packages before minimality or adoption",
            "no postulate adoption is performed by package sieve",
        ],
    ))

    for item in packages:
        status = GovernanceStatus.CANDIDATE_ROUTE
        if item.status in {"HIGH_RISK_STRONG_PACKAGE", "REJECTED_AS_CURRENT_MINIMAL_PACKAGE"}:
            status = GovernanceStatus.POLICY_RULE
        elif item.status in {"INSUFFICIENT", "LIKELY_INSUFFICIENT"}:
            status = GovernanceStatus.DEFERRED_PENDING_PREREQUISITES

        ns.record_claim(ClaimRecord(
            claim_id=f"g32_package_{item.name.split(':')[0].lower().replace(' ', '_')}",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=status,
            statement=(
                f"{item.name}: {item.classification}. Result: {item.result}. "
                f"Fails: {item.fails}. Forbidden upgrade: {item.forbidden_upgrade}."
            ),
            derivation_ids=["g32_postulate_package_sieve"],
            obligation_ids=obligation_ids,
        ))

    for item in tests:
        ns.record_claim(ClaimRecord(
            claim_id=f"g32_sieve_test_{item.name.split(':')[0].lower()}",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.POLICY_RULE,
            statement=f"{item.name}: {item.test}. Result: {item.result}. Failure mode: {item.failure_mode}.",
            derivation_ids=["g32_postulate_package_sieve"],
            obligation_ids=obligation_ids,
        ))

    for item in rules:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"g32_sieve_rule_{item.name.split(':')[0].lower()}",
            script_id=SCRIPT_ID,
            branch_id=item.rule,
            status=GovernanceStatus.POLICY_RULE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"{item.rule}. Reason: {item.reason}.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g32_postulate_package_sieve_complete",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Group 32 postulate package sieve is complete. Package B is the leading package to audit for minimal plausibility, "
            "but it is not selected, adopted, or recommended for adoption. Visibility-only, normalization-only, and membership-only packages are insufficient for trace-anchor audit. "
            "Too-strong and parent-closure packages remain high-risk or forbidden as current shortcut packages. Insertion, active O, residual control, and parent closure remain closed."
        ),
        derivation_ids=["g32_postulate_package_sieve"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Postulate Package Sieve")
    archive, ns, invalidated = prepare_archive()
    ensure_archive_write_dirs(ns)
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    packages = build_package_entries()
    tests = build_sieve_tests()
    rules = build_sieve_rules()
    obligations = build_obligations()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_symbolic_packages(symbols, out)
    case_2_package_entries(packages, out)
    case_3_sieve_tests(tests, out)
    case_4_sieve_rules(rules, out)
    case_5_obligations(obligations, out)
    case_6_conclusions(conclusions, out)
    final_interpretation(out)

    record_inventory_marker(ns, symbols)
    record_obligations(ns, obligations)
    record_governance(ns, packages, tests, rules)

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
