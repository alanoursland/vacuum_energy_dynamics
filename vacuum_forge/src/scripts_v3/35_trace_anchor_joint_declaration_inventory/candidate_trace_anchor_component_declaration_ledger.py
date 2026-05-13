# Candidate Trace Anchor Component Declaration Ledger
#
# Group:
#   35_trace_anchor_joint_declaration_inventory
#
# Human title:
#   Trace Anchor Joint Declaration Inventory
#
# Script type:
#   COMPONENT DECLARATION LEDGER
#
# Purpose
# -------
# Inventory the concrete declaration slots required before trace-normalization
# and safe-membership Package B components can be jointly used.
#
# This script does not choose any declaration value.
# It does not select trace normalization.
# It does not adopt trace normalization.
# It does not select safe membership.
# It does not adopt safe membership.
# It does not recommend Package B adoption.
# It does not derive a coefficient law or insertion.
# It does not open active O, residual control, or parent closure.
#
# Tiny goblin rule:
#   Name every blank on the form. Do not sign it yet.

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
        "ADMISSIBLE_DECLARATION_SLOT": StatusMark.INFO,
        "COMPATIBILITY_DECLARATION": StatusMark.INFO,
        "CONDITIONAL": StatusMark.DEFER,
        "DECLARATION_LEDGER": StatusMark.INFO,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_CHOSEN": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REQUIRED": StatusMark.OBLIGATION,
        "STATUS_MODE_SLOT": StatusMark.INFO,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
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
class ComponentSymbols:
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
    P_insertion: sp.Symbol
    P_active_O: sp.Symbol
    P_residual_kill: sp.Symbol
    P_parent: sp.Symbol
    L_trace_norm_slots: sp.Basic
    L_membership_slots: sp.Basic
    L_joint_slots: sp.Basic
    L_status_slots: sp.Basic
    L_downstream_closed: sp.Basic
    L_component_gap: sp.Basic


@dataclass
class DeclarationSlot:
    name: str
    slot: str
    component: str
    status: str
    required_content: str
    unresolved_if_missing: str
    forbidden_upgrade: str


@dataclass
class StatusMode:
    name: str
    mode: str
    status: str
    allowed_meaning: str
    forbidden_meaning: str
    consequence: str


@dataclass
class InvalidDeclaration:
    name: str
    shortcut: str
    status: str
    reason: str
    failure_mode: str


@dataclass
class LedgerObligation:
    name: str
    obligation: str
    status: str
    blocks: str
    discipline: str


@dataclass
class LedgerConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_symbols() -> ComponentSymbols:
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
    ) = sp.symbols(
        "B_s_decl zeta_decl d_decl exact_scope N_trace_status "
        "zeta_Bs_decl T_zeta_decl domain_decl codomain_decl membership_criterion "
        "role_purity diagnostic_scope norm_membership_separation component_status_mode"
    )
    P_insertion, P_active_O, P_residual_kill, P_parent = sp.symbols(
        "P_insertion P_active_O P_residual_kill P_parent"
    )

    L_trace_norm_slots = sp.simplify(B_s_decl + zeta_decl + d_decl + exact_scope + N_trace_status)
    L_membership_slots = sp.simplify(
        zeta_Bs_decl
        + T_zeta_decl
        + domain_decl
        + codomain_decl
        + membership_criterion
        + role_purity
        + diagnostic_scope
    )
    L_status_slots = sp.simplify(norm_membership_separation + component_status_mode)
    L_joint_slots = sp.simplify(L_trace_norm_slots + L_membership_slots + L_status_slots)
    L_downstream_closed = sp.simplify(P_insertion + P_active_O + P_residual_kill + P_parent)
    L_component_gap = sp.simplify(L_joint_slots + L_downstream_closed)

    return ComponentSymbols(
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
        P_insertion,
        P_active_O,
        P_residual_kill,
        P_parent,
        L_trace_norm_slots,
        L_membership_slots,
        L_joint_slots,
        L_status_slots,
        L_downstream_closed,
        L_component_gap,
    )


def build_declaration_slots() -> List[DeclarationSlot]:
    return [
        DeclarationSlot(
            "T1: B_s object convention",
            "declare whether B_s is scale-factor language, metric-coefficient language, or separate functional response",
            "trace normalization",
            "ADMISSIBLE_DECLARATION_SLOT",
            "one object convention named before using zeta/d or 2*zeta/d forms",
            "factor-of-two ambiguity remains",
            "must not be chosen from recovery, insertion, or parent fit",
        ),
        DeclarationSlot(
            "T2: zeta trace convention",
            "declare whether zeta is total volume-log trace or per-dimension normalized trace",
            "trace normalization",
            "ADMISSIBLE_DECLARATION_SLOT",
            "trace convention and notation scope stated explicitly",
            "dimension factor can hide in notation",
            "must not hide normalization in the definition of zeta",
        ),
        DeclarationSlot(
            "T3: traced sector dimension",
            "declare the traced sector dimension d and what sector is counted",
            "trace normalization",
            "ADMISSIBLE_DECLARATION_SLOT",
            "dimension d and sector basis named before dimensional forms are used",
            "zeta/d and 2*zeta/d are unavailable",
            "must not be selected after recovery targets are known",
        ),
        DeclarationSlot(
            "T4: exact versus linearized scope",
            "declare whether the trace-normalization form is exact determinant/volume structure or first-order only",
            "trace normalization",
            "ADMISSIBLE_DECLARATION_SLOT",
            "scope statement attached to the form",
            "linearized bookkeeping may be overclaimed as exact law",
            "must not upgrade first-order consistency to exact insertion law",
        ),
        DeclarationSlot(
            "T5: trace-normalization status mode",
            "declare whether the trace-normalization form is theorem target, explicit candidate, adopted postulate, diagnostic-only, or deferred",
            "trace normalization",
            "STATUS_MODE_SLOT",
            "status mode stated before any downstream use",
            "compatible-if-declared may drift into selected/adopted/derived language",
            "must not treat status mode as adoption or proof",
        ),
        DeclarationSlot(
            "M1: zeta_Bs object declaration",
            "declare what zeta_Bs is as an object before testing membership",
            "safe membership",
            "ADMISSIBLE_DECLARATION_SLOT",
            "object role and payload type stated",
            "membership remains a label rather than a testable form",
            "must not be residual payload, source carrier, correction reservoir, or insertion handle",
        ),
        DeclarationSlot(
            "M2: T_zeta sector declaration",
            "declare T_zeta sector, sector basis, and accepted trace content",
            "safe membership",
            "ADMISSIBLE_DECLARATION_SLOT",
            "target sector is typed before membership is claimed",
            "T_zeta label may be mistaken for proof",
            "must not imply incidence, active O, or residual kill",
        ),
        DeclarationSlot(
            "M3: domain and codomain declaration",
            "declare membership domain and codomain for zeta_Bs -> T_zeta",
            "safe membership",
            "ADMISSIBLE_DECLARATION_SLOT",
            "domain and codomain visible before compatibility testing",
            "membership claim is not well-posed",
            "must not include residual/source/correction zones by convenience",
        ),
        DeclarationSlot(
            "M4: membership criterion declaration",
            "declare the criterion by which zeta_Bs belongs to T_zeta",
            "safe membership",
            "ADMISSIBLE_DECLARATION_SLOT",
            "criterion stated before theorem/adoption use",
            "sector assignment remains unsupported",
            "must not imply zero incidence or residual control",
        ),
        DeclarationSlot(
            "M5: role-purity and exclusion declaration",
            "declare how residual, source, correction, and downstream payloads stay outside membership",
            "safe membership",
            "ADMISSIBLE_DECLARATION_SLOT",
            "exclusion zones visible before membership use",
            "membership can become hidden-load pocket",
            "must not become source theorem, divergence safety, or residual kill",
        ),
        DeclarationSlot(
            "M6: diagnostic versus active scope",
            "declare whether membership is diagnostic-only/inert or intended as active typed-sector theorem target",
            "safe membership",
            "ADMISSIBLE_DECLARATION_SLOT",
            "equation effect status stated explicitly",
            "diagnostic label may be used as active operator",
            "must not modify equations unless separately derived/adopted",
        ),
        DeclarationSlot(
            "J1: normalization/membership separation",
            "declare that P_trace_norm and P_safe_membership remain separate nodes",
            "joint trace anchor",
            "REQUIRED",
            "node separation carried before joint Package B use",
            "Package B collapses into one hidden choice",
            "must not let normalization choose membership or membership choose normalization",
        ),
        DeclarationSlot(
            "J2: component adoption/theorem status",
            "declare whether each component is theorem target, explicit candidate, adopted postulate, diagnostic-only, or deferred",
            "joint trace anchor",
            "REQUIRED",
            "status mode visible before any handoff",
            "audit result may become ambiguous theory status",
            "must not call adopted postulates derived or compatible-if-declared forms adopted",
        ),
    ]


def build_status_modes() -> List[StatusMode]:
    return [
        StatusMode(
            "S1: compatible-if-declared",
            "component form survives filters only after declarations are made",
            "STATUS_MODE_SLOT",
            "current status for Group 33/34 surviving forms",
            "not selected, not adopted, not derived",
            "may be carried into declaration ledger only",
        ),
        StatusMode(
            "S2: declared explicit candidate",
            "component is declared as candidate but not adopted",
            "CONDITIONAL",
            "possible future status after convention/criterion declaration",
            "not theorem and not postulate adoption",
            "may support later decision or theorem attempt",
        ),
        StatusMode(
            "S3: theorem target",
            "component is pursued by derivation after declarations",
            "CONDITIONAL",
            "possible future theorem route",
            "not already derived by declaration",
            "requires separate proof script",
        ),
        StatusMode(
            "S4: explicit adopted postulate",
            "component is adopted by separate user/theory decision",
            "CONDITIONAL",
            "possible future adoption route",
            "must not be reported as derived",
            "requires separate adoption record",
        ),
        StatusMode(
            "S5: diagnostic-only/inert",
            "component label is used only for audit and does not alter equations",
            "CONDITIONAL",
            "safe fallback for membership labels or bookkeeping",
            "not active membership and not insertion",
            "cannot license downstream gates",
        ),
        StatusMode(
            "S6: deferred/not ready",
            "component or downstream use remains unresolved",
            "NOT_READY",
            "safe status for incomplete declarations",
            "not a failure theorem or permanent no-go",
            "blocks insertion and parent work",
        ),
    ]


def build_invalid_declarations() -> List[InvalidDeclaration]:
    return [
        InvalidDeclaration(
            "X1: undeclared but used",
            "use a trace-anchor component while one or more required declaration slots remain blank",
            "FORBIDDEN_SHORTCUT",
            "compatible-if-declared survival is conditional",
            "hidden declarations enter later work",
        ),
        InvalidDeclaration(
            "X2: declaration as adoption",
            "treat component declaration as postulate adoption",
            "FORBIDDEN_SHORTCUT",
            "declaration inventory is not explicit decision",
            "audit language becomes theory choice",
        ),
        InvalidDeclaration(
            "X3: declaration as theorem",
            "treat component declaration as physical derivation",
            "FORBIDDEN_SHORTCUT",
            "declaration defines terms but does not prove field behavior",
            "naming becomes proof",
        ),
        InvalidDeclaration(
            "X4: node collapse",
            "collapse trace normalization and safe membership into one joint choice",
            "FORBIDDEN_SHORTCUT",
            "Groups 32-34 kept the nodes separate",
            "Package B hides a second choice",
        ),
        InvalidDeclaration(
            "X5: declaration as insertion",
            "treat a coherent declaration package as B_s/F_zeta insertion",
            "FORBIDDEN_SHORTCUT",
            "insertion remains downstream and not ready",
            "precondition clarity becomes metric insertion",
        ),
        InvalidDeclaration(
            "X6: declaration as parent readiness",
            "treat trace-anchor declaration clarity as parent equation readiness",
            "FORBIDDEN_SHORTCUT",
            "parent field equation remains blocked by recombination and safety gates",
            "parent gate opens prematurely",
        ),
    ]


def build_obligations() -> List[LedgerObligation]:
    return [
        LedgerObligation(
            "O1: complete trace-normalization declaration slots",
            "record B_s convention, zeta convention, traced dimension, exact/linearized scope, and trace-normalization status mode",
            "OPEN",
            "trace-normalization use",
            "no trace-normalization form can be used while its declarations are blank",
        ),
        LedgerObligation(
            "O2: complete safe-membership declaration slots",
            "record zeta_Bs object, T_zeta sector, domain/codomain, criterion, role-purity, and diagnostic/active scope",
            "OPEN",
            "safe-membership use",
            "no membership form can be used while its declarations are blank",
        ),
        LedgerObligation(
            "O3: preserve status-mode discipline",
            "state whether each component is compatible-if-declared, declared candidate, theorem target, adopted postulate, diagnostic-only, or deferred",
            "OPEN",
            "ambiguous downstream handoff",
            "status mode must be explicit before any future route",
        ),
        LedgerObligation(
            "O4: preserve node separation",
            "keep P_trace_norm and P_safe_membership separate unless a future explicit adoption record says otherwise",
            "OPEN",
            "Package B collapse",
            "joint declaration is not node collapse",
        ),
        LedgerObligation(
            "O5: adoption boundary",
            "do not adopt either Package B component in this ledger",
            "REQUIRED",
            "governance integrity",
            "adoption requires separate explicit decision",
        ),
        LedgerObligation(
            "O6: downstream gates",
            "keep B_s/F_zeta insertion, active O, residual control, and parent closure closed",
            "NOT_READY",
            "downstream overreach",
            "component declaration ledger is not insertion or parent readiness",
        ),
    ]


def build_conclusions() -> List[LedgerConclusion]:
    return [
        LedgerConclusion(
            "C1: declaration slots inventoried",
            "trace-normalization, safe-membership, joint separation, and status-mode slots are visible",
            "DECLARATION_LEDGER",
            "later work can see which blanks must be filled before use",
        ),
        LedgerConclusion(
            "C2: no declaration values chosen",
            "this ledger names declaration slots but does not fill them",
            "NOT_CHOSEN",
            "slot inventory is not convention choice",
        ),
        LedgerConclusion(
            "C3: no selection or adoption",
            "no trace-normalization or safe-membership form is selected or adopted",
            "NOT_ADOPTED",
            "compatible-if-declared remains conditional",
        ),
        LedgerConclusion(
            "C4: invalid shortcuts rejected",
            "undeclared use, declaration-as-adoption, declaration-as-theorem, node collapse, insertion, and parent readiness shortcuts are blocked",
            "REQUIRED",
            "declaration clarity cannot become downstream closure",
        ),
        LedgerConclusion(
            "C5: downstream gates closed",
            "B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready",
            "NOT_READY",
            "component declarations are not insertion",
        ),
        LedgerConclusion(
            "C6: next",
            "joint consistency matrix should run next",
            "OPEN",
            "declaration combinations can now be tested for coherence without selecting them",
        ),
    ]


def case_0_problem(out: ScriptOutput) -> None:
    header("Case 0: Component declaration ledger problem")
    print("Question:\n")
    print("  Which exact declaration slots must be visible before the trace-normalization")
    print("  and safe-membership Package B components can be jointly used?")
    print("\nDiscipline:\n")
    print("  This script inventories declaration slots.")
    print("  It chooses no declaration value.")
    print("  It selects no trace-normalization form.")
    print("  It selects no safe-membership form.")
    print("  It adopts no Package B component.")
    print("  It derives no coefficient law and no insertion.")
    print("  It keeps active O, residual control, and parent closure closed.")
    print("\nTiny goblin rule:")
    print("  Name every blank on the form. Do not sign it yet.")
    with out.governance_assessments():
        out.line(
            "component declaration ledger opened",
            StatusMark.INFO,
            "inventorying declaration slots after Group 35 opener; no choices made",
        )


def case_1_symbols(symbols: ComponentSymbols, out: ScriptOutput) -> None:
    header("Case 1: Component declaration symbolic ledger")
    print("Declaration symbols:")
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
        symbols.P_insertion,
        symbols.P_active_O,
        symbols.P_residual_kill,
        symbols.P_parent,
    ):
        print(f"  {sym} = {sym}")
    print("\nTrace-normalization slot load:")
    print(f"  L_trace_norm_slots = {symbols.L_trace_norm_slots}")
    print("\nSafe-membership slot load:")
    print(f"  L_membership_slots = {symbols.L_membership_slots}")
    print("\nJoint status slot load:")
    print(f"  L_status_slots = {symbols.L_status_slots}")
    print("\nJoint declaration slot load:")
    print(f"  L_joint_slots = {symbols.L_joint_slots}")
    print("\nDownstream closed load:")
    print(f"  L_downstream_closed = {symbols.L_downstream_closed}")
    with out.derived_results():
        out.line(
            "component declaration symbolic loads stated",
            StatusMark.OBLIGATION,
            f"L_joint_slots={symbols.L_joint_slots}; L_downstream_closed={symbols.L_downstream_closed}",
        )


def case_2_declaration_slots(slots: List[DeclarationSlot], out: ScriptOutput) -> None:
    header("Case 2: Component declaration slots")
    with out.governance_assessments():
        for item in slots:
            subheader(item.name)
            print(f"Component: {item.component}")
            print(f"Declaration slot: {item.slot}")
            out.line(item.name, status_mark(item.status), item.status)
            print(f"Required content: {item.required_content}")
            print(f"Unresolved if missing: {item.unresolved_if_missing}")
            print(f"Forbidden upgrade: {item.forbidden_upgrade}")
        out.line(
            "component declaration slots inventoried",
            StatusMark.OBLIGATION,
            f"{len(slots)} declaration slots stated; none filled or chosen",
        )


def case_3_status_modes(modes: List[StatusMode], out: ScriptOutput) -> None:
    header("Case 3: Component status modes")
    with out.governance_assessments():
        for item in modes:
            subheader(item.name)
            print(f"Mode: {item.mode}")
            out.line(item.name, status_mark(item.status), item.status)
            print(f"Allowed meaning: {item.allowed_meaning}")
            print(f"Forbidden meaning: {item.forbidden_meaning}")
            print(f"Consequence: {item.consequence}")
        out.line(
            "component status modes separated",
            StatusMark.OBLIGATION,
            "status modes stated without adoption or theorem claims",
        )


def case_4_invalid_declarations(invalids: List[InvalidDeclaration], out: ScriptOutput) -> None:
    header("Case 4: Invalid declaration shortcuts")
    with out.counterexamples():
        for item in invalids:
            subheader(item.name)
            print(f"Shortcut: {item.shortcut}")
            out.line(item.name, status_mark(item.status), item.status)
            print(f"Reason: {item.reason}")
            print(f"Failure mode: {item.failure_mode}")
        out.line(
            "invalid declaration shortcuts rejected",
            StatusMark.FAIL,
            f"{len(invalids)} shortcuts rejected",
        )


def case_5_obligations(obligations: List[LedgerObligation], out: ScriptOutput) -> None:
    header("Case 5: Component declaration obligations")
    with out.unresolved_obligations():
        for item in obligations:
            subheader(item.name)
            print(f"Obligation: {item.obligation}")
            out.line(item.name, status_mark(item.status), item.status)
            print(f"Blocks: {item.blocks}")
            print(f"Discipline: {item.discipline}")
        out.line(
            "component declaration obligations opened",
            StatusMark.OBLIGATION,
            f"{len(obligations)} obligations stated",
        )


def case_6_conclusions(conclusions: List[LedgerConclusion], out: ScriptOutput) -> None:
    header("Case 6: Component declaration conclusions")
    with out.governance_assessments():
        for item in conclusions:
            subheader(item.name)
            print(f"Conclusion: {item.conclusion}")
            out.line(item.name, status_mark(item.status), item.status)
            print(f"Meaning: {item.meaning}")
        out.line(
            "component declaration ledger conclusion stated",
            StatusMark.PASS,
            "declaration slots inventoried; no component selected/adopted; joint consistency matrix should run next",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Trace-anchor component declaration ledger result:\n")
    print("  The declaration slots for trace normalization and safe membership are now visible.")
    print("  Trace-normalization slots include B_s convention, zeta convention, traced dimension, scope, and status mode.")
    print("  Safe-membership slots include zeta_Bs, T_zeta, domain/codomain, membership criterion, role purity, and diagnostic/active scope.")
    print("  Joint slots preserve normalization/membership separation and component status mode.")
    print("  No declaration value is chosen by this ledger.")
    print("  No trace-normalization or safe-membership form is selected, adopted, or derived.")
    print("  Package B is not recommended for adoption.")
    print("  B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready.")
    print("\nPossible next script:")
    print("  candidate_trace_anchor_joint_consistency_matrix.py")
    print("\nTiny goblin label:")
    print("  Name every blank on the form. Do not sign it yet.")
    with out.governance_assessments():
        out.line(
            "trace-anchor component declaration ledger complete",
            StatusMark.PASS,
            "joint consistency matrix should run next; adoption and downstream gates remain closed",
        )


def record_inventory_marker(ns, symbols: ComponentSymbols) -> None:
    ns.record_derivation(
        derivation_id="g35_component_declaration_ledger",
        inputs=[
            symbols.L_trace_norm_slots,
            symbols.L_membership_slots,
            symbols.L_status_slots,
            symbols.L_downstream_closed,
        ],
        output=symbols.L_component_gap,
        method="Group 35 component declaration slot inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="component_declaration_ledger_marker",
        is_placeholder=True,
    )


def record_obligations(ns, obligations: List[LedgerObligation]) -> None:
    for item in obligations:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_obligation(
            ProofObligationRecord(
                obligation_id=f"g35_component_declaration_{ident}",
                script_id=SCRIPT_ID,
                title=item.name,
                status=ObligationStatus.OPEN if item.status != "NOT_READY" else ObligationStatus.DEFERRED,
                required_by=[SCRIPT_ID],
                description=f"{item.obligation} Blocks: {item.blocks}. Discipline: {item.discipline}.",
            )
        )


def record_governance(
    ns,
    slots: List[DeclarationSlot],
    modes: List[StatusMode],
    invalids: List[InvalidDeclaration],
) -> None:
    obligation_ids = [
        "g35_component_declaration_o1",
        "g35_component_declaration_o2",
        "g35_component_declaration_o3",
        "g35_component_declaration_o4",
        "g35_component_declaration_o5",
        "g35_component_declaration_o6",
    ]

    ns.record_route(
        RouteRecord(
            route_id="g35_component_declaration_ledger_route",
            script_id=SCRIPT_ID,
            name="Group 35 trace-anchor component declaration ledger route",
            status=GovernanceStatus.CANDIDATE_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            required_obligations=obligation_ids,
            activation_conditions=[
                "Group 35 joint declaration problem opened",
                "Group 33 trace normalization remains compatible-if-declared",
                "Group 34 safe membership remains compatible-if-declared",
                "component slots must be visible before joint consistency tests",
            ],
        )
    )

    for item in slots:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g35_declaration_slot_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.CANDIDATE_ROUTE,
                statement=(
                    f"Declaration slot for {item.component}: {item.slot}. "
                    f"Required content: {item.required_content}. "
                    f"Unresolved if missing: {item.unresolved_if_missing}. "
                    f"Forbidden upgrade: {item.forbidden_upgrade}."
                ),
                derivation_ids=["g35_component_declaration_ledger"],
                obligation_ids=obligation_ids,
            )
        )

    for item in modes:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g35_status_mode_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.CANDIDATE_ROUTE,
                statement=(
                    f"Status mode: {item.mode}. Allowed meaning: {item.allowed_meaning}. "
                    f"Forbidden meaning: {item.forbidden_meaning}. Consequence: {item.consequence}."
                ),
                derivation_ids=["g35_component_declaration_ledger"],
                obligation_ids=obligation_ids,
            )
        )

    for item in invalids:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g35_invalid_declaration_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.POLICY_RULE,
                statement=f"Rejected declaration shortcut: {item.shortcut}. Reason: {item.reason}. Failure mode: {item.failure_mode}.",
                derivation_ids=["g35_component_declaration_ledger"],
                obligation_ids=obligation_ids,
            )
        )

    ns.record_claim(
        ClaimRecord(
            claim_id="g35_component_declaration_ledger_complete",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.CANDIDATE_ROUTE,
            statement=(
                "Trace-anchor component declaration slots are inventoried. No declaration value is chosen; "
                "no Package B component is selected, adopted, or derived; downstream gates remain closed."
            ),
            derivation_ids=["g35_component_declaration_ledger"],
            obligation_ids=obligation_ids,
        )
    )


def main() -> None:
    header("Candidate Trace Anchor Component Declaration Ledger")
    archive, ns, invalidated = prepare_archive()
    ensure_archive_write_dirs(ns)
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    slots = build_declaration_slots()
    modes = build_status_modes()
    invalids = build_invalid_declarations()
    obligations = build_obligations()
    conclusions = build_conclusions()

    case_0_problem(out)
    case_1_symbols(symbols, out)
    case_2_declaration_slots(slots, out)
    case_3_status_modes(modes, out)
    case_4_invalid_declarations(invalids, out)
    case_5_obligations(obligations, out)
    case_6_conclusions(conclusions, out)
    final_interpretation(out)

    record_inventory_marker(ns, symbols)
    record_obligations(ns, obligations)
    record_governance(ns, slots, modes, invalids)

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
