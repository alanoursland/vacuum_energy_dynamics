# Candidate trace-normalization obligations
#
# Group:
#   33_trace_normalization_candidate_origin
#
# Human title:
#   Trace Normalization Candidate Origin
#
# Script type:
#   OBLIGATIONS / STATUS BRIDGE
#
# Purpose
# -------
# Summarize the surviving trace-normalization candidate forms, failed forms,
# unresolved convention decisions, and safe handoffs before the Group 33 status
# summary.
#
# Locked-door question:
#
#   What trace-normalization obligations remain after the compatibility sieve,
#   and what can safely be handed off without selecting or adopting N_trace?
#
# This script does not choose N_trace.
# It does not adopt a trace-normalization postulate.
# It does not derive a trace-normalization theorem.
# It does not derive B_s/F_zeta insertion.
# It does not open active O, residual control, or parent closure.
#
# Tiny goblin rule:
#
#   Count the cups. Still no drinking.

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
        "COMPATIBLE_IF_DECLARED": StatusMark.INFO,
        "CONVENTION_DEPENDENT": StatusMark.DEFER,
        "FILTER_FAIL": StatusMark.FAIL,
        "HANDOFF_READY": StatusMark.INFO,
        "LINEARIZED_ONLY": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REQUIRED": StatusMark.OBLIGATION,
        "SUMMARY": StatusMark.INFO,
        "THEOREM_TARGET": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g33_compatibility_sieve",
            "033_trace_normalization_candidate_origin__candidate_trace_normalization_compatibility_sieve",
            "g33_trace_normalization_compatibility_sieve",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g33_candidate_forms",
            "033_trace_normalization_candidate_origin__candidate_trace_normalization_candidate_forms",
            "g33_trace_normalization_candidate_forms",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g33_selector_firewall",
            "033_trace_normalization_candidate_origin__candidate_trace_normalization_selector_rejection",
            "g33_trace_normalization_selector_rejection",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g33_volume_trace",
            "033_trace_normalization_candidate_origin__candidate_trace_normalization_volume_trace_ledger",
            "g33_trace_normalization_volume_trace_ledger",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g33_origin_problem",
            "033_trace_normalization_candidate_origin__candidate_trace_normalization_origin_problem",
            "g33_trace_normalization_origin_problem",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g32_summary",
            "032_explicit_minimal_postulate_selection__candidate_group_32_status_summary",
            "g32_status_summary",
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
class ObligationSymbols:
    N_trace: sp.Symbol
    N_scale: sp.Expr
    N_metric: sp.Expr
    N_perdim_scale: sp.Expr
    N_perdim_metric: sp.Expr
    L_surviving_forms: sp.Expr
    L_failed_modes: sp.Expr
    L_open_decisions: sp.Expr
    L_downstream_closed: sp.Expr
    L_obligation_gap: sp.Expr


@dataclass
class SurvivingFormEntry:
    name: str
    form: str
    status: str
    survives_if: str
    remaining_decision: str
    boundary: str


@dataclass
class FailureModeEntry:
    name: str
    failure: str
    status: str
    reason: str
    consequence: str


@dataclass
class OpenDecisionEntry:
    name: str
    decision: str
    status: str
    blocks: str
    discipline: str


@dataclass
class HandoffEntry:
    name: str
    handoff: str
    status: str
    reason: str
    caution: str


@dataclass
class TraceObligationEntry:
    name: str
    obligation: str
    status: str
    blocks: str
    discipline: str


def case_0_problem(out: ScriptOutput) -> None:
    header("Case 0: Trace-normalization obligations problem")

    print("Question:")
    print()
    print("  What trace-normalization obligations remain after the compatibility sieve,")
    print("  and what can safely be handed off without selecting or adopting N_trace?")
    print()
    print("Discipline:")
    print()
    print("  This script summarizes obligations.")
    print("  It adopts no trace-normalization postulate.")
    print("  It selects no final normalization.")
    print("  It derives no trace-normalization theorem.")
    print("  It derives no coefficient law and no insertion.")
    print("  It keeps active O, residual control, and parent closure closed.")
    print()
    print("Tiny goblin rule:")
    print("  Count the cups. Still no drinking.")

    with out.governance_assessments():
        out.line(
            "trace-normalization obligations summary opened",
            StatusMark.INFO,
            "summarizing surviving forms, failed filters, open decisions, and safe handoffs",
        )


def case_1_symbolic_ledger(out: ScriptOutput) -> ObligationSymbols:
    header("Case 1: Obligations symbolic ledger")

    zeta, zeta_pd, d = sp.symbols("zeta zeta_pd d", nonzero=True)
    N_trace = sp.Symbol("N_trace")

    N_scale = sp.simplify(zeta / d)
    N_metric = sp.simplify(2 * zeta / d)
    N_perdim_scale = zeta_pd
    N_perdim_metric = 2 * zeta_pd

    O_Bs_decl, O_zeta_decl, O_d_decl = sp.symbols("O_Bs_decl O_zeta_decl O_d_decl")
    F_hidden_source, F_hidden_div, F_membership_collapse, F_linearized_upgrade = sp.symbols(
        "F_hidden_source F_hidden_div F_membership_collapse F_linearized_upgrade"
    )
    P_active_O, P_insertion, P_parent, P_residual_kill = sp.symbols(
        "P_active_O P_insertion P_parent P_residual_kill"
    )

    L_surviving_forms = sp.simplify(N_scale + N_metric + N_perdim_scale + N_perdim_metric)
    L_failed_modes = sp.simplify(F_hidden_source + F_hidden_div + F_membership_collapse + F_linearized_upgrade)
    L_open_decisions = sp.simplify(O_Bs_decl + O_zeta_decl + O_d_decl)
    L_downstream_closed = sp.simplify(P_active_O + P_insertion + P_parent + P_residual_kill)
    L_obligation_gap = sp.simplify(
        N_trace + L_surviving_forms + L_failed_modes + L_open_decisions + L_downstream_closed
    )

    print("Candidate / decision / gate symbols:")
    for name, value in [
        ("N_trace", N_trace),
        ("N_scale", N_scale),
        ("N_metric", N_metric),
        ("N_perdim_scale", N_perdim_scale),
        ("N_perdim_metric", N_perdim_metric),
        ("O_Bs_decl", O_Bs_decl),
        ("O_zeta_decl", O_zeta_decl),
        ("O_d_decl", O_d_decl),
    ]:
        print(f"\n  {name} = {value}")

    print()
    print(f"Surviving-form load:\n  L_surviving_forms = {L_surviving_forms}")
    print()
    print(f"Failed-mode load:\n  L_failed_modes = {L_failed_modes}")
    print()
    print(f"Open-decision load:\n  L_open_decisions = {L_open_decisions}")
    print()
    print(f"Downstream closed load:\n  L_downstream_closed = {L_downstream_closed}")
    print()
    print(f"Obligation gap:\n  L_obligation_gap = {L_obligation_gap}")

    with out.derived_results():
        out.line(
            "trace-normalization obligation loads stated",
            StatusMark.OBLIGATION,
            f"L_open_decisions={L_open_decisions}; L_downstream_closed={L_downstream_closed}",
        )

    return ObligationSymbols(
        N_trace=N_trace,
        N_scale=N_scale,
        N_metric=N_metric,
        N_perdim_scale=N_perdim_scale,
        N_perdim_metric=N_perdim_metric,
        L_surviving_forms=L_surviving_forms,
        L_failed_modes=L_failed_modes,
        L_open_decisions=L_open_decisions,
        L_downstream_closed=L_downstream_closed,
        L_obligation_gap=L_obligation_gap,
    )


def build_surviving_forms() -> List[SurvivingFormEntry]:
    return [
        SurvivingFormEntry(
            name="S1: scale-factor volume-log form",
            form="log(B_s)=zeta/d",
            status="COMPATIBLE_IF_DECLARED",
            survives_if="B_s is scale-factor language, zeta is total volume-log trace, and d is declared before recovery",
            remaining_decision="declare whether B_s is actually scale-factor language in the next theory step",
            boundary="survival is not selection, adoption, coefficient law, or insertion",
        ),
        SurvivingFormEntry(
            name="S2: metric-coefficient volume-log form",
            form="log(B_s)=2*zeta/d",
            status="COMPATIBLE_IF_DECLARED",
            survives_if="B_s is metric-coefficient language, zeta is total volume-log trace, and d is declared before recovery",
            remaining_decision="declare whether B_s denotes metric coefficient response in the next theory step",
            boundary="survival is not residual control, active O, or insertion",
        ),
        SurvivingFormEntry(
            name="S3: per-dimension zeta scale form",
            form="log(B_s)=zeta_pd",
            status="CONVENTION_DEPENDENT",
            survives_if="zeta_pd is explicitly declared as zeta_total/d and B_s is scale-factor language",
            remaining_decision="declare whether zeta notation already includes the dimension factor",
            boundary="notation equivalence must not hide the dimension factor",
        ),
        SurvivingFormEntry(
            name="S4: per-dimension zeta metric form",
            form="log(B_s)=2*zeta_pd",
            status="CONVENTION_DEPENDENT",
            survives_if="zeta_pd is explicitly declared as zeta_total/d and B_s is metric-coefficient language",
            remaining_decision="declare both zeta convention and B_s object convention",
            boundary="notation convention is not exact insertion law",
        ),
        SurvivingFormEntry(
            name="S5: linearized trace-only form",
            form="first-order delta ln sqrt(gamma) = 1/2 tr(h)",
            status="LINEARIZED_ONLY",
            survives_if="scope is explicitly first-order and perturbative variables are declared",
            remaining_decision="keep linearized bookkeeping separate from exact determinant/coefficient claims",
            boundary="linearized consistency is not exact theorem support",
        ),
    ]


def case_2_surviving_forms(out: ScriptOutput) -> List[SurvivingFormEntry]:
    header("Case 2: Surviving candidate forms")

    entries = build_surviving_forms()
    for item in entries:
        subheader(item.name)
        print(f"Form: {item.form}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Survives if: {item.survives_if}")
        print(f"Remaining decision: {item.remaining_decision}")
        print(f"Boundary: {item.boundary}")

    with out.governance_assessments():
        out.line(
            "surviving forms summarized",
            StatusMark.DEFER,
            "forms survive conditionally; none selected or adopted",
        )
    return entries


def build_failure_modes() -> List[FailureModeEntry]:
    return [
        FailureModeEntry(
            name="F1: undeclared B_s convention",
            failure="candidate form does not declare whether B_s is scale factor, metric coefficient, or separate functional response",
            status="FILTER_FAIL",
            reason="scale-factor and metric-coefficient conventions differ by a factor of two",
            consequence="form cannot be classified",
        ),
        FailureModeEntry(
            name="F2: undeclared zeta convention",
            failure="candidate form does not declare total volume-log trace versus per-dimension trace",
            status="FILTER_FAIL",
            reason="per-dimension notation can hide the dimension factor",
            consequence="normalization remains ambiguous",
        ),
        FailureModeEntry(
            name="F3: undeclared traced dimension",
            failure="candidate form uses zeta/d or 2*zeta/d without declaring d",
            status="FILTER_FAIL",
            reason="dimension count must be declared before recovery checks",
            consequence="dimensional route remains unavailable",
        ),
        FailureModeEntry(
            name="F4: hidden source dependence",
            failure="candidate form carries ordinary source load or source repair in normalization",
            status="FILTER_FAIL",
            reason="hidden source load is forbidden by inherited discipline",
            consequence="candidate violates source no-hidden discipline",
        ),
        FailureModeEntry(
            name="F5: hidden divergence reservoir",
            failure="candidate form requires hidden correction/divergence reservoir behavior",
            status="FILTER_FAIL",
            reason="divergence explicitness is non-reservoir discipline",
            consequence="candidate violates explicitness filter",
        ),
        FailureModeEntry(
            name="F6: membership collapse",
            failure="candidate form treats normalization as automatically giving safe membership or incidence",
            status="FILTER_FAIL",
            reason="normalization and membership remain separate candidate nodes",
            consequence="candidate smuggles Package B collapse or residual control",
        ),
        FailureModeEntry(
            name="F7: linearized exact-upgrade",
            failure="linearized trace relation is used as exact nonlinear coefficient law",
            status="FILTER_FAIL",
            reason="first-order consistency is not exact theorem support",
            consequence="candidate overclaims scope",
        ),
    ]


def case_3_failure_modes(out: ScriptOutput) -> List[FailureModeEntry]:
    header("Case 3: Failed forms and filter failures")

    entries = build_failure_modes()
    for item in entries:
        subheader(item.name)
        print(f"Failure: {item.failure}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Reason: {item.reason}")
        print(f"Consequence: {item.consequence}")

    with out.counterexamples():
        out.line(
            "failed compatibility modes summarized",
            StatusMark.FAIL,
            "ambiguous conventions, hidden loads, membership collapse, and exact-upgrade fail",
        )
    return entries


def build_open_decisions() -> List[OpenDecisionEntry]:
    return [
        OpenDecisionEntry(
            name="D1: B_s object convention",
            decision="decide whether B_s is scale-factor language, metric-coefficient language, or separate functional response",
            status="OPEN",
            blocks="candidate narrowing and any future trace-normalization choice",
            discipline="object convention must be declared before coefficient claims",
        ),
        OpenDecisionEntry(
            name="D2: zeta trace convention",
            decision="decide whether zeta is total volume-log trace or per-dimension normalized trace",
            status="OPEN",
            blocks="notation-equivalence and dimension accounting",
            discipline="do not hide dimension factor in notation",
        ),
        OpenDecisionEntry(
            name="D3: traced sector dimension",
            decision="state the traced sector dimension d and whether it is spatial, reduced radial, or another sector",
            status="OPEN",
            blocks="zeta/d and 2*zeta/d forms",
            discipline="dimension count cannot be recovery-selected",
        ),
        OpenDecisionEntry(
            name="D4: exact versus linearized scope",
            decision="decide whether a candidate is exact determinant/volume convention or first-order only",
            status="OPEN",
            blocks="theorem claims and compatibility interpretation",
            discipline="linearized success is not exact law",
        ),
        OpenDecisionEntry(
            name="D5: adoption boundary",
            decision="whether to explicitly adopt P_trace_norm remains a separate user/theory decision",
            status="OPEN",
            blocks="postulate use downstream",
            discipline="obligations summary is not adoption",
        ),
    ]


def case_4_open_decisions(out: ScriptOutput) -> List[OpenDecisionEntry]:
    header("Case 4: Open convention decisions")

    entries = build_open_decisions()
    for item in entries:
        subheader(item.name)
        print(f"Decision: {item.decision}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Blocks: {item.blocks}")
        print(f"Discipline: {item.discipline}")

    with out.unresolved_obligations():
        out.line(
            "open convention decisions summarized",
            StatusMark.OBLIGATION,
            "B_s object, zeta convention, traced dimension, scope, and adoption boundary remain open",
        )
    return entries


def build_handoffs() -> List[HandoffEntry]:
    return [
        HandoffEntry(
            name="H1: Group 33 status summary",
            handoff="candidate_group_33_status_summary.py",
            status="HANDOFF_READY",
            reason="compatibility sieve has enough information to summarize surviving forms and open decisions",
            caution="summary must not select or adopt N_trace",
        ),
        HandoffEntry(
            name="H2: explicit trace-normalization decision",
            handoff="explicit adoption decision record",
            status="OPEN",
            reason="P_trace_norm remains candidate if the theory owner wants to choose it explicitly",
            caution="adopted postulate must not be called derived",
        ),
        HandoffEntry(
            name="H3: trace-normalization theorem route",
            handoff="theorem attempt for one declared convention",
            status="OPEN",
            reason="surviving forms are conditional and may still be theorem targets",
            caution="must declare conventions before theorem attempt",
        ),
        HandoffEntry(
            name="H4: safe-membership compatibility continuation",
            handoff="safe membership route after conventions are declared",
            status="OPEN",
            reason="normalization and membership remain separate Package B nodes",
            caution="membership must not imply incidence, residual kill, active O, or insertion",
        ),
        HandoffEntry(
            name="H5: insertion-precondition inventory",
            handoff="conditional precondition inventory only",
            status="NOT_READY",
            reason="trace normalization is not selected/adopted and safe membership/incidence gates remain open",
            caution="must not be called insertion theorem",
        ),
        HandoffEntry(
            name="H6: parent field equation",
            handoff="parent route",
            status="NOT_READY",
            reason="scalar recombination and downstream gates remain unresolved",
            caution="parent gate remains closed",
        ),
    ]


def case_5_handoffs(out: ScriptOutput) -> List[HandoffEntry]:
    header("Case 5: Safe handoffs")

    entries = build_handoffs()
    for item in entries:
        subheader(item.name)
        print(f"Handoff: {item.handoff}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Reason: {item.reason}")
        print(f"Caution: {item.caution}")

    with out.governance_assessments():
        out.line(
            "trace-normalization handoffs summarized",
            StatusMark.DEFER,
            "status summary is ready; adoption and insertion remain separate/not ready",
        )
    return entries


def build_obligations() -> List[TraceObligationEntry]:
    return [
        TraceObligationEntry(
            name="O1: preserve compatible-if-declared status",
            obligation="record surviving exact forms as compatible-if-declared only",
            status="OPEN",
            blocks="selection drift",
            discipline="do not shorten to selected, adopted, or derived",
        ),
        TraceObligationEntry(
            name="O2: declare conventions before use",
            obligation="require B_s convention, zeta convention, and traced dimension before future use",
            status="OPEN",
            blocks="factor-of-two and dimension ambiguity",
            discipline="forms cannot hide convention choices",
        ),
        TraceObligationEntry(
            name="O3: keep filters negative",
            obligation="use source/divergence/membership/linearized checks only as filters unless separate theorem support exists",
            status="OPEN",
            blocks="selector drift",
            discipline="filters reject or flag; they do not choose N_trace",
        ),
        TraceObligationEntry(
            name="O4: keep normalization separate from membership",
            obligation="prevent candidate normalization from implying safe membership, incidence, residual kill, or active O",
            status="OPEN",
            blocks="Package B collapse",
            discipline="normalization is not membership",
        ),
        TraceObligationEntry(
            name="O5: adoption remains separate",
            obligation="keep P_trace_norm unadopted unless a separate explicit decision is requested",
            status="OPEN",
            blocks="accidental adoption",
            discipline="candidate survival is not adoption",
        ),
        TraceObligationEntry(
            name="O6: downstream gates remain closed",
            obligation="keep B_s/F_zeta insertion, active O, residual control, and parent equation closed",
            status="NOT_READY",
            blocks="downstream overreach",
            discipline="obligations summary is not insertion or parent closure",
        ),
    ]


def case_6_obligations(out: ScriptOutput) -> List[TraceObligationEntry]:
    header("Case 6: Trace-normalization final obligations")

    entries = build_obligations()
    for item in entries:
        subheader(item.name)
        print(f"Obligation: {item.obligation}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Blocks: {item.blocks}")
        print(f"Discipline: {item.discipline}")

    with out.unresolved_obligations():
        out.line(
            "trace-normalization final obligations stated",
            StatusMark.OBLIGATION,
            "6 obligations stated before Group 33 status summary",
        )
    return entries


def case_7_conclusions(out: ScriptOutput) -> None:
    header("Case 7: Trace-normalization obligations conclusions")

    conclusions = [
        (
            "C1: surviving forms",
            "scale-factor and metric-coefficient exact structural forms survive if declared",
            "COMPATIBLE_IF_DECLARED",
            "both remain candidate forms; neither is selected",
        ),
        (
            "C2: notation-dependent variants",
            "per-dimension zeta forms remain notation-dependent",
            "CONVENTION_DEPENDENT",
            "dimension factor must be explicit",
        ),
        (
            "C3: linearized scope",
            "linearized trace bookkeeping remains first-order only",
            "LINEARIZED_ONLY",
            "not exact coefficient law",
        ),
        (
            "C4: no derivation",
            "this obligations summary derives no trace-normalization theorem",
            "NOT_DERIVED",
            "open decisions remain",
        ),
        (
            "C5: no adoption",
            "this obligations summary adopts no trace-normalization postulate",
            "NOT_ADOPTED",
            "explicit decision remains separate",
        ),
        (
            "C6: next",
            "Group 33 status summary should run next",
            "OPEN",
            "summarize without selecting or adopting N_trace",
        ),
    ]

    for title, conclusion, status, meaning in conclusions:
        subheader(title)
        print(f"Conclusion: {conclusion}")
        print(f"[{status_mark(status).value}] {title}: {status}")
        print(f"Meaning: {meaning}")

    with out.governance_assessments():
        out.line(
            "trace-normalization obligations conclusion stated",
            StatusMark.PASS,
            "surviving forms and obligations summarized; no selection or adoption",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Trace-normalization obligations result:")
    print()
    print("  Scale-factor and metric-coefficient volume-log forms survive as compatible-if-declared candidates.")
    print("  Per-dimension forms survive only as notation-dependent variants.")
    print("  Linearized trace bookkeeping remains first-order only.")
    print("  Undeclared conventions, hidden source load, hidden divergence reservoirs, membership collapse, and exact-upgrade fail.")
    print("  The remaining open decisions are B_s object convention, zeta convention, traced dimension, and exact/linearized scope.")
    print("  No trace-normalization rule is selected, adopted, or derived by this obligations summary.")
    print("  B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready.")
    print()
    print("Possible next script:")
    print("  candidate_group_33_status_summary.py")
    print()
    print("Tiny goblin label:")
    print("  Count the cups. Still no drinking.")

    with out.governance_assessments():
        out.line(
            "trace-normalization obligations summary complete",
            StatusMark.PASS,
            "Group 33 status summary should run next; adoption and downstream gates remain closed",
        )


def record_inventory_marker(ns, symbols: ObligationSymbols) -> None:
    ns.record_derivation(
        derivation_id="g33_trace_normalization_obligations",
        inputs=[symbols.N_trace],
        output=symbols.L_obligation_gap,
        method="trace-normalization obligations summary ledger",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="obligations_summary_marker",
        is_placeholder=True,
    )


def record_governance(
    ns,
    surviving: List[SurvivingFormEntry],
    failures: List[FailureModeEntry],
    decisions: List[OpenDecisionEntry],
    handoffs: List[HandoffEntry],
) -> None:
    obligation_ids = [
        "g33_trace_obligation_o1",
        "g33_trace_obligation_o2",
        "g33_trace_obligation_o3",
        "g33_trace_obligation_o4",
        "g33_trace_obligation_o5",
        "g33_trace_obligation_o6",
    ]

    for item in surviving:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_route(
            RouteRecord(
                route_id=f"g33_obligations_surviving_{ident}",
                script_id=SCRIPT_ID,
                name=item.name,
                status=GovernanceStatus.CANDIDATE_ROUTE,
                tier=ClaimTier.CONSTRAINED,
                required_obligations=obligation_ids,
                activation_conditions=[
                    item.form,
                    f"Survives if: {item.survives_if}",
                    f"Remaining decision: {item.remaining_decision}",
                    f"Boundary: {item.boundary}",
                ],
            )
        )

    for item in failures:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g33_obligations_failure_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.REJECTED_ROUTE,
                statement=f"{item.failure}. Reason: {item.reason}. Consequence: {item.consequence}.",
                derivation_ids=["g33_trace_normalization_obligations"],
                obligation_ids=obligation_ids,
            )
        )

    for item in decisions:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g33_open_decision_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
                statement=f"{item.decision}. Blocks: {item.blocks}. Discipline: {item.discipline}.",
                derivation_ids=["g33_trace_normalization_obligations"],
                obligation_ids=obligation_ids,
            )
        )

    for item in handoffs:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g33_handoff_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=(
                    GovernanceStatus.DEFERRED_PENDING_PREREQUISITES
                    if item.status == "NOT_READY"
                    else GovernanceStatus.CANDIDATE_ROUTE
                ),
                statement=f"{item.handoff}. Reason: {item.reason}. Caution: {item.caution}.",
                derivation_ids=["g33_trace_normalization_obligations"],
                obligation_ids=obligation_ids,
            )
        )


def record_obligations(ns, obligations: List[TraceObligationEntry]) -> None:
    for item in obligations:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_obligation(
            ProofObligationRecord(
                obligation_id=f"g33_trace_obligation_{ident}",
                script_id=SCRIPT_ID,
                title=item.name,
                status=ObligationStatus.OPEN if item.status != "NOT_READY" else ObligationStatus.DEFERRED,
                required_by=[SCRIPT_ID],
                description=f"{item.obligation} Blocks: {item.blocks}. Discipline: {item.discipline}.",
            )
        )


def main() -> None:
    out = ScriptOutput()
    archive, ns, invalidated = prepare_archive()
    ensure_archive_write_dirs(ns)

    header("Candidate Trace-Normalization Obligations")
    print_archive_status(ns, invalidated)

    case_0_problem(out)
    symbols = case_1_symbolic_ledger(out)
    surviving = case_2_surviving_forms(out)
    failures = case_3_failure_modes(out)
    decisions = case_4_open_decisions(out)
    handoffs = case_5_handoffs(out)
    obligations = case_6_obligations(out)
    case_7_conclusions(out)
    final_interpretation(out)

    record_inventory_marker(ns, symbols)
    record_obligations(ns, obligations)
    record_governance(ns, surviving, failures, decisions, handoffs)

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
