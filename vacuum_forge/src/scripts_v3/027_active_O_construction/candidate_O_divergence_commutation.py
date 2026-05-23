# Candidate O divergence commutation
#
# Group:
#   27_active_O_construction
#
# Script type:
#   DIVERGENCE / CONSERVATION SAFETY AUDIT
#
# Purpose
# -------
# Audit whether candidate active O can preserve divergence and conservation
# constraints.
#
# Locked-door question:
#
#   Does O preserve divergence and conservation constraints?
#
# This script does not derive active O.
# It does not prove O commutes with divergence.
# It does not derive residual control.
# It does not derive B_s/F_zeta insertion.
# It does not open parent equation closure.
#
# Tiny goblin rule:
#
#   Do not throw the crumbs into divergence.

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


# =============================================================================
# Utilities
# =============================================================================


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def status_mark(status: str) -> StatusMark:
    return {
        "BLOCKED": StatusMark.FAIL,
        "CANDIDATE": StatusMark.DEFER,
        "CONDITIONALLY_SAFE": StatusMark.INFO,
        "INSUFFICIENT": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "PRESERVED_IF": StatusMark.INFO,
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
            "g27_O_problem",
            "027_active_O_construction__candidate_O_problem_ledger",
            "g27_O_problem",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g27_dc",
            "027_active_O_construction__candidate_O_domain_codomain",
            "g27_O_domain_codomain",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g27_ki",
            "027_active_O_construction__candidate_O_kernel_image",
            "g27_O_kernel_image",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g27_pair",
            "027_active_O_construction__candidate_O_no_overlap_pairing",
            "g27_O_pairing",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g27_alg",
            "027_active_O_construction__candidate_O_projection_law",
            "g27_O_alg_law",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g26_summary",
            "026_residual_control_theorem_attempt__candidate_group_26_status_summary",
            "g26_status_summary",
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


# =============================================================================
# Data models
# =============================================================================


@dataclass
class DivergenceSymbols:
    O: sp.Symbol
    Div: sp.Symbol
    X: sp.Symbol
    zeta_Bs: sp.Symbol
    zeta_res: sp.Symbol
    kappa_res: sp.Symbol
    J_leak: sp.Symbol
    B_bdy: sp.Symbol
    S_src: sp.Symbol
    comm_gap: sp.Symbol
    correction_gap: sp.Symbol
    source_gap: sp.Symbol
    boundary_gap: sp.Symbol
    current_gap: sp.Symbol
    parent_gap: sp.Symbol
    div_safety_gap: sp.Expr


@dataclass
class DivergenceCandidate:
    name: str
    candidate: str
    status: str
    works_if: str
    hazard: str


@dataclass
class DivergenceTest:
    name: str
    test: str
    status: str
    result: str
    implication: str


@dataclass
class ConservationRequirement:
    name: str
    requirement: str
    status: str
    required_for: str
    fails_if: str


@dataclass
class RejectedDivergenceShortcut:
    name: str
    shortcut: str
    status: str
    reason: str


@dataclass
class DivergenceConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


# =============================================================================
# Builders
# =============================================================================


def build_symbols() -> DivergenceSymbols:
    (
        O,
        Div,
        X,
        zeta_Bs,
        zeta_res,
        kappa_res,
        J_leak,
        B_bdy,
        S_src,
        comm_gap,
        correction_gap,
        source_gap,
        boundary_gap,
        current_gap,
        parent_gap,
    ) = sp.symbols(
        "O Div X zeta_Bs zeta_res kappa_res J_leak B_bdy S_src "
        "comm_gap correction_gap source_gap boundary_gap current_gap parent_gap",
        real=True,
    )

    div_safety_gap = sp.simplify(
        comm_gap + correction_gap + source_gap + boundary_gap + current_gap + parent_gap
    )

    return DivergenceSymbols(
        O=O,
        Div=Div,
        X=X,
        zeta_Bs=zeta_Bs,
        zeta_res=zeta_res,
        kappa_res=kappa_res,
        J_leak=J_leak,
        B_bdy=B_bdy,
        S_src=S_src,
        comm_gap=comm_gap,
        correction_gap=correction_gap,
        source_gap=source_gap,
        boundary_gap=boundary_gap,
        current_gap=current_gap,
        parent_gap=parent_gap,
        div_safety_gap=div_safety_gap,
    )


def build_candidates() -> List[DivergenceCandidate]:
    return [
        DivergenceCandidate(
            name="D1: strict commutation",
            candidate="Div(O X) = O(Div X)",
            status="NOT_DERIVED",
            works_if="O action, domain/codomain, and derivative behavior are all defined",
            hazard="commutation is assumed before O derivative behavior is derived",
        ),
        DivergenceCandidate(
            name="D2: commutation with correction",
            candidate="Div(O X) = O(Div X) + C_O(X)",
            status="CANDIDATE",
            works_if="correction term is explicit, local, auditable, and does not become hidden source",
            hazard="correction term becomes source reservoir or boundary repair",
        ),
        DivergenceCandidate(
            name="D3: divergence-safe constraint",
            candidate="C_constraint(O-state)=0 with divergence side condition",
            status="CANDIDATE",
            works_if="constraint preserves guardrail evidence and has no source/boundary leakage",
            hazard="constraint hides divergence failure",
        ),
        DivergenceCandidate(
            name="D4: residual-only divergence neutrality",
            candidate="Div(O zeta_res) and Div(O kappa_res) carry no ordinary source/current role",
            status="UNDERDETERMINED",
            works_if="residual action and no-overlap criterion are derived",
            hazard="residual neutrality is asserted by label",
        ),
        DivergenceCandidate(
            name="D5: parent-conservation readiness",
            candidate="O supplies parent conservation law",
            status="REJECTED",
            works_if="not allowed in this group",
            hazard="O divergence audit opens parent equation",
        ),
    ]


def build_tests() -> List[DivergenceTest]:
    return [
        DivergenceTest(
            name="T1: strict commutation test",
            test="can Div(OX)=O(Div X) be asserted now?",
            status="NOT_DERIVED",
            result="no; O derivative behavior is not derived",
            implication="strict commutation remains open",
        ),
        DivergenceTest(
            name="T2: correction-term test",
            test="can a correction term C_O be allowed?",
            status="CANDIDATE",
            result="yes as candidate if it is explicit and not a hidden source/boundary repair",
            implication="correction route is possible but controlled",
        ),
        DivergenceTest(
            name="T3: current leakage test",
            test="does O risk creating current flux leakage?",
            status="UNDERDETERMINED",
            result="yes unless current behavior is separately controlled",
            implication="current-flux behavior must be audited later",
        ),
        DivergenceTest(
            name="T4: boundary leakage test",
            test="does O risk creating boundary scalar-tail or shell terms?",
            status="UNDERDETERMINED",
            result="yes unless boundary behavior is separately controlled",
            implication="boundary/source/mass audit must follow",
        ),
        DivergenceTest(
            name="T5: source leakage test",
            test="does O risk creating ordinary source duplication?",
            status="UNDERDETERMINED",
            result="yes unless source behavior is separately controlled",
            implication="source no-double-counting remains open",
        ),
        DivergenceTest(
            name="T6: parent conservation test",
            test="does divergence behavior open parent equation?",
            status="REJECTED",
            result="no; parent equation remains closed",
            implication="divergence audit is not parent closure",
        ),
    ]


def build_requirements() -> List[ConservationRequirement]:
    return [
        ConservationRequirement(
            name="R1: no hidden source",
            requirement="O divergence behavior must not create hidden ordinary source load",
            status="REQUIRED",
            required_for="source no-double-counting",
            fails_if="correction term or residual image becomes source reservoir",
        ),
        ConservationRequirement(
            name="R2: no hidden boundary term",
            requirement="O divergence behavior must not hide boundary scalar-tail, shell, or support terms",
            status="REQUIRED",
            required_for="boundary/support auditability",
            fails_if="O erases boundary/source evidence",
        ),
        ConservationRequirement(
            name="R3: no current leakage",
            requirement="O must not create non-A current flux leakage",
            status="REQUIRED",
            required_for="current-flux neutrality",
            fails_if="O residual action generates current channel",
        ),
        ConservationRequirement(
            name="R4: no recovery selection",
            requirement="commutation/correction behavior cannot be chosen from recovery success",
            status="REQUIRED",
            required_for="recovery independence",
            fails_if="AB=1, Schwarzschild, gamma, or PPN selects divergence behavior",
        ),
        ConservationRequirement(
            name="R5: no insertion license",
            requirement="divergence safety does not license B_s/F_zeta insertion",
            status="REQUIRED",
            required_for="insertion separation",
            fails_if="commutation result is used as insertion law",
        ),
        ConservationRequirement(
            name="R6: no parent gate",
            requirement="divergence audit does not open parent equation",
            status="REQUIRED",
            required_for="parent-gate closure",
            fails_if="O divergence behavior is treated as parent identity",
        ),
    ]


def build_shortcuts() -> List[RejectedDivergenceShortcut]:
    return [
        RejectedDivergenceShortcut(
            name="S1: commutes by projection",
            shortcut="assume O commutes with divergence because it is a projector",
            status="REJECTED",
            reason="projection law itself is not derived",
        ),
        RejectedDivergenceShortcut(
            name="S2: correction as source",
            shortcut="use correction term as hidden ordinary source",
            status="REJECTED",
            reason="source no-double-counting must be preserved",
        ),
        RejectedDivergenceShortcut(
            name="S3: correction as boundary repair",
            shortcut="use correction term to cancel boundary/current/support failure",
            status="REJECTED",
            reason="boundary/source/support failure cannot select O",
        ),
        RejectedDivergenceShortcut(
            name="S4: residual neutrality by label",
            shortcut="declare residual image divergence-neutral",
            status="REJECTED",
            reason="neutrality requires a derived law",
        ),
        RejectedDivergenceShortcut(
            name="S5: recovery-selected commutation",
            shortcut="choose divergence behavior because recovery works",
            status="REJECTED",
            reason="recovery may audit but not construct O",
        ),
        RejectedDivergenceShortcut(
            name="S6: divergence licenses insertion",
            shortcut="use divergence safety as B_s/F_zeta insertion law",
            status="REJECTED",
            reason="insertion remains separate",
        ),
        RejectedDivergenceShortcut(
            name="S7: divergence opens parent",
            shortcut="use divergence audit as parent equation closure",
            status="REJECTED",
            reason="parent gate remains closed",
        ),
    ]


def build_conclusions() -> List[DivergenceConclusion]:
    return [
        DivergenceConclusion(
            name="C1: strict commutation",
            conclusion="Div(OX)=O(Div X) is not derived",
            status="NOT_DERIVED",
            meaning="O derivative behavior remains open",
        ),
        DivergenceConclusion(
            name="C2: correction route",
            conclusion="correction-term route is candidate but constrained",
            status="CANDIDATE",
            meaning="any correction must be explicit and not a source/boundary repair",
        ),
        DivergenceConclusion(
            name="C3: residual divergence neutrality",
            conclusion="residual divergence neutrality is underdetermined",
            status="UNDERDETERMINED",
            meaning="requires residual action and no-overlap law",
        ),
        DivergenceConclusion(
            name="C4: boundary/source/mass next",
            conclusion="boundary/source/mass behavior must be audited next",
            status="OPEN",
            meaning="divergence behavior exposes guardrail risks",
        ),
        DivergenceConclusion(
            name="C5: downstream gates",
            conclusion="divergence audit does not license insertion or parent closure",
            status="REQUIRED",
            meaning="downstream gates remain closed",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: O divergence commutation problem")
    print("Question:")
    print()
    print("  Does O preserve divergence and conservation constraints?")
    print()
    print("Reference discipline:")
    print()
    print("  O cannot enter field equations until derivative/divergence behavior is known.")
    print("  Commutation cannot be assumed from projection vocabulary.")
    print("  Correction terms cannot be hidden sources, boundary repairs, or parent equations.")

    with out.governance_assessments():
        out.line(
            "O divergence commutation audit opened",
            StatusMark.INFO,
            "testing divergence/conservation safety without deriving O",
        )


def case_1_symbol_ledger(symbols: DivergenceSymbols, out: ScriptOutput) -> None:
    header("Case 1: Divergence symbolic ledger")
    print("Candidate operators / leakage symbols:")
    print()
    print(f"  O      = {sp.sstr(symbols.O)}")
    print(f"  Div    = {sp.sstr(symbols.Div)}")
    print(f"  X      = {sp.sstr(symbols.X)}")
    print(f"  J_leak = {sp.sstr(symbols.J_leak)}")
    print(f"  B_bdy  = {sp.sstr(symbols.B_bdy)}")
    print(f"  S_src  = {sp.sstr(symbols.S_src)}")
    print()
    print("Divergence safety gap:")
    print()
    print(f"  L_O_div_gap = {sp.sstr(symbols.div_safety_gap)}")
    print()
    print("Interpretation:")
    print()
    print("  Commutation, correction, source, boundary, current, and parent gaps remain open.")
    print("  Divergence behavior cannot be assumed before O enters field equations.")

    with out.derived_results():
        out.line(
            "O divergence safety gap stated",
            StatusMark.OBLIGATION,
            f"L_O_div_gap = {sp.sstr(symbols.div_safety_gap)}",
        )


def case_2_candidates(items: List[DivergenceCandidate], out: ScriptOutput) -> None:
    header("Case 2: Candidate divergence behaviors")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Candidate: {item.candidate}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Works if: {item.works_if}")
        print(f"Hazard: {item.hazard}")

    with out.governance_assessments():
        out.line(
            "O divergence behavior candidates classified",
            StatusMark.PASS,
            f"{len(items)} divergence behavior candidates classified",
        )


def case_3_tests(items: List[DivergenceTest], out: ScriptOutput) -> None:
    header("Case 3: Divergence behavior tests")
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
            "O divergence behavior tests completed",
            StatusMark.DEFER,
            "strict commutation not derived; correction route candidate but constrained",
        )


def case_4_requirements(items: List[ConservationRequirement], out: ScriptOutput) -> None:
    header("Case 4: Conservation requirements")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Requirement: {item.requirement}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Required for: {item.required_for}")
        print(f"Fails if: {item.fails_if}")

    with out.unresolved_obligations():
        out.line(
            "O divergence conservation requirements stated",
            StatusMark.OBLIGATION,
            f"{len(items)} conservation requirements remain open",
        )


def case_5_shortcuts(items: List[RejectedDivergenceShortcut], out: ScriptOutput) -> None:
    header("Case 5: Rejected divergence shortcuts")
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
            "O divergence shortcuts rejected",
            StatusMark.FAIL,
            "commutes by projection, correction as source/boundary repair, residual neutrality by label, recovery-selected commutation, insertion, and parent shortcuts are rejected",
        )


def case_6_conclusions(items: List[DivergenceConclusion], out: ScriptOutput) -> None:
    header("Case 6: Divergence conclusions")
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
            "O divergence conclusion stated",
            StatusMark.DEFER,
            "strict commutation not derived; boundary/source/mass behavior is next",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("O divergence commutation result:")
    print()
    print("  Div(OX)=O(Div X) is not derived.")
    print("  O derivative behavior remains open.")
    print("  correction-term route is candidate but tightly constrained.")
    print("  residual divergence neutrality is underdetermined.")
    print("  O must not create hidden source, boundary, current, or support leakage.")
    print("  divergence behavior does not license insertion or parent closure.")
    print("  boundary/source/mass behavior must be audited next.")
    print("  O is not derived by this script.")
    print()
    print("Possible next script:")
    print("  candidate_O_boundary_source_mass.py")
    print()
    print("Tiny goblin label:")
    print("  Do not throw the crumbs into divergence.")

    with out.governance_assessments():
        out.line(
            "O divergence commutation audit complete",
            StatusMark.PASS,
            "strict commutation not derived; boundary/source/mass audit remains next",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, symbols: DivergenceSymbols) -> None:
    ns.record_derivation(
        derivation_id="g27_O_divergence",
        inputs=[
            symbols.comm_gap,
            symbols.correction_gap,
            symbols.source_gap,
            symbols.boundary_gap,
            symbols.current_gap,
            symbols.parent_gap,
        ],
        output=symbols.div_safety_gap,
        method="state active-O divergence safety gaps",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="O_divergence_marker",
        scope="Group 27 active O construction",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g27_div_comm", "Derive or reject strict divergence commutation"),
        ("g27_div_corr", "Constrain O divergence correction terms"),
        ("g27_div_source", "Prevent hidden source load"),
        ("g27_div_boundary", "Prevent hidden boundary/support terms"),
        ("g27_div_current", "Prevent current leakage"),
        ("g27_div_recovery", "Prevent recovery-selected divergence behavior"),
        ("g27_div_no_downstream", "Keep insertion and parent gates closed"),
        ("g27_div_next_bsm", "Audit boundary/source/mass behavior next"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g27_div_route"],
            description=(
                "O divergence behavior is not derived here. Any correction route must avoid hidden source, boundary, current, and parent roles."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g27_div_comm",
        "g27_div_corr",
        "g27_div_source",
        "g27_div_boundary",
        "g27_div_current",
        "g27_div_recovery",
        "g27_div_no_downstream",
        "g27_div_next_bsm",
    ]

    ns.record_route(RouteRecord(
        route_id="g27_div_route",
        script_id=SCRIPT_ID,
        name="Group 27 O divergence route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "strict commutation is not assumed",
            "correction terms are explicit and auditable",
            "O does not create hidden source/boundary/current leakage",
            "recovery does not select divergence behavior",
            "insertion and parent gates remain closed",
        ],
    ))

    for branch_id in [
        "commutes_by_projection",
        "correction_as_source",
        "correction_as_boundary_repair",
        "residual_neutral_by_label",
        "recovery_selected_commutation",
        "divergence_licenses_insertion",
        "divergence_opens_parent",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; O divergence behavior must be derived and cannot open downstream gates.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g27_div_not_derived",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "O divergence commutation is not derived. Div(OX)=O(Div X) is not licensed. "
            "A correction-term route remains candidate only if explicit and not a hidden source, boundary repair, current leak, insertion law, or parent opener. "
            "Boundary/source/mass behavior must be audited next."
        ),
        derivation_ids=["g27_O_divergence"],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate O Divergence Commutation")
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
    case_1_symbol_ledger(symbols, out)
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
