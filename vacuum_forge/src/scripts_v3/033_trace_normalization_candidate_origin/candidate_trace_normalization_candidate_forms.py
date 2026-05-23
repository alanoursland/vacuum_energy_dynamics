# Candidate trace-normalization candidate forms
#
# Group:
#   33_trace_normalization_candidate_origin
#
# Human title:
#   Trace Normalization Candidate Origin
#
# Script type:
#   CANDIDATE-FORM LEDGER / STRUCTURAL COMPARISON
#
# Purpose
# -------
# Define visible candidate trace-normalization forms after the selector firewall
# and before compatibility testing.
#
# Locked-door question:
#
#   Which visible candidate forms for N_trace follow from the declared meanings
#   of zeta, B_s, and the traced dimension, without selecting a final
#   normalization or adopting a postulate?
#
# This script does not choose N_trace.
# It does not adopt a trace-normalization postulate.
# It does not derive a trace-normalization theorem.
# It does not derive B_s/F_zeta insertion.
# It does not open active O, residual control, or parent closure.
#
# Tiny goblin rule:
#
#   Put the cups on the table. Do not drink yet.

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
        "CANDIDATE_FORM": StatusMark.INFO,
        "CONVENTION_DEPENDENT": StatusMark.DEFER,
        "STRUCTURAL_CONSTRAINT": StatusMark.INFO,
        "LINEARIZED_ONLY": StatusMark.DEFER,
        "COMPATIBILITY_PENDING": StatusMark.DEFER,
        "NOT_SELECTED": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REQUIRED": StatusMark.OBLIGATION,
        "REJECTED_AS_SELECTOR": StatusMark.FAIL,
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
class CandidateFormSymbols:
    zeta: sp.Symbol
    zeta_pd: sp.Symbol
    d: sp.Symbol
    N_trace: sp.Symbol
    N_scale: sp.Expr
    N_metric: sp.Expr
    N_perdim_scale: sp.Expr
    N_perdim_metric: sp.Expr
    N_linear: sp.Symbol
    Delta_scale_metric: sp.Expr
    L_candidate_forms: sp.Expr
    L_selection_forbidden: sp.Expr
    L_candidate_form_gap: sp.Expr


@dataclass
class CandidateForm:
    name: str
    convention: str
    candidate_form: str
    status: str
    requires: str
    scope: str
    not_equivalent_to: str
    next_test: str


@dataclass
class FormComparison:
    name: str
    comparison: str
    status: str
    result: str
    boundary: str


@dataclass
class FormRule:
    name: str
    rule: str
    status: str
    reason: str


@dataclass
class FormObligation:
    name: str
    obligation: str
    status: str
    blocks: str
    discipline: str


@dataclass
class FormConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_symbols() -> CandidateFormSymbols:
    zeta, zeta_pd, d = sp.symbols("zeta zeta_pd d", positive=True, real=True)
    N_trace = sp.symbols("N_trace", real=True)
    N_linear = sp.symbols("N_linear", real=True)

    N_scale = sp.simplify(zeta / d)
    N_metric = sp.simplify(2 * zeta / d)
    N_perdim_scale = sp.simplify(zeta_pd)
    N_perdim_metric = sp.simplify(2 * zeta_pd)
    Delta_scale_metric = sp.simplify(N_metric - N_scale)

    L_candidate_forms = sp.simplify(N_scale + N_metric + N_perdim_scale + N_perdim_metric + N_linear)

    S_recovery, S_repair, S_insertion, S_parent = sp.symbols(
        "S_recovery S_repair S_insertion S_parent", real=True
    )
    L_selection_forbidden = sp.simplify(S_recovery + S_repair + S_insertion + S_parent)
    L_candidate_form_gap = sp.simplify(N_trace + L_candidate_forms + L_selection_forbidden)

    return CandidateFormSymbols(
        zeta=zeta,
        zeta_pd=zeta_pd,
        d=d,
        N_trace=N_trace,
        N_scale=N_scale,
        N_metric=N_metric,
        N_perdim_scale=N_perdim_scale,
        N_perdim_metric=N_perdim_metric,
        N_linear=N_linear,
        Delta_scale_metric=Delta_scale_metric,
        L_candidate_forms=L_candidate_forms,
        L_selection_forbidden=L_selection_forbidden,
        L_candidate_form_gap=L_candidate_form_gap,
    )


def build_candidate_forms() -> List[CandidateForm]:
    return [
        CandidateForm(
            name="F1: scale-factor volume-log form",
            convention="B_s is a spatial scale factor and zeta is total volume-log trace",
            candidate_form="log(B_s) = zeta / d",
            status="CANDIDATE_FORM",
            requires="zeta is volume-log trace; d is declared traced sector dimension; B_s is scale-factor response",
            scope="structural convention candidate",
            not_equivalent_to="metric-coefficient form, safe membership, insertion, or recovery",
            next_test="test compatibility with source/divergence and safe-membership fences",
        ),
        CandidateForm(
            name="F2: metric-coefficient volume-log form",
            convention="B_s is a spatial metric coefficient response and zeta is total volume-log trace",
            candidate_form="log(B_s) = 2*zeta / d",
            status="CANDIDATE_FORM",
            requires="zeta is volume-log trace; d is declared traced sector dimension; B_s denotes metric coefficient response",
            scope="structural convention candidate",
            not_equivalent_to="scale-factor form, residual kill, active O, or insertion",
            next_test="test whether B_s notation in later scripts is scale-factor or metric-coefficient language",
        ),
        CandidateForm(
            name="F3: per-dimension zeta scale form",
            convention="zeta is already divided by traced dimension and B_s is a scale factor",
            candidate_form="log(B_s) = zeta_pd",
            status="CONVENTION_DEPENDENT",
            requires="explicit declaration that zeta_pd is per-direction trace variable",
            scope="renormalized variable convention candidate",
            not_equivalent_to="deriving normalization from Package B minimality or recovery",
            next_test="verify whether prior zeta notation is total trace or per-dimension trace",
        ),
        CandidateForm(
            name="F4: per-dimension zeta metric form",
            convention="zeta is already divided by traced dimension and B_s is a metric coefficient",
            candidate_form="log(B_s) = 2*zeta_pd",
            status="CONVENTION_DEPENDENT",
            requires="explicit declaration that zeta_pd is per-direction trace variable and B_s is metric coefficient",
            scope="renormalized variable convention candidate",
            not_equivalent_to="scale-factor convention or exact insertion law",
            next_test="verify notation before compatibility sieve",
        ),
        CandidateForm(
            name="F5: linearized trace-only form",
            convention="normalization fixed only at first order by spatial trace bookkeeping",
            candidate_form="first-order delta ln sqrt(gamma) = 1/2 tr(h)",
            status="LINEARIZED_ONLY",
            requires="explicit first-order scope and perturbative variables",
            scope="linearized consistency candidate only",
            not_equivalent_to="exact coefficient law, nonlinear determinant theorem, insertion, or parent closure",
            next_test="keep separate from exact structural forms",
        ),
    ]


def build_comparisons() -> List[FormComparison]:
    return [
        FormComparison(
            name="T1: scale versus metric coefficient factor",
            comparison="zeta/d versus 2*zeta/d",
            status="STRUCTURAL_CONSTRAINT",
            result="the two main volume-log forms differ by a factor of two because scale factor and metric coefficient are different objects",
            boundary="this does not choose which object B_s denotes",
        ),
        FormComparison(
            name="T2: total trace versus per-dimension trace",
            comparison="zeta_total/d versus zeta_per_dimension",
            status="CONVENTION_DEPENDENT",
            result="per-dimension forms can be notation-equivalent only after zeta convention is declared",
            boundary="notation choice is not physical derivation",
        ),
        FormComparison(
            name="T3: linearized versus exact",
            comparison="first-order trace bookkeeping versus exact determinant decomposition",
            status="LINEARIZED_ONLY",
            result="linearized success can constrain first-order consistency only",
            boundary="do not upgrade first-order form to exact B_s/F_zeta law",
        ),
        FormComparison(
            name="T4: visible form before compatibility filter",
            comparison="declared candidate form versus hidden prose normalization",
            status="REQUIRED",
            result="forms must be stated before source/divergence/membership filters are applied",
            boundary="filtering hidden forms reopens selector drift",
        ),
    ]


def build_rules() -> List[FormRule]:
    return [
        FormRule(
            name="R1: candidate form is not selection",
            rule="Listing a candidate form does not select N_trace",
            status="POLICY_RULE",
            reason="candidate-form ledger is weaker than adoption or theorem derivation",
        ),
        FormRule(
            name="R2: B_s convention must be explicit",
            rule="Every candidate form must state whether B_s is a scale factor, metric coefficient, or separate functional response",
            status="REQUIRED",
            reason="the normalization differs by a factor of two between scale-factor and metric-coefficient conventions",
        ),
        FormRule(
            name="R3: zeta convention must be explicit",
            rule="Every candidate form must state whether zeta is total volume-log trace or per-dimension trace",
            status="REQUIRED",
            reason="per-dimension notation can hide the same normalization in the variable definition",
        ),
        FormRule(
            name="R4: candidate form is not membership",
            rule="Candidate trace-normalization forms do not imply zeta_Bs -> T_zeta membership",
            status="POLICY_RULE",
            reason="normalization and safe membership remain separate Package B components",
        ),
        FormRule(
            name="R5: candidate form is not insertion",
            rule="No candidate form licenses B_s/F_zeta insertion, active O, residual control, or parent closure",
            status="POLICY_RULE",
            reason="downstream gates remain closed",
        ),
    ]


def build_obligations() -> List[FormObligation]:
    return [
        FormObligation(
            name="O1: B_s notation decision",
            obligation="declare whether B_s is scale-factor language, metric-coefficient language, or separate functional response",
            status="OPEN",
            blocks="candidate-form comparison and compatibility sieve",
            discipline="normalization depends on object meaning",
        ),
        FormObligation(
            name="O2: zeta notation decision",
            obligation="declare whether zeta is total volume-log trace or per-dimension normalized trace",
            status="OPEN",
            blocks="candidate-form comparison",
            discipline="do not hide dimension factor in notation",
        ),
        FormObligation(
            name="O3: traced dimension declaration",
            obligation="declare the traced sector dimension d before using zeta/d or 2*zeta/d forms",
            status="OPEN",
            blocks="dimensional-counting route",
            discipline="dimension count cannot be selected from recovery",
        ),
        FormObligation(
            name="O4: compatibility sieve next",
            obligation="test visible candidate forms against source-neutral, divergence-explicit, safe-membership, and linearized filters",
            status="OPEN",
            blocks="candidate narrowing",
            discipline="compatibility may reject but not select",
        ),
        FormObligation(
            name="O5: adoption boundary",
            obligation="keep P_trace_norm unadopted unless a separate explicit decision is requested",
            status="OPEN",
            blocks="accidental adoption",
            discipline="candidate form is not adopted postulate",
        ),
        FormObligation(
            name="O6: downstream gates",
            obligation="keep insertion, active O, residual control, and parent equation closed",
            status="NOT_READY",
            blocks="downstream overreach",
            discipline="candidate-form ledger is not insertion or parent closure",
        ),
    ]


def build_conclusions() -> List[FormConclusion]:
    return [
        FormConclusion(
            name="C1: candidate forms visible",
            conclusion="scale-factor, metric-coefficient, per-dimension, and linearized candidate forms are stated",
            status="CANDIDATE_FORM",
            meaning="normalization no longer hides in prose",
        ),
        FormConclusion(
            name="C2: convention dependence",
            conclusion="candidate form depends on declared meanings of zeta, B_s, and d",
            status="CONVENTION_DEPENDENT",
            meaning="no final normalization is selected by this ledger",
        ),
        FormConclusion(
            name="C3: no derivation",
            conclusion="this ledger derives no trace-normalization theorem",
            status="NOT_DERIVED",
            meaning="candidate forms are visible options, not proof",
        ),
        FormConclusion(
            name="C4: no adoption",
            conclusion="this ledger adopts no trace-normalization postulate",
            status="NOT_ADOPTED",
            meaning="explicit decision remains separate",
        ),
        FormConclusion(
            name="C5: downstream gates",
            conclusion="B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready",
            status="NOT_READY",
            meaning="candidate-form comparison does not open downstream gates",
        ),
        FormConclusion(
            name="C6: next",
            conclusion="trace-normalization compatibility sieve should run next",
            status="OPEN",
            meaning="visible candidate forms can now be filtered without selecting by forbidden routes",
        ),
    ]


def case_0_problem(out: ScriptOutput):
    header("Case 0: Trace-normalization candidate-form problem")
    print("Question:")
    print()
    print("  Which visible candidate forms for N_trace follow from the declared meanings")
    print("  of zeta, B_s, and the traced dimension, without selecting a final")
    print("  normalization or adopting a postulate?")
    print()
    print("Discipline:")
    print()
    print("  This script defines candidate forms.")
    print("  It adopts no trace-normalization postulate.")
    print("  It selects no final normalization.")
    print("  It derives no trace-normalization theorem.")
    print("  It derives no coefficient law and no insertion.")
    print("  It keeps active O, residual control, and parent closure closed.")
    print()
    print("Tiny goblin rule:")
    print("  Put the cups on the table. Do not drink yet.")
    with out.governance_assessments():
        out.line(
            "trace-normalization candidate-form ledger opened",
            StatusMark.INFO,
            "visible forms are stated after selector firewall and before compatibility sieve",
        )


def case_1_symbolic_forms(out: ScriptOutput, symbols: CandidateFormSymbols, ns=None):
    header("Case 1: Candidate-form symbolic ledger")
    print("Candidate-form symbols:")
    for name in ("zeta", "zeta_pd", "d", "N_trace", "N_linear"):
        print(f"\n  {name} = {getattr(symbols, name)}")
    print()
    print("Scale-factor volume-log form:")
    print(f"  N_scale = zeta/d = {symbols.N_scale}")
    print()
    print("Metric-coefficient volume-log form:")
    print(f"  N_metric = 2*zeta/d = {symbols.N_metric}")
    print()
    print("Per-dimension zeta scale form:")
    print(f"  N_perdim_scale = zeta_pd = {symbols.N_perdim_scale}")
    print()
    print("Per-dimension zeta metric form:")
    print(f"  N_perdim_metric = 2*zeta_pd = {symbols.N_perdim_metric}")
    print()
    print("Scale/metric difference:")
    print(f"  Delta_scale_metric = N_metric - N_scale = {symbols.Delta_scale_metric}")
    print()
    print("Candidate-form load:")
    print(f"  L_candidate_forms = {symbols.L_candidate_forms}")
    print()
    print("Forbidden-selection load:")
    print(f"  L_selection_forbidden = {symbols.L_selection_forbidden}")
    with out.derived_results():
        out.line(
            "candidate forms stated",
            StatusMark.OBLIGATION,
            f"N_scale={symbols.N_scale}; N_metric={symbols.N_metric}; Delta={symbols.Delta_scale_metric}",
        )
    if ns is not None:
        ns.record_derivation(
            derivation_id="g33_candidate_form_scale_metric_difference",
            inputs=[symbols.zeta, symbols.d],
            output=symbols.Delta_scale_metric,
            method="simplify(2*zeta/d - zeta/d)",
            status=Status.DERIVED,
            record_kind=RecordKind.DERIVATION,
            result_type="candidate_form_difference",
        )


def case_2_identity_checks(out: ScriptOutput, symbols: CandidateFormSymbols, ns=None):
    header("Case 2: Candidate-form identity checks")
    zeta, zeta_pd, d = symbols.zeta, symbols.zeta_pd, symbols.d

    scale_residual = sp.simplify(d * symbols.N_scale - zeta)
    metric_residual = sp.simplify(d * symbols.N_metric - 2 * zeta)
    perdim_scale_residual = sp.simplify(symbols.N_perdim_scale - zeta_pd)
    perdim_metric_residual = sp.simplify(symbols.N_perdim_metric - 2 * zeta_pd)

    print("Scale-factor total volume-log residual:")
    print(f"  d*(zeta/d) - zeta = {scale_residual}")
    print()
    print("Metric-coefficient total volume-log residual:")
    print(f"  d*(2*zeta/d) - 2*zeta = {metric_residual}")
    print()
    print("Per-dimension scale residual:")
    print(f"  zeta_pd - zeta_pd = {perdim_scale_residual}")
    print()
    print("Per-dimension metric residual:")
    print(f"  2*zeta_pd - 2*zeta_pd = {perdim_metric_residual}")

    with out.derived_results():
        out.line(
            "scale-factor total trace identity",
            StatusMark.PASS if is_zero(scale_residual) else StatusMark.FAIL,
            f"residual = {scale_residual}",
        )
        out.line(
            "metric-coefficient total trace identity",
            StatusMark.PASS if is_zero(metric_residual) else StatusMark.FAIL,
            f"residual = {metric_residual}",
        )
        out.line(
            "per-dimension scale identity",
            StatusMark.PASS if is_zero(perdim_scale_residual) else StatusMark.FAIL,
            f"residual = {perdim_scale_residual}",
        )
        out.line(
            "per-dimension metric identity",
            StatusMark.PASS if is_zero(perdim_metric_residual) else StatusMark.FAIL,
            f"residual = {perdim_metric_residual}",
        )

    if ns is not None:
        ns.record_derivation(
            derivation_id="g33_candidate_form_scale_trace_residual",
            inputs=[symbols.N_scale, zeta, d],
            output=scale_residual,
            method="simplify(d*(zeta/d) - zeta)",
            status=Status.DERIVED if is_zero(scale_residual) else Status.FAILED,
            record_kind=RecordKind.DERIVATION,
            result_type="identity_residual",
        )
        ns.record_derivation(
            derivation_id="g33_candidate_form_metric_trace_residual",
            inputs=[symbols.N_metric, zeta, d],
            output=metric_residual,
            method="simplify(d*(2*zeta/d) - 2*zeta)",
            status=Status.DERIVED if is_zero(metric_residual) else Status.FAILED,
            record_kind=RecordKind.DERIVATION,
            result_type="identity_residual",
        )


def case_3_candidate_forms(out: ScriptOutput, forms: List[CandidateForm]):
    header("Case 3: Visible candidate normalization forms")
    for item in forms:
        subheader(item.name)
        print(f"Convention: {item.convention}")
        print(f"Candidate form: {item.candidate_form}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Requires: {item.requires}")
        print(f"Scope: {item.scope}")
        print(f"Not equivalent to: {item.not_equivalent_to}")
        print(f"Next test: {item.next_test}")
    with out.governance_assessments():
        out.line(
            "visible candidate normalization forms stated",
            StatusMark.DEFER,
            f"{len(forms)} candidate forms stated; none selected or adopted",
        )


def case_4_comparisons(out: ScriptOutput, comparisons: List[FormComparison]):
    header("Case 4: Candidate-form comparisons")
    for item in comparisons:
        subheader(item.name)
        print(f"Comparison: {item.comparison}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Result: {item.result}")
        print(f"Boundary: {item.boundary}")
    with out.governance_assessments():
        out.line(
            "candidate-form comparisons stated",
            StatusMark.OBLIGATION,
            f"{len(comparisons)} comparisons stated before compatibility sieve",
        )


def case_5_rules(out: ScriptOutput, rules: List[FormRule]):
    header("Case 5: Candidate-form no-overclaim rules")
    for item in rules:
        subheader(item.name)
        print(f"Rule: {item.rule}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Reason: {item.reason}")
    with out.governance_assessments():
        out.line(
            "candidate-form no-overclaim rules stated",
            StatusMark.OBLIGATION,
            f"{len(rules)} rules stated",
        )


def case_6_obligations(out: ScriptOutput, obligations: List[FormObligation]):
    header("Case 6: Candidate-form obligations")
    for item in obligations:
        subheader(item.name)
        print(f"Obligation: {item.obligation}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Blocks: {item.blocks}")
        print(f"Discipline: {item.discipline}")
    with out.unresolved_obligations():
        out.line(
            "candidate-form obligations opened",
            StatusMark.OBLIGATION,
            f"{len(obligations)} obligations stated",
        )


def case_7_conclusions(out: ScriptOutput, conclusions: List[FormConclusion]):
    header("Case 7: Candidate-form conclusions")
    for item in conclusions:
        subheader(item.name)
        print(f"Conclusion: {item.conclusion}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Meaning: {item.meaning}")
    with out.governance_assessments():
        out.line(
            "trace-normalization candidate-form conclusion stated",
            StatusMark.PASS,
            "visible forms stated; no normalization selected or adopted; compatibility sieve should run next",
        )


def final_interpretation(out: ScriptOutput):
    header("Final interpretation")
    print("Trace-normalization candidate-form result:")
    print()
    print("  Visible candidate normalization forms are now stated.")
    print("  If zeta is total volume-log trace and B_s is a scale factor, log(B_s)=zeta/d.")
    print("  If zeta is total volume-log trace and B_s is a metric coefficient, log(B_s)=2*zeta/d.")
    print("  If zeta is per-dimension normalized, the dimension factor is already inside zeta.")
    print("  Linearized trace bookkeeping remains first-order only.")
    print("  These forms are convention-dependent candidates, not selected normalization.")
    print("  No trace-normalization rule is adopted or derived by this ledger.")
    print("  B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready.")
    print()
    print("Possible next script:")
    print("  candidate_trace_normalization_compatibility_sieve.py")
    print()
    print("Tiny goblin label:")
    print("  Put the cups on the table. Do not drink yet.")
    with out.governance_assessments():
        out.line(
            "trace-normalization candidate-form ledger complete",
            StatusMark.PASS,
            "compatibility sieve should run next; adoption and downstream gates remain closed",
        )


def record_inventory_marker(ns, symbols: CandidateFormSymbols) -> None:
    ns.record_derivation(
        derivation_id="g33_trace_normalization_candidate_forms",
        inputs=[symbols.N_trace],
        output=symbols.L_candidate_form_gap,
        method="candidate trace-normalization form ledger",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="candidate_forms_marker",
        is_placeholder=True,
    )


def record_governance(ns, forms: List[CandidateForm], comparisons: List[FormComparison], rules: List[FormRule]) -> None:
    obligation_ids = [
        "g33_form_obligation_b_s_notation_decision",
        "g33_form_obligation_zeta_notation_decision",
        "g33_form_obligation_traced_dimension_declaration",
        "g33_form_obligation_compatibility_sieve_next",
        "g33_form_obligation_adoption_boundary",
        "g33_form_obligation_downstream_gates",
    ]

    for item in forms:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_route(
            RouteRecord(
                route_id=f"g33_candidate_form_{ident}",
                script_id=SCRIPT_ID,
                name=item.name,
                status=GovernanceStatus.CANDIDATE_ROUTE,
                tier=ClaimTier.CONSTRAINED,
                required_obligations=obligation_ids,
                activation_conditions=[
                    item.convention,
                    f"Candidate form: {item.candidate_form}",
                    f"Requires: {item.requires}",
                    f"Scope: {item.scope}",
                    f"Not equivalent to: {item.not_equivalent_to}",
                ],
            )
        )

    for item in comparisons:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g33_form_comparison_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.POLICY_RULE if item.status == "REQUIRED" else GovernanceStatus.CANDIDATE_ROUTE,
                statement=f"{item.comparison}: {item.result}. Boundary: {item.boundary}.",
                derivation_ids=["g33_trace_normalization_candidate_forms"],
                obligation_ids=obligation_ids,
            )
        )

    for item in rules:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g33_form_rule_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.POLICY_RULE,
                statement=f"{item.rule}. Reason: {item.reason}.",
                derivation_ids=["g33_trace_normalization_candidate_forms"],
                obligation_ids=obligation_ids,
            )
        )


def record_obligations(ns, obligations: List[FormObligation]) -> None:
    for item in obligations:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_obligation(
            ProofObligationRecord(
                obligation_id=f"g33_form_obligation_{ident}",
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

    header("Candidate Trace-Normalization Candidate Forms")
    print_archive_status(ns, invalidated)

    symbols = build_symbols()
    forms = build_candidate_forms()
    comparisons = build_comparisons()
    rules = build_rules()
    obligations = build_obligations()
    conclusions = build_conclusions()

    case_0_problem(out)
    case_1_symbolic_forms(out, symbols, ns)
    case_2_identity_checks(out, symbols, ns)
    case_3_candidate_forms(out, forms)
    case_4_comparisons(out, comparisons)
    case_5_rules(out, rules)
    case_6_obligations(out, obligations)
    case_7_conclusions(out, conclusions)
    final_interpretation(out)

    record_inventory_marker(ns, symbols)
    record_governance(ns, forms, comparisons, rules)
    record_obligations(ns, obligations)

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
