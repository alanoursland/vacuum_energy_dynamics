# Candidate trace-normalization selector rejection
#
# Group:
#   33_trace_normalization_candidate_origin
#
# Human title:
#   Trace Normalization Candidate Origin
#
# Script type:
#   SIEVE / SELECTOR-REJECTION FIREWALL
#
# Purpose
# -------
# Record and enforce the rejected selector routes for trace normalization before
# candidate normalization forms are compared.
#
# Locked-door question:
#
#   Which ways of choosing N_trace are forbidden selectors rather than legitimate
#   structural origins or compatibility tests?
#
# This script does not choose N_trace.
# It does not adopt a trace-normalization postulate.
# It does not derive a trace-normalization theorem.
# It does not derive B_s/F_zeta insertion.
# It does not open active O, residual control, or parent closure.
#
# Tiny goblin rule:
#
#   Break the false cups before pouring anything.

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
        "ADMISSIBLE_FILTER_ONLY": StatusMark.INFO,
        "COMPATIBILITY_ONLY": StatusMark.INFO,
        "DEFERRED": StatusMark.DEFER,
        "FORBIDDEN_SELECTOR": StatusMark.FAIL,
        "GATE_CLOSED": StatusMark.DEFER,
        "NEGATIVE_FILTER_ONLY": StatusMark.INFO,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REJECTED_AS_SELECTOR": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g33_volume_trace",
            "033_trace_normalization_candidate_origin__candidate_trace_normalization_volume_trace_ledger",
            "g33_trace_normalization_volume_trace_ledger",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g33_origin_problem",
            "033_trace_normalization_candidate_origin__candidate_trace_normalization_origin_problem",
            "g33_trace_normalization_origin_problem",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g32_summary",
            "032_explicit_minimal_postulate_selection__candidate_group_32_status_summary",
            "g32_status_summary",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g32_minimality",
            "032_explicit_minimal_postulate_selection__candidate_postulate_package_minimality",
            "g32_postulate_package_minimality",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_trace_norm",
            "031_source_divergence_coefficient_law__candidate_trace_normalization_from_source_divergence",
            "g31_trace_normalization_fork",
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
class SelectorSymbols:
    N_trace: sp.Symbol
    S_recovery: sp.Symbol
    S_repair: sp.Symbol
    S_hidden_source: sp.Symbol
    S_insertion: sp.Symbol
    S_active_O: sp.Symbol
    S_parent: sp.Symbol
    S_divergence_safety: sp.Symbol
    S_membership: sp.Symbol
    S_compatibility: sp.Symbol
    F_negative_filter: sp.Expr
    F_forbidden_selector: sp.Expr
    F_compatibility_only: sp.Expr
    F_selector_firewall_gap: sp.Expr


@dataclass
class RejectedSelector:
    name: str
    selector: str
    status: str
    reason: str
    allowed_future_use: str
    failure_mode: str


@dataclass
class CompatibilityFilter:
    name: str
    filter: str
    status: str
    allowed_use: str
    forbidden_use: str
    consequence: str


@dataclass
class FirewallRule:
    name: str
    rule: str
    status: str
    reason: str


@dataclass
class SelectorObligation:
    name: str
    obligation: str
    status: str
    blocks: str
    discipline: str


@dataclass
class SelectorConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_symbols() -> SelectorSymbols:
    (
        N_trace,
        S_recovery,
        S_repair,
        S_hidden_source,
        S_insertion,
        S_active_O,
        S_parent,
        S_divergence_safety,
        S_membership,
        S_compatibility,
    ) = sp.symbols(
        "N_trace S_recovery S_repair S_hidden_source S_insertion S_active_O "
        "S_parent S_divergence_safety S_membership S_compatibility",
        real=True,
    )

    F_negative_filter = sp.simplify(S_repair + S_hidden_source + S_compatibility)
    F_forbidden_selector = sp.simplify(
        S_recovery + S_repair + S_hidden_source + S_insertion + S_active_O + S_parent
    )
    F_compatibility_only = sp.simplify(
        S_hidden_source + S_divergence_safety + S_membership + S_compatibility
    )
    F_selector_firewall_gap = sp.simplify(
        N_trace + F_forbidden_selector + F_compatibility_only
    )

    return SelectorSymbols(
        N_trace=N_trace,
        S_recovery=S_recovery,
        S_repair=S_repair,
        S_hidden_source=S_hidden_source,
        S_insertion=S_insertion,
        S_active_O=S_active_O,
        S_parent=S_parent,
        S_divergence_safety=S_divergence_safety,
        S_membership=S_membership,
        S_compatibility=S_compatibility,
        F_negative_filter=F_negative_filter,
        F_forbidden_selector=F_forbidden_selector,
        F_compatibility_only=F_compatibility_only,
        F_selector_firewall_gap=F_selector_firewall_gap,
    )


def build_rejected_selectors() -> List[RejectedSelector]:
    return [
        RejectedSelector(
            name="S1: recovery selector",
            selector="choose N_trace because AB=1, B=1/A, Schwarzschild, weak-field, gamma/PPN, or kappa=0 works",
            status="REJECTED_AS_SELECTOR",
            reason="recovery may audit after construction but cannot choose trace normalization",
            allowed_future_use="post-construction recovery check only",
            failure_mode="target success becomes construction rule",
        ),
        RejectedSelector(
            name="S2: repair selector",
            selector="choose N_trace because it repairs source, divergence, boundary, residual, coefficient, or matching failure",
            status="REJECTED_AS_SELECTOR",
            reason="failure may reject bad candidate forms but cannot select the good one",
            allowed_future_use="negative filter only",
            failure_mode="normalization becomes a patch for an unresolved theorem",
        ),
        RejectedSelector(
            name="S3: hidden-source selector",
            selector="choose N_trace to hide, cancel, or reroute ordinary source load",
            status="REJECTED_AS_SELECTOR",
            reason="ordinary source load must remain visible and may not pick the trace normalization",
            allowed_future_use="source-neutral compatibility test only",
            failure_mode="coefficient/source double-counting returns as normalization choice",
        ),
        RejectedSelector(
            name="S4: insertion selector",
            selector="choose N_trace because it makes B_s/F_zeta insertion work",
            status="REJECTED_AS_SELECTOR",
            reason="insertion is downstream and not ready",
            allowed_future_use="conditional precondition audit only after adoption or theorem support",
            failure_mode="candidate form becomes metric insertion by target fit",
        ),
        RejectedSelector(
            name="S5: active-O selector",
            selector="choose N_trace because it makes no-overlap operator O easier to state",
            status="REJECTED_AS_SELECTOR",
            reason="active O is not constructed and cannot select upstream normalization",
            allowed_future_use="future compatibility check only after O is constructed",
            failure_mode="undefined operator back-selects normalization",
        ),
        RejectedSelector(
            name="S6: parent-fit selector",
            selector="choose N_trace because it helps close the parent equation",
            status="REJECTED_AS_SELECTOR",
            reason="parent field equation is not ready and cannot choose trace normalization",
            allowed_future_use="future parent audit only after upstream gates close",
            failure_mode="parent closure pressure selects upstream trace convention",
        ),
        RejectedSelector(
            name="S7: membership selector",
            selector="choose N_trace because it makes zeta_Bs -> T_zeta membership easy or automatic",
            status="REJECTED_AS_SELECTOR",
            reason="safe membership is a separate candidate node and cannot choose normalization",
            allowed_future_use="compatibility check between separately declared candidates",
            failure_mode="Package B collapses normalization and membership into one choice",
        ),
        RejectedSelector(
            name="S8: divergence-safety selector",
            selector="choose N_trace because it appears to make divergence-safe coefficient behavior easier",
            status="REJECTED_AS_SELECTOR",
            reason="divergence explicitness and divergence safety are not trace-normalization theorems",
            allowed_future_use="compatibility check after candidate forms are visible",
            failure_mode="divergence theorem burden is hidden inside normalization",
        ),
    ]


def build_filters() -> List[CompatibilityFilter]:
    return [
        CompatibilityFilter(
            name="F1: source-neutral negative filter",
            filter="candidate form may be rejected if it hides or duplicates ordinary source load",
            status="ADMISSIBLE_FILTER_ONLY",
            allowed_use="reject candidate forms that violate inherited no-hidden-source discipline",
            forbidden_use="must not select a candidate merely because it avoids one source failure",
            consequence="source discipline filters candidates but does not derive N_trace",
        ),
        CompatibilityFilter(
            name="F2: divergence explicitness negative filter",
            filter="candidate form may be rejected if it requires hidden correction/divergence reservoirs",
            status="ADMISSIBLE_FILTER_ONLY",
            allowed_use="reject candidate forms incompatible with visible non-reservoir correction behavior",
            forbidden_use="must not select a candidate as divergence-safe coefficient law",
            consequence="explicitness filters candidates but does not derive divergence safety or N_trace",
        ),
        CompatibilityFilter(
            name="F3: safe-membership compatibility filter",
            filter="candidate form may be tested for coexistence with zeta_Bs -> T_zeta membership",
            status="COMPATIBILITY_ONLY",
            allowed_use="test whether normalization and membership can coexist as separate candidate nodes",
            forbidden_use="membership must not choose normalization, incidence, residual kill, or active O",
            consequence="compatibility does not collapse Package B into one postulate",
        ),
        CompatibilityFilter(
            name="F4: linearized consistency filter",
            filter="candidate form may be checked against first-order trace bookkeeping",
            status="COMPATIBILITY_ONLY",
            allowed_use="reject forms that fail declared linearized scope",
            forbidden_use="linearized success must not become exact theorem or insertion",
            consequence="first-order consistency is not exact trace-normalization theorem",
        ),
    ]


def build_rules() -> List[FirewallRule]:
    return [
        FirewallRule(
            name="R1: selector rejection is not derivation",
            rule="rejecting bad selectors does not derive the correct normalization",
            status="POLICY_RULE",
            reason="negative filter is weaker than theorem support",
        ),
        FirewallRule(
            name="R2: compatibility is not selection",
            rule="source/divergence/membership compatibility may reject candidates but cannot choose one",
            status="POLICY_RULE",
            reason="compatibility checks are downstream filters, not origin derivations",
        ),
        FirewallRule(
            name="R3: recovery remains audit only",
            rule="AB=1, Schwarzschild, gamma/PPN, weak-field, and kappa=0 may audit only after construction",
            status="POLICY_RULE",
            reason="recovery-selected normalization is forbidden",
        ),
        FirewallRule(
            name="R4: downstream gates cannot back-select",
            rule="insertion, active O, residual control, and parent closure cannot choose N_trace",
            status="POLICY_RULE",
            reason="downstream gates remain not ready",
        ),
        FirewallRule(
            name="R5: candidate forms must be visible before filtering",
            rule="candidate normalization forms must be stated before compatibility filters are applied",
            status="REQUIRED",
            reason="normalization must not hide in prose or failed candidate elimination",
        ),
    ]


def build_obligations() -> List[SelectorObligation]:
    return [
        SelectorObligation(
            name="O1: selector firewall",
            obligation="record recovery, repair, hidden-source, insertion, active-O, parent-fit, membership, and divergence-safety selectors as forbidden",
            status="OPEN",
            blocks="normalization drift",
            discipline="bad selector may reject or audit but not choose N_trace",
        ),
        SelectorObligation(
            name="O2: negative filter boundary",
            obligation="separate negative filters from structural origin routes",
            status="OPEN",
            blocks="theorem overclaim",
            discipline="candidate rejection is not candidate derivation",
        ),
        SelectorObligation(
            name="O3: candidate forms visible next",
            obligation="define scale-factor, metric-coefficient, per-dimension, and linearized candidate forms before compatibility sieve",
            status="OPEN",
            blocks="source/divergence/membership compatibility tests",
            discipline="forms first, filters second",
        ),
        SelectorObligation(
            name="O4: no adoption boundary",
            obligation="keep P_trace_norm unadopted unless separate explicit decision is requested",
            status="OPEN",
            blocks="accidental adoption",
            discipline="selector rejection is not postulate selection",
        ),
        SelectorObligation(
            name="O5: downstream gates",
            obligation="keep insertion, active O, residual control, and parent equation closed",
            status="NOT_READY",
            blocks="downstream overreach",
            discipline="selector firewall is not insertion or parent closure",
        ),
    ]


def build_conclusions() -> List[SelectorConclusion]:
    return [
        SelectorConclusion(
            name="C1: selector firewall complete",
            conclusion="forbidden selector routes are explicitly named and rejected",
            status="REQUIRED",
            meaning="trace normalization cannot be chosen from recovery, repair, hidden-source, insertion, active O, parent fit, membership convenience, or divergence-safety convenience",
        ),
        SelectorConclusion(
            name="C2: negative filters allowed only as filters",
            conclusion="source/divergence/membership compatibility can reject forms but cannot select N_trace",
            status="COMPATIBILITY_ONLY",
            meaning="compatibility remains weaker than derivation or adoption",
        ),
        SelectorConclusion(
            name="C3: no derivation",
            conclusion="this selector ledger derives no trace-normalization rule",
            status="NOT_DERIVED",
            meaning="rejected selectors do not determine the correct candidate",
        ),
        SelectorConclusion(
            name="C4: no adoption",
            conclusion="this selector ledger adopts no trace-normalization postulate",
            status="NOT_ADOPTED",
            meaning="explicit decision remains separate",
        ),
        SelectorConclusion(
            name="C5: downstream gates",
            conclusion="B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready",
            status="NOT_READY",
            meaning="selector firewall does not open downstream gates",
        ),
        SelectorConclusion(
            name="C6: next",
            conclusion="candidate trace-normalization forms should run next",
            status="OPEN",
            meaning="visible forms can now be compared without forbidden selectors",
        ),
    ]


def case_0_problem(out: ScriptOutput):
    header("Case 0: Trace-normalization selector-rejection problem")

    print("Question:")
    print()
    print("  Which ways of choosing N_trace are forbidden selectors rather than legitimate")
    print("  structural origins or compatibility tests?")
    print()
    print("Discipline:")
    print()
    print("  This script rejects selector shortcuts.")
    print("  It adopts no trace-normalization postulate.")
    print("  It derives no trace-normalization rule.")
    print("  It performs no candidate-form selection.")
    print("  It derives no coefficient law and no insertion.")
    print("  It keeps active O, residual control, and parent closure closed.")
    print()
    print("Tiny goblin rule:")
    print("  Break the false cups before pouring anything.")

    with out.governance_assessments():
        out.line(
            "trace-normalization selector firewall opened",
            StatusMark.INFO,
            "rejecting forbidden selectors before candidate-form comparison",
        )


def case_1_symbolic_loads(out: ScriptOutput, symbols: SelectorSymbols, ns=None):
    header("Case 1: Selector firewall symbolic loads")

    print("Selector / filter symbols:")
    for name in (
        "N_trace",
        "S_recovery",
        "S_repair",
        "S_hidden_source",
        "S_insertion",
        "S_active_O",
        "S_parent",
        "S_divergence_safety",
        "S_membership",
        "S_compatibility",
    ):
        print(f"\n  {name} = {getattr(symbols, name)}")

    print("\nNegative-filter load:")
    print(f"  F_negative_filter = {symbols.F_negative_filter}")
    print("\nForbidden-selector load:")
    print(f"  F_forbidden_selector = {symbols.F_forbidden_selector}")
    print("\nCompatibility-only load:")
    print(f"  F_compatibility_only = {symbols.F_compatibility_only}")
    print("\nSelector-firewall gap:")
    print(f"  F_selector_firewall_gap = {symbols.F_selector_firewall_gap}")

    with out.derived_results():
        out.line(
            "selector firewall symbolic loads stated",
            StatusMark.OBLIGATION,
            f"F_forbidden_selector = {symbols.F_forbidden_selector}; F_compatibility_only = {symbols.F_compatibility_only}",
        )

    if ns is not None:
        ns.record_derivation(
            derivation_id="trace_normalization_selector_firewall_loads",
            inputs=[
                symbols.N_trace,
                symbols.S_recovery,
                symbols.S_repair,
                symbols.S_hidden_source,
                symbols.S_insertion,
                symbols.S_active_O,
                symbols.S_parent,
                symbols.S_divergence_safety,
                symbols.S_membership,
                symbols.S_compatibility,
            ],
            output=symbols.F_selector_firewall_gap,
            method="bookkeeping sum of forbidden selector, compatibility-only, and unresolved normalization loads",
            status=Status.DERIVED,
            record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
            result_type="selector_firewall_symbolic_load",
        )


def case_2_rejected_selectors(out: ScriptOutput, selectors: List[RejectedSelector]):
    header("Case 2: Rejected trace-normalization selector routes")

    for item in selectors:
        subheader(item.name)
        print(f"Selector: {item.selector}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Reason: {item.reason}")
        print(f"Allowed future use: {item.allowed_future_use}")
        print(f"Failure mode: {item.failure_mode}")

    with out.counterexamples():
        out.line(
            "trace-normalization selector shortcuts rejected",
            StatusMark.FAIL,
            "recovery, repair, hidden-source, insertion, active-O, parent-fit, membership, and divergence-safety selectors rejected",
        )


def case_3_compatibility_filters(out: ScriptOutput, filters: List[CompatibilityFilter]):
    header("Case 3: Compatibility filters that may reject but not select")

    for item in filters:
        subheader(item.name)
        print(f"Filter: {item.filter}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Allowed use: {item.allowed_use}")
        print(f"Forbidden use: {item.forbidden_use}")
        print(f"Consequence: {item.consequence}")

    with out.governance_assessments():
        out.line(
            "compatibility filters fenced",
            StatusMark.INFO,
            "source/divergence/membership/linearized filters may reject forms but cannot select N_trace",
        )


def case_4_firewall_rules(out: ScriptOutput, rules: List[FirewallRule]):
    header("Case 4: Selector-firewall no-overclaim rules")

    for item in rules:
        subheader(item.name)
        print(f"Rule: {item.rule}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Reason: {item.reason}")

    with out.governance_assessments():
        out.line(
            "selector-firewall no-overclaim rules stated",
            StatusMark.OBLIGATION,
            f"{len(rules)} rules stated",
        )


def case_5_obligations(out: ScriptOutput, obligations: List[SelectorObligation]):
    header("Case 5: Selector-firewall obligations")

    for item in obligations:
        subheader(item.name)
        print(f"Obligation: {item.obligation}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Blocks: {item.blocks}")
        print(f"Discipline: {item.discipline}")

    with out.unresolved_obligations():
        out.line(
            "selector-firewall obligations opened",
            StatusMark.OBLIGATION,
            f"{len(obligations)} obligations stated",
        )


def case_6_conclusions(out: ScriptOutput, conclusions: List[SelectorConclusion]):
    header("Case 6: Selector-firewall conclusions")

    for item in conclusions:
        subheader(item.name)
        print(f"Conclusion: {item.conclusion}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Meaning: {item.meaning}")

    with out.governance_assessments():
        out.line(
            "trace-normalization selector firewall conclusion stated",
            StatusMark.PASS,
            "selector shortcuts rejected; candidate forms should run next; no normalization selected or adopted",
        )


def final_interpretation(out: ScriptOutput):
    header("Final interpretation")

    print("Trace-normalization selector-rejection result:")
    print()
    print("  Forbidden selector routes for N_trace are explicitly named and rejected.")
    print("  Recovery, repair, hidden-source, insertion, active-O, parent-fit,")
    print("  membership-convenience, and divergence-safety-convenience selectors are rejected.")
    print("  Source-neutral, divergence-explicit, safe-membership, and linearized checks")
    print("  may reject candidate forms but cannot choose N_trace.")
    print("  Selector rejection is not derivation.")
    print("  Selector rejection is not adoption.")
    print("  No candidate form is selected by this script.")
    print("  B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready.")
    print()
    print("Possible next script:")
    print("  candidate_trace_normalization_candidate_forms.py")
    print()
    print("Tiny goblin label:")
    print("  Break the false cups before pouring anything.")

    with out.governance_assessments():
        out.line(
            "trace-normalization selector firewall complete",
            StatusMark.PASS,
            "candidate forms should run next; adoption and downstream gates remain closed",
        )


def record_inventory_marker(ns, symbols: SelectorSymbols) -> None:
    ns.record_derivation(
        derivation_id="g33_trace_normalization_selector_rejection",
        inputs=[symbols.N_trace],
        output=symbols.F_selector_firewall_gap,
        method="selector rejection / firewall ledger for trace-normalization candidate-origin route",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="selector_rejection_marker",
        is_placeholder=True,
    )


def record_governance(
    ns,
    selectors: List[RejectedSelector],
    filters: List[CompatibilityFilter],
    rules: List[FirewallRule],
) -> None:
    obligation_ids = [
        "g33_selector_obligation_forbidden_selector_ledger",
        "g33_selector_obligation_negative_filter_boundary",
        "g33_selector_obligation_compatibility_not_selection",
        "g33_selector_obligation_candidate_forms_next",
        "g33_selector_obligation_adoption_boundary",
        "g33_selector_obligation_downstream_gates",
    ]

    for item in selectors:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g33_selector_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.REJECTED_ROUTE,
                statement=(
                    f"{item.selector}. Rejected as selector: {item.reason}. "
                    f"Allowed future use: {item.allowed_future_use}. "
                    f"Failure mode: {item.failure_mode}."
                ),
                derivation_ids=["g33_trace_normalization_selector_rejection"],
                obligation_ids=obligation_ids,
            )
        )

    for item in filters:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_route(
            RouteRecord(
                route_id=f"g33_filter_{ident}",
                script_id=SCRIPT_ID,
                name=item.name,
                status=GovernanceStatus.CANDIDATE_ROUTE,
                tier=ClaimTier.CONSTRAINED,
                required_obligations=obligation_ids,
                activation_conditions=[
                    item.filter,
                    f"Allowed use: {item.allowed_use}",
                    f"Forbidden use: {item.forbidden_use}",
                    f"Consequence: {item.consequence}",
                ],
            )
        )

    for item in rules:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g33_firewall_rule_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.POLICY_RULE,
                statement=f"{item.rule}. Reason: {item.reason}.",
                derivation_ids=["g33_trace_normalization_selector_rejection"],
                obligation_ids=obligation_ids,
            )
        )


def record_obligations(ns, obligations: List[SelectorObligation]) -> None:
    for item in obligations:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_obligation(
            ProofObligationRecord(
                obligation_id=f"g33_selector_obligation_{ident}",
                script_id=SCRIPT_ID,
                title=item.name,
                status=ObligationStatus.OPEN if item.status != "NOT_READY" else ObligationStatus.DEFERRED,
                required_by=[SCRIPT_ID],
                description=f"{item.obligation} Blocks: {item.blocks}. Discipline: {item.discipline}.",
            )
        )


def main() -> None:
    out = ScriptOutput()
    archive, ns, invalidated = prepare_archive()
    ensure_archive_write_dirs(ns)

    header("Candidate Trace-Normalization Selector Rejection")
    print_archive_status(ns, invalidated)

    symbols = build_symbols()
    selectors = build_rejected_selectors()
    filters = build_filters()
    rules = build_rules()
    obligations = build_obligations()
    conclusions = build_conclusions()

    case_0_problem(out)
    case_1_symbolic_loads(out, symbols, ns)
    case_2_rejected_selectors(out, selectors)
    case_3_compatibility_filters(out, filters)
    case_4_firewall_rules(out, rules)
    case_5_obligations(out, obligations)
    case_6_conclusions(out, conclusions)
    final_interpretation(out)

    record_inventory_marker(ns, symbols)
    record_governance(ns, selectors, filters, rules)
    record_obligations(ns, obligations)

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
