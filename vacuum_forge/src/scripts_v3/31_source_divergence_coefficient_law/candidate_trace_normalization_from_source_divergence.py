# Candidate trace normalization from source divergence
#
# Group:
#   31_source_divergence_coefficient_law
#
# Script type:
#   TRACE-NORMALIZATION SOURCE/DIVERGENCE FORK
#
# Purpose
# -------
# Test whether source/divergence constraints force trace normalization or leave it open.
#
# Locked-door question:
#
#   Does source/divergence discipline determine how B_s reads zeta,
#   or does trace normalization remain an open candidate/theorem target?
#
# This script does not adopt a new postulate.
# It does not derive the full coefficient law unless explicitly shown.
# It does not derive B_s/F_zeta insertion.
# It does not derive safe trace membership.
# It does not derive trace/residual incidence.
# It does not construct active O.
# It does not derive residual control.
# It does not open the parent equation.
#
# Tiny goblin rule:
#
#   A clean pipe does not choose the shape of the cup.

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
        "BLOCKED": StatusMark.FAIL,
        "CANDIDATE_REMAINS": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "PARTIAL_CONSTRAINT": StatusMark.INFO,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "THEOREM_TARGET": StatusMark.OBLIGATION,
        "UNDERDETERMINED": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g31_classifier",
            "31_source_divergence_coefficient_law__candidate_source_divergence_coefficient_law_classifier",
            "g31_source_divergence_classifier",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_explicitness",
            "31_source_divergence_coefficient_law__candidate_nonreservoir_divergence_explicitness",
            "g31_nonreservoir_explicitness",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_coeff",
            "31_source_divergence_coefficient_law__candidate_coefficient_source_no_double_counting_tests",
            "g31_coeff_source_tests",
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
class TraceNormSDSymbols:
    zeta: sp.Symbol
    B_s: sp.Symbol
    N_trace: sp.Symbol
    L_source_dup: sp.Symbol
    L_coeff_source: sp.Symbol
    L_div_reservoir: sp.Symbol
    L_explicitness: sp.Symbol
    recovery_selector: sp.Symbol
    repair_selector: sp.Symbol
    normalization_gap: sp.Expr


@dataclass
class TraceNormTest:
    name: str
    test: str
    status: str
    result: str
    blocker: str


@dataclass
class ForkRoute:
    name: str
    route: str
    status: str
    meaning: str


@dataclass
class RejectedUpgrade:
    name: str
    upgrade: str
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


def build_symbols() -> TraceNormSDSymbols:
    (
        zeta,
        B_s,
        N_trace,
        L_source_dup,
        L_coeff_source,
        L_div_reservoir,
        L_explicitness,
        recovery_selector,
        repair_selector,
    ) = sp.symbols(
        "zeta B_s N_trace L_source_dup L_coeff_source L_div_reservoir "
        "L_explicitness recovery_selector repair_selector",
        real=True,
    )

    normalization_gap = sp.simplify(
        N_trace
        + L_source_dup
        + L_coeff_source
        + L_div_reservoir
        + L_explicitness
        + recovery_selector
        + repair_selector
    )

    return TraceNormSDSymbols(
        zeta=zeta,
        B_s=B_s,
        N_trace=N_trace,
        L_source_dup=L_source_dup,
        L_coeff_source=L_coeff_source,
        L_div_reservoir=L_div_reservoir,
        L_explicitness=L_explicitness,
        recovery_selector=recovery_selector,
        repair_selector=repair_selector,
        normalization_gap=normalization_gap,
    )


def build_tests(symbols: TraceNormSDSymbols) -> List[TraceNormTest]:
    return [
        TraceNormTest(
            name="T1: source neutrality effect",
            test="source/divergence constraints remove hidden source carriers",
            status="PARTIAL_CONSTRAINT",
            result="narrows admissible coefficient behavior",
            blocker="does not specify how B_s reads zeta",
        ),
        TraceNormTest(
            name="T2: divergence explicitness effect",
            test="non-reservoir explicitness removes hidden correction pockets",
            status="PARTIAL_CONSTRAINT",
            result="narrows admissible correction behavior",
            blocker="does not fix trace normalization",
        ),
        TraceNormTest(
            name="T3: trace normalization target",
            test="N_trace = 0 or N_trace derived",
            status="THEOREM_TARGET",
            result="still required for coefficient law",
            blocker="not forced by source/divergence constraints so far",
        ),
        TraceNormTest(
            name="T4: recovery exclusion",
            test="recovery_selector = 0",
            status="REQUIRED",
            result="normalization cannot be selected from AB=1, Schwarzschild, weak-field, gamma/PPN, or kappa=0",
            blocker="recovery cannot choose normalization",
        ),
        TraceNormTest(
            name="T5: repair exclusion",
            test="repair_selector = 0",
            status="REQUIRED",
            result="normalization cannot be selected to repair source/divergence failure",
            blocker="repair cannot choose normalization",
        ),
        TraceNormTest(
            name="T6: normalization gap",
            test=f"G_trace_normalization = {sp.sstr(symbols.normalization_gap)}",
            status="OPEN",
            result="source/divergence constraints do not close N_trace",
            blocker="trace normalization remains open theorem target/candidate",
        ),
    ]


def build_forks() -> List[ForkRoute]:
    return [
        ForkRoute(
            name="F1: theorem derivation",
            route="source/divergence constraints force trace normalization",
            status="NOT_DERIVED",
            meaning="not achieved in this fork",
        ),
        ForkRoute(
            name="F2: partial constraint",
            route="source/divergence constraints restrict admissible normalization choices",
            status="PARTIAL_CONSTRAINT",
            meaning="achieved only as anti-smuggling discipline",
        ),
        ForkRoute(
            name="F3: candidate remains",
            route="trace normalization remains candidate/theorem target",
            status="CANDIDATE_REMAINS",
            meaning="normalization still open after source/divergence route",
        ),
        ForkRoute(
            name="F4: postulate adoption",
            route="adopt trace-normalization postulate",
            status="REJECTED",
            meaning="forbidden without explicit user/theory decision",
        ),
        ForkRoute(
            name="F5: insertion shortcut",
            route="treat source/divergence-normalization discipline as B_s/F_zeta insertion",
            status="REJECTED",
            meaning="normalization discipline is not insertion",
        ),
    ]


def build_rejected() -> List[RejectedUpgrade]:
    return [
        RejectedUpgrade(
            name="R1: recovery-selected normalization",
            upgrade="choose trace normalization because recovery works",
            status="REJECTED",
            reason="recovery may audit only after construction",
        ),
        RejectedUpgrade(
            name="R2: repair-selected normalization",
            upgrade="choose trace normalization because it repairs source/divergence gaps",
            status="REJECTED",
            reason="failure may reject but not select",
        ),
        RejectedUpgrade(
            name="R3: source neutrality as normalization",
            upgrade="source neutrality treated as trace-normalization theorem",
            status="REJECTED",
            reason="source neutrality does not specify how B_s reads zeta",
        ),
        RejectedUpgrade(
            name="R4: explicitness as normalization",
            upgrade="divergence explicitness treated as trace-normalization theorem",
            status="REJECTED",
            reason="explicit correction accounting does not fix zeta reading",
        ),
        RejectedUpgrade(
            name="R5: normalization as membership",
            upgrade="trace normalization treated as safe membership theorem",
            status="REJECTED",
            reason="membership remains separate",
        ),
        RejectedUpgrade(
            name="R6: normalization as insertion",
            upgrade="trace normalization treated as B_s/F_zeta insertion",
            status="REJECTED",
            reason="normalization is one gap, not insertion",
        ),
        RejectedUpgrade(
            name="R7: normalization as parent readiness",
            upgrade="trace normalization opens parent equation",
            status="REJECTED",
            reason="parent gate remains closed",
        ),
    ]


def build_obligations() -> List[TraceNormObligation]:
    return [
        TraceNormObligation(
            name="O1: normalization remains open",
            obligation="keep N_trace as theorem target/candidate unless derived or explicitly adopted",
            status="OPEN",
            blocks="coefficient law",
            discipline="do not select from recovery or repair",
        ),
        TraceNormObligation(
            name="O2: membership next",
            obligation="keep safe trace membership separate and open",
            status="OPEN",
            blocks="sector membership",
            discipline="normalization is not membership",
        ),
        TraceNormObligation(
            name="O3: explicit-choice boundary",
            obligation="only explicit user/theory decision may adopt trace-normalization postulate",
            status="REQUIRED",
            blocks="postulate governance",
            discipline="classification is not adoption",
        ),
        TraceNormObligation(
            name="O4: Group 31 summary",
            obligation="summarize source/divergence partial constraints and open normalization",
            status="OPEN",
            blocks="Group 31 closure",
            discipline="partial constraint is not coefficient law",
        ),
        TraceNormObligation(
            name="O5: downstream gates",
            obligation="keep insertion, active O, residual control, and parent equation closed",
            status="NOT_READY",
            blocks="premature closure",
            discipline="normalization fork is not insertion",
        ),
    ]


def build_conclusions() -> List[TraceNormConclusion]:
    return [
        TraceNormConclusion(
            name="C1: trace normalization status",
            conclusion="source/divergence constraints do not derive trace normalization",
            status="NOT_DERIVED",
            meaning="N_trace remains open",
        ),
        TraceNormConclusion(
            name="C2: partial constraint",
            conclusion="source/divergence discipline restricts admissible normalization selection",
            status="PARTIAL_CONSTRAINT",
            meaning="normalization cannot be recovery-selected, repair-selected, or hidden-source-selected",
        ),
        TraceNormConclusion(
            name="C3: candidate remains",
            conclusion="trace normalization remains candidate/theorem target",
            status="CANDIDATE_REMAINS",
            meaning="still not adopted",
        ),
        TraceNormConclusion(
            name="C4: no insertion",
            conclusion="B_s/F_zeta insertion is not derived",
            status="NOT_READY",
            meaning="normalization fork is not insertion",
        ),
        TraceNormConclusion(
            name="C5: next",
            conclusion="source/divergence obligations summary should run next",
            status="OPEN",
            meaning="Group 31 can summarize partial constraints and remaining gaps",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Trace normalization from source/divergence problem")
    print("Question:")
    print()
    print("  Does source/divergence discipline determine how B_s reads zeta, or does trace normalization remain an open candidate/theorem target?")
    print()
    print("Discipline:")
    print()
    print("  This script tests the normalization fork.")
    print("  It adopts no postulate.")
    print("  It derives no insertion.")
    print()
    print("Tiny goblin rule:")
    print("  A clean pipe does not choose the shape of the cup.")

    with out.governance_assessments():
        out.line(
            "trace-normalization source/divergence fork opened",
            StatusMark.INFO,
            "testing whether source/divergence constraints fix N_trace",
        )


def case_1_symbolic_ledger(symbols: TraceNormSDSymbols, out: ScriptOutput) -> None:
    header("Case 1: Trace-normalization source/divergence ledger")
    print("Trace-normalization source/divergence symbols:")
    print()
    for name in [
        "zeta",
        "B_s",
        "N_trace",
        "L_source_dup",
        "L_coeff_source",
        "L_div_reservoir",
        "L_explicitness",
        "recovery_selector",
        "repair_selector",
    ]:
        print(f"  {name} = {sp.sstr(getattr(symbols, name))}")

    print()
    print("Trace-normalization source/divergence gap:")
    print(f"  G_trace_normalization = {sp.sstr(symbols.normalization_gap)}")

    with out.derived_results():
        out.line(
            "trace-normalization source/divergence gap stated",
            StatusMark.OBLIGATION,
            f"G_trace_normalization = {sp.sstr(symbols.normalization_gap)}",
        )


def case_2_tests(items: List[TraceNormTest], out: ScriptOutput) -> None:
    header("Case 2: Trace-normalization source/divergence tests")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Test: {item.test}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Result: {item.result}")
        print(f"Blocker: {item.blocker}")

    with out.governance_assessments():
        out.line(
            "trace-normalization source/divergence tests stated",
            StatusMark.DEFER,
            f"{len(items)} tests stated",
        )


def case_3_forks(items: List[ForkRoute], out: ScriptOutput) -> None:
    header("Case 3: Trace-normalization fork routes")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Route: {item.route}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Meaning: {item.meaning}")

    with out.governance_assessments():
        out.line(
            "trace-normalization fork classified",
            StatusMark.PASS,
            "normalization remains open candidate/theorem target",
        )


def case_4_rejected(items: List[RejectedUpgrade], out: ScriptOutput) -> None:
    header("Case 4: Rejected trace-normalization upgrades")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Upgrade: {item.upgrade}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Reason: {item.reason}")

    with out.counterexamples():
        out.line(
            "trace-normalization forbidden upgrades rejected",
            StatusMark.FAIL,
            "recovery, repair, source neutrality, explicitness, membership, insertion, and parent upgrades rejected",
        )


def case_5_obligations(items: List[TraceNormObligation], out: ScriptOutput) -> None:
    header("Case 5: Trace-normalization obligations")
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
            f"{len(items)} obligations remain",
        )


def case_6_conclusions(items: List[TraceNormConclusion], out: ScriptOutput) -> None:
    header("Case 6: Trace-normalization conclusions")
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
            "trace-normalization source/divergence conclusion stated",
            StatusMark.PASS,
            "normalization remains open; no postulate or insertion",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Trace-normalization from source/divergence result:")
    print()
    print("  Source/divergence constraints do not derive trace normalization.")
    print("  They constrain admissible normalization selection by rejecting recovery-selected, repair-selected, hidden-source-selected, and insertion-selected routes.")
    print("  Trace normalization remains an open candidate/theorem target.")
    print("  It is not adopted.")
    print("  It does not derive safe trace membership.")
    print("  It does not derive trace/residual incidence.")
    print("  It does not derive B_s/F_zeta insertion.")
    print("  Active O, residual control, and parent equation remain not ready.")
    print()
    print("Possible next script:")
    print("  candidate_source_divergence_obligations.py")
    print()
    print("Tiny goblin label:")
    print("  A clean pipe does not choose the shape of the cup.")

    with out.governance_assessments():
        out.line(
            "trace-normalization source/divergence fork complete",
            StatusMark.PASS,
            "source/divergence obligations summary should run next",
        )


def record_derivations(ns, symbols: TraceNormSDSymbols) -> None:
    ns.record_derivation(
        derivation_id="g31_trace_normalization_fork",
        inputs=[
            symbols.N_trace,
            symbols.L_source_dup,
            symbols.L_coeff_source,
            symbols.L_div_reservoir,
            symbols.L_explicitness,
            symbols.recovery_selector,
            symbols.repair_selector,
        ],
        output=symbols.normalization_gap,
        method="test whether source/divergence constraints derive trace normalization",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="trace_normalization_source_divergence_fork_marker",
        scope="Group 31 source/divergence coefficient law",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g31_tn_open", "Keep trace normalization open unless derived or explicitly adopted"),
        ("g31_tn_no_recovery", "Do not select trace normalization from recovery"),
        ("g31_tn_no_repair", "Do not select trace normalization from repair"),
        ("g31_tn_membership_open", "Keep safe trace membership separate"),
        ("g31_tn_no_insertion", "Do not treat trace normalization as insertion"),
        ("g31_tn_summary_next", "Summarize Group 31 obligations next"),
        ("g31_tn_downstream_closed", "Keep insertion/O/residual/parent gates closed"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g31_trace_normalization_route"],
            description=(
                "Source/divergence constraints do not derive trace normalization. N_trace remains open candidate/theorem target."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g31_tn_open",
        "g31_tn_no_recovery",
        "g31_tn_no_repair",
        "g31_tn_membership_open",
        "g31_tn_no_insertion",
        "g31_tn_summary_next",
        "g31_tn_downstream_closed",
    ]

    ns.record_route(RouteRecord(
        route_id="g31_trace_normalization_route",
        script_id=SCRIPT_ID,
        name="Group 31 trace-normalization source/divergence fork",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "source/divergence constraints do not derive trace normalization",
            "trace normalization remains open candidate/theorem target",
            "normalization cannot be recovery-selected or repair-selected",
            "safe membership remains separate",
            "no postulate adopted",
            "downstream gates remain closed",
        ],
    ))

    for branch_id in [
        "recovery_selected_trace_normalization",
        "repair_selected_trace_normalization",
        "source_neutrality_as_trace_normalization",
        "explicitness_as_trace_normalization",
        "trace_normalization_as_membership",
        "trace_normalization_as_insertion",
        "trace_normalization_as_parent_readiness",
        "trace_normalization_fork_as_postulate_adoption",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; trace-normalization fork is not postulate adoption or theorem closure.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g31_trace_normalization_still_open",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Source/divergence constraints do not derive trace normalization. They constrain admissible normalization selection by rejecting recovery-selected, repair-selected, hidden-source-selected, and insertion-selected routes. "
            "Trace normalization remains an open candidate/theorem target and is not adopted. It does not derive safe trace membership, trace/residual incidence, or B_s/F_zeta insertion. "
            "Active O, residual control, and parent equation remain not ready."
        ),
        derivation_ids=["g31_trace_normalization_fork"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Trace Normalization From Source Divergence")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    tests = build_tests(symbols)
    forks = build_forks()
    rejected = build_rejected()
    obligations = build_obligations()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_symbolic_ledger(symbols, out)
    case_2_tests(tests, out)
    case_3_forks(forks, out)
    case_4_rejected(rejected, out)
    case_5_obligations(obligations, out)
    case_6_conclusions(conclusions, out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns, symbols)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
