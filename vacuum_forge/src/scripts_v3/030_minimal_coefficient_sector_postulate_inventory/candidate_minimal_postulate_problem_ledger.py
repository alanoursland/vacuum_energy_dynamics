# Candidate minimal postulate problem ledger
#
# Group:
#   30_minimal_coefficient_sector_postulate_inventory
#
# Human title:
#   Minimal Coefficient / Sector Postulate Inventory
#
# Script type:
#   PROBLEM LEDGER / INVENTORY CLASSIFIER
#
# Purpose
# -------
# Open the minimal coefficient/sector postulate inventory problem.
# Classify missing structures from Groups 28 and 29 as theorem targets,
# partially constrained candidates, candidate postulates, rejected smuggling,
# or not-ready downstream theorem targets.
#
# Locked-door question:
#
#   What is the smallest explicit coefficient/sector structure that would
#   need to be chosen if it is not derivable?
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
#   Name the missing teeth before cutting the key.

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
        "CANDIDATE_POSTULATE": StatusMark.OBLIGATION,
        "CANDIDATE_ROUTE": StatusMark.DEFER,
        "EXPLICIT_CHOICE_REQUIRED_IF_NOT_DERIVED": StatusMark.OBLIGATION,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "PARTIALLY_CONSTRAINED": StatusMark.INFO,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "THEOREM_TARGET": StatusMark.OBLIGATION,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g29_summary",
            "29_Bs_Fzeta_coefficient_origin__candidate_group_29_status_summary",
            "g29_status_summary",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g29_obligations",
            "29_Bs_Fzeta_coefficient_origin__candidate_coefficient_origin_obligations",
            "g29_obligations",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g28_summary",
            "28_sector_pairing_no_overlap__candidate_group_28_status_summary",
            "g28_status_summary",
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
class InventorySymbols:
    P_trace_norm: sp.Symbol
    P_safe_membership: sp.Symbol
    P_incidence: sp.Symbol
    P_source_once: sp.Symbol
    P_guardrail_visibility: sp.Symbol
    P_divergence_explicit: sp.Symbol
    T_coeff: sp.Symbol
    T_source_div: sp.Symbol
    insertion_gate: sp.Symbol
    parent_gate: sp.Symbol
    postulate_burden: sp.Expr


@dataclass
class MissingStructure:
    name: str
    structure: str
    prior_status: str
    inventory_status: str
    reason: str


@dataclass
class CandidatePostulateFamily:
    name: str
    candidate: str
    status: str
    purpose: str
    risk: str


@dataclass
class RejectedPostulateRoute:
    name: str
    route: str
    status: str
    reason: str


@dataclass
class InitialObligation:
    name: str
    obligation: str
    status: str
    blocks: str
    discipline: str


@dataclass
class InitialConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_symbols() -> InventorySymbols:
    (
        P_trace_norm,
        P_safe_membership,
        P_incidence,
        P_source_once,
        P_guardrail_visibility,
        P_divergence_explicit,
        T_coeff,
        T_source_div,
        insertion_gate,
        parent_gate,
    ) = sp.symbols(
        "P_trace_norm P_safe_membership P_incidence P_source_once "
        "P_guardrail_visibility P_divergence_explicit T_coeff T_source_div "
        "insertion_gate parent_gate",
        real=True,
    )

    postulate_burden = sp.simplify(
        P_trace_norm
        + P_safe_membership
        + P_incidence
        + P_source_once
        + P_guardrail_visibility
        + P_divergence_explicit
        + T_coeff
        + T_source_div
        + insertion_gate
        + parent_gate
    )

    return InventorySymbols(
        P_trace_norm=P_trace_norm,
        P_safe_membership=P_safe_membership,
        P_incidence=P_incidence,
        P_source_once=P_source_once,
        P_guardrail_visibility=P_guardrail_visibility,
        P_divergence_explicit=P_divergence_explicit,
        T_coeff=T_coeff,
        T_source_div=T_source_div,
        insertion_gate=insertion_gate,
        parent_gate=parent_gate,
        postulate_burden=postulate_burden,
    )


def build_missing_structures() -> List[MissingStructure]:
    return [
        MissingStructure(
            name="M1: volume/trace coefficient origin",
            structure="volume/trace algebra for zeta and B_s coefficient origin",
            prior_status="PARTIALLY_CONSTRAINED",
            inventory_status="THEOREM_TARGET",
            reason="real structural candidate exists; do not replace with postulate yet",
        ),
        MissingStructure(
            name="M2: trace normalization",
            structure="how B_s reads the volume-trace scalar",
            prior_status="OPEN",
            inventory_status="CANDIDATE_POSTULATE",
            reason="normalization remains underdetermined after Group 29",
        ),
        MissingStructure(
            name="M3: safe trace membership",
            structure="zeta_Bs -> T_zeta as membership rule",
            prior_status="CONSTRAINED_CANDIDATE",
            inventory_status="CANDIDATE_POSTULATE",
            reason="structurally strengthened but not theorem",
        ),
        MissingStructure(
            name="M4: trace/residual zero incidence",
            structure="I(T_zeta,R_zeta)=0 and I(T_zeta,R_kappa)=0",
            prior_status="NOT_DERIVED",
            inventory_status="HIGH_RISK_CANDIDATE_POSTULATE",
            reason="needed for no-overlap, but postulating it may smuggle residual control",
        ),
        MissingStructure(
            name="M5: source no-double-counting",
            structure="ordinary source load not duplicated through coefficient/accounting sectors",
            prior_status="NOT_DERIVED",
            inventory_status="THEOREM_TARGET_OR_CANDIDATE_POSTULATE",
            reason="may be source/divergence theorem route rather than postulate",
        ),
        MissingStructure(
            name="M6: guardrail visibility",
            structure="boundary/current/mass/support loads remain visible and non-reservoir",
            prior_status="COMPATIBLE_CANDIDATE",
            inventory_status="CANDIDATE_POSTULATE",
            reason="visibility already required; neutralities remain theorem targets",
        ),
        MissingStructure(
            name="M7: divergence explicitness",
            structure="any divergence correction is explicit, auditable, and non-reservoir",
            prior_status="OPEN",
            inventory_status="CANDIDATE_POSTULATE_OR_THEOREM_TARGET",
            reason="needed to prevent hidden load; may be law rather than postulate",
        ),
        MissingStructure(
            name="M8: B_s/F_zeta insertion",
            structure="B_s = F_zeta[...] insertion theorem",
            prior_status="NOT_READY",
            inventory_status="NOT_READY",
            reason="cannot be postulated wholesale without collapsing the program",
        ),
        MissingStructure(
            name="M9: parent equation",
            structure="parent field equation closure",
            prior_status="NOT_READY",
            inventory_status="NOT_READY",
            reason="forbidden until upstream gates close",
        ),
    ]


def build_candidate_families() -> List[CandidatePostulateFamily]:
    return [
        CandidatePostulateFamily(
            name="P1: trace-normalization postulate",
            candidate="B_s reads the volume-trace scalar through a fixed normalization rule",
            status="CANDIDATE_POSTULATE",
            purpose="close normalization gap without recovery selection",
            risk="overfits weak-field, AB=1, or Schwarzschild",
        ),
        CandidatePostulateFamily(
            name="P2: safe-trace membership postulate",
            candidate="zeta_Bs is assigned to T_zeta as safe trace membership",
            status="CANDIDATE_POSTULATE",
            purpose="turn constrained candidate into explicit membership rule",
            risk="mistaken for no-overlap, source routing, or residual control",
        ),
        CandidatePostulateFamily(
            name="P3: trace/residual incidence postulate",
            candidate="I(T_zeta,R_zeta)=0 and/or I(T_zeta,R_kappa)=0",
            status="CANDIDATE_POSTULATE",
            purpose="supply no-overlap relation if not derivable",
            risk="too strong; may hide residuals or assert residual control",
        ),
        CandidatePostulateFamily(
            name="P4: source no-double-counting postulate",
            candidate="ordinary source load enters once and is not duplicated through coefficient/accounting sectors",
            status="CANDIDATE_POSTULATE",
            purpose="protect count-once recombination",
            risk="source routing chosen by repair rather than principle",
        ),
        CandidatePostulateFamily(
            name="P5: guardrail visibility postulate",
            candidate="boundary/current/mass/support loads remain visible and cannot be absorbed into coefficient, accounting, or correction terms",
            status="CANDIDATE_POSTULATE",
            purpose="prevent hidden repair reservoirs",
            risk="visibility mistaken for neutrality theorem",
        ),
        CandidatePostulateFamily(
            name="P6: divergence explicitness postulate",
            candidate="any divergence correction must be explicit, auditable, and non-reservoir",
            status="CANDIDATE_POSTULATE",
            purpose="avoid hidden load in correction terms",
            risk="correction becomes parent-fit closure",
        ),
    ]


def build_rejected_routes() -> List[RejectedPostulateRoute]:
    return [
        RejectedPostulateRoute(
            name="R1: recovery-selected postulate",
            route="choose postulate to make AB=1, B=1/A, Schwarzschild, gamma/PPN, weak field, or kappa=0 work",
            status="REJECTED",
            reason="recovery may audit only after construction",
        ),
        RejectedPostulateRoute(
            name="R2: repair-selected postulate",
            route="choose postulate to repair residual/source/boundary/current/mass/support failure",
            status="REJECTED",
            reason="failure may reject but not select",
        ),
        RejectedPostulateRoute(
            name="R3: postulate as derivation",
            route="state a postulate but record it as a theorem",
            status="REJECTED",
            reason="explicit choice must remain explicitly marked",
        ),
        RejectedPostulateRoute(
            name="R4: insertion by postulate bundle",
            route="postulate B_s/F_zeta insertion wholesale",
            status="REJECTED",
            reason="too large; collapses coefficient/source/divergence obligations",
        ),
        RejectedPostulateRoute(
            name="R5: active-O by postulate",
            route="postulate active O from coefficient/sector scaffold",
            status="REJECTED",
            reason="operator construction remains not ready",
        ),
        RejectedPostulateRoute(
            name="R6: parent by postulate",
            route="postulate parent equation closure",
            status="REJECTED",
            reason="parent gate remains closed",
        ),
    ]


def build_initial_obligations() -> List[InitialObligation]:
    return [
        InitialObligation(
            name="O1: minimality",
            obligation="test whether each candidate postulate is independent and minimal",
            status="REQUIRED",
            blocks="postulate inventory",
            discipline="reject overlarge bundled postulates",
        ),
        InitialObligation(
            name="O2: anti-smuggling",
            obligation="filter candidate postulates against recovery, repair, residual cleanup, active O, and parent fit",
            status="REQUIRED",
            blocks="admissibility",
            discipline="postulates may not be selected by desired endpoint",
        ),
        InitialObligation(
            name="O3: trace normalization",
            obligation="decide whether trace-normalization is theorem target or explicit choice",
            status="OPEN",
            blocks="coefficient law",
            discipline="do not choose from recovery",
        ),
        InitialObligation(
            name="O4: membership",
            obligation="decide whether zeta_Bs -> T_zeta needs explicit membership postulate",
            status="OPEN",
            blocks="sector geometry",
            discipline="do not upgrade membership to no-overlap",
        ),
        InitialObligation(
            name="O5: incidence/source/divergence split",
            obligation="classify zero incidence, source no-double-counting, and divergence explicitness as theorem routes or postulate candidates",
            status="OPEN",
            blocks="insertion and residual control",
            discipline="do not hide residuals or source load",
        ),
        InitialObligation(
            name="O6: downstream gates",
            obligation="keep B_s/F_zeta insertion, active O, residual control, and parent equation closed",
            status="NOT_READY",
            blocks="premature closure",
            discipline="inventory is not theorem closure",
        ),
    ]


def build_initial_conclusions() -> List[InitialConclusion]:
    return [
        InitialConclusion(
            name="C1: next group",
            conclusion="minimal coefficient/sector postulate inventory is the right next group",
            status="CANDIDATE_ROUTE",
            meaning="Groups 28 and 29 localized missing structures not forced by current derivations",
        ),
        InitialConclusion(
            name="C2: adoption status",
            conclusion="no new postulate is adopted in this opening ledger",
            status="NOT_ADOPTED",
            meaning="this is an inventory problem, not a choice event",
        ),
        InitialConclusion(
            name="C3: candidate families",
            conclusion="six candidate postulate families are named for testing",
            status="CANDIDATE_POSTULATE",
            meaning="trace normalization, safe membership, incidence, source, guardrail visibility, and divergence explicitness",
        ),
        InitialConclusion(
            name="C4: downstream gates",
            conclusion="insertion, active O, residual control, and parent equation remain not ready",
            status="NOT_READY",
            meaning="postulate inventory cannot be upgraded to closure",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Minimal postulate inventory problem")
    print("Question:")
    print()
    print("  What is the smallest explicit coefficient/sector structure that would need to be chosen if it is not derivable?")
    print()
    print("Discipline:")
    print()
    print("  This script does not adopt a postulate.")
    print("  This script does not derive insertion.")
    print("  This script does not open the parent equation.")
    print()
    print("Tiny goblin rule:")
    print("  Name the missing teeth before cutting the key.")

    with out.governance_assessments():
        out.line(
            "minimal coefficient/sector postulate inventory opened",
            StatusMark.INFO,
            "opening explicit-choice inventory after Group 29 partial coefficient-origin constraint",
        )


def case_1_symbolic_ledger(symbols: InventorySymbols, out: ScriptOutput) -> None:
    header("Case 1: Minimal postulate symbolic ledger")
    print("Inventory symbols:")
    print()
    for name in [
        "P_trace_norm",
        "P_safe_membership",
        "P_incidence",
        "P_source_once",
        "P_guardrail_visibility",
        "P_divergence_explicit",
        "T_coeff",
        "T_source_div",
        "insertion_gate",
        "parent_gate",
    ]:
        print(f"  {name} = {sp.sstr(getattr(symbols, name))}")
    print()
    print("Minimal postulate burden:")
    print()
    print(f"  L_minimal_postulate_inventory = {sp.sstr(symbols.postulate_burden)}")

    with out.derived_results():
        out.line(
            "minimal postulate inventory burden stated",
            StatusMark.OBLIGATION,
            f"L_minimal_postulate_inventory = {sp.sstr(symbols.postulate_burden)}",
        )


def case_2_missing_structures(items: List[MissingStructure], out: ScriptOutput) -> None:
    header("Case 2: Missing structure inventory")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Structure: {item.structure}")
        print(f"Prior status: {item.prior_status}")
        print(f"[{status_mark(item.inventory_status).value}] {item.name}: {item.inventory_status}")
        print(f"Reason: {item.reason}")

    with out.governance_assessments():
        out.line(
            "missing structures classified for postulate inventory",
            StatusMark.DEFER,
            f"{len(items)} missing structures classified",
        )


def case_3_candidate_postulates(items: List[CandidatePostulateFamily], out: ScriptOutput) -> None:
    header("Case 3: Candidate postulate families")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Candidate: {item.candidate}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Purpose: {item.purpose}")
        print(f"Risk: {item.risk}")

    with out.unresolved_obligations():
        out.line(
            "candidate postulate families named",
            StatusMark.OBLIGATION,
            f"{len(items)} candidate postulate families named; none adopted",
        )


def case_4_rejected_routes(items: List[RejectedPostulateRoute], out: ScriptOutput) -> None:
    header("Case 4: Rejected postulate-selection routes")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Route: {item.route}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Reason: {item.reason}")

    with out.counterexamples():
        out.line(
            "rejected postulate-selection routes stated",
            StatusMark.FAIL,
            "recovery, repair, postulate-as-derivation, insertion bundle, active O, and parent routes rejected",
        )


def case_5_initial_obligations(items: List[InitialObligation], out: ScriptOutput) -> None:
    header("Case 5: Initial inventory obligations")
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
            "minimal postulate inventory obligations stated",
            StatusMark.OBLIGATION,
            f"{len(items)} inventory obligations opened",
        )


def case_6_initial_conclusions(items: List[InitialConclusion], out: ScriptOutput) -> None:
    header("Case 6: Initial inventory conclusions")
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
            "minimal postulate inventory initial conclusion stated",
            StatusMark.PASS,
            "inventory route opened; no postulate adopted; downstream gates closed",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Minimal postulate inventory ledger result:")
    print()
    print("  Minimal coefficient/sector postulate inventory is opened.")
    print("  No new postulate is adopted in this script.")
    print("  Candidate postulate families are named:")
    print("    trace normalization;")
    print("    safe trace membership;")
    print("    trace/residual incidence;")
    print("    source no-double-counting;")
    print("    guardrail visibility;")
    print("    divergence explicitness.")
    print("  Volume/trace coefficient origin remains a theorem target / partial constraint, not a postulate replacement.")
    print("  B_s/F_zeta insertion is not derived.")
    print("  Active O, residual control, and parent equation remain not ready.")
    print()
    print("Possible next script:")
    print("  candidate_postulate_minimality_tests.py")
    print()
    print("Tiny goblin label:")
    print("  Name the missing teeth before cutting the key.")

    with out.governance_assessments():
        out.line(
            "minimal postulate inventory problem ledger complete",
            StatusMark.PASS,
            "minimality tests should run next",
        )


def record_derivations(ns, symbols: InventorySymbols) -> None:
    ns.record_derivation(
        derivation_id="g30_postulate_problem",
        inputs=[
            symbols.P_trace_norm,
            symbols.P_safe_membership,
            symbols.P_incidence,
            symbols.P_source_once,
            symbols.P_guardrail_visibility,
            symbols.P_divergence_explicit,
            symbols.T_coeff,
            symbols.T_source_div,
            symbols.insertion_gate,
            symbols.parent_gate,
        ],
        output=symbols.postulate_burden,
        method="open minimal coefficient/sector postulate inventory without adopting postulates",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="minimal_postulate_problem_marker",
        scope="Group 30 minimal coefficient/sector postulate inventory",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g30_minimality", "Test candidate postulates for independence and minimality"),
        ("g30_antismuggling", "Filter candidate postulates against recovery and repair selection"),
        ("g30_trace_norm", "Classify trace-normalization postulate candidate"),
        ("g30_safe_membership", "Classify safe-trace membership postulate candidate"),
        ("g30_incidence", "Classify trace/residual incidence postulate candidate"),
        ("g30_source_once", "Classify source no-double-counting postulate candidate"),
        ("g30_guardrail_visibility", "Classify guardrail visibility postulate candidate"),
        ("g30_divergence_explicit", "Classify divergence explicitness postulate candidate"),
        ("g30_downstream", "Keep insertion/O/residual/parent gates closed"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g30_postulate_inventory_route"],
            description=(
                "The postulate inventory route is opened. No postulate is adopted and no downstream theorem is derived."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g30_minimality",
        "g30_antismuggling",
        "g30_trace_norm",
        "g30_safe_membership",
        "g30_incidence",
        "g30_source_once",
        "g30_guardrail_visibility",
        "g30_divergence_explicit",
        "g30_downstream",
    ]

    ns.record_route(RouteRecord(
        route_id="g30_postulate_inventory_route",
        script_id=SCRIPT_ID,
        name="Group 30 minimal coefficient/sector postulate inventory route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "explicit choices are marked as postulates, not derivations",
            "no postulate is adopted in opening ledger",
            "recovery and repair may not select postulates",
            "candidate postulate families are tested for minimality next",
            "B_s/F_zeta insertion, active O, residual control, and parent equation remain closed",
        ],
    ))

    for branch_id in [
        "postulate_as_derivation",
        "recovery_selected_postulate",
        "repair_selected_postulate",
        "residual_cleanup_postulate",
        "source_hiding_postulate",
        "divergence_reservoir_postulate",
        "insertion_by_postulate_bundle",
        "active_O_by_postulate",
        "residual_control_by_postulate",
        "parent_by_postulate",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; minimal postulate inventory is not theorem closure or endpoint-selected construction.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g30_postulate_inventory_opened",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Group 30 opens a minimal coefficient/sector postulate inventory. Candidate postulate families are trace normalization, safe trace membership, trace/residual incidence, "
            "source no-double-counting, guardrail visibility, and divergence explicitness. No postulate is adopted in the opening ledger. Postulates may not be selected by recovery, repair, residual cleanup, active O convenience, or parent fit. "
            "B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready."
        ),
        derivation_ids=["g30_postulate_problem"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Minimal Postulate Problem Ledger")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    missing = build_missing_structures()
    candidate_postulates = build_candidate_families()
    rejected_routes = build_rejected_routes()
    obligations = build_initial_obligations()
    conclusions = build_initial_conclusions()

    case_0_problem_statement(out)
    case_1_symbolic_ledger(symbols, out)
    case_2_missing_structures(missing, out)
    case_3_candidate_postulates(candidate_postulates, out)
    case_4_rejected_routes(rejected_routes, out)
    case_5_initial_obligations(obligations, out)
    case_6_initial_conclusions(conclusions, out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns, symbols)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
