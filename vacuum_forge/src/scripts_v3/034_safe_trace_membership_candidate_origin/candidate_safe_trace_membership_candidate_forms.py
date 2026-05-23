# Candidate safe trace membership candidate forms
#
# Group:
#   34_safe_trace_membership_candidate_origin
#
# Human title:
#   Safe Trace Membership Candidate Origin
#
# Script type:
#   LEDGER / CANDIDATE FORMS
#
# Purpose
# -------
# State visible candidate membership forms for zeta_Bs -> T_zeta after
# domain objects and selector fences have been declared.
#
# Locked-door question:
#
#   Which visible candidate forms for zeta_Bs -> T_zeta can be tested next,
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
#   Put the shelf labels on the table. Do not shelve the cup yet.

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
        "COMPATIBILITY_ONLY": StatusMark.INFO,
        "FILTER_FAIL": StatusMark.FAIL,
        "INVALID_FORM": StatusMark.FAIL,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REQUIRED": StatusMark.OBLIGATION,
        "TYPED_IF_DECLARED": StatusMark.INFO,
        "VISIBILITY_REQUIRED": StatusMark.OBLIGATION,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
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
class MembershipFormSymbols:
    zeta_Bs: sp.Symbol
    T_zeta: sp.Symbol
    D_Bs: sp.Symbol
    C_Tzeta: sp.Symbol
    M_typed: sp.Symbol
    M_role_pure: sp.Symbol
    M_diag: sp.Symbol
    M_norm_compat: sp.Symbol
    M_invalid_residual: sp.Symbol
    M_invalid_source: sp.Symbol
    M_invalid_correction: sp.Symbol
    M_invalid_incidence: sp.Symbol
    P_trace_norm: sp.Symbol
    P_incidence_zero: sp.Symbol
    P_active_O: sp.Symbol
    P_residual_kill: sp.Symbol
    P_insertion: sp.Symbol
    P_parent: sp.Symbol
    L_candidate_forms: sp.Expr
    L_invalid_forms: sp.Expr
    L_downstream_gates: sp.Expr
    L_form_gap: sp.Expr


@dataclass
class MembershipForm:
    name: str
    form: str
    status: str
    requires: str
    scope: str
    not_equivalent_to: str
    next_test: str


@dataclass
class InvalidForm:
    name: str
    form: str
    status: str
    reason: str
    failure_mode: str


@dataclass
class ComparisonEntry:
    name: str
    comparison: str
    status: str
    result: str
    boundary: str


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


def build_symbols() -> MembershipFormSymbols:
    zeta_Bs, T_zeta, D_Bs, C_Tzeta = sp.symbols("zeta_Bs T_zeta D_Bs C_Tzeta")
    M_typed, M_role_pure, M_diag, M_norm_compat = sp.symbols(
        "M_typed M_role_pure M_diag M_norm_compat"
    )
    M_invalid_residual, M_invalid_source, M_invalid_correction, M_invalid_incidence = sp.symbols(
        "M_invalid_residual M_invalid_source M_invalid_correction M_invalid_incidence"
    )
    P_trace_norm, P_incidence_zero, P_active_O, P_residual_kill, P_insertion, P_parent = sp.symbols(
        "P_trace_norm P_incidence_zero P_active_O P_residual_kill P_insertion P_parent"
    )

    L_candidate_forms = sp.simplify(M_typed + M_role_pure + M_diag + M_norm_compat)
    L_invalid_forms = sp.simplify(
        M_invalid_residual + M_invalid_source + M_invalid_correction + M_invalid_incidence
    )
    L_downstream_gates = sp.simplify(P_active_O + P_residual_kill + P_insertion + P_parent)
    L_form_gap = sp.simplify(
        zeta_Bs
        + T_zeta
        + D_Bs
        + C_Tzeta
        + P_trace_norm
        + P_incidence_zero
        + L_candidate_forms
        + L_invalid_forms
        + L_downstream_gates
    )

    return MembershipFormSymbols(
        zeta_Bs=zeta_Bs,
        T_zeta=T_zeta,
        D_Bs=D_Bs,
        C_Tzeta=C_Tzeta,
        M_typed=M_typed,
        M_role_pure=M_role_pure,
        M_diag=M_diag,
        M_norm_compat=M_norm_compat,
        M_invalid_residual=M_invalid_residual,
        M_invalid_source=M_invalid_source,
        M_invalid_correction=M_invalid_correction,
        M_invalid_incidence=M_invalid_incidence,
        P_trace_norm=P_trace_norm,
        P_incidence_zero=P_incidence_zero,
        P_active_O=P_active_O,
        P_residual_kill=P_residual_kill,
        P_insertion=P_insertion,
        P_parent=P_parent,
        L_candidate_forms=L_candidate_forms,
        L_invalid_forms=L_invalid_forms,
        L_downstream_gates=L_downstream_gates,
        L_form_gap=L_form_gap,
    )


def build_membership_forms() -> List[MembershipForm]:
    return [
        MembershipForm(
            name="F1: typed trace-sector assignment",
            form="zeta_Bs is assigned to T_zeta with declared domain D_Bs and codomain C_Tzeta",
            status="CANDIDATE_FORM",
            requires="zeta_Bs object, T_zeta sector, D_Bs domain, and C_Tzeta codomain are declared before use",
            scope="typed membership candidate",
            not_equivalent_to="trace-normalization choice, incidence theorem, residual kill, insertion, or parent closure",
            next_test="test domain/codomain consistency and exclusion-zone compatibility",
        ),
        MembershipForm(
            name="F2: role-pure trace-payload assignment",
            form="zeta_Bs belongs to T_zeta only as trace-sector payload, not as residual/source/correction payload",
            status="CANDIDATE_FORM",
            requires="residual, ordinary-source, and correction/divergence zones are excluded from membership payload",
            scope="anti-smuggling membership candidate",
            not_equivalent_to="source no-double-counting theorem, divergence-safe law, or residual-control theorem",
            next_test="filter against hidden source, hidden divergence, and residual-zone leakage",
        ),
        MembershipForm(
            name="F3: normalization-compatible membership assignment",
            form="zeta_Bs -> T_zeta is compatible with a separately declared N_trace convention",
            status="COMPATIBILITY_ONLY",
            requires="Group 33 compatible-if-declared trace-normalization form is carried as a separate node",
            scope="Package B component-compatibility candidate",
            not_equivalent_to="normalization selecting membership or membership selecting normalization",
            next_test="verify Package B nodes remain separate in compatibility sieve",
        ),
        MembershipForm(
            name="F4: diagnostic-only trace label",
            form="zeta_Bs is labeled as T_zeta for audit without modifying equations",
            status="TYPED_IF_DECLARED",
            requires="label has no source, metric, residual, insertion, or parent effect",
            scope="safe diagnostic fallback",
            not_equivalent_to="adopted membership postulate or insertable trace sector",
            next_test="distinguish diagnostic label from active membership used downstream",
        ),
    ]


def build_invalid_forms() -> List[InvalidForm]:
    return [
        InvalidForm(
            name="X1: residual-inclusive membership",
            form="T_zeta membership includes R_zeta or R_kappa payload",
            status="INVALID_FORM",
            reason="membership is not residual control and cannot erase residual zones",
            failure_mode="safe membership becomes residual kill or zero-incidence by implication",
        ),
        InvalidForm(
            name="X2: source-inclusive membership",
            form="T_zeta membership carries ordinary source load",
            status="INVALID_FORM",
            reason="ordinary source load must remain visible and protected outside membership",
            failure_mode="membership becomes hidden source pocket",
        ),
        InvalidForm(
            name="X3: correction-inclusive membership",
            form="T_zeta membership carries hidden correction/divergence reservoir load",
            status="INVALID_FORM",
            reason="divergence explicitness requires correction load to remain visible and non-reservoir",
            failure_mode="membership becomes divergence reservoir",
        ),
        InvalidForm(
            name="X4: incidence-by-membership form",
            form="zeta_Bs -> T_zeta is written as if it implies I(T_zeta,R_zeta)=0 or I(T_zeta,R_kappa)=0",
            status="INVALID_FORM",
            reason="zero incidence is high-risk and separate from membership",
            failure_mode="membership smuggles no-overlap/residual-control theorem",
        ),
        InvalidForm(
            name="X5: insertion-ready membership form",
            form="zeta_Bs -> T_zeta is treated as B_s/F_zeta insertion-ready membership",
            status="INVALID_FORM",
            reason="insertion is downstream and not ready",
            failure_mode="candidate form opens metric insertion by naming membership",
        ),
    ]


def build_comparisons() -> List[ComparisonEntry]:
    return [
        ComparisonEntry(
            name="T1: typed assignment versus sector label",
            comparison="declared zeta_Bs -> T_zeta assignment versus bare T_zeta label",
            status="VISIBILITY_REQUIRED",
            result="a sector label alone is not proof of membership",
            boundary="membership object, domain, codomain, and criterion must be visible",
        ),
        ComparisonEntry(
            name="T2: role-pure versus hidden payload",
            comparison="trace payload only versus residual/source/correction payload",
            status="VISIBILITY_REQUIRED",
            result="role-pure membership can be tested; hidden payload forms fail",
            boundary="role-purity is not full source/divergence/residual theorem",
        ),
        ComparisonEntry(
            name="T3: normalization compatibility versus collapse",
            comparison="membership compatible with N_trace versus membership chosen by N_trace",
            status="COMPATIBILITY_ONLY",
            result="compatibility is allowed, collapse is forbidden",
            boundary="Package B keeps normalization and membership separate",
        ),
        ComparisonEntry(
            name="T4: diagnostic label versus active downstream use",
            comparison="diagnostic membership label versus insertable membership rule",
            status="TYPED_IF_DECLARED",
            result="diagnostic labels are safer than active downstream membership use",
            boundary="diagnostic label is not insertion, active O, residual control, or parent readiness",
        ),
    ]


def build_rules() -> List[RuleEntry]:
    return [
        RuleEntry(
            name="R1: candidate form is not selection",
            rule="Listing a membership form does not select safe membership",
            status="POLICY_RULE",
            reason="candidate-form ledger is weaker than adoption or theorem derivation",
        ),
        RuleEntry(
            name="R2: typed label is not proof",
            rule="A label T_zeta does not prove zeta_Bs belongs to T_zeta",
            status="POLICY_RULE",
            reason="domain, codomain, object, and criterion must be explicit",
        ),
        RuleEntry(
            name="R3: membership is not normalization",
            rule="Candidate membership forms do not choose N_trace and are not chosen by N_trace",
            status="POLICY_RULE",
            reason="normalization and safe membership remain separate Package B components",
        ),
        RuleEntry(
            name="R4: membership is not incidence",
            rule="Candidate membership forms must not imply zero trace/residual incidence",
            status="POLICY_RULE",
            reason="incidence remains high-risk and separate",
        ),
        RuleEntry(
            name="R5: membership is not insertion",
            rule="No candidate membership form licenses B_s/F_zeta insertion, active O, residual control, or parent closure",
            status="POLICY_RULE",
            reason="downstream gates remain closed",
        ),
    ]


def build_obligations() -> List[ObligationEntry]:
    return [
        ObligationEntry(
            name="O1: membership forms visible",
            obligation="state candidate membership forms before compatibility filtering",
            status="OPEN",
            blocks="compatibility sieve",
            discipline="forms first, filters second",
        ),
        ObligationEntry(
            name="O2: typed-object declaration",
            obligation="declare zeta_Bs, T_zeta, domain, codomain, and membership criterion",
            status="OPEN",
            blocks="typed membership claims",
            discipline="label is not proof",
        ),
        ObligationEntry(
            name="O3: role-purity fence",
            obligation="keep residual/source/correction payloads outside membership forms",
            status="OPEN",
            blocks="hidden-load smuggling",
            discipline="membership is not cleanup",
        ),
        ObligationEntry(
            name="O4: normalization separation",
            obligation="keep membership forms separate from Group 33 trace-normalization forms",
            status="OPEN",
            blocks="Package B collapse",
            discipline="membership is not normalization",
        ),
        ObligationEntry(
            name="O5: adoption boundary",
            obligation="keep P_safe_membership unadopted unless a separate explicit decision is requested",
            status="OPEN",
            blocks="accidental adoption",
            discipline="candidate form is not adopted postulate",
        ),
        ObligationEntry(
            name="O6: downstream gates",
            obligation="keep insertion, active O, residual control, and parent equation closed",
            status="NOT_READY",
            blocks="downstream overreach",
            discipline="candidate-form ledger is not insertion or parent closure",
        ),
    ]


def build_conclusions() -> List[ConclusionEntry]:
    return [
        ConclusionEntry(
            name="C1: membership forms visible",
            conclusion="typed, role-pure, normalization-compatible, and diagnostic-only membership forms are stated",
            status="CANDIDATE_FORM",
            meaning="membership no longer hides in prose",
        ),
        ConclusionEntry(
            name="C2: invalid forms fenced",
            conclusion="residual-inclusive, source-inclusive, correction-inclusive, incidence-by-membership, and insertion-ready forms fail",
            status="REQUIRED",
            meaning="membership cannot smuggle residual control, hidden load, incidence, or insertion",
        ),
        ConclusionEntry(
            name="C3: no derivation",
            conclusion="this ledger derives no safe-membership theorem",
            status="NOT_DERIVED",
            meaning="candidate forms are visible options, not proof",
        ),
        ConclusionEntry(
            name="C4: no adoption",
            conclusion="this ledger adopts no safe-membership postulate",
            status="NOT_ADOPTED",
            meaning="explicit decision remains separate",
        ),
        ConclusionEntry(
            name="C5: downstream gates",
            conclusion="B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready",
            status="NOT_READY",
            meaning="candidate-form comparison does not open downstream gates",
        ),
        ConclusionEntry(
            name="C6: next",
            conclusion="safe-membership compatibility sieve should run next",
            status="OPEN",
            meaning="visible forms can now be filtered without selecting by forbidden routes",
        ),
    ]


def case_0_problem(out: ScriptOutput) -> None:
    header("Case 0: Safe-membership candidate-form problem")
    print("Question:\n")
    print("  Which visible candidate forms for zeta_Bs -> T_zeta can be tested next,")
    print("  without selecting, adopting, or deriving safe membership?\n")
    print("Discipline:\n")
    print("  This script defines candidate membership forms.")
    print("  It adopts no safe-membership postulate.")
    print("  It selects no final membership form.")
    print("  It derives no safe-membership theorem.")
    print("  It derives no trace/residual zero incidence.")
    print("  It derives no coefficient law and no insertion.")
    print("  It keeps active O, residual control, and parent closure closed.\n")
    print("Tiny goblin rule:")
    print("  Put the shelf labels on the table. Do not shelve the cup yet.\n")

    with out.governance_assessments():
        out.line(
            "safe-membership candidate-form ledger opened",
            StatusMark.INFO,
            "visible forms are stated after selector firewall and before compatibility sieve",
        )


def case_1_symbolic_loads(out: ScriptOutput, symbols: MembershipFormSymbols, ns=None) -> None:
    header("Case 1: Membership-form symbolic ledger")
    print("Membership-form symbols:\n")
    for name in [
        "zeta_Bs",
        "T_zeta",
        "D_Bs",
        "C_Tzeta",
        "M_typed",
        "M_role_pure",
        "M_diag",
        "M_norm_compat",
        "M_invalid_residual",
        "M_invalid_source",
        "M_invalid_correction",
        "M_invalid_incidence",
        "P_trace_norm",
        "P_incidence_zero",
        "P_active_O",
        "P_residual_kill",
        "P_insertion",
        "P_parent",
    ]:
        print(f"  {name} = {getattr(symbols, name)}")

    print("\nCandidate membership-form load:")
    print(f"  L_candidate_forms = {symbols.L_candidate_forms}")
    print("\nInvalid-form load:")
    print(f"  L_invalid_forms = {symbols.L_invalid_forms}")
    print("\nDownstream gate load:")
    print(f"  L_downstream_gates = {symbols.L_downstream_gates}")
    print("\nMembership-form gap:")
    print(f"  L_form_gap = {symbols.L_form_gap}")

    with out.derived_results():
        out.line(
            "safe-membership candidate-form loads stated",
            StatusMark.OBLIGATION,
            f"L_candidate_forms = {symbols.L_candidate_forms}; L_invalid_forms = {symbols.L_invalid_forms}",
        )

    if ns is not None:
        ns.record_derivation(
            derivation_id="safe_membership_candidate_form_loads",
            inputs=[symbols.zeta_Bs, symbols.T_zeta, symbols.D_Bs, symbols.C_Tzeta],
            output=symbols.L_form_gap,
            method="symbolic ledger for visible candidate membership forms and invalid form loads",
            status=Status.DERIVED,
            record_kind=RecordKind.DERIVATION,
            result_type="membership_form_load",
        )


def case_2_candidate_forms(out: ScriptOutput, forms: List[MembershipForm]) -> None:
    header("Case 2: Visible candidate membership forms")
    for item in forms:
        subheader(item.name)
        print(f"Form: {item.form}")
        with out.governance_assessments():
            out.line(f"{item.name} -- {item.status}", status_mark(item.status))
        print(f"Requires: {item.requires}")
        print(f"Scope: {item.scope}")
        print(f"Not equivalent to: {item.not_equivalent_to}")
        print(f"Next test: {item.next_test}")

    with out.governance_assessments():
        out.line(
            "visible membership forms stated",
            StatusMark.DEFER,
            f"{len(forms)} candidate forms stated; none selected or adopted",
        )


def case_3_invalid_forms(out: ScriptOutput, invalids: List[InvalidForm]) -> None:
    header("Case 3: Invalid membership-form patterns")
    for item in invalids:
        subheader(item.name)
        print(f"Form: {item.form}")
        with out.counterexamples():
            out.line(f"{item.name} -- {item.status}", status_mark(item.status))
        print(f"Reason: {item.reason}")
        print(f"Failure mode: {item.failure_mode}")

    with out.counterexamples():
        out.line(
            "invalid membership-form patterns rejected",
            StatusMark.FAIL,
            "residual/source/correction/incidence/insertion smuggling forms fail",
        )


def case_4_comparisons(out: ScriptOutput, comparisons: List[ComparisonEntry]) -> None:
    header("Case 4: Membership-form comparisons")
    for item in comparisons:
        subheader(item.name)
        print(f"Comparison: {item.comparison}")
        with out.governance_assessments():
            out.line(f"{item.name} -- {item.status}", status_mark(item.status))
        print(f"Result: {item.result}")
        print(f"Boundary: {item.boundary}")

    with out.governance_assessments():
        out.line(
            "membership-form comparisons stated",
            StatusMark.OBLIGATION,
            f"{len(comparisons)} comparisons stated before compatibility sieve",
        )


def case_5_rules(out: ScriptOutput, rules: List[RuleEntry]) -> None:
    header("Case 5: Candidate-form no-overclaim rules")
    for item in rules:
        subheader(item.name)
        print(f"Rule: {item.rule}")
        with out.governance_assessments():
            out.line(f"{item.name} -- {item.status}", status_mark(item.status))
        print(f"Reason: {item.reason}")

    with out.governance_assessments():
        out.line(
            "safe-membership candidate-form no-overclaim rules stated",
            StatusMark.OBLIGATION,
            f"{len(rules)} rules stated",
        )


def case_6_obligations(out: ScriptOutput, obligations: List[ObligationEntry]) -> None:
    header("Case 6: Candidate-form obligations")
    for item in obligations:
        subheader(item.name)
        print(f"Obligation: {item.obligation}")
        with out.unresolved_obligations():
            out.line(f"{item.name} -- {item.status}", status_mark(item.status))
        print(f"Blocks: {item.blocks}")
        print(f"Discipline: {item.discipline}")

    with out.unresolved_obligations():
        out.line(
            "safe-membership candidate-form obligations opened",
            StatusMark.OBLIGATION,
            f"{len(obligations)} obligations stated",
        )


def case_7_conclusions(out: ScriptOutput, conclusions: List[ConclusionEntry]) -> None:
    header("Case 7: Candidate-form conclusions")
    for item in conclusions:
        subheader(item.name)
        print(f"Conclusion: {item.conclusion}")
        with out.governance_assessments():
            out.line(f"{item.name} -- {item.status}", status_mark(item.status))
        print(f"Meaning: {item.meaning}")

    with out.governance_assessments():
        out.line(
            "safe-membership candidate-form conclusion stated",
            StatusMark.PASS,
            "visible forms stated; no membership selected or adopted; compatibility sieve should run next",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Safe-membership candidate-form result:\n")
    print("  Visible candidate membership forms are now stated.")
    print("  Typed trace-sector assignment is a candidate form if zeta_Bs, T_zeta, domain, and codomain are declared.")
    print("  Role-pure trace-payload assignment is a candidate form if residual/source/correction zones remain excluded.")
    print("  Normalization-compatible membership is compatibility only and does not collapse Package B.")
    print("  Diagnostic-only trace labels remain a safe fallback only if they do not modify equations.")
    print("  Residual-inclusive, source-inclusive, correction-inclusive, incidence-by-membership, and insertion-ready forms fail.")
    print("  No safe-membership theorem is derived or adopted by this ledger.")
    print("  B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready.\n")
    print("Possible next script:")
    print("  candidate_safe_trace_membership_compatibility_sieve.py\n")
    print("Tiny goblin label:")
    print("  Put the shelf labels on the table. Do not shelve the cup yet.\n")

    with out.governance_assessments():
        out.line(
            "safe-membership candidate-form ledger complete",
            StatusMark.PASS,
            "compatibility sieve should run next; adoption and downstream gates remain closed",
        )


def record_inventory_marker(ns, symbols: MembershipFormSymbols) -> None:
    ns.record_derivation(
        derivation_id="g34_safe_membership_candidate_forms",
        inputs=[symbols.zeta_Bs, symbols.T_zeta, symbols.D_Bs, symbols.C_Tzeta],
        output=symbols.L_form_gap,
        method="safe-membership candidate-form ledger",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="candidate_forms_marker",
        is_placeholder=True,
    )


def record_governance(
    ns,
    forms: List[MembershipForm],
    invalids: List[InvalidForm],
    comparisons: List[ComparisonEntry],
    rules: List[RuleEntry],
) -> None:
    obligation_ids = [
        "g34_membership_form_obligation_o1",
        "g34_membership_form_obligation_o2",
        "g34_membership_form_obligation_o3",
        "g34_membership_form_obligation_o4",
        "g34_membership_form_obligation_o5",
        "g34_membership_form_obligation_o6",
    ]

    for item in forms:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_route(
            RouteRecord(
                route_id=f"g34_membership_form_{ident}",
                script_id=SCRIPT_ID,
                name=item.name,
                status=GovernanceStatus.CANDIDATE_ROUTE,
                tier=ClaimTier.CONSTRAINED,
                required_obligations=obligation_ids,
                activation_conditions=[
                    item.form,
                    f"Requires: {item.requires}",
                    f"Scope: {item.scope}",
                    f"Not equivalent to: {item.not_equivalent_to}",
                ],
            )
        )

    for item in invalids:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g34_invalid_membership_form_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.REJECTED_ROUTE,
                statement=f"{item.form}. Invalid form: {item.reason}. Failure mode: {item.failure_mode}.",
                derivation_ids=["g34_safe_membership_candidate_forms"],
                obligation_ids=obligation_ids,
            )
        )

    for item in comparisons:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g34_membership_comparison_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.POLICY_RULE,
                statement=f"{item.comparison}. Result: {item.result}. Boundary: {item.boundary}.",
                derivation_ids=["g34_safe_membership_candidate_forms"],
                obligation_ids=obligation_ids,
            )
        )

    for item in rules:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g34_membership_form_rule_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.POLICY_RULE,
                statement=f"{item.rule}. Reason: {item.reason}.",
                derivation_ids=["g34_safe_membership_candidate_forms"],
                obligation_ids=obligation_ids,
            )
        )


def record_obligations(ns, obligations: List[ObligationEntry]) -> None:
    for item in obligations:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_obligation(
            ProofObligationRecord(
                obligation_id=f"g34_membership_form_obligation_{ident}",
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

    header("Candidate Safe Trace Membership Candidate Forms")
    print_archive_status(ns, invalidated)

    symbols = build_symbols()
    forms = build_membership_forms()
    invalids = build_invalid_forms()
    comparisons = build_comparisons()
    rules = build_rules()
    obligations = build_obligations()
    conclusions = build_conclusions()

    case_0_problem(out)
    case_1_symbolic_loads(out, symbols, ns)
    case_2_candidate_forms(out, forms)
    case_3_invalid_forms(out, invalids)
    case_4_comparisons(out, comparisons)
    case_5_rules(out, rules)
    case_6_obligations(out, obligations)
    case_7_conclusions(out, conclusions)
    final_interpretation(out)

    record_inventory_marker(ns, symbols)
    record_governance(ns, forms, invalids, comparisons, rules)
    record_obligations(ns, obligations)

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
