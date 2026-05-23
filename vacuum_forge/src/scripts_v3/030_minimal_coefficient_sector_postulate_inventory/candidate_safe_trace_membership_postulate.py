# Candidate safe trace membership postulate
#
# Group:
#   30_minimal_coefficient_sector_postulate_inventory
#
# Script type:
#   SAFE-TRACE MEMBERSHIP POSTULATE AUDIT
#
# Purpose
# -------
# Audit whether zeta_Bs -> T_zeta should be retained as an explicit
# safe-trace membership candidate.
#
# Locked-door question:
#
#   Is safe-trace membership a minimal admissible postulate candidate,
#   or should it remain a theorem target?
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
#   Naming the shelf is not locking the monsters away.

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
        "CANDIDATE_POSTULATE": StatusMark.OBLIGATION,
        "CONSTRAINED_CANDIDATE": StatusMark.INFO,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
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
            "g30_trace_norm",
            "030_minimal_coefficient_sector_postulate_inventory__candidate_trace_normalization_postulate",
            "g30_trace_normalization",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g30_filter",
            "030_minimal_coefficient_sector_postulate_inventory__candidate_postulate_smuggling_filter",
            "g30_postulate_smuggling_filter",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g30_minimality",
            "030_minimal_coefficient_sector_postulate_inventory__candidate_postulate_minimality_tests",
            "g30_postulate_minimality",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g30_problem",
            "030_minimal_coefficient_sector_postulate_inventory__candidate_minimal_postulate_problem_ledger",
            "g30_postulate_problem",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g29_summary",
            "029_Bs_Fzeta_coefficient_origin__candidate_group_29_status_summary",
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
class MembershipSymbols:
    zeta_Bs: sp.Symbol
    T_zeta: sp.Symbol
    R_zeta: sp.Symbol
    R_kappa: sp.Symbol
    P_safe_membership: sp.Symbol
    M_safe: sp.Symbol
    incidence_gap: sp.Symbol
    residual_gap: sp.Symbol
    source_gap: sp.Symbol
    insertion_gap: sp.Symbol
    recovery_gap: sp.Symbol
    parent_gap: sp.Symbol
    membership_load: sp.Expr


@dataclass
class MembershipCriterion:
    name: str
    criterion: str
    status: str
    result: str
    caveat: str


@dataclass
class MembershipBoundary:
    name: str
    boundary: str
    status: str
    reason: str


@dataclass
class MembershipObligation:
    name: str
    obligation: str
    status: str
    blocks: str
    discipline: str


@dataclass
class MembershipConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_symbols() -> MembershipSymbols:
    (
        zeta_Bs,
        T_zeta,
        R_zeta,
        R_kappa,
        P_safe_membership,
        M_safe,
        incidence_gap,
        residual_gap,
        source_gap,
        insertion_gap,
        recovery_gap,
        parent_gap,
    ) = sp.symbols(
        "zeta_Bs T_zeta R_zeta R_kappa P_safe_membership M_safe "
        "incidence_gap residual_gap source_gap insertion_gap recovery_gap parent_gap",
        real=True,
    )

    membership_load = sp.simplify(
        incidence_gap + residual_gap + source_gap + insertion_gap + recovery_gap + parent_gap
    )

    return MembershipSymbols(
        zeta_Bs=zeta_Bs,
        T_zeta=T_zeta,
        R_zeta=R_zeta,
        R_kappa=R_kappa,
        P_safe_membership=P_safe_membership,
        M_safe=M_safe,
        incidence_gap=incidence_gap,
        residual_gap=residual_gap,
        source_gap=source_gap,
        insertion_gap=insertion_gap,
        recovery_gap=recovery_gap,
        parent_gap=parent_gap,
        membership_load=membership_load,
    )


def build_criteria() -> List[MembershipCriterion]:
    return [
        MembershipCriterion(
            name="C1: constrained anchor",
            criterion="zeta_Bs -> T_zeta was structurally strengthened by Group 29",
            status="CONSTRAINED_CANDIDATE",
            result="candidate has real volume/trace support",
            caveat="not complete membership theorem",
        ),
        MembershipCriterion(
            name="C2: narrowness",
            criterion="postulate assigns zeta_Bs to safe trace channel and nothing else",
            status="ADMISSIBLE_CANDIDATE",
            result="minimal if it does not imply incidence, source routing, residual control, or insertion",
            caveat="must not be bundled",
        ),
        MembershipCriterion(
            name="C3: normalization separation",
            criterion="safe membership does not fix trace normalization",
            status="REQUIRED",
            result="normalization remains separate candidate/theorem target",
            caveat="do not make membership into coefficient law",
        ),
        MembershipCriterion(
            name="C4: incidence separation",
            criterion="safe membership does not imply I(T_zeta,R_zeta)=0 or I(T_zeta,R_kappa)=0",
            status="REQUIRED",
            result="incidence remains high-risk separate candidate",
            caveat="do not turn shelf label into monster lock",
        ),
        MembershipCriterion(
            name="C5: recovery independence",
            criterion="safe membership is not selected because recovery works",
            status="REQUIRED",
            result="required by smuggling filter",
            caveat="recovery may audit only later",
        ),
        MembershipCriterion(
            name="C6: theorem-route openness",
            criterion="safe membership may remain theorem target if later sector/source/divergence law derives it",
            status="OPEN",
            result="retain candidate status, not adopted",
            caveat="future theorem route may supersede explicit choice",
        ),
    ]


def build_boundaries() -> List[MembershipBoundary]:
    return [
        MembershipBoundary(
            name="B1: no no-overlap theorem",
            boundary="do not let safe membership imply no-overlap sector geometry",
            status="REJECTED",
            reason="complete sector geometry remains not derived",
        ),
        MembershipBoundary(
            name="B2: no zero incidence",
            boundary="do not let safe membership imply I(T_zeta,R_zeta)=0 or I(T_zeta,R_kappa)=0",
            status="REJECTED",
            reason="incidence remains separate and high-risk",
        ),
        MembershipBoundary(
            name="B3: no residual control",
            boundary="do not let safe membership kill, inert, absorb, or hide residuals",
            status="REJECTED",
            reason="residuals remain visible and live",
        ),
        MembershipBoundary(
            name="B4: no source routing",
            boundary="do not let safe membership prove source no-double-counting",
            status="REJECTED",
            reason="source discipline is separate",
        ),
        MembershipBoundary(
            name="B5: no insertion",
            boundary="do not let safe membership derive B_s/F_zeta insertion",
            status="REJECTED",
            reason="insertion gate remains closed",
        ),
        MembershipBoundary(
            name="B6: no parent closure",
            boundary="do not let safe membership open parent equation",
            status="REJECTED",
            reason="parent gate remains closed",
        ),
    ]


def build_obligations() -> List[MembershipObligation]:
    return [
        MembershipObligation(
            name="O1: keep as candidate",
            obligation="retain safe-trace membership as admissible candidate postulate, not adopted",
            status="OPEN",
            blocks="postulate inventory closure",
            discipline="explicit choice only if later selected",
        ),
        MembershipObligation(
            name="O2: define narrow form",
            obligation="state candidate as zeta_Bs -> T_zeta membership only",
            status="REQUIRED",
            blocks="minimality",
            discipline="do not bundle incidence/source/residual/insertion",
        ),
        MembershipObligation(
            name="O3: incidence audit next",
            obligation="audit trace/residual incidence separately",
            status="OPEN",
            blocks="no-overlap/residual-control honesty",
            discipline="membership is not incidence",
        ),
        MembershipObligation(
            name="O4: theorem-route check",
            obligation="leave room for sector/source/divergence theorem route to derive membership",
            status="OPEN",
            blocks="future derivation",
            discipline="do not postulate prematurely",
        ),
        MembershipObligation(
            name="O5: downstream gates",
            obligation="keep insertion, active O, residual control, and parent equation closed",
            status="NOT_READY",
            blocks="premature closure",
            discipline="membership audit is not insertion",
        ),
    ]


def build_conclusions() -> List[MembershipConclusion]:
    return [
        MembershipConclusion(
            name="R1: status",
            conclusion="safe-trace membership survives as admissible candidate postulate",
            status="ADMISSIBLE_CANDIDATE",
            meaning="it is narrow if it only assigns zeta_Bs to T_zeta",
        ),
        MembershipConclusion(
            name="R2: adoption",
            conclusion="safe-trace membership is not adopted",
            status="NOT_ADOPTED",
            meaning="this audit retains candidate status only",
        ),
        MembershipConclusion(
            name="R3: theorem target",
            conclusion="safe-trace membership may still be theorem target",
            status="THEOREM_TARGET",
            meaning="future sector/source/divergence law may derive it",
        ),
        MembershipConclusion(
            name="R4: separation",
            conclusion="membership does not imply incidence, source routing, residual control, or insertion",
            status="REQUIRED",
            meaning="one shelf label only",
        ),
        MembershipConclusion(
            name="R5: next",
            conclusion="trace/residual incidence candidate should be audited next",
            status="OPEN",
            meaning="incidence is high-risk and must be assessed separately",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Safe-trace membership postulate problem")
    print("Question:")
    print()
    print("  Is safe-trace membership a minimal admissible postulate candidate, or should it remain a theorem target?")
    print()
    print("Discipline:")
    print()
    print("  This audit retains or rejects candidate status.")
    print("  It adopts no postulate.")
    print("  It derives no insertion.")
    print()
    print("Tiny goblin rule:")
    print("  Naming the shelf is not locking the monsters away.")

    with out.governance_assessments():
        out.line(
            "safe-trace membership postulate audit opened",
            StatusMark.INFO,
            "testing zeta_Bs -> T_zeta candidate without adoption",
        )


def case_1_symbolic_ledger(symbols: MembershipSymbols, out: ScriptOutput) -> None:
    header("Case 1: Safe-trace membership symbolic ledger")
    print("Membership symbols:")
    print()
    for name in [
        "zeta_Bs",
        "T_zeta",
        "R_zeta",
        "R_kappa",
        "P_safe_membership",
        "M_safe",
        "incidence_gap",
        "residual_gap",
        "source_gap",
        "insertion_gap",
        "recovery_gap",
        "parent_gap",
    ]:
        print(f"  {name} = {sp.sstr(getattr(symbols, name))}")
    print()
    print("Safe-trace membership load:")
    print()
    print(f"  L_safe_trace_membership = {sp.sstr(symbols.membership_load)}")

    with out.derived_results():
        out.line(
            "safe-trace membership load stated",
            StatusMark.OBLIGATION,
            f"L_safe_trace_membership = {sp.sstr(symbols.membership_load)}",
        )


def case_2_criteria(items: List[MembershipCriterion], out: ScriptOutput) -> None:
    header("Case 2: Safe-trace membership admissibility criteria")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Criterion: {item.criterion}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Result: {item.result}")
        print(f"Caveat: {item.caveat}")

    with out.governance_assessments():
        out.line(
            "safe-trace membership criteria evaluated",
            StatusMark.DEFER,
            f"{len(items)} safe-trace membership criteria evaluated",
        )


def case_3_boundaries(items: List[MembershipBoundary], out: ScriptOutput) -> None:
    header("Case 3: Safe-trace membership rejected upgrades")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Boundary: {item.boundary}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Reason: {item.reason}")

    with out.counterexamples():
        out.line(
            "safe-trace membership forbidden upgrades rejected",
            StatusMark.FAIL,
            "no-overlap, zero incidence, residual control, source routing, insertion, and parent closure rejected",
        )


def case_4_obligations(items: List[MembershipObligation], out: ScriptOutput) -> None:
    header("Case 4: Safe-trace membership obligations")
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
            "safe-trace membership obligations stated",
            StatusMark.OBLIGATION,
            f"{len(items)} safe-trace membership obligations remain",
        )


def case_5_conclusions(items: List[MembershipConclusion], out: ScriptOutput) -> None:
    header("Case 5: Safe-trace membership conclusions")
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
            "safe-trace membership conclusion stated",
            StatusMark.PASS,
            "safe-trace membership retained as admissible candidate; no adoption",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Safe-trace membership postulate audit result:")
    print()
    print("  zeta_Bs -> T_zeta survives as an admissible candidate postulate.")
    print("  It is not adopted.")
    print("  It may also remain a theorem target if a later sector/source/divergence law derives it.")
    print("  The candidate is narrow only if it assigns zeta_Bs to T_zeta and nothing else.")
    print("  It does not imply normalization, incidence, no-overlap, source no-double-counting, insertion, residual control, active O, or parent closure.")
    print()
    print("Possible next script:")
    print("  candidate_incidence_source_divergence_postulate_inventory.py")
    print()
    print("Tiny goblin label:")
    print("  Naming the shelf is not locking the monsters away.")

    with out.governance_assessments():
        out.line(
            "safe-trace membership postulate audit complete",
            StatusMark.PASS,
            "incidence/source/divergence postulate inventory should run next",
        )


def record_derivations(ns, symbols: MembershipSymbols) -> None:
    ns.record_derivation(
        derivation_id="g30_safe_membership",
        inputs=[
            symbols.incidence_gap,
            symbols.residual_gap,
            symbols.source_gap,
            symbols.insertion_gap,
            symbols.recovery_gap,
            symbols.parent_gap,
        ],
        output=symbols.membership_load,
        method="audit safe-trace membership as admissible candidate postulate without adoption",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="safe_trace_membership_postulate_marker",
        scope="Group 30 minimal coefficient/sector postulate inventory",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g30_sm_candidate", "Retain safe-trace membership as candidate only"),
        ("g30_sm_narrow", "Define safe-trace membership narrowly"),
        ("g30_sm_theorem_route", "Keep sector/source/divergence theorem route open"),
        ("g30_sm_no_recovery", "Reject recovery-selected membership"),
        ("g30_sm_no_incidence_bundle", "Do not bundle membership with incidence/no-overlap"),
        ("g30_sm_next_incidence", "Audit incidence/source/divergence next"),
        ("g30_sm_downstream", "Keep insertion/O/residual/parent gates closed"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g30_sm_route"],
            description=(
                "Safe-trace membership survives as admissible candidate only. No postulate is adopted and no downstream theorem is derived."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g30_sm_candidate",
        "g30_sm_narrow",
        "g30_sm_theorem_route",
        "g30_sm_no_recovery",
        "g30_sm_no_incidence_bundle",
        "g30_sm_next_incidence",
        "g30_sm_downstream",
    ]

    ns.record_route(RouteRecord(
        route_id="g30_sm_route",
        script_id=SCRIPT_ID,
        name="Group 30 safe-trace membership postulate audit route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "safe-trace membership retained as admissible candidate only",
            "membership is not recovery-selected",
            "membership is not incidence/no-overlap/source/insertion",
            "no postulate is adopted",
            "downstream gates remain closed",
        ],
    ))

    for branch_id in [
        "safe_membership_selected_by_recovery",
        "safe_membership_as_no_overlap",
        "safe_membership_as_zero_incidence",
        "safe_membership_as_source_routing",
        "safe_membership_as_residual_control",
        "safe_membership_as_insertion",
        "safe_membership_as_active_O",
        "safe_membership_as_parent_closure",
        "safe_membership_adopted_here",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; safe-trace membership audit is not adoption or theorem closure.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g30_safe_membership_candidate",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "zeta_Bs -> T_zeta survives as an admissible candidate postulate, but is not adopted. It may also remain a theorem target if a later sector/source/divergence law derives it. "
            "The candidate is narrow only if it assigns zeta_Bs to T_zeta and nothing else. It does not imply normalization, incidence, no-overlap, source no-double-counting, insertion, residual control, active O, or parent closure."
        ),
        derivation_ids=["g30_safe_membership"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Safe Trace Membership Postulate")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    criteria = build_criteria()
    boundaries = build_boundaries()
    obligations = build_obligations()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_symbolic_ledger(symbols, out)
    case_2_criteria(criteria, out)
    case_3_boundaries(boundaries, out)
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
