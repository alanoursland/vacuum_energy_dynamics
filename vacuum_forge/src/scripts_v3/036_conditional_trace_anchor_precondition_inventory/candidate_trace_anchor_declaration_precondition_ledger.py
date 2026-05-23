# Candidate Trace Anchor Declaration Precondition Ledger
#
# Group:
#   36_conditional_trace_anchor_precondition_inventory
#
# Human title:
#   Trace Anchor Declaration Precondition Ledger
#
# Script type:
#   PRECONDITION LEDGER / DECLARATION-SLOT AUDIT
#
# Purpose
# -------
# Inventory the declaration preconditions that must be explicit before
# trace-normalization and safe-membership Package B components can be used in
# theorem, adoption, precondition, insertion-facing, or parent-facing work.
#
# This script does not fill declaration slots.
# It does not assign Package B component status as theory state.
# It does not select trace normalization.
# It does not select safe membership.
# It does not adopt Package B.
# It does not recommend Package B adoption.
# It does not derive a coefficient law or insertion.
# It does not open active O, residual control, or parent closure.
#
# Tiny goblin rule:
#   Inspect the lock pins. Do not turn the key.

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

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


def safe_ident(name: str) -> str:
    raw = name.split(":", 1)[0].lower()
    return "".join(ch if ch.isalnum() else "_" for ch in raw).strip("_")


def status_mark(status: str) -> StatusMark:
    return {
        "ADMISSIBLE_DECLARATION_PRECONDITION": StatusMark.INFO,
        "BLOCKED_IF_BLANK": StatusMark.DEFER,
        "CONDITIONAL": StatusMark.DEFER,
        "FAIL": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
        "HANDOFF_READY": StatusMark.INFO,
        "INCOMPLETE": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_CHOSEN": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "PASS": StatusMark.PASS,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "PRECONDITION_REQUIRED": StatusMark.OBLIGATION,
        "REQUIRED": StatusMark.OBLIGATION,
        "STATUS_REQUIRED": StatusMark.OBLIGATION,
    }.get(status, StatusMark.INFO)


def out_line(section: str, status: str, title: str, detail: str = "") -> None:
    mark = status_mark(status).value
    print(f"[{section}]")
    if detail:
        print(f"{mark} {title} -- {status}\n{detail}")
    else:
        print(f"{mark} {title} -- {status}")


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g36_problem",
            "036_conditional_trace_anchor_precondition_inventory__candidate_trace_anchor_precondition_inventory_problem",
            "g36_precondition_inventory_problem",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g35_summary",
            "035_trace_anchor_joint_declaration_inventory__candidate_group_35_status_summary",
            "g35_status_summary",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g35_declaration_obligations",
            "035_trace_anchor_joint_declaration_inventory__candidate_trace_anchor_declaration_obligations",
            "g35_declaration_obligations",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g34_summary",
            "034_safe_trace_membership_candidate_origin__candidate_group_34_status_summary",
            "g34_status_summary",
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
class DeclarationSymbols:
    L_trace_norm_declaration_preconditions: sp.Basic
    L_membership_declaration_preconditions: sp.Basic
    L_joint_declaration_preconditions: sp.Basic
    L_invalid_declaration_modes: sp.Basic
    L_downstream_closed: sp.Basic
    L_declaration_gap: sp.Basic


@dataclass
class DeclarationPrecondition:
    name: str
    component: str
    precondition: str
    status: str
    required_before: str
    blank_failure: str
    forbidden_upgrade: str


@dataclass
class CompletenessCheck:
    name: str
    check: str
    status: str
    passes_if: str
    fails_if: str
    boundary: str


@dataclass
class InvalidDeclarationUse:
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
class ConclusionEntry:
    name: str
    conclusion: str
    status: str
    meaning: str


# ----------------------------------------------------------------------------------------------------------------------
# Case builders
# ----------------------------------------------------------------------------------------------------------------------


def build_declaration_preconditions() -> list[DeclarationPrecondition]:
    return [
        DeclarationPrecondition(
            name="T1: B_s object convention precondition",
            component="trace normalization",
            precondition="B_s must be declared as scale-factor language, metric-coefficient language, or separate functional response before any N_trace form is used",
            status="PRECONDITION_REQUIRED",
            required_before="trace-normalization form comparison, theorem target, adoption record, or precondition handoff",
            blank_failure="factor-of-two ambiguity remains and zeta/d versus 2*zeta/d cannot be interpreted",
            forbidden_upgrade="must not choose B_s convention from Schwarzschild recovery, insertion convenience, or parent fit",
        ),
        DeclarationPrecondition(
            name="T2: zeta trace convention precondition",
            component="trace normalization",
            precondition="zeta must be declared as total volume-log trace, per-dimension normalized trace, or another explicitly scoped trace convention",
            status="PRECONDITION_REQUIRED",
            required_before="any statement that B_s reads zeta",
            blank_failure="dimension factors can hide in notation",
            forbidden_upgrade="must not hide normalization by redefining zeta after compatibility tests",
        ),
        DeclarationPrecondition(
            name="T3: traced dimension precondition",
            component="trace normalization",
            precondition="the traced sector dimension d and sector basis must be explicit",
            status="PRECONDITION_REQUIRED",
            required_before="using zeta/d, 2*zeta/d, or per-dimension notation",
            blank_failure="dimensional trace forms are not well-posed",
            forbidden_upgrade="must not select d after recovery or insertion targets are known",
        ),
        DeclarationPrecondition(
            name="T4: exact versus linearized scope precondition",
            component="trace normalization",
            precondition="the form must be marked exact determinant/volume structure or first-order bookkeeping only",
            status="PRECONDITION_REQUIRED",
            required_before="theorem route, adoption route, or any exact precondition route",
            blank_failure="linearized bookkeeping may be overclaimed as exact law",
            forbidden_upgrade="must not promote first-order compatibility into exact trace law",
        ),
        DeclarationPrecondition(
            name="M1: zeta_Bs object precondition",
            component="safe membership",
            precondition="zeta_Bs must be declared as an object with role and payload type before membership is tested",
            status="PRECONDITION_REQUIRED",
            required_before="zeta_Bs -> T_zeta membership criterion or theorem route",
            blank_failure="membership remains a label rather than a testable assignment",
            forbidden_upgrade="must not let zeta_Bs carry residual, ordinary-source, correction, boundary, support, or insertion payload",
        ),
        DeclarationPrecondition(
            name="M2: T_zeta sector precondition",
            component="safe membership",
            precondition="T_zeta must have a declared sector basis and accepted trace content",
            status="PRECONDITION_REQUIRED",
            required_before="safe-membership compatibility, theorem target, or adoption record",
            blank_failure="T_zeta label can be mistaken for proof of membership",
            forbidden_upgrade="must not imply incidence, active O, residual kill, or insertion",
        ),
        DeclarationPrecondition(
            name="M3: domain and codomain precondition",
            component="safe membership",
            precondition="membership domain and codomain for zeta_Bs -> T_zeta must be visible",
            status="PRECONDITION_REQUIRED",
            required_before="any typed membership claim",
            blank_failure="membership claim is not well-posed",
            forbidden_upgrade="must not include residual/source/correction/downstream zones by convenience",
        ),
        DeclarationPrecondition(
            name="M4: membership criterion precondition",
            component="safe membership",
            precondition="the criterion by which zeta_Bs belongs to T_zeta must be stated before use",
            status="PRECONDITION_REQUIRED",
            required_before="safe-membership theorem attempt or explicit adoption record",
            blank_failure="sector assignment remains unsupported",
            forbidden_upgrade="must not imply trace/residual zero incidence or residual control",
        ),
        DeclarationPrecondition(
            name="M5: role-purity and exclusion-zone precondition",
            component="safe membership",
            precondition="residual, ordinary-source, correction/divergence, boundary/support, and downstream payload exclusions must be explicit",
            status="PRECONDITION_REQUIRED",
            required_before="role-pure membership use or Package B precondition handoff",
            blank_failure="membership can become a hidden-load pocket",
            forbidden_upgrade="must not become source no-double-counting theorem, divergence safety, or residual kill",
        ),
        DeclarationPrecondition(
            name="M6: diagnostic versus active scope precondition",
            component="safe membership",
            precondition="membership must be marked diagnostic-only/inert or active theorem/adoption target",
            status="PRECONDITION_REQUIRED",
            required_before="future downstream use of membership language",
            blank_failure="diagnostic label may be used as active operator",
            forbidden_upgrade="diagnostic-only labels must not alter equations",
        ),
        DeclarationPrecondition(
            name="J1: node-separation precondition",
            component="joint trace anchor",
            precondition="P_trace_norm and P_safe_membership must remain separate nodes",
            status="PRECONDITION_REQUIRED",
            required_before="joint Package B use, mixed-status handoff, or precondition inventory",
            blank_failure="Package B can collapse into one hidden choice",
            forbidden_upgrade="normalization must not choose membership and membership must not choose normalization",
        ),
        DeclarationPrecondition(
            name="J2: component status-mode precondition",
            component="joint trace anchor",
            precondition="each component must carry a visible status mode before handoff",
            status="STATUS_REQUIRED",
            required_before="theorem, adoption, explicit declaration, or insertion-facing precondition route",
            blank_failure="compatible-if-declared can drift into selected/adopted/derived language",
            forbidden_upgrade="status mode classification must not assign theory status",
        ),
    ]


def build_completeness_checks() -> list[CompletenessCheck]:
    return [
        CompletenessCheck(
            name="Ck1: trace-normalization declaration completeness",
            check="B_s convention + zeta convention + d + exact/linearized scope must be simultaneously visible",
            status="BLOCKED_IF_BLANK",
            passes_if="all trace-normalization slots are filled in a separate declaration record",
            fails_if="any factor, convention, dimension, or scope is implicit",
            boundary="complete declarations still do not select, adopt, or derive trace normalization",
        ),
        CompletenessCheck(
            name="Ck2: safe-membership declaration completeness",
            check="zeta_Bs + T_zeta + domain + codomain + criterion + role purity + diagnostic/active scope must be simultaneously visible",
            status="BLOCKED_IF_BLANK",
            passes_if="all membership slots are filled in a separate declaration record",
            fails_if="membership is only a label or criterion remains missing",
            boundary="complete declarations still do not prove membership",
        ),
        CompletenessCheck(
            name="Ck3: node-separation completeness",
            check="normalization and membership must be listed as separate Package B nodes with separate status modes",
            status="PRECONDITION_REQUIRED",
            passes_if="both nodes remain independently auditable",
            fails_if="one node silently chooses, licenses, or substitutes for the other",
            boundary="node separation is not Package B adoption",
        ),
        CompletenessCheck(
            name="Ck4: mixed-status visibility",
            check="if component statuses differ, the mixed status must be explicitly recorded",
            status="STATUS_REQUIRED",
            passes_if="future handoff states the status of each node independently",
            fails_if="Package B is described as uniformly declared, adopted, derived, or ready when only one component has changed status",
            boundary="mixed status is an obligation, not a recommendation",
        ),
        CompletenessCheck(
            name="Ck5: downstream gate completeness",
            check="insertion, active O, residual control, and parent closure must remain marked not ready unless separately derived",
            status="NOT_READY",
            passes_if="future handoff keeps downstream gates separate from declaration clarity",
            fails_if="complete declarations are treated as insertion or parent readiness",
            boundary="declaration completeness is not field-equation use",
        ),
    ]


def build_invalid_uses() -> list[InvalidDeclarationUse]:
    return [
        InvalidDeclarationUse(
            name="X1: blank slot used as declaration",
            shortcut="use a Package B component while one or more required declaration preconditions remain blank",
            status="FORBIDDEN_SHORTCUT",
            reason="compatible-if-declared status is conditional on actual declarations",
            failure_mode="hidden declaration enters later theorem/adoption/precondition work",
        ),
        InvalidDeclarationUse(
            name="X2: declaration precondition as declaration value",
            shortcut="treat the required declaration slot itself as if its value were filled",
            status="FORBIDDEN_SHORTCUT",
            reason="a precondition names a blank; it does not fill the blank",
            failure_mode="inventory becomes declaration record by prose drift",
        ),
        InvalidDeclarationUse(
            name="X3: declaration completeness as adoption",
            shortcut="treat a complete declaration set as Package B adoption",
            status="FORBIDDEN_SHORTCUT",
            reason="adoption requires a separate explicit user/theory decision",
            failure_mode="declared candidate becomes postulate by shortcut",
        ),
        InvalidDeclarationUse(
            name="X4: declaration completeness as theorem proof",
            shortcut="treat declared conventions or criteria as proof of trace normalization or safe membership",
            status="FORBIDDEN_SHORTCUT",
            reason="declarations define terms and assumptions; they do not prove field behavior",
            failure_mode="theorem burden disappears by naming",
        ),
        InvalidDeclarationUse(
            name="X5: declaration completeness as insertion",
            shortcut="treat filled declaration slots as B_s/F_zeta insertion readiness",
            status="FORBIDDEN_SHORTCUT",
            reason="insertion remains downstream and not ready",
            failure_mode="declarations become metric insertion handle",
        ),
        InvalidDeclarationUse(
            name="X6: declaration completeness as parent readiness",
            shortcut="open the parent field equation from declaration clarity",
            status="FORBIDDEN_SHORTCUT",
            reason="parent closure remains blocked by recombination and safety gates",
            failure_mode="parent gate opens prematurely",
        ),
    ]


def build_obligations() -> list[LedgerObligation]:
    return [
        LedgerObligation(
            name="O1: trace-normalization declaration preconditions",
            obligation="keep B_s convention, zeta convention, traced dimension, exact/linearized scope, and status mode visible before trace-normalization use",
            status="OPEN",
            blocks="trace-normalization theorem, adoption, or precondition handoff",
            discipline="preconditions remain blank until a separate declaration record fills them",
        ),
        LedgerObligation(
            name="O2: safe-membership declaration preconditions",
            obligation="keep zeta_Bs object, T_zeta sector, domain/codomain, membership criterion, role purity, and diagnostic/active scope visible before membership use",
            status="OPEN",
            blocks="safe-membership theorem, adoption, or precondition handoff",
            discipline="label visibility is prerequisite, not proof",
        ),
        LedgerObligation(
            name="O3: node-separation precondition",
            obligation="keep P_trace_norm and P_safe_membership separate in all future declaration and precondition routes",
            status="OPEN",
            blocks="Package B collapse",
            discipline="one node cannot choose or license the other",
        ),
        LedgerObligation(
            name="O4: status-mode precondition",
            obligation="require explicit component status modes before theorem/adoption/precondition handoff",
            status="OPEN",
            blocks="ambiguous downstream handoff",
            discipline="current status remains compatible-if-declared unless later changed explicitly",
        ),
        LedgerObligation(
            name="O5: adoption boundary",
            obligation="do not adopt Package B or either component in this declaration precondition ledger",
            status="REQUIRED",
            blocks="accidental adoption",
            discipline="adoption requires a separate explicit decision record",
        ),
        LedgerObligation(
            name="O6: downstream gates",
            obligation="keep B_s/F_zeta insertion, active O, residual control, and parent closure closed",
            status="NOT_READY",
            blocks="downstream overreach",
            discipline="declaration preconditions are not insertion or parent readiness",
        ),
    ]


def build_conclusions() -> list[ConclusionEntry]:
    return [
        ConclusionEntry(
            name="C1: declaration preconditions inventoried",
            conclusion="trace-normalization, safe-membership, node-separation, and status-mode declaration preconditions are visible",
            status="PRECONDITION_REQUIRED",
            meaning="later work can see which declaration locks must be explicit before use",
        ),
        ConclusionEntry(
            name="C2: slots remain unfilled",
            conclusion="this ledger fills no declaration slots",
            status="NOT_CHOSEN",
            meaning="precondition ledger is not a declaration record",
        ),
        ConclusionEntry(
            name="C3: status remains unassigned",
            conclusion="this ledger assigns no Package B component status as theory state",
            status="NOT_CHOSEN",
            meaning="status mode remains a precondition, not a state change",
        ),
        ConclusionEntry(
            name="C4: no adoption or theorem proof",
            conclusion="no trace-normalization or safe-membership form is selected, adopted, or derived",
            status="NOT_ADOPTED",
            meaning="explicit decision or theorem route remains separate",
        ),
        ConclusionEntry(
            name="C5: downstream gates closed",
            conclusion="B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready",
            status="NOT_READY",
            meaning="declaration preconditions do not open field-equation gates",
        ),
        ConclusionEntry(
            name="C6: next",
            conclusion="status precondition matrix should run next",
            status="OPEN",
            meaning="status assumptions can now be inventoried without assigning them",
        ),
    ]


# ----------------------------------------------------------------------------------------------------------------------
# Cases
# ----------------------------------------------------------------------------------------------------------------------


def case_0_problem() -> None:
    header("Case 0: Declaration precondition ledger problem")
    print(
        "Question:\n\n"
        "  Which declaration preconditions must be explicit before trace-normalization\n"
        "  and safe-membership Package B components can be used in later routes?\n\n"
        "Discipline:\n\n"
        "  This script inventories declaration preconditions.\n"
        "  It fills no declaration slot.\n"
        "  It assigns no Package B component status as theory state.\n"
        "  It selects no trace-normalization form.\n"
        "  It selects no safe-membership form.\n"
        "  It adopts no Package B component.\n"
        "  It recommends no Package B adoption.\n"
        "  It derives no coefficient law and no insertion.\n"
        "  It keeps active O, residual control, and parent closure closed.\n\n"
        "Tiny goblin rule:\n"
        "  Inspect the lock pins. Do not turn the key.\n"
    )
    out_line(
        "governance_assessments",
        "PASS",
        "declaration precondition ledger opened",
        "declaration slots are audited as preconditions only; no values are filled",
    )


def case_1_symbolic_ledger() -> DeclarationSymbols:
    header("Case 1: Declaration precondition symbolic ledger")

    B_s_decl, zeta_decl, d_decl, exact_scope, N_trace_status = sp.symbols(
        "B_s_decl zeta_decl d_decl exact_scope N_trace_status"
    )
    zeta_Bs_decl, T_zeta_decl, domain_decl, codomain_decl = sp.symbols(
        "zeta_Bs_decl T_zeta_decl domain_decl codomain_decl"
    )
    membership_criterion, role_purity, diagnostic_scope = sp.symbols(
        "membership_criterion role_purity diagnostic_scope"
    )
    node_separation, component_status_mode, mixed_status = sp.symbols(
        "node_separation component_status_mode mixed_status"
    )
    blank_slot, hidden_declaration, scope_mismatch, node_collapse = sp.symbols(
        "blank_slot hidden_declaration scope_mismatch node_collapse"
    )
    P_insertion, P_active_O, P_residual_kill, P_parent = sp.symbols(
        "P_insertion P_active_O P_residual_kill P_parent"
    )

    L_trace = sp.simplify(B_s_decl + zeta_decl + d_decl + exact_scope + N_trace_status)
    L_membership = sp.simplify(
        zeta_Bs_decl + T_zeta_decl + domain_decl + codomain_decl + membership_criterion + role_purity + diagnostic_scope
    )
    L_joint = sp.simplify(node_separation + component_status_mode + mixed_status)
    L_invalid = sp.simplify(blank_slot + hidden_declaration + scope_mismatch + node_collapse)
    L_downstream = sp.simplify(P_insertion + P_active_O + P_residual_kill + P_parent)
    L_gap = sp.simplify(L_trace + L_membership + L_joint + L_invalid + L_downstream)

    print("Declaration-precondition symbols:")
    for sym in [
        B_s_decl, zeta_decl, d_decl, exact_scope, N_trace_status,
        zeta_Bs_decl, T_zeta_decl, domain_decl, codomain_decl,
        membership_criterion, role_purity, diagnostic_scope,
        node_separation, component_status_mode, mixed_status,
        blank_slot, hidden_declaration, scope_mismatch, node_collapse,
        P_insertion, P_active_O, P_residual_kill, P_parent,
    ]:
        print(f"  {sym} = {sym}")

    print()
    print(f"Trace-normalization declaration-precondition load:\n  L_trace_norm_declaration_preconditions = {L_trace}")
    print(f"Safe-membership declaration-precondition load:\n  L_membership_declaration_preconditions = {L_membership}")
    print(f"Joint declaration-precondition load:\n  L_joint_declaration_preconditions = {L_joint}")
    print(f"Invalid declaration mode load:\n  L_invalid_declaration_modes = {L_invalid}")
    print(f"Downstream closed load:\n  L_downstream_closed = {L_downstream}")
    print(f"Declaration-precondition gap:\n  L_declaration_gap = {L_gap}")

    out_line(
        "derived_results",
        "PASS",
        "declaration-precondition symbolic loads stated",
        f"L_joint_declaration_preconditions={L_joint}; L_downstream_closed={L_downstream}",
    )

    return DeclarationSymbols(L_trace, L_membership, L_joint, L_invalid, L_downstream, L_gap)


def case_2_declaration_preconditions(items: Iterable[DeclarationPrecondition]) -> None:
    header("Case 2: Declaration precondition slots")
    for item in items:
        subheader(item.name)
        print(f"Component: {item.component}")
        print(f"Precondition: {item.precondition}")
        out_line("governance_assessments", item.status, item.name)
        print(f"Required before: {item.required_before}")
        print(f"Blank failure: {item.blank_failure}")
        print(f"Forbidden upgrade: {item.forbidden_upgrade}")
    out_line("governance_assessments", "PASS", "declaration precondition slots inventoried", f"{len(list(items)) if not isinstance(items, list) else len(items)} precondition slots stated")


def case_3_completeness_checks(items: Iterable[CompletenessCheck]) -> None:
    header("Case 3: Declaration completeness checks")
    for item in items:
        subheader(item.name)
        print(f"Check: {item.check}")
        out_line("governance_assessments", item.status, item.name)
        print(f"Passes if: {item.passes_if}")
        print(f"Fails if: {item.fails_if}")
        print(f"Boundary: {item.boundary}")
    out_line("governance_assessments", "OBLIGATION", "declaration completeness checks stated", f"{len(list(items)) if not isinstance(items, list) else len(items)} checks stated")


def case_4_invalid_uses(items: Iterable[InvalidDeclarationUse]) -> None:
    header("Case 4: Invalid declaration-precondition uses")
    for item in items:
        subheader(item.name)
        print(f"Shortcut: {item.shortcut}")
        out_line("counterexamples", item.status, item.name)
        print(f"Reason: {item.reason}")
        print(f"Failure mode: {item.failure_mode}")
    out_line("counterexamples", "FAIL", "invalid declaration-precondition uses rejected", f"{len(list(items)) if not isinstance(items, list) else len(items)} shortcuts rejected")


def case_5_obligations(items: Iterable[LedgerObligation]) -> None:
    header("Case 5: Declaration-precondition obligations")
    for item in items:
        subheader(item.name)
        print(f"Obligation: {item.obligation}")
        out_line("unresolved_obligations", item.status, item.name)
        print(f"Blocks: {item.blocks}")
        print(f"Discipline: {item.discipline}")
    out_line("unresolved_obligations", "OBLIGATION", "declaration-precondition obligations opened", f"{len(list(items)) if not isinstance(items, list) else len(items)} obligations stated")


def case_6_conclusions(items: Iterable[ConclusionEntry]) -> None:
    header("Case 6: Declaration-precondition conclusions")
    for item in items:
        subheader(item.name)
        print(f"Conclusion: {item.conclusion}")
        out_line("governance_assessments", item.status, item.name)
        print(f"Meaning: {item.meaning}")
    out_line(
        "governance_assessments",
        "PASS",
        "declaration precondition ledger conclusion stated",
        "declaration preconditions inventoried; no slots filled, no status assigned, downstream gates closed",
    )


def final_interpretation() -> None:
    header("Final interpretation")
    print(
        "Trace-anchor declaration precondition ledger result:\n\n"
        "  Declaration preconditions for trace normalization and safe membership are now inventoried.\n"
        "  Trace-normalization preconditions include B_s convention, zeta convention, traced dimension, exact/linearized scope, and status mode.\n"
        "  Safe-membership preconditions include zeta_Bs object, T_zeta sector, domain/codomain, membership criterion, role purity, and diagnostic/active scope.\n"
        "  Joint preconditions preserve node separation, status-mode visibility, and mixed-status visibility.\n"
        "  Blank-slot, declaration-as-value, adoption, theorem-proof, insertion, and parent-readiness shortcuts fail.\n"
        "  No declaration value is filled by this ledger.\n"
        "  No Package B component status is assigned as theory state.\n"
        "  No trace-normalization or safe-membership form is selected, adopted, or derived.\n"
        "  Package B is not recommended for adoption.\n"
        "  B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready.\n\n"
        "Possible next script:\n"
        "  candidate_trace_anchor_status_precondition_matrix.py\n\n"
        "Tiny goblin label:\n"
        "  Inspect the lock pins. Do not turn the key.\n"
    )
    out_line(
        "governance_assessments",
        "PASS",
        "trace-anchor declaration precondition ledger complete",
        "status precondition matrix should run next; adoption and downstream gates remain closed",
    )


# ----------------------------------------------------------------------------------------------------------------------
# Archive records
# ----------------------------------------------------------------------------------------------------------------------


def record_inventory_marker(ns, symbolic: DeclarationSymbols) -> None:
    ns.record_derivation(
        derivation_id="g36_decl_precond_ledger",
        inputs=[
            symbolic.L_trace_norm_declaration_preconditions,
            symbolic.L_membership_declaration_preconditions,
            symbolic.L_joint_declaration_preconditions,
            symbolic.L_invalid_declaration_modes,
            symbolic.L_downstream_closed,
        ],
        output=symbolic.L_declaration_gap,
        method="Group 36 trace-anchor declaration precondition ledger",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="declaration_precondition_ledger_marker",
        is_placeholder=True,
    )


def record_obligations(ns, obligations: Iterable[LedgerObligation]) -> None:
    for item in obligations:
        ident = safe_ident(item.name)
        status = ObligationStatus.OPEN if item.status != "NOT_READY" else ObligationStatus.DEFERRED
        ns.record_obligation(
            ProofObligationRecord(
                obligation_id=f"g36_decl_{ident}",
                script_id=SCRIPT_ID,
                title=item.name,
                status=status,
                required_by=[SCRIPT_ID],
                description=f"{item.obligation}. Blocks: {item.blocks}. Discipline: {item.discipline}.",
            )
        )


def record_governance(
    ns,
    preconditions: Iterable[DeclarationPrecondition],
    checks: Iterable[CompletenessCheck],
    invalid_uses: Iterable[InvalidDeclarationUse],
) -> None:
    ns.record_route(
        RouteRecord(
            route_id="g36_decl_precond",
            script_id=SCRIPT_ID,
            name="Trace-anchor declaration precondition ledger route",
            status=GovernanceStatus.CANDIDATE_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            required_obligations=[
                "g36_decl_o1",
                "g36_decl_o2",
                "g36_decl_o3",
                "g36_decl_o4",
                "g36_decl_o5",
                "g36_decl_o6",
            ],
            activation_conditions=[
                "Group 36 precondition inventory opener complete",
                "declaration preconditions inventoried only",
                "no declaration slots filled",
                "no component status assigned",
                "no Package B component adopted",
                "downstream gates closed",
            ],
        )
    )

    for item in preconditions:
        ident = safe_ident(item.name)
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g36_decl_pc_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.CANDIDATE_ROUTE,
                statement=(
                    f"Declaration precondition for {item.component}: {item.precondition}. "
                    f"Required before: {item.required_before}. Blank failure: {item.blank_failure}. "
                    f"Forbidden upgrade: {item.forbidden_upgrade}."
                ),
                derivation_ids=["g36_decl_precond_ledger"],
                obligation_ids=[],
            )
        )

    for item in checks:
        ident = safe_ident(item.name)
        status = GovernanceStatus.CANDIDATE_ROUTE
        if item.status in {"NOT_READY", "BLOCKED_IF_BLANK"}:
            status = GovernanceStatus.DEFERRED_PENDING_PREREQUISITES
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g36_decl_ck_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=status,
                statement=(
                    f"Completeness check: {item.check}. Passes if: {item.passes_if}. "
                    f"Fails if: {item.fails_if}. Boundary: {item.boundary}."
                ),
                derivation_ids=["g36_decl_precond_ledger"],
                obligation_ids=[],
            )
        )

    for item in invalid_uses:
        ident = safe_ident(item.name)
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g36_decl_x_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.REJECTED_ROUTE,
                statement=f"Forbidden declaration-precondition shortcut: {item.shortcut}. Reason: {item.reason}. Failure mode: {item.failure_mode}.",
                derivation_ids=["g36_decl_precond_ledger"],
                obligation_ids=[],
            )
        )

    policy_rules = [
        ("g36_decl_pol_blank", "Declaration precondition inventory names blank slots but does not fill them."),
        ("g36_decl_pol_status", "Declaration precondition inventory assigns no Package B component status as theory state."),
        ("g36_decl_pol_adopt", "Declaration precondition inventory adopts no Package B component."),
        ("g36_decl_pol_insert", "Declaration precondition inventory does not license insertion, active O, residual control, or parent closure."),
    ]
    for claim_id, statement in policy_rules:
        ns.record_claim(
            ClaimRecord(
                claim_id=claim_id,
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.POLICY_RULE,
                statement=statement,
                derivation_ids=["g36_decl_precond_ledger"],
                obligation_ids=[],
            )
        )


# ----------------------------------------------------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------------------------------------------------


def main() -> None:
    header("Candidate Trace Anchor Declaration Precondition Ledger")
    archive, ns, invalidated = prepare_archive()
    ensure_archive_write_dirs(ns)
    print_archive_status(ns, invalidated)

    preconditions = build_declaration_preconditions()
    checks = build_completeness_checks()
    invalid_uses = build_invalid_uses()
    obligations = build_obligations()
    conclusions = build_conclusions()

    case_0_problem()
    symbolic = case_1_symbolic_ledger()
    case_2_declaration_preconditions(preconditions)
    case_3_completeness_checks(checks)
    case_4_invalid_uses(invalid_uses)
    case_5_obligations(obligations)
    case_6_conclusions(conclusions)
    final_interpretation()

    record_inventory_marker(ns, symbolic)
    record_obligations(ns, obligations)
    record_governance(ns, preconditions, checks, invalid_uses)

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
