# Candidate trace-normalization compatibility sieve
#
# Group:
#   33_trace_normalization_candidate_origin
#
# Human title:
#   Trace Normalization Candidate Origin
#
# Script type:
#   COMPATIBILITY SIEVE / NEGATIVE FILTER AUDIT
#
# Purpose
# -------
# Test visible candidate trace-normalization forms against source-neutral,
# divergence-explicit, safe-membership, and linearized filters.
#
# Locked-door question:
#
#   Which visible candidate forms survive compatibility filters, and which
#   remain convention-dependent, without selecting or adopting N_trace?
#
# This script does not choose N_trace.
# It does not adopt a trace-normalization postulate.
# It does not derive a trace-normalization theorem.
# It does not derive B_s/F_zeta insertion.
# It does not open active O, residual control, or parent closure.
#
# Tiny goblin rule:
#
#   Shake the cups. Do not drink yet.

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
        "COMPATIBLE_IF_DECLARED": StatusMark.INFO,
        "COMPATIBILITY_ONLY": StatusMark.INFO,
        "CONVENTION_DEPENDENT": StatusMark.DEFER,
        "FILTER_FAIL": StatusMark.FAIL,
        "LINEARIZED_ONLY": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REQUIRED": StatusMark.OBLIGATION,
        "SURVIVES_FILTER_IF_DECLARED": StatusMark.INFO,
        "UNDECLARED": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def is_zero(expr) -> bool:
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g33_candidate_forms",
            "033_trace_normalization_candidate_origin__candidate_trace_normalization_candidate_forms",
            "g33_trace_normalization_candidate_forms",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g33_selector_firewall",
            "033_trace_normalization_candidate_origin__candidate_trace_normalization_selector_rejection",
            "g33_trace_normalization_selector_rejection",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g33_volume_trace",
            "033_trace_normalization_candidate_origin__candidate_trace_normalization_volume_trace_ledger",
            "g33_volume_trace_ledger",
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
class CompatibilitySymbols:
    zeta: sp.Symbol
    zeta_pd: sp.Symbol
    d: sp.Symbol
    N_trace: sp.Symbol
    N_scale: sp.Expr
    N_metric: sp.Expr
    N_perdim_scale: sp.Expr
    N_perdim_metric: sp.Expr
    N_linear: sp.Symbol
    F_source_neutral: sp.Symbol
    F_div_explicit: sp.Symbol
    F_safe_membership: sp.Symbol
    F_linearized: sp.Symbol
    F_exact_scope: sp.Symbol
    L_visible_forms: sp.Expr
    L_compatibility_filters: sp.Expr
    L_failed_filters: sp.Expr
    L_downstream_closed: sp.Expr
    L_compatibility_gap: sp.Expr


@dataclass
class CompatibilityEntry:
    name: str
    candidate_form: str
    status: str
    survives_if: str
    filter_result: str
    still_open: str
    forbidden_upgrade: str


@dataclass
class FailureEntry:
    name: str
    failure: str
    status: str
    reason: str
    consequence: str


@dataclass
class FilterRule:
    name: str
    rule: str
    status: str
    reason: str


@dataclass
class CompatibilityObligation:
    name: str
    obligation: str
    status: str
    blocks: str
    discipline: str


@dataclass
class CompatibilityConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_symbols() -> CompatibilitySymbols:
    zeta, zeta_pd, d = sp.symbols("zeta zeta_pd d", real=True, nonzero=True)
    N_trace, N_linear = sp.symbols("N_trace N_linear", real=True)

    F_source_neutral, F_div_explicit, F_safe_membership, F_linearized, F_exact_scope = sp.symbols(
        "F_source_neutral F_div_explicit F_safe_membership F_linearized F_exact_scope",
        real=True,
    )
    P_active_O, P_residual_kill, P_insertion, P_parent = sp.symbols(
        "P_active_O P_residual_kill P_insertion P_parent",
        real=True,
    )
    ambiguous_Bs, ambiguous_zeta, hidden_source, hidden_divergence, collapsed_membership = sp.symbols(
        "ambiguous_Bs ambiguous_zeta hidden_source hidden_divergence collapsed_membership",
        real=True,
    )

    N_scale = sp.simplify(zeta / d)
    N_metric = sp.simplify(2 * zeta / d)
    N_perdim_scale = zeta_pd
    N_perdim_metric = sp.simplify(2 * zeta_pd)

    L_visible_forms = sp.simplify(N_scale + N_metric + N_perdim_scale + N_perdim_metric + N_linear)
    L_compatibility_filters = sp.simplify(
        F_source_neutral + F_div_explicit + F_safe_membership + F_linearized + F_exact_scope
    )
    L_failed_filters = sp.simplify(
        ambiguous_Bs + ambiguous_zeta + hidden_source + hidden_divergence + collapsed_membership
    )
    L_downstream_closed = sp.simplify(P_active_O + P_residual_kill + P_insertion + P_parent)
    L_compatibility_gap = sp.simplify(
        N_trace + L_visible_forms + L_compatibility_filters + L_failed_filters + L_downstream_closed
    )

    return CompatibilitySymbols(
        zeta=zeta,
        zeta_pd=zeta_pd,
        d=d,
        N_trace=N_trace,
        N_scale=N_scale,
        N_metric=N_metric,
        N_perdim_scale=N_perdim_scale,
        N_perdim_metric=N_perdim_metric,
        N_linear=N_linear,
        F_source_neutral=F_source_neutral,
        F_div_explicit=F_div_explicit,
        F_safe_membership=F_safe_membership,
        F_linearized=F_linearized,
        F_exact_scope=F_exact_scope,
        L_visible_forms=L_visible_forms,
        L_compatibility_filters=L_compatibility_filters,
        L_failed_filters=L_failed_filters,
        L_downstream_closed=L_downstream_closed,
        L_compatibility_gap=L_compatibility_gap,
    )


def build_compatibility_entries() -> List[CompatibilityEntry]:
    return [
        CompatibilityEntry(
            name="C1: scale-factor volume-log form",
            candidate_form="log(B_s) = zeta/d",
            status="SURVIVES_FILTER_IF_DECLARED",
            survives_if="B_s is declared to be scale-factor language, zeta is total volume-log trace, and d is declared before recovery",
            filter_result="passes structural visibility and remains compatible with source/divergence filters as long as it introduces no hidden source or correction reservoir",
            still_open="does not decide safe membership, incidence, exact coefficient law, or insertion",
            forbidden_upgrade="must not be selected just because it later recovers AB=1 or gamma=1",
        ),
        CompatibilityEntry(
            name="C2: metric-coefficient volume-log form",
            candidate_form="log(B_s) = 2*zeta/d",
            status="SURVIVES_FILTER_IF_DECLARED",
            survives_if="B_s is declared to be metric-coefficient language, zeta is total volume-log trace, and d is declared before recovery",
            filter_result="passes structural visibility and remains compatible with source/divergence filters if no ordinary source load or hidden reservoir is introduced",
            still_open="does not decide safe membership, residual non-entry, active O, or insertion",
            forbidden_upgrade="must not be selected to make downstream metric insertion easier",
        ),
        CompatibilityEntry(
            name="C3: per-dimension zeta scale form",
            candidate_form="log(B_s) = zeta_pd",
            status="CONVENTION_DEPENDENT",
            survives_if="zeta_pd is explicitly declared to be zeta_total/d and B_s is scale-factor language",
            filter_result="notation-equivalent to the scale-factor volume-log form only after convention declaration",
            still_open="does not remove the need to declare the total/per-dimension convention",
            forbidden_upgrade="must not hide the dimension factor inside notation without declaring it",
        ),
        CompatibilityEntry(
            name="C4: per-dimension zeta metric form",
            candidate_form="log(B_s) = 2*zeta_pd",
            status="CONVENTION_DEPENDENT",
            survives_if="zeta_pd is explicitly declared to be zeta_total/d and B_s is metric-coefficient language",
            filter_result="notation-equivalent to metric-coefficient volume-log form only after convention declaration",
            still_open="does not derive exact insertion or residual control",
            forbidden_upgrade="must not hide factor-of-two convention in notation",
        ),
        CompatibilityEntry(
            name="C5: linearized trace-only form",
            candidate_form="first-order delta ln sqrt(gamma) = 1/2 tr(h)",
            status="LINEARIZED_ONLY",
            survives_if="scope is explicitly first-order and perturbative variables are declared",
            filter_result="usable as first-order consistency check only",
            still_open="does not derive exact nonlinear trace normalization or coefficient law",
            forbidden_upgrade="must not be promoted to exact B_s/F_zeta law or parent insertion",
        ),
    ]


def build_failure_entries() -> List[FailureEntry]:
    return [
        FailureEntry(
            name="F1: undeclared B_s convention",
            failure="candidate form does not say whether B_s is scale factor, metric coefficient, or separate functional response",
            status="FILTER_FAIL",
            reason="the scale-factor and metric-coefficient conventions differ by a factor of two",
            consequence="compatibility sieve cannot classify the form",
        ),
        FailureEntry(
            name="F2: undeclared zeta convention",
            failure="candidate form does not say whether zeta is total volume-log trace or per-dimension trace",
            status="FILTER_FAIL",
            reason="per-dimension notation can hide the dimension factor",
            consequence="normalization remains ambiguous",
        ),
        FailureEntry(
            name="F3: undeclared traced dimension",
            failure="candidate form uses zeta/d or 2*zeta/d without declaring d",
            status="FILTER_FAIL",
            reason="dimension count must not be selected after recovery targets are known",
            consequence="dimensional route remains unavailable",
        ),
        FailureEntry(
            name="F4: hidden source dependence",
            failure="candidate form carries ordinary source load or source repair in normalization",
            status="FILTER_FAIL",
            reason="source-neutral filter may reject but not select forms",
            consequence="candidate form violates inherited no-hidden-source discipline",
        ),
        FailureEntry(
            name="F5: hidden divergence reservoir",
            failure="candidate form requires hidden correction/divergence reservoir behavior",
            status="FILTER_FAIL",
            reason="divergence explicitness is required as non-reservoir discipline",
            consequence="candidate form violates explicitness filter",
        ),
        FailureEntry(
            name="F6: membership collapse",
            failure="candidate form treats normalization as automatically giving zeta_Bs -> T_zeta membership or incidence",
            status="FILTER_FAIL",
            reason="normalization and membership are separate Package B nodes",
            consequence="candidate form smuggles safe membership or residual control",
        ),
        FailureEntry(
            name="F7: exact upgrade from linearized form",
            failure="linearized trace relation is used as exact nonlinear coefficient law",
            status="FILTER_FAIL",
            reason="linearized consistency is not exact theorem support",
            consequence="candidate form overclaims its scope",
        ),
    ]


def build_filter_rules() -> List[FilterRule]:
    return [
        FilterRule(
            name="R1: compatible-if-declared is not selected",
            rule="A form that survives filters if declared is still not selected or adopted",
            status="POLICY_RULE",
            reason="compatibility sieve is weaker than theorem derivation or explicit choice",
        ),
        FilterRule(
            name="R2: filters reject but do not choose",
            rule="source/divergence/membership/linearized filters may reject forms but cannot choose N_trace",
            status="POLICY_RULE",
            reason="negative filters are not origin derivations",
        ),
        FilterRule(
            name="R3: convention declaration is mandatory",
            rule="B_s convention, zeta convention, and traced dimension must be declared before compatibility claims",
            status="REQUIRED",
            reason="otherwise factor-of-two and dimension factors are hidden",
        ),
        FilterRule(
            name="R4: membership remains separate",
            rule="compatibility with safe membership does not derive membership or incidence",
            status="POLICY_RULE",
            reason="Package B components remain separate nodes",
        ),
        FilterRule(
            name="R5: downstream gates remain closed",
            rule="surviving candidate forms do not license insertion, active O, residual control, or parent closure",
            status="POLICY_RULE",
            reason="candidate-form compatibility is not downstream theorem closure",
        ),
    ]


def build_obligations() -> List[CompatibilityObligation]:
    return [
        CompatibilityObligation(
            name="O1: declare B_s object status",
            obligation="decide whether future use of B_s is scale-factor language, metric-coefficient language, or separate functional response",
            status="OPEN",
            blocks="candidate narrowing and trace-normalization status summary",
            discipline="compatible-if-declared is not selected",
        ),
        CompatibilityObligation(
            name="O2: declare zeta convention",
            obligation="decide whether zeta means total volume-log trace or per-dimension normalized trace",
            status="OPEN",
            blocks="candidate narrowing",
            discipline="do not hide dimension factor in notation",
        ),
        CompatibilityObligation(
            name="O3: declare traced dimension",
            obligation="state the traced sector dimension before using zeta/d or 2*zeta/d",
            status="OPEN",
            blocks="dimensional normalization route",
            discipline="dimension count cannot be recovery-selected",
        ),
        CompatibilityObligation(
            name="O4: keep filters negative",
            obligation="use source/divergence/membership/linearized filters only to reject or flag forms, not to select N_trace",
            status="OPEN",
            blocks="selector drift",
            discipline="compatibility is not derivation",
        ),
        CompatibilityObligation(
            name="O5: adoption boundary",
            obligation="keep P_trace_norm unadopted unless a separate explicit decision is requested",
            status="OPEN",
            blocks="accidental adoption",
            discipline="sieve survival is not postulate selection",
        ),
        CompatibilityObligation(
            name="O6: downstream gates",
            obligation="keep insertion, active O, residual control, and parent equation closed",
            status="NOT_READY",
            blocks="downstream overreach",
            discipline="compatibility sieve is not insertion or parent closure",
        ),
    ]


def build_conclusions() -> List[CompatibilityConclusion]:
    return [
        CompatibilityConclusion(
            name="C1: exact structural forms survive if declared",
            conclusion="scale-factor and metric-coefficient volume-log forms survive compatibility filters only under explicit object conventions",
            status="COMPATIBLE_IF_DECLARED",
            meaning="both remain visible candidate forms; neither is selected",
        ),
        CompatibilityConclusion(
            name="C2: per-dimension forms remain notation-dependent",
            conclusion="per-dimension zeta forms survive only if zeta_pd is declared as per-direction trace variable",
            status="CONVENTION_DEPENDENT",
            meaning="notation may be equivalent but cannot hide the dimension factor",
        ),
        CompatibilityConclusion(
            name="C3: linearized form remains linearized only",
            conclusion="linearized trace bookkeeping survives as first-order consistency check only",
            status="LINEARIZED_ONLY",
            meaning="not exact trace-normalization theorem",
        ),
        CompatibilityConclusion(
            name="C4: no selection",
            conclusion="this compatibility sieve selects no final normalization form",
            status="NOT_SELECTED",
            meaning="filter survival is not selection, adoption, or theorem derivation",
        ),
        CompatibilityConclusion(
            name="C5: downstream gates",
            conclusion="B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready",
            status="NOT_READY",
            meaning="compatibility sieve does not open downstream gates",
        ),
        CompatibilityConclusion(
            name="C6: next",
            conclusion="trace-normalization obligations or status summary should run next",
            status="OPEN",
            meaning="the group can summarize surviving forms and unresolved convention decisions without adopting",
        ),
    ]


def case_0_problem(out: ScriptOutput) -> None:
    header("Case 0: Trace-normalization compatibility-sieve problem")
    print("Question:")
    print()
    print("  Which visible candidate forms survive compatibility filters, and which")
    print("  remain convention-dependent, without selecting or adopting N_trace?")
    print()
    print("Discipline:")
    print()
    print("  This script applies compatibility filters.")
    print("  It adopts no trace-normalization postulate.")
    print("  It selects no final normalization.")
    print("  It derives no trace-normalization theorem.")
    print("  It derives no coefficient law and no insertion.")
    print("  It keeps active O, residual control, and parent closure closed.")
    print()
    print("Tiny goblin rule:")
    print("  Shake the cups. Do not drink yet.")

    with out.governance_assessments():
        out.line(
            "trace-normalization compatibility sieve opened",
            StatusMark.INFO,
            "visible forms are filtered without selecting or adopting N_trace",
        )


def case_1_symbolic_ledger(out: ScriptOutput) -> CompatibilitySymbols:
    header("Case 1: Compatibility-sieve symbolic ledger")
    symbols = build_symbols()

    print("Candidate forms:")
    print()
    print(f"  N_scale = zeta/d = {symbols.N_scale}")
    print(f"  N_metric = 2*zeta/d = {symbols.N_metric}")
    print(f"  N_perdim_scale = zeta_pd = {symbols.N_perdim_scale}")
    print(f"  N_perdim_metric = 2*zeta_pd = {symbols.N_perdim_metric}")
    print()
    print("Filter symbols:")
    print()
    for item in (
        symbols.F_source_neutral,
        symbols.F_div_explicit,
        symbols.F_safe_membership,
        symbols.F_linearized,
        symbols.F_exact_scope,
    ):
        print(f"  {item} = {item}")
    print()
    print(f"Visible-form load:\n  L_visible_forms = {symbols.L_visible_forms}")
    print()
    print(f"Compatibility-filter load:\n  L_compatibility_filters = {symbols.L_compatibility_filters}")
    print()
    print(f"Failed-filter load:\n  L_failed_filters = {symbols.L_failed_filters}")
    print()
    print(f"Downstream closed load:\n  L_downstream_closed = {symbols.L_downstream_closed}")
    print()
    print(f"Compatibility gap:\n  L_compatibility_gap = {symbols.L_compatibility_gap}")

    with out.derived_results():
        out.line(
            "compatibility sieve symbolic loads stated",
            StatusMark.OBLIGATION,
            f"L_visible_forms={symbols.L_visible_forms}; L_compatibility_filters={symbols.L_compatibility_filters}",
        )

    return symbols


def case_2_candidate_filter_results(out: ScriptOutput) -> List[CompatibilityEntry]:
    header("Case 2: Candidate-form compatibility results")
    entries = build_compatibility_entries()

    for entry in entries:
        subheader(entry.name)
        print(f"Candidate form: {entry.candidate_form}")
        print(f"[{status_mark(entry.status).value}] {entry.name}: {entry.status}")
        print(f"Survives if: {entry.survives_if}")
        print(f"Filter result: {entry.filter_result}")
        print(f"Still open: {entry.still_open}")
        print(f"Forbidden upgrade: {entry.forbidden_upgrade}")

    with out.governance_assessments():
        out.line(
            "candidate forms filtered",
            StatusMark.DEFER,
            "forms survive only conditionally; none selected or adopted",
        )

    return entries


def case_3_failure_modes(out: ScriptOutput) -> List[FailureEntry]:
    header("Case 3: Compatibility failure modes")
    entries = build_failure_entries()

    for entry in entries:
        subheader(entry.name)
        print(f"Failure: {entry.failure}")
        print(f"[{status_mark(entry.status).value}] {entry.name}: {entry.status}")
        print(f"Reason: {entry.reason}")
        print(f"Consequence: {entry.consequence}")

    with out.counterexamples():
        out.line(
            "compatibility failure modes stated",
            StatusMark.FAIL,
            "ambiguous conventions, hidden sources, hidden reservoirs, membership collapse, and linearized exact-upgrade fail the sieve",
        )

    return entries


def case_4_filter_rules(out: ScriptOutput) -> List[FilterRule]:
    header("Case 4: Compatibility-sieve no-overclaim rules")
    rules = build_filter_rules()

    for rule in rules:
        subheader(rule.name)
        print(f"Rule: {rule.rule}")
        print(f"[{status_mark(rule.status).value}] {rule.name}: {rule.status}")
        print(f"Reason: {rule.reason}")

    with out.governance_assessments():
        out.line(
            "compatibility-sieve no-overclaim rules stated",
            StatusMark.OBLIGATION,
            "5 rules stated",
        )

    return rules


def case_5_obligations(out: ScriptOutput) -> List[CompatibilityObligation]:
    header("Case 5: Compatibility-sieve obligations")
    obligations = build_obligations()

    for obligation in obligations:
        subheader(obligation.name)
        print(f"Obligation: {obligation.obligation}")
        print(f"[{status_mark(obligation.status).value}] {obligation.name}: {obligation.status}")
        print(f"Blocks: {obligation.blocks}")
        print(f"Discipline: {obligation.discipline}")

    with out.unresolved_obligations():
        out.line(
            "compatibility-sieve obligations opened",
            StatusMark.OBLIGATION,
            "6 obligations stated",
        )

    return obligations


def case_6_conclusions(out: ScriptOutput) -> List[CompatibilityConclusion]:
    header("Case 6: Compatibility-sieve conclusions")
    conclusions = build_conclusions()

    for conclusion in conclusions:
        subheader(conclusion.name)
        print(f"Conclusion: {conclusion.conclusion}")
        print(f"[{status_mark(conclusion.status).value}] {conclusion.name}: {conclusion.status}")
        print(f"Meaning: {conclusion.meaning}")

    with out.governance_assessments():
        out.line(
            "trace-normalization compatibility sieve conclusion stated",
            StatusMark.PASS,
            "forms survive conditionally; no normalization selected or adopted; obligations/status summary should run next",
        )

    return conclusions


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Trace-normalization compatibility-sieve result:")
    print()
    print("  Scale-factor and metric-coefficient volume-log forms survive only if their object conventions are explicitly declared.")
    print("  Per-dimension zeta forms survive only as notation-dependent variants with the dimension factor already inside zeta.")
    print("  Linearized trace bookkeeping survives only as a first-order consistency check.")
    print("  Forms with undeclared B_s convention, undeclared zeta convention, hidden source load, hidden divergence reservoir, membership collapse, or linearized exact-upgrade fail the sieve.")
    print("  Compatibility filters may reject or flag forms but cannot choose N_trace.")
    print("  No trace-normalization rule is selected, adopted, or derived by this sieve.")
    print("  B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready.")
    print()
    print("Possible next script:")
    print("  candidate_trace_normalization_obligations.py")
    print()
    print("Tiny goblin label:")
    print("  Shake the cups. Do not drink yet.")
    with out.governance_assessments():
        out.line(
            "trace-normalization compatibility sieve complete",
            StatusMark.PASS,
            "obligations/status summary should run next; adoption and downstream gates remain closed",
        )


def record_inventory_marker(ns, symbols: CompatibilitySymbols) -> None:
    ns.record_derivation(
        derivation_id="g33_trace_normalization_compatibility_sieve",
        inputs=[symbols.N_trace],
        output=symbols.L_compatibility_gap,
        method="trace-normalization compatibility sieve ledger",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="compatibility_sieve_marker",
        is_placeholder=True,
    )


def record_governance(
    ns,
    compat_entries: List[CompatibilityEntry],
    failure_entries: List[FailureEntry],
    rules: List[FilterRule],
) -> None:
    obligation_ids = [
        "g33_compat_obligation_o1",
        "g33_compat_obligation_o2",
        "g33_compat_obligation_o3",
        "g33_compat_obligation_o4",
        "g33_compat_obligation_o5",
        "g33_compat_obligation_o6",
    ]

    for item in compat_entries:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_route(
            RouteRecord(
                route_id=f"g33_compat_form_{ident}",
                script_id=SCRIPT_ID,
                name=item.name,
                status=GovernanceStatus.CANDIDATE_ROUTE,
                tier=ClaimTier.CONSTRAINED,
                required_obligations=obligation_ids,
                activation_conditions=[
                    item.candidate_form,
                    f"Survives if: {item.survives_if}",
                    f"Filter result: {item.filter_result}",
                    f"Still open: {item.still_open}",
                    f"Forbidden upgrade: {item.forbidden_upgrade}",
                ],
            )
        )

    for item in failure_entries:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g33_compat_failure_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.REJECTED_ROUTE,
                statement=f"{item.failure}. Reason: {item.reason}. Consequence: {item.consequence}.",
                derivation_ids=["g33_trace_normalization_compatibility_sieve"],
                obligation_ids=obligation_ids,
            )
        )

    for item in rules:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g33_compat_rule_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.POLICY_RULE,
                statement=f"{item.rule}. Reason: {item.reason}.",
                derivation_ids=["g33_trace_normalization_compatibility_sieve"],
                obligation_ids=obligation_ids,
            )
        )


def record_obligations(ns, obligations: List[CompatibilityObligation]) -> None:
    for item in obligations:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_obligation(
            ProofObligationRecord(
                obligation_id=f"g33_compat_obligation_{ident}",
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

    header("Candidate Trace-Normalization Compatibility Sieve")
    print_archive_status(ns, invalidated)

    case_0_problem(out)
    symbols = case_1_symbolic_ledger(out)
    compat_entries = case_2_candidate_filter_results(out)
    failure_entries = case_3_failure_modes(out)
    rules = case_4_filter_rules(out)
    obligations = case_5_obligations(out)
    case_6_conclusions(out)
    final_interpretation(out)

    record_inventory_marker(ns, symbols)
    record_obligations(ns, obligations)
    record_governance(ns, compat_entries, failure_entries, rules)

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
