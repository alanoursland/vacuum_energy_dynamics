# Candidate Trace Anchor Handoff Condition Ledger
#
# Group:
#   36_conditional_trace_anchor_precondition_inventory
#
# Human title:
#   Trace Anchor Handoff Condition Ledger
#
# Script type:
#   PRECONDITION LEDGER / HANDOFF AUDIT
#
# Purpose
# -------
# Inventory the conditions that must be explicit before Group 36 can hand
# trace-normalization and safe-membership Package B components to any later
# declaration, theorem, adoption, precondition, insertion-facing, or
# parent-facing route.
#
# This script does not choose a route.
# It fills no declaration slot.
# It assigns no Package B component status as theory state.
# It selects no trace-normalization form.
# It selects no safe-membership form.
# It adopts no Package B component.
# It recommends no Package B adoption.
# It derives no coefficient law and no insertion.
# It keeps active O, residual control, and parent closure closed.
#
# Tiny goblin rule:
#   Label the doors. Do not walk through them.

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
        "ADOPTION_REQUIRES_DECISION": StatusMark.DEFER,
        "AUDIT_READY": StatusMark.INFO,
        "BLOCKED_IF_BLANK": StatusMark.DEFER,
        "COMPATIBLE_IF_DECLARED": StatusMark.INFO,
        "CONDITIONAL": StatusMark.DEFER,
        "DECLARATION_REQUIRED": StatusMark.OBLIGATION,
        "DEFERRED": StatusMark.DEFER,
        "FAIL": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
        "HANDOFF_READY": StatusMark.INFO,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_ASSIGNED": StatusMark.DEFER,
        "NOT_CHOSEN": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "PASS": StatusMark.PASS,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "PRECONDITION_REQUIRED": StatusMark.OBLIGATION,
        "REQUIRED": StatusMark.OBLIGATION,
        "ROUTE_CONDITION": StatusMark.OBLIGATION,
        "SAFETY_REQUIRED": StatusMark.OBLIGATION,
        "STATUS_REQUIRED": StatusMark.OBLIGATION,
        "THEOREM_TARGET": StatusMark.DEFER,
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
            "g36_safety_pc",
            "036_conditional_trace_anchor_precondition_inventory__candidate_trace_anchor_safety_precondition_ledger",
            "g36_safety_pc",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g36_status_pc",
            "036_conditional_trace_anchor_precondition_inventory__candidate_trace_anchor_status_precondition_matrix",
            "g36_status_precond_matrix",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g36_decl_pc",
            "036_conditional_trace_anchor_precondition_inventory__candidate_trace_anchor_declaration_precondition_ledger",
            "g36_decl_precond_ledger",
            RecordKind.INVENTORY_MARKER,
        ),
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
class HandoffSymbols:
    L_route_handoffs: sp.Basic
    L_assumption_surface: sp.Basic
    L_handoff_blocks: sp.Basic
    L_downstream_closed: sp.Basic
    L_handoff_gap: sp.Basic


@dataclass
class HandoffRoute:
    name: str
    route: str
    status: str
    allowed_use: str
    requires: str
    caution: str


@dataclass
class HandoffCondition:
    name: str
    condition: str
    status: str
    required_before: str
    fails_if: str
    boundary: str


@dataclass
class InvalidHandoff:
    name: str
    shortcut: str
    status: str
    reason: str
    failure_mode: str


@dataclass
class HandoffObligation:
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


def build_handoff_routes() -> list[HandoffRoute]:
    return [
        HandoffRoute(
            name="H1: Group 36 status summary",
            route="summarize the conditional precondition inventory after declaration, status, safety, and handoff ledgers",
            status="HANDOFF_READY",
            allowed_use="close Group 36 as a precondition inventory",
            requires="no declaration values filled, no status assigned, no adoption, downstream gates closed",
            caution="summary must not become declaration record, adoption record, theorem proof, or insertion theorem",
        ),
        HandoffRoute(
            name="H2: explicit declaration record",
            route="fill concrete B_s, zeta, dimension, scope, membership, role-purity, and status-mode declarations",
            status="CONDITIONAL",
            allowed_use="possible later route if theory owner supplies declaration values",
            requires="separate declaration record and explicit status for each component",
            caution="declaration is not adoption and not theorem proof",
        ),
        HandoffRoute(
            name="H3: explicit Package B adoption decision",
            route="adopt one or both Package B components by separate user/theory decision",
            status="CONDITIONAL",
            allowed_use="possible later theory-choice route",
            requires="separate adoption record naming exactly which components are adopted",
            caution="adopted postulates must not be reported as derived",
        ),
        HandoffRoute(
            name="H4: theorem route after declarations",
            route="attempt theorem support for trace normalization and/or safe membership after declarations are explicit",
            status="THEOREM_TARGET",
            allowed_use="possible proof route after assumptions and obligations are stated",
            requires="declaration values, status mode, proof assumptions, and proof obligations",
            caution="theorem target is not theorem proof",
        ),
        HandoffRoute(
            name="H5: conditional insertion-precondition inventory",
            route="inventory insertion-facing preconditions under explicit declaration/status assumptions",
            status="CONDITIONAL",
            allowed_use="possible organizational route after assumptions are named",
            requires="explicit statement that inventory is conditional and not insertion",
            caution="precondition inventory is not B_s/F_zeta insertion theorem",
        ),
        HandoffRoute(
            name="H6: B_s/F_zeta insertion theorem",
            route="derive scalar trace insertion into B_s/F_zeta",
            status="NOT_READY",
            allowed_use="not available from Group 36 alone",
            requires="explicit component status plus incidence, residual, source/divergence, active-O, and recombination gates",
            caution="forbidden as immediate handoff",
        ),
        HandoffRoute(
            name="H7: parent field equation",
            route="open parent field equation closure",
            status="NOT_READY",
            allowed_use="not available from Group 36 alone",
            requires="scalar recombination, residual control, no-overlap, source neutrality, divergence safety, and parent identity",
            caution="parent gate remains closed",
        ),
    ]


def build_handoff_conditions() -> list[HandoffCondition]:
    return [
        HandoffCondition(
            name="Ck1: route kind explicit",
            condition="future handoff must say whether it is declaration, adoption, theorem, precondition inventory, insertion theorem, or parent route",
            status="ROUTE_CONDITION",
            required_before="any Group 36 handoff",
            fails_if="route kind is implicit or mixed by prose",
            boundary="route classification is not route selection",
        ),
        HandoffCondition(
            name="Ck2: declaration assumptions explicit",
            condition="future handoff must state which declaration slots are filled, blank, or assumed",
            status="DECLARATION_REQUIRED",
            required_before="theorem, adoption, or insertion-facing work",
            fails_if="compatible-if-declared status is treated as already declared",
            boundary="declaration assumptions are not proof",
        ),
        HandoffCondition(
            name="Ck3: component status explicit",
            condition="future handoff must state status mode for P_trace_norm and P_safe_membership separately",
            status="STATUS_REQUIRED",
            required_before="any component use",
            fails_if="Package B is given a single status while components differ or remain unresolved",
            boundary="status visibility is not status assignment",
        ),
        HandoffCondition(
            name="Ck4: safety gates imported",
            condition="future handoff must preserve node separation, hidden-load exclusion, incidence/residual separation, source visibility, divergence explicitness, and diagnostic inertness",
            status="SAFETY_REQUIRED",
            required_before="any Package B-facing continuation",
            fails_if="handoff drops safety gates or treats them as solved theorems",
            boundary="safety import is not downstream license",
        ),
        HandoffCondition(
            name="Ck5: mixed status explicit",
            condition="if one Package B component changes status before the other, the mixed state must be carried visibly",
            status="STATUS_REQUIRED",
            required_before="any non-uniform Package B handoff",
            fails_if="one component's status licenses the other",
            boundary="mixed status is an obligation, not a recommendation",
        ),
        HandoffCondition(
            name="Ck6: downstream locks explicit",
            condition="insertion, active O, residual control, and parent closure must remain marked not ready unless separately derived",
            status="NOT_READY",
            required_before="any downstream-facing route",
            fails_if="precondition clarity is treated as field-equation use",
            boundary="handoff conditions are not insertion or parent readiness",
        ),
    ]


def build_invalid_handoffs() -> list[InvalidHandoff]:
    return [
        InvalidHandoff(
            name="X1: hidden route kind",
            shortcut="handoff proceeds without saying whether it is declaration, adoption, theorem, precondition, insertion, or parent route",
            status="FORBIDDEN_SHORTCUT",
            reason="route ambiguity hides claim strength",
            failure_mode="audit handoff becomes theory choice or theorem by drift",
        ),
        InvalidHandoff(
            name="X2: hidden assumptions",
            shortcut="handoff uses Package B components without explicit declaration/status assumptions",
            status="FORBIDDEN_SHORTCUT",
            reason="Group 35/36 left declarations and statuses unfilled",
            failure_mode="blank slots behave as filled declarations",
        ),
        InvalidHandoff(
            name="X3: declaration route as adoption",
            shortcut="future declaration record is treated as Package B adoption",
            status="FORBIDDEN_SHORTCUT",
            reason="adoption requires separate explicit decision",
            failure_mode="declared candidate becomes postulate by handoff language",
        ),
        InvalidHandoff(
            name="X4: adoption route as derivation",
            shortcut="explicit adopted postulate is described as derived theorem",
            status="FORBIDDEN_SHORTCUT",
            reason="choice and proof remain separate",
            failure_mode="postulate/theorem boundary collapses",
        ),
        InvalidHandoff(
            name="X5: theorem target as proof",
            shortcut="handoff treats theorem-target status as already proved",
            status="FORBIDDEN_SHORTCUT",
            reason="proof target is not proof",
            failure_mode="open theorem burden disappears by label",
        ),
        InvalidHandoff(
            name="X6: precondition inventory as insertion",
            shortcut="conditional precondition inventory is treated as B_s/F_zeta insertion theorem",
            status="FORBIDDEN_SHORTCUT",
            reason="insertion remains downstream and not ready",
            failure_mode="door labels become door opening",
        ),
        InvalidHandoff(
            name="X7: parent route from handoff clarity",
            shortcut="parent field equation is opened because declaration/status/safety handoffs are organized",
            status="FORBIDDEN_SHORTCUT",
            reason="parent gate remains blocked by recombination and safety theorems",
            failure_mode="parent closure opens prematurely",
        ),
    ]


def build_obligations() -> list[HandoffObligation]:
    return [
        HandoffObligation(
            name="O1: state route kind",
            obligation="require every future handoff to name its route type explicitly",
            status="OPEN",
            blocks="route confusion",
            discipline="handoff taxonomy is not route selection",
        ),
        HandoffObligation(
            name="O2: state declaration assumptions",
            obligation="require declaration slots to be marked filled, blank, or assumed before use",
            status="OPEN",
            blocks="hidden declaration use",
            discipline="blank slots remain blank until a separate declaration record fills them",
        ),
        HandoffObligation(
            name="O3: state component statuses",
            obligation="require P_trace_norm and P_safe_membership status modes separately",
            status="OPEN",
            blocks="ambiguous Package B status",
            discipline="one component's status cannot license the other",
        ),
        HandoffObligation(
            name="O4: preserve safety gates",
            obligation="carry node separation, hidden-load exclusion, incidence/residual separation, source/divergence visibility, diagnostic inertness, and downstream locks into handoffs",
            status="OPEN",
            blocks="safety gate loss",
            discipline="safety gates are preconditions, not solved theorems",
        ),
        HandoffObligation(
            name="O5: adoption boundary",
            obligation="do not adopt Package B or either component in this handoff ledger",
            status="REQUIRED",
            blocks="accidental adoption",
            discipline="adoption requires a separate explicit decision record",
        ),
        HandoffObligation(
            name="O6: downstream gates",
            obligation="keep B_s/F_zeta insertion, active O, residual control, and parent closure closed",
            status="NOT_READY",
            blocks="downstream overreach",
            discipline="handoff conditions are not insertion or parent readiness",
        ),
    ]


def build_conclusions() -> list[ConclusionEntry]:
    return [
        ConclusionEntry(
            name="C1: handoff conditions inventoried",
            conclusion="route-kind, declaration, status, safety, mixed-status, and downstream-lock handoff conditions are visible",
            status="ROUTE_CONDITION",
            meaning="future work can state exactly what kind of handoff it is using",
        ),
        ConclusionEntry(
            name="C2: no route chosen",
            conclusion="this ledger classifies handoff routes but chooses none",
            status="NOT_CHOSEN",
            meaning="handoff ledger is not declaration, adoption, theorem, or insertion route",
        ),
        ConclusionEntry(
            name="C3: no declarations or statuses assigned",
            conclusion="this ledger fills no declaration slots and assigns no component status",
            status="NOT_ASSIGNED",
            meaning="current Package B component status remains compatible-if-declared only",
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
            meaning="handoff clarity does not open field-equation gates",
        ),
        ConclusionEntry(
            name="C6: next",
            conclusion="precondition obligations summary should run next",
            status="OPEN",
            meaning="Group 36 can then close as a conditional precondition inventory",
        ),
    ]


# ----------------------------------------------------------------------------------------------------------------------
# Cases
# ----------------------------------------------------------------------------------------------------------------------


def case_0_problem() -> None:
    header("Case 0: Handoff condition ledger problem")
    print(
        "Question:\n\n"
        "  Which handoff conditions must be explicit before Group 36 results can\n"
        "  be used in declaration, theorem, adoption, precondition, insertion,\n"
        "  or parent routes?\n\n"
        "Discipline:\n\n"
        "  This script inventories handoff conditions.\n"
        "  It chooses no route.\n"
        "  It fills no declaration slot.\n"
        "  It assigns no Package B component status as theory state.\n"
        "  It selects no trace-normalization form.\n"
        "  It selects no safe-membership form.\n"
        "  It adopts no Package B component.\n"
        "  It recommends no Package B adoption.\n"
        "  It derives no coefficient law and no insertion.\n"
        "  It keeps active O, residual control, and parent closure closed.\n\n"
        "Tiny goblin rule:\n"
        "  Label the doors. Do not walk through them."
    )
    out_line(
        "governance_assessments",
        "PASS",
        "handoff condition ledger opened",
        "handoff routes are audited as conditional routes only; no route is chosen",
    )


def case_1_symbolic_ledger() -> HandoffSymbols:
    header("Case 1: Handoff condition symbolic ledger")

    names = [
        "declaration_record",
        "adoption_record",
        "theorem_route",
        "precondition_inventory",
        "insertion_route",
        "parent_route",
        "route_kind",
        "declaration_assumptions",
        "status_assumptions",
        "safety_imports",
        "mixed_status",
        "hidden_assumption",
        "route_drift",
        "one_node_license",
        "P_insertion",
        "P_active_O",
        "P_residual_kill",
        "P_parent",
    ]
    symbols = dict(zip(names, sp.symbols(" ".join(names))))

    print("Handoff-condition symbols:")
    for name in names:
        print(f"  {name} = {symbols[name]}")

    L_route_handoffs = sp.simplify(
        symbols["declaration_record"]
        + symbols["adoption_record"]
        + symbols["theorem_route"]
        + symbols["precondition_inventory"]
        + symbols["insertion_route"]
        + symbols["parent_route"]
    )
    L_assumption_surface = sp.simplify(
        symbols["route_kind"]
        + symbols["declaration_assumptions"]
        + symbols["status_assumptions"]
        + symbols["safety_imports"]
        + symbols["mixed_status"]
    )
    L_handoff_blocks = sp.simplify(
        symbols["hidden_assumption"] + symbols["route_drift"] + symbols["one_node_license"]
    )
    L_downstream_closed = sp.simplify(
        symbols["P_insertion"] + symbols["P_active_O"] + symbols["P_residual_kill"] + symbols["P_parent"]
    )
    L_handoff_gap = sp.simplify(L_route_handoffs + L_assumption_surface + L_handoff_blocks + L_downstream_closed)

    print()
    print(f"Route handoff load:\n  L_route_handoffs = {L_route_handoffs}")
    print(f"Assumption surface load:\n  L_assumption_surface = {L_assumption_surface}")
    print(f"Handoff block load:\n  L_handoff_blocks = {L_handoff_blocks}")
    print(f"Downstream closed load:\n  L_downstream_closed = {L_downstream_closed}")
    print(f"Handoff-condition gap:\n  L_handoff_gap = {L_handoff_gap}")

    out_line(
        "derived_results",
        "PASS",
        "handoff-condition symbolic loads stated",
        f"L_assumption_surface={L_assumption_surface}; L_downstream_closed={L_downstream_closed}",
    )

    return HandoffSymbols(
        L_route_handoffs=L_route_handoffs,
        L_assumption_surface=L_assumption_surface,
        L_handoff_blocks=L_handoff_blocks,
        L_downstream_closed=L_downstream_closed,
        L_handoff_gap=L_handoff_gap,
    )


def case_2_routes(routes: Iterable[HandoffRoute]) -> None:
    header("Case 2: Handoff route types")
    for item in routes:
        subheader(item.name)
        print(f"Route: {item.route}")
        out_line("governance_assessments", item.status, item.name, "")
        print(f"Allowed use: {item.allowed_use}")
        print(f"Requires: {item.requires}")
        print(f"Caution: {item.caution}")
    out_line("governance_assessments", "INFO", "handoff route types separated", "7 handoff routes classified without choosing one")


def case_3_conditions(conditions: Iterable[HandoffCondition]) -> None:
    header("Case 3: Handoff condition checks")
    for item in conditions:
        subheader(item.name)
        print(f"Condition: {item.condition}")
        out_line("governance_assessments", item.status, item.name, "")
        print(f"Required before: {item.required_before}")
        print(f"Fails if: {item.fails_if}")
        print(f"Boundary: {item.boundary}")
    out_line("governance_assessments", "INFO", "handoff condition checks stated", "6 checks stated")


def case_4_invalid(invalids: Iterable[InvalidHandoff]) -> None:
    header("Case 4: Invalid handoff uses")
    for item in invalids:
        subheader(item.name)
        print(f"Shortcut: {item.shortcut}")
        out_line("counterexamples", item.status, item.name, "")
        print(f"Reason: {item.reason}")
        print(f"Failure mode: {item.failure_mode}")
    out_line("counterexamples", "FAIL", "invalid handoff uses rejected", "7 shortcuts rejected")


def case_5_obligations(obligations: Iterable[HandoffObligation]) -> None:
    header("Case 5: Handoff-condition obligations")
    for item in obligations:
        subheader(item.name)
        print(f"Obligation: {item.obligation}")
        out_line("unresolved_obligations", item.status, item.name, "")
        print(f"Blocks: {item.blocks}")
        print(f"Discipline: {item.discipline}")
    out_line("unresolved_obligations", "INFO", "handoff-condition obligations opened", "6 obligations stated")


def case_6_conclusions(conclusions: Iterable[ConclusionEntry]) -> None:
    header("Case 6: Handoff-condition conclusions")
    for item in conclusions:
        subheader(item.name)
        print(f"Conclusion: {item.conclusion}")
        out_line("governance_assessments", item.status, item.name, "")
        print(f"Meaning: {item.meaning}")
    out_line(
        "governance_assessments",
        "PASS",
        "handoff condition ledger conclusion stated",
        "handoff conditions inventoried; no route chosen, no adoption, downstream gates closed",
    )


def final_interpretation() -> None:
    header("Final interpretation")
    print(
        "Trace-anchor handoff condition ledger result:\n\n"
        "  Handoff conditions for Package B routes are now inventoried.\n"
        "  Future work must state route kind, declaration assumptions, component statuses, mixed status, and imported safety gates.\n"
        "  Declaration, adoption, theorem, precondition, insertion, and parent routes remain separated.\n"
        "  Group 36 status summary is handoff-ready, but it must remain an inventory summary.\n"
        "  Explicit declaration, adoption, theorem, and insertion-facing routes remain conditional or not ready.\n"
        "  No declaration value is filled by this ledger.\n"
        "  No Package B component status is assigned as theory state.\n"
        "  No trace-normalization or safe-membership form is selected, adopted, or derived.\n"
        "  Package B is not recommended for adoption.\n"
        "  B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready.\n\n"
        "Possible next script:\n"
        "  candidate_trace_anchor_precondition_obligations.py\n\n"
        "Tiny goblin label:\n"
        "  Label the doors. Do not walk through them.\n"
    )
    out_line(
        "governance_assessments",
        "PASS",
        "trace-anchor handoff condition ledger complete",
        "precondition obligations summary should run next; adoption and downstream gates remain closed",
    )


# ----------------------------------------------------------------------------------------------------------------------
# Archive records
# ----------------------------------------------------------------------------------------------------------------------


def record_inventory_marker(ns, symbolic: HandoffSymbols) -> None:
    ns.record_derivation(
        derivation_id="g36_handoff_pc",
        inputs=[
            symbolic.L_route_handoffs,
            symbolic.L_assumption_surface,
            symbolic.L_handoff_blocks,
            symbolic.L_downstream_closed,
        ],
        output=symbolic.L_handoff_gap,
        method="Group 36 trace-anchor handoff condition ledger",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="handoff_condition_ledger_marker",
        is_placeholder=True,
    )


def record_obligations(ns, obligations: Iterable[HandoffObligation]) -> None:
    for item in obligations:
        ident = safe_ident(item.name)
        status = ObligationStatus.OPEN if item.status != "NOT_READY" else ObligationStatus.DEFERRED
        ns.record_obligation(
            ProofObligationRecord(
                obligation_id=f"g36_hf_{ident}",
                script_id=SCRIPT_ID,
                title=item.name,
                status=status,
                required_by=[SCRIPT_ID],
                description=f"{item.obligation}. Blocks: {item.blocks}. Discipline: {item.discipline}.",
            )
        )


def record_governance(
    ns,
    routes: Iterable[HandoffRoute],
    conditions: Iterable[HandoffCondition],
    invalids: Iterable[InvalidHandoff],
) -> None:
    ns.record_route(
        RouteRecord(
            route_id="g36_handoff_pc",
            script_id=SCRIPT_ID,
            name="Trace-anchor handoff condition ledger route",
            status=GovernanceStatus.CANDIDATE_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            required_obligations=[
                "g36_hf_o1",
                "g36_hf_o2",
                "g36_hf_o3",
                "g36_hf_o4",
                "g36_hf_o5",
                "g36_hf_o6",
            ],
            activation_conditions=[
                "Group 36 safety precondition ledger complete",
                "handoff route conditions inventoried only",
                "no route chosen",
                "no declaration values filled",
                "no component status assigned",
                "no Package B component adopted",
                "downstream gates closed",
            ],
        )
    )

    for item in routes:
        ident = safe_ident(item.name)
        status = GovernanceStatus.CANDIDATE_ROUTE
        if item.status == "NOT_READY":
            status = GovernanceStatus.DEFERRED_PENDING_PREREQUISITES
        elif item.status in {"THEOREM_TARGET", "CONDITIONAL"}:
            status = GovernanceStatus.CANDIDATE_ROUTE
        elif item.status == "HANDOFF_READY":
            status = GovernanceStatus.CANDIDATE_ROUTE
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g36_hf_h_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=status,
                statement=(
                    f"Handoff route: {item.route}. Allowed use: {item.allowed_use}. "
                    f"Requires: {item.requires}. Caution: {item.caution}."
                ),
                derivation_ids=["g36_handoff_pc"],
                obligation_ids=[],
            )
        )

    for item in conditions:
        ident = safe_ident(item.name)
        status = GovernanceStatus.POLICY_RULE
        if item.status == "NOT_READY":
            status = GovernanceStatus.DEFERRED_PENDING_PREREQUISITES
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g36_hf_c_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=status,
                statement=(
                    f"Handoff condition: {item.condition}. Required before: {item.required_before}. "
                    f"Fails if: {item.fails_if}. Boundary: {item.boundary}."
                ),
                derivation_ids=["g36_handoff_pc"],
                obligation_ids=[],
            )
        )

    for item in invalids:
        ident = safe_ident(item.name)
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g36_hf_x_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.REJECTED_ROUTE,
                statement=f"Forbidden handoff shortcut: {item.shortcut}. Reason: {item.reason}. Failure mode: {item.failure_mode}.",
                derivation_ids=["g36_handoff_pc"],
                obligation_ids=[],
            )
        )

    policy_rules = [
        ("g36_hf_pol_route", "Every future handoff must state its route kind explicitly."),
        ("g36_hf_pol_decl", "Declaration assumptions must be stated before declaration-dependent use."),
        ("g36_hf_pol_status", "Package B component statuses must be stated separately before handoff."),
        ("g36_hf_pol_safety", "Safety gates must be imported as preconditions, not treated as solved theorems."),
        ("g36_hf_pol_adopt", "Adoption requires a separate explicit decision record."),
        ("g36_hf_pol_down", "Handoff clarity does not license insertion, active O, residual control, or parent closure."),
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
                derivation_ids=["g36_handoff_pc"],
                obligation_ids=[],
            )
        )


# ----------------------------------------------------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------------------------------------------------


def main() -> None:
    header("Candidate Trace Anchor Handoff Condition Ledger")
    archive, ns, invalidated = prepare_archive()
    ensure_archive_write_dirs(ns)
    print_archive_status(ns, invalidated)

    routes = build_handoff_routes()
    conditions = build_handoff_conditions()
    invalids = build_invalid_handoffs()
    obligations = build_obligations()
    conclusions = build_conclusions()

    case_0_problem()
    symbolic = case_1_symbolic_ledger()
    case_2_routes(routes)
    case_3_conditions(conditions)
    case_4_invalid(invalids)
    case_5_obligations(obligations)
    case_6_conclusions(conclusions)
    final_interpretation()

    record_inventory_marker(ns, symbolic)
    record_obligations(ns, obligations)
    record_governance(ns, routes, conditions, invalids)

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
