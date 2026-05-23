# Candidate Group 34 status summary
#
# Group:
#   34_safe_trace_membership_candidate_origin
#
# Human title:
#   Safe Trace Membership Candidate Origin
#
# Script type:
#   SUMMARY / ORIGIN-ROUTE CLOSURE
#
# Purpose
# -------
# Close Group 34 by summarizing the safe-trace-membership candidate-origin route:
#
#   origin problem opener,
#   domain ledger,
#   selector firewall,
#   candidate membership forms,
#   compatibility sieve,
#   obligations summary.
#
# Locked-door question:
#
#   What did the safe trace membership candidate-origin route establish,
#   and what remains open before zeta_Bs -> T_zeta can be selected, adopted, or used?
#
# This script does not adopt a safe-membership postulate.
# It does not select a final membership form.
# It does not derive a safe-membership theorem.
# It does not derive trace/residual zero incidence.
# It does not derive a complete B_s/F_zeta coefficient law.
# It does not derive B_s/F_zeta insertion.
# It does not open active O, residual control, or parent closure.
#
# Tiny goblin rule:
#
#   Count the shelves. Close the cupboard. Still no shelving.

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
        "CANDIDATE_FORM": StatusMark.INFO,
        "COMPATIBILITY_ONLY": StatusMark.INFO,
        "COMPATIBLE_IF_DECLARED": StatusMark.INFO,
        "CONDITIONAL": StatusMark.DEFER,
        "FILTER_FAIL": StatusMark.FAIL,
        "HANDOFF_READY": StatusMark.INFO,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "ORIGIN_ROUTE_SUMMARY": StatusMark.INFO,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REQUIRED": StatusMark.OBLIGATION,
        "SELECTOR_REJECTED": StatusMark.FAIL,
        "SUMMARY": StatusMark.INFO,
        "VALID_IF_INERT": StatusMark.INFO,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g34_obligations",
            "034_safe_trace_membership_candidate_origin__candidate_safe_trace_membership_obligations",
            "g34_safe_membership_obligations",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g34_compatibility_sieve",
            "034_safe_trace_membership_candidate_origin__candidate_safe_trace_membership_compatibility_sieve",
            "g34_safe_membership_compatibility_sieve",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g34_candidate_forms",
            "034_safe_trace_membership_candidate_origin__candidate_safe_trace_membership_candidate_forms",
            "g34_safe_membership_candidate_forms",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g34_selector_firewall",
            "034_safe_trace_membership_candidate_origin__candidate_safe_trace_membership_selector_rejection",
            "g34_safe_membership_selector_rejection",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g34_domain_ledger",
            "034_safe_trace_membership_candidate_origin__candidate_safe_trace_membership_domain_ledger",
            "g34_safe_membership_domain_ledger",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g34_origin_problem",
            "034_safe_trace_membership_candidate_origin__candidate_safe_trace_membership_origin_problem",
            "g34_safe_membership_origin_problem",
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
class SummarySymbols:
    M_safe: sp.Symbol
    M_typed: sp.Symbol
    M_role_pure: sp.Symbol
    M_norm_compat: sp.Symbol
    M_diag: sp.Symbol
    O_membership_criterion: sp.Symbol
    O_role_purity: sp.Symbol
    O_norm_separation: sp.Symbol
    O_inert_label: sp.Symbol
    P_insertion: sp.Symbol
    P_active_O: sp.Symbol
    P_residual_kill: sp.Symbol
    P_parent: sp.Symbol
    L_surviving_forms: sp.Basic
    L_open_decisions: sp.Basic
    L_downstream_closed: sp.Basic
    L_group34_summary: sp.Basic


@dataclass
class Group34StatusEntry:
    name: str
    topic: str
    status: str
    result: str
    boundary: str


@dataclass
class FinalGap:
    name: str
    status: str
    reason: str
    discipline: str


@dataclass
class FinalHandoff:
    name: str
    status: str
    reason: str
    caution: str


@dataclass
class RejectedUpgrade:
    name: str
    upgrade: str
    reason: str


@dataclass
class FinalObligation:
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


def build_symbols() -> SummarySymbols:
    M_safe = sp.Symbol("M_safe")
    M_typed = sp.Symbol("M_typed")
    M_role_pure = sp.Symbol("M_role_pure")
    M_norm_compat = sp.Symbol("M_norm_compat")
    M_diag = sp.Symbol("M_diag")
    O_membership_criterion = sp.Symbol("O_membership_criterion")
    O_role_purity = sp.Symbol("O_role_purity")
    O_norm_separation = sp.Symbol("O_norm_separation")
    O_inert_label = sp.Symbol("O_inert_label")
    P_insertion = sp.Symbol("P_insertion")
    P_active_O = sp.Symbol("P_active_O")
    P_residual_kill = sp.Symbol("P_residual_kill")
    P_parent = sp.Symbol("P_parent")

    L_surviving_forms = sp.simplify(M_typed + M_role_pure + M_norm_compat + M_diag)
    L_open_decisions = sp.simplify(
        O_membership_criterion + O_role_purity + O_norm_separation + O_inert_label
    )
    L_downstream_closed = sp.simplify(P_active_O + P_insertion + P_parent + P_residual_kill)
    L_group34_summary = sp.simplify(
        M_safe + L_surviving_forms + L_open_decisions + L_downstream_closed
    )

    return SummarySymbols(
        M_safe=M_safe,
        M_typed=M_typed,
        M_role_pure=M_role_pure,
        M_norm_compat=M_norm_compat,
        M_diag=M_diag,
        O_membership_criterion=O_membership_criterion,
        O_role_purity=O_role_purity,
        O_norm_separation=O_norm_separation,
        O_inert_label=O_inert_label,
        P_insertion=P_insertion,
        P_active_O=P_active_O,
        P_residual_kill=P_residual_kill,
        P_parent=P_parent,
        L_surviving_forms=L_surviving_forms,
        L_open_decisions=L_open_decisions,
        L_downstream_closed=L_downstream_closed,
        L_group34_summary=L_group34_summary,
    )


def build_status_entries() -> List[Group34StatusEntry]:
    return [
        Group34StatusEntry(
            "G34-1: origin route opener",
            "Group 34 opened the safe trace membership candidate-origin route",
            "ORIGIN_ROUTE_SUMMARY",
            "route opened after Group 33 clarified trace-normalization forms as compatible-if-declared candidates",
            "opener adopted no postulate and derived no membership theorem",
        ),
        Group34StatusEntry(
            "G34-2: domain ledger",
            "zeta_Bs, T_zeta, membership domain, codomain, and exclusion zones were inventoried",
            "SUMMARY",
            "membership objects and fences became visible before membership-form testing",
            "domain visibility is not proof of membership",
        ),
        Group34StatusEntry(
            "G34-3: selector firewall",
            "forbidden selector routes were rejected",
            "SELECTOR_REJECTED",
            "recovery, repair, incidence, residual kill, active-O, insertion, parent-fit, normalization-convenience, and hidden-load selectors are rejected",
            "selector rejection is not derivation of the correct membership form",
        ),
        Group34StatusEntry(
            "G34-4: candidate forms",
            "visible candidate membership forms were stated",
            "CANDIDATE_FORM",
            "typed, role-pure, normalization-compatible, and diagnostic-only forms are visible candidates",
            "candidate form is not selected, adopted, incidence, or insertion",
        ),
        Group34StatusEntry(
            "G34-5: compatibility sieve",
            "membership forms were filtered for typed-domain clarity and anti-smuggling discipline",
            "SUMMARY",
            "typed and role-pure forms survive if declared; diagnostic label survives only if inert; invalid payloads fail",
            "compatibility filters may reject or flag but cannot choose safe membership",
        ),
        Group34StatusEntry(
            "G34-6: obligations summary",
            "surviving forms and open decisions were summarized",
            "SUMMARY",
            "membership criterion, role-purity enforcement, normalization compatibility, diagnostic/active scope, and adoption boundary remain open",
            "obligations summary adopted no postulate and selected no membership form",
        ),
        Group34StatusEntry(
            "G34-7: downstream gates",
            "B_s/F_zeta insertion, active O, residual control, and parent closure",
            "NOT_READY",
            "all downstream gates remain closed",
            "Group 34 is not insertion, residual control, active O, or parent readiness",
        ),
    ]


def build_final_gaps() -> List[FinalGap]:
    return [
        FinalGap(
            "G1: membership criterion",
            "OPEN",
            "typed membership requires an explicit criterion for zeta_Bs belonging to T_zeta",
            "label T_zeta is not proof",
        ),
        FinalGap(
            "G2: role-purity enforcement",
            "OPEN",
            "role-pure forms require a way to keep residual/source/correction payloads outside membership",
            "role-purity is not residual kill, source theorem, or divergence safety",
        ),
        FinalGap(
            "G3: normalization compatibility",
            "OPEN",
            "membership must remain compatible with but separate from Group 33 trace-normalization forms",
            "membership is not normalization",
        ),
        FinalGap(
            "G4: diagnostic versus active membership scope",
            "OPEN",
            "diagnostic labels are safe only if inert; active membership would need further theorem support or explicit adoption",
            "diagnostic label cannot alter equations",
        ),
        FinalGap(
            "G5: safe-membership theorem",
            "NOT_DERIVED",
            "forms survived conditionally but no theorem proved zeta_Bs belongs to T_zeta",
            "compatible-if-declared is not derived",
        ),
        FinalGap(
            "G6: safe-membership adoption",
            "NOT_ADOPTED",
            "Group 34 is an origin audit, not an adoption event",
            "explicit user/theory decision remains separate",
        ),
        FinalGap(
            "G7: trace/residual incidence",
            "NOT_READY",
            "safe membership remains separate from I(T_zeta,R_zeta)=0 and I(T_zeta,R_kappa)=0",
            "membership is not incidence or residual control",
        ),
        FinalGap(
            "G8: insertion and parent closure",
            "NOT_READY",
            "safe membership is not selected/adopted and incidence/residual/no-overlap gates remain open",
            "Group 34 does not license insertion or parent equation",
        ),
    ]


def build_handoffs() -> List[FinalHandoff]:
    return [
        FinalHandoff(
            "H1: explicit safe-membership decision",
            "OPEN",
            "surviving forms are visible if the theory owner wants to choose one explicitly",
            "adopted postulate must not be called derived",
        ),
        FinalHandoff(
            "H2: safe-membership theorem attempt",
            "OPEN",
            "typed and role-pure forms remain theorem targets after declarations",
            "declare object, sector, domain, codomain, criterion, and exclusion zones first",
        ),
        FinalHandoff(
            "H3: trace-anchor package continuation",
            "CONDITIONAL",
            "normalization and membership are both audited but remain separate Package B components",
            "Package B compatibility is not insertion",
        ),
        FinalHandoff(
            "H4: conditional trace-anchor precondition inventory",
            "CONDITIONAL",
            "may be useful only if adoption/theorem status is explicitly stated",
            "precondition inventory is not insertion theorem",
        ),
        FinalHandoff(
            "H5: B_s/F_zeta insertion theorem",
            "NOT_READY",
            "membership is not selected/adopted and incidence/no-overlap/residual gates remain open",
            "forbidden as immediate theorem route from Group 34 alone",
        ),
        FinalHandoff(
            "H6: parent field equation",
            "NOT_READY",
            "scalar recombination and downstream gates remain unresolved",
            "parent gate remains closed",
        ),
    ]


def build_rejected_upgrades() -> List[RejectedUpgrade]:
    return [
        RejectedUpgrade(
            "R1: compatible-if-declared as selected",
            "treat a surviving membership form as the selected safe membership",
            "survival under filters is weaker than selection",
        ),
        RejectedUpgrade(
            "R2: compatible-if-declared as adopted",
            "treat a surviving membership form as adopted P_safe_membership",
            "Group 34 performed origin audit, not adoption",
        ),
        RejectedUpgrade(
            "R3: typed label as theorem",
            "treat T_zeta label or domain visibility as proof of membership",
            "domain/codomain visibility is prerequisite, not proof",
        ),
        RejectedUpgrade(
            "R4: membership as normalization",
            "treat zeta_Bs -> T_zeta as choosing P_trace_norm or being chosen by P_trace_norm",
            "normalization and membership are separate Package B nodes",
        ),
        RejectedUpgrade(
            "R5: membership as incidence",
            "treat safe membership as zero trace/residual incidence",
            "incidence remains high-risk and separate",
        ),
        RejectedUpgrade(
            "R6: membership as residual/source/divergence cleanup",
            "use membership to carry or erase residual, ordinary source, or correction/divergence payloads",
            "membership cannot be a hidden-load pocket",
        ),
        RejectedUpgrade(
            "R7: surviving form as insertion",
            "treat a surviving membership form as B_s/F_zeta insertion",
            "insertion remains downstream and not ready",
        ),
        RejectedUpgrade(
            "R8: surviving form as parent closure",
            "open parent equation from safe-membership form survival",
            "parent gate remains closed",
        ),
    ]


def build_obligations() -> List[FinalObligation]:
    return [
        FinalObligation(
            "O1: preserve compatible-if-declared status",
            "record surviving typed and role-pure forms as compatible-if-declared only",
            "OPEN",
            "selection drift",
            "do not shorten to selected, adopted, or derived",
        ),
        FinalObligation(
            "O2: declare membership criterion before use",
            "require zeta_Bs object, T_zeta sector, domain, codomain, and criterion before theorem or adoption use",
            "OPEN",
            "typed membership claims",
            "label is not proof",
        ),
        FinalObligation(
            "O3: preserve role purity",
            "keep residual/source/correction payloads outside membership unless separately derived",
            "OPEN",
            "hidden-load smuggling",
            "membership is not cleanup",
        ),
        FinalObligation(
            "O4: keep normalization separate from membership",
            "carry Group 33 trace-normalization forms as separate compatibility nodes only",
            "OPEN",
            "Package B collapse",
            "membership is not normalization",
        ),
        FinalObligation(
            "O5: adoption remains separate",
            "keep P_safe_membership unadopted unless a separate explicit decision is requested",
            "OPEN",
            "accidental adoption",
            "candidate survival is not adoption",
        ),
        FinalObligation(
            "O6: downstream gates remain closed",
            "keep B_s/F_zeta insertion, active O, residual control, and parent equation closed",
            "NOT_READY",
            "downstream overreach",
            "Group 34 is not insertion or parent closure",
        ),
    ]


def build_conclusions() -> List[Conclusion]:
    return [
        Conclusion(
            "C1: Group 34 result",
            "Group 34 completed a safe-trace-membership candidate-origin audit",
            "ORIGIN_ROUTE_SUMMARY",
            "surviving forms, selector failures, failed filters, and open decisions are visible",
        ),
        Conclusion(
            "C2: surviving forms",
            "typed trace-sector and role-pure membership forms survive if declared",
            "COMPATIBLE_IF_DECLARED",
            "both remain candidate forms; neither is selected",
        ),
        Conclusion(
            "C3: diagnostic scope",
            "diagnostic-only trace label survives only if strictly inert",
            "VALID_IF_INERT",
            "not adopted membership or insertion",
        ),
        Conclusion(
            "C4: no derivation or adoption",
            "Group 34 derives no safe-membership theorem and adopts no postulate",
            "NOT_ADOPTED",
            "explicit choice or theorem route remains separate",
        ),
        Conclusion(
            "C5: downstream gates",
            "B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready",
            "NOT_READY",
            "Group 34 does not open downstream gates",
        ),
        Conclusion(
            "C6: next",
            "future work requires explicit adoption, theorem attempt after declarations, or conditional trace-anchor precondition inventory",
            "OPEN",
            "do not name an insertion theorem unless adoption/theorem status is explicit",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Group 34 status summary problem")
    print("Question:\n")
    print("  What did the safe trace membership candidate-origin route establish,")
    print("  and what remains open before zeta_Bs -> T_zeta can be selected, adopted, or used?")
    print("\nDiscipline:\n")
    print("  This script summarizes Group 34.")
    print("  It adopts no safe-membership postulate.")
    print("  It selects no final membership form.")
    print("  It derives no safe-membership theorem.")
    print("  It derives no trace/residual zero incidence.")
    print("  It derives no coefficient law and no insertion.")
    print("  It keeps active O, residual control, and parent closure closed.")
    print("\nTiny goblin rule:")
    print("  Count the shelves. Close the cupboard. Still no shelving.")
    with out.governance_assessments():
        out.line(
            "Group 34 status summary opened",
            StatusMark.INFO,
            "closing safe-membership origin route while preserving no-selection/no-adoption boundary",
        )


def case_1_symbolic_summary(symbols: SummarySymbols, out: ScriptOutput) -> None:
    header("Case 1: Group 34 symbolic summary loads")
    print("Candidate symbols:")
    for name in [
        "M_safe",
        "M_typed",
        "M_role_pure",
        "M_norm_compat",
        "M_diag",
        "O_membership_criterion",
        "O_role_purity",
        "O_norm_separation",
        "O_inert_label",
        "P_insertion",
        "P_active_O",
        "P_residual_kill",
        "P_parent",
    ]:
        print(f"  {name} = {getattr(symbols, name)}")
    print("\nSurviving-form load:")
    print(f"  L_surviving_forms = {symbols.L_surviving_forms}")
    print("\nOpen-decision load:")
    print(f"  L_open_decisions = {symbols.L_open_decisions}")
    print("\nDownstream closed load:")
    print(f"  L_downstream_closed = {symbols.L_downstream_closed}")
    print("\nGroup 34 summary load:")
    print(f"  L_group34_summary = {symbols.L_group34_summary}")
    with out.derived_results():
        out.line(
            "Group 34 symbolic summary loads stated",
            StatusMark.OBLIGATION,
            f"L_open_decisions={symbols.L_open_decisions}; L_downstream_closed={symbols.L_downstream_closed}",
        )


def case_2_status_entries(entries: List[Group34StatusEntry], out: ScriptOutput) -> None:
    header("Case 2: Group 34 status entries")
    with out.governance_assessments():
        for item in entries:
            subheader(item.name)
            print(f"Topic: {item.topic}\n")
            out.line(item.name, status_mark(item.status), item.status)
            print(f"Result: {item.result}")
            print(f"Boundary: {item.boundary}")
        out.line("Group 34 status entries stated", StatusMark.INFO, f"{len(entries)} status entries stated")


def case_3_final_gaps(gaps: List[FinalGap], out: ScriptOutput) -> None:
    header("Case 3: Final open gaps")
    with out.unresolved_obligations():
        for item in gaps:
            subheader(item.name)
            out.line(item.name, status_mark(item.status), item.status)
            print(f"Reason: {item.reason}")
            print(f"Discipline: {item.discipline}")
        out.line("Group 34 final gaps stated", StatusMark.OBLIGATION, f"{len(gaps)} gaps remain open or not ready")


def case_4_final_handoffs(handoffs: List[FinalHandoff], out: ScriptOutput) -> None:
    header("Case 4: Final handoffs")
    with out.governance_assessments():
        for item in handoffs:
            subheader(item.name)
            out.line(item.name, status_mark(item.status), item.status)
            print(f"Reason: {item.reason}")
            print(f"Caution: {item.caution}")
        out.line("Group 34 handoffs stated", StatusMark.DEFER, f"{len(handoffs)} handoffs stated; adoption/insertion remain separate")


def case_5_rejected_upgrades(upgrades: List[RejectedUpgrade], out: ScriptOutput) -> None:
    header("Case 5: Rejected summary upgrades")
    with out.governance_assessments():
        for item in upgrades:
            subheader(item.name)
            print(f"Upgrade: {item.upgrade}\n")
            out.line(item.name, StatusMark.OBLIGATION, "POLICY_RULE")
            print(f"Reason: {item.reason}")
        out.line("Group 34 summary upgrades rejected", StatusMark.OBLIGATION, f"{len(upgrades)} upgrade shortcuts rejected as policy rules")


def case_6_final_obligations(obligations: List[FinalObligation], out: ScriptOutput) -> None:
    header("Case 6: Group 34 final obligations")
    with out.unresolved_obligations():
        for item in obligations:
            subheader(item.name)
            print(f"Obligation: {item.obligation}\n")
            out.line(item.name, status_mark(item.status), item.status)
            print(f"Blocks: {item.blocks}")
            print(f"Discipline: {item.discipline}")
        out.line("Group 34 final obligations opened", StatusMark.OBLIGATION, f"{len(obligations)} obligations stated")


def case_7_conclusions(conclusions: List[Conclusion], out: ScriptOutput) -> None:
    header("Case 7: Group 34 conclusions")
    with out.governance_assessments():
        for item in conclusions:
            subheader(item.name)
            print(f"Conclusion: {item.conclusion}\n")
            out.line(item.name, status_mark(item.status), item.status)
            print(f"Meaning: {item.meaning}")
        out.line(
            "Group 34 status summary conclusion stated",
            StatusMark.PASS,
            "candidate-origin audit complete; no membership selected or adopted; downstream gates closed",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Group 34 status summary result:\n")
    print("  Group 34 completed a safe trace membership candidate-origin audit.")
    print("  Typed trace-sector and role-pure membership forms survive as compatible-if-declared candidates.")
    print("  Normalization-compatible membership remains compatibility only and does not collapse Package B.")
    print("  Diagnostic-only trace labels remain safe only if strictly equation-inert.")
    print("  Undeclared objects, hidden source load, hidden divergence reservoirs, residual payloads,")
    print("  normalization collapse, and downstream use fail.")
    print("  The remaining open decisions are membership criterion, role-purity enforcement,")
    print("  normalization compatibility, diagnostic/active scope, and adoption boundary.")
    print("  No safe-membership theorem is derived.")
    print("  No safe-membership postulate is adopted.")
    print("  B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready.")
    print("\nPossible next step:")
    print("  explicit safe-membership decision record, theorem attempt after declarations,")
    print("  trace-anchor package continuation, or conditional precondition inventory")
    print("\nTiny goblin label:")
    print("  Count the shelves. Close the cupboard. Still no shelving.")
    with out.governance_assessments():
        out.line(
            "candidate Group 34 status summary complete",
            StatusMark.PASS,
            "safe-membership origin route closed as audit; adoption and downstream gates remain separate",
        )


def record_inventory_marker(ns, symbols: SummarySymbols) -> None:
    ns.record_derivation(
        derivation_id="g34_status_summary",
        inputs=[symbols.M_safe, symbols.M_typed, symbols.M_role_pure, symbols.M_norm_compat, symbols.M_diag],
        output=symbols.L_group34_summary,
        method="Group 34 safe-membership origin-route status summary ledger",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="status_summary_marker",
        is_placeholder=True,
    )


def record_obligations(ns, obligations: List[FinalObligation]) -> None:
    for item in obligations:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_obligation(
            ProofObligationRecord(
                obligation_id=f"g34_summary_{ident}",
                script_id=SCRIPT_ID,
                title=item.name,
                status=ObligationStatus.OPEN if item.status != "NOT_READY" else ObligationStatus.DEFERRED,
                required_by=[SCRIPT_ID],
                description=f"{item.obligation} Blocks: {item.blocks}. Discipline: {item.discipline}.",
            )
        )


def record_governance(
    ns,
    status_entries: List[Group34StatusEntry],
    gaps: List[FinalGap],
    handoffs: List[FinalHandoff],
    upgrades: List[RejectedUpgrade],
) -> None:
    obligation_ids = [
        "g34_summary_o1",
        "g34_summary_o2",
        "g34_summary_o3",
        "g34_summary_o4",
        "g34_summary_o5",
        "g34_summary_o6",
    ]

    ns.record_route(
        RouteRecord(
            route_id="g34_safe_membership_origin_summary_route",
            script_id=SCRIPT_ID,
            name="Group 34 safe-membership origin-route summary",
            status=GovernanceStatus.CANDIDATE_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            required_obligations=obligation_ids,
            activation_conditions=[
                "origin problem completed",
                "domain ledger completed",
                "selector firewall completed",
                "candidate forms completed",
                "compatibility sieve completed",
                "obligations summary completed",
                "selection/adoption remain separate",
            ],
        )
    )

    for item in status_entries:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        status = GovernanceStatus.CANDIDATE_ROUTE
        if item.status in {"NOT_READY", "FILTER_FAIL"}:
            status = GovernanceStatus.DEFERRED_PENDING_PREREQUISITES
        elif item.status == "SELECTOR_REJECTED":
            status = GovernanceStatus.REJECTED_ROUTE
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g34_status_entry_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=status,
                statement=f"{item.topic}. Result: {item.result}. Boundary: {item.boundary}.",
                derivation_ids=["g34_status_summary"],
                obligation_ids=obligation_ids,
            )
        )

    for item in gaps:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_obligation(
            ProofObligationRecord(
                obligation_id=f"g34_final_gap_{ident}",
                script_id=SCRIPT_ID,
                title=item.name,
                status=ObligationStatus.OPEN if item.status != "NOT_READY" else ObligationStatus.DEFERRED,
                required_by=[SCRIPT_ID],
                description=f"{item.reason} Discipline: {item.discipline}.",
            )
        )

    for item in handoffs:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g34_handoff_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=(
                    GovernanceStatus.DEFERRED_PENDING_PREREQUISITES
                    if item.status == "NOT_READY"
                    else GovernanceStatus.CANDIDATE_ROUTE
                ),
                statement=f"{item.name}: {item.reason}. Caution: {item.caution}.",
                derivation_ids=["g34_status_summary"],
                obligation_ids=obligation_ids,
            )
        )

    for item in upgrades:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g34_rejected_upgrade_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.POLICY_RULE,
                statement=f"Forbidden upgrade: {item.upgrade}. Reason: {item.reason}.",
                derivation_ids=["g34_status_summary"],
                obligation_ids=obligation_ids,
            )
        )

    ns.record_claim(
        ClaimRecord(
            claim_id="g34_status_summary_complete",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.POLICY_RULE,
            statement=(
                "Group 34 is closed as a safe trace membership candidate-origin audit. "
                "Typed and role-pure membership forms survive as compatible-if-declared candidates, "
                "but no safe-membership form is selected, adopted, or derived. Downstream gates remain closed."
            ),
            derivation_ids=["g34_status_summary"],
            obligation_ids=obligation_ids,
        )
    )


def main() -> None:
    header("Candidate Group 34 Status Summary")
    archive, ns, invalidated = prepare_archive()
    ensure_archive_write_dirs(ns)
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    status_entries = build_status_entries()
    final_gaps = build_final_gaps()
    handoffs = build_handoffs()
    rejected_upgrades = build_rejected_upgrades()
    obligations = build_obligations()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_symbolic_summary(symbols, out)
    case_2_status_entries(status_entries, out)
    case_3_final_gaps(final_gaps, out)
    case_4_final_handoffs(handoffs, out)
    case_5_rejected_upgrades(rejected_upgrades, out)
    case_6_final_obligations(obligations, out)
    case_7_conclusions(conclusions, out)
    final_interpretation(out)

    record_inventory_marker(ns, symbols)
    record_obligations(ns, obligations)
    record_governance(ns, status_entries, final_gaps, handoffs, rejected_upgrades)

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
