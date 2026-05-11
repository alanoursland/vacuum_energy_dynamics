# Candidate O projection law
#
# Group:
#   27_active_O_construction
#
# Script type:
#   ALGEBRAIC OPERATOR LAW INVENTORY
#
# Purpose
# -------
# Test whether active O is a projection, replacement map, constraint operator,
# or something else.
#
# Locked-door question:
#
#   Is O a projection, a replacement map, a constraint operator, or something else?
#
# This script does not derive active O.
# It does not prove no-overlap.
# It does not prove kernel/image closure.
# It does not derive residual control.
# It does not derive B_s/F_zeta insertion.
# It does not open parent equation closure.
#
# Tiny goblin rule:
#
#   A projector must project, not merely point.

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
        "ADMISSIBLE_CANDIDATE": StatusMark.INFO,
        "BLOCKED": StatusMark.FAIL,
        "CANDIDATE": StatusMark.DEFER,
        "INSUFFICIENT": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "PARTIAL": StatusMark.INFO,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "TARGET": StatusMark.DEFER,
        "UNDERDETERMINED": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g27_O_problem",
            "27_active_O_construction__candidate_O_problem_ledger",
            "g27_O_problem",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g27_dc",
            "27_active_O_construction__candidate_O_domain_codomain",
            "g27_O_domain_codomain",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g27_ki",
            "27_active_O_construction__candidate_O_kernel_image",
            "g27_O_kernel_image",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g27_pair",
            "27_active_O_construction__candidate_O_no_overlap_pairing",
            "g27_O_pairing",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g26_summary",
            "26_residual_control_theorem_attempt__candidate_group_26_status_summary",
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
class ProjectionLawSymbols:
    O: sp.Symbol
    I: sp.Symbol
    P_trace: sp.Symbol
    P_res: sp.Symbol
    R_replace: sp.Symbol
    C_constraint: sp.Symbol
    zeta_Bs: sp.Symbol
    zeta_res: sp.Symbol
    kappa_res: sp.Symbol
    idempotence_gap: sp.Symbol
    preservation_gap: sp.Symbol
    residual_action_gap: sp.Symbol
    linearity_gap: sp.Symbol
    composition_gap: sp.Symbol
    replacement_gap: sp.Symbol
    constraint_gap: sp.Symbol
    alg_gap: sp.Expr


@dataclass
class OperatorLawCandidate:
    name: str
    law: str
    status: str
    works_if: str
    hazard: str


@dataclass
class AlgebraicTest:
    name: str
    test: str
    status: str
    result: str
    implication: str


@dataclass
class RequiredOperatorBehavior:
    name: str
    behavior: str
    status: str
    required_for: str
    fails_if: str


@dataclass
class RejectedProjectionShortcut:
    name: str
    shortcut: str
    status: str
    reason: str


@dataclass
class ProjectionLawConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


# =============================================================================
# Builders
# =============================================================================


def build_symbols() -> ProjectionLawSymbols:
    (
        O,
        I,
        P_trace,
        P_res,
        R_replace,
        C_constraint,
        zeta_Bs,
        zeta_res,
        kappa_res,
        idempotence_gap,
        preservation_gap,
        residual_action_gap,
        linearity_gap,
        composition_gap,
        replacement_gap,
        constraint_gap,
    ) = sp.symbols(
        "O I P_trace P_res R_replace C_constraint zeta_Bs zeta_res kappa_res "
        "idempotence_gap preservation_gap residual_action_gap linearity_gap composition_gap replacement_gap constraint_gap",
        real=True,
    )

    alg_gap = sp.simplify(
        idempotence_gap
        + preservation_gap
        + residual_action_gap
        + linearity_gap
        + composition_gap
        + replacement_gap
        + constraint_gap
    )

    return ProjectionLawSymbols(
        O=O,
        I=I,
        P_trace=P_trace,
        P_res=P_res,
        R_replace=R_replace,
        C_constraint=C_constraint,
        zeta_Bs=zeta_Bs,
        zeta_res=zeta_res,
        kappa_res=kappa_res,
        idempotence_gap=idempotence_gap,
        preservation_gap=preservation_gap,
        residual_action_gap=residual_action_gap,
        linearity_gap=linearity_gap,
        composition_gap=composition_gap,
        replacement_gap=replacement_gap,
        constraint_gap=constraint_gap,
        alg_gap=alg_gap,
    )


def build_law_candidates() -> List[OperatorLawCandidate]:
    return [
        OperatorLawCandidate(
            name="L1: projection law",
            law="O^2 = O",
            status="UNDERDETERMINED",
            works_if="domain/codomain, kernel/image, and sector composition are derived",
            hazard="idempotence is assumed because O is called a projector",
        ),
        OperatorLawCandidate(
            name="L2: trace-preserving projection",
            law="O(zeta_Bs) = zeta_Bs",
            status="CANDIDATE",
            works_if="zeta_Bs belongs to safe trace image and is excluded from kernel",
            hazard="safe trace preservation is assumed but not compatible with residual action",
        ),
        OperatorLawCandidate(
            name="L3: residual-kill projection",
            law="O(zeta_res) = 0 and O(kappa_res) = 0",
            status="UNDERDETERMINED",
            works_if="zeta/kappa kernel membership follows from no-overlap criterion",
            hazard="residual kill is smuggled as operator law",
        ),
        OperatorLawCandidate(
            name="L4: inert replacement law",
            law="O(zeta_res, kappa_res) -> inert_residual sector",
            status="UNDERDETERMINED",
            works_if="inert sector is derived as no-reentry/no-role sector",
            hazard="inert sector is used by label",
        ),
        OperatorLawCandidate(
            name="L5: constraint operator law",
            law="C_constraint(O-state) = 0 imposes no-overlap without erasing data",
            status="CANDIDATE",
            works_if="constraint preserves guardrail auditability and has divergence behavior",
            hazard="constraint hides boundary/source failures or acts as parent equation",
        ),
        OperatorLawCandidate(
            name="L6: universal linear operator law",
            law="O(aX+bY)=aO(X)+bO(Y) on all sectors",
            status="NOT_DERIVED",
            works_if="linearity and universal domain are derived",
            hazard="linearity/universal domain are assumed",
        ),
    ]


def build_tests() -> List[AlgebraicTest]:
    return [
        AlgebraicTest(
            name="T1: idempotence test",
            test="can O^2 = O be asserted now?",
            status="NOT_DERIVED",
            result="no; idempotence requires domain/codomain, kernel/image, and composition law",
            implication="projection status remains underdetermined",
        ),
        AlgebraicTest(
            name="T2: trace preservation test",
            test="can O(zeta_Bs)=zeta_Bs be used as candidate?",
            status="CANDIDATE",
            result="yes as a candidate preservation law, not as full O derivation",
            implication="safe trace image remains the cleanest preserved direction",
        ),
        AlgebraicTest(
            name="T3: residual kill test",
            test="can O(zeta_res)=0 and O(kappa_res)=0 be asserted now?",
            status="NOT_DERIVED",
            result="no; this would smuggle residual kill unless kernel membership is derived",
            implication="residual-kill projection is not licensed",
        ),
        AlgebraicTest(
            name="T4: inert replacement test",
            test="can O map residuals into an inert sector now?",
            status="UNDERDETERMINED",
            result="not yet; inert sector safety remains underived",
            implication="replacement law remains candidate only",
        ),
        AlgebraicTest(
            name="T5: constraint law test",
            test="can O be treated as a constraint rather than eraser?",
            status="CANDIDATE",
            result="possible, but constraint must preserve guardrail auditability and divergence behavior",
            implication="constraint route may be safer than kill-by-projection",
        ),
        AlgebraicTest(
            name="T6: linearity test",
            test="can O be assumed linear?",
            status="NOT_DERIVED",
            result="no; linearity is not supplied by current objects",
            implication="do not use linear projector algebra unless derived",
        ),
    ]


def build_required_behaviors() -> List[RequiredOperatorBehavior]:
    return [
        RequiredOperatorBehavior(
            name="B1: preserve safe trace",
            behavior="O must preserve zeta_Bs if zeta_Bs is in image",
            status="REQUIRED",
            required_for="safe scalar trace target",
            fails_if="O kills or duplicates zeta_Bs",
        ),
        RequiredOperatorBehavior(
            name="B2: control residuals by law",
            behavior="O action on zeta_res/kappa_res must follow from no-overlap criterion",
            status="REQUIRED",
            required_for="residual-control retest",
            fails_if="residual action is declared",
        ),
        RequiredOperatorBehavior(
            name="B3: preserve guardrail data",
            behavior="O must not erase boundary/source/support failure evidence",
            status="REQUIRED",
            required_for="boundary/source/support compatibility",
            fails_if="O hides repair failures",
        ),
        RequiredOperatorBehavior(
            name="B4: preserve accounting discipline",
            behavior="O must not map residuals into accounting reservoir",
            status="REQUIRED",
            required_for="accounting no-hidden-role discipline",
            fails_if="epsilon/e_kappa carries residual metric/source load",
        ),
        RequiredOperatorBehavior(
            name="B5: leave divergence open",
            behavior="O algebraic law must not assume divergence commutation",
            status="REQUIRED",
            required_for="next divergence-commutation audit",
            fails_if="O is used in field equations before divergence behavior",
        ),
        RequiredOperatorBehavior(
            name="B6: keep downstream gates closed",
            behavior="O algebraic law must not license insertion or parent closure",
            status="REQUIRED",
            required_for="insertion separation and parent-gate closure",
            fails_if="O law opens B_s/F_zeta insertion or parent equation",
        ),
    ]


def build_shortcuts() -> List[RejectedProjectionShortcut]:
    return [
        RejectedProjectionShortcut(
            name="S1: projector by name",
            shortcut="assume O^2=O because O is called a projection",
            status="REJECTED",
            reason="idempotence requires derived composition law",
        ),
        RejectedProjectionShortcut(
            name="S2: linear by habit",
            shortcut="assume O is linear on all sectors",
            status="REJECTED",
            reason="linearity and universal domain are not derived",
        ),
        RejectedProjectionShortcut(
            name="S3: residual kill by projection",
            shortcut="set O(zeta_res)=O(kappa_res)=0 without kernel theorem",
            status="REJECTED",
            reason="this smuggles residual kill",
        ),
        RejectedProjectionShortcut(
            name="S4: inert replacement by label",
            shortcut="map residuals to inert sector by vocabulary",
            status="REJECTED",
            reason="inert sector safety is not derived",
        ),
        RejectedProjectionShortcut(
            name="S5: constraint hides failure",
            shortcut="constraint law removes boundary/source/support failures from view",
            status="REJECTED",
            reason="guardrail auditability must be preserved",
        ),
        RejectedProjectionShortcut(
            name="S6: algebraic law licenses insertion",
            shortcut="projection/replacement law opens B_s/F_zeta insertion",
            status="REJECTED",
            reason="insertion law remains separate",
        ),
        RejectedProjectionShortcut(
            name="S7: algebraic law opens parent",
            shortcut="projection/replacement law opens parent equation",
            status="REJECTED",
            reason="parent gate remains closed",
        ),
    ]


def build_conclusions() -> List[ProjectionLawConclusion]:
    return [
        ProjectionLawConclusion(
            name="C1: projection law",
            conclusion="O^2=O is not derived",
            status="NOT_DERIVED",
            meaning="projection status remains underdetermined",
        ),
        ProjectionLawConclusion(
            name="C2: trace preservation",
            conclusion="O(zeta_Bs)=zeta_Bs is a candidate preservation law",
            status="CANDIDATE",
            meaning="safe trace direction remains the cleanest preserved image candidate",
        ),
        ProjectionLawConclusion(
            name="C3: residual kill law",
            conclusion="O(zeta_res)=O(kappa_res)=0 is not derived",
            status="NOT_DERIVED",
            meaning="kernel membership and no-overlap criterion are still missing",
        ),
        ProjectionLawConclusion(
            name="C4: replacement/constraint route",
            conclusion="inert replacement or constraint law remains candidate but underdetermined",
            status="UNDERDETERMINED",
            meaning="may be safer than eraser O, but requires divergence and guardrail behavior",
        ),
        ProjectionLawConclusion(
            name="C5: next route",
            conclusion="divergence commutation must be audited before O can enter field equations",
            status="OPEN",
            meaning="algebraic law inventory points to divergence behavior next",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: O projection/replacement law problem")
    print("Question:")
    print()
    print("  Is O a projection, a replacement map, a constraint operator, or something else?")
    print()
    print("Reference discipline:")
    print()
    print("  Projection requires idempotence and composition law.")
    print("  Replacement requires safe target sector.")
    print("  Constraint requires auditability and divergence behavior.")
    print("  None may license insertion or parent closure.")

    with out.governance_assessments():
        out.line(
            "O projection/replacement law inventory opened",
            StatusMark.INFO,
            "testing algebraic operator law candidates without deriving O",
        )


def case_1_symbol_ledger(symbols: ProjectionLawSymbols, out: ScriptOutput) -> None:
    header("Case 1: Algebraic law symbolic ledger")
    print("Candidate operator symbols:")
    print()
    print(f"  O            = {sp.sstr(symbols.O)}")
    print(f"  I            = {sp.sstr(symbols.I)}")
    print(f"  P_trace      = {sp.sstr(symbols.P_trace)}")
    print(f"  P_res        = {sp.sstr(symbols.P_res)}")
    print(f"  R_replace    = {sp.sstr(symbols.R_replace)}")
    print(f"  C_constraint = {sp.sstr(symbols.C_constraint)}")
    print()
    print("Algebraic law gap:")
    print()
    print(f"  L_O_alg_gap = {sp.sstr(symbols.alg_gap)}")
    print()
    print("Interpretation:")
    print()
    print("  Projection, replacement, constraint, linearity, composition, and residual action remain open.")
    print("  Algebraic law cannot close without no-overlap and divergence behavior.")

    with out.derived_results():
        out.line(
            "O algebraic law gap stated",
            StatusMark.OBLIGATION,
            f"L_O_alg_gap = {sp.sstr(symbols.alg_gap)}",
        )


def case_2_law_candidates(items: List[OperatorLawCandidate], out: ScriptOutput) -> None:
    header("Case 2: Candidate O algebraic laws")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Law: {item.law}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Works if: {item.works_if}")
        print(f"Hazard: {item.hazard}")

    with out.governance_assessments():
        out.line(
            "O algebraic law candidates classified",
            StatusMark.PASS,
            f"{len(items)} algebraic law candidates classified",
        )


def case_3_tests(items: List[AlgebraicTest], out: ScriptOutput) -> None:
    header("Case 3: Algebraic law tests")
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
            "O algebraic law tests completed",
            StatusMark.DEFER,
            "trace preservation candidate survives; projection and residual kill are not derived",
        )


def case_4_required_behaviors(items: List[RequiredOperatorBehavior], out: ScriptOutput) -> None:
    header("Case 4: Required behavior for any algebraic law")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Behavior: {item.behavior}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Required for: {item.required_for}")
        print(f"Fails if: {item.fails_if}")

    with out.unresolved_obligations():
        out.line(
            "O algebraic-law behavior requirements stated",
            StatusMark.OBLIGATION,
            f"{len(items)} behaviors must be preserved by any algebraic law",
        )


def case_5_shortcuts(items: List[RejectedProjectionShortcut], out: ScriptOutput) -> None:
    header("Case 5: Rejected projection/replacement shortcuts")
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
            "O algebraic-law shortcuts rejected",
            StatusMark.FAIL,
            "projector by name, linear by habit, residual kill by projection, inert replacement by label, constraint hiding, insertion, and parent shortcuts are rejected",
        )


def case_6_conclusions(items: List[ProjectionLawConclusion], out: ScriptOutput) -> None:
    header("Case 6: Projection/replacement law conclusions")
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
            "O algebraic law conclusion stated",
            StatusMark.DEFER,
            "projection not derived; trace preservation candidate survives; divergence behavior is next",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("O projection/replacement law result:")
    print()
    print("  O^2 = O is not derived.")
    print("  O linearity is not derived.")
    print("  O(zeta_Bs) = zeta_Bs remains a candidate preservation law.")
    print("  O(zeta_res)=O(kappa_res)=0 is not derived.")
    print("  inert replacement or constraint law remains candidate but underdetermined.")
    print("  algebraic law must preserve guardrail data and cannot license insertion or parent closure.")
    print("  divergence behavior must be audited before O can enter field equations.")
    print("  O is not derived by this script.")
    print()
    print("Possible next script:")
    print("  candidate_O_divergence_commutation.py")
    print()
    print("Tiny goblin label:")
    print("  A projector must project, not merely point.")

    with out.governance_assessments():
        out.line(
            "O projection/replacement law inventory complete",
            StatusMark.PASS,
            "projection law not derived; divergence behavior remains next",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, symbols: ProjectionLawSymbols) -> None:
    ns.record_derivation(
        derivation_id="g27_O_alg_law",
        inputs=[
            symbols.idempotence_gap,
            symbols.preservation_gap,
            symbols.residual_action_gap,
            symbols.linearity_gap,
            symbols.composition_gap,
            symbols.replacement_gap,
            symbols.constraint_gap,
        ],
        output=symbols.alg_gap,
        method="state candidate active-O algebraic law gaps",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="O_alg_law_marker",
        scope="Group 27 active O construction",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g27_alg_idempotence", "Derive or reject O idempotence"),
        ("g27_alg_preserve_zeta", "Preserve zeta_Bs if O acts on safe trace"),
        ("g27_alg_res_action", "Derive O residual action"),
        ("g27_alg_linearity", "Derive or reject O linearity"),
        ("g27_alg_replacement", "Define replacement law if used"),
        ("g27_alg_constraint", "Define constraint law if used"),
        ("g27_alg_div_next", "Audit divergence behavior next"),
        ("g27_alg_no_downstream", "Keep insertion and parent gates closed"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g27_alg_route"],
            description=(
                "O algebraic law candidates are inventoried here, but O is not derived. Divergence behavior remains open."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g27_alg_idempotence",
        "g27_alg_preserve_zeta",
        "g27_alg_res_action",
        "g27_alg_linearity",
        "g27_alg_replacement",
        "g27_alg_constraint",
        "g27_alg_div_next",
        "g27_alg_no_downstream",
    ]

    ns.record_route(RouteRecord(
        route_id="g27_alg_route",
        script_id=SCRIPT_ID,
        name="Group 27 O algebraic law route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "idempotence is not assumed",
            "linearity is not assumed",
            "trace preservation remains candidate",
            "residual action is not declared",
            "replacement/constraint law is not downstream closure",
            "divergence behavior remains next",
        ],
    ))

    for branch_id in [
        "projector_by_name",
        "linear_by_habit",
        "residual_kill_by_projection",
        "inert_replacement_by_label",
        "constraint_hides_failure",
        "alg_law_licenses_insertion",
        "alg_law_opens_parent",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; O algebraic law must be derived and cannot open downstream gates.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g27_alg_not_derived",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "O algebraic law is not derived. O^2=O, linearity, and residual-kill projection are not licensed. "
            "O(zeta_Bs)=zeta_Bs remains a candidate preservation law. Inert replacement or constraint law remains candidate but underdetermined. "
            "Divergence behavior must be audited next; insertion and parent gates remain closed."
        ),
        derivation_ids=["g27_O_alg_law"],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate O Projection Law")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    laws = build_law_candidates()
    tests = build_tests()
    behaviors = build_required_behaviors()
    shortcuts = build_shortcuts()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_symbol_ledger(symbols, out)
    case_2_law_candidates(laws, out)
    case_3_tests(tests, out)
    case_4_required_behaviors(behaviors, out)
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
