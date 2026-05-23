# Candidate trace normalization postulate
#
# Group:
#   30_minimal_coefficient_sector_postulate_inventory
#
# Script type:
#   TRACE-NORMALIZATION POSTULATE AUDIT
#
# Purpose
# -------
# Audit whether a trace-normalization postulate should be retained as an
# explicit admissible candidate.
#
# Locked-door question:
#
#   Is trace normalization a minimal admissible postulate candidate, or should
#   it remain a theorem target?
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
#   Measuring the tooth is not biting the lock.

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
        "CONDITIONAL_RETAIN": StatusMark.DEFER,
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
            "g30_filter",
            "30_minimal_coefficient_sector_postulate_inventory__candidate_postulate_smuggling_filter",
            "g30_postulate_smuggling_filter",
            RecordKind.INVENTORY_MARKER,
        ),
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
class TraceNormSymbols:
    zeta: sp.Symbol
    gamma: sp.Symbol
    B_s: sp.Symbol
    c_trace: sp.Symbol
    P_trace_norm: sp.Symbol
    N_trace: sp.Symbol
    recovery_gap: sp.Symbol
    normalization_gap: sp.Symbol
    membership_gap: sp.Symbol
    source_gap: sp.Symbol
    divergence_gap: sp.Symbol
    insertion_gap: sp.Symbol
    trace_norm_load: sp.Expr


@dataclass
class TraceNormCriterion:
    name: str
    criterion: str
    status: str
    result: str
    caveat: str


@dataclass
class TraceNormBoundary:
    name: str
    boundary: str
    status: str
    reason: str


@dataclass
class TraceNormObligation:
    name: str
    obligation: str
    status: str
    blocks: str
    discipline: str


@dataclass
class TraceNormConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_symbols() -> TraceNormSymbols:
    (
        zeta,
        gamma,
        B_s,
        c_trace,
        P_trace_norm,
        N_trace,
        recovery_gap,
        normalization_gap,
        membership_gap,
        source_gap,
        divergence_gap,
        insertion_gap,
    ) = sp.symbols(
        "zeta gamma B_s c_trace P_trace_norm N_trace "
        "recovery_gap normalization_gap membership_gap source_gap divergence_gap insertion_gap",
        real=True,
    )

    trace_norm_load = sp.simplify(
        recovery_gap
        + normalization_gap
        + membership_gap
        + source_gap
        + divergence_gap
        + insertion_gap
    )

    return TraceNormSymbols(
        zeta=zeta,
        gamma=gamma,
        B_s=B_s,
        c_trace=c_trace,
        P_trace_norm=P_trace_norm,
        N_trace=N_trace,
        recovery_gap=recovery_gap,
        normalization_gap=normalization_gap,
        membership_gap=membership_gap,
        source_gap=source_gap,
        divergence_gap=divergence_gap,
        insertion_gap=insertion_gap,
        trace_norm_load=trace_norm_load,
    )


def build_criteria() -> List[TraceNormCriterion]:
    return [
        TraceNormCriterion(
            name="C1: volume-trace anchor",
            criterion="normalization acts only on zeta = ln sqrt(gamma) / volume-trace scalar",
            status="ADMISSIBLE_CANDIDATE",
            result="structural target exists from Group 29",
            caveat="does not derive numerical coefficient",
        ),
        TraceNormCriterion(
            name="C2: narrowness",
            criterion="postulate states how B_s reads zeta and nothing else",
            status="ADMISSIBLE_CANDIDATE",
            result="minimal if it does not imply membership, incidence, source, divergence, or insertion",
            caveat="must not be bundled",
        ),
        TraceNormCriterion(
            name="C3: recovery independence",
            criterion="normalization is not selected from AB=1, B=1/A, Schwarzschild, gamma/PPN, weak-field, or kappa=0",
            status="REQUIRED",
            result="required by smuggling filter",
            caveat="recovery may audit only later",
        ),
        TraceNormCriterion(
            name="C4: membership separation",
            criterion="trace normalization does not imply zeta_Bs -> T_zeta membership",
            status="REQUIRED",
            result="membership remains separate candidate",
            caveat="do not make normalization into sector rule",
        ),
        TraceNormCriterion(
            name="C5: insertion separation",
            criterion="trace normalization does not derive B_s/F_zeta insertion",
            status="REQUIRED",
            result="insertion gate remains closed",
            caveat="normalization is one missing tooth, not whole key",
        ),
        TraceNormCriterion(
            name="C6: theorem-route openness",
            criterion="normalization may remain theorem target if a source/divergence law later fixes it",
            status="OPEN",
            result="retain as candidate postulate, not adopted",
            caveat="future theorem route may supersede explicit choice",
        ),
    ]


def build_boundaries() -> List[TraceNormBoundary]:
    return [
        TraceNormBoundary(
            name="B1: no recovery selection",
            boundary="do not choose c_trace to make recovery work",
            status="REJECTED",
            reason="endpoint-selected normalization is smuggling",
        ),
        TraceNormBoundary(
            name="B2: no source rule",
            boundary="do not let trace-normalization define source no-double-counting",
            status="REJECTED",
            reason="source discipline is separate",
        ),
        TraceNormBoundary(
            name="B3: no membership theorem",
            boundary="do not let trace-normalization prove zeta_Bs -> T_zeta",
            status="REJECTED",
            reason="membership is separate candidate",
        ),
        TraceNormBoundary(
            name="B4: no zero incidence",
            boundary="do not let trace-normalization imply I(T_zeta,R_zeta)=0 or I(T_zeta,R_kappa)=0",
            status="REJECTED",
            reason="incidence is high-risk and separate",
        ),
        TraceNormBoundary(
            name="B5: no residual control",
            boundary="do not let trace-normalization kill or inert residuals",
            status="REJECTED",
            reason="residual control remains not derived",
        ),
        TraceNormBoundary(
            name="B6: no parent closure",
            boundary="do not let trace-normalization open parent equation",
            status="REJECTED",
            reason="parent gate remains closed",
        ),
    ]


def build_obligations() -> List[TraceNormObligation]:
    return [
        TraceNormObligation(
            name="O1: keep as candidate",
            obligation="retain trace-normalization as admissible candidate postulate, not adopted",
            status="OPEN",
            blocks="postulate inventory closure",
            discipline="explicit choice only if later selected",
        ),
        TraceNormObligation(
            name="O2: define narrow form",
            obligation="state candidate as B_s reading rule for zeta only",
            status="REQUIRED",
            blocks="minimality",
            discipline="do not bundle membership/source/divergence/insertion",
        ),
        TraceNormObligation(
            name="O3: theorem-route check",
            obligation="leave room for source/divergence theorem route to fix normalization",
            status="OPEN",
            blocks="future derivation",
            discipline="do not postulate prematurely",
        ),
        TraceNormObligation(
            name="O4: safe-membership audit next",
            obligation="audit safe-trace membership candidate separately",
            status="OPEN",
            blocks="sector membership",
            discipline="normalization is not membership",
        ),
        TraceNormObligation(
            name="O5: downstream gates",
            obligation="keep insertion, active O, residual control, and parent equation closed",
            status="NOT_READY",
            blocks="premature closure",
            discipline="normalization audit is not insertion",
        ),
    ]


def build_conclusions() -> List[TraceNormConclusion]:
    return [
        TraceNormConclusion(
            name="R1: status",
            conclusion="trace-normalization survives as admissible candidate postulate",
            status="ADMISSIBLE_CANDIDATE",
            meaning="it is narrow and structural if not recovery-selected",
        ),
        TraceNormConclusion(
            name="R2: adoption",
            conclusion="trace-normalization is not adopted",
            status="NOT_ADOPTED",
            meaning="this audit retains candidate status only",
        ),
        TraceNormConclusion(
            name="R3: theorem target",
            conclusion="trace-normalization may still be theorem target",
            status="THEOREM_TARGET",
            meaning="source/divergence law may later fix it",
        ),
        TraceNormConclusion(
            name="R4: separation",
            conclusion="normalization does not imply membership, incidence, source, divergence, or insertion",
            status="REQUIRED",
            meaning="one tooth only",
        ),
        TraceNormConclusion(
            name="R5: next",
            conclusion="safe-trace membership postulate audit should run next",
            status="OPEN",
            meaning="membership must be assessed separately",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Trace-normalization postulate problem")
    print("Question:")
    print()
    print("  Is trace normalization a minimal admissible postulate candidate, or should it remain a theorem target?")
    print()
    print("Discipline:")
    print()
    print("  This audit retains or rejects candidate status.")
    print("  It adopts no postulate.")
    print("  It derives no insertion.")
    print()
    print("Tiny goblin rule:")
    print("  Measuring the tooth is not biting the lock.")

    with out.governance_assessments():
        out.line(
            "trace-normalization postulate audit opened",
            StatusMark.INFO,
            "testing trace-normalization candidate without adoption",
        )


def case_1_symbolic_ledger(symbols: TraceNormSymbols, out: ScriptOutput) -> None:
    header("Case 1: Trace-normalization symbolic ledger")
    print("Trace-normalization symbols:")
    print()
    for name in [
        "zeta",
        "gamma",
        "B_s",
        "c_trace",
        "P_trace_norm",
        "N_trace",
        "recovery_gap",
        "normalization_gap",
        "membership_gap",
        "source_gap",
        "divergence_gap",
        "insertion_gap",
    ]:
        print(f"  {name} = {sp.sstr(getattr(symbols, name))}")
    print()
    print("Trace-normalization load:")
    print()
    print(f"  L_trace_normalization = {sp.sstr(symbols.trace_norm_load)}")

    with out.derived_results():
        out.line(
            "trace-normalization load stated",
            StatusMark.OBLIGATION,
            f"L_trace_normalization = {sp.sstr(symbols.trace_norm_load)}",
        )


def case_2_criteria(items: List[TraceNormCriterion], out: ScriptOutput) -> None:
    header("Case 2: Trace-normalization admissibility criteria")
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
            "trace-normalization criteria evaluated",
            StatusMark.DEFER,
            f"{len(items)} trace-normalization criteria evaluated",
        )


def case_3_boundaries(items: List[TraceNormBoundary], out: ScriptOutput) -> None:
    header("Case 3: Trace-normalization rejected upgrades")
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
            "trace-normalization forbidden upgrades rejected",
            StatusMark.FAIL,
            "recovery selection, source rule, membership theorem, incidence, residual control, and parent closure rejected",
        )


def case_4_obligations(items: List[TraceNormObligation], out: ScriptOutput) -> None:
    header("Case 4: Trace-normalization obligations")
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
            "trace-normalization obligations stated",
            StatusMark.OBLIGATION,
            f"{len(items)} trace-normalization obligations remain",
        )


def case_5_conclusions(items: List[TraceNormConclusion], out: ScriptOutput) -> None:
    header("Case 5: Trace-normalization conclusions")
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
            "trace-normalization conclusion stated",
            StatusMark.PASS,
            "trace-normalization retained as admissible candidate; no adoption",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Trace-normalization postulate audit result:")
    print()
    print("  Trace-normalization survives as an admissible candidate postulate.")
    print("  It is not adopted.")
    print("  It may also remain a theorem target if source/divergence law later fixes it.")
    print("  The candidate is narrow only if it states how B_s reads zeta and nothing else.")
    print("  It does not imply membership, incidence, source no-double-counting, divergence safety, insertion, residual control, active O, or parent closure.")
    print()
    print("Possible next script:")
    print("  candidate_safe_trace_membership_postulate.py")
    print()
    print("Tiny goblin label:")
    print("  Measuring the tooth is not biting the lock.")

    with out.governance_assessments():
        out.line(
            "trace-normalization postulate audit complete",
            StatusMark.PASS,
            "safe-trace membership postulate audit should run next",
        )


def record_derivations(ns, symbols: TraceNormSymbols) -> None:
    ns.record_derivation(
        derivation_id="g30_trace_normalization",
        inputs=[
            symbols.recovery_gap,
            symbols.normalization_gap,
            symbols.membership_gap,
            symbols.source_gap,
            symbols.divergence_gap,
            symbols.insertion_gap,
        ],
        output=symbols.trace_norm_load,
        method="audit trace-normalization as admissible candidate postulate without adoption",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="trace_normalization_postulate_marker",
        scope="Group 30 minimal coefficient/sector postulate inventory",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g30_tn_candidate", "Retain trace-normalization as candidate only"),
        ("g30_tn_narrow", "Define trace-normalization narrowly"),
        ("g30_tn_theorem_route", "Keep source/divergence theorem route open"),
        ("g30_tn_no_recovery", "Reject recovery-selected normalization"),
        ("g30_tn_no_bundle", "Do not bundle normalization with membership/source/divergence/insertion"),
        ("g30_tn_next_membership", "Audit safe-trace membership next"),
        ("g30_tn_downstream", "Keep insertion/O/residual/parent gates closed"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g30_tn_route"],
            description=(
                "Trace-normalization survives as admissible candidate only. No postulate is adopted and no downstream theorem is derived."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g30_tn_candidate",
        "g30_tn_narrow",
        "g30_tn_theorem_route",
        "g30_tn_no_recovery",
        "g30_tn_no_bundle",
        "g30_tn_next_membership",
        "g30_tn_downstream",
    ]

    ns.record_route(RouteRecord(
        route_id="g30_tn_route",
        script_id=SCRIPT_ID,
        name="Group 30 trace-normalization postulate audit route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "trace-normalization retained as admissible candidate only",
            "normalization is not recovery-selected",
            "normalization is not membership/source/divergence/insertion",
            "no postulate is adopted",
            "downstream gates remain closed",
        ],
    ))

    for branch_id in [
        "trace_norm_selected_by_recovery",
        "trace_norm_as_source_rule",
        "trace_norm_as_membership_theorem",
        "trace_norm_as_zero_incidence",
        "trace_norm_as_residual_control",
        "trace_norm_as_insertion",
        "trace_norm_as_active_O",
        "trace_norm_as_parent_closure",
        "trace_norm_adopted_here",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; trace-normalization audit is not adoption or theorem closure.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g30_trace_normalization_candidate",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Trace-normalization survives as an admissible candidate postulate, but is not adopted. It may also remain a theorem target if source/divergence law later fixes it. "
            "The candidate is narrow only if it states how B_s reads zeta and nothing else. It does not imply membership, incidence, source no-double-counting, divergence safety, insertion, residual control, active O, or parent closure."
        ),
        derivation_ids=["g30_trace_normalization"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Trace Normalization Postulate")
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
