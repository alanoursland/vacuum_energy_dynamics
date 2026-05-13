# Candidate Trace Anchor Precondition Obligations
#
# Group:
#   36_conditional_trace_anchor_precondition_inventory
#
# Human title:
#   Trace Anchor Precondition Obligations
#
# Script type:
#   PRECONDITION OBLIGATION SUMMARY
#
# Purpose
# -------
# Summarize the remaining declaration, status, safety, and handoff obligations
# after the Group 36 declaration-precondition, status-precondition,
# safety-precondition, and handoff-condition ledgers.
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
#   Count the locks, tags, traps, and doors. Close the sack.

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
            "g36_handoff_pc",
            "36_conditional_trace_anchor_precondition_inventory__candidate_trace_anchor_handoff_condition_ledger",
            "g36_handoff_pc",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g36_safety_pc",
            "36_conditional_trace_anchor_precondition_inventory__candidate_trace_anchor_safety_precondition_ledger",
            "g36_safety_pc",
            RecordKind.INVENTORY_MARKER,
        ),
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
class ObligationSymbols:
    L_declaration_obligations: sp.Basic
    L_status_obligations: sp.Basic
    L_safety_obligations: sp.Basic
    L_handoff_obligations: sp.Basic
    L_downstream_closed: sp.Basic
    L_obligation_gap: sp.Basic


@dataclass
class ObligationEntry:
    name: str
    obligation: str
    status: str
    source: str
    blocks: str
    discipline: str


@dataclass
class HandoffEntry:
    name: str
    handoff: str
    status: str
    allowed_if: str
    blocked_if: str
    caution: str


@dataclass
class InvalidUpgrade:
    name: str
    shortcut: str
    status: str
    reason: str
    failure_mode: str


@dataclass
class RuleEntry:
    name: str
    rule: str
    status: str
    reason: str


@dataclass
class ConclusionEntry:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_obligations() -> list[ObligationEntry]:
    return [
        ObligationEntry(
            name="O1: declaration preconditions remain open",
            obligation="keep B_s convention, zeta convention, traced dimension, scope, zeta_Bs object, T_zeta sector, domain/codomain, criterion, role purity, diagnostic/active scope, and status mode explicit before use",
            status="OPEN",
            source="declaration precondition ledger",
            blocks="hidden declaration use",
            discipline="blank slots remain blank until a separate declaration record fills them",
        ),
        ObligationEntry(
            name="O2: status preconditions remain open",
            obligation="state P_trace_norm and P_safe_membership status modes separately before theorem, adoption, declaration, or precondition handoff",
            status="OPEN",
            source="status precondition matrix",
            blocks="ambiguous Package B status",
            discipline="current surviving forms remain compatible-if-declared unless explicitly changed",
        ),
        ObligationEntry(
            name="O3: mixed-status visibility remains required",
            obligation="carry mixed component status visibly if one Package B node changes before the other",
            status="OPEN",
            source="status precondition matrix and handoff condition ledger",
            blocks="one-node licensing and Package B overclaim",
            discipline="one component's status cannot license the other",
        ),
        ObligationEntry(
            name="O4: safety preconditions remain open",
            obligation="preserve node separation, hidden-load exclusion, role purity, incidence/residual separation, source visibility, divergence explicitness, diagnostic inertness, and downstream locks",
            status="OPEN",
            source="safety precondition ledger",
            blocks="smuggling through trace-anchor components",
            discipline="safety gates are preconditions, not solved theorems",
        ),
        ObligationEntry(
            name="O5: handoff conditions remain open",
            obligation="require every future handoff to state route kind, declaration assumptions, component statuses, mixed status, safety imports, and downstream lock status",
            status="OPEN",
            source="handoff condition ledger",
            blocks="route drift and hidden assumptions",
            discipline="handoff taxonomy is not route selection",
        ),
        ObligationEntry(
            name="O6: compatible-if-declared boundary remains current",
            obligation="record Group 33/34 surviving forms as compatible-if-declared only unless later changed explicitly",
            status="OPEN",
            source="Groups 33-36",
            blocks="selection, adoption, derivation, declaration, and insertion drift",
            discipline="compatible-if-declared is conditional audit status only",
        ),
        ObligationEntry(
            name="O7: postulate theorem boundary remains required",
            obligation="do not call adopted postulates derived and do not call theorem targets proved",
            status="OPEN",
            source="status and handoff ledgers",
            blocks="governance drift",
            discipline="choice and proof remain separate",
        ),
        ObligationEntry(
            name="O8: adoption boundary remains required",
            obligation="do not adopt Package B or either component in Group 36",
            status="REQUIRED",
            source="Group 36 discipline",
            blocks="accidental adoption",
            discipline="adoption requires a separate explicit user/theory decision record",
        ),
        ObligationEntry(
            name="O9: downstream gates remain closed",
            obligation="keep B_s/F_zeta insertion, active O, residual control, and parent closure closed",
            status="NOT_READY",
            source="Group 36 downstream locks",
            blocks="downstream overreach",
            discipline="precondition obligations are not insertion or parent readiness",
        ),
    ]


def build_handoffs() -> list[HandoffEntry]:
    return [
        HandoffEntry(
            name="H1: Group 36 status summary",
            handoff="candidate_group_36_status_summary.py",
            status="HANDOFF_READY",
            allowed_if="summary closes Group 36 as conditional precondition inventory only",
            blocked_if="summary fills declarations, assigns statuses, adopts Package B, or opens downstream gates",
            caution="summary is ready but must remain an inventory summary",
        ),
        HandoffEntry(
            name="H2: explicit declaration record",
            handoff="future record filling declaration values",
            status="CONDITIONAL",
            allowed_if="theory owner supplies concrete B_s, zeta, d, scope, membership, role-purity, and status-mode declarations",
            blocked_if="declarations are inferred from compatibility, recovery, insertion, or parent fit",
            caution="declaration record is not adoption or theorem proof",
        ),
        HandoffEntry(
            name="H3: explicit Package B adoption decision",
            handoff="separate explicit user/theory decision record",
            status="CONDITIONAL",
            allowed_if="decision names exactly which Package B components are adopted",
            blocked_if="adoption is inferred from audit survival or declaration clarity",
            caution="adopted postulates must not be called derived",
        ),
        HandoffEntry(
            name="H4: theorem route after declarations",
            handoff="trace-normalization and/or safe-membership theorem attempt after declarations",
            status="THEOREM_TARGET",
            allowed_if="declarations, assumptions, and proof obligations are explicit",
            blocked_if="theorem target status is treated as proof",
            caution="proof requires separate scripts",
        ),
        HandoffEntry(
            name="H5: conditional insertion-precondition inventory",
            handoff="insertion-facing precondition inventory under explicit assumptions",
            status="CONDITIONAL",
            allowed_if="declaration/status assumptions are explicit and route is labeled conditional",
            blocked_if="precondition inventory is treated as insertion theorem",
            caution="may organize prerequisites but cannot insert B_s/F_zeta",
        ),
        HandoffEntry(
            name="H6: B_s/F_zeta insertion theorem",
            handoff="downstream scalar trace insertion theorem",
            status="NOT_READY",
            allowed_if="not available from Group 36 alone",
            blocked_if="incidence, residual, active O, source/divergence, recombination, or component-status gates remain unresolved",
            caution="forbidden as immediate route",
        ),
        HandoffEntry(
            name="H7: parent field equation",
            handoff="parent closure route",
            status="NOT_READY",
            allowed_if="not available from Group 36 alone",
            blocked_if="scalar recombination, residual control, no-overlap, source neutrality, divergence safety, and parent identity remain unresolved",
            caution="parent gate remains closed",
        ),
    ]


def build_invalid_upgrades() -> list[InvalidUpgrade]:
    return [
        InvalidUpgrade(
            name="X1: obligation summary as declaration record",
            shortcut="treat summarized declaration obligations as filled declaration values",
            status="FORBIDDEN_SHORTCUT",
            reason="obligations name what remains required; they do not fill blanks",
            failure_mode="hidden declarations enter later work",
        ),
        InvalidUpgrade(
            name="X2: obligation summary as status assignment",
            shortcut="treat status obligations as assigned Package B component status",
            status="FORBIDDEN_SHORTCUT",
            reason="status preconditions are weaker than status-change records",
            failure_mode="compatible-if-declared becomes selected, declared, adopted, or derived",
        ),
        InvalidUpgrade(
            name="X3: safety obligations as solved safety theorems",
            shortcut="treat node separation, hidden-load exclusion, source visibility, or divergence explicitness as completed theorems",
            status="FORBIDDEN_SHORTCUT",
            reason="safety gates remain preconditions and obligations",
            failure_mode="source, divergence, incidence, or residual burdens disappear by summary",
        ),
        InvalidUpgrade(
            name="X4: obligation summary as adoption",
            shortcut="treat Package B obligations as adoption of one or both components",
            status="FORBIDDEN_SHORTCUT",
            reason="adoption requires a separate explicit decision",
            failure_mode="audit obligation becomes theory choice",
        ),
        InvalidUpgrade(
            name="X5: obligation summary as theorem proof",
            shortcut="treat precondition clarity as proof of trace normalization or safe membership",
            status="FORBIDDEN_SHORTCUT",
            reason="theorem proof requires separate derivation scripts",
            failure_mode="open theorem burden disappears by bookkeeping",
        ),
        InvalidUpgrade(
            name="X6: obligation summary as insertion",
            shortcut="treat organized preconditions as B_s/F_zeta insertion or insertion readiness",
            status="FORBIDDEN_SHORTCUT",
            reason="insertion remains downstream and not ready",
            failure_mode="locks list becomes door opening",
        ),
        InvalidUpgrade(
            name="X7: obligation summary as parent readiness",
            shortcut="open the parent field equation from Group 36 obligation clarity",
            status="FORBIDDEN_SHORTCUT",
            reason="parent closure remains blocked by recombination and safety gates",
            failure_mode="parent gate opens prematurely",
        ),
    ]


def build_rules() -> list[RuleEntry]:
    return [
        RuleEntry(
            name="R1: obligations are not choices",
            rule="Precondition obligations must not fill declaration slots or assign component statuses.",
            status="POLICY_RULE",
            reason="Group 36 is an inventory route, not a declaration or status-change route",
        ),
        RuleEntry(
            name="R2: obligations are not adoption",
            rule="No Package B component is adopted by obligation summary.",
            status="POLICY_RULE",
            reason="adoption requires a separate explicit decision record",
        ),
        RuleEntry(
            name="R3: obligations are not theorem proof",
            rule="Theorem routes remain open until separate derivation scripts prove them.",
            status="POLICY_RULE",
            reason="theorem targets and proof obligations are not proofs",
        ),
        RuleEntry(
            name="R4: safety obligations are not safety theorems",
            rule="Safety gates remain preconditions unless independently derived.",
            status="POLICY_RULE",
            reason="visibility, explicitness, and separation are weaker than source, divergence, incidence, or residual theorems",
        ),
        RuleEntry(
            name="R5: obligations are not downstream licenses",
            rule="Precondition obligations do not license insertion, active O, residual control, or parent closure.",
            status="POLICY_RULE",
            reason="downstream gates require separate theorem or adoption/precondition status",
        ),
    ]


def build_conclusions() -> list[ConclusionEntry]:
    return [
        ConclusionEntry(
            name="C1: obligations summarized",
            conclusion="declaration, status, safety, handoff, adoption, and downstream obligations are visible",
            status="PRECONDITION_REQUIRED",
            meaning="Group 36 can close as a conditional precondition inventory",
        ),
        ConclusionEntry(
            name="C2: current status preserved",
            conclusion="trace-normalization and safe-membership surviving forms remain compatible-if-declared only",
            status="COMPATIBLE_IF_DECLARED",
            meaning="current audit status is not selected, declared, adopted, derived, or insertable",
        ),
        ConclusionEntry(
            name="C3: no choices made",
            conclusion="this obligation summary fills no declaration slots and assigns no component status",
            status="NOT_CHOSEN",
            meaning="obligation summary is not declaration record or status-change record",
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
            meaning="precondition obligations do not open field-equation gates",
        ),
        ConclusionEntry(
            name="C6: next",
            conclusion="Group 36 status summary should run next",
            status="OPEN",
            meaning="summarize Group 36 without changing any theory status",
        ),
    ]


def case_0_problem() -> None:
    header("Case 0: Precondition obligations problem")
    print(
        "Question:\n\n"
        "  What declaration, status, safety, and handoff obligations remain after\n"
        "  the Group 36 precondition ledgers, and what can be safely handed to\n"
        "  the Group 36 status summary without filling declarations, assigning\n"
        "  statuses, adopting Package B, or opening downstream gates?\n\n"
        "Discipline:\n\n"
        "  This script summarizes precondition obligations.\n"
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
        "  Count the locks, tags, traps, and doors. Close the sack."
    )
    out_line(
        "governance_assessments",
        "PASS",
        "precondition obligations summary opened",
        "summarizing remaining Group 36 obligations only; no choices made",
    )


def case_1_symbolic_ledger() -> ObligationSymbols:
    header("Case 1: Precondition-obligation symbolic ledger")

    names = [
        "declaration_pc",
        "status_pc",
        "mixed_status_pc",
        "safety_pc",
        "handoff_pc",
        "compatible_boundary",
        "postulate_theorem_boundary",
        "adoption_boundary",
        "downstream_lock",
        "hidden_declaration",
        "hidden_status",
        "hidden_payload",
        "route_drift",
        "P_insertion",
        "P_active_O",
        "P_residual_kill",
        "P_parent",
    ]
    symbols = {name: sp.Symbol(name) for name in names}

    print("Obligation symbols:")
    for name in names:
        print(f"  {name} = {symbols[name]}")

    L_declaration_obligations = sp.simplify(symbols["declaration_pc"] + symbols["hidden_declaration"])
    L_status_obligations = sp.simplify(symbols["status_pc"] + symbols["mixed_status_pc"] + symbols["hidden_status"])
    L_safety_obligations = sp.simplify(symbols["safety_pc"] + symbols["hidden_payload"])
    L_handoff_obligations = sp.simplify(symbols["handoff_pc"] + symbols["route_drift"])
    L_downstream_closed = sp.simplify(
        symbols["P_insertion"] + symbols["P_active_O"] + symbols["P_residual_kill"] + symbols["P_parent"]
    )
    L_obligation_gap = sp.simplify(
        L_declaration_obligations
        + L_status_obligations
        + L_safety_obligations
        + L_handoff_obligations
        + symbols["compatible_boundary"]
        + symbols["postulate_theorem_boundary"]
        + symbols["adoption_boundary"]
        + L_downstream_closed
    )

    print()
    print(f"Declaration obligation load:\n  L_declaration_obligations = {L_declaration_obligations}")
    print(f"Status obligation load:\n  L_status_obligations = {L_status_obligations}")
    print(f"Safety obligation load:\n  L_safety_obligations = {L_safety_obligations}")
    print(f"Handoff obligation load:\n  L_handoff_obligations = {L_handoff_obligations}")
    print(f"Downstream closed load:\n  L_downstream_closed = {L_downstream_closed}")
    print(f"Precondition-obligation gap:\n  L_obligation_gap = {L_obligation_gap}")

    out_line(
        "derived_results",
        "PASS",
        "precondition-obligation symbolic loads stated",
        f"L_handoff_obligations={L_handoff_obligations}; L_downstream_closed={L_downstream_closed}",
    )

    return ObligationSymbols(
        L_declaration_obligations=L_declaration_obligations,
        L_status_obligations=L_status_obligations,
        L_safety_obligations=L_safety_obligations,
        L_handoff_obligations=L_handoff_obligations,
        L_downstream_closed=L_downstream_closed,
        L_obligation_gap=L_obligation_gap,
    )


def case_2_obligations(obligations: Iterable[ObligationEntry]) -> None:
    header("Case 2: Consolidated precondition obligations")
    for item in obligations:
        subheader(item.name)
        print(f"Obligation: {item.obligation}")
        out_line("unresolved_obligations", item.status, item.name, "")
        print(f"Source: {item.source}")
        print(f"Blocks: {item.blocks}")
        print(f"Discipline: {item.discipline}")
    out_line("unresolved_obligations", "PASS", "precondition obligations consolidated", "9 obligations stated")


def case_3_handoffs(handoffs: Iterable[HandoffEntry]) -> None:
    header("Case 3: Safe handoff options")
    for item in handoffs:
        subheader(item.name)
        print(f"Handoff: {item.handoff}")
        out_line("governance_assessments", item.status, item.name, "")
        print(f"Allowed if: {item.allowed_if}")
        print(f"Blocked if: {item.blocked_if}")
        print(f"Caution: {item.caution}")
    out_line("governance_assessments", "INFO", "safe handoff options summarized", "status summary ready; other routes conditional or not ready")


def case_4_invalid_upgrades(invalids: Iterable[InvalidUpgrade]) -> None:
    header("Case 4: Invalid obligation-summary upgrades")
    for item in invalids:
        subheader(item.name)
        print(f"Shortcut: {item.shortcut}")
        out_line("counterexamples", item.status, item.name, "")
        print(f"Reason: {item.reason}")
        print(f"Failure mode: {item.failure_mode}")
    out_line("counterexamples", "FAIL", "invalid obligation-summary upgrades rejected", "7 shortcuts rejected")


def case_5_rules(rules: Iterable[RuleEntry]) -> None:
    header("Case 5: Precondition-obligation no-overclaim rules")
    for item in rules:
        subheader(item.name)
        print(f"Rule: {item.rule}")
        out_line("governance_assessments", item.status, item.name, "")
        print(f"Reason: {item.reason}")
    out_line("governance_assessments", "PASS", "precondition-obligation no-overclaim rules stated", "5 rules stated")


def case_6_conclusions(conclusions: Iterable[ConclusionEntry]) -> None:
    header("Case 6: Precondition-obligation conclusions")
    for item in conclusions:
        subheader(item.name)
        print(f"Conclusion: {item.conclusion}")
        out_line("governance_assessments", item.status, item.name, "")
        print(f"Meaning: {item.meaning}")
    out_line(
        "governance_assessments",
        "PASS",
        "precondition obligations conclusion stated",
        "obligations summarized; no choices made, no adoption, downstream gates closed",
    )


def final_interpretation() -> None:
    header("Final interpretation")
    print(
        "Trace-anchor precondition obligations result:\n\n"
        "  Group 36 precondition obligations are now consolidated.\n"
        "  Declaration, status, safety, and handoff obligations remain visible and open.\n"
        "  Trace-normalization and safe-membership surviving forms remain compatible-if-declared only.\n"
        "  Blank declarations remain blank.\n"
        "  No Package B component status is assigned as theory state.\n"
        "  No trace-normalization or safe-membership form is selected, adopted, or derived.\n"
        "  Package B is not recommended for adoption.\n"
        "  Group 36 status summary is ready as an inventory summary only.\n"
        "  Explicit declaration, adoption, theorem, and insertion-facing routes remain conditional or not ready.\n"
        "  B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready.\n\n"
        "Possible next script:\n"
        "  candidate_group_36_status_summary.py\n\n"
        "Tiny goblin label:\n"
        "  Count the locks, tags, traps, and doors. Close the sack.\n"
    )
    out_line(
        "governance_assessments",
        "PASS",
        "trace-anchor precondition obligations complete",
        "Group 36 status summary should run next; adoption and downstream gates remain closed",
    )


# ----------------------------------------------------------------------------------------------------------------------
# Archive records
# ----------------------------------------------------------------------------------------------------------------------


def record_inventory_marker(ns, symbolic: ObligationSymbols) -> None:
    ns.record_derivation(
        derivation_id="g36_pc_obligations",
        inputs=[
            symbolic.L_declaration_obligations,
            symbolic.L_status_obligations,
            symbolic.L_safety_obligations,
            symbolic.L_handoff_obligations,
            symbolic.L_downstream_closed,
        ],
        output=symbolic.L_obligation_gap,
        method="Group 36 trace-anchor precondition obligations summary",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="precondition_obligations_marker",
        is_placeholder=True,
    )


def record_obligations(ns, obligations: Iterable[ObligationEntry]) -> None:
    for item in obligations:
        ident = safe_ident(item.name)
        status = ObligationStatus.OPEN if item.status != "NOT_READY" else ObligationStatus.DEFERRED
        ns.record_obligation(
            ProofObligationRecord(
                obligation_id=f"g36_pc_{ident}",
                script_id=SCRIPT_ID,
                title=item.name,
                status=status,
                required_by=[SCRIPT_ID],
                description=(
                    f"{item.obligation}. Source: {item.source}. Blocks: {item.blocks}. "
                    f"Discipline: {item.discipline}."
                ),
            )
        )


def record_governance(
    ns,
    obligations: Iterable[ObligationEntry],
    handoffs: Iterable[HandoffEntry],
    invalids: Iterable[InvalidUpgrade],
    rules: Iterable[RuleEntry],
) -> None:
    ns.record_route(
        RouteRecord(
            route_id="g36_pc_obl",
            script_id=SCRIPT_ID,
            name="Trace-anchor precondition obligations summary route",
            status=GovernanceStatus.CANDIDATE_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            required_obligations=[
                "g36_pc_o1",
                "g36_pc_o2",
                "g36_pc_o3",
                "g36_pc_o4",
                "g36_pc_o5",
                "g36_pc_o6",
                "g36_pc_o7",
                "g36_pc_o8",
                "g36_pc_o9",
            ],
            activation_conditions=[
                "Group 36 handoff condition ledger complete",
                "precondition obligations summarized only",
                "no route chosen",
                "no declaration values filled",
                "no component status assigned",
                "no Package B component adopted",
                "downstream gates closed",
            ],
        )
    )

    for item in obligations:
        ident = safe_ident(item.name)
        status = GovernanceStatus.POLICY_RULE
        if item.status == "NOT_READY":
            status = GovernanceStatus.DEFERRED_PENDING_PREREQUISITES
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g36_pc_ob_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=status,
                statement=(
                    f"Precondition obligation: {item.obligation}. Source: {item.source}. "
                    f"Blocks: {item.blocks}. Discipline: {item.discipline}."
                ),
                derivation_ids=["g36_pc_obligations"],
                obligation_ids=[f"g36_pc_{ident}"],
            )
        )

    for item in handoffs:
        ident = safe_ident(item.name)
        status = GovernanceStatus.CANDIDATE_ROUTE
        if item.status == "NOT_READY":
            status = GovernanceStatus.DEFERRED_PENDING_PREREQUISITES
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g36_pc_h_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=status,
                statement=(
                    f"Handoff option: {item.handoff}. Allowed if: {item.allowed_if}. "
                    f"Blocked if: {item.blocked_if}. Caution: {item.caution}."
                ),
                derivation_ids=["g36_pc_obligations"],
                obligation_ids=[],
            )
        )

    for item in invalids:
        ident = safe_ident(item.name)
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g36_pc_x_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.REJECTED_ROUTE,
                statement=(
                    f"Forbidden obligation-summary shortcut: {item.shortcut}. "
                    f"Reason: {item.reason}. Failure mode: {item.failure_mode}."
                ),
                derivation_ids=["g36_pc_obligations"],
                obligation_ids=[],
            )
        )

    for item in rules:
        ident = safe_ident(item.name)
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g36_pc_r_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.POLICY_RULE,
                statement=f"{item.rule} Reason: {item.reason}.",
                derivation_ids=["g36_pc_obligations"],
                obligation_ids=[],
            )
        )


# ----------------------------------------------------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------------------------------------------------


def main() -> None:
    header("Candidate Trace Anchor Precondition Obligations")
    archive, ns, invalidated = prepare_archive()
    ensure_archive_write_dirs(ns)
    print_archive_status(ns, invalidated)

    obligations = build_obligations()
    handoffs = build_handoffs()
    invalids = build_invalid_upgrades()
    rules = build_rules()
    conclusions = build_conclusions()

    case_0_problem()
    symbolic = case_1_symbolic_ledger()
    case_2_obligations(obligations)
    case_3_handoffs(handoffs)
    case_4_invalid_upgrades(invalids)
    case_5_rules(rules)
    case_6_conclusions(conclusions)
    final_interpretation()

    record_inventory_marker(ns, symbolic)
    record_obligations(ns, obligations)
    record_governance(ns, obligations, handoffs, invalids, rules)

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
