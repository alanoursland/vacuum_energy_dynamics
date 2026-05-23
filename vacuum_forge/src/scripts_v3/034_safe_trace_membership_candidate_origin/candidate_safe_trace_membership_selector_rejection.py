# Candidate safe trace membership selector rejection
#
# Group:
#   34_safe_trace_membership_candidate_origin
#
# Human title:
#   Safe Trace Membership Candidate Origin
#
# Script type:
#   SIEVE / SELECTOR-REJECTION FIREWALL
#
# Purpose
# -------
# Record and enforce the rejected selector routes for safe trace membership
# before candidate membership forms are compared.
#
# Locked-door question:
#
#   Which ways of choosing zeta_Bs -> T_zeta are forbidden selectors rather
#   than legitimate typed-sector origins or compatibility tests?
#
# This script does not choose safe membership.
# It does not adopt a safe-membership postulate.
# It does not derive a safe-membership theorem.
# It does not derive trace/residual zero incidence.
# It does not derive B_s/F_zeta insertion.
# It does not open active O, residual control, or parent closure.
#
# Tiny goblin rule:
#
#   Break the false shelves before placing the cup.

from dataclasses import dataclass
from pathlib import Path
from typing import List

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
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
        "FILTER_ONLY": StatusMark.INFO,
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
            "g34_domain_ledger",
            "034_safe_trace_membership_candidate_origin__candidate_safe_trace_membership_domain_ledger",
            "g34_safe_membership_domain_ledger",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g34_origin_problem",
            "034_safe_trace_membership_candidate_origin__candidate_safe_trace_membership_origin_problem",
            "g34_safe_membership_origin_problem",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g33_summary",
            "033_trace_normalization_candidate_origin__candidate_group_33_status_summary",
            "g33_status_summary",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g32_summary",
            "032_explicit_minimal_postulate_selection__candidate_group_32_status_summary",
            "g32_status_summary",
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
    M_safe: sp.Symbol
    zeta_Bs: sp.Symbol
    T_zeta: sp.Symbol
    S_recovery: sp.Symbol
    S_repair: sp.Symbol
    S_incidence: sp.Symbol
    S_residual_kill: sp.Symbol
    S_active_O: sp.Symbol
    S_insertion: sp.Symbol
    S_parent: sp.Symbol
    S_normalization: sp.Symbol
    S_hidden_source: sp.Symbol
    S_hidden_div: sp.Symbol
    S_boundary: sp.Symbol
    F_negative_filter: sp.Expr
    F_forbidden_selector: sp.Expr
    F_compatibility_only: sp.Expr
    F_selector_gap: sp.Expr


@dataclass
class RejectedSelector:
    name: str
    selector: str
    status: str
    reason: str
    allowed_future_use: str
    failure_mode: str


@dataclass
class MembershipFilter:
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
class ObligationEntry:
    name: str
    obligation: str
    status: str
    blocks: str
    discipline: str


@dataclass
class ConclusionEntry:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_symbols() -> SelectorSymbols:
    M_safe, zeta_Bs, T_zeta = sp.symbols("M_safe zeta_Bs T_zeta")
    (
        S_recovery,
        S_repair,
        S_incidence,
        S_residual_kill,
        S_active_O,
        S_insertion,
        S_parent,
        S_normalization,
        S_hidden_source,
        S_hidden_div,
        S_boundary,
    ) = sp.symbols(
        "S_recovery S_repair S_incidence S_residual_kill S_active_O S_insertion S_parent "
        "S_normalization S_hidden_source S_hidden_div S_boundary"
    )

    F_negative_filter = sp.simplify(S_repair + S_hidden_source + S_hidden_div + S_boundary)
    F_forbidden_selector = sp.simplify(
        S_recovery
        + S_repair
        + S_incidence
        + S_residual_kill
        + S_active_O
        + S_insertion
        + S_parent
        + S_normalization
    )
    F_compatibility_only = sp.simplify(S_hidden_source + S_hidden_div + S_normalization + S_boundary)
    F_selector_gap = sp.simplify(
        M_safe
        + zeta_Bs
        + T_zeta
        + F_negative_filter
        + F_forbidden_selector
        + F_compatibility_only
    )

    return SelectorSymbols(
        M_safe=M_safe,
        zeta_Bs=zeta_Bs,
        T_zeta=T_zeta,
        S_recovery=S_recovery,
        S_repair=S_repair,
        S_incidence=S_incidence,
        S_residual_kill=S_residual_kill,
        S_active_O=S_active_O,
        S_insertion=S_insertion,
        S_parent=S_parent,
        S_normalization=S_normalization,
        S_hidden_source=S_hidden_source,
        S_hidden_div=S_hidden_div,
        S_boundary=S_boundary,
        F_negative_filter=F_negative_filter,
        F_forbidden_selector=F_forbidden_selector,
        F_compatibility_only=F_compatibility_only,
        F_selector_gap=F_selector_gap,
    )


def build_rejected_selectors() -> List[RejectedSelector]:
    return [
        RejectedSelector(
            name="S1: recovery selector",
            selector="choose safe membership because AB=1, B=1/A, Schwarzschild, weak-field, gamma/PPN, or kappa=0 works",
            status="REJECTED_AS_SELECTOR",
            reason="recovery may audit after construction but cannot choose zeta_Bs -> T_zeta membership",
            allowed_future_use="post-construction recovery check only",
            failure_mode="target success becomes membership rule",
        ),
        RejectedSelector(
            name="S2: repair selector",
            selector="choose safe membership because it repairs source, divergence, boundary, residual, coefficient, or matching failure",
            status="REJECTED_AS_SELECTOR",
            reason="failure may reject bad membership forms but cannot select the correct one",
            allowed_future_use="negative filter only",
            failure_mode="membership becomes patch for unresolved theorem burden",
        ),
        RejectedSelector(
            name="S3: incidence selector",
            selector="choose membership because it makes I(T_zeta,R_zeta)=0 or I(T_zeta,R_kappa)=0 convenient",
            status="REJECTED_AS_SELECTOR",
            reason="zero incidence is separate high-risk theorem or strong-postulate target",
            allowed_future_use="future incidence theorem only after membership is independently defined",
            failure_mode="membership silently becomes trace/residual no-overlap",
        ),
        RejectedSelector(
            name="S4: residual-kill selector",
            selector="choose membership because it kills residual zeta/kappa trace by declaration",
            status="REJECTED_AS_SELECTOR",
            reason="residual control is not derived and cannot select membership",
            allowed_future_use="future residual-control theorem route only",
            failure_mode="membership becomes residual eraser",
        ),
        RejectedSelector(
            name="S5: active-O selector",
            selector="choose membership because it makes active no-overlap operator O easier to state",
            status="REJECTED_AS_SELECTOR",
            reason="active O is not constructed and cannot select upstream membership",
            allowed_future_use="future compatibility check only after O exists",
            failure_mode="undefined operator back-selects membership",
        ),
        RejectedSelector(
            name="S6: insertion selector",
            selector="choose membership because it makes B_s/F_zeta insertion work",
            status="REJECTED_AS_SELECTOR",
            reason="insertion is downstream and not ready",
            allowed_future_use="conditional precondition audit only after adoption or theorem support",
            failure_mode="candidate membership becomes metric insertion by target fit",
        ),
        RejectedSelector(
            name="S7: parent-fit selector",
            selector="choose membership because it helps close the parent equation",
            status="REJECTED_AS_SELECTOR",
            reason="parent field equation is not ready and cannot choose safe membership",
            allowed_future_use="future parent audit only after upstream gates close",
            failure_mode="parent closure pressure selects upstream membership",
        ),
        RejectedSelector(
            name="S8: normalization selector",
            selector="choose membership because it makes a trace-normalization form convenient or automatic",
            status="REJECTED_AS_SELECTOR",
            reason="trace normalization and safe membership are separate Package B nodes",
            allowed_future_use="compatibility check between separately declared candidates",
            failure_mode="Package B collapses normalization and membership into one choice",
        ),
        RejectedSelector(
            name="S9: hidden-load selector",
            selector="choose membership to hide ordinary source, boundary, support, correction, or divergence load",
            status="REJECTED_AS_SELECTOR",
            reason="membership may not carry hidden source, boundary, support, or correction load",
            allowed_future_use="negative visibility filter only",
            failure_mode="membership becomes hidden load pocket",
        ),
    ]


def build_filters() -> List[MembershipFilter]:
    return [
        MembershipFilter(
            name="F1: source-visible negative filter",
            filter="candidate membership form may be rejected if it carries ordinary source load",
            status="ADMISSIBLE_FILTER_ONLY",
            allowed_use="reject membership forms that violate inherited no-hidden-source discipline",
            forbidden_use="must not select membership merely because it avoids source hiding",
            consequence="source visibility filters candidates but does not derive membership",
        ),
        MembershipFilter(
            name="F2: divergence-visible negative filter",
            filter="candidate membership form may be rejected if it requires hidden correction/divergence reservoir behavior",
            status="ADMISSIBLE_FILTER_ONLY",
            allowed_use="reject forms incompatible with visible non-reservoir correction behavior",
            forbidden_use="must not select membership as divergence-safe coefficient law",
            consequence="explicitness filters candidates but does not derive membership or divergence safety",
        ),
        MembershipFilter(
            name="F3: normalization compatibility filter",
            filter="candidate membership form may be tested for coexistence with separately declared N_trace form",
            status="COMPATIBILITY_ONLY",
            allowed_use="check compatibility with Group 33 compatible-if-declared trace-normalization forms",
            forbidden_use="normalization must not choose membership and membership must not choose normalization",
            consequence="Package B components remain separate nodes",
        ),
        MembershipFilter(
            name="F4: residual-zone negative filter",
            filter="candidate membership form may be rejected if it includes R_zeta or R_kappa as membership payload",
            status="ADMISSIBLE_FILTER_ONLY",
            allowed_use="reject residual-smuggling membership forms",
            forbidden_use="must not use rejection to derive residual kill or zero incidence",
            consequence="residual filtering does not produce residual-control theorem",
        ),
        MembershipFilter(
            name="F5: typed-domain filter",
            filter="candidate membership form may be rejected if zeta_Bs, T_zeta, domain, or codomain are undeclared",
            status="ADMISSIBLE_FILTER_ONLY",
            allowed_use="enforce visibility of membership objects before forms are tested",
            forbidden_use="must not treat a label T_zeta as proof of membership",
            consequence="typed-domain visibility is prerequisite only",
        ),
    ]


def build_rules() -> List[FirewallRule]:
    return [
        FirewallRule(
            name="R1: selector rejection is not derivation",
            rule="rejecting bad selectors does not derive safe membership",
            status="POLICY_RULE",
            reason="negative filter is weaker than theorem support",
        ),
        FirewallRule(
            name="R2: compatibility is not selection",
            rule="source/divergence/normalization/residual compatibility may reject candidates but cannot choose membership",
            status="POLICY_RULE",
            reason="compatibility checks are filters, not origin derivations",
        ),
        FirewallRule(
            name="R3: membership is not normalization",
            rule="zeta_Bs -> T_zeta must not choose P_trace_norm or be chosen by P_trace_norm",
            status="POLICY_RULE",
            reason="Package B keeps normalization and membership as separate nodes",
        ),
        FirewallRule(
            name="R4: membership is not incidence",
            rule="safe membership must not imply I(T_zeta,R_zeta)=0 or I(T_zeta,R_kappa)=0",
            status="POLICY_RULE",
            reason="zero incidence remains high-risk and separate",
        ),
        FirewallRule(
            name="R5: downstream gates cannot back-select",
            rule="insertion, active O, residual control, and parent closure cannot choose safe membership",
            status="POLICY_RULE",
            reason="downstream gates remain not ready",
        ),
        FirewallRule(
            name="R6: membership forms must be visible before filtering",
            rule="candidate membership forms must state object, target sector, domain, codomain, and exclusions before filters are applied",
            status="REQUIRED",
            reason="membership must not hide in prose or failed candidate elimination",
        ),
    ]


def build_obligations() -> List[ObligationEntry]:
    return [
        ObligationEntry(
            name="O1: selector firewall",
            obligation="record recovery, repair, incidence, residual-kill, active-O, insertion, parent-fit, normalization-convenience, and hidden-load selectors as forbidden",
            status="OPEN",
            blocks="membership drift",
            discipline="bad selector may reject or audit but not choose safe membership",
        ),
        ObligationEntry(
            name="O2: negative filter boundary",
            obligation="separate negative filters from typed-sector origin routes",
            status="OPEN",
            blocks="theorem overclaim",
            discipline="candidate rejection is not candidate derivation",
        ),
        ObligationEntry(
            name="O3: membership forms visible next",
            obligation="define candidate membership forms before compatibility sieve",
            status="OPEN",
            blocks="source/divergence/normalization/residual compatibility tests",
            discipline="forms first, filters second",
        ),
        ObligationEntry(
            name="O4: normalization separation",
            obligation="keep safe membership separate from P_trace_norm and Group 33 compatible-if-declared forms",
            status="OPEN",
            blocks="Package B collapse",
            discipline="membership is not normalization",
        ),
        ObligationEntry(
            name="O5: no adoption boundary",
            obligation="keep P_safe_membership unadopted unless separate explicit decision is requested",
            status="OPEN",
            blocks="accidental adoption",
            discipline="selector rejection is not postulate selection",
        ),
        ObligationEntry(
            name="O6: downstream gates",
            obligation="keep insertion, active O, residual control, and parent equation closed",
            status="NOT_READY",
            blocks="downstream overreach",
            discipline="selector firewall is not insertion or parent closure",
        ),
    ]


def build_conclusions() -> List[ConclusionEntry]:
    return [
        ConclusionEntry(
            name="C1: selector firewall complete",
            conclusion="forbidden selector routes are explicitly named and rejected",
            status="REQUIRED",
            meaning="safe membership cannot be chosen from recovery, repair, incidence, residual kill, active O, insertion, parent fit, normalization convenience, or hidden load convenience",
        ),
        ConclusionEntry(
            name="C2: negative filters allowed only as filters",
            conclusion="source/divergence/normalization/residual compatibility can reject forms but cannot select membership",
            status="COMPATIBILITY_ONLY",
            meaning="compatibility remains weaker than derivation or adoption",
        ),
        ConclusionEntry(
            name="C3: no derivation",
            conclusion="this selector ledger derives no safe-membership theorem",
            status="NOT_DERIVED",
            meaning="rejected selectors do not determine the correct membership form",
        ),
        ConclusionEntry(
            name="C4: no adoption",
            conclusion="this selector ledger adopts no safe-membership postulate",
            status="NOT_ADOPTED",
            meaning="explicit decision remains separate",
        ),
        ConclusionEntry(
            name="C5: downstream gates",
            conclusion="B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready",
            status="NOT_READY",
            meaning="selector firewall does not open downstream gates",
        ),
        ConclusionEntry(
            name="C6: next",
            conclusion="candidate safe-membership forms should run next",
            status="OPEN",
            meaning="visible forms can now be compared without forbidden selectors",
        ),
    ]


def line(out: ScriptOutput, label: str, status: str, detail: str) -> None:
    out.line(label, status_mark(status), detail)


def case_0_problem(out: ScriptOutput) -> None:
    header("Case 0: Safe-membership selector-rejection problem")
    print("Question:\n")
    print("  Which ways of choosing zeta_Bs -> T_zeta are forbidden selectors rather")
    print("  than legitimate typed-sector origins or compatibility tests?\n")
    print("Discipline:\n")
    print("  This script rejects selector shortcuts.")
    print("  It adopts no safe-membership postulate.")
    print("  It derives no safe-membership theorem.")
    print("  It derives no trace/residual zero incidence.")
    print("  It performs no membership-form selection.")
    print("  It derives no coefficient law and no insertion.")
    print("  It keeps active O, residual control, and parent closure closed.\n")
    print("Tiny goblin rule:")
    print("  Break the false shelves before placing the cup.\n")
    with out.governance_assessments():
        line(
            out,
            "safe-membership selector firewall opened",
            "OPEN",
            "rejecting forbidden selectors before membership-form comparison",
        )


def case_1_symbolic_loads(out: ScriptOutput, symbols: SelectorSymbols, ns=None) -> None:
    header("Case 1: Selector firewall symbolic loads")
    print("Selector / filter symbols:\n")
    for name in (
        "M_safe",
        "zeta_Bs",
        "T_zeta",
        "S_recovery",
        "S_repair",
        "S_incidence",
        "S_residual_kill",
        "S_active_O",
        "S_insertion",
        "S_parent",
        "S_normalization",
        "S_hidden_source",
        "S_hidden_div",
        "S_boundary",
    ):
        print(f"  {name} = {getattr(symbols, name)}\n")

    print(f"Negative-filter load:\n  F_negative_filter = {symbols.F_negative_filter}\n")
    print(f"Forbidden-selector load:\n  F_forbidden_selector = {symbols.F_forbidden_selector}\n")
    print(f"Compatibility-only load:\n  F_compatibility_only = {symbols.F_compatibility_only}\n")
    print(f"Selector-firewall gap:\n  F_selector_gap = {symbols.F_selector_gap}\n")

    with out.derived_results():
        line(
            out,
            "safe-membership selector firewall symbolic loads stated",
            "REQUIRED",
            f"F_forbidden_selector = {symbols.F_forbidden_selector}; F_compatibility_only = {symbols.F_compatibility_only}",
        )

    if ns is not None:
        ns.record_derivation(
            derivation_id="g34_safe_membership_selector_symbolic_loads",
            inputs=[
                symbols.M_safe,
                symbols.zeta_Bs,
                symbols.T_zeta,
                symbols.S_recovery,
                symbols.S_repair,
                symbols.S_incidence,
                symbols.S_residual_kill,
                symbols.S_active_O,
                symbols.S_insertion,
                symbols.S_parent,
                symbols.S_normalization,
                symbols.S_hidden_source,
                symbols.S_hidden_div,
                symbols.S_boundary,
            ],
            output=symbols.F_selector_gap,
            method="safe-membership selector firewall symbolic load inventory",
            status=Status.DERIVED,
            record_kind=RecordKind.DERIVATION,
            result_type="symbolic_load_inventory",
        )


def case_2_rejected_selectors(out: ScriptOutput, selectors: List[RejectedSelector]) -> None:
    header("Case 2: Rejected safe-membership selector routes")
    for item in selectors:
        subheader(item.name)
        print(f"Selector: {item.selector}")
        line(out, item.name, item.status, item.status)
        print(f"Reason: {item.reason}")
        print(f"Allowed future use: {item.allowed_future_use}")
        print(f"Failure mode: {item.failure_mode}")

    with out.counterexamples():
        line(
            out,
            "safe-membership selector shortcuts rejected",
            "REJECTED_AS_SELECTOR",
            "recovery, repair, incidence, residual kill, active-O, insertion, parent-fit, normalization-convenience, and hidden-load selectors rejected",
        )


def case_3_filters(out: ScriptOutput, filters: List[MembershipFilter]) -> None:
    header("Case 3: Compatibility filters that may reject but not select")
    for item in filters:
        subheader(item.name)
        print(f"Filter: {item.filter}")
        line(out, item.name, item.status, item.status)
        print(f"Allowed use: {item.allowed_use}")
        print(f"Forbidden use: {item.forbidden_use}")
        print(f"Consequence: {item.consequence}")

    with out.governance_assessments():
        line(
            out,
            "safe-membership compatibility filters fenced",
            "COMPATIBILITY_ONLY",
            "source/divergence/normalization/residual filters may reject forms but cannot select membership",
        )


def case_4_rules(out: ScriptOutput, rules: List[FirewallRule]) -> None:
    header("Case 4: Safe-membership selector-firewall no-overclaim rules")
    for item in rules:
        subheader(item.name)
        print(f"Rule: {item.rule}")
        line(out, item.name, item.status, item.status)
        print(f"Reason: {item.reason}")

    with out.governance_assessments():
        line(out, "safe-membership selector-firewall no-overclaim rules stated", "REQUIRED", "6 rules stated")


def case_5_obligations(out: ScriptOutput, obligations: List[ObligationEntry]) -> None:
    header("Case 5: Selector-firewall obligations")
    for item in obligations:
        subheader(item.name)
        print(f"Obligation: {item.obligation}")
        line(out, item.name, item.status, item.status)
        print(f"Blocks: {item.blocks}")
        print(f"Discipline: {item.discipline}")

    with out.unresolved_obligations():
        line(out, "selector-firewall obligations opened", "REQUIRED", "6 obligations stated")


def case_6_conclusions(out: ScriptOutput, conclusions: List[ConclusionEntry]) -> None:
    header("Case 6: Selector-firewall conclusions")
    for item in conclusions:
        subheader(item.name)
        print(f"Conclusion: {item.conclusion}")
        line(out, item.name, item.status, item.status)
        print(f"Meaning: {item.meaning}")

    with out.governance_assessments():
        line(
            out,
            "safe-membership selector firewall conclusion stated",
            "REQUIRED",
            "selector shortcuts rejected; membership forms should run next; no membership selected or adopted",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Safe-membership selector-rejection result:\n")
    print("  Forbidden selector routes for zeta_Bs -> T_zeta are explicitly named and rejected.")
    print("  Recovery, repair, incidence, residual-kill, active-O, insertion, parent-fit,")
    print("  normalization-convenience, and hidden-load selectors are rejected.")
    print("  Source-visible, divergence-visible, normalization, residual-zone, and typed-domain checks")
    print("  may reject candidate forms but cannot choose safe membership.")
    print("  Selector rejection is not derivation.")
    print("  Selector rejection is not adoption.")
    print("  No membership form is selected by this script.")
    print("  B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready.\n")
    print("Possible next script:")
    print("  candidate_safe_trace_membership_candidate_forms.py\n")
    print("Tiny goblin label:")
    print("  Break the false shelves before placing the cup.\n")
    with out.governance_assessments():
        line(
            out,
            "safe-membership selector firewall complete",
            "REQUIRED",
            "candidate membership forms should run next; adoption and downstream gates remain closed",
        )


def record_inventory_marker(ns, symbols: SelectorSymbols) -> None:
    ns.record_derivation(
        derivation_id="g34_safe_membership_selector_rejection",
        inputs=[symbols.M_safe, symbols.zeta_Bs, symbols.T_zeta],
        output=symbols.F_selector_gap,
        method="safe-membership selector-rejection firewall",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="selector_firewall_marker",
        is_placeholder=True,
    )


def record_governance(
    ns,
    selectors: List[RejectedSelector],
    filters: List[MembershipFilter],
    rules: List[FirewallRule],
) -> None:
    obligation_ids = [
        "g34_selector_obligation_o1",
        "g34_selector_obligation_o2",
        "g34_selector_obligation_o3",
        "g34_selector_obligation_o4",
        "g34_selector_obligation_o5",
        "g34_selector_obligation_o6",
    ]

    for item in selectors:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g34_selector_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.REJECTED_ROUTE,
                statement=(
                    f"{item.selector}. Rejected as selector: {item.reason}. "
                    f"Allowed future use: {item.allowed_future_use}. Failure mode: {item.failure_mode}."
                ),
                derivation_ids=["g34_safe_membership_selector_rejection"],
                obligation_ids=obligation_ids,
            )
        )

    for item in filters:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_route(
            RouteRecord(
                route_id=f"g34_filter_{ident}",
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
                claim_id=f"g34_firewall_rule_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.POLICY_RULE,
                statement=f"{item.rule}. Reason: {item.reason}.",
                derivation_ids=["g34_safe_membership_selector_rejection"],
                obligation_ids=obligation_ids,
            )
        )


def record_obligations(ns, obligations: List[ObligationEntry]) -> None:
    for item in obligations:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_obligation(
            ProofObligationRecord(
                obligation_id=f"g34_selector_obligation_{ident}",
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

    header("Candidate Safe Trace Membership Selector Rejection")
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
    case_3_filters(out, filters)
    case_4_rules(out, rules)
    case_5_obligations(out, obligations)
    case_6_conclusions(out, conclusions)
    final_interpretation(out)

    record_inventory_marker(ns, symbols)
    record_governance(ns, selectors, filters, rules)
    record_obligations(ns, obligations)

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
