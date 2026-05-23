# Candidate Group 36 Status Summary
#
# Group:
#   36_conditional_trace_anchor_precondition_inventory
#
# Human title:
#   Conditional Trace Anchor Precondition Inventory
#
# Script type:
#   SUMMARY / PRECONDITION-INVENTORY CLOSURE
#
# Purpose
# -------
# Close Group 36 by summarizing the conditional trace-anchor precondition inventory:
#
#   precondition inventory opener,
#   declaration precondition ledger,
#   status precondition matrix,
#   safety precondition ledger,
#   handoff condition ledger,
#   precondition obligations summary.
#
# Locked-door question:
#
#   What did Group 36 establish about the preconditions needed before Package B
#   components can be used, and what remains open before declaration, adoption,
#   theorem, insertion, or parent routes?
#
# This script does not choose a route.
# It does not fill declaration slots.
# It does not assign Package B component status as theory state.
# It does not select trace-normalization or safe-membership forms.
# It does not adopt Package B or either component.
# It does not recommend Package B adoption.
# It does not derive a coefficient law or B_s/F_zeta insertion.
# It does not open active O, residual control, or parent closure.
#
# Tiny goblin rule:
#   Count the locks. Close the inventory. Do not open the door.

from __future__ import annotations

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


# ----------------------------------------------------------------------------------------------------------------------
# Output helpers
# ----------------------------------------------------------------------------------------------------------------------


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
    raw = name.split(":", 1)[0].strip().lower()
    return "".join(ch if ch.isalnum() else "_" for ch in raw).strip("_")


def status_mark(status: str) -> StatusMark:
    return {
        "ADOPTION_REQUIRES_DECISION": StatusMark.DEFER,
        "AUDIT_READY": StatusMark.INFO,
        "COMPATIBLE_IF_DECLARED": StatusMark.INFO,
        "CONDITIONAL": StatusMark.DEFER,
        "DECLARATION_PRECONDITION": StatusMark.OBLIGATION,
        "DEFER": StatusMark.DEFER,
        "FAIL": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
        "HANDOFF_READY": StatusMark.INFO,
        "HANDOFF_CONDITION": StatusMark.OBLIGATION,
        "INFO": StatusMark.INFO,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_ASSIGNED": StatusMark.DEFER,
        "NOT_CHOSEN": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "PASS": StatusMark.PASS,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "PRECONDITION_INVENTORY": StatusMark.INFO,
        "PRECONDITION_OBLIGATION": StatusMark.OBLIGATION,
        "REQUIRED": StatusMark.OBLIGATION,
        "SAFETY_PRECONDITION": StatusMark.OBLIGATION,
        "STATUS_PRECONDITION": StatusMark.OBLIGATION,
        "THEOREM_TARGET": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def out_line(block: str, status: str, label: str, detail: str = "") -> None:
    mark = status_mark(status).value
    print(f"[{block}]")
    if detail:
        print(f"{mark} {label} -- {status}\n{detail}")
    else:
        print(f"{mark} {label} -- {status}")


# ----------------------------------------------------------------------------------------------------------------------
# Archive setup
# ----------------------------------------------------------------------------------------------------------------------


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g36_pc_obl",
            "036_conditional_trace_anchor_precondition_inventory__candidate_trace_anchor_precondition_obligations",
            "g36_pc_obligations",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g36_handoff_pc",
            "036_conditional_trace_anchor_precondition_inventory__candidate_trace_anchor_handoff_condition_ledger",
            "g36_handoff_pc",
            RecordKind.INVENTORY_MARKER,
        ),
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


# ----------------------------------------------------------------------------------------------------------------------
# Data
# ----------------------------------------------------------------------------------------------------------------------


@dataclass
class SummarySymbols:
    L_declaration: sp.Basic
    L_status: sp.Basic
    L_safety: sp.Basic
    L_handoff: sp.Basic
    L_downstream_closed: sp.Basic
    L_group36_summary: sp.Basic


@dataclass
class StatusEntry:
    name: str
    topic: str
    result: str
    status: str
    boundary: str


@dataclass
class GapEntry:
    name: str
    reason: str
    status: str
    discipline: str


@dataclass
class HandoffEntry:
    name: str
    reason: str
    status: str
    caution: str


@dataclass
class RuleEntry:
    name: str
    upgrade: str
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


def build_status_entries() -> list[StatusEntry]:
    return [
        StatusEntry(
            name="G36-1: precondition inventory opener",
            topic="Group 36 opened a conditional trace-anchor precondition inventory route",
            result="declaration, status, node-separation, hidden-load, incidence/residual, source/divergence, and downstream-gate preconditions were initialized",
            status="PRECONDITION_INVENTORY",
            boundary="opener filled no declarations, assigned no statuses, and adopted no Package B components",
        ),
        StatusEntry(
            name="G36-2: declaration precondition ledger",
            topic="declaration locks for trace normalization and safe membership were inventoried",
            result="B_s convention, zeta convention, d, scope, zeta_Bs, T_zeta, domain/codomain, criterion, role purity, diagnostic/active scope, node separation, and status mode are visible preconditions",
            status="DECLARATION_PRECONDITION",
            boundary="precondition visibility is not declaration filling",
        ),
        StatusEntry(
            name="G36-3: status precondition matrix",
            topic="component status modes and status-pair hazards were inventoried",
            result="compatible-if-declared, declared candidate, theorem target, adopted postulate, diagnostic-only, deferred, and mixed-status cases are separated",
            status="STATUS_PRECONDITION",
            boundary="status classification assigns no theory status",
        ),
        StatusEntry(
            name="G36-4: safety precondition ledger",
            topic="trace-anchor safety gates were inventoried",
            result="node separation, hidden-load exclusion, role purity, incidence/residual separation, source visibility, divergence explicitness, diagnostic inertness, and downstream locks are visible",
            status="SAFETY_PRECONDITION",
            boundary="safety gates are preconditions, not solved theorems",
        ),
        StatusEntry(
            name="G36-5: handoff condition ledger",
            topic="future route handoff conditions were separated",
            result="declaration, adoption, theorem, precondition, insertion, and parent routes remain distinct and conditionalized",
            status="HANDOFF_CONDITION",
            boundary="handoff clarity is not route choice",
        ),
        StatusEntry(
            name="G36-6: precondition obligations",
            topic="remaining Group 36 obligations were consolidated",
            result="declaration, status, safety, handoff, compatible-if-declared, postulate/theorem, adoption, and downstream obligations remain visible",
            status="PRECONDITION_OBLIGATION",
            boundary="obligation summary does not close those obligations",
        ),
        StatusEntry(
            name="G36-7: current Package B status",
            topic="trace-normalization and safe-membership surviving forms remain conditional",
            result="Group 33/34 surviving forms remain compatible-if-declared only",
            status="COMPATIBLE_IF_DECLARED",
            boundary="Package B is not selected, adopted, recommended, derived, declared, or insertable",
        ),
        StatusEntry(
            name="G36-8: downstream gates",
            topic="B_s/F_zeta insertion, active O, residual control, and parent closure",
            result="all downstream gates remain closed",
            status="NOT_READY",
            boundary="Group 36 is not insertion, residual control, active O, or parent readiness",
        ),
    ]


def build_gaps() -> list[GapEntry]:
    return [
        GapEntry(
            name="G1: declaration values",
            reason="B_s convention, zeta convention, traced dimension, scope, membership objects, criterion, role purity, and diagnostic/active scope remain unfilled",
            status="OPEN",
            discipline="blank slots remain blank until a separate declaration record fills them",
        ),
        GapEntry(
            name="G2: component status assignment",
            reason="P_trace_norm and P_safe_membership remain compatible-if-declared only unless later changed explicitly",
            status="OPEN",
            discipline="status preconditions are not status-change records",
        ),
        GapEntry(
            name="G3: mixed-status handling",
            reason="one Package B component may later change status before the other",
            status="OPEN",
            discipline="one component cannot license the other",
        ),
        GapEntry(
            name="G4: safety theorem support",
            reason="node separation, visibility, explicitness, incidence separation, and residual separation remain preconditions rather than full theorems",
            status="OPEN",
            discipline="safety gates must not be reported as solved source, divergence, incidence, or residual theorems",
        ),
        GapEntry(
            name="G5: Package B adoption",
            reason="Group 36 is an inventory route, not an adoption event",
            status="NOT_ADOPTED",
            discipline="explicit user/theory decision remains separate",
        ),
        GapEntry(
            name="G6: trace-anchor theorem support",
            reason="no theorem proves the trace-normalization or safe-membership component",
            status="NOT_DERIVED",
            discipline="theorem routes require separate scripts after declarations",
        ),
        GapEntry(
            name="G7: insertion and parent closure",
            reason="precondition clarity does not resolve recombination, residual, no-overlap, source/divergence, or parent gates",
            status="NOT_READY",
            discipline="Group 36 does not license insertion or parent equation",
        ),
    ]


def build_handoffs() -> list[HandoffEntry]:
    return [
        HandoffEntry(
            name="H1: explicit declaration record",
            reason="future work may fill concrete B_s, zeta, d, scope, membership criterion, role-purity, and status-mode declarations",
            status="OPEN",
            caution="declaration record is not adoption or proof",
        ),
        HandoffEntry(
            name="H2: explicit Package B adoption decision",
            reason="theory owner may later adopt one or both components deliberately",
            status="OPEN",
            caution="adopted postulates must not be called derived",
        ),
        HandoffEntry(
            name="H3: theorem route after declarations",
            reason="trace-normalization and safe-membership theorem attempts may proceed after declaration slots are filled",
            status="THEOREM_TARGET",
            caution="theorem target is not theorem proof",
        ),
        HandoffEntry(
            name="H4: conditional insertion-precondition inventory",
            reason="may organize later insertion prerequisites only under explicit declaration/status/safety assumptions",
            status="CONDITIONAL",
            caution="precondition inventory is not B_s/F_zeta insertion theorem",
        ),
        HandoffEntry(
            name="H5: B_s/F_zeta insertion theorem",
            reason="component status, incidence, residual, active O, source/divergence, and recombination gates remain unresolved",
            status="NOT_READY",
            caution="forbidden as immediate route from Group 36 alone",
        ),
        HandoffEntry(
            name="H6: parent field equation",
            reason="scalar recombination, residual control, no-overlap, source neutrality, divergence safety, and parent identity remain unresolved",
            status="NOT_READY",
            caution="parent gate remains closed",
        ),
    ]


def build_rules() -> list[RuleEntry]:
    return [
        RuleEntry(
            name="R1: precondition inventory as declaration record",
            upgrade="treat listed locks or obligations as filled declaration values",
            status="POLICY_RULE",
            reason="inventory names blanks; it does not fill them",
        ),
        RuleEntry(
            name="R2: status precondition as status assignment",
            upgrade="treat possible or required status modes as assigned theory status",
            status="POLICY_RULE",
            reason="status classification is not a status change",
        ),
        RuleEntry(
            name="R3: safety precondition as safety theorem",
            upgrade="treat visibility, explicitness, node separation, or role purity as completed theorems",
            status="POLICY_RULE",
            reason="safety gates remain preconditions unless independently derived",
        ),
        RuleEntry(
            name="R4: compatible-if-declared as selected",
            upgrade="shorten compatible-if-declared to selected, adopted, declared, derived, or insertable",
            status="POLICY_RULE",
            reason="conditional survival is weaker than choice, proof, declaration, or adoption",
        ),
        RuleEntry(
            name="R5: one-node licensing",
            upgrade="let one Package B component choose, prove, or license the other",
            status="POLICY_RULE",
            reason="trace normalization and safe membership remain separate candidate nodes",
        ),
        RuleEntry(
            name="R6: precondition clarity as insertion",
            upgrade="treat organized preconditions as B_s/F_zeta insertion",
            status="POLICY_RULE",
            reason="insertion remains downstream and not ready",
        ),
        RuleEntry(
            name="R7: precondition clarity as parent readiness",
            upgrade="open parent equation from trace-anchor precondition clarity",
            status="POLICY_RULE",
            reason="parent gate remains closed",
        ),
    ]


def build_obligations() -> list[ObligationEntry]:
    return [
        ObligationEntry(
            name="O1: preserve declaration precondition boundary",
            obligation="keep declaration slots visible but unfilled unless a separate declaration record fills them",
            status="OPEN",
            blocks="hidden declaration use",
            discipline="precondition inventory is not a declaration record",
        ),
        ObligationEntry(
            name="O2: preserve status precondition boundary",
            obligation="keep component statuses explicit and separate before any future use",
            status="OPEN",
            blocks="ambiguous Package B status",
            discipline="status preconditions are not status assignments",
        ),
        ObligationEntry(
            name="O3: preserve mixed-status discipline",
            obligation="carry mixed Package B component statuses visibly if they arise",
            status="OPEN",
            blocks="one-node licensing",
            discipline="one component status cannot license the other",
        ),
        ObligationEntry(
            name="O4: preserve safety gates",
            obligation="carry node separation, hidden-load exclusion, incidence/residual separation, source/divergence visibility, diagnostic inertness, and downstream locks forward",
            status="OPEN",
            blocks="trace-anchor smuggling",
            discipline="safety gates are not solved theorems",
        ),
        ObligationEntry(
            name="O5: preserve compatible-if-declared status",
            obligation="record Group 33/34 surviving forms as compatible-if-declared only unless later changed explicitly",
            status="OPEN",
            blocks="selection drift",
            discipline="do not shorten to selected, declared, adopted, derived, or insertable",
        ),
        ObligationEntry(
            name="O6: preserve postulate/theorem boundary",
            obligation="do not call adopted postulates derived and do not call theorem targets proved",
            status="OPEN",
            blocks="governance drift",
            discipline="choice and proof remain separate",
        ),
        ObligationEntry(
            name="O7: adoption remains separate",
            obligation="keep Package B and both components unadopted unless a separate explicit decision is made",
            status="OPEN",
            blocks="accidental adoption",
            discipline="Group 36 adopts nothing",
        ),
        ObligationEntry(
            name="O8: downstream gates remain closed",
            obligation="keep B_s/F_zeta insertion, active O, residual control, and parent closure closed",
            status="NOT_READY",
            blocks="downstream overreach",
            discipline="Group 36 is not insertion or parent readiness",
        ),
    ]


def build_conclusions() -> list[ConclusionEntry]:
    return [
        ConclusionEntry(
            name="C1: Group 36 result",
            conclusion="Group 36 completed a conditional trace-anchor precondition inventory",
            status="PRECONDITION_INVENTORY",
            meaning="precondition classes, declaration locks, status locks, safety gates, handoff conditions, and obligations are visible",
        ),
        ConclusionEntry(
            name="C2: current Package B component status",
            conclusion="trace-normalization and safe-membership surviving forms remain compatible-if-declared only",
            status="COMPATIBLE_IF_DECLARED",
            meaning="neither component is selected, declared, adopted, derived, or insertable",
        ),
        ConclusionEntry(
            name="C3: declarations remain blank",
            conclusion="Group 36 fills no declaration slots",
            status="NOT_CHOSEN",
            meaning="precondition inventory is not declaration record",
        ),
        ConclusionEntry(
            name="C4: status remains unassigned",
            conclusion="Group 36 assigns no Package B component status as theory state",
            status="NOT_ASSIGNED",
            meaning="status modes are preconditions, not applied states",
        ),
        ConclusionEntry(
            name="C5: no adoption or recommendation",
            conclusion="Group 36 adopts no Package B component and recommends no Package B adoption",
            status="NOT_ADOPTED",
            meaning="explicit decision remains separate",
        ),
        ConclusionEntry(
            name="C6: downstream gates",
            conclusion="B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready",
            status="NOT_READY",
            meaning="precondition clarity does not close recombination or parent gates",
        ),
    ]


# ----------------------------------------------------------------------------------------------------------------------
# Cases
# ----------------------------------------------------------------------------------------------------------------------


def case_0_problem() -> None:
    header("Case 0: Group 36 status summary problem")
    print(
        "Question:\n\n"
        "  What did Group 36 establish about the preconditions needed before Package B\n"
        "  components can be used, and what remains open before declaration, adoption,\n"
        "  theorem, precondition, insertion, or parent routes?\n\n"
        "Discipline:\n\n"
        "  This script summarizes Group 36.\n"
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
        "  Count the locks. Close the inventory. Do not open the door."
    )
    out_line(
        "governance_assessments",
        "PASS",
        "Group 36 status summary opened",
        "closing conditional trace-anchor precondition inventory while preserving no-choice/no-adoption boundary",
    )


def case_1_symbolic_summary() -> SummarySymbols:
    header("Case 1: Group 36 symbolic summary loads")

    names = [
        "P_trace_norm",
        "P_safe_membership",
        "declaration_pc",
        "status_pc",
        "safety_pc",
        "handoff_pc",
        "mixed_status",
        "node_separation",
        "hidden_payload_gate",
        "incidence_gate",
        "residual_gate",
        "source_visibility",
        "div_visibility",
        "diagnostic_inertness",
        "adoption_boundary",
        "P_insertion",
        "P_active_O",
        "P_residual_kill",
        "P_parent",
    ]
    symbols = {name: sp.Symbol(name) for name in names}

    print("Summary symbols:")
    for name in names:
        print(f"  {name} = {symbols[name]}")

    L_declaration = symbols["declaration_pc"]
    L_status = sp.simplify(symbols["status_pc"] + symbols["mixed_status"])
    L_safety = sp.simplify(
        symbols["safety_pc"]
        + symbols["node_separation"]
        + symbols["hidden_payload_gate"]
        + symbols["incidence_gate"]
        + symbols["residual_gate"]
        + symbols["source_visibility"]
        + symbols["div_visibility"]
        + symbols["diagnostic_inertness"]
    )
    L_handoff = symbols["handoff_pc"]
    L_downstream_closed = sp.simplify(
        symbols["P_insertion"] + symbols["P_active_O"] + symbols["P_residual_kill"] + symbols["P_parent"]
    )
    L_group36_summary = sp.simplify(
        symbols["P_trace_norm"]
        + symbols["P_safe_membership"]
        + L_declaration
        + L_status
        + L_safety
        + L_handoff
        + symbols["adoption_boundary"]
        + L_downstream_closed
    )

    print()
    print(f"Declaration precondition load:\n  L_declaration = {L_declaration}")
    print(f"Status precondition load:\n  L_status = {L_status}")
    print(f"Safety precondition load:\n  L_safety = {L_safety}")
    print(f"Handoff precondition load:\n  L_handoff = {L_handoff}")
    print(f"Downstream closed load:\n  L_downstream_closed = {L_downstream_closed}")
    print(f"Group 36 summary load:\n  L_group36_summary = {L_group36_summary}")

    out_line(
        "derived_results",
        "PASS",
        "Group 36 symbolic summary loads stated",
        f"L_safety={L_safety}; L_downstream_closed={L_downstream_closed}",
    )

    return SummarySymbols(
        L_declaration=L_declaration,
        L_status=L_status,
        L_safety=L_safety,
        L_handoff=L_handoff,
        L_downstream_closed=L_downstream_closed,
        L_group36_summary=L_group36_summary,
    )


def case_2_status_entries(entries: Iterable[StatusEntry]) -> None:
    header("Case 2: Group 36 status entries")
    for item in entries:
        subheader(item.name)
        print(f"Topic: {item.topic}")
        out_line("governance_assessments", item.status, item.name, "")
        print(f"Result: {item.result}")
        print(f"Boundary: {item.boundary}")
    out_line("governance_assessments", "INFO", "Group 36 status entries stated", "8 status entries stated")


def case_3_final_gaps(gaps: Iterable[GapEntry]) -> None:
    header("Case 3: Final open gaps")
    for item in gaps:
        subheader(item.name)
        out_line("unresolved_obligations", item.status, item.name, "")
        print(f"Reason: {item.reason}")
        print(f"Discipline: {item.discipline}")
    out_line("unresolved_obligations", "PASS", "Group 36 final gaps stated", "7 gaps remain open or not ready")


def case_4_handoffs(handoffs: Iterable[HandoffEntry]) -> None:
    header("Case 4: Final handoffs")
    for item in handoffs:
        subheader(item.name)
        out_line("governance_assessments", item.status, item.name, "")
        print(f"Reason: {item.reason}")
        print(f"Caution: {item.caution}")
    out_line("governance_assessments", "DEFER", "Group 36 handoffs stated", "6 handoffs stated; adoption/insertion remain separate")


def case_5_rules(rules: Iterable[RuleEntry]) -> None:
    header("Case 5: Rejected summary upgrades")
    for item in rules:
        subheader(item.name)
        print(f"Upgrade: {item.upgrade}")
        out_line("governance_assessments", item.status, item.name, "")
        print(f"Reason: {item.reason}")
    out_line("governance_assessments", "PASS", "Group 36 summary upgrades rejected", "7 upgrade shortcuts rejected as policy rules")


def case_6_obligations(obligations: Iterable[ObligationEntry]) -> None:
    header("Case 6: Group 36 final obligations")
    for item in obligations:
        subheader(item.name)
        print(f"Obligation: {item.obligation}")
        out_line("unresolved_obligations", item.status, item.name, "")
        print(f"Blocks: {item.blocks}")
        print(f"Discipline: {item.discipline}")
    out_line("unresolved_obligations", "PASS", "Group 36 final obligations opened", "8 obligations stated")


def case_7_conclusions(conclusions: Iterable[ConclusionEntry]) -> None:
    header("Case 7: Group 36 conclusions")
    for item in conclusions:
        subheader(item.name)
        print(f"Conclusion: {item.conclusion}")
        out_line("governance_assessments", item.status, item.name, "")
        print(f"Meaning: {item.meaning}")
    out_line(
        "governance_assessments",
        "PASS",
        "Group 36 status summary conclusion stated",
        "conditional precondition inventory complete; no declarations filled, no status assigned, no adoption, downstream gates closed",
    )


def final_interpretation() -> None:
    header("Final interpretation")
    print(
        "Group 36 status summary result:\n\n"
        "  Group 36 completed a conditional trace-anchor precondition inventory.\n"
        "  Declaration preconditions are visible but unfilled.\n"
        "  Status preconditions are visible but unassigned.\n"
        "  Safety gates and handoff conditions are visible and open.\n"
        "  Trace-normalization and safe-membership surviving forms remain compatible-if-declared only.\n"
        "  No declaration value is filled.\n"
        "  No Package B component status is assigned as theory state.\n"
        "  No trace-normalization form is selected, adopted, or derived.\n"
        "  No safe-membership form is selected, adopted, or derived.\n"
        "  Package B is not adopted or recommended for adoption.\n"
        "  B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready.\n\n"
        "Possible next step:\n"
        "  explicit declaration record, explicit Package B adoption decision, theorem route after declarations,\n"
        "  or conditional insertion-precondition inventory\n\n"
        "Tiny goblin label:\n"
        "  Count the locks. Close the inventory. Do not open the door.\n"
    )
    out_line(
        "governance_assessments",
        "PASS",
        "candidate Group 36 status summary complete",
        "conditional precondition inventory closed as audit; adoption and downstream gates remain separate",
    )


# ----------------------------------------------------------------------------------------------------------------------
# Archive records
# ----------------------------------------------------------------------------------------------------------------------


def record_inventory_marker(ns, symbols: SummarySymbols) -> None:
    ns.record_derivation(
        derivation_id="g36_status_summary",
        inputs=[
            symbols.L_declaration,
            symbols.L_status,
            symbols.L_safety,
            symbols.L_handoff,
            symbols.L_downstream_closed,
        ],
        output=symbols.L_group36_summary,
        method="Group 36 conditional trace-anchor precondition inventory status summary",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="group_status_summary_marker",
        is_placeholder=True,
    )


def record_obligations(ns, obligations: Iterable[ObligationEntry]) -> None:
    for item in obligations:
        ident = safe_ident(item.name)
        status = ObligationStatus.OPEN if item.status != "NOT_READY" else ObligationStatus.DEFERRED
        ns.record_obligation(
            ProofObligationRecord(
                obligation_id=f"g36_sum_{ident}",
                script_id=SCRIPT_ID,
                title=item.name,
                status=status,
                required_by=[SCRIPT_ID],
                description=(
                    f"{item.obligation}. Blocks: {item.blocks}. Discipline: {item.discipline}."
                ),
            )
        )


def governance_status(status: str) -> GovernanceStatus:
    if status == "NOT_READY":
        return GovernanceStatus.DEFERRED_PENDING_PREREQUISITES
    if status == "NOT_ADOPTED":
        return GovernanceStatus.DEFERRED_PENDING_PREREQUISITES
    if status == "THEOREM_TARGET":
        return GovernanceStatus.CANDIDATE_ROUTE
    if status == "POLICY_RULE":
        return GovernanceStatus.POLICY_RULE
    return GovernanceStatus.POLICY_RULE


def record_governance(
    ns,
    status_entries: Iterable[StatusEntry],
    gaps: Iterable[GapEntry],
    handoffs: Iterable[HandoffEntry],
    rules: Iterable[RuleEntry],
) -> None:
    ns.record_route(
        RouteRecord(
            route_id="g36_summary",
            script_id=SCRIPT_ID,
            name="Group 36 conditional trace-anchor precondition inventory summary route",
            status=GovernanceStatus.CANDIDATE_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            required_obligations=[
                "g36_sum_o1",
                "g36_sum_o2",
                "g36_sum_o3",
                "g36_sum_o4",
                "g36_sum_o5",
                "g36_sum_o6",
                "g36_sum_o7",
                "g36_sum_o8",
            ],
            activation_conditions=[
                "Group 36 declaration, status, safety, handoff, and obligation ledgers complete",
                "summary is inventory-only",
                "no declaration values filled",
                "no Package B status assigned",
                "no Package B component adopted",
                "downstream gates closed",
            ],
        )
    )

    for item in status_entries:
        ident = safe_ident(item.name)
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g36_sum_s_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=governance_status(item.status),
                statement=(
                    f"{item.topic}. Result: {item.result}. Boundary: {item.boundary}."
                ),
                derivation_ids=["g36_status_summary"],
                obligation_ids=[],
            )
        )

    for item in gaps:
        ident = safe_ident(item.name)
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g36_sum_g_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=governance_status(item.status),
                statement=f"Open Group 36 gap: {item.reason}. Discipline: {item.discipline}.",
                derivation_ids=["g36_status_summary"],
                obligation_ids=[],
            )
        )

    for item in handoffs:
        ident = safe_ident(item.name)
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g36_sum_h_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=governance_status(item.status),
                statement=f"Handoff: {item.reason}. Caution: {item.caution}.",
                derivation_ids=["g36_status_summary"],
                obligation_ids=[],
            )
        )

    for item in rules:
        ident = safe_ident(item.name)
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g36_sum_r_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.POLICY_RULE,
                statement=f"Rejected summary upgrade: {item.upgrade}. Reason: {item.reason}.",
                derivation_ids=["g36_status_summary"],
                obligation_ids=[],
            )
        )


# ----------------------------------------------------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------------------------------------------------


def main() -> None:
    header("Candidate Group 36 Status Summary")
    archive, ns, invalidated = prepare_archive()
    ensure_archive_write_dirs(ns)
    print_archive_status(ns, invalidated)

    status_entries = build_status_entries()
    gaps = build_gaps()
    handoffs = build_handoffs()
    rules = build_rules()
    obligations = build_obligations()
    conclusions = build_conclusions()

    case_0_problem()
    symbols = case_1_symbolic_summary()
    case_2_status_entries(status_entries)
    case_3_final_gaps(gaps)
    case_4_handoffs(handoffs)
    case_5_rules(rules)
    case_6_obligations(obligations)
    case_7_conclusions(conclusions)
    final_interpretation()

    record_inventory_marker(ns, symbols)
    record_obligations(ns, obligations)
    record_governance(ns, status_entries, gaps, handoffs, rules)

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
