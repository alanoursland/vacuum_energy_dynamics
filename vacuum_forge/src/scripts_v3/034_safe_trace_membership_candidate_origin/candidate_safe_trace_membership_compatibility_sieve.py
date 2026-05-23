# Candidate safe trace membership compatibility sieve
#
# Group:
#   34_safe_trace_membership_candidate_origin
#
# Human title:
#   Safe Trace Membership Candidate Origin
#
# Script type:
#   COMPATIBILITY SIEVE
#
# Purpose
# -------
# Filter visible candidate membership forms for zeta_Bs -> T_zeta after the
# domain ledger, selector firewall, and candidate-form ledger.
#
# Locked-door question:
#
#   Which safe-membership candidate forms survive compatibility filters,
#   without selecting, adopting, or deriving safe membership?
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
#   Shake the shelves. Do not shelve the cup yet.

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
        "COMPATIBLE_IF_DECLARED": StatusMark.INFO,
        "COMPATIBILITY_ONLY": StatusMark.INFO,
        "CONVENTION_DEPENDENT": StatusMark.DEFER,
        "FILTER_FAIL": StatusMark.FAIL,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "NOT_SELECTED": StatusMark.INFO,
        "OPEN": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REQUIRED": StatusMark.OBLIGATION,
        "TYPED_IF_DECLARED": StatusMark.INFO,
        "VALID_IF_INERT": StatusMark.INFO,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g34_candidate_forms",
            "034_safe_trace_membership_candidate_origin__candidate_safe_trace_membership_candidate_forms",
            "g34_safe_membership_candidate_forms",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g34_selector_firewall",
            "034_safe_trace_membership_candidate_origin__candidate_safe_trace_membership_selector_rejection",
            "g34_safe_membership_selector_rejection",
            RecordKind.INVENTORY_MARKER,
        ),
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
class CompatibilitySymbols:
    zeta_Bs: sp.Symbol
    T_zeta: sp.Symbol
    D_Bs: sp.Symbol
    C_Tzeta: sp.Symbol
    M_typed: sp.Symbol
    M_role_pure: sp.Symbol
    M_diag: sp.Symbol
    M_norm_compat: sp.Symbol
    F_source_visible: sp.Symbol
    F_div_visible: sp.Symbol
    F_residual_zone: sp.Symbol
    F_normalization: sp.Symbol
    F_typed_domain: sp.Symbol
    ambiguous_domain: sp.Symbol
    hidden_source: sp.Symbol
    hidden_divergence: sp.Symbol
    residual_payload: sp.Symbol
    membership_collapse: sp.Symbol
    downstream_use: sp.Symbol
    P_trace_norm: sp.Symbol
    P_incidence_zero: sp.Symbol
    P_active_O: sp.Symbol
    P_residual_kill: sp.Symbol
    P_insertion: sp.Symbol
    P_parent: sp.Symbol
    L_surviving_forms: sp.Expr
    L_filter_load: sp.Expr
    L_failure_modes: sp.Expr
    L_downstream_gates: sp.Expr
    L_compatibility_gap: sp.Expr


@dataclass
class CompatibilityResult:
    name: str
    form: str
    status: str
    survives_if: str
    filter_result: str
    still_open: str
    forbidden_upgrade: str


@dataclass
class FailureMode:
    name: str
    failure: str
    status: str
    reason: str
    consequence: str


@dataclass
class RuleEntry:
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


def build_symbols() -> CompatibilitySymbols:
    zeta_Bs, T_zeta, D_Bs, C_Tzeta = sp.symbols("zeta_Bs T_zeta D_Bs C_Tzeta")
    M_typed, M_role_pure, M_diag, M_norm_compat = sp.symbols(
        "M_typed M_role_pure M_diag M_norm_compat"
    )
    F_source_visible, F_div_visible, F_residual_zone, F_normalization, F_typed_domain = sp.symbols(
        "F_source_visible F_div_visible F_residual_zone F_normalization F_typed_domain"
    )
    ambiguous_domain, hidden_source, hidden_divergence, residual_payload = sp.symbols(
        "ambiguous_domain hidden_source hidden_divergence residual_payload"
    )
    membership_collapse, downstream_use = sp.symbols("membership_collapse downstream_use")
    P_trace_norm, P_incidence_zero, P_active_O, P_residual_kill, P_insertion, P_parent = sp.symbols(
        "P_trace_norm P_incidence_zero P_active_O P_residual_kill P_insertion P_parent"
    )

    L_surviving_forms = sp.simplify(M_typed + M_role_pure + M_diag + M_norm_compat)
    L_filter_load = sp.simplify(
        F_source_visible + F_div_visible + F_residual_zone + F_normalization + F_typed_domain
    )
    L_failure_modes = sp.simplify(
        ambiguous_domain + hidden_source + hidden_divergence + residual_payload + membership_collapse + downstream_use
    )
    L_downstream_gates = sp.simplify(P_active_O + P_residual_kill + P_insertion + P_parent)
    L_compatibility_gap = sp.simplify(
        L_surviving_forms
        + L_filter_load
        + L_failure_modes
        + L_downstream_gates
        + P_trace_norm
        + P_incidence_zero
        + zeta_Bs
        + T_zeta
        + D_Bs
        + C_Tzeta
    )

    return CompatibilitySymbols(
        zeta_Bs=zeta_Bs,
        T_zeta=T_zeta,
        D_Bs=D_Bs,
        C_Tzeta=C_Tzeta,
        M_typed=M_typed,
        M_role_pure=M_role_pure,
        M_diag=M_diag,
        M_norm_compat=M_norm_compat,
        F_source_visible=F_source_visible,
        F_div_visible=F_div_visible,
        F_residual_zone=F_residual_zone,
        F_normalization=F_normalization,
        F_typed_domain=F_typed_domain,
        ambiguous_domain=ambiguous_domain,
        hidden_source=hidden_source,
        hidden_divergence=hidden_divergence,
        residual_payload=residual_payload,
        membership_collapse=membership_collapse,
        downstream_use=downstream_use,
        P_trace_norm=P_trace_norm,
        P_incidence_zero=P_incidence_zero,
        P_active_O=P_active_O,
        P_residual_kill=P_residual_kill,
        P_insertion=P_insertion,
        P_parent=P_parent,
        L_surviving_forms=L_surviving_forms,
        L_filter_load=L_filter_load,
        L_failure_modes=L_failure_modes,
        L_downstream_gates=L_downstream_gates,
        L_compatibility_gap=L_compatibility_gap,
    )


def build_results() -> List[CompatibilityResult]:
    return [
        CompatibilityResult(
            name="C1: typed trace-sector assignment",
            form="zeta_Bs is assigned to T_zeta with declared D_Bs and C_Tzeta",
            status="COMPATIBLE_IF_DECLARED",
            survives_if="zeta_Bs object, T_zeta sector, domain, codomain, and membership criterion are declared before use",
            filter_result="passes typed-domain visibility and remains compatible if it carries no residual/source/correction payload",
            still_open="does not prove zeta_Bs belongs to T_zeta and does not decide incidence",
            forbidden_upgrade="must not be selected merely because the labels are declared",
        ),
        CompatibilityResult(
            name="C2: role-pure trace-payload assignment",
            form="zeta_Bs belongs to T_zeta only as trace-sector payload",
            status="COMPATIBLE_IF_DECLARED",
            survives_if="residual, ordinary-source, correction/divergence, and downstream payloads remain excluded",
            filter_result="passes anti-smuggling filters as a candidate role-pure membership form",
            still_open="does not derive full source no-double-counting, divergence safety, or residual non-entry",
            forbidden_upgrade="must not be promoted into residual kill or zero-incidence theorem",
        ),
        CompatibilityResult(
            name="C3: normalization-compatible membership",
            form="membership is compatible with separately declared N_trace",
            status="COMPATIBILITY_ONLY",
            survives_if="Group 33 trace-normalization convention is declared separately and does not choose membership",
            filter_result="allowed only as Package B component compatibility",
            still_open="normalization and membership remain independent candidate nodes",
            forbidden_upgrade="must not collapse Package B into one postulate",
        ),
        CompatibilityResult(
            name="C4: diagnostic-only trace label",
            form="zeta_Bs is labeled as T_zeta for audit only",
            status="VALID_IF_INERT",
            survives_if="label has no source, metric, residual, insertion, parent, or equation-modifying effect",
            filter_result="safe diagnostic fallback if strictly inert",
            still_open="does not provide active membership for downstream use",
            forbidden_upgrade="must not be treated as adopted membership or insertable trace sector",
        ),
    ]


def build_failures() -> List[FailureMode]:
    return [
        FailureMode(
            name="F1: undeclared membership objects",
            failure="membership form omits zeta_Bs, T_zeta, domain, codomain, or criterion",
            status="FILTER_FAIL",
            reason="typed membership requires visible objects before filtering",
            consequence="membership remains a label, not a testable form",
        ),
        FailureMode(
            name="F2: residual payload",
            failure="membership form includes R_zeta or R_kappa payload",
            status="FILTER_FAIL",
            reason="membership is not residual control",
            consequence="form smuggles residual kill or incidence",
        ),
        FailureMode(
            name="F3: hidden ordinary source load",
            failure="membership form carries ordinary source load",
            status="FILTER_FAIL",
            reason="ordinary source load must remain visible and protected",
            consequence="form becomes hidden source pocket",
        ),
        FailureMode(
            name="F4: hidden divergence reservoir",
            failure="membership form carries hidden correction/divergence reservoir load",
            status="FILTER_FAIL",
            reason="divergence explicitness requires visible non-reservoir correction behavior",
            consequence="form becomes correction reservoir",
        ),
        FailureMode(
            name="F5: normalization collapse",
            failure="membership is chosen by trace normalization or chooses trace normalization",
            status="FILTER_FAIL",
            reason="P_trace_norm and P_safe_membership are separate Package B nodes",
            consequence="Package B collapses into one hidden choice",
        ),
        FailureMode(
            name="F6: downstream use",
            failure="membership form is treated as insertion, active O, residual control, or parent readiness",
            status="FILTER_FAIL",
            reason="downstream gates remain closed",
            consequence="candidate compatibility becomes theorem closure by shortcut",
        ),
    ]


def build_rules() -> List[RuleEntry]:
    return [
        RuleEntry(
            name="R1: compatible-if-declared is not selected",
            rule="A membership form that survives filters if declared is still not selected or adopted",
            status="POLICY_RULE",
            reason="compatibility sieve is weaker than theorem derivation or explicit choice",
        ),
        RuleEntry(
            name="R2: filters reject but do not choose",
            rule="source/divergence/normalization/residual filters may reject forms but cannot choose membership",
            status="POLICY_RULE",
            reason="negative filters are not origin derivations",
        ),
        RuleEntry(
            name="R3: typed-domain declaration is mandatory",
            rule="zeta_Bs, T_zeta, domain, codomain, and membership criterion must be declared before compatibility claims",
            status="REQUIRED",
            reason="a sector label alone is not proof of membership",
        ),
        RuleEntry(
            name="R4: normalization remains separate",
            rule="membership compatibility with N_trace does not derive normalization or membership",
            status="POLICY_RULE",
            reason="Package B components remain separate nodes",
        ),
        RuleEntry(
            name="R5: downstream gates remain closed",
            rule="surviving membership forms do not license insertion, active O, residual control, or parent closure",
            status="POLICY_RULE",
            reason="candidate-form compatibility is not downstream theorem closure",
        ),
    ]


def build_obligations() -> List[ObligationEntry]:
    return [
        ObligationEntry(
            name="O1: declare membership criterion",
            obligation="state the membership criterion for any typed zeta_Bs -> T_zeta form before use",
            status="OPEN",
            blocks="membership theorem attempt and status summary",
            discipline="compatible-if-declared is not selected",
        ),
        ObligationEntry(
            name="O2: preserve role purity",
            obligation="keep residual/source/correction payloads outside membership forms unless separately derived",
            status="OPEN",
            blocks="hidden-load smuggling",
            discipline="membership is not cleanup",
        ),
        ObligationEntry(
            name="O3: keep normalization separate",
            obligation="carry Group 33 trace-normalization forms as separate compatibility nodes only",
            status="OPEN",
            blocks="Package B collapse",
            discipline="membership is not normalization",
        ),
        ObligationEntry(
            name="O4: keep filters negative",
            obligation="use source/divergence/residual/normalization filters only to reject or flag forms",
            status="OPEN",
            blocks="selector drift",
            discipline="filter survival is not derivation",
        ),
        ObligationEntry(
            name="O5: adoption boundary",
            obligation="keep P_safe_membership unadopted unless a separate explicit decision is requested",
            status="OPEN",
            blocks="accidental adoption",
            discipline="compatibility sieve is not postulate selection",
        ),
        ObligationEntry(
            name="O6: downstream gates",
            obligation="keep insertion, active O, residual control, and parent equation closed",
            status="NOT_READY",
            blocks="downstream overreach",
            discipline="compatibility sieve is not insertion or parent closure",
        ),
    ]


def build_conclusions() -> List[ConclusionEntry]:
    return [
        ConclusionEntry(
            name="C1: typed forms survive if declared",
            conclusion="typed trace-sector and role-pure membership forms survive compatibility filters only with explicit declarations",
            status="COMPATIBLE_IF_DECLARED",
            meaning="both remain candidate forms; neither is selected",
        ),
        ConclusionEntry(
            name="C2: diagnostic fallback survives if inert",
            conclusion="diagnostic-only trace label remains safe only if strictly equation-inert",
            status="VALID_IF_INERT",
            meaning="diagnostic label is not adopted membership or insertion",
        ),
        ConclusionEntry(
            name="C3: invalid payloads fail",
            conclusion="residual/source/correction payloads, normalization collapse, and downstream use fail the sieve",
            status="REQUIRED",
            meaning="membership cannot smuggle hidden load or downstream closure",
        ),
        ConclusionEntry(
            name="C4: no selection",
            conclusion="this compatibility sieve selects no final membership form",
            status="NOT_SELECTED",
            meaning="filter survival is not selection, adoption, or theorem derivation",
        ),
        ConclusionEntry(
            name="C5: downstream gates",
            conclusion="B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready",
            status="NOT_READY",
            meaning="compatibility sieve does not open downstream gates",
        ),
        ConclusionEntry(
            name="C6: next",
            conclusion="safe-membership obligations or status summary should run next",
            status="OPEN",
            meaning="the group can summarize surviving forms and unresolved membership decisions without adopting",
        ),
    ]


def case_0_problem(out: ScriptOutput) -> None:
    header("Case 0: Safe-membership compatibility-sieve problem")
    print("Question:\n")
    print("  Which safe-membership candidate forms survive compatibility filters,")
    print("  without selecting, adopting, or deriving safe membership?\n")
    print("Discipline:\n")
    print("  This script applies compatibility filters.")
    print("  It adopts no safe-membership postulate.")
    print("  It selects no final membership form.")
    print("  It derives no safe-membership theorem.")
    print("  It derives no trace/residual zero incidence.")
    print("  It derives no coefficient law and no insertion.")
    print("  It keeps active O, residual control, and parent closure closed.\n")
    print("Tiny goblin rule:")
    print("  Shake the shelves. Do not shelve the cup yet.\n")

    with out.governance_assessments():
        out.line(
            "safe-membership compatibility sieve opened",
            StatusMark.INFO,
            "visible membership forms are filtered without selecting or adopting safe membership",
        )


def case_1_symbolic_loads(out: ScriptOutput, symbols: CompatibilitySymbols, ns=None) -> None:
    header("Case 1: Compatibility-sieve symbolic ledger")
    print("Candidate / filter symbols:\n")
    for sym in (
        symbols.zeta_Bs,
        symbols.T_zeta,
        symbols.D_Bs,
        symbols.C_Tzeta,
        symbols.M_typed,
        symbols.M_role_pure,
        symbols.M_diag,
        symbols.M_norm_compat,
        symbols.F_source_visible,
        symbols.F_div_visible,
        symbols.F_residual_zone,
        symbols.F_normalization,
        symbols.F_typed_domain,
    ):
        print(f"  {sym} = {sym}")
    print()
    print(f"Surviving-form load:\n  L_surviving_forms = {symbols.L_surviving_forms}\n")
    print(f"Compatibility-filter load:\n  L_filter_load = {symbols.L_filter_load}\n")
    print(f"Failure-mode load:\n  L_failure_modes = {symbols.L_failure_modes}\n")
    print(f"Downstream gate load:\n  L_downstream_gates = {symbols.L_downstream_gates}\n")
    print(f"Compatibility gap:\n  L_compatibility_gap = {symbols.L_compatibility_gap}\n")

    with out.derived_results():
        out.line(
            "safe-membership compatibility loads stated",
            StatusMark.OBLIGATION,
            f"L_surviving_forms={symbols.L_surviving_forms}; L_failure_modes={symbols.L_failure_modes}",
        )

    if ns is not None:
        ns.record_derivation(
            derivation_id="g34_safe_membership_compatibility_symbolic_loads",
            inputs=[symbols.zeta_Bs, symbols.T_zeta, symbols.D_Bs, symbols.C_Tzeta],
            output=symbols.L_compatibility_gap,
            method="symbolic compatibility-sieve load bookkeeping",
            status=Status.DERIVED,
            record_kind=RecordKind.DERIVATION,
            result_type="symbolic_load",
        )


def case_2_results(out: ScriptOutput, results: List[CompatibilityResult]) -> None:
    header("Case 2: Candidate membership compatibility results")
    for item in results:
        subheader(item.name)
        print(f"Form: {item.form}")
        with out.governance_assessments():
            out.line(item.name, status_mark(item.status), item.status)
        print(f"Survives if: {item.survives_if}")
        print(f"Filter result: {item.filter_result}")
        print(f"Still open: {item.still_open}")
        print(f"Forbidden upgrade: {item.forbidden_upgrade}")

    with out.governance_assessments():
        out.line(
            "candidate membership forms filtered",
            StatusMark.DEFER,
            "forms survive conditionally; none selected or adopted",
        )


def case_3_failures(out: ScriptOutput, failures: List[FailureMode]) -> None:
    header("Case 3: Compatibility failure modes")
    for item in failures:
        subheader(item.name)
        print(f"Failure: {item.failure}")
        with out.counterexamples():
            out.line(item.name, status_mark(item.status), item.status)
        print(f"Reason: {item.reason}")
        print(f"Consequence: {item.consequence}")

    with out.counterexamples():
        out.line(
            "safe-membership compatibility failure modes stated",
            StatusMark.FAIL,
            "undeclared objects, hidden payloads, Package B collapse, and downstream use fail the sieve",
        )


def case_4_rules(out: ScriptOutput, rules: List[RuleEntry]) -> None:
    header("Case 4: Compatibility-sieve no-overclaim rules")
    for item in rules:
        subheader(item.name)
        print(f"Rule: {item.rule}")
        with out.governance_assessments():
            out.line(item.name, status_mark(item.status), item.status)
        print(f"Reason: {item.reason}")

    with out.governance_assessments():
        out.line("safe-membership compatibility no-overclaim rules stated", StatusMark.OBLIGATION, "5 rules stated")


def case_5_obligations(out: ScriptOutput, obligations: List[ObligationEntry]) -> None:
    header("Case 5: Compatibility-sieve obligations")
    for item in obligations:
        subheader(item.name)
        print(f"Obligation: {item.obligation}")
        with out.unresolved_obligations():
            out.line(item.name, status_mark(item.status), item.status)
        print(f"Blocks: {item.blocks}")
        print(f"Discipline: {item.discipline}")

    with out.unresolved_obligations():
        out.line("safe-membership compatibility obligations opened", StatusMark.OBLIGATION, "6 obligations stated")


def case_6_conclusions(out: ScriptOutput, conclusions: List[ConclusionEntry]) -> None:
    header("Case 6: Compatibility-sieve conclusions")
    for item in conclusions:
        subheader(item.name)
        print(f"Conclusion: {item.conclusion}")
        with out.governance_assessments():
            out.line(item.name, status_mark(item.status), item.status)
        print(f"Meaning: {item.meaning}")

    with out.governance_assessments():
        out.line(
            "safe-membership compatibility sieve conclusion stated",
            StatusMark.PASS,
            "forms survive conditionally; no membership selected or adopted; obligations/status summary should run next",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Safe-membership compatibility-sieve result:\n")
    print("  Typed trace-sector and role-pure membership forms survive only if their objects, types, and exclusion zones are declared.")
    print("  Normalization-compatible membership remains compatibility only and does not collapse Package B.")
    print("  Diagnostic-only trace labels remain safe only if strictly equation-inert.")
    print("  Undeclared objects, hidden source load, hidden divergence reservoirs, residual payloads, normalization collapse, and downstream use fail.")
    print("  Compatibility filters may reject or flag forms but cannot choose safe membership.")
    print("  No safe-membership theorem is selected, adopted, or derived by this sieve.")
    print("  B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready.\n")
    print("Possible next script:")
    print("  candidate_safe_trace_membership_obligations.py\n")
    print("Tiny goblin label:")
    print("  Shake the shelves. Do not shelve the cup yet.\n")

    with out.governance_assessments():
        out.line(
            "safe-membership compatibility sieve complete",
            StatusMark.PASS,
            "obligations/status summary should run next; adoption and downstream gates remain closed",
        )


def record_inventory_marker(ns, symbols: CompatibilitySymbols) -> None:
    ns.record_derivation(
        derivation_id="g34_safe_membership_compatibility_sieve",
        inputs=[symbols.zeta_Bs, symbols.T_zeta, symbols.D_Bs, symbols.C_Tzeta],
        output=symbols.L_compatibility_gap,
        method="safe-membership compatibility sieve",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="compatibility_sieve_marker",
        is_placeholder=True,
    )


def record_governance(ns, results: List[CompatibilityResult], failures: List[FailureMode], rules: List[RuleEntry]) -> None:
    obligation_ids = [
        "g34_membership_compat_obligation_o1",
        "g34_membership_compat_obligation_o2",
        "g34_membership_compat_obligation_o3",
        "g34_membership_compat_obligation_o4",
        "g34_membership_compat_obligation_o5",
        "g34_membership_compat_obligation_o6",
    ]

    for item in results:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_route(
            RouteRecord(
                route_id=f"g34_membership_compat_result_{ident}",
                script_id=SCRIPT_ID,
                name=item.name,
                status=GovernanceStatus.CANDIDATE_ROUTE,
                tier=ClaimTier.CONSTRAINED,
                required_obligations=obligation_ids,
                activation_conditions=[
                    item.form,
                    f"Survives if: {item.survives_if}",
                    f"Filter result: {item.filter_result}",
                    f"Still open: {item.still_open}",
                ],
            )
        )

    for item in failures:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g34_membership_compat_failure_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.REJECTED_ROUTE,
                statement=f"{item.failure}. Reason: {item.reason}. Consequence: {item.consequence}.",
                derivation_ids=["g34_safe_membership_compatibility_sieve"],
                obligation_ids=obligation_ids,
            )
        )

    for item in rules:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g34_membership_compat_rule_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.POLICY_RULE,
                statement=f"{item.rule}. Reason: {item.reason}.",
                derivation_ids=["g34_safe_membership_compatibility_sieve"],
                obligation_ids=obligation_ids,
            )
        )


def record_obligations(ns, obligations: List[ObligationEntry]) -> None:
    for item in obligations:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_obligation(
            ProofObligationRecord(
                obligation_id=f"g34_membership_compat_obligation_{ident}",
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

    header("Candidate Safe Trace Membership Compatibility Sieve")
    print_archive_status(ns, invalidated)

    symbols = build_symbols()
    results = build_results()
    failures = build_failures()
    rules = build_rules()
    obligations = build_obligations()
    conclusions = build_conclusions()

    case_0_problem(out)
    case_1_symbolic_loads(out, symbols, ns)
    case_2_results(out, results)
    case_3_failures(out, failures)
    case_4_rules(out, rules)
    case_5_obligations(out, obligations)
    case_6_conclusions(out, conclusions)
    final_interpretation(out)

    record_inventory_marker(ns, symbols)
    record_governance(ns, results, failures, rules)
    record_obligations(ns, obligations)

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
