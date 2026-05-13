# Candidate postulate smuggling filter
#
# Group:
#   30_minimal_coefficient_sector_postulate_inventory
#
# Script type:
#   POSTULATE ANTI-SMUGGLING FILTER
#
# Purpose
# -------
# Filter surviving minimal postulate candidates against recovery, repair,
# residual cleanup, source hiding, divergence reservoir, active-O convenience,
# and parent-fit selection.
#
# Locked-door question:
#
#   Which candidate postulates survive anti-smuggling discipline?
#
# This script does not adopt a new postulate.
# It does not derive B_s/F_zeta insertion.
# It does not derive no-overlap sector geometry.
# It does not construct active O.
# It does not derive residual control.
# It does not open the parent equation.
#
# Tiny goblin rule:
#
#   A clean tooth is still not a bitten lock.

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


def status_mark(status: str) -> StatusMark:
    return {
        "ADMISSIBLE_CANDIDATE": StatusMark.INFO,
        "HIGH_RISK": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "REJECTED": StatusMark.FAIL,
        "REQUIRES_FURTHER_TEST": StatusMark.OBLIGATION,
        "REQUIRED": StatusMark.OBLIGATION,
        "THEOREM_ROUTE_PREFERRED": StatusMark.INFO,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g30_minimality",
            "30_minimal_coefficient_sector_postulate_inventory__candidate_postulate_minimality_tests",
            "g30_postulate_minimality",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g30_problem",
            "30_minimal_coefficient_sector_postulate_inventory__candidate_minimal_postulate_problem_ledger",
            "g30_postulate_problem",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g29_summary",
            "29_Bs_Fzeta_coefficient_origin__candidate_group_29_status_summary",
            "g29_status_summary",
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
class SmugglingSymbols:
    P_trace_norm: sp.Symbol
    P_safe_membership: sp.Symbol
    P_incidence: sp.Symbol
    P_source_once: sp.Symbol
    P_guardrail_visibility: sp.Symbol
    P_divergence_explicit: sp.Symbol
    recovery_smuggle: sp.Symbol
    repair_smuggle: sp.Symbol
    residual_smuggle: sp.Symbol
    source_smuggle: sp.Symbol
    divergence_smuggle: sp.Symbol
    parent_smuggle: sp.Symbol
    filter_load: sp.Expr


@dataclass
class SmugglingFilterResult:
    name: str
    candidate: str
    status: str
    survives_if: str
    rejected_if: str


@dataclass
class RejectedSelection:
    name: str
    selection: str
    status: str
    reason: str


@dataclass
class FilterObligation:
    name: str
    obligation: str
    status: str
    blocks: str
    discipline: str


@dataclass
class FilterConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_symbols() -> SmugglingSymbols:
    (
        P_trace_norm,
        P_safe_membership,
        P_incidence,
        P_source_once,
        P_guardrail_visibility,
        P_divergence_explicit,
        recovery_smuggle,
        repair_smuggle,
        residual_smuggle,
        source_smuggle,
        divergence_smuggle,
        parent_smuggle,
    ) = sp.symbols(
        "P_trace_norm P_safe_membership P_incidence P_source_once "
        "P_guardrail_visibility P_divergence_explicit "
        "recovery_smuggle repair_smuggle residual_smuggle source_smuggle divergence_smuggle parent_smuggle",
        real=True,
    )

    filter_load = sp.simplify(
        P_trace_norm
        + P_safe_membership
        + P_incidence
        + P_source_once
        + P_guardrail_visibility
        + P_divergence_explicit
        + recovery_smuggle
        + repair_smuggle
        + residual_smuggle
        + source_smuggle
        + divergence_smuggle
        + parent_smuggle
    )

    return SmugglingSymbols(
        P_trace_norm=P_trace_norm,
        P_safe_membership=P_safe_membership,
        P_incidence=P_incidence,
        P_source_once=P_source_once,
        P_guardrail_visibility=P_guardrail_visibility,
        P_divergence_explicit=P_divergence_explicit,
        recovery_smuggle=recovery_smuggle,
        repair_smuggle=repair_smuggle,
        residual_smuggle=residual_smuggle,
        source_smuggle=source_smuggle,
        divergence_smuggle=divergence_smuggle,
        parent_smuggle=parent_smuggle,
        filter_load=filter_load,
    )


def build_filter_results() -> List[SmugglingFilterResult]:
    return [
        SmugglingFilterResult(
            name="F1: trace-normalization",
            candidate="B_s reads the volume-trace scalar through a fixed normalization rule",
            status="ADMISSIBLE_CANDIDATE",
            survives_if="normalization is structural and not selected from AB=1, Schwarzschild, gamma/PPN, weak-field, or kappa=0",
            rejected_if="chosen to force recovery or parent fit",
        ),
        SmugglingFilterResult(
            name="F2: safe-trace membership",
            candidate="zeta_Bs is assigned to T_zeta as safe trace membership",
            status="ADMISSIBLE_CANDIDATE",
            survives_if="membership only assigns safe channel and does not assert no-overlap, source routing, or residual control",
            rejected_if="used to hide residuals or derive insertion",
        ),
        SmugglingFilterResult(
            name="F3: trace/residual incidence",
            candidate="I(T_zeta,R_zeta)=0 and/or I(T_zeta,R_kappa)=0",
            status="HIGH_RISK",
            survives_if="kept as explicit incidence-only candidate and does not imply residual kill/inertness",
            rejected_if="used as residual-control theorem, no-overlap geometry theorem, or residual erasure",
        ),
        SmugglingFilterResult(
            name="F4: source no-double-counting",
            candidate="ordinary source load enters once and is not duplicated through coefficient/accounting sectors",
            status="THEOREM_ROUTE_PREFERRED",
            survives_if="derived from source/divergence law or stated as narrow non-repair choice",
            rejected_if="chosen to repair source leakage or force insertion",
        ),
        SmugglingFilterResult(
            name="F5: guardrail visibility",
            candidate="boundary/current/mass/support loads remain visible and non-reservoir",
            status="ADMISSIBLE_CANDIDATE",
            survives_if="visibility only; no neutrality or cancellation claimed",
            rejected_if="used to repair boundary/current/mass/support failure",
        ),
        SmugglingFilterResult(
            name="F6: divergence explicitness",
            candidate="any divergence correction must be explicit, auditable, and non-reservoir",
            status="ADMISSIBLE_CANDIDATE",
            survives_if="correction is visible and not a source/boundary/current/mass/support reservoir",
            rejected_if="used to close parent equation or hide correction load",
        ),
    ]


def build_rejected_selections() -> List[RejectedSelection]:
    return [
        RejectedSelection(
            name="R1: recovery selection",
            selection="postulate chosen to make AB=1, B=1/A, Schwarzschild, gamma/PPN, weak-field, or kappa=0 work",
            status="REJECTED",
            reason="recovery may audit only after construction",
        ),
        RejectedSelection(
            name="R2: repair selection",
            selection="postulate chosen to repair residual/source/boundary/current/mass/support failure",
            status="REJECTED",
            reason="failure may reject but not select",
        ),
        RejectedSelection(
            name="R3: residual cleanup",
            selection="postulate chosen to kill, inert, absorb, or hide residuals",
            status="REJECTED",
            reason="residual control remains not derived",
        ),
        RejectedSelection(
            name="R4: source hiding",
            selection="ordinary source load hidden inside coefficient, accounting, or correction term",
            status="REJECTED",
            reason="source visibility remains required",
        ),
        RejectedSelection(
            name="R5: divergence reservoir",
            selection="divergence correction absorbs source/boundary/current/mass/support load",
            status="REJECTED",
            reason="correction must remain explicit and auditable",
        ),
        RejectedSelection(
            name="R6: active-O convenience",
            selection="postulate chosen to make active O possible",
            status="REJECTED",
            reason="operator construction remains not ready",
        ),
        RejectedSelection(
            name="R7: parent fit",
            selection="postulate chosen so parent equation closes",
            status="REJECTED",
            reason="parent gate remains closed",
        ),
        RejectedSelection(
            name="R8: postulate as theorem",
            selection="postulate recorded as derivation",
            status="REJECTED",
            reason="explicit choice must remain marked as choice",
        ),
    ]


def build_obligations() -> List[FilterObligation]:
    return [
        FilterObligation(
            name="O1: trace normalization next",
            obligation="audit whether trace-normalization postulate should be retained as explicit candidate",
            status="OPEN",
            blocks="coefficient law",
            discipline="do not select normalization from recovery",
        ),
        FilterObligation(
            name="O2: safe membership next",
            obligation="audit whether zeta_Bs -> T_zeta should be retained as explicit membership candidate",
            status="OPEN",
            blocks="sector membership",
            discipline="do not upgrade membership to no-overlap",
        ),
        FilterObligation(
            name="O3: incidence caution",
            obligation="decide whether trace/residual incidence is too risky to postulate directly",
            status="REQUIRES_FURTHER_TEST",
            blocks="residual-control honesty",
            discipline="do not hide residuals",
        ),
        FilterObligation(
            name="O4: source/divergence fork",
            obligation="prefer source/divergence theorem route unless a narrow postulate is unavoidable",
            status="OPEN",
            blocks="field-equation usability",
            discipline="do not hide source or correction load",
        ),
        FilterObligation(
            name="O5: downstream closure",
            obligation="keep B_s/F_zeta insertion, active O, residual control, and parent equation closed",
            status="NOT_READY",
            blocks="premature closure",
            discipline="anti-smuggling is not theorem closure",
        ),
    ]


def build_conclusions() -> List[FilterConclusion]:
    return [
        FilterConclusion(
            name="C1: admissible candidates",
            conclusion="trace normalization, safe membership, guardrail visibility, and divergence explicitness survive anti-smuggling as admissible candidates",
            status="ADMISSIBLE_CANDIDATE",
            meaning="they remain candidates only; no adoption",
        ),
        FilterConclusion(
            name="C2: source route",
            conclusion="source no-double-counting should prefer source/divergence theorem route",
            status="THEOREM_ROUTE_PREFERRED",
            meaning="postulate only if theorem route fails and choice is explicit",
        ),
        FilterConclusion(
            name="C3: incidence",
            conclusion="trace/residual incidence remains high-risk",
            status="HIGH_RISK",
            meaning="it may smuggle no-overlap or residual control",
        ),
        FilterConclusion(
            name="C4: rejected selections",
            conclusion="recovery, repair, residual cleanup, source hiding, divergence reservoir, active-O convenience, parent fit, and postulate-as-theorem are rejected",
            status="REJECTED",
            meaning="candidate postulates must not be endpoint-selected",
        ),
        FilterConclusion(
            name="C5: adoption",
            conclusion="no postulate is adopted",
            status="NOT_ADOPTED",
            meaning="the filter only narrows admissible candidates",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Postulate smuggling filter problem")
    print("Question:")
    print()
    print("  Which candidate postulates survive anti-smuggling discipline?")
    print()
    print("Discipline:")
    print()
    print("  The filter rejects endpoint-selected choices.")
    print("  The filter adopts no postulate.")
    print("  The filter derives no insertion.")
    print()
    print("Tiny goblin rule:")
    print("  A clean tooth is still not a bitten lock.")

    with out.governance_assessments():
        out.line(
            "postulate smuggling filter opened",
            StatusMark.INFO,
            "filtering minimal candidates against recovery, repair, residual, source, divergence, active-O, and parent smuggling",
        )


def case_1_symbolic_ledger(symbols: SmugglingSymbols, out: ScriptOutput) -> None:
    header("Case 1: Postulate smuggling symbolic ledger")
    print("Smuggling filter symbols:")
    print()
    for name in [
        "P_trace_norm",
        "P_safe_membership",
        "P_incidence",
        "P_source_once",
        "P_guardrail_visibility",
        "P_divergence_explicit",
        "recovery_smuggle",
        "repair_smuggle",
        "residual_smuggle",
        "source_smuggle",
        "divergence_smuggle",
        "parent_smuggle",
    ]:
        print(f"  {name} = {sp.sstr(getattr(symbols, name))}")
    print()
    print("Postulate smuggling filter load:")
    print()
    print(f"  L_postulate_smuggling_filter = {sp.sstr(symbols.filter_load)}")

    with out.derived_results():
        out.line(
            "postulate smuggling filter load stated",
            StatusMark.OBLIGATION,
            f"L_postulate_smuggling_filter = {sp.sstr(symbols.filter_load)}",
        )


def case_2_filter_results(items: List[SmugglingFilterResult], out: ScriptOutput) -> None:
    header("Case 2: Candidate postulate anti-smuggling results")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Candidate: {item.candidate}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Survives if: {item.survives_if}")
        print(f"Rejected if: {item.rejected_if}")

    with out.governance_assessments():
        out.line(
            "candidate postulates filtered",
            StatusMark.DEFER,
            f"{len(items)} candidate postulates filtered against smuggling",
        )


def case_3_rejected_selections(items: List[RejectedSelection], out: ScriptOutput) -> None:
    header("Case 3: Rejected postulate-selection modes")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Selection: {item.selection}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Reason: {item.reason}")

    with out.counterexamples():
        out.line(
            "rejected postulate-selection modes stated",
            StatusMark.FAIL,
            "recovery, repair, residual cleanup, source hiding, divergence reservoir, active-O, parent, and theorem-recording selections rejected",
        )


def case_4_obligations(items: List[FilterObligation], out: ScriptOutput) -> None:
    header("Case 4: Postulate smuggling filter obligations")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Obligation: {item.obligation}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Blocks: {item.blocks}")
        print(f"Discipline: {item.discipline}")

    with out.unresolved_obligations():
        out.line(
            "postulate smuggling filter obligations stated",
            StatusMark.OBLIGATION,
            f"{len(items)} obligations remain after smuggling filter",
        )


def case_5_conclusions(items: List[FilterConclusion], out: ScriptOutput) -> None:
    header("Case 5: Postulate smuggling filter conclusions")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Conclusion: {item.conclusion}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Meaning: {item.meaning}")

    with out.governance_assessments():
        out.line(
            "postulate smuggling filter conclusions stated",
            StatusMark.PASS,
            "admissible candidates narrowed; no postulate adopted",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Postulate smuggling filter result:")
    print()
    print("  Trace normalization survives as admissible candidate.")
    print("  Safe trace membership survives as admissible candidate.")
    print("  Guardrail visibility survives as admissible candidate.")
    print("  Divergence explicitness survives as admissible candidate.")
    print("  Source no-double-counting prefers source/divergence theorem route.")
    print("  Trace/residual incidence remains high-risk.")
    print("  Recovery-selected, repair-selected, residual-cleanup, source-hiding, divergence-reservoir, active-O-selected, parent-fit, and postulate-as-theorem routes are rejected.")
    print("  No postulate is adopted.")
    print("  B_s/F_zeta insertion is not derived.")
    print("  Active O, residual control, and parent equation remain not ready.")
    print()
    print("Possible next script:")
    print("  candidate_trace_normalization_postulate.py")
    print()
    print("Tiny goblin label:")
    print("  A clean tooth is still not a bitten lock.")

    with out.governance_assessments():
        out.line(
            "postulate smuggling filter complete",
            StatusMark.PASS,
            "trace-normalization postulate audit should run next",
        )


def record_derivations(ns, symbols: SmugglingSymbols) -> None:
    ns.record_derivation(
        derivation_id="g30_postulate_smuggling_filter",
        inputs=[
            symbols.P_trace_norm,
            symbols.P_safe_membership,
            symbols.P_incidence,
            symbols.P_source_once,
            symbols.P_guardrail_visibility,
            symbols.P_divergence_explicit,
            symbols.recovery_smuggle,
            symbols.repair_smuggle,
            symbols.residual_smuggle,
            symbols.source_smuggle,
            symbols.divergence_smuggle,
            symbols.parent_smuggle,
        ],
        output=symbols.filter_load,
        method="filter candidate postulates against recovery, repair, residual, source, divergence, active-O, and parent smuggling",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="postulate_smuggling_filter_marker",
        scope="Group 30 minimal coefficient/sector postulate inventory",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g30_filter_trace_norm", "Audit trace-normalization postulate next"),
        ("g30_filter_safe_membership", "Audit safe-trace membership postulate"),
        ("g30_filter_incidence_caution", "Treat trace/residual incidence as high-risk"),
        ("g30_filter_source_div", "Prefer source/divergence theorem route for source no-double-counting"),
        ("g30_filter_no_smuggling", "Reject endpoint-selected postulates"),
        ("g30_filter_downstream", "Keep insertion/O/residual/parent gates closed"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g30_filter_route"],
            description=(
                "Candidate postulates are filtered against smuggling only. No postulate is adopted and no downstream theorem is derived."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g30_filter_trace_norm",
        "g30_filter_safe_membership",
        "g30_filter_incidence_caution",
        "g30_filter_source_div",
        "g30_filter_no_smuggling",
        "g30_filter_downstream",
    ]

    ns.record_route(RouteRecord(
        route_id="g30_filter_route",
        script_id=SCRIPT_ID,
        name="Group 30 postulate smuggling filter route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "trace normalization, safe membership, guardrail visibility, and divergence explicitness survive as admissible candidates",
            "source no-double-counting prefers source/divergence theorem route",
            "trace/residual incidence remains high-risk",
            "no postulate is adopted",
            "downstream gates remain closed",
        ],
    ))

    for branch_id in [
        "recovery_selected_postulate",
        "repair_selected_postulate",
        "residual_cleanup_postulate",
        "source_hiding_postulate",
        "divergence_reservoir_postulate",
        "active_O_selected_postulate",
        "parent_fit_postulate",
        "postulate_as_theorem",
        "filter_as_adoption",
        "filter_as_insertion",
        "filter_as_parent_readiness",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; postulate smuggling filter is not adoption or theorem closure.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g30_postulate_smuggling_filter_result",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Trace normalization, safe trace membership, guardrail visibility, and divergence explicitness survive anti-smuggling as admissible candidates. "
            "Source no-double-counting should prefer source/divergence theorem route. Trace/residual incidence remains high-risk. "
            "Recovery-selected, repair-selected, residual-cleanup, source-hiding, divergence-reservoir, active-O-selected, parent-fit, and postulate-as-theorem routes are rejected. "
            "No postulate is adopted. B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready."
        ),
        derivation_ids=["g30_postulate_smuggling_filter"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Postulate Smuggling Filter")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    filter_results = build_filter_results()
    rejected_selections = build_rejected_selections()
    obligations = build_obligations()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_symbolic_ledger(symbols, out)
    case_2_filter_results(filter_results, out)
    case_3_rejected_selections(rejected_selections, out)
    case_4_obligations(obligations, out)
    case_5_conclusions(conclusions, out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns, symbols)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
