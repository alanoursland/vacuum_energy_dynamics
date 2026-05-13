# Candidate safe trace membership origin problem
#
# Group:
#   34_safe_trace_membership_candidate_origin
#
# Human title:
#   Safe Trace Membership Candidate Origin
#
# Script type:
#   PROBLEM LEDGER / CANDIDATE-ORIGIN ROUTE OPENER
#
# Purpose
# -------
# Open the safe-trace-membership candidate-origin route for:
#
#   P_safe_membership:
#       zeta_Bs -> T_zeta
#
# Group 32 classified P_safe_membership as a fresh Package B candidate.
# Group 33 narrowed the trace-normalization side of Package B, but did not
# select or adopt N_trace.
#
# This script asks whether safe trace membership can be derived, structurally
# constrained, or honestly left open without using membership to smuggle
# incidence, residual kill, active O, insertion, or parent closure.
#
# Locked-door question:
#
#   Can safe trace membership be justified as a typed trace-sector assignment,
#   or does it remain an explicit candidate choice?
#
# This script does not adopt a safe-membership postulate.
# It does not derive a safe-membership theorem.
# It does not derive trace/residual zero incidence.
# It does not derive residual control.
# It does not derive B_s/F_zeta insertion.
# It does not open active O or parent closure.
#
# Tiny goblin rule:
#
#   Name the cup shelf before claiming the cup is safe.

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
        "ADMISSIBLE_ORIGIN_ROUTE": StatusMark.INFO,
        "COMPATIBILITY_ONLY": StatusMark.INFO,
        "FORBIDDEN_UPGRADE": StatusMark.FAIL,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "ORIGIN_ROUTE": StatusMark.INFO,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REJECTED_AS_SELECTOR": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "THEOREM_TARGET": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g33_summary",
            "33_trace_normalization_candidate_origin__candidate_group_33_status_summary",
            "g33_status_summary",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g33_obligations",
            "33_trace_normalization_candidate_origin__candidate_trace_normalization_obligations",
            "g33_trace_normalization_obligations",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g32_summary",
            "32_explicit_minimal_postulate_selection__candidate_group_32_status_summary",
            "g32_status_summary",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g32_candidate_ledger",
            "32_explicit_minimal_postulate_selection__candidate_postulate_candidate_ledger",
            "g32_postulate_candidate_ledger",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_summary",
            "31_source_divergence_coefficient_law__candidate_group_31_status_summary",
            "source_divergence_group_status_summary_marker",
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
class MembershipSymbols:
    M_safe: sp.Symbol
    zeta_Bs: sp.Symbol
    T_zeta: sp.Symbol
    R_zeta: sp.Symbol
    R_kappa: sp.Symbol
    P_trace_norm: sp.Symbol
    P_incidence_zero: sp.Symbol
    P_active_O: sp.Symbol
    P_residual_kill: sp.Symbol
    P_insertion: sp.Symbol
    P_parent: sp.Symbol
    L_membership_origin: sp.Expr
    L_compatibility: sp.Expr
    L_forbidden_upgrades: sp.Expr
    L_membership_problem_gap: sp.Expr


@dataclass
class OriginRouteEntry:
    name: str
    route: str
    status: str
    allowed_use: str
    forbidden_use: str
    next_test: str


@dataclass
class ForbiddenSelectorEntry:
    name: str
    selector: str
    status: str
    reason: str
    allowed_future_use: str


@dataclass
class InitialObligationEntry:
    name: str
    obligation: str
    status: str
    blocks: str
    discipline: str


@dataclass
class InitialConclusionEntry:
    name: str
    conclusion: str
    status: str
    meaning: str


def case_0_problem(out: ScriptOutput) -> None:
    header("Candidate Safe Trace Membership Origin Problem")
    header("Case 0: Safe trace membership origin problem")
    print("Question:")
    print()
    print("  Can safe trace membership zeta_Bs -> T_zeta be justified as a typed")
    print("  trace-sector assignment, or does it remain an explicit candidate choice?")
    print()
    print("Discipline:")
    print()
    print("  This script opens a safe-membership candidate-origin route.")
    print("  It adopts no safe-membership postulate.")
    print("  It derives no safe-membership theorem.")
    print("  It derives no trace/residual zero incidence.")
    print("  It derives no coefficient law and no insertion.")
    print("  It keeps active O, residual control, and parent closure closed.")
    print()
    print("Tiny goblin rule:")
    print("  Name the cup shelf before claiming the cup is safe.")

    with out.governance_assessments():
        out.line(
            "safe trace membership origin route opened",
            StatusMark.INFO,
            "opening membership-origin route after Group 33 trace-normalization audit",
        )


def case_1_symbolic_ledger(out: ScriptOutput) -> MembershipSymbols:
    header("Case 1: Safe-membership symbolic ledger")

    M_safe = sp.Symbol("M_safe")
    zeta_Bs = sp.Symbol("zeta_Bs")
    T_zeta = sp.Symbol("T_zeta")
    R_zeta = sp.Symbol("R_zeta")
    R_kappa = sp.Symbol("R_kappa")
    P_trace_norm = sp.Symbol("P_trace_norm")
    P_incidence_zero = sp.Symbol("P_incidence_zero")
    P_active_O = sp.Symbol("P_active_O")
    P_residual_kill = sp.Symbol("P_residual_kill")
    P_insertion = sp.Symbol("P_insertion")
    P_parent = sp.Symbol("P_parent")
    C_source_visible = sp.Symbol("C_source_visible")
    C_div_visible = sp.Symbol("C_div_visible")
    C_norm_compat = sp.Symbol("C_norm_compat")

    L_membership_origin = sp.simplify(M_safe + T_zeta + zeta_Bs)
    L_compatibility = sp.simplify(C_source_visible + C_div_visible + C_norm_compat + P_trace_norm)
    L_forbidden_upgrades = sp.simplify(
        P_incidence_zero + P_active_O + P_residual_kill + P_insertion + P_parent + R_zeta + R_kappa
    )
    L_membership_problem_gap = sp.simplify(
        L_membership_origin + L_compatibility + L_forbidden_upgrades
    )

    print("Membership / residual / downstream symbols:")
    for name, value in [
        ("M_safe", M_safe),
        ("zeta_Bs", zeta_Bs),
        ("T_zeta", T_zeta),
        ("R_zeta", R_zeta),
        ("R_kappa", R_kappa),
        ("P_trace_norm", P_trace_norm),
        ("P_incidence_zero", P_incidence_zero),
        ("P_active_O", P_active_O),
        ("P_residual_kill", P_residual_kill),
        ("P_insertion", P_insertion),
        ("P_parent", P_parent),
    ]:
        print(f"  {name} = {value}")

    print()
    print("Membership-origin load:")
    print(f"  L_membership_origin = {L_membership_origin}")
    print()
    print("Compatibility-check load:")
    print(f"  L_compatibility = {L_compatibility}")
    print()
    print("Forbidden-upgrade load:")
    print(f"  L_forbidden_upgrades = {L_forbidden_upgrades}")
    print()
    print("Safe-membership origin problem gap:")
    print(f"  L_membership_problem_gap = {L_membership_problem_gap}")

    with out.derived_results():
        out.line(
            "safe-membership origin ledgers stated",
            StatusMark.OBLIGATION,
            f"L_membership_origin = {L_membership_origin}; L_forbidden_upgrades = {L_forbidden_upgrades}",
        )

    return MembershipSymbols(
        M_safe=M_safe,
        zeta_Bs=zeta_Bs,
        T_zeta=T_zeta,
        R_zeta=R_zeta,
        R_kappa=R_kappa,
        P_trace_norm=P_trace_norm,
        P_incidence_zero=P_incidence_zero,
        P_active_O=P_active_O,
        P_residual_kill=P_residual_kill,
        P_insertion=P_insertion,
        P_parent=P_parent,
        L_membership_origin=L_membership_origin,
        L_compatibility=L_compatibility,
        L_forbidden_upgrades=L_forbidden_upgrades,
        L_membership_problem_gap=L_membership_problem_gap,
    )


def build_origin_routes() -> List[OriginRouteEntry]:
    return [
        OriginRouteEntry(
            name="O1: typed trace-sector membership",
            route="define T_zeta as a typed trace sector and test whether zeta_Bs belongs to it",
            status="ADMISSIBLE_ORIGIN_ROUTE",
            allowed_use="candidate theorem route for safe membership",
            forbidden_use="must not imply zero incidence, residual kill, active O, insertion, or parent closure",
            next_test="define T_zeta domain, zeta_Bs object, and membership criterion",
        ),
        OriginRouteEntry(
            name="O2: domain/codomain assignment",
            route="state the domain of zeta_Bs and the codomain T_zeta before membership is claimed",
            status="ADMISSIBLE_ORIGIN_ROUTE",
            allowed_use="well-posedness route for membership claims",
            forbidden_use="must not use undefined sector labels as proof of membership",
            next_test="inventory domain, codomain, and exclusion zones",
        ),
        OriginRouteEntry(
            name="O3: variable-role separation",
            route="separate zeta_Bs from residual zeta, residual kappa, ordinary source load, and correction load",
            status="ADMISSIBLE_ORIGIN_ROUTE",
            allowed_use="anti-smuggling route for safe membership",
            forbidden_use="must not turn separation into residual kill or source theorem",
            next_test="state residual/source/correction non-membership fences",
        ),
        OriginRouteEntry(
            name="O4: trace-normalization compatibility",
            route="test compatibility with Group 33 compatible-if-declared trace-normalization forms",
            status="COMPATIBILITY_ONLY",
            allowed_use="compatibility check between Package B components",
            forbidden_use="normalization must not choose membership and membership must not choose normalization",
            next_test="carry N_trace as separate candidate node",
        ),
        OriginRouteEntry(
            name="O5: source/divergence visibility compatibility",
            route="test whether membership keeps ordinary source and correction loads visible and non-reservoir",
            status="COMPATIBILITY_ONLY",
            allowed_use="negative filter against hidden load membership forms",
            forbidden_use="visibility compatibility must not become source no-double-counting theorem or divergence-safe law",
            next_test="reject forms that hide source or divergence burden",
        ),
    ]


def case_2_origin_routes(out: ScriptOutput) -> List[OriginRouteEntry]:
    header("Case 2: Admissible membership-origin and compatibility routes")
    routes = build_origin_routes()

    for item in routes:
        subheader(item.name)
        print(f"Route: {item.route}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Allowed use: {item.allowed_use}")
        print(f"Forbidden use: {item.forbidden_use}")
        print(f"Next test: {item.next_test}")

    with out.governance_assessments():
        out.line(
            "safe-membership origin routes initialized",
            StatusMark.INFO,
            f"{len(routes)} origin / compatibility routes initialized",
        )

    return routes


def build_forbidden_selectors() -> List[ForbiddenSelectorEntry]:
    return [
        ForbiddenSelectorEntry(
            name="S1: recovery selector",
            selector="choose membership because AB=1, gamma/PPN, Schwarzschild, weak-field, or kappa=0 recovery works",
            status="REJECTED_AS_SELECTOR",
            reason="recovery may audit after construction but cannot choose safe membership",
            allowed_future_use="post-construction recovery check only",
        ),
        ForbiddenSelectorEntry(
            name="S2: repair selector",
            selector="choose membership because it repairs source, divergence, boundary, residual, coefficient, or matching failure",
            status="REJECTED_AS_SELECTOR",
            reason="failure may reject bad membership forms but cannot select the correct one",
            allowed_future_use="negative filter only",
        ),
        ForbiddenSelectorEntry(
            name="S3: incidence selector",
            selector="choose membership because it makes I(T_zeta,R_zeta)=0 or I(T_zeta,R_kappa)=0 convenient",
            status="REJECTED_AS_SELECTOR",
            reason="zero incidence is separate high-risk theorem/strong-postulate target",
            allowed_future_use="future incidence theorem only after membership is independently defined",
        ),
        ForbiddenSelectorEntry(
            name="S4: residual-kill selector",
            selector="choose membership because it kills residual zeta/kappa trace by declaration",
            status="REJECTED_AS_SELECTOR",
            reason="residual control is not derived and cannot select membership",
            allowed_future_use="future residual-control theorem route only",
        ),
        ForbiddenSelectorEntry(
            name="S5: active-O selector",
            selector="choose membership because it makes active O easier to state",
            status="REJECTED_AS_SELECTOR",
            reason="active O is not constructed and cannot select upstream membership",
            allowed_future_use="future compatibility check only after O exists",
        ),
        ForbiddenSelectorEntry(
            name="S6: insertion selector",
            selector="choose membership because it makes B_s/F_zeta insertion work",
            status="REJECTED_AS_SELECTOR",
            reason="insertion is downstream and not ready",
            allowed_future_use="conditional precondition audit only after adoption or theorem support",
        ),
        ForbiddenSelectorEntry(
            name="S7: parent-fit selector",
            selector="choose membership because it helps close the parent equation",
            status="REJECTED_AS_SELECTOR",
            reason="parent field equation is not ready and cannot choose safe membership",
            allowed_future_use="future parent audit only after upstream gates close",
        ),
    ]


def case_3_forbidden_selectors(out: ScriptOutput) -> List[ForbiddenSelectorEntry]:
    header("Case 3: Rejected safe-membership selector routes")
    selectors = build_forbidden_selectors()

    for item in selectors:
        subheader(item.name)
        print(f"Selector: {item.selector}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Reason: {item.reason}")
        print(f"Allowed future use: {item.allowed_future_use}")

    with out.counterexamples():
        out.line(
            "safe-membership selector shortcuts rejected",
            StatusMark.FAIL,
            "recovery, repair, incidence, residual kill, active-O, insertion, and parent-fit selectors rejected",
        )

    return selectors


def build_initial_obligations() -> List[InitialObligationEntry]:
    return [
        InitialObligationEntry(
            name="O1: membership domain ledger",
            obligation="inventory zeta_Bs, T_zeta, residual zones, source/correction zones, and membership criterion",
            status="OPEN",
            blocks="candidate membership forms",
            discipline="membership objects must be visible before membership is claimed",
        ),
        InitialObligationEntry(
            name="O2: selector rejection ledger",
            obligation="reject recovery, repair, incidence, residual-kill, active-O, insertion, and parent-fit selectors",
            status="OPEN",
            blocks="membership drift",
            discipline="bad selector may reject candidates but not choose membership",
        ),
        InitialObligationEntry(
            name="O3: normalization separation",
            obligation="keep safe membership separate from P_trace_norm and Group 33 compatible-if-declared forms",
            status="OPEN",
            blocks="Package B collapse",
            discipline="membership is not normalization",
        ),
        InitialObligationEntry(
            name="O4: incidence fence",
            obligation="keep safe membership separate from trace/residual zero incidence",
            status="OPEN",
            blocks="residual-control smuggling",
            discipline="membership is not incidence",
        ),
        InitialObligationEntry(
            name="O5: adoption boundary",
            obligation="keep P_safe_membership unadopted unless a separate explicit decision is requested",
            status="REQUIRED",
            blocks="accidental adoption",
            discipline="candidate-origin route is not explicit adoption",
        ),
        InitialObligationEntry(
            name="O6: downstream gates",
            obligation="keep insertion, active O, residual control, and parent equation closed",
            status="NOT_READY",
            blocks="downstream overreach",
            discipline="safe-membership origin is not insertion or parent closure",
        ),
    ]


def case_4_initial_obligations(out: ScriptOutput) -> List[InitialObligationEntry]:
    header("Case 4: Initial safe-membership origin obligations")
    obligations = build_initial_obligations()

    for item in obligations:
        subheader(item.name)
        print(f"Obligation: {item.obligation}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Blocks: {item.blocks}")
        print(f"Discipline: {item.discipline}")

    with out.unresolved_obligations():
        out.line(
            "initial safe-membership origin obligations stated",
            StatusMark.OBLIGATION,
            f"{len(obligations)} obligations opened",
        )

    return obligations


def build_initial_conclusions() -> List[InitialConclusionEntry]:
    return [
        InitialConclusionEntry(
            name="C1: route opened",
            conclusion="safe trace membership candidate-origin route is opened",
            status="ORIGIN_ROUTE",
            meaning="next route after trace-normalization origin audit, without adoption",
        ),
        InitialConclusionEntry(
            name="C2: no derivation yet",
            conclusion="this opener derives no safe-membership theorem",
            status="NOT_DERIVED",
            meaning="origin routes are listed, not solved",
        ),
        InitialConclusionEntry(
            name="C3: selectors rejected",
            conclusion="recovery, repair, incidence, active-O, insertion, and parent-fit selectors are rejected",
            status="REQUIRED",
            meaning="membership must not be chosen from target success, repair need, or downstream convenience",
        ),
        InitialConclusionEntry(
            name="C4: no adoption",
            conclusion="this opener adopts no safe-membership postulate",
            status="NOT_ADOPTED",
            meaning="separate explicit decision required for adoption",
        ),
        InitialConclusionEntry(
            name="C5: downstream gates",
            conclusion="B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready",
            status="NOT_READY",
            meaning="origin problem does not open downstream gates",
        ),
        InitialConclusionEntry(
            name="C6: next",
            conclusion="safe-membership domain ledger should run next",
            status="OPEN",
            meaning="first concrete membership-object audit",
        ),
    ]


def case_5_initial_conclusions(out: ScriptOutput) -> List[InitialConclusionEntry]:
    header("Case 5: Initial safe-membership origin conclusions")
    conclusions = build_initial_conclusions()

    for item in conclusions:
        subheader(item.name)
        print(f"Conclusion: {item.conclusion}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Meaning: {item.meaning}")

    with out.governance_assessments():
        out.line(
            "safe-membership origin problem conclusion stated",
            StatusMark.PASS,
            "origin route opened; no membership adopted; selector shortcuts rejected; downstream gates closed",
        )

    return conclusions


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Safe trace membership origin opener result:")
    print()
    print("  Group 34 is opened as a candidate-origin route for P_safe_membership.")
    print("  The route asks whether zeta_Bs -> T_zeta can be justified as typed trace-sector membership.")
    print("  Typed trace-sector, domain/codomain, and variable-role separation routes are admissible to test.")
    print("  Trace-normalization, source/divergence, and guardrail relations are compatibility checks only.")
    print("  Recovery, repair, incidence, residual-kill, active-O, insertion, and parent-fit selectors are rejected.")
    print("  No safe-membership theorem is derived or adopted by this opener.")
    print("  B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready.")
    print()
    print("Possible next script:")
    print("  candidate_safe_trace_membership_domain_ledger.py")
    print()
    print("Tiny goblin label:")
    print("  Name the cup shelf before claiming the cup is safe.")

    with out.governance_assessments():
        out.line(
            "safe trace membership origin opener complete",
            StatusMark.PASS,
            "domain ledger should run next; adoption and downstream gates remain closed",
        )


def record_inventory_marker(ns, symbols: MembershipSymbols) -> None:
    ns.record_derivation(
        derivation_id="g34_safe_membership_origin_problem",
        inputs=[symbols.M_safe, symbols.zeta_Bs, symbols.T_zeta],
        output=symbols.L_membership_problem_gap,
        method="safe trace membership origin problem ledger",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="origin_problem_marker",
        is_placeholder=True,
    )


def record_governance(
    ns,
    routes: List[OriginRouteEntry],
    selectors: List[ForbiddenSelectorEntry],
    conclusions: List[InitialConclusionEntry],
) -> None:
    obligation_ids = [
        "g34_origin_obligation_o1",
        "g34_origin_obligation_o2",
        "g34_origin_obligation_o3",
        "g34_origin_obligation_o4",
        "g34_origin_obligation_o5",
        "g34_origin_obligation_o6",
    ]

    ns.record_route(
        RouteRecord(
            route_id="g34_safe_membership_origin_route",
            script_id=SCRIPT_ID,
            name="Safe trace membership candidate-origin route",
            status=GovernanceStatus.CANDIDATE_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            required_obligations=obligation_ids,
            activation_conditions=[
                "Group 32 leaves P_safe_membership as fresh candidate",
                "Group 33 leaves trace normalization compatible-if-declared only",
                "membership must not imply incidence, residual control, active O, insertion, or parent closure",
            ],
        )
    )

    for item in routes:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_route(
            RouteRecord(
                route_id=f"g34_membership_origin_{ident}",
                script_id=SCRIPT_ID,
                name=item.name,
                status=GovernanceStatus.CANDIDATE_ROUTE,
                tier=ClaimTier.CONSTRAINED,
                required_obligations=obligation_ids,
                activation_conditions=[
                    item.route,
                    f"Allowed use: {item.allowed_use}",
                    f"Forbidden use: {item.forbidden_use}",
                    f"Next test: {item.next_test}",
                ],
            )
        )

    for item in selectors:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g34_selector_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.REJECTED_ROUTE,
                statement=(
                    f"{item.selector}. Rejected as selector: {item.reason}. "
                    f"Allowed future use: {item.allowed_future_use}."
                ),
                derivation_ids=["g34_safe_membership_origin_problem"],
                obligation_ids=obligation_ids,
            )
        )

    for item in conclusions:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g34_origin_conclusion_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=(
                    GovernanceStatus.DEFERRED_PENDING_PREREQUISITES
                    if item.status in {"NOT_READY", "NOT_DERIVED", "NOT_ADOPTED", "OPEN"}
                    else GovernanceStatus.CANDIDATE_ROUTE
                ),
                statement=f"{item.conclusion}. Meaning: {item.meaning}.",
                derivation_ids=["g34_safe_membership_origin_problem"],
                obligation_ids=obligation_ids,
            )
        )


def record_obligations(ns, obligations: List[InitialObligationEntry]) -> None:
    for item in obligations:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_obligation(
            ProofObligationRecord(
                obligation_id=f"g34_origin_obligation_{ident}",
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
    print_archive_status(ns, invalidated)

    case_0_problem(out)
    symbols = case_1_symbolic_ledger(out)
    routes = case_2_origin_routes(out)
    selectors = case_3_forbidden_selectors(out)
    obligations = case_4_initial_obligations(out)
    conclusions = case_5_initial_conclusions(out)
    final_interpretation(out)

    record_inventory_marker(ns, symbols)
    record_obligations(ns, obligations)
    record_governance(ns, routes, selectors, conclusions)

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
