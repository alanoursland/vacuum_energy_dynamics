# Candidate Trace Anchor Safety Precondition Ledger
#
# Group:
#   36_conditional_trace_anchor_precondition_inventory
#
# Human title:
#   Trace Anchor Safety Precondition Ledger
#
# Script type:
#   PRECONDITION LEDGER / SAFETY AUDIT
#
# Purpose
# -------
# Inventory the safety preconditions that must remain explicit before
# trace-normalization and safe-membership Package B components can be used in
# later declaration, theorem, adoption, precondition, insertion-facing, or
# parent-facing routes.
#
# This script does not fill any declaration slot.
# It assigns no Package B component status as theory state.
# It selects no trace-normalization form.
# It selects no safe-membership form.
# It adopts no Package B component.
# It recommends no Package B adoption.
# It derives no coefficient law and no insertion.
# It keeps active O, residual control, and parent closure closed.
#
# Tiny goblin rule:
#   Check the traps around the lock. Still do not open the door.

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
        "BLOCKED_IF_BLANK": StatusMark.DEFER,
        "COMPATIBLE_IF_DECLARED": StatusMark.INFO,
        "CONDITIONAL": StatusMark.DEFER,
        "DEFERRED": StatusMark.DEFER,
        "FAIL": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
        "INERT_ONLY": StatusMark.INFO,
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
            "g36_status_pc",
            "36_conditional_trace_anchor_precondition_inventory__candidate_trace_anchor_status_precondition_matrix",
            "g36_status_precond_matrix",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g36_decl_pc",
            "36_conditional_trace_anchor_precondition_inventory__candidate_trace_anchor_declaration_precondition_ledger",
            "g36_decl_precond_ledger",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g36_problem",
            "36_conditional_trace_anchor_precondition_inventory__candidate_trace_anchor_precondition_inventory_problem",
            "g36_precondition_inventory_problem",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g35_summary",
            "35_trace_anchor_joint_declaration_inventory__candidate_group_35_status_summary",
            "g35_status_summary",
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
class SafetySymbols:
    L_trace_anchor_safety: sp.Basic
    L_visibility_safety: sp.Basic
    L_downstream_closed: sp.Basic
    L_invalid_safety_modes: sp.Basic
    L_safety_gap: sp.Basic


@dataclass
class SafetyGate:
    name: str
    gate: str
    status: str
    required_before: str
    discipline: str
    forbidden_upgrade: str


@dataclass
class SafetyCheck:
    name: str
    check: str
    status: str
    passes_if: str
    fails_if: str
    boundary: str


@dataclass
class InvalidSafetyUse:
    name: str
    shortcut: str
    status: str
    reason: str
    failure_mode: str


@dataclass
class SafetyObligation:
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


def build_safety_gates() -> list[SafetyGate]:
    return [
        SafetyGate(
            name="G1: node-separation gate",
            gate="P_trace_norm and P_safe_membership remain separate Package B nodes",
            status="SAFETY_REQUIRED",
            required_before="any joint Package B use or handoff",
            discipline="normalization cannot choose membership and membership cannot choose normalization",
            forbidden_upgrade="must not collapse Package B into one hidden choice",
        ),
        SafetyGate(
            name="G2: hidden-load exclusion gate",
            gate="membership and normalization carry no hidden residual, ordinary-source, correction, boundary, support, or downstream payload",
            status="SAFETY_REQUIRED",
            required_before="safe-membership or joint trace-anchor use",
            discipline="Package B components are not cleanup reservoirs",
            forbidden_upgrade="must not hide load in a trace anchor component",
        ),
        SafetyGate(
            name="G3: role-purity gate",
            gate="safe membership remains trace-sector membership only unless separately derived or adopted otherwise",
            status="SAFETY_REQUIRED",
            required_before="role-pure membership use or theorem attempt",
            discipline="role purity is a precondition, not residual kill or source theorem",
            forbidden_upgrade="must not use membership as source, divergence, residual, boundary, or insertion mechanism",
        ),
        SafetyGate(
            name="G4: incidence separation gate",
            gate="safe membership remains separate from trace/residual zero incidence",
            status="SAFETY_REQUIRED",
            required_before="any scalar recombination or insertion-facing handoff",
            discipline="membership is not I(T_zeta,R_zeta)=0 or I(T_zeta,R_kappa)=0",
            forbidden_upgrade="must not smuggle no-overlap through a membership label",
        ),
        SafetyGate(
            name="G5: residual-control separation gate",
            gate="trace normalization and safe membership remain separate from residual kill, residual inertness, and active O",
            status="SAFETY_REQUIRED",
            required_before="any residual-facing or insertion-facing route",
            discipline="Package B is not a residual-control theorem",
            forbidden_upgrade="must not turn trace-anchor clarity into residual control",
        ),
        SafetyGate(
            name="G6: source-visibility gate",
            gate="ordinary source load remains visible and cannot be hidden in coefficients, membership, correction, boundary, support, or parent-placeholder channels",
            status="SAFETY_REQUIRED",
            required_before="any theorem, adoption, or precondition route that touches source behavior",
            discipline="visibility is not the full source no-double-counting theorem",
            forbidden_upgrade="must not treat visibility as source neutrality or source theorem",
        ),
        SafetyGate(
            name="G7: divergence-explicitness gate",
            gate="correction/divergence behavior remains explicit, auditable, and non-reservoir",
            status="SAFETY_REQUIRED",
            required_before="any route that might touch correction or divergence behavior",
            discipline="explicitness is not divergence-safe coefficient law",
            forbidden_upgrade="must not use explicit correction language as a reservoir or Bianchi repair",
        ),
        SafetyGate(
            name="G8: diagnostic-inertness gate",
            gate="diagnostic-only labels remain strictly equation-inert",
            status="INERT_ONLY",
            required_before="diagnostic membership or trace-anchor audit labels",
            discipline="diagnostic labels may audit but cannot alter equations",
            forbidden_upgrade="must not become active projector, insertion handle, or parent input",
        ),
        SafetyGate(
            name="G9: downstream-gate lock",
            gate="B_s/F_zeta insertion, active O, residual control, and parent closure remain not ready",
            status="NOT_READY",
            required_before="any downstream route",
            discipline="safety preconditions are not insertion or parent readiness",
            forbidden_upgrade="must not open downstream gates from safety clarity",
        ),
    ]


def build_safety_checks() -> list[SafetyCheck]:
    return [
        SafetyCheck(
            name="Ck1: hidden-load check",
            check="trace-anchor components are checked for residual, source, correction, boundary, support, or downstream payload",
            status="BLOCKED_IF_BLANK",
            passes_if="all exclusion zones are explicit before use",
            fails_if="any payload is hidden inside membership, normalization, coefficient, or status language",
            boundary="a clean payload check does not prove source neutrality or residual control",
        ),
        SafetyCheck(
            name="Ck2: incidence check",
            check="membership is checked not to imply trace/residual zero incidence",
            status="BLOCKED_IF_BLANK",
            passes_if="incidence remains a separate theorem target or explicit later route",
            fails_if="membership survival is treated as zero incidence or no-overlap",
            boundary="incidence separation is not an incidence theorem",
        ),
        SafetyCheck(
            name="Ck3: residual check",
            check="trace-anchor use is checked not to imply residual kill, residual inertness, or active O",
            status="NOT_READY",
            passes_if="residual gates remain marked separate and not ready",
            fails_if="Package B is used as residual control",
            boundary="residual control remains downstream and unresolved",
        ),
        SafetyCheck(
            name="Ck4: source/divergence visibility check",
            check="source and divergence loads are checked for visibility and non-reservoir behavior",
            status="SAFETY_REQUIRED",
            passes_if="loads remain explicit and auditable",
            fails_if="ordinary source or divergence load is hidden in a trace-anchor component",
            boundary="visibility filters may reject but cannot choose or prove components",
        ),
        SafetyCheck(
            name="Ck5: downstream lock check",
            check="insertion, active O, residual control, and parent closure remain closed",
            status="NOT_READY",
            passes_if="future handoff keeps downstream status separate from trace-anchor preconditions",
            fails_if="safety preconditions are treated as field-equation use",
            boundary="precondition clarity is not insertion or parent readiness",
        ),
    ]


def build_invalid_uses() -> list[InvalidSafetyUse]:
    return [
        InvalidSafetyUse(
            name="X1: hidden payload as trace anchor",
            shortcut="carry residual, source, correction, boundary, support, or downstream payload through a Package B component",
            status="FORBIDDEN_SHORTCUT",
            reason="trace-anchor components are not hidden-load pockets",
            failure_mode="membership or normalization becomes cleanup reservoir",
        ),
        InvalidSafetyUse(
            name="X2: membership as incidence",
            shortcut="treat zeta_Bs -> T_zeta as trace/residual zero incidence",
            status="FORBIDDEN_SHORTCUT",
            reason="safe membership and incidence are separate nodes",
            failure_mode="high-risk no-overlap theorem burden disappears by label",
        ),
        InvalidSafetyUse(
            name="X3: normalization as residual control",
            shortcut="treat trace-normalization compatibility as residual kill or residual non-entry",
            status="FORBIDDEN_SHORTCUT",
            reason="normalization tells how B_s reads zeta; it does not control residuals",
            failure_mode="Package B becomes residual-control shortcut",
        ),
        InvalidSafetyUse(
            name="X4: visibility as source theorem",
            shortcut="treat source visibility as full source no-double-counting theorem",
            status="FORBIDDEN_SHORTCUT",
            reason="visibility is an audit precondition, not a completed source theorem",
            failure_mode="ordinary source duplication risk is silently closed",
        ),
        InvalidSafetyUse(
            name="X5: explicitness as divergence safety",
            shortcut="treat correction/divergence explicitness as divergence-safe coefficient law",
            status="FORBIDDEN_SHORTCUT",
            reason="explicit non-reservoir behavior is weaker than divergence proof",
            failure_mode="Bianchi or parent divergence burden disappears",
        ),
        InvalidSafetyUse(
            name="X6: diagnostic label as active operator",
            shortcut="use diagnostic-only labels to alter equations, project sectors, or support insertion",
            status="FORBIDDEN_SHORTCUT",
            reason="diagnostic labels are safe only if inert",
            failure_mode="audit label becomes active O by another name",
        ),
        InvalidSafetyUse(
            name="X7: safety precondition as downstream theorem",
            shortcut="treat safety clarity as B_s/F_zeta insertion, active O, residual control, or parent readiness",
            status="FORBIDDEN_SHORTCUT",
            reason="downstream gates remain closed",
            failure_mode="precondition ledger opens field-equation gates prematurely",
        ),
    ]


def build_obligations() -> list[SafetyObligation]:
    return [
        SafetyObligation(
            name="O1: preserve node separation",
            obligation="keep trace normalization and safe membership as separate nodes in all future routes",
            status="OPEN",
            blocks="Package B collapse",
            discipline="one node cannot choose, prove, or license the other",
        ),
        SafetyObligation(
            name="O2: exclude hidden payloads",
            obligation="keep residual, source, correction/divergence, boundary/support, and downstream payloads outside Package B components unless separately derived",
            status="OPEN",
            blocks="hidden-load smuggling",
            discipline="trace-anchor components are not cleanup reservoirs",
        ),
        SafetyObligation(
            name="O3: preserve incidence and residual separation",
            obligation="keep trace/residual zero incidence, residual kill, residual inertness, and active O separate from Package B compatibility",
            status="OPEN",
            blocks="no-overlap and residual-control shortcuts",
            discipline="membership and normalization are not incidence or residual control",
        ),
        SafetyObligation(
            name="O4: preserve source and divergence visibility",
            obligation="keep source load and divergence/correction behavior visible, auditable, and non-reservoir",
            status="OPEN",
            blocks="source and divergence smuggling",
            discipline="visibility and explicitness are preconditions, not full theorems",
        ),
        SafetyObligation(
            name="O5: adoption boundary",
            obligation="do not adopt Package B or either component in this safety precondition ledger",
            status="REQUIRED",
            blocks="accidental adoption",
            discipline="adoption requires a separate explicit decision record",
        ),
        SafetyObligation(
            name="O6: downstream gates",
            obligation="keep B_s/F_zeta insertion, active O, residual control, and parent closure closed",
            status="NOT_READY",
            blocks="downstream overreach",
            discipline="safety preconditions are not insertion or parent readiness",
        ),
    ]


def build_conclusions() -> list[ConclusionEntry]:
    return [
        ConclusionEntry(
            name="C1: safety preconditions inventoried",
            conclusion="node separation, hidden-load exclusion, role purity, incidence/residual separation, source/divergence visibility, diagnostic inertness, and downstream locks are visible",
            status="SAFETY_REQUIRED",
            meaning="future work can see which safety gates must remain explicit before use",
        ),
        ConclusionEntry(
            name="C2: no declarations filled",
            conclusion="this ledger fills no declaration slots",
            status="NOT_CHOSEN",
            meaning="safety precondition ledger is not a declaration record",
        ),
        ConclusionEntry(
            name="C3: no status assigned",
            conclusion="this ledger assigns no Package B component status as theory state",
            status="NOT_ASSIGNED",
            meaning="safety inventory is not a status-change record",
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
            meaning="safety preconditions do not open field-equation gates",
        ),
        ConclusionEntry(
            name="C6: next",
            conclusion="handoff condition ledger should run next",
            status="OPEN",
            meaning="route handoff conditions can now be inventoried without choosing a route",
        ),
    ]


# ----------------------------------------------------------------------------------------------------------------------
# Cases
# ----------------------------------------------------------------------------------------------------------------------


def case_0_problem() -> None:
    header("Case 0: Safety precondition ledger problem")
    print(
        "Question:\n\n"
        "  Which safety preconditions must remain explicit before trace-normalization\n"
        "  and safe-membership Package B components can be used in later routes?\n\n"
        "Discipline:\n\n"
        "  This script inventories safety preconditions.\n"
        "  It fills no declaration slot.\n"
        "  It assigns no Package B component status as theory state.\n"
        "  It selects no trace-normalization form.\n"
        "  It selects no safe-membership form.\n"
        "  It adopts no Package B component.\n"
        "  It recommends no Package B adoption.\n"
        "  It derives no coefficient law and no insertion.\n"
        "  It keeps active O, residual control, and parent closure closed.\n\n"
        "Tiny goblin rule:\n"
        "  Check the traps around the lock. Still do not open the door."
    )
    out_line(
        "governance_assessments",
        "PASS",
        "safety precondition ledger opened",
        "safety gates are audited as preconditions only; no downstream gate is opened",
    )


def case_1_symbolic_ledger() -> SafetySymbols:
    header("Case 1: Safety precondition symbolic ledger")

    names = [
        "node_separation",
        "hidden_payload_gate",
        "role_purity",
        "incidence_gate",
        "residual_gate",
        "source_visibility",
        "div_visibility",
        "diagnostic_inertness",
        "downstream_lock",
        "hidden_load",
        "node_collapse",
        "incidence_smuggle",
        "residual_smuggle",
        "divergence_reservoir",
        "P_insertion",
        "P_active_O",
        "P_residual_kill",
        "P_parent",
    ]
    symbols = dict(zip(names, sp.symbols(" ".join(names))))

    print("Safety-precondition symbols:")
    for name in names:
        print(f"  {name} = {symbols[name]}")

    L_trace_anchor_safety = sp.simplify(
        symbols["node_separation"]
        + symbols["hidden_payload_gate"]
        + symbols["role_purity"]
        + symbols["incidence_gate"]
        + symbols["residual_gate"]
        + symbols["diagnostic_inertness"]
    )
    L_visibility_safety = sp.simplify(symbols["source_visibility"] + symbols["div_visibility"])
    L_downstream_closed = sp.simplify(
        symbols["P_insertion"] + symbols["P_active_O"] + symbols["P_residual_kill"] + symbols["P_parent"]
    )
    L_invalid_safety_modes = sp.simplify(
        symbols["hidden_load"]
        + symbols["node_collapse"]
        + symbols["incidence_smuggle"]
        + symbols["residual_smuggle"]
        + symbols["divergence_reservoir"]
    )
    L_safety_gap = sp.simplify(
        L_trace_anchor_safety + L_visibility_safety + L_downstream_closed + L_invalid_safety_modes
    )

    print()
    print(f"Trace-anchor safety load:\n  L_trace_anchor_safety = {L_trace_anchor_safety}")
    print(f"Visibility safety load:\n  L_visibility_safety = {L_visibility_safety}")
    print(f"Downstream closed load:\n  L_downstream_closed = {L_downstream_closed}")
    print(f"Invalid safety mode load:\n  L_invalid_safety_modes = {L_invalid_safety_modes}")
    print(f"Safety-precondition gap:\n  L_safety_gap = {L_safety_gap}")

    out_line(
        "derived_results",
        "PASS",
        "safety-precondition symbolic loads stated",
        f"L_trace_anchor_safety={L_trace_anchor_safety}; L_downstream_closed={L_downstream_closed}",
    )

    return SafetySymbols(
        L_trace_anchor_safety=L_trace_anchor_safety,
        L_visibility_safety=L_visibility_safety,
        L_downstream_closed=L_downstream_closed,
        L_invalid_safety_modes=L_invalid_safety_modes,
        L_safety_gap=L_safety_gap,
    )


def case_2_safety_gates(gates: Iterable[SafetyGate]) -> None:
    header("Case 2: Safety precondition gates")
    for item in gates:
        subheader(item.name)
        print(f"Gate: {item.gate}")
        out_line("governance_assessments", item.status, item.name, "")
        print(f"Required before: {item.required_before}")
        print(f"Discipline: {item.discipline}")
        print(f"Forbidden upgrade: {item.forbidden_upgrade}")
    out_line("governance_assessments", "PASS", "safety gates inventoried", "9 safety gates stated")


def case_3_safety_checks(checks: Iterable[SafetyCheck]) -> None:
    header("Case 3: Safety completeness checks")
    for item in checks:
        subheader(item.name)
        print(f"Check: {item.check}")
        out_line("governance_assessments", item.status, item.name, "")
        print(f"Passes if: {item.passes_if}")
        print(f"Fails if: {item.fails_if}")
        print(f"Boundary: {item.boundary}")
    out_line("governance_assessments", "INFO", "safety completeness checks stated", "5 checks stated")


def case_4_invalid_uses(invalid_uses: Iterable[InvalidSafetyUse]) -> None:
    header("Case 4: Invalid safety-precondition uses")
    for item in invalid_uses:
        subheader(item.name)
        print(f"Shortcut: {item.shortcut}")
        out_line("counterexamples", item.status, item.name, "")
        print(f"Reason: {item.reason}")
        print(f"Failure mode: {item.failure_mode}")
    out_line("counterexamples", "FAIL", "invalid safety-precondition uses rejected", "7 shortcuts rejected")


def case_5_obligations(obligations: Iterable[SafetyObligation]) -> None:
    header("Case 5: Safety-precondition obligations")
    for item in obligations:
        subheader(item.name)
        print(f"Obligation: {item.obligation}")
        out_line("unresolved_obligations", item.status, item.name, "")
        print(f"Blocks: {item.blocks}")
        print(f"Discipline: {item.discipline}")
    out_line("unresolved_obligations", "INFO", "safety-precondition obligations opened", "6 obligations stated")


def case_6_conclusions(conclusions: Iterable[ConclusionEntry]) -> None:
    header("Case 6: Safety-precondition conclusions")
    for item in conclusions:
        subheader(item.name)
        print(f"Conclusion: {item.conclusion}")
        out_line("governance_assessments", item.status, item.name, "")
        print(f"Meaning: {item.meaning}")
    out_line(
        "governance_assessments",
        "PASS",
        "safety precondition ledger conclusion stated",
        "safety preconditions inventoried; no choices made, no adoption, downstream gates closed",
    )


def final_interpretation() -> None:
    header("Final interpretation")
    print(
        "Trace-anchor safety precondition ledger result:\n\n"
        "  Safety preconditions for Package B use are now inventoried.\n"
        "  Node separation, hidden-load exclusion, role purity, incidence/residual separation, source visibility, divergence explicitness, and diagnostic inertness remain required.\n"
        "  Source visibility is not source no-double-counting theorem.\n"
        "  Divergence explicitness is not divergence-safe coefficient law.\n"
        "  Safe membership is not incidence, residual kill, active O, insertion, or parent readiness.\n"
        "  Trace normalization is not residual control or source cleanup.\n"
        "  No declaration value is filled by this ledger.\n"
        "  No Package B component status is assigned as theory state.\n"
        "  No trace-normalization or safe-membership form is selected, adopted, or derived.\n"
        "  Package B is not recommended for adoption.\n"
        "  B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready.\n\n"
        "Possible next script:\n"
        "  candidate_trace_anchor_handoff_condition_ledger.py\n\n"
        "Tiny goblin label:\n"
        "  Check the traps around the lock. Still do not open the door.\n"
    )
    out_line(
        "governance_assessments",
        "PASS",
        "trace-anchor safety precondition ledger complete",
        "handoff condition ledger should run next; adoption and downstream gates remain closed",
    )


# ----------------------------------------------------------------------------------------------------------------------
# Archive records
# ----------------------------------------------------------------------------------------------------------------------


def record_inventory_marker(ns, symbolic: SafetySymbols) -> None:
    ns.record_derivation(
        derivation_id="g36_safety_pc",
        inputs=[
            symbolic.L_trace_anchor_safety,
            symbolic.L_visibility_safety,
            symbolic.L_downstream_closed,
            symbolic.L_invalid_safety_modes,
        ],
        output=symbolic.L_safety_gap,
        method="Group 36 trace-anchor safety precondition ledger",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="safety_precondition_ledger_marker",
        is_placeholder=True,
    )


def record_obligations(ns, obligations: Iterable[SafetyObligation]) -> None:
    for item in obligations:
        ident = safe_ident(item.name)
        status = ObligationStatus.OPEN if item.status != "NOT_READY" else ObligationStatus.DEFERRED
        ns.record_obligation(
            ProofObligationRecord(
                obligation_id=f"g36_sf_{ident}",
                script_id=SCRIPT_ID,
                title=item.name,
                status=status,
                required_by=[SCRIPT_ID],
                description=f"{item.obligation}. Blocks: {item.blocks}. Discipline: {item.discipline}.",
            )
        )


def record_governance(
    ns,
    gates: Iterable[SafetyGate],
    checks: Iterable[SafetyCheck],
    invalid_uses: Iterable[InvalidSafetyUse],
) -> None:
    ns.record_route(
        RouteRecord(
            route_id="g36_safety_pc",
            script_id=SCRIPT_ID,
            name="Trace-anchor safety precondition ledger route",
            status=GovernanceStatus.CANDIDATE_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            required_obligations=[
                "g36_sf_o1",
                "g36_sf_o2",
                "g36_sf_o3",
                "g36_sf_o4",
                "g36_sf_o5",
                "g36_sf_o6",
            ],
            activation_conditions=[
                "Group 36 status precondition matrix complete",
                "safety preconditions inventoried only",
                "no declaration values filled",
                "no component status assigned",
                "no Package B component adopted",
                "downstream gates closed",
            ],
        )
    )

    for item in gates:
        ident = safe_ident(item.name)
        status = GovernanceStatus.CANDIDATE_ROUTE
        if item.status in {"SAFETY_REQUIRED", "PRECONDITION_REQUIRED"}:
            status = GovernanceStatus.POLICY_RULE
        if item.status == "NOT_READY":
            status = GovernanceStatus.DEFERRED_PENDING_PREREQUISITES
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g36_sf_g_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=status,
                statement=(
                    f"Safety precondition gate: {item.gate}. Required before: {item.required_before}. "
                    f"Discipline: {item.discipline}. Forbidden upgrade: {item.forbidden_upgrade}."
                ),
                derivation_ids=["g36_safety_pc"],
                obligation_ids=[],
            )
        )

    for item in checks:
        ident = safe_ident(item.name)
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g36_sf_c_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
                statement=(
                    f"Safety completeness check: {item.check}. Passes if: {item.passes_if}. "
                    f"Fails if: {item.fails_if}. Boundary: {item.boundary}."
                ),
                derivation_ids=["g36_safety_pc"],
                obligation_ids=[],
            )
        )

    for item in invalid_uses:
        ident = safe_ident(item.name)
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g36_sf_x_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.REJECTED_ROUTE,
                statement=f"Forbidden safety-precondition shortcut: {item.shortcut}. Reason: {item.reason}. Failure mode: {item.failure_mode}.",
                derivation_ids=["g36_safety_pc"],
                obligation_ids=[],
            )
        )

    policy_rules = [
        ("g36_sf_pol_nodes", "Trace normalization and safe membership remain separate Package B nodes."),
        ("g36_sf_pol_payload", "Package B components cannot carry hidden residual, source, correction, boundary, support, or downstream payloads."),
        ("g36_sf_pol_inc", "Safe membership is not trace/residual zero incidence."),
        ("g36_sf_pol_res", "Trace-anchor clarity is not residual control or active O."),
        ("g36_sf_pol_vis", "Source visibility and divergence explicitness are preconditions, not completed source/divergence theorems."),
        ("g36_sf_pol_down", "Safety preconditions do not license insertion, active O, residual control, or parent closure."),
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
                derivation_ids=["g36_safety_pc"],
                obligation_ids=[],
            )
        )


# ----------------------------------------------------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------------------------------------------------


def main() -> None:
    header("Candidate Trace Anchor Safety Precondition Ledger")
    archive, ns, invalidated = prepare_archive()
    ensure_archive_write_dirs(ns)
    print_archive_status(ns, invalidated)

    gates = build_safety_gates()
    checks = build_safety_checks()
    invalid_uses = build_invalid_uses()
    obligations = build_obligations()
    conclusions = build_conclusions()

    case_0_problem()
    symbolic = case_1_symbolic_ledger()
    case_2_safety_gates(gates)
    case_3_safety_checks(checks)
    case_4_invalid_uses(invalid_uses)
    case_5_obligations(obligations)
    case_6_conclusions(conclusions)
    final_interpretation()

    record_inventory_marker(ns, symbolic)
    record_obligations(ns, obligations)
    record_governance(ns, gates, checks, invalid_uses)

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
