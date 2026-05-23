# Candidate Trace Anchor Joint Consistency Matrix
#
# Group:
#   35_trace_anchor_joint_declaration_inventory
#
# Human title:
#   Trace Anchor Joint Declaration Inventory
#
# Script type:
#   JOINT CONSISTENCY MATRIX
#
# Purpose
# -------
# Test declaration combinations for coherence before any trace-anchor component
# is selected, adopted, derived, or used downstream.
#
# This script does not fill declaration values.
# It does not select trace normalization.
# It does not adopt trace normalization.
# It does not select safe membership.
# It does not adopt safe membership.
# It does not recommend Package B adoption.
# It does not derive a coefficient law or insertion.
# It does not open active O, residual control, or parent closure.
#
# Tiny goblin rule:
#   Check which blanks can stand together. Do not sign the form.

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
        "COHERENT_IF_DECLARED": StatusMark.INFO,
        "CONDITIONAL": StatusMark.DEFER,
        "CONSISTENCY_MATRIX": StatusMark.INFO,
        "DECLARATION_REQUIRED": StatusMark.OBLIGATION,
        "FORBIDDEN_COMBINATION": StatusMark.FAIL,
        "INCOMPLETE": StatusMark.DEFER,
        "INVALID_COMBINATION": StatusMark.FAIL,
        "MIXED_STATUS": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_CHOSEN": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REQUIRED": StatusMark.OBLIGATION,
        "SCOPE_LIMITED": StatusMark.DEFER,
        "STATUS_MODE_REQUIRED": StatusMark.OBLIGATION,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g35_component_ledger",
            "35_trace_anchor_joint_declaration_inventory__candidate_trace_anchor_component_declaration_ledger",
            "g35_component_declaration_ledger",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g35_problem",
            "35_trace_anchor_joint_declaration_inventory__candidate_trace_anchor_joint_declaration_problem",
            "g35_trace_anchor_joint_declaration_problem",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g34_summary",
            "34_safe_trace_membership_candidate_origin__candidate_group_34_status_summary",
            "g34_status_summary",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g33_summary",
            "33_trace_normalization_candidate_origin__candidate_group_33_status_summary",
            "g33_status_summary",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g32_summary",
            "32_explicit_minimal_postulate_selection__candidate_group_32_status_summary",
            "g32_status_summary",
            RecordKind.INVENTORY_MARKER,
        ),
    ]

    for dependency_id, upstream_script_id, upstream_derivation_id, record_kind in dependencies:
        ns.declare_dependency(
            dependency_id=dependency_id,
            upstream_script_id=upstream_script_id,
            upstream_derivation_id=upstream_derivation_id,
            expected_record_kind=record_kind,
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
class MatrixSymbols:
    B_s_decl: sp.Symbol
    zeta_decl: sp.Symbol
    d_decl: sp.Symbol
    exact_scope: sp.Symbol
    N_trace_status: sp.Symbol
    zeta_Bs_decl: sp.Symbol
    T_zeta_decl: sp.Symbol
    domain_decl: sp.Symbol
    codomain_decl: sp.Symbol
    membership_criterion: sp.Symbol
    role_purity: sp.Symbol
    diagnostic_scope: sp.Symbol
    norm_membership_separation: sp.Symbol
    component_status_mode: sp.Symbol
    mixed_status: sp.Symbol
    scope_mismatch: sp.Symbol
    hidden_declaration: sp.Symbol
    node_collapse: sp.Symbol
    P_insertion: sp.Symbol
    P_active_O: sp.Symbol
    P_residual_kill: sp.Symbol
    P_parent: sp.Symbol
    L_norm_axis: sp.Basic
    L_membership_axis: sp.Basic
    L_joint_axis: sp.Basic
    L_incoherence_modes: sp.Basic
    L_downstream_closed: sp.Basic
    L_matrix_gap: sp.Basic


@dataclass
class ConsistencyRow:
    name: str
    combination: str
    status: str
    coherent_if: str
    fails_if: str
    boundary: str


@dataclass
class IncoherentCombination:
    name: str
    combination: str
    status: str
    reason: str
    failure_mode: str


@dataclass
class MatrixRule:
    name: str
    rule: str
    status: str
    reason: str


@dataclass
class MatrixObligation:
    name: str
    obligation: str
    status: str
    blocks: str
    discipline: str


@dataclass
class MatrixConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_symbols() -> MatrixSymbols:
    (
        B_s_decl,
        zeta_decl,
        d_decl,
        exact_scope,
        N_trace_status,
        zeta_Bs_decl,
        T_zeta_decl,
        domain_decl,
        codomain_decl,
        membership_criterion,
        role_purity,
        diagnostic_scope,
        norm_membership_separation,
        component_status_mode,
        mixed_status,
        scope_mismatch,
        hidden_declaration,
        node_collapse,
    ) = sp.symbols(
        "B_s_decl zeta_decl d_decl exact_scope N_trace_status "
        "zeta_Bs_decl T_zeta_decl domain_decl codomain_decl membership_criterion "
        "role_purity diagnostic_scope norm_membership_separation component_status_mode "
        "mixed_status scope_mismatch hidden_declaration node_collapse"
    )
    P_insertion, P_active_O, P_residual_kill, P_parent = sp.symbols(
        "P_insertion P_active_O P_residual_kill P_parent"
    )

    L_norm_axis = sp.simplify(B_s_decl + zeta_decl + d_decl + exact_scope + N_trace_status)
    L_membership_axis = sp.simplify(
        zeta_Bs_decl + T_zeta_decl + domain_decl + codomain_decl + membership_criterion + role_purity + diagnostic_scope
    )
    L_joint_axis = sp.simplify(norm_membership_separation + component_status_mode)
    L_incoherence_modes = sp.simplify(mixed_status + scope_mismatch + hidden_declaration + node_collapse)
    L_downstream_closed = sp.simplify(P_insertion + P_active_O + P_residual_kill + P_parent)
    L_matrix_gap = sp.simplify(L_norm_axis + L_membership_axis + L_joint_axis + L_incoherence_modes + L_downstream_closed)

    return MatrixSymbols(
        B_s_decl,
        zeta_decl,
        d_decl,
        exact_scope,
        N_trace_status,
        zeta_Bs_decl,
        T_zeta_decl,
        domain_decl,
        codomain_decl,
        membership_criterion,
        role_purity,
        diagnostic_scope,
        norm_membership_separation,
        component_status_mode,
        mixed_status,
        scope_mismatch,
        hidden_declaration,
        node_collapse,
        P_insertion,
        P_active_O,
        P_residual_kill,
        P_parent,
        L_norm_axis,
        L_membership_axis,
        L_joint_axis,
        L_incoherence_modes,
        L_downstream_closed,
        L_matrix_gap,
    )


def build_consistency_rows() -> List[ConsistencyRow]:
    return [
        ConsistencyRow(
            "J1: scale-factor normalization with typed membership",
            "B_s scale-factor convention + total volume-log zeta + declared d + typed zeta_Bs -> T_zeta",
            "COHERENT_IF_DECLARED",
            "B_s, zeta, d, zeta_Bs, T_zeta, domain, codomain, and membership criterion are all declared",
            "any object convention, trace convention, dimension, or membership criterion remains blank",
            "coherence does not select, adopt, derive, or insert the pair",
        ),
        ConsistencyRow(
            "J2: metric-coefficient normalization with typed membership",
            "B_s metric-coefficient convention + total volume-log zeta + declared d + typed zeta_Bs -> T_zeta",
            "COHERENT_IF_DECLARED",
            "the factor-of-two convention is explicit and membership is typed separately",
            "B_s metric coefficient language is used without declaring it or membership collapses into normalization",
            "coherence does not prove metric insertion or residual control",
        ),
        ConsistencyRow(
            "J3: per-dimension trace notation with membership",
            "per-dimension zeta notation + typed or role-pure membership",
            "CONDITIONAL",
            "zeta is explicitly declared as already divided by the traced dimension",
            "dimension factor is hidden in notation or d is selected from recovery",
            "notation-equivalence is not physical derivation",
        ),
        ConsistencyRow(
            "J4: exact trace form with active membership theorem target",
            "exact determinant/volume trace scope + active typed membership theorem target",
            "CONDITIONAL",
            "both components are explicitly marked theorem targets and downstream gates remain closed",
            "active membership is used as insertion, active O, residual control, or parent readiness",
            "theorem-target status is not already theorem proof",
        ),
        ConsistencyRow(
            "J5: diagnostic membership with trace-normalization candidate",
            "trace-normalization candidate + diagnostic-only/inert membership label",
            "COHERENT_IF_DECLARED",
            "diagnostic label is strictly equation-inert and status mode is explicit",
            "diagnostic label modifies equations or is used downstream",
            "diagnostic coherence cannot license Package B use for insertion",
        ),
        ConsistencyRow(
            "J6: mixed theorem/adoption status",
            "one Package B component adopted or theorem-supported while the other remains compatible-if-declared",
            "MIXED_STATUS",
            "the mixed status is explicitly recorded and downstream use is blocked or conditionalized",
            "mixed status is hidden and Package B is treated as uniformly adopted/derived",
            "mixed status is an obligation, not a recommendation",
        ),
        ConsistencyRow(
            "J7: joint deferred status",
            "both Package B components remain compatible-if-declared or deferred",
            "INCOMPLETE",
            "handoff states that Package B remains audit-only and not usable downstream",
            "deferred status is shortened to selected, adopted, derived, or insertable",
            "incomplete is safe; it does not mean permanent no-go",
        ),
    ]


def build_incoherent_combinations() -> List[IncoherentCombination]:
    return [
        IncoherentCombination(
            "X1: hidden declaration combination",
            "a joint trace-anchor pair is used while required declaration slots remain blank",
            "INVALID_COMBINATION",
            "compatible-if-declared status is conditional on declarations",
            "hidden conventions enter later theorem or insertion work",
        ),
        IncoherentCombination(
            "X2: normalization membership collapse",
            "P_trace_norm chooses P_safe_membership or P_safe_membership chooses P_trace_norm",
            "FORBIDDEN_COMBINATION",
            "Groups 32-34 keep the Package B nodes separate",
            "Package B hides two choices as one",
        ),
        IncoherentCombination(
            "X3: scope mismatch",
            "linearized-only trace normalization paired with exact active membership or exact downstream use",
            "INVALID_COMBINATION",
            "linearized scope cannot be upgraded to exact law by pairing",
            "first-order bookkeeping becomes exact coefficient law",
        ),
        IncoherentCombination(
            "X4: diagnostic label used actively",
            "diagnostic-only membership label is used to modify equations or support insertion",
            "INVALID_COMBINATION",
            "diagnostic labels are safe only if strictly inert",
            "audit labels become active projectors or insertion handles",
        ),
        IncoherentCombination(
            "X5: role-purity violation",
            "membership pair carries residual, ordinary-source, correction, or downstream payload",
            "INVALID_COMBINATION",
            "safe membership cannot be a hidden-load pocket",
            "membership becomes residual/source/divergence cleanup",
        ),
        IncoherentCombination(
            "X6: declaration pair as insertion",
            "a coherent pair of declarations is treated as B_s/F_zeta insertion",
            "FORBIDDEN_COMBINATION",
            "insertion remains downstream and not ready",
            "declaration coherence becomes metric insertion",
        ),
        IncoherentCombination(
            "X7: declaration pair as parent readiness",
            "a coherent pair of declarations is treated as parent field equation readiness",
            "FORBIDDEN_COMBINATION",
            "parent field equation remains blocked by recombination and safety gates",
            "parent gate opens by declaration clarity",
        ),
    ]


def build_rules() -> List[MatrixRule]:
    return [
        MatrixRule(
            "R1: coherence is not selection",
            "A coherent-if-declared pair is still not selected",
            "POLICY_RULE",
            "joint consistency is weaker than component choice",
        ),
        MatrixRule(
            "R2: coherence is not adoption",
            "A coherent-if-declared pair is not Package B adoption",
            "POLICY_RULE",
            "adoption requires a separate explicit decision record",
        ),
        MatrixRule(
            "R3: coherence is not theorem proof",
            "A coherent declaration pair does not prove trace normalization or safe membership",
            "POLICY_RULE",
            "declarations define terms and compatibility, not field behavior",
        ),
        MatrixRule(
            "R4: mixed status must be visible",
            "If component statuses differ, the mixed status must be recorded before handoff",
            "STATUS_MODE_REQUIRED",
            "hidden mixed status creates accidental downstream licensing",
        ),
        MatrixRule(
            "R5: downstream gates remain closed",
            "Joint consistency does not license insertion, active O, residual control, or parent closure",
            "POLICY_RULE",
            "downstream gates require separate theorem/adoption/precondition status",
        ),
    ]


def build_obligations() -> List[MatrixObligation]:
    return [
        MatrixObligation(
            "O1: preserve joint consistency boundary",
            "record coherent pairs as coherent-if-declared only",
            "OPEN",
            "selection drift",
            "coherent pair is not selected, adopted, or derived",
        ),
        MatrixObligation(
            "O2: block incoherent combinations",
            "reject hidden declarations, node collapse, scope mismatch, diagnostic-active misuse, hidden payloads, insertion, and parent readiness",
            "OPEN",
            "smuggling and downstream overreach",
            "invalid pair must fail before handoff",
        ),
        MatrixObligation(
            "O3: preserve component status modes",
            "require explicit status mode for each Package B component before future use",
            "OPEN",
            "ambiguous handoff",
            "mixed or deferred status must be visible",
        ),
        MatrixObligation(
            "O4: preserve node separation",
            "keep trace normalization and safe membership as separate nodes in all coherent pairs",
            "OPEN",
            "Package B collapse",
            "joint matrix is not node merger",
        ),
        MatrixObligation(
            "O5: adoption boundary",
            "do not adopt Package B or either component in this matrix",
            "REQUIRED",
            "governance integrity",
            "adoption requires separate explicit decision",
        ),
        MatrixObligation(
            "O6: downstream gates",
            "keep B_s/F_zeta insertion, active O, residual control, and parent closure closed",
            "NOT_READY",
            "downstream overreach",
            "joint consistency matrix is not insertion or parent readiness",
        ),
    ]


def build_conclusions() -> List[MatrixConclusion]:
    return [
        MatrixConclusion(
            "C1: consistency matrix stated",
            "joint declaration combinations are classified for coherence, mixed status, incompleteness, or invalidity",
            "CONSISTENCY_MATRIX",
            "declaration pairs can now be audited without selecting them",
        ),
        MatrixConclusion(
            "C2: coherent pairs remain conditional",
            "scale-factor/metric-coefficient trace forms can be coherent with typed or role-pure membership only if declarations are explicit",
            "COHERENT_IF_DECLARED",
            "coherent-if-declared is not selected, adopted, or derived",
        ),
        MatrixConclusion(
            "C3: invalid pairs fail",
            "hidden declarations, node collapse, scope mismatch, diagnostic-active misuse, hidden payloads, insertion, and parent readiness fail",
            "REQUIRED",
            "joint clarity cannot become smuggling",
        ),
        MatrixConclusion(
            "C4: no declaration values chosen",
            "this matrix tests combinations but fills no declaration slots",
            "NOT_CHOSEN",
            "matrix classification is not convention choice",
        ),
        MatrixConclusion(
            "C5: no adoption",
            "this matrix adopts no Package B component and recommends no adoption",
            "NOT_ADOPTED",
            "explicit decision remains separate",
        ),
        MatrixConclusion(
            "C6: next",
            "status-mode sieve or declaration-obligations script should run next",
            "OPEN",
            "future handoff should distinguish compatible-if-declared, declared candidate, theorem target, adopted postulate, diagnostic-only, and deferred statuses",
        ),
    ]


def case_0_problem(out: ScriptOutput) -> None:
    header("Case 0: Joint consistency matrix problem")
    print("Question:\n")
    print("  Which trace-normalization and safe-membership declaration combinations")
    print("  are coherent, incomplete, mixed-status, or invalid before any component")
    print("  is chosen, adopted, derived, or used downstream?")
    print("\nDiscipline:\n")
    print("  This script tests declaration-combination coherence.")
    print("  It fills no declaration slot.")
    print("  It selects no trace-normalization form.")
    print("  It selects no safe-membership form.")
    print("  It adopts no Package B component.")
    print("  It recommends no Package B adoption.")
    print("  It derives no coefficient law and no insertion.")
    print("  It keeps active O, residual control, and parent closure closed.")
    print("\nTiny goblin rule:")
    print("  Check which blanks can stand together. Do not sign the form.")
    with out.governance_assessments():
        out.line(
            "joint consistency matrix opened",
            StatusMark.INFO,
            "testing declaration-combination coherence after component declaration ledger; no choices made",
        )


def case_1_symbols(symbols: MatrixSymbols, out: ScriptOutput) -> None:
    header("Case 1: Joint consistency symbolic ledger")
    print("Matrix symbols:")
    for sym in (
        symbols.B_s_decl,
        symbols.zeta_decl,
        symbols.d_decl,
        symbols.exact_scope,
        symbols.N_trace_status,
        symbols.zeta_Bs_decl,
        symbols.T_zeta_decl,
        symbols.domain_decl,
        symbols.codomain_decl,
        symbols.membership_criterion,
        symbols.role_purity,
        symbols.diagnostic_scope,
        symbols.norm_membership_separation,
        symbols.component_status_mode,
        symbols.mixed_status,
        symbols.scope_mismatch,
        symbols.hidden_declaration,
        symbols.node_collapse,
        symbols.P_insertion,
        symbols.P_active_O,
        symbols.P_residual_kill,
        symbols.P_parent,
    ):
        print(f"  {sym} = {sym}")
    print("\nTrace-normalization axis load:")
    print(f"  L_norm_axis = {symbols.L_norm_axis}")
    print("\nSafe-membership axis load:")
    print(f"  L_membership_axis = {symbols.L_membership_axis}")
    print("\nJoint status axis load:")
    print(f"  L_joint_axis = {symbols.L_joint_axis}")
    print("\nIncoherence-mode load:")
    print(f"  L_incoherence_modes = {symbols.L_incoherence_modes}")
    print("\nDownstream closed load:")
    print(f"  L_downstream_closed = {symbols.L_downstream_closed}")
    print("\nJoint consistency matrix gap:")
    print(f"  L_matrix_gap = {symbols.L_matrix_gap}")
    with out.derived_results():
        out.line(
            "joint consistency symbolic loads stated",
            StatusMark.OBLIGATION,
            f"L_norm_axis={symbols.L_norm_axis}; L_membership_axis={symbols.L_membership_axis}; L_downstream_closed={symbols.L_downstream_closed}",
        )


def case_2_consistency_rows(rows: List[ConsistencyRow], out: ScriptOutput) -> None:
    header("Case 2: Joint consistency matrix rows")
    with out.governance_assessments():
        for item in rows:
            subheader(item.name)
            print(f"Combination: {item.combination}")
            out.line(item.name, status_mark(item.status), item.status)
            print(f"Coherent if: {item.coherent_if}")
            print(f"Fails if: {item.fails_if}")
            print(f"Boundary: {item.boundary}")
        out.line(
            "joint consistency rows stated",
            StatusMark.DEFER,
            f"{len(rows)} declaration combinations classified; none selected or adopted",
        )


def case_3_incoherent_combinations(invalids: List[IncoherentCombination], out: ScriptOutput) -> None:
    header("Case 3: Incoherent / invalid joint combinations")
    with out.counterexamples():
        for item in invalids:
            subheader(item.name)
            print(f"Combination: {item.combination}")
            out.line(item.name, status_mark(item.status), item.status)
            print(f"Reason: {item.reason}")
            print(f"Failure mode: {item.failure_mode}")
        out.line(
            "invalid joint combinations rejected",
            StatusMark.FAIL,
            f"{len(invalids)} invalid or forbidden combinations rejected",
        )


def case_4_rules(rules: List[MatrixRule], out: ScriptOutput) -> None:
    header("Case 4: Joint consistency no-overclaim rules")
    with out.governance_assessments():
        for item in rules:
            subheader(item.name)
            print(f"Rule: {item.rule}")
            out.line(item.name, status_mark(item.status), item.status)
            print(f"Reason: {item.reason}")
        out.line(
            "joint consistency no-overclaim rules stated",
            StatusMark.OBLIGATION,
            f"{len(rules)} rules stated",
        )


def case_5_obligations(obligations: List[MatrixObligation], out: ScriptOutput) -> None:
    header("Case 5: Joint consistency obligations")
    with out.unresolved_obligations():
        for item in obligations:
            subheader(item.name)
            print(f"Obligation: {item.obligation}")
            out.line(item.name, status_mark(item.status), item.status)
            print(f"Blocks: {item.blocks}")
            print(f"Discipline: {item.discipline}")
        out.line(
            "joint consistency obligations opened",
            StatusMark.OBLIGATION,
            f"{len(obligations)} obligations stated",
        )


def case_6_conclusions(conclusions: List[MatrixConclusion], out: ScriptOutput) -> None:
    header("Case 6: Joint consistency conclusions")
    with out.governance_assessments():
        for item in conclusions:
            subheader(item.name)
            print(f"Conclusion: {item.conclusion}")
            out.line(item.name, status_mark(item.status), item.status)
            print(f"Meaning: {item.meaning}")
        out.line(
            "joint consistency matrix conclusion stated",
            StatusMark.PASS,
            "coherent pairs remain conditional; invalid pairs fail; status-mode sieve or obligations should run next",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Trace-anchor joint consistency matrix result:\n")
    print("  Joint declaration combinations are now classified for coherence, mixed status, incompleteness, or invalidity.")
    print("  Scale-factor and metric-coefficient trace-normalization forms can pair coherently with typed or role-pure membership only if all declarations are explicit.")
    print("  Per-dimension and diagnostic cases remain conditional on notation and inertness.")
    print("  Mixed component statuses must be visible before handoff.")
    print("  Hidden declarations, node collapse, scope mismatch, diagnostic-active misuse, hidden payloads, insertion, and parent readiness fail.")
    print("  No declaration value is chosen by this matrix.")
    print("  No trace-normalization or safe-membership form is selected, adopted, or derived.")
    print("  Package B is not recommended for adoption.")
    print("  B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready.")
    print("\nPossible next script:")
    print("  candidate_trace_anchor_status_mode_sieve.py")
    print("\nTiny goblin label:")
    print("  Check which blanks can stand together. Do not sign the form.")
    with out.governance_assessments():
        out.line(
            "trace-anchor joint consistency matrix complete",
            StatusMark.PASS,
            "status-mode sieve or declaration-obligations script should run next; adoption and downstream gates remain closed",
        )


def record_inventory_marker(ns, symbols: MatrixSymbols) -> None:
    ns.record_derivation(
        derivation_id="g35_joint_consistency_matrix",
        inputs=[
            symbols.L_norm_axis,
            symbols.L_membership_axis,
            symbols.L_joint_axis,
            symbols.L_incoherence_modes,
            symbols.L_downstream_closed,
        ],
        output=symbols.L_matrix_gap,
        method="Group 35 joint consistency matrix over trace-anchor declaration combinations",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="joint_consistency_matrix_marker",
        is_placeholder=True,
    )


def record_obligations(ns, obligations: List[MatrixObligation]) -> None:
    for item in obligations:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_obligation(
            ProofObligationRecord(
                obligation_id=f"g35_joint_consistency_{ident}",
                script_id=SCRIPT_ID,
                title=item.name,
                status=ObligationStatus.OPEN if item.status != "NOT_READY" else ObligationStatus.DEFERRED,
                required_by=[SCRIPT_ID],
                description=f"{item.obligation} Blocks: {item.blocks}. Discipline: {item.discipline}.",
            )
        )


def record_governance(
    ns,
    rows: List[ConsistencyRow],
    invalids: List[IncoherentCombination],
    rules: List[MatrixRule],
) -> None:
    obligation_ids = [
        "g35_joint_consistency_o1",
        "g35_joint_consistency_o2",
        "g35_joint_consistency_o3",
        "g35_joint_consistency_o4",
        "g35_joint_consistency_o5",
        "g35_joint_consistency_o6",
    ]

    ns.record_route(
        RouteRecord(
            route_id="g35_joint_consistency_matrix_route",
            script_id=SCRIPT_ID,
            name="Group 35 trace-anchor joint consistency matrix route",
            status=GovernanceStatus.CANDIDATE_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            required_obligations=obligation_ids,
            activation_conditions=[
                "component declaration ledger completed",
                "trace-normalization and safe-membership declaration slots are visible",
                "joint combinations can be tested without filling slots",
                "adoption and downstream gates remain closed",
            ],
        )
    )

    for item in rows:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g35_consistency_row_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.CANDIDATE_ROUTE,
                statement=(
                    f"Joint consistency row: {item.combination}. Status: {item.status}. "
                    f"Coherent if: {item.coherent_if}. Fails if: {item.fails_if}. Boundary: {item.boundary}."
                ),
                derivation_ids=["g35_joint_consistency_matrix"],
                obligation_ids=obligation_ids,
            )
        )

    for item in invalids:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g35_invalid_joint_combination_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.POLICY_RULE,
                statement=f"Invalid joint combination: {item.combination}. Reason: {item.reason}. Failure mode: {item.failure_mode}.",
                derivation_ids=["g35_joint_consistency_matrix"],
                obligation_ids=obligation_ids,
            )
        )

    for item in rules:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g35_joint_consistency_rule_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.POLICY_RULE,
                statement=f"{item.rule}. Reason: {item.reason}.",
                derivation_ids=["g35_joint_consistency_matrix"],
                obligation_ids=obligation_ids,
            )
        )

    ns.record_claim(
        ClaimRecord(
            claim_id="g35_joint_consistency_matrix_complete",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.CANDIDATE_ROUTE,
            statement=(
                "Trace-anchor joint consistency matrix completed. Coherent pairs remain conditional; "
                "invalid pairs fail; no declaration value is chosen; no Package B component is selected, adopted, or derived."
            ),
            derivation_ids=["g35_joint_consistency_matrix"],
            obligation_ids=obligation_ids,
        )
    )


def main() -> None:
    header("Candidate Trace Anchor Joint Consistency Matrix")
    archive, ns, invalidated = prepare_archive()
    ensure_archive_write_dirs(ns)
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    rows = build_consistency_rows()
    invalids = build_incoherent_combinations()
    rules = build_rules()
    obligations = build_obligations()
    conclusions = build_conclusions()

    case_0_problem(out)
    case_1_symbols(symbols, out)
    case_2_consistency_rows(rows, out)
    case_3_incoherent_combinations(invalids, out)
    case_4_rules(rules, out)
    case_5_obligations(obligations, out)
    case_6_conclusions(conclusions, out)
    final_interpretation(out)

    record_inventory_marker(ns, symbols)
    record_obligations(ns, obligations)
    record_governance(ns, rows, invalids, rules)

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
