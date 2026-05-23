# Candidate Trace Anchor Status Mode Sieve
#
# Group:
#   35_trace_anchor_joint_declaration_inventory
#
# Human title:
#   Trace Anchor Joint Declaration Inventory
#
# Script type:
#   STATUS-MODE SIEVE / GOVERNANCE LEDGER
#
# Purpose
# -------
# Classify the possible status modes for the two Package B components after
# the joint consistency matrix:
#
#   P_trace_norm
#   P_safe_membership
#
# The script distinguishes compatible-if-declared, declared candidate,
# theorem target, explicit adopted postulate, diagnostic-only/inert,
# deferred/not-ready, and mixed component status.
#
# It does not assign any status mode as the theory state.
# It does not adopt Package B or either component.
# It does not choose declaration values.
# It does not derive a coefficient law or insertion.
# It keeps active O, residual control, and parent closure closed.
#
# Tiny goblin rule:
#
#   Sort the tags before hanging them on the cups.

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
        "ADOPTION_REQUIRES_DECISION": StatusMark.DEFER,
        "CONDITIONAL": StatusMark.DEFER,
        "COMPATIBLE_IF_DECLARED": StatusMark.INFO,
        "DECLARED_CANDIDATE": StatusMark.INFO,
        "DEFERRED": StatusMark.DEFER,
        "DIAGNOSTIC_ONLY": StatusMark.INFO,
        "FORBIDDEN_STATUS_UPGRADE": StatusMark.FAIL,
        "INVALID_STATUS": StatusMark.FAIL,
        "MIXED_STATUS_VISIBLE": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_CHOSEN": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REQUIRED": StatusMark.OBLIGATION,
        "STATUS_MODE": StatusMark.INFO,
        "STATUS_MODE_SIEVE": StatusMark.INFO,
        "THEOREM_TARGET": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
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
            "g35_problem",
            "035_trace_anchor_joint_declaration_inventory__candidate_trace_anchor_joint_declaration_problem",
            "g35_trace_anchor_joint_declaration_problem",
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
    P_trace_norm: sp.Symbol
    P_safe_membership: sp.Symbol
    compatible_if_declared: sp.Symbol
    declared_candidate: sp.Symbol
    theorem_target: sp.Symbol
    adopted_postulate: sp.Symbol
    diagnostic_only: sp.Symbol
    deferred_status: sp.Symbol
    mixed_status: sp.Symbol
    hidden_status: sp.Symbol
    status_drift: sp.Symbol
    P_insertion: sp.Symbol
    P_active_O: sp.Symbol
    P_residual_kill: sp.Symbol
    P_parent: sp.Symbol
    L_component_status_modes: sp.Basic
    L_mixed_status_modes: sp.Basic
    L_invalid_status_modes: sp.Basic
    L_downstream_closed: sp.Basic
    L_status_sieve_gap: sp.Basic


@dataclass
class StatusMode:
    name: str
    mode: str
    status: str
    allowed_meaning: str
    forbidden_meaning: str
    consequence: str


@dataclass
class StatusPair:
    name: str
    pair: str
    status: str
    coherent_if: str
    fails_if: str
    boundary: str


@dataclass
class InvalidStatus:
    name: str
    shortcut: str
    status: str
    reason: str
    failure_mode: str


@dataclass
class SieveRule:
    name: str
    rule: str
    status: str
    reason: str


@dataclass
class SieveObligation:
    name: str
    obligation: str
    status: str
    blocks: str
    discipline: str


@dataclass
class SieveConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_symbols() -> StatusSymbols:
    P_trace_norm = sp.Symbol("P_trace_norm")
    P_safe_membership = sp.Symbol("P_safe_membership")
    compatible_if_declared = sp.Symbol("compatible_if_declared")
    declared_candidate = sp.Symbol("declared_candidate")
    theorem_target = sp.Symbol("theorem_target")
    adopted_postulate = sp.Symbol("adopted_postulate")
    diagnostic_only = sp.Symbol("diagnostic_only")
    deferred_status = sp.Symbol("deferred_status")
    mixed_status = sp.Symbol("mixed_status")
    hidden_status = sp.Symbol("hidden_status")
    status_drift = sp.Symbol("status_drift")
    P_insertion = sp.Symbol("P_insertion")
    P_active_O = sp.Symbol("P_active_O")
    P_residual_kill = sp.Symbol("P_residual_kill")
    P_parent = sp.Symbol("P_parent")

    L_component_status_modes = sp.simplify(
        compatible_if_declared
        + declared_candidate
        + theorem_target
        + adopted_postulate
        + diagnostic_only
        + deferred_status
    )
    L_mixed_status_modes = sp.simplify(mixed_status)
    L_invalid_status_modes = sp.simplify(hidden_status + status_drift)
    L_downstream_closed = sp.simplify(P_active_O + P_insertion + P_parent + P_residual_kill)
    L_status_sieve_gap = sp.simplify(
        P_trace_norm
        + P_safe_membership
        + L_component_status_modes
        + L_mixed_status_modes
        + L_invalid_status_modes
        + L_downstream_closed
    )

    return StatusSymbols(
        P_trace_norm=P_trace_norm,
        P_safe_membership=P_safe_membership,
        compatible_if_declared=compatible_if_declared,
        declared_candidate=declared_candidate,
        theorem_target=theorem_target,
        adopted_postulate=adopted_postulate,
        diagnostic_only=diagnostic_only,
        deferred_status=deferred_status,
        mixed_status=mixed_status,
        hidden_status=hidden_status,
        status_drift=status_drift,
        P_insertion=P_insertion,
        P_active_O=P_active_O,
        P_residual_kill=P_residual_kill,
        P_parent=P_parent,
        L_component_status_modes=L_component_status_modes,
        L_mixed_status_modes=L_mixed_status_modes,
        L_invalid_status_modes=L_invalid_status_modes,
        L_downstream_closed=L_downstream_closed,
        L_status_sieve_gap=L_status_sieve_gap,
    )


def build_status_modes() -> List[StatusMode]:
    return [
        StatusMode(
            "S1: compatible-if-declared",
            "component form survives filters only if required declarations are explicit",
            "COMPATIBLE_IF_DECLARED",
            "current safe status for Group 33 and Group 34 surviving forms",
            "not selected, not adopted, not derived, not insertable",
            "can be carried only as audit status until declarations/status are changed explicitly",
        ),
        StatusMode(
            "S2: declared explicit candidate",
            "component declaration values are stated but no adoption occurs",
            "DECLARED_CANDIDATE",
            "possible future status after convention or membership criterion is declared",
            "not theorem proof and not adopted postulate",
            "may support a later theorem attempt or explicit decision record",
        ),
        StatusMode(
            "S3: theorem target",
            "component is pursued by derivation after declarations",
            "THEOREM_TARGET",
            "possible future route if declarations are fixed and a proof attempt is opened",
            "not already derived by being named as theorem target",
            "requires separate theorem script and proof obligations",
        ),
        StatusMode(
            "S4: explicit adopted postulate",
            "component is adopted by separate user/theory decision",
            "ADOPTION_REQUIRES_DECISION",
            "possible future theory-choice status",
            "must not be reported as derived or forced by audits",
            "requires separate adoption record and downstream handoff conditions",
        ),
        StatusMode(
            "S5: diagnostic-only/inert",
            "component label is used only for audit and does not alter equations",
            "DIAGNOSTIC_ONLY",
            "safe fallback for labels or bookkeeping objects",
            "not active membership, not trace insertion, not projector, not coefficient law",
            "cannot license downstream gates",
        ),
        StatusMode(
            "S6: deferred/not ready",
            "component or use remains unresolved",
            "DEFERRED",
            "safe status for incomplete declarations or blocked downstream use",
            "not permanent no-go theorem and not failure proof",
            "blocks insertion and parent work until status changes explicitly",
        ),
    ]


def build_status_pairs() -> List[StatusPair]:
    return [
        StatusPair(
            "P1: both compatible-if-declared",
            "P_trace_norm and P_safe_membership both remain compatible-if-declared",
            "COMPATIBLE_IF_DECLARED",
            "handoff says Package B remains audit-only and declaration-dependent",
            "the pair is shortened to selected, adopted, derived, or insertable",
            "safe current state; no downstream use licensed",
        ),
        StatusPair(
            "P2: one declared candidate, one compatible-if-declared",
            "one component has explicit declarations while the other remains conditional",
            "MIXED_STATUS_VISIBLE",
            "mixed status is recorded and downstream use is blocked or conditionalized",
            "Package B is treated as uniformly declared or usable",
            "mixed status is an obligation, not a recommendation",
        ),
        StatusPair(
            "P3: both declared explicit candidates",
            "both components have declarations but neither is adopted or proved",
            "DECLARED_CANDIDATE",
            "declarations are explicit and node separation is preserved",
            "declared candidates are treated as adopted postulates or theorem results",
            "may support a later decision/theorem route, not insertion",
        ),
        StatusPair(
            "P4: theorem target pair",
            "one or both components are pursued as theorem targets",
            "THEOREM_TARGET",
            "proof obligations and assumptions are explicit",
            "theorem target status is treated as theorem proof",
            "requires separate proof scripts before downstream use",
        ),
        StatusPair(
            "P5: adopted/deferred mixed pair",
            "one component is explicitly adopted while the other remains deferred or compatible-if-declared",
            "MIXED_STATUS_VISIBLE",
            "the adopted component has a separate adoption record and the deferred component blocks downstream use",
            "Package B is treated as fully adopted by one-component adoption",
            "mixed status must be carried visibly into handoff",
        ),
        StatusPair(
            "P6: diagnostic membership plus normalization candidate",
            "safe membership is diagnostic-only while trace normalization remains candidate or compatible-if-declared",
            "DIAGNOSTIC_ONLY",
            "diagnostic label is inert and cannot alter equations",
            "diagnostic label is used actively for insertion or residual control",
            "safe for audits only, not active Package B use",
        ),
    ]


def build_invalid_statuses() -> List[InvalidStatus]:
    return [
        InvalidStatus(
            "X1: hidden status mode",
            "handoff uses a Package B component without saying whether it is compatible-if-declared, candidate, theorem target, adopted, diagnostic-only, or deferred",
            "INVALID_STATUS",
            "status mode is required before future use",
            "audit status becomes ambiguous theory status",
        ),
        InvalidStatus(
            "X2: compatible-if-declared as adopted",
            "compatible-if-declared is shortened to adopted or selected",
            "FORBIDDEN_STATUS_UPGRADE",
            "conditional survival is weaker than adoption",
            "Group 35 accidentally adopts Package B",
        ),
        InvalidStatus(
            "X3: theorem target as theorem proof",
            "theorem-target status is treated as already derived",
            "FORBIDDEN_STATUS_UPGRADE",
            "proof target is not proof",
            "open theorem burden disappears by label",
        ),
        InvalidStatus(
            "X4: adopted postulate as derivation",
            "explicit adopted postulate is reported as derived theorem",
            "FORBIDDEN_STATUS_UPGRADE",
            "adoption is choice, not proof",
            "postulate/theorem boundary collapses",
        ),
        InvalidStatus(
            "X5: diagnostic-only as active",
            "diagnostic-only label is used to alter equations or support insertion",
            "FORBIDDEN_STATUS_UPGRADE",
            "diagnostic labels are safe only if inert",
            "audit label becomes active projector or insertion handle",
        ),
        InvalidStatus(
            "X6: status mode as insertion",
            "any status mode is treated as B_s/F_zeta insertion or parent readiness",
            "FORBIDDEN_STATUS_UPGRADE",
            "downstream gates remain closed",
            "status bookkeeping opens field equation gates prematurely",
        ),
    ]


def build_rules() -> List[SieveRule]:
    return [
        SieveRule(
            "R1: status mode is mandatory",
            "Every future handoff must state the status mode of P_trace_norm and P_safe_membership",
            "REQUIRED",
            "hidden status creates accidental adoption or downstream licensing",
        ),
        SieveRule(
            "R2: status mode is not status change",
            "This sieve classifies possible modes but assigns none as theory state",
            "POLICY_RULE",
            "classification is weaker than declaration, adoption, or proof",
        ),
        SieveRule(
            "R3: mixed status must remain visible",
            "A mixed Package B pair must not be reported as uniformly adopted, derived, or declared",
            "POLICY_RULE",
            "one component cannot license the other",
        ),
        SieveRule(
            "R4: adoption requires separate record",
            "Adopted-postulate mode requires a separate explicit user/theory decision record",
            "POLICY_RULE",
            "script classification must not adopt by implication",
        ),
        SieveRule(
            "R5: downstream gates remain closed",
            "No status mode licenses insertion, active O, residual control, or parent closure",
            "POLICY_RULE",
            "status bookkeeping is not downstream theorem closure",
        ),
    ]


def build_obligations() -> List[SieveObligation]:
    return [
        SieveObligation(
            "O1: preserve current status",
            "record current surviving forms as compatible-if-declared only unless later changed explicitly",
            "OPEN",
            "selection drift",
            "do not shorten current audit status to selected, adopted, or derived",
        ),
        SieveObligation(
            "O2: require explicit status mode before handoff",
            "require status mode for each Package B component before theorem/adoption/precondition handoff",
            "OPEN",
            "ambiguous downstream use",
            "mode must be visible before use",
        ),
        SieveObligation(
            "O3: preserve mixed-status discipline",
            "if component statuses differ, carry mixed status explicitly",
            "OPEN",
            "Package B overclaim",
            "one component's status cannot license the other",
        ),
        SieveObligation(
            "O4: preserve postulate/theorem boundary",
            "do not call adopted postulates derived and do not call theorem targets proved",
            "OPEN",
            "governance drift",
            "choice and proof remain separate",
        ),
        SieveObligation(
            "O5: adoption boundary",
            "do not adopt Package B or either component in this sieve",
            "REQUIRED",
            "governance integrity",
            "adoption requires a separate explicit decision",
        ),
        SieveObligation(
            "O6: downstream gates",
            "keep B_s/F_zeta insertion, active O, residual control, and parent closure closed",
            "NOT_READY",
            "downstream overreach",
            "status-mode sieve is not insertion or parent readiness",
        ),
    ]


def build_conclusions() -> List[SieveConclusion]:
    return [
        SieveConclusion(
            "C1: status modes classified",
            "possible component status modes are classified without assigning one as theory state",
            "STATUS_MODE_SIEVE",
            "future handoffs can distinguish audit status, candidate status, theorem target, adoption, diagnostic-only, deferred, and mixed status",
        ),
        SieveConclusion(
            "C2: current status preserved",
            "Group 33/34 surviving forms remain compatible-if-declared only",
            "COMPATIBLE_IF_DECLARED",
            "current audit status is not selected, adopted, derived, or insertable",
        ),
        SieveConclusion(
            "C3: mixed status fenced",
            "mixed component statuses must be visible before handoff",
            "MIXED_STATUS_VISIBLE",
            "mixed status is not recommendation or Package B adoption",
        ),
        SieveConclusion(
            "C4: invalid upgrades fail",
            "hidden status, adopted-as-derived, theorem-target-as-proof, diagnostic-as-active, and insertion/parent upgrades fail",
            "REQUIRED",
            "status language cannot smuggle proof or downstream gates",
        ),
        SieveConclusion(
            "C5: no adoption",
            "this sieve adopts no Package B component and recommends no adoption",
            "NOT_ADOPTED",
            "explicit decision remains separate",
        ),
        SieveConclusion(
            "C6: next",
            "declaration obligations or Group 35 status summary should run next",
            "OPEN",
            "summarize status-mode obligations without selecting components",
        ),
    ]


def case_0_problem(out: ScriptOutput) -> None:
    header("Case 0: Trace-anchor status-mode sieve problem")
    print("Question:\n")
    print("  Which status modes can be carried for trace normalization and safe membership")
    print("  before any Package B component is chosen, adopted, derived, or used downstream?")
    print("\nDiscipline:\n")
    print("  This script classifies status modes.")
    print("  It assigns no component status as the theory state.")
    print("  It chooses no declaration value.")
    print("  It selects no trace-normalization form.")
    print("  It selects no safe-membership form.")
    print("  It adopts no Package B component.")
    print("  It derives no coefficient law and no insertion.")
    print("  It keeps active O, residual control, and parent closure closed.")
    print("\nTiny goblin rule:")
    print("  Sort the tags before hanging them on the cups.")
    with out.governance_assessments():
        out.line(
            "trace-anchor status-mode sieve opened",
            StatusMark.INFO,
            "classifying component status modes after joint consistency matrix; no status assigned",
        )


def case_1_symbols(symbols: StatusSymbols, out: ScriptOutput) -> None:
    header("Case 1: Status-mode symbolic ledger")
    print("Status symbols:")
    for sym in (
        symbols.P_trace_norm,
        symbols.P_safe_membership,
        symbols.compatible_if_declared,
        symbols.declared_candidate,
        symbols.theorem_target,
        symbols.adopted_postulate,
        symbols.diagnostic_only,
        symbols.deferred_status,
        symbols.mixed_status,
        symbols.hidden_status,
        symbols.status_drift,
        symbols.P_insertion,
        symbols.P_active_O,
        symbols.P_residual_kill,
        symbols.P_parent,
    ):
        print(f"  {sym} = {sym}")
    print("\nComponent status-mode load:")
    print(f"  L_component_status_modes = {symbols.L_component_status_modes}")
    print("\nMixed-status load:")
    print(f"  L_mixed_status_modes = {symbols.L_mixed_status_modes}")
    print("\nInvalid-status load:")
    print(f"  L_invalid_status_modes = {symbols.L_invalid_status_modes}")
    print("\nDownstream closed load:")
    print(f"  L_downstream_closed = {symbols.L_downstream_closed}")
    print("\nStatus-sieve gap:")
    print(f"  L_status_sieve_gap = {symbols.L_status_sieve_gap}")
    with out.derived_results():
        out.line(
            "status-mode symbolic loads stated",
            StatusMark.OBLIGATION,
            f"L_component_status_modes={symbols.L_component_status_modes}; L_downstream_closed={symbols.L_downstream_closed}",
        )


def case_2_status_modes(modes: List[StatusMode], out: ScriptOutput) -> None:
    header("Case 2: Component status modes")
    with out.governance_assessments():
        for item in modes:
            subheader(item.name)
            print(f"Mode: {item.mode}")
            out.line(item.name, status_mark(item.status), item.status)
            print(f"Allowed meaning: {item.allowed_meaning}")
            print(f"Forbidden meaning: {item.forbidden_meaning}")
            print(f"Consequence: {item.consequence}")
        out.line(
            "component status modes classified",
            StatusMark.OBLIGATION,
            f"{len(modes)} possible modes classified; none assigned as current theory status",
        )


def case_3_status_pairs(pairs: List[StatusPair], out: ScriptOutput) -> None:
    header("Case 3: Joint status pair cases")
    with out.governance_assessments():
        for item in pairs:
            subheader(item.name)
            print(f"Pair: {item.pair}")
            out.line(item.name, status_mark(item.status), item.status)
            print(f"Coherent if: {item.coherent_if}")
            print(f"Fails if: {item.fails_if}")
            print(f"Boundary: {item.boundary}")
        out.line(
            "joint status pair cases stated",
            StatusMark.DEFER,
            f"{len(pairs)} status pair cases classified; no Package B status selected",
        )


def case_4_invalid_statuses(invalids: List[InvalidStatus], out: ScriptOutput) -> None:
    header("Case 4: Invalid status-mode shortcuts")
    with out.counterexamples():
        for item in invalids:
            subheader(item.name)
            print(f"Shortcut: {item.shortcut}")
            out.line(item.name, status_mark(item.status), item.status)
            print(f"Reason: {item.reason}")
            print(f"Failure mode: {item.failure_mode}")
        out.line(
            "invalid status-mode shortcuts rejected",
            StatusMark.FAIL,
            f"{len(invalids)} shortcuts rejected",
        )


def case_5_rules(rules: List[SieveRule], out: ScriptOutput) -> None:
    header("Case 5: Status-mode no-overclaim rules")
    with out.governance_assessments():
        for item in rules:
            subheader(item.name)
            print(f"Rule: {item.rule}")
            out.line(item.name, status_mark(item.status), item.status)
            print(f"Reason: {item.reason}")
        out.line(
            "status-mode no-overclaim rules stated",
            StatusMark.OBLIGATION,
            f"{len(rules)} rules stated",
        )


def case_6_obligations(obligations: List[SieveObligation], out: ScriptOutput) -> None:
    header("Case 6: Status-mode obligations")
    with out.unresolved_obligations():
        for item in obligations:
            subheader(item.name)
            print(f"Obligation: {item.obligation}")
            out.line(item.name, status_mark(item.status), item.status)
            print(f"Blocks: {item.blocks}")
            print(f"Discipline: {item.discipline}")
        out.line(
            "status-mode obligations opened",
            StatusMark.OBLIGATION,
            f"{len(obligations)} obligations stated",
        )


def case_7_conclusions(conclusions: List[SieveConclusion], out: ScriptOutput) -> None:
    header("Case 7: Status-mode conclusions")
    with out.governance_assessments():
        for item in conclusions:
            subheader(item.name)
            print(f"Conclusion: {item.conclusion}")
            out.line(item.name, status_mark(item.status), item.status)
            print(f"Meaning: {item.meaning}")
        out.line(
            "trace-anchor status-mode sieve conclusion stated",
            StatusMark.PASS,
            "status modes classified; current compatible-if-declared status preserved; no adoption or downstream gates",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Trace-anchor status-mode sieve result:\n")
    print("  Possible Package B component status modes are classified.")
    print("  The current Group 33/34 surviving forms remain compatible-if-declared only.")
    print("  Declared-candidate, theorem-target, adopted-postulate, diagnostic-only, and deferred modes are possible future modes only if explicitly recorded.")
    print("  Mixed component statuses must be visible before handoff.")
    print("  Hidden status, compatible-if-declared-as-adopted, theorem-target-as-proof, adopted-postulate-as-derived, diagnostic-as-active, and status-as-insertion fail.")
    print("  No Package B component status is assigned, selected, adopted, or derived by this sieve.")
    print("  B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready.")
    print("\nPossible next script:")
    print("  candidate_trace_anchor_declaration_obligations.py")
    print("\nTiny goblin label:")
    print("  Sort the tags before hanging them on the cups.")
    with out.governance_assessments():
        out.line(
            "trace-anchor status-mode sieve complete",
            StatusMark.PASS,
            "declaration obligations should run next; adoption and downstream gates remain closed",
        )


def record_inventory_marker(ns, symbols: StatusSymbols) -> None:
    ns.record_derivation(
        derivation_id="g35_status_mode_sieve",
        inputs=[
            symbols.L_component_status_modes,
            symbols.L_mixed_status_modes,
            symbols.L_invalid_status_modes,
            symbols.L_downstream_closed,
        ],
        output=symbols.L_status_sieve_gap,
        method="Group 35 status-mode sieve over trace-anchor Package B components",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="trace_anchor_status_mode_sieve_marker",
        is_placeholder=True,
    )


def record_obligations(ns, obligations: List[SieveObligation]) -> None:
    for item in obligations:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_obligation(
            ProofObligationRecord(
                obligation_id=f"g35_status_mode_{ident}",
                script_id=SCRIPT_ID,
                title=item.name,
                status=ObligationStatus.OPEN if item.status != "NOT_READY" else ObligationStatus.DEFERRED,
                required_by=[SCRIPT_ID],
                description=f"{item.obligation} Blocks: {item.blocks}. Discipline: {item.discipline}.",
            )
        )


def record_governance(
    ns,
    modes: List[StatusMode],
    pairs: List[StatusPair],
    invalids: List[InvalidStatus],
    rules: List[SieveRule],
) -> None:
    obligation_ids = [
        "g35_status_mode_o1",
        "g35_status_mode_o2",
        "g35_status_mode_o3",
        "g35_status_mode_o4",
        "g35_status_mode_o5",
        "g35_status_mode_o6",
    ]

    ns.record_route(
        RouteRecord(
            route_id="g35_status_mode_sieve_route",
            script_id=SCRIPT_ID,
            name="Group 35 trace-anchor status-mode sieve route",
            status=GovernanceStatus.CANDIDATE_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            required_obligations=obligation_ids,
            activation_conditions=[
                "joint consistency matrix classified declaration combinations",
                "current trace normalization forms remain compatible-if-declared",
                "current safe membership forms remain compatible-if-declared",
                "future handoffs require explicit component status modes",
            ],
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
                derivation_ids=["g35_status_mode_sieve"],
                obligation_ids=obligation_ids,
            )
        )

    for item in pairs:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g35_status_pair_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.CANDIDATE_ROUTE,
                statement=(
                    f"Status pair: {item.pair}. Coherent if: {item.coherent_if}. "
                    f"Fails if: {item.fails_if}. Boundary: {item.boundary}."
                ),
                derivation_ids=["g35_status_mode_sieve"],
                obligation_ids=obligation_ids,
            )
        )

    for item in invalids:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g35_invalid_status_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.POLICY_RULE,
                statement=f"Invalid status shortcut: {item.shortcut}. Reason: {item.reason}. Failure mode: {item.failure_mode}.",
                derivation_ids=["g35_status_mode_sieve"],
                obligation_ids=obligation_ids,
            )
        )

    for item in rules:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g35_status_rule_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.POLICY_RULE,
                statement=f"{item.rule}. Reason: {item.reason}.",
                derivation_ids=["g35_status_mode_sieve"],
                obligation_ids=obligation_ids,
            )
        )

    ns.record_claim(
        ClaimRecord(
            claim_id="g35_status_mode_sieve_complete",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.CANDIDATE_ROUTE,
            statement=(
                "Trace-anchor component status modes are classified. Current surviving forms remain "
                "compatible-if-declared only; no status mode is assigned as adopted, derived, selected, or insertable."
            ),
            derivation_ids=["g35_status_mode_sieve"],
            obligation_ids=obligation_ids,
        )
    )


def main() -> None:
    header("Candidate Trace Anchor Status Mode Sieve")
    archive, ns, invalidated = prepare_archive()
    ensure_archive_write_dirs(ns)
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    modes = build_status_modes()
    pairs = build_status_pairs()
    invalids = build_invalid_statuses()
    rules = build_rules()
    obligations = build_obligations()
    conclusions = build_conclusions()

    case_0_problem(out)
    case_1_symbols(symbols, out)
    case_2_status_modes(modes, out)
    case_3_status_pairs(pairs, out)
    case_4_invalid_statuses(invalids, out)
    case_5_rules(rules, out)
    case_6_obligations(obligations, out)
    case_7_conclusions(conclusions, out)
    final_interpretation(out)

    record_inventory_marker(ns, symbols)
    record_obligations(ns, obligations)
    record_governance(ns, modes, pairs, invalids, rules)

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
