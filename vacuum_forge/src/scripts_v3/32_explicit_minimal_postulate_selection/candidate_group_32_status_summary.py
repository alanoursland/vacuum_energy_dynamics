# Candidate Group 32 status summary
#
# Group:
#   32_explicit_minimal_postulate_selection
#
# Human title:
#   Explicit Minimal Postulate Selection
#
# Script type:
#   SUMMARY / ADOPTION-BOUNDARY RECORD
#
# Purpose
# -------
# Close Group 32 by summarizing the explicit minimal postulate selection audit:
#
#   explicit-choice route opener,
#   candidate postulate ledger,
#   dependency / no-smuggling graph,
#   package sieve,
#   package minimality accounting.
#
# Locked-door question:
#
#   What did Group 32 establish, and what remains outside the adoption boundary?
#
# This script does not adopt a postulate.
# It does not recommend adoption.
# It does not select Package B.
# It does not derive trace normalization.
# It does not derive safe trace membership.
# It does not derive trace/residual incidence.
# It does not derive the complete coefficient law.
# It does not derive B_s/F_zeta insertion.
# It does not derive active O.
# It does not derive residual control.
# It does not open the parent equation.
#
# Tiny goblin rule:
#
#   Count the teeth. Close the mouth. The bite is still a choice.

from dataclasses import dataclass
from pathlib import Path
from typing import List

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    BranchDecisionRecord,
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
        "ADOPTION_SEPARATE": StatusMark.DEFER,
        "CANDIDATE_REMAINS": StatusMark.DEFER,
        "CANDIDATE_ROUTE": StatusMark.DEFER,
        "EXPLICIT_CHOICE_AUDIT": StatusMark.INFO,
        "GATE_CLOSED": StatusMark.DEFER,
        "HIGH_RISK": StatusMark.DEFER,
        "INHERITED_DISCIPLINE": StatusMark.INFO,
        "INSUFFICIENT": StatusMark.DEFER,
        "MINIMAL_PLAUSIBLE_TO_AUDIT": StatusMark.INFO,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "OVERSTRONG": StatusMark.DEFER,
        "PARTIAL_CONSTRAINT": StatusMark.INFO,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REJECTED_AS_CURRENT_SHORTCUT": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "SUMMARY": StatusMark.INFO,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g32_minimality",
            "32_explicit_minimal_postulate_selection__candidate_postulate_package_minimality",
            "g32_postulate_package_minimality",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g32_package_sieve",
            "32_explicit_minimal_postulate_selection__candidate_postulate_package_sieve",
            "g32_postulate_package_sieve",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g32_dependency_graph",
            "32_explicit_minimal_postulate_selection__candidate_postulate_dependency_graph",
            "g32_postulate_dependency_graph",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g32_candidate_ledger",
            "32_explicit_minimal_postulate_selection__candidate_postulate_candidate_ledger",
            "g32_candidate_postulate_ledger",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g32_problem",
            "32_explicit_minimal_postulate_selection__candidate_explicit_postulate_selection_problem",
            "g32_explicit_selection_problem",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_summary",
            "31_source_divergence_coefficient_law__candidate_group_31_status_summary",
            "g31_status_summary",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_obligations",
            "31_source_divergence_coefficient_law__candidate_source_divergence_obligations",
            "g31_obligations",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g30_summary",
            "30_minimal_coefficient_sector_postulate_inventory__candidate_group_30_status_summary",
            "g30_status_summary",
            RecordKind.INVENTORY_MARKER,
        ),
    ]

    for dependency_id, upstream_script_id, upstream_derivation_id, expected_record_kind in dependencies:
        ns.declare_dependency(
            dependency_id=dependency_id,
            upstream_script_id=upstream_script_id,
            upstream_derivation_id=upstream_derivation_id,
            expected_record_kind=expected_record_kind,
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
    P_trace_norm: sp.Symbol
    P_safe_membership: sp.Symbol
    P_guardrail_visibility: sp.Symbol
    P_div_explicitness: sp.Symbol
    P_source_no_hidden: sp.Symbol
    P_incidence_zero: sp.Symbol
    P_active_O: sp.Symbol
    P_residual_kill: sp.Symbol
    P_insertion: sp.Symbol
    P_parent: sp.Symbol
    L_package_B_audit: sp.Expr
    L_adoption_boundary: sp.Expr
    L_downstream_closed: sp.Expr
    L_open_theorem_burden: sp.Expr
    L_group32_summary: sp.Expr


@dataclass
class Group32StatusEntry:
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
    status: str
    reason: str


@dataclass
class SummaryConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


@dataclass
class SummaryObligation:
    name: str
    obligation: str
    status: str
    blocks: str
    discipline: str


def build_symbols() -> SummarySymbols:
    (
        P_trace_norm,
        P_safe_membership,
        P_guardrail_visibility,
        P_div_explicitness,
        P_source_no_hidden,
        P_incidence_zero,
        P_active_O,
        P_residual_kill,
        P_insertion,
        P_parent,
    ) = sp.symbols(
        "P_trace_norm P_safe_membership P_guardrail_visibility P_div_explicitness "
        "P_source_no_hidden P_incidence_zero P_active_O P_residual_kill P_insertion P_parent",
        real=True,
    )

    L_package_B_audit = sp.simplify(
        P_trace_norm
        + P_safe_membership
        + P_guardrail_visibility
        + P_div_explicitness
        + P_source_no_hidden
    )
    L_adoption_boundary = sp.simplify(P_trace_norm + P_safe_membership)
    L_downstream_closed = sp.simplify(P_active_O + P_residual_kill + P_insertion + P_parent)
    L_open_theorem_burden = sp.simplify(
        P_incidence_zero + P_active_O + P_residual_kill + P_insertion + P_parent
    )
    L_group32_summary = sp.simplify(L_package_B_audit + L_open_theorem_burden)

    return SummarySymbols(
        P_trace_norm=P_trace_norm,
        P_safe_membership=P_safe_membership,
        P_guardrail_visibility=P_guardrail_visibility,
        P_div_explicitness=P_div_explicitness,
        P_source_no_hidden=P_source_no_hidden,
        P_incidence_zero=P_incidence_zero,
        P_active_O=P_active_O,
        P_residual_kill=P_residual_kill,
        P_insertion=P_insertion,
        P_parent=P_parent,
        L_package_B_audit=L_package_B_audit,
        L_adoption_boundary=L_adoption_boundary,
        L_downstream_closed=L_downstream_closed,
        L_open_theorem_burden=L_open_theorem_burden,
        L_group32_summary=L_group32_summary,
    )


def build_status_entries() -> List[Group32StatusEntry]:
    return [
        Group32StatusEntry(
            name="G32-1: explicit-choice route opener",
            topic="Group 32 opened the explicit minimal postulate selection route",
            status="EXPLICIT_CHOICE_AUDIT",
            result="route opened after Group 31 closed as partial-constraint result",
            boundary="opener adopted no postulate and derived no insertion",
        ),
        Group32StatusEntry(
            name="G32-2: candidate postulate ledger",
            topic="fresh candidates and inherited disciplines were separated",
            status="SUMMARY",
            result="trace normalization and safe membership remain fresh candidates; guardrail visibility, divergence explicitness, and source-hidden exclusion carry inherited/discipline status",
            boundary="candidate survival is not adoption",
        ),
        Group32StatusEntry(
            name="G32-3: dependency graph",
            topic="valid prerequisite edges and forbidden implication edges were mapped",
            status="REQUIRED",
            result="normalization is not membership; membership is not incidence or active O; visibility is not neutrality; explicitness is not divergence-safe law",
            boundary="dependency edge is not proof edge",
        ),
        Group32StatusEntry(
            name="G32-4: package sieve",
            topic="package families were classified before selection",
            status="SUMMARY",
            result="Package A likely insufficient; Package B plausible to audit; Package C high-risk; Package D rejected as current shortcut; Packages E/F insufficient",
            boundary="sieve classification is not selection, adoption, or recommendation",
        ),
        Group32StatusEntry(
            name="G32-5: package minimality accounting",
            topic="Package B tested under current trace-anchor audit criteria",
            status="MINIMAL_PLAUSIBLE_TO_AUDIT",
            result="Package B is minimal plausible-to-audit under current criteria",
            boundary="full phrase required: not selected, not adopted, not recommended for adoption",
        ),
        Group32StatusEntry(
            name="G32-6: downstream gates",
            topic="incidence, active O, residual kill, insertion, and parent closure",
            status="NOT_READY",
            result="all downstream gates remain closed",
            boundary="Group 32 does not license downstream theorem closure",
        ),
    ]


def build_final_gaps() -> List[FinalGap]:
    return [
        FinalGap(
            name="G1: adoption decision",
            status="OPEN",
            reason="Package B is minimal plausible-to-audit only; no adoption has occurred",
            discipline="requires separate explicit user/theory decision",
        ),
        FinalGap(
            name="G2: trace normalization",
            status="CANDIDATE_REMAINS",
            reason="normalization role is required for audit but not derived or chosen",
            discipline="do not select from recovery or repair",
        ),
        FinalGap(
            name="G3: safe trace membership",
            status="CANDIDATE_REMAINS",
            reason="membership is required for audit but not derived or chosen",
            discipline="membership is not incidence, active O, residual kill, or insertion",
        ),
        FinalGap(
            name="G4: source no-double-counting theorem",
            status="NOT_DERIVED",
            reason="P_source_no_hidden carries inherited partial constraint only",
            discipline="hidden-pocket exclusion is not full source theorem",
        ),
        FinalGap(
            name="G5: divergence-safe coefficient law",
            status="NOT_DERIVED",
            reason="divergence explicitness is weaker than divergence safety",
            discipline="visible correction is not conservation compatibility",
        ),
        FinalGap(
            name="G6: trace/residual incidence",
            status="HIGH_RISK",
            reason="zero incidence remains too close to no-overlap/residual-control smuggling",
            discipline="do not fold incidence into safe membership or Package B",
        ),
        FinalGap(
            name="G7: B_s/F_zeta insertion",
            status="NOT_READY",
            reason="normalization, membership, incidence, coefficient-law, no-overlap, and residual gates remain open",
            discipline="minimal plausible-to-audit package is not insertion",
        ),
        FinalGap(
            name="G8: active O / residual control / parent closure",
            status="NOT_READY",
            reason="active O is not constructed, residual kill is not derived, and parent equation is not ready",
            discipline="all downstream gates remain closed",
        ),
    ]


def build_handoffs() -> List[FinalHandoff]:
    return [
        FinalHandoff(
            name="H1: explicit adoption decision",
            status="OPEN",
            reason="Package B is minimal plausible-to-audit, but adoption is still a separate theory decision",
            caution="must record adoption explicitly and must not call adopted postulates derived",
        ),
        FinalHandoff(
            name="H2: trace-normalization choice or theorem route",
            status="OPEN",
            reason="P_trace_norm remains a candidate/theorem target",
            caution="must not be recovery-selected, repair-selected, insertion-selected, or parent-fit selected",
        ),
        FinalHandoff(
            name="H3: safe-membership choice or theorem route",
            status="OPEN",
            reason="P_safe_membership remains a candidate/theorem target",
            caution="must not imply incidence, no-overlap geometry, residual kill, active O, or insertion",
        ),
        FinalHandoff(
            name="H4: trace-anchor insertion-precondition inventory",
            status="CONDITIONAL",
            reason="may be useful only after explicit adoption or theorem support clarifies trace anchor status",
            caution="precondition inventory is not insertion and cannot open parent closure",
        ),
        FinalHandoff(
            name="H5: B_s/F_zeta insertion theorem",
            status="NOT_READY",
            reason="upstream trace-anchor, incidence, coefficient-law, no-overlap, and residual gates remain open",
            caution="forbidden as immediate theorem route from Group 32 alone",
        ),
        FinalHandoff(
            name="H6: parent field equation",
            status="NOT_READY",
            reason="scalar recombination and downstream gates remain unresolved",
            caution="parent gate remains closed",
        ),
    ]


def build_rejected_upgrades() -> List[RejectedUpgrade]:
    return [
        RejectedUpgrade(
            name="R1: minimal plausible-to-audit as adoption",
            upgrade="shorten Package B status into adoption, selection, or recommendation",
            status="POLICY_RULE",
            reason="minimality accounting is not explicit choice",
        ),
        RejectedUpgrade(
            name="R2: removal tests as physical proof",
            upgrade="treat necessary-for-audit components as derived physical postulates",
            status="POLICY_RULE",
            reason="removal tests are criteria-based, not physics derivations",
        ),
        RejectedUpgrade(
            name="R3: inherited discipline as fresh theorem",
            upgrade="treat P_source_no_hidden as full source no-double-counting theorem",
            status="POLICY_RULE",
            reason="Group 31 ruled out hidden pockets but did not derive full source theorem",
        ),
        RejectedUpgrade(
            name="R4: safe membership as incidence",
            upgrade="treat zeta_Bs -> T_zeta as zero trace/residual incidence",
            status="POLICY_RULE",
            reason="incidence is high-risk and separate from membership",
        ),
        RejectedUpgrade(
            name="R5: Package B as insertion",
            upgrade="treat Package B as B_s/F_zeta insertion or coefficient law",
            status="POLICY_RULE",
            reason="Package B can at most prepare later precondition audits",
        ),
        RejectedUpgrade(
            name="R6: Package B as parent closure",
            upgrade="open parent equation from minimal plausible-to-audit status",
            status="POLICY_RULE",
            reason="parent gate remains closed",
        ),
    ]


def build_obligations() -> List[SummaryObligation]:
    return [
        SummaryObligation(
            name="O1: preserve full Package B status phrase",
            obligation="record Package B as minimal plausible-to-audit only",
            status="OPEN",
            blocks="adoption drift",
            discipline="do not shorten to minimal, selected, adopted, or recommended",
        ),
        SummaryObligation(
            name="O2: adoption remains explicit",
            obligation="require separate explicit user/theory decision before any postulate adoption",
            status="OPEN",
            blocks="accidental adoption",
            discipline="candidate survival and minimality accounting are not adoption",
        ),
        SummaryObligation(
            name="O3: theorem targets remain theorem targets",
            obligation="keep trace normalization, membership, incidence, source theorem, and divergence safety unresolved unless derived or adopted explicitly",
            status="OPEN",
            blocks="theorem overclaim",
            discipline="do not turn audit criteria into derivations",
        ),
        SummaryObligation(
            name="O4: downstream gates remain closed",
            obligation="keep insertion, active O, residual control, and parent closure closed after Group 32",
            status="NOT_READY",
            blocks="downstream overreach",
            discipline="Group 32 is not insertion or parent readiness",
        ),
        SummaryObligation(
            name="O5: future handoff must state adoption condition",
            obligation="any Group 33 or later route must say whether Package B was explicitly adopted, deferred, or only audited",
            status="OPEN",
            blocks="ambiguous handoff",
            discipline="handoff cannot treat audit status as theory status",
        ),
    ]


def build_conclusions() -> List[SummaryConclusion]:
    return [
        SummaryConclusion(
            name="C1: Group 32 result",
            conclusion="Group 32 completed an explicit-choice audit, not an adoption event",
            status="EXPLICIT_CHOICE_AUDIT",
            meaning="the group classified choices and packages without choosing them",
        ),
        SummaryConclusion(
            name="C2: Package B status",
            conclusion="Package B is minimal plausible-to-audit under current trace-anchor criteria",
            status="MINIMAL_PLAUSIBLE_TO_AUDIT",
            meaning="full phrase required; this is not selected, adopted, or recommended",
        ),
        SummaryConclusion(
            name="C3: candidate status",
            conclusion="trace normalization and safe membership remain candidates, not derived or adopted postulates",
            status="CANDIDATE_REMAINS",
            meaning="a separate explicit decision or theorem route is still required",
        ),
        SummaryConclusion(
            name="C4: inherited discipline status",
            conclusion="source-hidden exclusion remains inherited partial constraint, not full source no-double-counting theorem",
            status="INHERITED_DISCIPLINE",
            meaning="it participates in audit accounting but is not fresh automatic adoption",
        ),
        SummaryConclusion(
            name="C5: downstream gates",
            conclusion="incidence, active O, residual kill, B_s/F_zeta insertion, and parent closure remain not ready",
            status="NOT_READY",
            meaning="Group 32 does not open downstream gates",
        ),
        SummaryConclusion(
            name="C6: next",
            conclusion="future work requires explicit adoption decision or separate theorem routes before insertion-precondition work can be treated as licensed",
            status="OPEN",
            meaning="do not name a Group 33 insertion route unless the adoption/theorem status is explicit",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Group 32 status summary problem")
    print("Question:")
    print()
    print("  What did Group 32 establish, and what remains outside the adoption boundary?")
    print()
    print("Discipline:")
    print()
    print("  This script summarizes Group 32.")
    print("  It adopts no postulate.")
    print("  It recommends no adoption.")
    print("  It does not select Package B.")
    print("  It derives no coefficient law and no insertion.")
    print("  It keeps active O, residual control, and parent closure closed.")
    print()
    print("Tiny goblin rule:")
    print("  Count the teeth. Close the mouth. The bite is still a choice.")

    with out.governance_assessments():
        out.line(
            "Group 32 status summary opened",
            StatusMark.INFO,
            "closing explicit-choice audit while preserving no-adoption boundary",
        )


def case_1_symbolic_summary(symbols: SummarySymbols, out: ScriptOutput) -> None:
    header("Case 1: Group 32 symbolic summary loads")
    print("Candidate symbols:")
    print()
    for name in (
        "P_trace_norm",
        "P_safe_membership",
        "P_guardrail_visibility",
        "P_div_explicitness",
        "P_source_no_hidden",
        "P_incidence_zero",
        "P_active_O",
        "P_residual_kill",
        "P_insertion",
        "P_parent",
    ):
        print(f"  {name} = {getattr(symbols, name)}")

    print()
    print("Package B audit load:")
    print(f"  L_package_B_audit = {symbols.L_package_B_audit}")
    print()
    print("Adoption-boundary load:")
    print(f"  L_adoption_boundary = {symbols.L_adoption_boundary}")
    print()
    print("Downstream closed load:")
    print(f"  L_downstream_closed = {symbols.L_downstream_closed}")
    print()
    print("Open theorem burden:")
    print(f"  L_open_theorem_burden = {symbols.L_open_theorem_burden}")
    print()
    print("Group 32 summary load:")
    print(f"  L_group32_summary = {symbols.L_group32_summary}")

    with out.derived_results():
        out.line(
            "Group 32 symbolic summary loads stated",
            StatusMark.OBLIGATION,
            f"L_package_B_audit = {symbols.L_package_B_audit}; L_downstream_closed = {symbols.L_downstream_closed}",
        )


def case_2_status_entries(entries: List[Group32StatusEntry], out: ScriptOutput) -> None:
    header("Case 2: Group 32 status entries")

    for item in entries:
        subheader(item.name)
        print(f"Topic: {item.topic}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Result: {item.result}")
        print(f"Boundary: {item.boundary}")

    with out.governance_assessments():
        out.line(
            "Group 32 status entries stated",
            StatusMark.INFO,
            f"{len(entries)} status entries stated",
        )


def case_3_final_gaps(gaps: List[FinalGap], out: ScriptOutput) -> None:
    header("Case 3: Final open gaps")

    for item in gaps:
        subheader(item.name)
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Reason: {item.reason}")
        print(f"Discipline: {item.discipline}")

    with out.unresolved_obligations():
        out.line(
            "Group 32 final gaps stated",
            StatusMark.OBLIGATION,
            f"{len(gaps)} gaps remain open or not ready",
        )


def case_4_final_handoffs(handoffs: List[FinalHandoff], out: ScriptOutput) -> None:
    header("Case 4: Final handoffs")

    for item in handoffs:
        subheader(item.name)
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Reason: {item.reason}")
        print(f"Caution: {item.caution}")

    with out.governance_assessments():
        out.line(
            "Group 32 handoffs stated",
            StatusMark.DEFER,
            f"{len(handoffs)} handoffs stated; adoption condition remains explicit",
        )


def case_5_rejected_upgrades(upgrades: List[RejectedUpgrade], out: ScriptOutput) -> None:
    header("Case 5: Rejected summary upgrades")

    for item in upgrades:
        subheader(item.name)
        print(f"Upgrade: {item.upgrade}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Reason: {item.reason}")

    with out.governance_assessments():
        out.line(
            "Group 32 summary upgrades rejected",
            StatusMark.OBLIGATION,
            f"{len(upgrades)} upgrade shortcuts rejected as policy rules",
        )


def case_6_obligations(obligations: List[SummaryObligation], out: ScriptOutput) -> None:
    header("Case 6: Group 32 final obligations")

    for item in obligations:
        subheader(item.name)
        print(f"Obligation: {item.obligation}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Blocks: {item.blocks}")
        print(f"Discipline: {item.discipline}")

    with out.unresolved_obligations():
        out.line(
            "Group 32 final obligations opened",
            StatusMark.OBLIGATION,
            f"{len(obligations)} obligations stated",
        )


def case_7_conclusions(conclusions: List[SummaryConclusion], out: ScriptOutput) -> None:
    header("Case 7: Group 32 conclusions")

    for item in conclusions:
        subheader(item.name)
        print(f"Conclusion: {item.conclusion}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Meaning: {item.meaning}")

    with out.governance_assessments():
        out.line(
            "Group 32 status summary conclusion stated",
            StatusMark.PASS,
            "explicit-choice audit complete; Package B minimal plausible-to-audit only; no postulate adopted",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Group 32 status summary result:")
    print()
    print("  Group 32 completed an explicit-choice audit, not an adoption event.")
    print("  Package B is minimal plausible-to-audit under the current trace-anchor criteria.")
    print("  Package B is not selected, not adopted, and not recommended for adoption.")
    print("  Trace normalization and safe membership remain candidates, not derived or adopted postulates.")
    print("  Source hidden-pocket exclusion remains inherited partial constraint, not full source no-double-counting theorem.")
    print("  Divergence explicitness remains discipline, not divergence-safe coefficient law.")
    print("  Trace/residual incidence remains high-risk and separate.")
    print("  Active O, residual kill, B_s/F_zeta insertion, and parent closure remain not ready.")
    print("  Any future adoption requires a separate explicit user/theory decision.")
    print()
    print("Possible next step:")
    print("  explicit adoption decision record, trace-normalization/safe-membership theorem route, or conditional trace-anchor precondition inventory")
    print()
    print("Tiny goblin label:")
    print("  Count the teeth. Close the mouth. The bite is still a choice.")

    with out.governance_assessments():
        out.line(
            "candidate Group 32 status summary complete",
            StatusMark.PASS,
            "explicit-choice audit closed; adoption remains separate; downstream gates closed",
        )


def record_inventory_marker(ns, symbols: SummarySymbols) -> None:
    ns.record_derivation(
        derivation_id="g32_status_summary",
        inputs=[
            symbols.P_trace_norm,
            symbols.P_safe_membership,
            symbols.P_guardrail_visibility,
            symbols.P_div_explicitness,
            symbols.P_source_no_hidden,
            symbols.P_incidence_zero,
            symbols.P_active_O,
            symbols.P_residual_kill,
            symbols.P_insertion,
            symbols.P_parent,
        ],
        output=symbols.L_group32_summary,
        method="summarize Group 32 explicit-choice audit and adoption-boundary status",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="group_32_status_summary_marker",
        scope="Group 32 explicit minimal postulate selection",
        is_placeholder=True,
    )


def record_obligations(ns, obligations: List[SummaryObligation]) -> None:
    obligation_id_map = {
        "O1: preserve full Package B status phrase": "g32_summary_preserve_package_b_status_phrase",
        "O2: adoption remains explicit": "g32_summary_adoption_remains_explicit",
        "O3: theorem targets remain theorem targets": "g32_summary_theorem_targets_remain_open",
        "O4: downstream gates remain closed": "g32_summary_downstream_gates_closed",
        "O5: future handoff must state adoption condition": "g32_summary_future_handoff_adoption_condition",
    }

    for item in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id_map[item.name],
            script_id=SCRIPT_ID,
            title=item.obligation,
            status=ObligationStatus.OPEN,
            required_by=["g32_status_summary"],
            description=f"{item.discipline} Blocks: {item.blocks}.",
        ))


def record_governance(
    ns,
    status_entries: List[Group32StatusEntry],
    gaps: List[FinalGap],
    handoffs: List[FinalHandoff],
    upgrades: List[RejectedUpgrade],
) -> None:
    obligation_ids = [
        "g32_summary_preserve_package_b_status_phrase",
        "g32_summary_adoption_remains_explicit",
        "g32_summary_theorem_targets_remain_open",
        "g32_summary_downstream_gates_closed",
        "g32_summary_future_handoff_adoption_condition",
    ]

    ns.record_route(RouteRecord(
        route_id="g32_explicit_choice_audit_summary_route",
        script_id=SCRIPT_ID,
        name="Group 32 explicit-choice audit summary route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "explicit-selection opener completed",
            "candidate ledger completed",
            "dependency graph completed",
            "package sieve completed",
            "package minimality accounting completed",
            "adoption remains separate",
        ],
    ))

    for item in status_entries:
        status = GovernanceStatus.POLICY_RULE
        if item.status in {"EXPLICIT_CHOICE_AUDIT", "SUMMARY", "MINIMAL_PLAUSIBLE_TO_AUDIT"}:
            status = GovernanceStatus.CANDIDATE_ROUTE
        elif item.status == "NOT_READY":
            status = GovernanceStatus.DEFERRED_PENDING_PREREQUISITES

        ns.record_claim(ClaimRecord(
            claim_id=f"g32_status_entry_{item.name.split(':')[0].lower().replace('-', '_')}",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=status,
            statement=f"{item.topic}. Result: {item.result}. Boundary: {item.boundary}.",
            derivation_ids=["g32_status_summary"],
            obligation_ids=obligation_ids,
        ))

    for item in gaps:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=f"g32_final_gap_{item.name.split(':')[0].lower()}",
            script_id=SCRIPT_ID,
            title=f"{item.name}: {item.reason}",
            status=ObligationStatus.OPEN,
            required_by=["g32_status_summary"],
            description=f"{item.discipline}",
        ))

    for item in handoffs:
        ns.record_claim(ClaimRecord(
            claim_id=f"g32_handoff_{item.name.split(':')[0].lower()}",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.CANDIDATE_ROUTE if item.status in {"OPEN", "CONDITIONAL"} else GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
            statement=f"{item.name}: {item.reason}. Caution: {item.caution}.",
            derivation_ids=["g32_status_summary"],
            obligation_ids=obligation_ids,
        ))

    for item in upgrades:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"g32_rejected_upgrade_{item.name.split(':')[0].lower()}",
            script_id=SCRIPT_ID,
            branch_id=item.upgrade,
            status=GovernanceStatus.POLICY_RULE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"{item.upgrade}. Reason: {item.reason}.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g32_status_summary_complete",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Group 32 is closed as an explicit-choice audit. Package B is minimal plausible-to-audit under current trace-anchor criteria, "
            "but is not selected, adopted, or recommended for adoption. Trace normalization and safe membership remain candidates. "
            "Downstream gates remain closed."
        ),
        derivation_ids=["g32_status_summary"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Group 32 Status Summary")
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
    case_6_obligations(obligations, out)
    case_7_conclusions(conclusions, out)
    final_interpretation(out)

    record_inventory_marker(ns, symbols)
    record_obligations(ns, obligations)
    record_governance(ns, status_entries, final_gaps, handoffs, rejected_upgrades)

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
