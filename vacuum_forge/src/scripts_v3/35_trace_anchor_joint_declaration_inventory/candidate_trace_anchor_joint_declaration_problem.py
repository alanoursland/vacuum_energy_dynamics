# Candidate Trace Anchor Joint Declaration Problem
#
# Group:
#   35_trace_anchor_joint_declaration_inventory
#
# Human title:
#   Trace Anchor Joint Declaration Inventory
#
# Script type:
#   PROBLEM LEDGER / JOINT-DECLARATION ROUTE OPENER
#
# Purpose
# -------
# Open Group 35 by asking what declarations must be made before the
# trace-normalization and safe-membership components of Package B can be
# jointly used.
#
# This script does not select trace normalization.
# It does not adopt trace normalization.
# It does not select safe membership.
# It does not adopt safe membership.
# It does not recommend Package B adoption.
# It does not derive a coefficient law or insertion.
# It does not open active O, residual control, or parent closure.
#
# Tiny goblin rule:
#   Put the two cups on the same table. Still do not drink.

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
        "ADMISSIBLE_DECLARATION_SURFACE": StatusMark.INFO,
        "COMPATIBILITY_ONLY": StatusMark.INFO,
        "COMPATIBLE_IF_DECLARED": StatusMark.INFO,
        "CONDITIONAL": StatusMark.DEFER,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
        "JOINT_DECLARATION_ROUTE": StatusMark.INFO,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REQUIRED": StatusMark.OBLIGATION,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g34_summary",
            "34_safe_trace_membership_candidate_origin__candidate_group_34_status_summary",
            "g34_status_summary",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g34_obligations",
            "34_safe_trace_membership_candidate_origin__candidate_safe_trace_membership_obligations",
            "g34_safe_membership_obligations",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g33_summary",
            "33_trace_normalization_candidate_origin__candidate_group_33_status_summary",
            "g33_status_summary",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g33_obligations",
            "33_trace_normalization_candidate_origin__candidate_trace_normalization_obligations",
            "g33_trace_normalization_obligations",
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
class JointSymbols:
    P_trace_norm: sp.Symbol
    P_safe_membership: sp.Symbol
    B_s_decl: sp.Symbol
    zeta_decl: sp.Symbol
    d_decl: sp.Symbol
    exact_scope: sp.Symbol
    membership_criterion: sp.Symbol
    role_purity: sp.Symbol
    norm_membership_separation: sp.Symbol
    adoption_status: sp.Symbol
    P_insertion: sp.Symbol
    P_active_O: sp.Symbol
    P_residual_kill: sp.Symbol
    P_parent: sp.Symbol
    L_trace_norm_declarations: sp.Basic
    L_membership_declarations: sp.Basic
    L_joint_declaration_surface: sp.Basic
    L_downstream_closed: sp.Basic
    L_problem_gap: sp.Basic


@dataclass
class DeclarationSurface:
    name: str
    declaration: str
    status: str
    meaning: str
    required_before: str
    forbidden_upgrade: str


@dataclass
class RouteEntry:
    name: str
    route: str
    status: str
    allowed_use: str
    forbidden_use: str
    next_test: str


@dataclass
class RejectedShortcut:
    name: str
    shortcut: str
    status: str
    reason: str
    failure_mode: str


@dataclass
class OpeningObligation:
    name: str
    obligation: str
    status: str
    blocks: str
    discipline: str


@dataclass
class Conclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_symbols() -> JointSymbols:
    P_trace_norm, P_safe_membership = sp.symbols("P_trace_norm P_safe_membership")
    B_s_decl, zeta_decl, d_decl = sp.symbols("B_s_decl zeta_decl d_decl")
    exact_scope, membership_criterion = sp.symbols("exact_scope membership_criterion")
    role_purity, norm_membership_separation = sp.symbols("role_purity norm_membership_separation")
    adoption_status = sp.symbols("adoption_status")
    P_insertion, P_active_O, P_residual_kill, P_parent = sp.symbols(
        "P_insertion P_active_O P_residual_kill P_parent"
    )

    L_trace_norm_declarations = sp.simplify(B_s_decl + zeta_decl + d_decl + exact_scope)
    L_membership_declarations = sp.simplify(membership_criterion + role_purity)
    L_joint_declaration_surface = sp.simplify(
        L_trace_norm_declarations + L_membership_declarations + norm_membership_separation + adoption_status
    )
    L_downstream_closed = sp.simplify(P_insertion + P_active_O + P_residual_kill + P_parent)
    L_problem_gap = sp.simplify(
        P_trace_norm
        + P_safe_membership
        + L_joint_declaration_surface
        + L_downstream_closed
    )

    return JointSymbols(
        P_trace_norm,
        P_safe_membership,
        B_s_decl,
        zeta_decl,
        d_decl,
        exact_scope,
        membership_criterion,
        role_purity,
        norm_membership_separation,
        adoption_status,
        P_insertion,
        P_active_O,
        P_residual_kill,
        P_parent,
        L_trace_norm_declarations,
        L_membership_declarations,
        L_joint_declaration_surface,
        L_downstream_closed,
        L_problem_gap,
    )


def build_declaration_surfaces() -> List[DeclarationSurface]:
    return [
        DeclarationSurface(
            "D1: B_s object convention",
            "declare whether B_s is scale-factor language, metric-coefficient language, or separate functional response",
            "ADMISSIBLE_DECLARATION_SURFACE",
            "Group 33 showed that the factor differs by object convention",
            "trace-normalization form use",
            "must not be chosen from recovery, insertion, or parent fit",
        ),
        DeclarationSurface(
            "D2: zeta trace convention",
            "declare whether zeta is total volume-log trace or per-dimension normalized trace",
            "ADMISSIBLE_DECLARATION_SURFACE",
            "per-dimension notation can hide the dimension factor",
            "trace-normalization comparison",
            "must not hide normalization in notation",
        ),
        DeclarationSurface(
            "D3: traced dimension",
            "declare the traced sector dimension d before using zeta/d or 2*zeta/d",
            "ADMISSIBLE_DECLARATION_SURFACE",
            "dimension count is part of the trace convention",
            "dimensional trace forms",
            "must not be selected after recovery is known",
        ),
        DeclarationSurface(
            "D4: exact versus linearized scope",
            "declare whether the trace form is exact determinant/volume structure or first-order only",
            "ADMISSIBLE_DECLARATION_SURFACE",
            "linearized trace survives only as first-order bookkeeping",
            "theorem or adoption use",
            "must not upgrade first-order success to exact law",
        ),
        DeclarationSurface(
            "D5: membership criterion",
            "declare the criterion by which zeta_Bs belongs to T_zeta",
            "ADMISSIBLE_DECLARATION_SURFACE",
            "a T_zeta label is not proof of membership",
            "safe-membership theorem/adoption use",
            "must not imply incidence or residual kill",
        ),
        DeclarationSurface(
            "D6: role-purity and exclusion zones",
            "declare how residual, source, correction, and downstream payloads remain outside membership",
            "ADMISSIBLE_DECLARATION_SURFACE",
            "role-pure membership survives only if hidden payloads are excluded",
            "safe-membership compatibility",
            "must not become source theorem, divergence safety, or residual control",
        ),
        DeclarationSurface(
            "D7: normalization/membership separation",
            "declare that P_trace_norm and P_safe_membership remain separate nodes unless explicitly adopted otherwise",
            "REQUIRED",
            "Package B must not collapse into one hidden choice",
            "joint Package B use",
            "must not let normalization choose membership or membership choose normalization",
        ),
        DeclarationSurface(
            "D8: adoption/theorem status",
            "declare whether each component is theorem target, explicit candidate, adopted postulate, or deferred",
            "REQUIRED",
            "downstream work needs status clarity before any use",
            "handoffs after Group 35",
            "must not treat compatible-if-declared as adopted or derived",
        ),
    ]


def build_routes() -> List[RouteEntry]:
    return [
        RouteEntry(
            "R1: joint declaration ledger",
            "inventory all declarations required for both Package B candidate nodes",
            "JOINT_DECLARATION_ROUTE",
            "make the combined declaration surface visible",
            "must not choose the declarations by convenience",
            "component declaration ledger should run next",
        ),
        RouteEntry(
            "R2: theorem-after-declarations route",
            "attempt theorem support only after conventions and membership criteria are declared",
            "CONDITIONAL",
            "possible later theorem path",
            "must not treat declaration as proof",
            "status-mode sieve should distinguish theorem target from adopted postulate",
        ),
        RouteEntry(
            "R3: explicit decision route",
            "explicit user/theory decision may later adopt one or both Package B components",
            "CONDITIONAL",
            "possible later adoption path",
            "adopted postulate must not be called derived",
            "adoption record must be separate from this group",
        ),
        RouteEntry(
            "R4: conditional precondition inventory",
            "inventory downstream preconditions only under explicit adoption/theorem-status assumptions",
            "CONDITIONAL",
            "possible later inventory path",
            "must not become insertion theorem",
            "only after declaration/status mode is explicit",
        ),
    ]


def build_rejected_shortcuts() -> List[RejectedShortcut]:
    return [
        RejectedShortcut(
            "S1: compatible-if-declared as declared",
            "treat compatible-if-declared forms as if all conventions have already been declared",
            "FORBIDDEN_SHORTCUT",
            "compatibility survival is conditional",
            "hidden declaration choices enter later work",
        ),
        RejectedShortcut(
            "S2: declaration as adoption",
            "treat a declaration inventory as adoption of Package B components",
            "FORBIDDEN_SHORTCUT",
            "inventory is not explicit theory choice",
            "audit status becomes postulate status",
        ),
        RejectedShortcut(
            "S3: declaration as theorem",
            "treat a declared convention or criterion as physical derivation",
            "FORBIDDEN_SHORTCUT",
            "declaration can define terms but does not prove field behavior",
            "naming becomes proof",
        ),
        RejectedShortcut(
            "S4: joint declaration as insertion",
            "treat a coherent declaration package as B_s/F_zeta insertion",
            "FORBIDDEN_SHORTCUT",
            "insertion remains downstream and not ready",
            "precondition inventory becomes metric insertion",
        ),
        RejectedShortcut(
            "S5: joint declaration as parent readiness",
            "treat trace-anchor declaration clarity as parent equation closure",
            "FORBIDDEN_SHORTCUT",
            "parent field equation remains blocked by recombination and safety gates",
            "parent closure is opened prematurely",
        ),
    ]


def build_obligations() -> List[OpeningObligation]:
    return [
        OpeningObligation(
            "O1: component declaration ledger",
            "inventory B_s convention, zeta convention, d, scope, membership criterion, role purity, and status mode",
            "OPEN",
            "joint trace-anchor use",
            "all component declarations must be visible before compatibility/precondition claims",
        ),
        OpeningObligation(
            "O2: preserve compatible-if-declared boundary",
            "keep trace-normalization and safe-membership forms compatible-if-declared only unless later explicitly chosen or derived",
            "OPEN",
            "selection drift",
            "compatible-if-declared is not selected, adopted, or derived",
        ),
        OpeningObligation(
            "O3: preserve Package B node separation",
            "keep P_trace_norm and P_safe_membership as separate candidate nodes",
            "OPEN",
            "Package B collapse",
            "joint declaration is not node collapse",
        ),
        OpeningObligation(
            "O4: adoption boundary",
            "do not adopt either Package B component in this route opener",
            "REQUIRED",
            "governance integrity",
            "adoption requires a separate explicit decision record",
        ),
        OpeningObligation(
            "O5: downstream gates",
            "keep B_s/F_zeta insertion, active O, residual control, and parent closure closed",
            "NOT_READY",
            "downstream overreach",
            "joint declaration inventory is not insertion or parent readiness",
        ),
    ]


def build_conclusions() -> List[Conclusion]:
    return [
        Conclusion(
            "C1: route opened",
            "trace-anchor joint declaration inventory route is opened",
            "JOINT_DECLARATION_ROUTE",
            "next route after separate trace-normalization and safe-membership audits",
        ),
        Conclusion(
            "C2: declaration surface visible",
            "required declaration categories are initialized",
            "REQUIRED",
            "component declarations must be made before joint Package B use",
        ),
        Conclusion(
            "C3: no selection",
            "this opener selects no trace-normalization or safe-membership form",
            "NOT_DERIVED",
            "joint declaration problem is not component choice",
        ),
        Conclusion(
            "C4: no adoption",
            "this opener adopts no Package B component",
            "NOT_ADOPTED",
            "explicit decision remains separate",
        ),
        Conclusion(
            "C5: downstream gates",
            "B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready",
            "NOT_READY",
            "declaration inventory does not open downstream gates",
        ),
        Conclusion(
            "C6: next",
            "component declaration ledger should run next",
            "OPEN",
            "first concrete joint declaration audit",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Trace-anchor joint declaration problem")
    print("Question:\n")
    print("  What declarations must be made before trace normalization and safe membership")
    print("  can be jointly used, without treating compatible-if-declared status as")
    print("  adoption, derivation, insertion, or parent readiness?")
    print("\nDiscipline:\n")
    print("  This script opens a joint declaration inventory route.")
    print("  It adopts no trace-normalization postulate.")
    print("  It adopts no safe-membership postulate.")
    print("  It selects no Package B component form.")
    print("  It recommends no Package B adoption.")
    print("  It derives no coefficient law and no insertion.")
    print("  It keeps active O, residual control, and parent closure closed.")
    print("\nTiny goblin rule:")
    print("  Put the two cups on the same table. Still do not drink.")
    with out.governance_assessments():
        out.line(
            "trace-anchor joint declaration route opened",
            StatusMark.INFO,
            "opening joint declaration inventory after Group 33/34 compatible-if-declared audits",
        )


def case_1_symbolic_ledger(symbols: JointSymbols, out: ScriptOutput) -> None:
    header("Case 1: Joint declaration symbolic ledger")
    print("Trace-anchor symbols:")
    for name in [
        "P_trace_norm",
        "P_safe_membership",
        "B_s_decl",
        "zeta_decl",
        "d_decl",
        "exact_scope",
        "membership_criterion",
        "role_purity",
        "norm_membership_separation",
        "adoption_status",
        "P_insertion",
        "P_active_O",
        "P_residual_kill",
        "P_parent",
    ]:
        print(f"  {name} = {getattr(symbols, name)}")
    print("\nTrace-normalization declaration load:")
    print(f"  L_trace_norm_declarations = {symbols.L_trace_norm_declarations}")
    print("\nSafe-membership declaration load:")
    print(f"  L_membership_declarations = {symbols.L_membership_declarations}")
    print("\nJoint declaration surface load:")
    print(f"  L_joint_declaration_surface = {symbols.L_joint_declaration_surface}")
    print("\nDownstream closed load:")
    print(f"  L_downstream_closed = {symbols.L_downstream_closed}")
    print("\nJoint declaration problem gap:")
    print(f"  L_problem_gap = {symbols.L_problem_gap}")
    with out.derived_results():
        out.line(
            "joint declaration ledgers stated",
            StatusMark.OBLIGATION,
            f"L_joint_declaration_surface={symbols.L_joint_declaration_surface}; L_downstream_closed={symbols.L_downstream_closed}",
        )


def case_2_declaration_surfaces(items: List[DeclarationSurface], out: ScriptOutput) -> None:
    header("Case 2: Required declaration surfaces")
    with out.governance_assessments():
        for item in items:
            subheader(item.name)
            print(f"Declaration: {item.declaration}")
            out.line(item.name, status_mark(item.status), item.status)
            print(f"Meaning: {item.meaning}")
            print(f"Required before: {item.required_before}")
            print(f"Forbidden upgrade: {item.forbidden_upgrade}")
        out.line("declaration surfaces initialized", StatusMark.INFO, f"{len(items)} declaration surfaces initialized")


def case_3_routes(routes: List[RouteEntry], out: ScriptOutput) -> None:
    header("Case 3: Allowed future route types")
    with out.governance_assessments():
        for item in routes:
            subheader(item.name)
            print(f"Route: {item.route}")
            out.line(item.name, status_mark(item.status), item.status)
            print(f"Allowed use: {item.allowed_use}")
            print(f"Forbidden use: {item.forbidden_use}")
            print(f"Next test: {item.next_test}")
        out.line("future route types separated", StatusMark.DEFER, f"{len(routes)} routes stated without adopting or inserting")


def case_4_rejected_shortcuts(shortcuts: List[RejectedShortcut], out: ScriptOutput) -> None:
    header("Case 4: Rejected joint-declaration shortcuts")
    with out.counterexamples():
        for item in shortcuts:
            subheader(item.name)
            print(f"Shortcut: {item.shortcut}")
            out.line(item.name, status_mark(item.status), item.status)
            print(f"Reason: {item.reason}")
            print(f"Failure mode: {item.failure_mode}")
        out.line("joint-declaration shortcuts rejected", StatusMark.FAIL, f"{len(shortcuts)} shortcuts rejected")


def case_5_obligations(obligations: List[OpeningObligation], out: ScriptOutput) -> None:
    header("Case 5: Initial joint-declaration obligations")
    with out.unresolved_obligations():
        for item in obligations:
            subheader(item.name)
            print(f"Obligation: {item.obligation}")
            out.line(item.name, status_mark(item.status), item.status)
            print(f"Blocks: {item.blocks}")
            print(f"Discipline: {item.discipline}")
        out.line("initial joint-declaration obligations stated", StatusMark.OBLIGATION, f"{len(obligations)} obligations opened")


def case_6_conclusions(conclusions: List[Conclusion], out: ScriptOutput) -> None:
    header("Case 6: Initial joint-declaration conclusions")
    with out.governance_assessments():
        for item in conclusions:
            subheader(item.name)
            print(f"Conclusion: {item.conclusion}")
            out.line(item.name, status_mark(item.status), item.status)
            print(f"Meaning: {item.meaning}")
        out.line(
            "trace-anchor joint declaration problem conclusion stated",
            StatusMark.PASS,
            "joint declaration route opened; no Package B component selected or adopted; downstream gates closed",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Trace-anchor joint declaration opener result:\n")
    print("  Group 35 is opened as a joint declaration inventory route.")
    print("  Group 33 trace-normalization forms remain compatible-if-declared only.")
    print("  Group 34 safe-membership forms remain compatible-if-declared only.")
    print("  The required declarations for joint Package B use are now initialized.")
    print("  No trace-normalization form is selected, adopted, or derived.")
    print("  No safe-membership form is selected, adopted, or derived.")
    print("  Package B is not recommended for adoption.")
    print("  B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready.")
    print("\nPossible next script:")
    print("  candidate_trace_anchor_component_declaration_ledger.py")
    print("\nTiny goblin label:")
    print("  Put the two cups on the same table. Still do not drink.")
    with out.governance_assessments():
        out.line(
            "trace-anchor joint declaration opener complete",
            StatusMark.PASS,
            "component declaration ledger should run next; adoption and downstream gates remain closed",
        )


def record_inventory_marker(ns, symbols: JointSymbols) -> None:
    ns.record_derivation(
        derivation_id="g35_trace_anchor_joint_declaration_problem",
        inputs=[
            symbols.P_trace_norm,
            symbols.P_safe_membership,
            symbols.L_joint_declaration_surface,
            symbols.L_downstream_closed,
        ],
        output=symbols.L_problem_gap,
        method="Group 35 trace-anchor joint declaration problem ledger",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="problem_ledger_marker",
        is_placeholder=True,
    )


def record_obligations(ns, obligations: List[OpeningObligation]) -> None:
    for item in obligations:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_obligation(
            ProofObligationRecord(
                obligation_id=f"g35_joint_declaration_{ident}",
                script_id=SCRIPT_ID,
                title=item.name,
                status=ObligationStatus.OPEN if item.status != "NOT_READY" else ObligationStatus.DEFERRED,
                required_by=[SCRIPT_ID],
                description=f"{item.obligation} Blocks: {item.blocks}. Discipline: {item.discipline}.",
            )
        )


def record_governance(
    ns,
    declarations: List[DeclarationSurface],
    routes: List[RouteEntry],
    shortcuts: List[RejectedShortcut],
) -> None:
    obligation_ids = [
        "g35_joint_declaration_o1",
        "g35_joint_declaration_o2",
        "g35_joint_declaration_o3",
        "g35_joint_declaration_o4",
        "g35_joint_declaration_o5",
    ]

    ns.record_route(
        RouteRecord(
            route_id="g35_trace_anchor_joint_declaration_route",
            script_id=SCRIPT_ID,
            name="Group 35 trace-anchor joint declaration inventory route",
            status=GovernanceStatus.CANDIDATE_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            required_obligations=obligation_ids,
            activation_conditions=[
                "Group 33 closed trace normalization as compatible-if-declared audit",
                "Group 34 closed safe membership as compatible-if-declared audit",
                "Package B remains not selected and not adopted",
                "component declarations are required before any joint Package B use",
            ],
        )
    )

    for item in declarations:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g35_declaration_surface_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.CANDIDATE_ROUTE,
                statement=(
                    f"{item.declaration}. Meaning: {item.meaning}. "
                    f"Required before: {item.required_before}. Forbidden upgrade: {item.forbidden_upgrade}."
                ),
                derivation_ids=["g35_trace_anchor_joint_declaration_problem"],
                obligation_ids=obligation_ids,
            )
        )

    for item in routes:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g35_allowed_route_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.CANDIDATE_ROUTE,
                statement=(
                    f"{item.route}. Allowed use: {item.allowed_use}. "
                    f"Forbidden use: {item.forbidden_use}. Next test: {item.next_test}."
                ),
                derivation_ids=["g35_trace_anchor_joint_declaration_problem"],
                obligation_ids=obligation_ids,
            )
        )

    for item in shortcuts:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g35_rejected_shortcut_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.POLICY_RULE,
                statement=f"Rejected shortcut: {item.shortcut}. Reason: {item.reason}. Failure mode: {item.failure_mode}.",
                derivation_ids=["g35_trace_anchor_joint_declaration_problem"],
                obligation_ids=obligation_ids,
            )
        )

    ns.record_claim(
        ClaimRecord(
            claim_id="g35_joint_declaration_problem_opened",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.CANDIDATE_ROUTE,
            statement=(
                "Group 35 is opened as a trace-anchor joint declaration inventory. "
                "Trace-normalization and safe-membership candidate forms remain compatible-if-declared only; "
                "no Package B component is selected, adopted, or derived; downstream gates remain closed."
            ),
            derivation_ids=["g35_trace_anchor_joint_declaration_problem"],
            obligation_ids=obligation_ids,
        )
    )


def main() -> None:
    header("Candidate Trace Anchor Joint Declaration Problem")
    archive, ns, invalidated = prepare_archive()
    ensure_archive_write_dirs(ns)
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    declarations = build_declaration_surfaces()
    routes = build_routes()
    shortcuts = build_rejected_shortcuts()
    obligations = build_obligations()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_symbolic_ledger(symbols, out)
    case_2_declaration_surfaces(declarations, out)
    case_3_routes(routes, out)
    case_4_rejected_shortcuts(shortcuts, out)
    case_5_obligations(obligations, out)
    case_6_conclusions(conclusions, out)
    final_interpretation(out)

    record_inventory_marker(ns, symbols)
    record_obligations(ns, obligations)
    record_governance(ns, declarations, routes, shortcuts)

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
