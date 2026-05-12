# Candidate coefficient membership bridge
#
# Group:
#   29_Bs_Fzeta_coefficient_origin
#
# Script type:
#   COEFFICIENT / MEMBERSHIP BRIDGE AUDIT
#
# Purpose
# -------
# Test whether the surviving volume/trace coefficient-origin candidate can
# improve zeta_Bs -> T_zeta from candidate anchor to structurally constrained
# membership.
#
# Locked-door question:
#
#   Does coefficient origin force safe trace membership?
#
# This script does not derive B_s/F_zeta insertion.
# It does not derive no-overlap sector geometry.
# It does not construct active O.
# It does not derive residual control.
# It does not open the parent equation.
#
# Tiny goblin rule:
#
#   A name tag is not a bloodline.

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
        "CANDIDATE": StatusMark.DEFER,
        "CONSTRAINED_CANDIDATE": StatusMark.INFO,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "PARTIAL": StatusMark.INFO,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "UNDERDETERMINED": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g29_filter",
            "29_Bs_Fzeta_coefficient_origin__candidate_recovery_smuggling_filter",
            "g29_recovery_filter",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g29_volume_trace",
            "29_Bs_Fzeta_coefficient_origin__candidate_volume_trace_coefficient_origin",
            "g29_volume_trace",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g29_problem",
            "29_Bs_Fzeta_coefficient_origin__candidate_coefficient_origin_problem_ledger",
            "g29_coeff_problem",
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
class MembershipBridgeSymbols:
    zeta: sp.Symbol
    zeta_Bs: sp.Symbol
    T_zeta: sp.Symbol
    R_zeta: sp.Symbol
    R_kappa: sp.Symbol
    c_vol: sp.Symbol
    c_Bs: sp.Symbol
    M_coeff: sp.Symbol
    M_sector: sp.Symbol
    I_TRz: sp.Symbol
    I_TRk: sp.Symbol
    coeff_gap: sp.Symbol
    membership_gap: sp.Symbol
    incidence_gap: sp.Symbol
    source_gap: sp.Symbol
    residual_gap: sp.Symbol
    insertion_gap: sp.Symbol
    bridge_load: sp.Expr


@dataclass
class BridgeCandidate:
    name: str
    candidate: str
    status: str
    supports: str
    does_not_support: str


@dataclass
class BridgeTest:
    name: str
    test: str
    status: str
    result: str
    implication: str


@dataclass
class BridgeRequirement:
    name: str
    requirement: str
    status: str
    needed_for: str
    fails_if: str


@dataclass
class RejectedBridgeShortcut:
    name: str
    shortcut: str
    status: str
    reason: str


@dataclass
class BridgeConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_symbols() -> MembershipBridgeSymbols:
    (
        zeta,
        zeta_Bs,
        T_zeta,
        R_zeta,
        R_kappa,
        c_vol,
        c_Bs,
        M_coeff,
        M_sector,
        I_TRz,
        I_TRk,
        coeff_gap,
        membership_gap,
        incidence_gap,
        source_gap,
        residual_gap,
        insertion_gap,
    ) = sp.symbols(
        "zeta zeta_Bs T_zeta R_zeta R_kappa c_vol c_Bs M_coeff M_sector I_TRz I_TRk "
        "coeff_gap membership_gap incidence_gap source_gap residual_gap insertion_gap",
        real=True,
    )

    bridge_load = sp.simplify(
        coeff_gap + membership_gap + incidence_gap + source_gap + residual_gap + insertion_gap
    )

    return MembershipBridgeSymbols(
        zeta=zeta,
        zeta_Bs=zeta_Bs,
        T_zeta=T_zeta,
        R_zeta=R_zeta,
        R_kappa=R_kappa,
        c_vol=c_vol,
        c_Bs=c_Bs,
        M_coeff=M_coeff,
        M_sector=M_sector,
        I_TRz=I_TRz,
        I_TRk=I_TRk,
        coeff_gap=coeff_gap,
        membership_gap=membership_gap,
        incidence_gap=incidence_gap,
        source_gap=source_gap,
        residual_gap=residual_gap,
        insertion_gap=insertion_gap,
        bridge_load=bridge_load,
    )


def build_candidates() -> List[BridgeCandidate]:
    return [
        BridgeCandidate(
            name="B1: volume-trace anchor",
            candidate="zeta_Bs belongs to candidate safe trace sector T_zeta because zeta is volume trace",
            status="CONSTRAINED_CANDIDATE",
            supports="safe trace anchor with structural backing",
            does_not_support="complete membership theorem or insertion",
        ),
        BridgeCandidate(
            name="B2: coefficient membership bridge",
            candidate="coefficient origin defines membership M_coeff(zeta_Bs)=T_zeta",
            status="UNDERDETERMINED",
            supports="possible bridge target",
            does_not_support="zero incidence or source routing",
        ),
        BridgeCandidate(
            name="B3: residual exclusion from coefficient",
            candidate="coefficient origin implies I(T_zeta,R_zeta)=0 and I(T_zeta,R_kappa)=0",
            status="NOT_DERIVED",
            supports="nothing yet",
            does_not_support="trace/residual no-overlap",
        ),
        BridgeCandidate(
            name="B4: source discipline from coefficient",
            candidate="coefficient origin prevents ordinary source double counting",
            status="NOT_DERIVED",
            supports="future source-routing audit",
            does_not_support="source no-double-counting now",
        ),
        BridgeCandidate(
            name="B5: insertion from membership",
            candidate="zeta_Bs -> T_zeta membership derives B_s/F_zeta insertion",
            status="REJECTED",
            supports="nothing",
            does_not_support="insertion gate remains separate",
        ),
        BridgeCandidate(
            name="B6: recovery membership",
            candidate="membership is accepted because recovery works",
            status="REJECTED",
            supports="nothing",
            does_not_support="membership cannot be recovery-selected",
        ),
    ]


def build_tests() -> List[BridgeTest]:
    return [
        BridgeTest(
            name="T1: anchor strengthening",
            test="does volume/trace origin strengthen zeta_Bs -> T_zeta?",
            status="PARTIAL",
            result="yes; it gives the anchor structural backing",
            implication="zeta_Bs -> T_zeta can be treated as constrained candidate",
        ),
        BridgeTest(
            name="T2: membership theorem",
            test="does coefficient origin prove complete sector membership?",
            status="NOT_DERIVED",
            result="no; membership rule remains incomplete",
            implication="sector geometry remains not constructed",
        ),
        BridgeTest(
            name="T3: zero incidence",
            test="does coefficient origin prove I(T_zeta,R_zeta)=0 or I(T_zeta,R_kappa)=0?",
            status="NOT_DERIVED",
            result="no; residual non-overlap remains open",
            implication="no-overlap sector geometry remains not constructed",
        ),
        BridgeTest(
            name="T4: residual control",
            test="does coefficient membership bridge kill or inert residuals?",
            status="REJECTED",
            result="no",
            implication="residual control remains not derived",
        ),
        BridgeTest(
            name="T5: source routing",
            test="does coefficient membership bridge derive source no-double-counting?",
            status="NOT_DERIVED",
            result="no",
            implication="source discipline remains separate",
        ),
        BridgeTest(
            name="T6: insertion",
            test="does coefficient membership bridge derive B_s/F_zeta insertion?",
            status="NOT_DERIVED",
            result="no",
            implication="insertion gate remains closed",
        ),
        BridgeTest(
            name="T7: recovery selection",
            test="does membership depend on recovery?",
            status="REJECTED",
            result="any recovery-selected membership is rejected",
            implication="membership bridge must remain structural",
        ),
    ]


def build_requirements() -> List[BridgeRequirement]:
    return [
        BridgeRequirement(
            name="R1: membership rule",
            requirement="define what coefficient-origin membership means",
            status="REQUIRED",
            needed_for="membership theorem",
            fails_if="zeta_Bs -> T_zeta is promoted by naming",
        ),
        BridgeRequirement(
            name="R2: residual non-overlap",
            requirement="derive zero incidence or residual exclusion separately",
            status="REQUIRED",
            needed_for="no-overlap geometry",
            fails_if="coefficient anchor is treated as residual exclusion",
        ),
        BridgeRequirement(
            name="R3: source no-double-counting",
            requirement="show coefficient-origin membership does not duplicate ordinary source",
            status="REQUIRED",
            needed_for="source discipline",
            fails_if="safe trace channel carries hidden source",
        ),
        BridgeRequirement(
            name="R4: residual honesty",
            requirement="do not erase residual zeta/kappa by assigning zeta_Bs to T_zeta",
            status="REQUIRED",
            needed_for="residual-control honesty",
            fails_if="membership becomes inertness",
        ),
        BridgeRequirement(
            name="R5: insertion separation",
            requirement="keep B_s/F_zeta insertion separate from membership bridge",
            status="REQUIRED",
            needed_for="theorem hygiene",
            fails_if="membership becomes insertion",
        ),
        BridgeRequirement(
            name="R6: recovery independence",
            requirement="reject recovery-selected membership",
            status="REQUIRED",
            needed_for="anti-smuggling",
            fails_if="AB=1 or Schwarzschild selects membership",
        ),
    ]


def build_shortcuts() -> List[RejectedBridgeShortcut]:
    return [
        RejectedBridgeShortcut(
            name="F1: anchor as theorem",
            shortcut="zeta_Bs -> T_zeta treated as complete sector membership theorem",
            status="REJECTED",
            reason="coefficient/volume trace supports the anchor but does not complete membership",
        ),
        RejectedBridgeShortcut(
            name="F2: membership as no-overlap",
            shortcut="safe trace membership treated as I(T_zeta,R_zeta)=0",
            status="REJECTED",
            reason="zero incidence is not derived",
        ),
        RejectedBridgeShortcut(
            name="F3: membership as residual control",
            shortcut="safe trace membership kills residuals",
            status="REJECTED",
            reason="residuals are not killed by membership",
        ),
        RejectedBridgeShortcut(
            name="F4: membership as source routing",
            shortcut="safe trace membership proves source no-double-counting",
            status="REJECTED",
            reason="source routing remains separate",
        ),
        RejectedBridgeShortcut(
            name="F5: membership as insertion",
            shortcut="safe trace membership derives B_s/F_zeta insertion",
            status="REJECTED",
            reason="insertion gate remains separate",
        ),
        RejectedBridgeShortcut(
            name="F6: recovery-selected membership",
            shortcut="membership accepted because recovery works",
            status="REJECTED",
            reason="recovery may audit only after construction",
        ),
    ]


def build_conclusions() -> List[BridgeConclusion]:
    return [
        BridgeConclusion(
            name="C1: safe trace anchor",
            conclusion="zeta_Bs -> T_zeta is upgraded to constrained candidate",
            status="CONSTRAINED_CANDIDATE",
            meaning="volume/trace coefficient origin gives structural backing",
        ),
        BridgeConclusion(
            name="C2: membership theorem",
            conclusion="complete membership theorem is not derived",
            status="NOT_DERIVED",
            meaning="sector geometry remains not constructed",
        ),
        BridgeConclusion(
            name="C3: zero incidence",
            conclusion="trace/residual zero incidence is not derived",
            status="NOT_DERIVED",
            meaning="no-overlap geometry remains open",
        ),
        BridgeConclusion(
            name="C4: downstream gates",
            conclusion="insertion, residual control, active O, and parent closure remain closed",
            status="NOT_READY",
            meaning="membership bridge cannot be upgraded to downstream theorem",
        ),
        BridgeConclusion(
            name="C5: next route",
            conclusion="residual interpretation from coefficient should be audited next",
            status="OPEN",
            meaning="test what the coefficient-origin result says about residuals without killing them",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Coefficient/membership bridge problem")
    print("Question:")
    print()
    print("  Does coefficient origin force safe trace membership?")
    print()
    print("Discipline:")
    print()
    print("  Anchor is not complete membership.")
    print("  Membership is not zero incidence.")
    print("  Membership is not insertion.")
    print("  Membership is not residual control.")
    print()
    print("Tiny goblin rule:")
    print("  A name tag is not a bloodline.")

    with out.governance_assessments():
        out.line(
            "coefficient/membership bridge audit opened",
            StatusMark.INFO,
            "testing whether surviving coefficient origin improves safe trace membership",
        )


def case_1_symbolic_ledger(symbols: MembershipBridgeSymbols, out: ScriptOutput) -> None:
    header("Case 1: Coefficient/membership symbolic ledger")
    print("Bridge symbols:")
    print()
    for name in [
        "zeta",
        "zeta_Bs",
        "T_zeta",
        "R_zeta",
        "R_kappa",
        "c_vol",
        "c_Bs",
        "M_coeff",
        "M_sector",
        "I_TRz",
        "I_TRk",
    ]:
        print(f"  {name} = {sp.sstr(getattr(symbols, name))}")
    print()
    print("Coefficient/membership bridge load:")
    print()
    print(f"  L_membership_bridge = {sp.sstr(symbols.bridge_load)}")

    with out.derived_results():
        out.line(
            "coefficient/membership bridge load stated",
            StatusMark.OBLIGATION,
            f"L_membership_bridge = {sp.sstr(symbols.bridge_load)}",
        )


def case_2_candidates(items: List[BridgeCandidate], out: ScriptOutput) -> None:
    header("Case 2: Coefficient/membership bridge candidates")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Candidate: {item.candidate}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Supports: {item.supports}")
        print(f"Does not support: {item.does_not_support}")

    with out.governance_assessments():
        out.line(
            "coefficient/membership bridge candidates classified",
            StatusMark.DEFER,
            f"{len(items)} bridge candidates classified",
        )


def case_3_tests(items: List[BridgeTest], out: ScriptOutput) -> None:
    header("Case 3: Coefficient/membership bridge tests")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Test: {item.test}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Result: {item.result}")
        print(f"Implication: {item.implication}")

    with out.governance_assessments():
        out.line(
            "coefficient/membership bridge tests completed",
            StatusMark.DEFER,
            "safe trace anchor upgraded to constrained candidate; membership theorem not derived",
        )


def case_4_requirements(items: List[BridgeRequirement], out: ScriptOutput) -> None:
    header("Case 4: Coefficient/membership bridge requirements")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Requirement: {item.requirement}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Needed for: {item.needed_for}")
        print(f"Fails if: {item.fails_if}")

    with out.unresolved_obligations():
        out.line(
            "coefficient/membership bridge requirements stated",
            StatusMark.OBLIGATION,
            f"{len(items)} requirements remain open after bridge audit",
        )


def case_5_shortcuts(items: List[RejectedBridgeShortcut], out: ScriptOutput) -> None:
    header("Case 5: Rejected coefficient/membership shortcuts")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Shortcut: {item.shortcut}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Reason: {item.reason}")

    with out.counterexamples():
        out.line(
            "coefficient/membership shortcuts rejected",
            StatusMark.FAIL,
            "anchor-as-theorem, membership-as-no-overlap, residual control, source routing, insertion, and recovery-selected membership are rejected",
        )


def case_6_conclusions(items: List[BridgeConclusion], out: ScriptOutput) -> None:
    header("Case 6: Coefficient/membership bridge conclusions")
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
            "coefficient/membership bridge conclusion stated",
            StatusMark.DEFER,
            "residual interpretation from coefficient should be audited next",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Coefficient/membership bridge result:")
    print()
    print("  zeta_Bs -> T_zeta is upgraded to constrained candidate.")
    print("  Volume/trace coefficient origin gives structural backing to the safe trace anchor.")
    print("  Complete membership theorem is not derived.")
    print("  I(T_zeta,R_zeta)=0 is not derived.")
    print("  I(T_zeta,R_kappa)=0 is not derived.")
    print("  Source no-double-counting is not derived.")
    print("  Residual control is not derived.")
    print("  B_s/F_zeta insertion is not derived.")
    print("  Active O and parent equation remain not ready.")
    print()
    print("Possible next script:")
    print("  candidate_residual_interpretation_from_coefficient.py")
    print()
    print("Tiny goblin label:")
    print("  A name tag is not a bloodline.")

    with out.governance_assessments():
        out.line(
            "coefficient/membership bridge audit complete",
            StatusMark.PASS,
            "safe trace anchor constrained; membership theorem not derived",
        )


def record_derivations(ns, symbols: MembershipBridgeSymbols) -> None:
    ns.record_derivation(
        derivation_id="g29_membership_bridge",
        inputs=[
            symbols.coeff_gap,
            symbols.membership_gap,
            symbols.incidence_gap,
            symbols.source_gap,
            symbols.residual_gap,
            symbols.insertion_gap,
        ],
        output=symbols.bridge_load,
        method="audit whether coefficient origin improves zeta_Bs to T_zeta membership",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="coefficient_membership_bridge_marker",
        scope="Group 29 B_s/F_zeta coefficient origin",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g29_mb_membership", "Derive complete coefficient-origin membership rule"),
        ("g29_mb_incidence", "Derive trace/residual zero incidence separately"),
        ("g29_mb_source", "Derive source no-double-counting separately"),
        ("g29_mb_residual", "Prevent residual erasure by membership"),
        ("g29_mb_insertion", "Keep B_s/F_zeta insertion separate"),
        ("g29_mb_recovery", "Reject recovery-selected membership"),
        ("g29_mb_next_residual", "Audit residual interpretation from coefficient next"),
        ("g29_mb_downstream", "Keep active O/residual/insertion/parent gates closed"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g29_mb_route"],
            description=(
                "The safe trace anchor is structurally strengthened, but complete membership, zero incidence, source routing, insertion, residual control, and parent closure are not derived."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g29_mb_membership",
        "g29_mb_incidence",
        "g29_mb_source",
        "g29_mb_residual",
        "g29_mb_insertion",
        "g29_mb_recovery",
        "g29_mb_next_residual",
        "g29_mb_downstream",
    ]

    ns.record_route(RouteRecord(
        route_id="g29_mb_route",
        script_id=SCRIPT_ID,
        name="Group 29 coefficient/membership bridge route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "zeta_Bs -> T_zeta may be treated as constrained candidate",
            "complete membership is not claimed",
            "zero incidence is not claimed",
            "source no-double-counting is not claimed",
            "insertion, active O, residual control, and parent gates remain closed",
        ],
    ))

    for branch_id in [
        "anchor_as_theorem",
        "membership_as_no_overlap",
        "membership_as_zero_incidence",
        "membership_as_residual_control",
        "membership_as_source_routing",
        "membership_as_insertion",
        "recovery_selected_membership",
        "membership_opens_parent",
        "membership_constructs_active_O",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; coefficient/membership bridge is not no-overlap, insertion, residual control, active O, or parent closure.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g29_membership_bridge_constrained",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "zeta_Bs -> T_zeta is upgraded to constrained candidate because volume/trace coefficient origin gives structural backing to the safe trace anchor. "
            "However, complete membership theorem, trace/residual zero incidence, source no-double-counting, residual control, B_s/F_zeta insertion, active O, and parent equation are not derived."
        ),
        derivation_ids=["g29_membership_bridge"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Coefficient Membership Bridge")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    candidates = build_candidates()
    tests = build_tests()
    requirements = build_requirements()
    shortcuts = build_shortcuts()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_symbolic_ledger(symbols, out)
    case_2_candidates(candidates, out)
    case_3_tests(tests, out)
    case_4_requirements(requirements, out)
    case_5_shortcuts(shortcuts, out)
    case_6_conclusions(conclusions, out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns, symbols)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
