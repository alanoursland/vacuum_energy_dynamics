# Candidate Trace Anchor Precondition Inventory Problem
#
# Group:
#   36_conditional_trace_anchor_precondition_inventory
#
# Human title:
#   Conditional Trace Anchor Precondition Inventory
#
# Script type:
#   PROBLEM LEDGER / CONDITIONAL-PRECONDITION ROUTE OPENER
#
# Purpose
# -------
# Open Group 36 by asking what has to be true before the trace-anchor
# package can be used in later precondition, theorem, adoption, or insertion
# routes.
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
#   Count the locks before touching the door.

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
        "AUDIT_READY": StatusMark.INFO,
        "COMPATIBILITY_ONLY": StatusMark.INFO,
        "CONDITIONAL": StatusMark.DEFER,
        "CONDITIONAL_AFTER_ADOPTION_OR_THEOREM_SUPPORT": StatusMark.DEFER,
        "CONDITIONAL_AFTER_DECLARATIONS": StatusMark.DEFER,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
        "HANDOFF_READY": StatusMark.INFO,
        "MIXED_STATUS_REQUIRES_RECORD": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_CHOSEN": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "PRECONDITION_REQUIRED": StatusMark.OBLIGATION,
        "REQUIRED": StatusMark.OBLIGATION,
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
            "g35_status_mode_sieve",
            "035_trace_anchor_joint_declaration_inventory__candidate_trace_anchor_status_mode_sieve",
            "g35_status_mode_sieve",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g35_joint_consistency_matrix",
            "035_trace_anchor_joint_declaration_inventory__candidate_trace_anchor_joint_consistency_matrix",
            "g35_joint_consistency_matrix",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g35_component_ledger",
            "035_trace_anchor_joint_declaration_inventory__candidate_trace_anchor_component_declaration_ledger",
            "g35_component_declaration_ledger",
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
class PreconditionSymbols:
    L_declaration_preconditions: sp.Basic
    L_status_preconditions: sp.Basic
    L_safety_preconditions: sp.Basic
    L_downstream_closed: sp.Basic
    L_problem_gap: sp.Basic


@dataclass
class PreconditionClass:
    name: str
    precondition: str
    status: str
    required_before: str
    discipline: str
    forbidden_upgrade: str


@dataclass
class ConditionalRoute:
    name: str
    route: str
    status: str
    allowed_use: str
    blocked_until: str
    caution: str


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
class ConclusionEntry:
    name: str
    conclusion: str
    status: str
    meaning: str


# ----------------------------------------------------------------------------------------------------------------------
# Builders
# ----------------------------------------------------------------------------------------------------------------------


def build_preconditions() -> list[PreconditionClass]:
    return [
        PreconditionClass(
            name="P1: declaration slots explicit",
            precondition="B_s convention, zeta convention, traced dimension, scope, zeta_Bs object, T_zeta sector, domain/codomain, criterion, role purity, and diagnostic/active scope must be explicit",
            status="PRECONDITION_REQUIRED",
            required_before="any joint Package B theorem, adoption, precondition, or handoff use",
            discipline="Group 35 inventory made blanks visible but did not fill them",
            forbidden_upgrade="must not treat compatible-if-declared as declared",
        ),
        PreconditionClass(
            name="P2: component status modes explicit",
            precondition="P_trace_norm and P_safe_membership must each carry visible status mode",
            status="PRECONDITION_REQUIRED",
            required_before="theorem/adoption/precondition handoff",
            discipline="current status remains compatible-if-declared unless changed explicitly",
            forbidden_upgrade="must not hide mixed or deferred status",
        ),
        PreconditionClass(
            name="P3: node separation preserved",
            precondition="trace normalization and safe membership remain separate Package B nodes",
            status="PRECONDITION_REQUIRED",
            required_before="joint trace-anchor use",
            discipline="normalization cannot choose membership and membership cannot choose normalization",
            forbidden_upgrade="must not collapse Package B into one hidden choice",
        ),
        PreconditionClass(
            name="P4: role purity and hidden-load exclusion",
            precondition="membership payload excludes residual, ordinary source, correction/divergence, boundary/support, and downstream payloads",
            status="PRECONDITION_REQUIRED",
            required_before="safe-membership theorem/adoption/precondition use",
            discipline="role purity is not source theorem, divergence safety, or residual kill",
            forbidden_upgrade="must not use membership as hidden-load pocket",
        ),
        PreconditionClass(
            name="P5: incidence and residual gates separate",
            precondition="trace/residual zero incidence, residual kill, and residual non-entry remain separate theorem targets",
            status="PRECONDITION_REQUIRED",
            required_before="any scalar recombination or insertion-facing handoff",
            discipline="membership is not incidence and normalization is not residual control",
            forbidden_upgrade="must not smuggle no-overlap or residual control into Package B",
        ),
        PreconditionClass(
            name="P6: source and divergence visibility preserved",
            precondition="ordinary source and correction/divergence behavior remain visible, auditable, and non-reservoir",
            status="PRECONDITION_REQUIRED",
            required_before="conditional precondition or theorem route",
            discipline="visibility filters may reject but do not choose components",
            forbidden_upgrade="must not treat visibility as source no-double-counting theorem or divergence-safe law",
        ),
        PreconditionClass(
            name="P7: downstream gate status explicit",
            precondition="B_s/F_zeta insertion, active O, residual control, and parent closure remain marked not ready unless separately derived",
            status="NOT_READY",
            required_before="any downstream theorem route",
            discipline="precondition inventory is not insertion",
            forbidden_upgrade="must not open field-equation gates from precondition clarity",
        ),
    ]


def build_routes() -> list[ConditionalRoute]:
    return [
        ConditionalRoute(
            name="R1: audit-only precondition inventory",
            route="inventory preconditions while leaving declarations blank and status compatible-if-declared",
            status="AUDIT_READY",
            allowed_use="safe continuation of Group 35 without choices",
            blocked_until="none; this group may run as audit inventory",
            caution="audit-ready is not downstream-ready",
        ),
        ConditionalRoute(
            name="R2: explicit declaration record",
            route="fill concrete declaration values for B_s, zeta, d, scope, membership criterion, role purity, and status modes",
            status="CONDITIONAL_AFTER_DECLARATIONS",
            allowed_use="possible future route if theory owner supplies choices",
            blocked_until="separate declaration record exists",
            caution="declaration record is not adoption or theorem proof",
        ),
        ConditionalRoute(
            name="R3: explicit adoption decision",
            route="adopt one or both Package B components by separate user/theory decision",
            status="CONDITIONAL_AFTER_ADOPTION_OR_THEOREM_SUPPORT",
            allowed_use="possible future theory-choice route",
            blocked_until="separate adoption record exists",
            caution="adopted postulates must not be called derived",
        ),
        ConditionalRoute(
            name="R4: theorem route after declarations",
            route="attempt theorem support for trace normalization and/or safe membership after declarations are explicit",
            status="CONDITIONAL_AFTER_DECLARATIONS",
            allowed_use="possible proof route",
            blocked_until="declarations and proof obligations are stated",
            caution="theorem target is not theorem proof",
        ),
        ConditionalRoute(
            name="R5: conditional insertion-precondition inventory",
            route="inventory insertion-facing preconditions only under explicit declaration/status assumptions",
            status="CONDITIONAL",
            allowed_use="possible organizational route after status assumptions are visible",
            blocked_until="explicit declaration/status assumptions are stated",
            caution="precondition inventory is not B_s/F_zeta insertion theorem",
        ),
        ConditionalRoute(
            name="R6: insertion or parent route",
            route="derive B_s/F_zeta insertion or parent equation closure",
            status="NOT_READY",
            allowed_use="not available from Group 36 opener",
            blocked_until="trace-anchor status, incidence, residual, active O, source/divergence, and parent gates are resolved",
            caution="forbidden as immediate route",
        ),
    ]


def build_rejected_shortcuts() -> list[RejectedShortcut]:
    return [
        RejectedShortcut(
            name="S1: precondition inventory as declaration record",
            shortcut="treat a list of required preconditions as if declaration values were filled",
            status="FORBIDDEN_SHORTCUT",
            reason="precondition inventory names locks; it does not unlock them",
            failure_mode="hidden declarations enter later work",
        ),
        RejectedShortcut(
            name="S2: precondition inventory as adoption",
            shortcut="treat required Package B preconditions as adoption of Package B",
            status="FORBIDDEN_SHORTCUT",
            reason="adoption requires a separate explicit decision",
            failure_mode="audit status becomes theory choice",
        ),
        RejectedShortcut(
            name="S3: precondition inventory as theorem proof",
            shortcut="treat precondition clarity as derivation of trace normalization or safe membership",
            status="FORBIDDEN_SHORTCUT",
            reason="proof requires separate theorem scripts",
            failure_mode="open theorem burden disappears by label",
        ),
        RejectedShortcut(
            name="S4: precondition inventory as insertion",
            shortcut="treat preconditions as B_s/F_zeta insertion",
            status="FORBIDDEN_SHORTCUT",
            reason="insertion remains downstream and not ready",
            failure_mode="precondition clarity becomes metric insertion",
        ),
        RejectedShortcut(
            name="S5: Package B status as parent readiness",
            shortcut="open the parent equation from trace-anchor precondition clarity",
            status="FORBIDDEN_SHORTCUT",
            reason="parent equation remains blocked by recombination and safety gates",
            failure_mode="parent gate opens prematurely",
        ),
    ]


def build_obligations() -> list[OpeningObligation]:
    return [
        OpeningObligation(
            name="O1: declaration precondition ledger",
            obligation="inventory declaration preconditions without filling slots",
            status="OPEN",
            blocks="hidden declaration use",
            discipline="blank slots remain blank unless a separate declaration record fills them",
        ),
        OpeningObligation(
            name="O2: status precondition ledger",
            obligation="inventory status-mode preconditions without assigning theory status",
            status="OPEN",
            blocks="ambiguous component handoff",
            discipline="compatible-if-declared remains current status unless explicitly changed",
        ),
        OpeningObligation(
            name="O3: safety gate ledger",
            obligation="inventory node separation, role purity, incidence/residual separation, source visibility, and divergence visibility gates",
            status="OPEN",
            blocks="smuggling and hidden-load routes",
            discipline="safety gates are preconditions, not proofs",
        ),
        OpeningObligation(
            name="O4: handoff condition ledger",
            obligation="separate declaration, adoption, theorem, precondition, insertion, and parent handoffs",
            status="OPEN",
            blocks="route confusion",
            discipline="future work must state which route it is using",
        ),
        OpeningObligation(
            name="O5: adoption boundary",
            obligation="do not adopt Package B or either component in this opener",
            status="REQUIRED",
            blocks="accidental adoption",
            discipline="adoption requires a separate explicit user/theory decision record",
        ),
        OpeningObligation(
            name="O6: downstream gates",
            obligation="keep B_s/F_zeta insertion, active O, residual control, and parent closure closed",
            status="NOT_READY",
            blocks="downstream overreach",
            discipline="precondition inventory is not insertion or parent readiness",
        ),
    ]


def build_conclusions() -> list[ConclusionEntry]:
    return [
        ConclusionEntry(
            name="C1: route opened",
            conclusion="conditional trace-anchor precondition inventory route is opened",
            status="AUDIT_READY",
            meaning="safe next route after Group 35 without filling declarations or adopting Package B",
        ),
        ConclusionEntry(
            name="C2: precondition classes initialized",
            conclusion="declaration, status, separation, safety, and downstream-gate preconditions are initialized",
            status="PRECONDITION_REQUIRED",
            meaning="preconditions can be inventoried without becoming proofs",
        ),
        ConclusionEntry(
            name="C3: no choices made",
            conclusion="this opener fills no declaration slots and assigns no component status",
            status="NOT_CHOSEN",
            meaning="Group 36 opener is not an explicit declaration record",
        ),
        ConclusionEntry(
            name="C4: no adoption",
            conclusion="this opener adopts no Package B component and recommends no adoption",
            status="NOT_ADOPTED",
            meaning="explicit decision remains separate",
        ),
        ConclusionEntry(
            name="C5: downstream gates",
            conclusion="B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready",
            status="NOT_READY",
            meaning="precondition inventory does not open field-equation gates",
        ),
        ConclusionEntry(
            name="C6: next",
            conclusion="declaration precondition ledger should run next",
            status="OPEN",
            meaning="first concrete precondition audit",
        ),
    ]


# ----------------------------------------------------------------------------------------------------------------------
# Cases
# ----------------------------------------------------------------------------------------------------------------------


def case_0_problem() -> None:
    header("Case 0: Trace-anchor precondition inventory problem")
    print(
        "Question:\n\n"
        "  What preconditions must be explicit before trace-normalization and\n"
        "  safe-membership Package B components can be used in later declaration,\n"
        "  theorem, adoption, precondition, insertion, or parent routes?\n\n"
        "Discipline:\n\n"
        "  This script opens a conditional precondition inventory route.\n"
        "  It fills no declaration slot.\n"
        "  It assigns no Package B component status as theory state.\n"
        "  It selects no trace-normalization form.\n"
        "  It selects no safe-membership form.\n"
        "  It adopts no Package B component.\n"
        "  It recommends no Package B adoption.\n"
        "  It derives no coefficient law and no insertion.\n"
        "  It keeps active O, residual control, and parent closure closed.\n"
    )
    print("Tiny goblin rule:\n  Count the locks before touching the door.")
    out_line(
        "governance_assessments",
        "AUDIT_READY",
        "trace-anchor precondition inventory route opened",
        "opening conditional precondition route after Group 35 declaration inventory; no choices made",
    )


def case_1_symbolic_ledger() -> PreconditionSymbols:
    header("Case 1: Precondition inventory symbolic ledger")
    symbols = sp.symbols(
        "B_s_decl zeta_decl d_decl exact_scope zeta_Bs_decl T_zeta_decl domain_decl codomain_decl "
        "membership_criterion role_purity diagnostic_scope component_status_mode mixed_status "
        "node_separation hidden_payload_gate incidence_gate residual_gate source_visibility div_visibility "
        "P_insertion P_active_O P_residual_kill P_parent"
    )
    (
        B_s_decl,
        zeta_decl,
        d_decl,
        exact_scope,
        zeta_Bs_decl,
        T_zeta_decl,
        domain_decl,
        codomain_decl,
        membership_criterion,
        role_purity,
        diagnostic_scope,
        component_status_mode,
        mixed_status,
        node_separation,
        hidden_payload_gate,
        incidence_gate,
        residual_gate,
        source_visibility,
        div_visibility,
        P_insertion,
        P_active_O,
        P_residual_kill,
        P_parent,
    ) = symbols

    L_declaration_preconditions = sp.simplify(
        B_s_decl
        + zeta_decl
        + d_decl
        + exact_scope
        + zeta_Bs_decl
        + T_zeta_decl
        + domain_decl
        + codomain_decl
        + membership_criterion
        + role_purity
        + diagnostic_scope
    )
    L_status_preconditions = sp.simplify(component_status_mode + mixed_status)
    L_safety_preconditions = sp.simplify(
        node_separation + hidden_payload_gate + incidence_gate + residual_gate + source_visibility + div_visibility
    )
    L_downstream_closed = sp.simplify(P_insertion + P_active_O + P_residual_kill + P_parent)
    L_problem_gap = sp.simplify(
        L_declaration_preconditions + L_status_preconditions + L_safety_preconditions + L_downstream_closed
    )

    print("Precondition symbols:")
    for sym in symbols:
        print(f"  {sym} = {sym}")
    print()
    print(f"Declaration precondition load:\n  L_declaration_preconditions = {L_declaration_preconditions}")
    print(f"Status precondition load:\n  L_status_preconditions = {L_status_preconditions}")
    print(f"Safety precondition load:\n  L_safety_preconditions = {L_safety_preconditions}")
    print(f"Downstream closed load:\n  L_downstream_closed = {L_downstream_closed}")
    print(f"Precondition problem gap:\n  L_problem_gap = {L_problem_gap}")
    out_line(
        "derived_results",
        "OBLIGATION",
        "trace-anchor precondition ledgers stated",
        f"L_declaration_preconditions={L_declaration_preconditions}; L_downstream_closed={L_downstream_closed}",
    )
    return PreconditionSymbols(
        L_declaration_preconditions=L_declaration_preconditions,
        L_status_preconditions=L_status_preconditions,
        L_safety_preconditions=L_safety_preconditions,
        L_downstream_closed=L_downstream_closed,
        L_problem_gap=L_problem_gap,
    )


def case_2_precondition_classes(preconditions: Iterable[PreconditionClass]) -> None:
    header("Case 2: Required precondition classes")
    for item in preconditions:
        subheader(item.name)
        print(f"Precondition: {item.precondition}")
        out_line("governance_assessments", item.status, item.name)
        print(f"Required before: {item.required_before}")
        print(f"Discipline: {item.discipline}")
        print(f"Forbidden upgrade: {item.forbidden_upgrade}")
    out_line("governance_assessments", "OBLIGATION", "precondition classes initialized", f"{len(list(preconditions)) if not isinstance(preconditions, list) else len(preconditions)} precondition classes stated")


def case_3_conditional_routes(routes: Iterable[ConditionalRoute]) -> None:
    header("Case 3: Conditional future route types")
    for item in routes:
        subheader(item.name)
        print(f"Route: {item.route}")
        out_line("governance_assessments", item.status, item.name)
        print(f"Allowed use: {item.allowed_use}")
        print(f"Blocked until: {item.blocked_until}")
        print(f"Caution: {item.caution}")
    out_line("governance_assessments", "DEFER", "conditional route types separated", f"{len(list(routes)) if not isinstance(routes, list) else len(routes)} routes classified without choosing a route")


def case_4_rejected_shortcuts(shortcuts: Iterable[RejectedShortcut]) -> None:
    header("Case 4: Rejected precondition shortcuts")
    for item in shortcuts:
        subheader(item.name)
        print(f"Shortcut: {item.shortcut}")
        out_line("counterexamples", item.status, item.name)
        print(f"Reason: {item.reason}")
        print(f"Failure mode: {item.failure_mode}")
    out_line("counterexamples", "FAIL", "precondition shortcuts rejected", f"{len(list(shortcuts)) if not isinstance(shortcuts, list) else len(shortcuts)} shortcuts rejected")


def case_5_opening_obligations(obligations: Iterable[OpeningObligation]) -> None:
    header("Case 5: Initial precondition-inventory obligations")
    for item in obligations:
        subheader(item.name)
        print(f"Obligation: {item.obligation}")
        out_line("unresolved_obligations", item.status, item.name)
        print(f"Blocks: {item.blocks}")
        print(f"Discipline: {item.discipline}")
    out_line("unresolved_obligations", "OBLIGATION", "initial precondition obligations stated", f"{len(list(obligations)) if not isinstance(obligations, list) else len(obligations)} obligations opened")


def case_6_conclusions(conclusions: Iterable[ConclusionEntry]) -> None:
    header("Case 6: Initial precondition-inventory conclusions")
    for item in conclusions:
        subheader(item.name)
        print(f"Conclusion: {item.conclusion}")
        out_line("governance_assessments", item.status, item.name)
        print(f"Meaning: {item.meaning}")
    out_line(
        "governance_assessments",
        "PASS",
        "trace-anchor precondition inventory conclusion stated",
        "conditional precondition route opened; no declarations filled, no adoption, downstream gates closed",
    )


def final_interpretation() -> None:
    header("Final interpretation")
    print(
        "Trace-anchor precondition inventory opener result:\n\n"
        "  Group 36 is opened as a conditional precondition inventory route.\n"
        "  It asks what must be true before Package B components can be used in later routes.\n"
        "  Declaration, status, node-separation, hidden-load, incidence/residual, source/divergence, and downstream-gate preconditions are initialized.\n"
        "  Explicit declaration, adoption, theorem, precondition, insertion, and parent routes are separated.\n"
        "  No declaration value is filled by this opener.\n"
        "  No Package B component status is assigned as theory state.\n"
        "  No trace-normalization or safe-membership form is selected, adopted, or derived.\n"
        "  Package B is not recommended for adoption.\n"
        "  B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready.\n\n"
        "Possible next script:\n"
        "  candidate_trace_anchor_declaration_precondition_ledger.py\n\n"
        "Tiny goblin label:\n"
        "  Count the locks before touching the door.\n"
    )
    out_line(
        "governance_assessments",
        "PASS",
        "trace-anchor precondition inventory opener complete",
        "declaration precondition ledger should run next; adoption and downstream gates remain closed",
    )


# ----------------------------------------------------------------------------------------------------------------------
# Archive records
# ----------------------------------------------------------------------------------------------------------------------


def record_inventory_marker(ns, symbolic: PreconditionSymbols) -> None:
    ns.record_derivation(
        derivation_id="g36_precondition_inventory_problem",
        inputs=[
            symbolic.L_declaration_preconditions,
            symbolic.L_status_preconditions,
            symbolic.L_safety_preconditions,
            symbolic.L_downstream_closed,
        ],
        output=symbolic.L_problem_gap,
        method="Group 36 conditional trace-anchor precondition inventory opener ledger",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="problem_ledger_marker",
        is_placeholder=True,
    )


def record_obligations(ns, obligations: Iterable[OpeningObligation]) -> None:
    for item in obligations:
        ident = safe_ident(item.name)
        status = ObligationStatus.OPEN if item.status != "NOT_READY" else ObligationStatus.DEFERRED
        ns.record_obligation(
            ProofObligationRecord(
                obligation_id=f"g36_precondition_problem_{ident}",
                script_id=SCRIPT_ID,
                title=item.name,
                status=status,
                required_by=[SCRIPT_ID],
                description=f"{item.obligation}. Blocks: {item.blocks}. Discipline: {item.discipline}.",
            )
        )


def record_governance(ns, preconditions: Iterable[PreconditionClass], routes: Iterable[ConditionalRoute], shortcuts: Iterable[RejectedShortcut]) -> None:
    ns.record_route(
        RouteRecord(
            route_id="g36_precond_route",
            script_id=SCRIPT_ID,
            name="Conditional trace-anchor precondition inventory route",
            status=GovernanceStatus.CANDIDATE_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            required_obligations=[
                "g36_precondition_problem_o1",
                "g36_precondition_problem_o2",
                "g36_precondition_problem_o3",
                "g36_precondition_problem_o4",
                "g36_precondition_problem_o5",
                "g36_precondition_problem_o6",
            ],
            activation_conditions=[
                "Group 35 declaration inventory complete",
                "trace-normalization compatible-if-declared only",
                "safe-membership compatible-if-declared only",
                "no declaration values filled",
                "no Package B component adopted",
                "downstream gates closed",
            ],
        )
    )

    for item in preconditions:
        ident = safe_ident(item.name)
        status = GovernanceStatus.CANDIDATE_ROUTE
        if item.status == "NOT_READY":
            status = GovernanceStatus.DEFERRED_PENDING_PREREQUISITES
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g36_precondition_class_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=status,
                statement=(
                    f"Precondition: {item.precondition}. Required before: {item.required_before}. "
                    f"Discipline: {item.discipline}. Forbidden upgrade: {item.forbidden_upgrade}."
                ),
                derivation_ids=["g36_precondition_inventory_problem"],
                obligation_ids=[],
            )
        )

    for item in routes:
        ident = safe_ident(item.name)
        status = GovernanceStatus.CANDIDATE_ROUTE
        if item.status in {"NOT_READY", "CONDITIONAL", "CONDITIONAL_AFTER_DECLARATIONS", "CONDITIONAL_AFTER_ADOPTION_OR_THEOREM_SUPPORT"}:
            status = GovernanceStatus.DEFERRED_PENDING_PREREQUISITES
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g36_conditional_route_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=status,
                statement=(
                    f"Route: {item.route}. Allowed use: {item.allowed_use}. "
                    f"Blocked until: {item.blocked_until}. Caution: {item.caution}."
                ),
                derivation_ids=["g36_precondition_inventory_problem"],
                obligation_ids=[],
            )
        )

    for item in shortcuts:
        ident = safe_ident(item.name)
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g36_rejected_shortcut_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.REJECTED_ROUTE,
                statement=f"Forbidden shortcut: {item.shortcut}. Reason: {item.reason}. Failure mode: {item.failure_mode}.",
                derivation_ids=["g36_precondition_inventory_problem"],
                obligation_ids=[],
            )
        )

    policy_rules = [
        ("g36_policy_no_declarations_filled", "Group 36 opener fills no declaration slots."),
        ("g36_policy_no_status_assigned", "Group 36 opener assigns no Package B component status as theory state."),
        ("g36_policy_no_adoption", "Group 36 opener adopts no Package B component and recommends no adoption."),
        ("g36_policy_downstream_gates_closed", "Group 36 opener does not license insertion, active O, residual control, or parent closure."),
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
                derivation_ids=["g36_precondition_inventory_problem"],
                obligation_ids=[],
            )
        )


# ----------------------------------------------------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------------------------------------------------


def main() -> None:
    header("Candidate Trace Anchor Precondition Inventory Problem")
    archive, ns, invalidated = prepare_archive()
    ensure_archive_write_dirs(ns)
    print_archive_status(ns, invalidated)

    preconditions = build_preconditions()
    routes = build_routes()
    shortcuts = build_rejected_shortcuts()
    obligations = build_obligations()
    conclusions = build_conclusions()

    case_0_problem()
    symbolic = case_1_symbolic_ledger()
    case_2_precondition_classes(preconditions)
    case_3_conditional_routes(routes)
    case_4_rejected_shortcuts(shortcuts)
    case_5_opening_obligations(obligations)
    case_6_conclusions(conclusions)
    final_interpretation()

    record_inventory_marker(ns, symbolic)
    record_obligations(ns, obligations)
    record_governance(ns, preconditions, routes, shortcuts)

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
