# Candidate Trace Anchor Status Precondition Matrix
#
# Group:
#   36_conditional_trace_anchor_precondition_inventory
#
# Human title:
#   Trace Anchor Status Precondition Matrix
#
# Script type:
#   PRECONDITION MATRIX / STATUS-MODE AUDIT
#
# Purpose
# -------
# Inventory the status preconditions that must be explicit before
# trace-normalization and safe-membership Package B components can be used in
# theorem, adoption, declaration, precondition, insertion-facing, or
# parent-facing work.
#
# This script does not assign any Package B component status as theory state.
# It fills no declaration slot.
# It selects no trace-normalization form.
# It selects no safe-membership form.
# It adopts no Package B component.
# It recommends no Package B adoption.
# It derives no coefficient law and no insertion.
# It keeps active O, residual control, and parent closure closed.
#
# Tiny goblin rule:
#   Sort the key tags. Do not put one in the lock.

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
        "BLOCKED_IF_HIDDEN": StatusMark.DEFER,
        "COMPATIBLE_IF_DECLARED": StatusMark.INFO,
        "CONDITIONAL": StatusMark.DEFER,
        "DEFERRED": StatusMark.DEFER,
        "DIAGNOSTIC_ONLY": StatusMark.INFO,
        "FAIL": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
        "MIXED_STATUS_REQUIRED": StatusMark.OBLIGATION,
        "MIXED_STATUS_VISIBLE": StatusMark.DEFER,
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
        "STATUS_REQUIRED": StatusMark.OBLIGATION,
        "STATUS_MODE": StatusMark.INFO,
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
            "g35_status_sieve",
            "035_trace_anchor_joint_declaration_inventory__candidate_trace_anchor_status_mode_sieve",
            "g35_status_mode_sieve",
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
class StatusSymbols:
    L_component_status_preconditions: sp.Basic
    L_status_pair_preconditions: sp.Basic
    L_invalid_status_modes: sp.Basic
    L_downstream_closed: sp.Basic
    L_status_gap: sp.Basic


@dataclass
class StatusModePrecondition:
    name: str
    mode: str
    status: str
    allowed_meaning: str
    required_before: str
    forbidden_upgrade: str


@dataclass
class StatusPairCase:
    name: str
    pair: str
    status: str
    coherent_if: str
    blocked_if: str
    boundary: str


@dataclass
class InvalidStatusUse:
    name: str
    shortcut: str
    status: str
    reason: str
    failure_mode: str


@dataclass
class StatusObligation:
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


def build_status_modes() -> list[StatusModePrecondition]:
    return [
        StatusModePrecondition(
            name="S1: compatible-if-declared mode",
            mode="component form survives filters only if required declarations are explicit",
            status="COMPATIBLE_IF_DECLARED",
            allowed_meaning="current audit status for Group 33/34 surviving forms",
            required_before="any handoff that mentions trace normalization or safe membership",
            forbidden_upgrade="must not be shortened to selected, adopted, derived, or insertable",
        ),
        StatusModePrecondition(
            name="S2: declared explicit candidate mode",
            mode="declaration values are filled but component is not adopted or proved",
            status="STATUS_MODE",
            allowed_meaning="possible future status after an explicit declaration record",
            required_before="theorem attempt, adoption decision, or precondition handoff based on declared values",
            forbidden_upgrade="must not be called a theorem or adopted postulate",
        ),
        StatusModePrecondition(
            name="S3: theorem target mode",
            mode="component is pursued by proof after declarations",
            status="THEOREM_TARGET",
            allowed_meaning="possible future proof route with explicit assumptions and obligations",
            required_before="any proof attempt or theorem-route handoff",
            forbidden_upgrade="must not be treated as already proved",
        ),
        StatusModePrecondition(
            name="S4: explicit adopted postulate mode",
            mode="component is adopted by separate user/theory decision",
            status="ADOPTION_REQUIRES_DECISION",
            allowed_meaning="possible future theory-choice status",
            required_before="any downstream use that relies on adoption",
            forbidden_upgrade="must not be reported as derived or forced by audits",
        ),
        StatusModePrecondition(
            name="S5: diagnostic-only inert mode",
            mode="component label is used only for audit and has no equation effect",
            status="DIAGNOSTIC_ONLY",
            allowed_meaning="safe fallback for labels and bookkeeping",
            required_before="any diagnostic handoff that keeps labels inert",
            forbidden_upgrade="must not become active membership, coefficient law, projector, insertion, or parent input",
        ),
        StatusModePrecondition(
            name="S6: deferred or not-ready mode",
            mode="component or use remains unresolved",
            status="DEFERRED",
            allowed_meaning="safe status for incomplete declarations or blocked downstream use",
            required_before="any route that carries unresolved components forward",
            forbidden_upgrade="must not be treated as permanent no-go or as sufficient support",
        ),
    ]


def build_status_pairs() -> list[StatusPairCase]:
    return [
        StatusPairCase(
            name="P1: both compatible-if-declared",
            pair="P_trace_norm and P_safe_membership both remain compatible-if-declared",
            status="COMPATIBLE_IF_DECLARED",
            coherent_if="handoff says Package B remains audit-only and declaration-dependent",
            blocked_if="the pair is shortened to selected, adopted, derived, or insertable",
            boundary="safe current state; no downstream use licensed",
        ),
        StatusPairCase(
            name="P2: one declared candidate and one compatible-if-declared",
            pair="one component has explicit declarations while the other remains conditional",
            status="MIXED_STATUS_VISIBLE",
            coherent_if="mixed status is recorded and downstream use is blocked or conditionalized",
            blocked_if="Package B is treated as uniformly declared or usable",
            boundary="mixed status is an obligation, not a recommendation",
        ),
        StatusPairCase(
            name="P3: both declared explicit candidates",
            pair="both components have declarations but neither is adopted or proved",
            status="STATUS_MODE",
            coherent_if="declarations are explicit, node separation is preserved, and status remains candidate-only",
            blocked_if="declared candidates are treated as adopted postulates or theorem results",
            boundary="may support later decision or theorem route, not insertion",
        ),
        StatusPairCase(
            name="P4: theorem-target pair",
            pair="one or both components are theorem targets after declarations",
            status="THEOREM_TARGET",
            coherent_if="proof obligations and assumptions are explicit",
            blocked_if="theorem-target status is treated as theorem proof",
            boundary="requires separate proof scripts before downstream use",
        ),
        StatusPairCase(
            name="P5: adopted/deferred mixed pair",
            pair="one component is explicitly adopted while the other remains deferred or compatible-if-declared",
            status="MIXED_STATUS_VISIBLE",
            coherent_if="the adopted component has a separate adoption record and the deferred component blocks downstream use",
            blocked_if="Package B is treated as fully adopted by one-component adoption",
            boundary="mixed status must be visible in every handoff",
        ),
        StatusPairCase(
            name="P6: diagnostic membership plus normalization candidate",
            pair="safe membership is diagnostic-only while trace normalization remains candidate or compatible-if-declared",
            status="DIAGNOSTIC_ONLY",
            coherent_if="diagnostic label is inert and cannot alter equations",
            blocked_if="diagnostic label is used actively for insertion or residual control",
            boundary="safe for audits only, not active Package B use",
        ),
    ]


def build_invalid_uses() -> list[InvalidStatusUse]:
    return [
        InvalidStatusUse(
            name="X1: hidden status handoff",
            shortcut="future handoff uses a component without stating its status mode",
            status="FORBIDDEN_SHORTCUT",
            reason="status mode is mandatory before theorem, adoption, precondition, or downstream handoff",
            failure_mode="audit status becomes ambiguous theory status",
        ),
        InvalidStatusUse(
            name="X2: compatible-if-declared as assigned status change",
            shortcut="treat compatible-if-declared as selected, adopted, derived, declared, or insertable",
            status="FORBIDDEN_SHORTCUT",
            reason="conditional survival is weaker than status assignment or choice",
            failure_mode="Group 36 accidentally changes Package B status",
        ),
        InvalidStatusUse(
            name="X3: theorem target as proof",
            shortcut="treat theorem-target status as already derived",
            status="FORBIDDEN_SHORTCUT",
            reason="proof target is not proof",
            failure_mode="open theorem burden disappears by label",
        ),
        InvalidStatusUse(
            name="X4: adopted postulate as derivation",
            shortcut="report an explicit postulate adoption as a derived theorem",
            status="FORBIDDEN_SHORTCUT",
            reason="adoption is choice, not proof",
            failure_mode="postulate/theorem boundary collapses",
        ),
        InvalidStatusUse(
            name="X5: one component status licenses the other",
            shortcut="use one component's declaration, theorem, or adoption status to license the other Package B node",
            status="FORBIDDEN_SHORTCUT",
            reason="trace normalization and safe membership remain separate nodes",
            failure_mode="Package B hides a second choice or proof burden",
        ),
        InvalidStatusUse(
            name="X6: diagnostic-only as active",
            shortcut="use a diagnostic-only label to alter equations or support insertion",
            status="FORBIDDEN_SHORTCUT",
            reason="diagnostic labels are safe only if inert",
            failure_mode="audit label becomes active projector or insertion handle",
        ),
        InvalidStatusUse(
            name="X7: status precondition as insertion",
            shortcut="treat status clarity as B_s/F_zeta insertion, active O, residual control, or parent readiness",
            status="FORBIDDEN_SHORTCUT",
            reason="downstream gates remain closed",
            failure_mode="status bookkeeping opens field-equation gates prematurely",
        ),
    ]


def build_obligations() -> list[StatusObligation]:
    return [
        StatusObligation(
            name="O1: preserve current compatible-if-declared status",
            obligation="record Group 33/34 surviving forms as compatible-if-declared only unless later changed explicitly",
            status="OPEN",
            blocks="selection and adoption drift",
            discipline="do not shorten current status to selected, adopted, derived, declared, or insertable",
        ),
        StatusObligation(
            name="O2: require explicit status mode before handoff",
            obligation="state status mode for P_trace_norm and P_safe_membership before theorem, adoption, declaration, or precondition handoff",
            status="OPEN",
            blocks="ambiguous component use",
            discipline="hidden status must not license downstream work",
        ),
        StatusObligation(
            name="O3: preserve mixed-status visibility",
            obligation="if component statuses differ, carry mixed status explicitly",
            status="OPEN",
            blocks="Package B overclaim",
            discipline="one component's status cannot license the other",
        ),
        StatusObligation(
            name="O4: preserve postulate/theorem boundary",
            obligation="do not call adopted postulates derived and do not call theorem targets proved",
            status="OPEN",
            blocks="governance drift",
            discipline="choice and proof remain separate",
        ),
        StatusObligation(
            name="O5: adoption boundary",
            obligation="do not adopt Package B or either component in this status precondition matrix",
            status="REQUIRED",
            blocks="accidental adoption",
            discipline="adoption requires a separate explicit decision record",
        ),
        StatusObligation(
            name="O6: downstream gates",
            obligation="keep B_s/F_zeta insertion, active O, residual control, and parent closure closed",
            status="NOT_READY",
            blocks="downstream overreach",
            discipline="status preconditions are not insertion or parent readiness",
        ),
    ]


def build_conclusions() -> list[ConclusionEntry]:
    return [
        ConclusionEntry(
            name="C1: status preconditions inventoried",
            conclusion="component status modes and status-pair hazards are visible as preconditions",
            status="STATUS_REQUIRED",
            meaning="future work can see which status tags must be explicit before use",
        ),
        ConclusionEntry(
            name="C2: current status preserved",
            conclusion="trace-normalization and safe-membership surviving forms remain compatible-if-declared only",
            status="COMPATIBLE_IF_DECLARED",
            meaning="current audit status is not selected, adopted, derived, declared, or insertable",
        ),
        ConclusionEntry(
            name="C3: no status assigned",
            conclusion="this matrix assigns no Package B component status as theory state",
            status="NOT_ASSIGNED",
            meaning="status precondition matrix is not a status-change record",
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
            meaning="status preconditions do not open field-equation gates",
        ),
        ConclusionEntry(
            name="C6: next",
            conclusion="safety precondition ledger should run next",
            status="OPEN",
            meaning="node separation, hidden-load, incidence/residual, source/divergence, and downstream gate preconditions should be inventoried next",
        ),
    ]


# ----------------------------------------------------------------------------------------------------------------------
# Cases
# ----------------------------------------------------------------------------------------------------------------------


def case_0_problem() -> None:
    header("Case 0: Status precondition matrix problem")
    print(
        "Question:\n\n"
        "  Which status modes and status-pair conditions must be explicit before\n"
        "  trace-normalization and safe-membership Package B components can be\n"
        "  used in later routes?\n\n"
        "Discipline:\n\n"
        "  This script inventories status preconditions.\n"
        "  It assigns no Package B component status as theory state.\n"
        "  It fills no declaration slot.\n"
        "  It selects no trace-normalization form.\n"
        "  It selects no safe-membership form.\n"
        "  It adopts no Package B component.\n"
        "  It recommends no Package B adoption.\n"
        "  It derives no coefficient law and no insertion.\n"
        "  It keeps active O, residual control, and parent closure closed.\n\n"
        "Tiny goblin rule:\n"
        "  Sort the key tags. Do not put one in the lock.\n"
    )
    out_line(
        "governance_assessments",
        "PASS",
        "status precondition matrix opened",
        "status modes are audited as preconditions only; none are assigned as theory state",
    )


def case_1_symbolic_ledger() -> StatusSymbols:
    header("Case 1: Status precondition symbolic ledger")

    P_trace_norm, P_safe_membership = sp.symbols("P_trace_norm P_safe_membership")
    compatible_if_declared, declared_candidate, theorem_target = sp.symbols(
        "compatible_if_declared declared_candidate theorem_target"
    )
    adopted_postulate, diagnostic_only, deferred_status = sp.symbols(
        "adopted_postulate diagnostic_only deferred_status"
    )
    mixed_status, hidden_status, status_drift, node_license = sp.symbols(
        "mixed_status hidden_status status_drift node_license"
    )
    P_insertion, P_active_O, P_residual_kill, P_parent = sp.symbols(
        "P_insertion P_active_O P_residual_kill P_parent"
    )

    L_component = sp.simplify(
        compatible_if_declared + declared_candidate + theorem_target + adopted_postulate + diagnostic_only + deferred_status
    )
    L_pairs = sp.simplify(mixed_status + node_license)
    L_invalid = sp.simplify(hidden_status + status_drift)
    L_downstream = sp.simplify(P_insertion + P_active_O + P_residual_kill + P_parent)
    L_gap = sp.simplify(P_trace_norm + P_safe_membership + L_component + L_pairs + L_invalid + L_downstream)

    print("Status-precondition symbols:")
    for sym in [
        P_trace_norm, P_safe_membership, compatible_if_declared, declared_candidate,
        theorem_target, adopted_postulate, diagnostic_only, deferred_status,
        mixed_status, hidden_status, status_drift, node_license,
        P_insertion, P_active_O, P_residual_kill, P_parent,
    ]:
        print(f"  {sym} = {sym}")

    print()
    print(f"Component status-precondition load:\n  L_component_status_preconditions = {L_component}")
    print(f"Status-pair precondition load:\n  L_status_pair_preconditions = {L_pairs}")
    print(f"Invalid status mode load:\n  L_invalid_status_modes = {L_invalid}")
    print(f"Downstream closed load:\n  L_downstream_closed = {L_downstream}")
    print(f"Status-precondition gap:\n  L_status_gap = {L_gap}")

    out_line(
        "derived_results",
        "PASS",
        "status-precondition symbolic loads stated",
        f"L_component_status_preconditions={L_component}; L_downstream_closed={L_downstream}",
    )

    return StatusSymbols(L_component, L_pairs, L_invalid, L_downstream, L_gap)


def case_2_status_modes(items: Iterable[StatusModePrecondition]) -> None:
    header("Case 2: Component status-mode preconditions")
    items_list = list(items)
    for item in items_list:
        subheader(item.name)
        print(f"Mode: {item.mode}")
        out_line("governance_assessments", item.status, item.name)
        print(f"Allowed meaning: {item.allowed_meaning}")
        print(f"Required before: {item.required_before}")
        print(f"Forbidden upgrade: {item.forbidden_upgrade}")
    out_line("governance_assessments", "PASS", "component status-mode preconditions inventoried", f"{len(items_list)} status modes stated")


def case_3_status_pairs(items: Iterable[StatusPairCase]) -> None:
    header("Case 3: Joint status-pair preconditions")
    items_list = list(items)
    for item in items_list:
        subheader(item.name)
        print(f"Pair: {item.pair}")
        out_line("governance_assessments", item.status, item.name)
        print(f"Coherent if: {item.coherent_if}")
        print(f"Blocked if: {item.blocked_if}")
        print(f"Boundary: {item.boundary}")
    out_line("governance_assessments", "OBLIGATION", "joint status-pair preconditions stated", f"{len(items_list)} status-pair cases stated")


def case_4_invalid_uses(items: Iterable[InvalidStatusUse]) -> None:
    header("Case 4: Invalid status-precondition uses")
    items_list = list(items)
    for item in items_list:
        subheader(item.name)
        print(f"Shortcut: {item.shortcut}")
        out_line("counterexamples", item.status, item.name)
        print(f"Reason: {item.reason}")
        print(f"Failure mode: {item.failure_mode}")
    out_line("counterexamples", "FAIL", "invalid status-precondition uses rejected", f"{len(items_list)} shortcuts rejected")


def case_5_obligations(items: Iterable[StatusObligation]) -> None:
    header("Case 5: Status-precondition obligations")
    items_list = list(items)
    for item in items_list:
        subheader(item.name)
        print(f"Obligation: {item.obligation}")
        out_line("unresolved_obligations", item.status, item.name)
        print(f"Blocks: {item.blocks}")
        print(f"Discipline: {item.discipline}")
    out_line("unresolved_obligations", "OBLIGATION", "status-precondition obligations opened", f"{len(items_list)} obligations stated")


def case_6_conclusions(items: Iterable[ConclusionEntry]) -> None:
    header("Case 6: Status-precondition conclusions")
    items_list = list(items)
    for item in items_list:
        subheader(item.name)
        print(f"Conclusion: {item.conclusion}")
        out_line("governance_assessments", item.status, item.name)
        print(f"Meaning: {item.meaning}")
    out_line(
        "governance_assessments",
        "PASS",
        "status precondition matrix conclusion stated",
        "status preconditions inventoried; no statuses assigned, no adoption, downstream gates closed",
    )


def final_interpretation() -> None:
    header("Final interpretation")
    print(
        "Trace-anchor status precondition matrix result:\n\n"
        "  Status preconditions for trace normalization and safe membership are now inventoried.\n"
        "  Current Group 33/34 surviving forms remain compatible-if-declared only.\n"
        "  Future modes include declared candidate, theorem target, adopted postulate, diagnostic-only, and deferred, but none are assigned here.\n"
        "  Mixed component statuses must remain visible before any handoff.\n"
        "  Hidden status, compatible-if-declared-as-assigned, theorem-target-as-proof, adopted-as-derived, one-node-licenses-the-other, diagnostic-as-active, and status-as-insertion shortcuts fail.\n"
        "  No Package B component status is assigned as theory state.\n"
        "  No trace-normalization or safe-membership form is selected, adopted, or derived.\n"
        "  Package B is not recommended for adoption.\n"
        "  B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready.\n\n"
        "Possible next script:\n"
        "  candidate_trace_anchor_safety_precondition_ledger.py\n\n"
        "Tiny goblin label:\n"
        "  Sort the key tags. Do not put one in the lock.\n"
    )
    out_line(
        "governance_assessments",
        "PASS",
        "trace-anchor status precondition matrix complete",
        "safety precondition ledger should run next; adoption and downstream gates remain closed",
    )


# ----------------------------------------------------------------------------------------------------------------------
# Archive records
# ----------------------------------------------------------------------------------------------------------------------


def record_inventory_marker(ns, symbolic: StatusSymbols) -> None:
    ns.record_derivation(
        derivation_id="g36_status_precond_matrix",
        inputs=[
            symbolic.L_component_status_preconditions,
            symbolic.L_status_pair_preconditions,
            symbolic.L_invalid_status_modes,
            symbolic.L_downstream_closed,
        ],
        output=symbolic.L_status_gap,
        method="Group 36 trace-anchor status precondition matrix",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="status_precondition_matrix_marker",
        is_placeholder=True,
    )


def record_obligations(ns, obligations: Iterable[StatusObligation]) -> None:
    for item in obligations:
        ident = safe_ident(item.name)
        status = ObligationStatus.OPEN if item.status != "NOT_READY" else ObligationStatus.DEFERRED
        ns.record_obligation(
            ProofObligationRecord(
                obligation_id=f"g36_st_{ident}",
                script_id=SCRIPT_ID,
                title=item.name,
                status=status,
                required_by=[SCRIPT_ID],
                description=f"{item.obligation}. Blocks: {item.blocks}. Discipline: {item.discipline}.",
            )
        )


def record_governance(
    ns,
    modes: Iterable[StatusModePrecondition],
    pairs: Iterable[StatusPairCase],
    invalid_uses: Iterable[InvalidStatusUse],
) -> None:
    ns.record_route(
        RouteRecord(
            route_id="g36_st_precond",
            script_id=SCRIPT_ID,
            name="Trace-anchor status precondition matrix route",
            status=GovernanceStatus.CANDIDATE_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            required_obligations=[
                "g36_st_o1",
                "g36_st_o2",
                "g36_st_o3",
                "g36_st_o4",
                "g36_st_o5",
                "g36_st_o6",
            ],
            activation_conditions=[
                "Group 36 declaration precondition ledger complete",
                "status preconditions inventoried only",
                "no component status assigned as theory state",
                "no Package B component adopted",
                "downstream gates closed",
            ],
        )
    )

    for item in modes:
        ident = safe_ident(item.name)
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g36_st_m_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.CANDIDATE_ROUTE,
                statement=(
                    f"Status-mode precondition: {item.mode}. Allowed meaning: {item.allowed_meaning}. "
                    f"Required before: {item.required_before}. Forbidden upgrade: {item.forbidden_upgrade}."
                ),
                derivation_ids=["g36_status_precond_matrix"],
                obligation_ids=[],
            )
        )

    for item in pairs:
        ident = safe_ident(item.name)
        status = GovernanceStatus.CANDIDATE_ROUTE
        if item.status in {"MIXED_STATUS_VISIBLE", "THEOREM_TARGET"}:
            status = GovernanceStatus.DEFERRED_PENDING_PREREQUISITES
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g36_st_p_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=status,
                statement=(
                    f"Status-pair precondition: {item.pair}. Coherent if: {item.coherent_if}. "
                    f"Blocked if: {item.blocked_if}. Boundary: {item.boundary}."
                ),
                derivation_ids=["g36_status_precond_matrix"],
                obligation_ids=[],
            )
        )

    for item in invalid_uses:
        ident = safe_ident(item.name)
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g36_st_x_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.REJECTED_ROUTE,
                statement=f"Forbidden status-precondition shortcut: {item.shortcut}. Reason: {item.reason}. Failure mode: {item.failure_mode}.",
                derivation_ids=["g36_status_precond_matrix"],
                obligation_ids=[],
            )
        )

    policy_rules = [
        ("g36_st_pol_hidden", "Future handoffs must state status mode for each Package B component."),
        ("g36_st_pol_current", "Compatible-if-declared remains current audit status unless changed explicitly."),
        ("g36_st_pol_mixed", "Mixed component statuses must remain visible and cannot license uniform Package B use."),
        ("g36_st_pol_adopt", "Status-precondition inventory adopts no Package B component."),
        ("g36_st_pol_insert", "Status-precondition inventory does not license insertion, active O, residual control, or parent closure."),
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
                derivation_ids=["g36_status_precond_matrix"],
                obligation_ids=[],
            )
        )


# ----------------------------------------------------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------------------------------------------------


def main() -> None:
    header("Candidate Trace Anchor Status Precondition Matrix")
    archive, ns, invalidated = prepare_archive()
    ensure_archive_write_dirs(ns)
    print_archive_status(ns, invalidated)

    modes = build_status_modes()
    pairs = build_status_pairs()
    invalid_uses = build_invalid_uses()
    obligations = build_obligations()
    conclusions = build_conclusions()

    case_0_problem()
    symbolic = case_1_symbolic_ledger()
    case_2_status_modes(modes)
    case_3_status_pairs(pairs)
    case_4_invalid_uses(invalid_uses)
    case_5_obligations(obligations)
    case_6_conclusions(conclusions)
    final_interpretation()

    record_inventory_marker(ns, symbolic)
    record_obligations(ns, obligations)
    record_governance(ns, modes, pairs, invalid_uses)

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
