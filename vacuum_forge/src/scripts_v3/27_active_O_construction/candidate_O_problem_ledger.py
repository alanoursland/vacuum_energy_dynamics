# Candidate O problem ledger
#
# Group:
#   27_active_O_construction
#
# Human title:
#   Active No-Overlap Operator Construction
#
# Script type:
#   PROBLEM LEDGER / OPERATOR CONSTRUCTION TARGET
#
# Purpose
# -------
# Open the active-O construction group by stating what active O must do,
# what it must preserve, what it must separate, and what it is forbidden to
# repair, select, license, or open.
#
# Locked-door question:
#
#   What exactly must active O do, and what is forbidden?
#
# This script does not derive active O.
# It does not derive residual control.
# It does not derive B_s/F_zeta insertion.
# It does not derive count-once recombination.
# It does not open parent equation closure.
#
# Tiny goblin rule:
#
#   Do not wave the wand.
#   Forge the tool.

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
        "FORBIDDEN": StatusMark.FAIL,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "PRESERVE": StatusMark.OBLIGATION,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "TARGET": StatusMark.DEFER,
        "THEOREM_TARGET": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g26_summary",
            "26_residual_control_theorem_attempt__candidate_group_26_status_summary",
            "g26_status_summary",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g26_oblig",
            "26_residual_control_theorem_attempt__candidate_residual_control_theorem_attempt_obligations",
            "g26_obligation_status",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g26_nonO",
            "26_residual_control_theorem_attempt__candidate_residual_control_without_active_O_obstruction",
            "residual_control_without_active_O_obstruction_marker_26",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g26_O_class",
            "26_residual_control_theorem_attempt__candidate_minimal_O_necessity_or_deferral",
            "minimal_O_necessity_or_deferral_marker_26",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g25_O_burden",
            "25_residual_kill_or_no_overlap_theorem__candidate_no_overlap_operator_minimum_burden",
            "no_overlap_operator_minimum_burden_marker_25",
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
class OProblemSymbols:
    zeta_Bs: sp.Symbol
    zeta_res: sp.Symbol
    kappa_res: sp.Symbol
    eps_acc: sp.Symbol
    ekappa_acc: sp.Symbol
    domain_gap: sp.Symbol
    codomain_gap: sp.Symbol
    kernel_gap: sp.Symbol
    image_gap: sp.Symbol
    pairing_gap: sp.Symbol
    law_gap: sp.Symbol
    div_gap: sp.Symbol
    boundary_gap: sp.Symbol
    source_gap: sp.Symbol
    mass_gap: sp.Symbol
    current_gap: sp.Symbol
    support_gap: sp.Symbol
    recovery_gap: sp.Symbol
    insertion_gap: sp.Symbol
    parent_gap: sp.Symbol
    O_burden: sp.Expr


@dataclass
class OTask:
    name: str
    task: str
    status: str
    needed_for: str
    failure_if: str


@dataclass
class OGuardrail:
    name: str
    preserve: str
    status: str
    reason: str
    violation_if: str


@dataclass
class ForbiddenOUse:
    name: str
    forbidden_use: str
    status: str
    reason: str


@dataclass
class OConstructionBoundary:
    name: str
    boundary: str
    status: str
    meaning: str


# =============================================================================
# Builders
# =============================================================================


def build_symbols() -> OProblemSymbols:
    (
        zeta_Bs,
        zeta_res,
        kappa_res,
        eps_acc,
        ekappa_acc,
        domain_gap,
        codomain_gap,
        kernel_gap,
        image_gap,
        pairing_gap,
        law_gap,
        div_gap,
        boundary_gap,
        source_gap,
        mass_gap,
        current_gap,
        support_gap,
        recovery_gap,
        insertion_gap,
        parent_gap,
    ) = sp.symbols(
        "zeta_Bs zeta_res kappa_res eps_acc ekappa_acc "
        "domain_gap codomain_gap kernel_gap image_gap pairing_gap law_gap div_gap "
        "boundary_gap source_gap mass_gap current_gap support_gap recovery_gap insertion_gap parent_gap",
        real=True,
    )

    O_burden = sp.simplify(
        domain_gap
        + codomain_gap
        + kernel_gap
        + image_gap
        + pairing_gap
        + law_gap
        + div_gap
        + boundary_gap
        + source_gap
        + mass_gap
        + current_gap
        + support_gap
        + recovery_gap
        + insertion_gap
        + parent_gap
    )

    return OProblemSymbols(
        zeta_Bs=zeta_Bs,
        zeta_res=zeta_res,
        kappa_res=kappa_res,
        eps_acc=eps_acc,
        ekappa_acc=ekappa_acc,
        domain_gap=domain_gap,
        codomain_gap=codomain_gap,
        kernel_gap=kernel_gap,
        image_gap=image_gap,
        pairing_gap=pairing_gap,
        law_gap=law_gap,
        div_gap=div_gap,
        boundary_gap=boundary_gap,
        source_gap=source_gap,
        mass_gap=mass_gap,
        current_gap=current_gap,
        support_gap=support_gap,
        recovery_gap=recovery_gap,
        insertion_gap=insertion_gap,
        parent_gap=parent_gap,
        O_burden=O_burden,
    )


def build_tasks() -> List[OTask]:
    return [
        OTask(
            name="T1: define domain",
            task="specify the input sector D_O on which O acts",
            status="REQUIRED",
            needed_for="preventing O from acting on undefined objects",
            failure_if="O acts on zeta/kappa/current/support/source data without declaring the input sector",
        ),
        OTask(
            name="T2: define codomain",
            task="specify the output sector C_O after O acts",
            status="REQUIRED",
            needed_for="knowing whether output is metric, inert, diagnostic, projected, or constrained",
            failure_if="O output silently becomes metric/source/boundary/parent data",
        ),
        OTask(
            name="T3: define kernel",
            task="state which residual directions are killed or removed by O, if any",
            status="REQUIRED",
            needed_for="honest residual separation",
            failure_if="zeta_residual_metric or kappa_metric are erased by name",
        ),
        OTask(
            name="T4: define image",
            task="state what O preserves or produces",
            status="REQUIRED",
            needed_for="protecting zeta_to_Bs as the safe trace channel",
            failure_if="O changes zeta_to_Bs or creates a second scalar trace path",
        ),
        OTask(
            name="T5: define no-overlap criterion",
            task="derive the pairing, sector split, support split, or routing rule that makes overlap meaningful",
            status="REQUIRED",
            needed_for="turning no-overlap into mathematics rather than vocabulary",
            failure_if="orthogonality or disjointness is asserted without a criterion",
        ),
        OTask(
            name="T6: define algebraic law",
            task="classify O as projection, replacement map, constraint, or another operator type",
            status="REQUIRED",
            needed_for="knowing whether O^2=O, whether O is linear, and how O composes",
            failure_if="projection/idempotence/linearity is assumed before derivation",
        ),
        OTask(
            name="T7: derive divergence behavior",
            task="check whether O commutes with divergence or creates correction terms",
            status="REQUIRED",
            needed_for="future conservation and parent-equation safety",
            failure_if="O is used inside field equations without divergence behavior",
        ),
        OTask(
            name="T8: derive boundary/source/mass behavior",
            task="prove O does not shift A-sector mass, create scalar/current tails, create shell/source load, or duplicate ordinary source",
            status="REQUIRED",
            needed_for="boundary neutrality and source no-double-counting",
            failure_if="O repairs boundary/source failure or hides mass/current leakage",
        ),
        OTask(
            name="T9: derive recovery independence",
            task="define O without selecting it from Schwarzschild, AB=1, B=1/A, gamma, PPN, or weak-field success",
            status="REQUIRED",
            needed_for="keeping recovery as audit rather than construction",
            failure_if="recovery target chooses O",
        ),
        OTask(
            name="T10: preserve downstream gates",
            task="keep B_s/F_zeta insertion and parent equation closed",
            status="REQUIRED",
            needed_for="preventing O construction from becoming insertion or parent closure",
            failure_if="O construction licenses insertion or opens parent equation",
        ),
    ]


def build_guardrails() -> List[OGuardrail]:
    return [
        OGuardrail(
            name="G1: preserve safe scalar trace target",
            preserve="zeta_to_Bs remains the only safe ordinary scalar trace insertion target",
            status="PRESERVE",
            reason="count-once scalar trace requires no second zeta residual path",
            violation_if="zeta enters both B_s and residual metric trace",
        ),
        OGuardrail(
            name="G2: preserve geometric residual discipline",
            preserve="zeta_residual_metric and kappa_metric remain unresolved unless O actually controls them",
            status="PRESERVE",
            reason="Group 26 did not derive their non-reentry",
            violation_if="O erases zeta/kappa residuals by name",
        ),
        OGuardrail(
            name="G3: preserve accounting discipline",
            preserve="epsilon_vac and e_kappa remain accounting targets, not hidden reservoirs",
            status="PRESERVE",
            reason="accounting partial reduction cannot repair geometry",
            violation_if="epsilon/e_kappa hides zeta/kappa residuals or supplies source/metric load",
        ),
        OGuardrail(
            name="G4: preserve recovery independence",
            preserve="recovery may audit O but may not define or select O",
            status="PRESERVE",
            reason="recovery-selected O would smuggle weak-field or Schwarzschild targets",
            violation_if="AB=1, B=1/A, gamma, PPN, or Schwarzschild success selects O",
        ),
        OGuardrail(
            name="G5: preserve boundary/source independence",
            preserve="boundary/source/support failure may reject O but may not choose O",
            status="PRESERVE",
            reason="O cannot be a repair patch",
            violation_if="tail, flux, shell, source duplication, mass shift, or support load selects O",
        ),
        OGuardrail(
            name="G6: preserve insertion separation",
            preserve="O construction does not license B_s/F_zeta insertion",
            status="PRESERVE",
            reason="insertion law and coefficient origin remain separate obligations",
            violation_if="O existence or O classification is treated as insertion theorem",
        ),
        OGuardrail(
            name="G7: preserve parent-gate closure",
            preserve="O construction does not open the parent field equation",
            status="PRESERVE",
            reason="parent closure requires residual control, insertion, source/boundary/support, divergence, and parent identity",
            violation_if="O construction is treated as parent equation readiness",
        ),
    ]


def build_forbidden_uses() -> List[ForbiddenOUse]:
    return [
        ForbiddenOUse(
            name="F1: O by name",
            forbidden_use="using O because it is called no-overlap",
            status="REJECTED",
            reason="name is not structure",
        ),
        ForbiddenOUse(
            name="F2: O as magic eraser",
            forbidden_use="O removes residuals without domain, codomain, kernel, image, or no-overlap criterion",
            status="REJECTED",
            reason="residual control would be declared rather than derived",
        ),
        ForbiddenOUse(
            name="F3: O as hidden recovery postulate",
            forbidden_use="O is selected because it recovers AB=1, B=1/A, Schwarzschild, gamma, or PPN",
            status="REJECTED",
            reason="recovery is downstream audit only",
        ),
        ForbiddenOUse(
            name="F4: O as boundary/source repair",
            forbidden_use="O is chosen to remove scalar tails, current flux, shell/source load, support load, or source duplication",
            status="REJECTED",
            reason="guardrail failure cannot construct the operator",
        ),
        ForbiddenOUse(
            name="F5: O as accounting reservoir",
            forbidden_use="O sends residuals into epsilon/e_kappa accounting variables that then carry metric/source roles",
            status="REJECTED",
            reason="accounting reductions cannot hide geometry",
        ),
        ForbiddenOUse(
            name="F6: O as insertion license",
            forbidden_use="O construction is treated as B_s/F_zeta insertion law",
            status="REJECTED",
            reason="coefficient origin and insertion law remain separate",
        ),
        ForbiddenOUse(
            name="F7: O as parent opener",
            forbidden_use="O construction is treated as parent equation readiness",
            status="REJECTED",
            reason="parent gate remains closed",
        ),
        ForbiddenOUse(
            name="F8: O necessity by frustration",
            forbidden_use="O is declared necessary merely because non-O routes did not close",
            status="REJECTED",
            reason="controlled obstruction is not mathematical no-go theorem",
        ),
    ]


def build_boundaries() -> List[OConstructionBoundary]:
    return [
        OConstructionBoundary(
            name="B1: candidate O allowed",
            boundary="it is allowed to propose a candidate O structure",
            status="CANDIDATE",
            meaning="only if domain/codomain/kernel/image/no-overlap behavior are explicitly tracked",
        ),
        OConstructionBoundary(
            name="B2: partial O allowed",
            boundary="it is allowed to derive only part of O",
            status="CANDIDATE",
            meaning="partial domain/codomain/kernel/image results are useful if not promoted to full operator",
        ),
        OConstructionBoundary(
            name="B3: O underdetermination allowed",
            boundary="it is allowed to conclude O cannot be built from current objects",
            status="CANDIDATE",
            meaning="a missing pairing, coefficient origin, divergence law, or boundary/source theorem would be a valid obstruction",
        ),
        OConstructionBoundary(
            name="B4: O not automatically residual control",
            boundary="even a candidate O does not automatically solve residual control",
            status="REQUIRED",
            meaning="residual control must be retested with the actual O structure",
        ),
        OConstructionBoundary(
            name="B5: O not insertion or parent closure",
            boundary="O construction does not automatically license insertion or parent field equation",
            status="REQUIRED",
            meaning="downstream gates remain separate",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Active O construction problem")
    print("Question:")
    print()
    print("  What exactly must active O do, and what is forbidden?")
    print()
    print("Reference discipline:")
    print()
    print("  O is optional-open/deferred, not derived, and not proven necessary.")
    print("  O is the preferred constructive route only if it is actually built.")
    print("  This script states the construction burden; it does not construct O.")

    with out.governance_assessments():
        out.line(
            "active-O construction problem ledger opened",
            StatusMark.INFO,
            "stating O construction burden without using O as tool",
        )


def case_1_symbol_ledger(symbols: OProblemSymbols, out: ScriptOutput) -> None:
    header("Case 1: O construction burden ledger")
    print("Core sectors:")
    print()
    print(f"  safe trace target: {sp.sstr(symbols.zeta_Bs)}")
    print(f"  zeta residual:    {sp.sstr(symbols.zeta_res)}")
    print(f"  kappa residual:   {sp.sstr(symbols.kappa_res)}")
    print(f"  epsilon account:  {sp.sstr(symbols.eps_acc)}")
    print(f"  e_kappa account:  {sp.sstr(symbols.ekappa_acc)}")
    print()
    print("O construction gaps:")
    print()
    for name in [
        "domain_gap",
        "codomain_gap",
        "kernel_gap",
        "image_gap",
        "pairing_gap",
        "law_gap",
        "div_gap",
        "boundary_gap",
        "source_gap",
        "mass_gap",
        "current_gap",
        "support_gap",
        "recovery_gap",
        "insertion_gap",
        "parent_gap",
    ]:
        print(f"  {name} = {sp.sstr(getattr(symbols, name))}")
    print()
    print("Total O construction burden:")
    print()
    print(f"  L_O_burden = {sp.sstr(symbols.O_burden)}")
    print()
    print("Interpretation:")
    print()
    print("  O is not available until the relevant burdens are closed by construction.")
    print("  Each gap is a theorem target, not an assumed property.")

    with out.derived_results():
        out.line(
            "active-O construction burden stated",
            StatusMark.OBLIGATION,
            f"L_O_burden = {sp.sstr(symbols.O_burden)}",
        )


def case_2_tasks(tasks: List[OTask], out: ScriptOutput) -> None:
    header("Case 2: Active O construction tasks")
    for task in tasks:
        print()
        print("-" * 120)
        print(task.name)
        print("-" * 120)
        print(f"Task: {task.task}")
        print(f"[{status_mark(task.status).value}] {task.name}: {task.status}")
        print(f"Needed for: {task.needed_for}")
        print(f"Failure if: {task.failure_if}")

    with out.unresolved_obligations():
        out.line(
            "active-O construction task ledger populated",
            StatusMark.OBLIGATION,
            f"{len(tasks)} construction tasks remain open",
        )


def case_3_guardrails(guardrails: List[OGuardrail], out: ScriptOutput) -> None:
    header("Case 3: Guardrails O must preserve")
    for guardrail in guardrails:
        print()
        print("-" * 120)
        print(guardrail.name)
        print("-" * 120)
        print(f"Preserve: {guardrail.preserve}")
        print(f"[{status_mark(guardrail.status).value}] {guardrail.name}: {guardrail.status}")
        print(f"Reason: {guardrail.reason}")
        print(f"Violation if: {guardrail.violation_if}")

    with out.governance_assessments():
        out.line(
            "active-O preservation guardrails stated",
            StatusMark.PASS,
            f"{len(guardrails)} guardrails must be preserved by any candidate O",
        )


def case_4_forbidden_uses(forbidden: List[ForbiddenOUse], out: ScriptOutput) -> None:
    header("Case 4: Forbidden O uses")
    for item in forbidden:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Forbidden use: {item.forbidden_use}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Reason: {item.reason}")

    with out.counterexamples():
        out.line(
            "active-O shortcut uses rejected",
            StatusMark.FAIL,
            "O by name, magic eraser, recovery-selected O, repair-selected O, accounting reservoir, insertion, parent, and necessity-by-frustration are rejected",
        )


def case_5_boundaries(boundaries: List[OConstructionBoundary], out: ScriptOutput) -> None:
    header("Case 5: Construction boundaries")
    for boundary in boundaries:
        print()
        print("-" * 120)
        print(boundary.name)
        print("-" * 120)
        print(f"Boundary: {boundary.boundary}")
        print(f"[{status_mark(boundary.status).value}] {boundary.name}: {boundary.status}")
        print(f"Meaning: {boundary.meaning}")

    with out.governance_assessments():
        out.line(
            "active-O construction boundaries stated",
            StatusMark.PASS,
            "candidate, partial, and obstruction outcomes are allowed; automatic residual/insertion/parent closure is not",
        )


def case_6_failure_controls(out: ScriptOutput) -> None:
    header("Case 6: Failure controls")
    print("The active-O problem ledger fails if a later script allows:")
    print()
    print("1. O used by name")
    print("2. O used as magic eraser")
    print("3. O selected from recovery")
    print("4. O selected from boundary/source/support failure")
    print("5. O acts without domain/codomain")
    print("6. O acts without kernel/image")
    print("7. O acts without no-overlap criterion")
    print("8. O acts without divergence behavior")
    print("9. O licenses B_s/F_zeta insertion")
    print("10. O opens parent equation")

    with out.governance_assessments():
        out.line(
            "active-O problem ledger failure controls stated",
            StatusMark.OBLIGATION,
            "future scripts must construct O rather than invoking it",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Active-O construction opening result:")
    print()
    print("  O construction target is explicit.")
    print("  O must define domain, codomain, kernel, image, no-overlap criterion, algebraic law, divergence behavior, boundary/source/mass/current/support behavior, recovery independence, insertion separation, and parent-gate closure.")
    print("  O must preserve zeta_to_Bs as the safe trace target.")
    print("  O must not hide zeta/kappa residuals in accounting variables.")
    print("  O must not be selected from recovery or boundary/source failure.")
    print("  O must not license insertion or parent closure.")
    print("  O is not derived by this script.")
    print()
    print("Possible next script:")
    print("  candidate_O_domain_codomain.py")
    print()
    print("Tiny goblin label:")
    print("  Do not wave the wand. Forge the tool.")

    with out.governance_assessments():
        out.line(
            "active-O problem ledger complete",
            StatusMark.PASS,
            "active-O construction burden stated; O remains not derived",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, symbols: OProblemSymbols) -> None:
    ns.record_derivation(
        derivation_id="g27_O_problem",
        inputs=[
            symbols.domain_gap,
            symbols.codomain_gap,
            symbols.kernel_gap,
            symbols.image_gap,
            symbols.pairing_gap,
            symbols.law_gap,
            symbols.div_gap,
            symbols.boundary_gap,
            symbols.source_gap,
            symbols.mass_gap,
            symbols.current_gap,
            symbols.support_gap,
            symbols.recovery_gap,
            symbols.insertion_gap,
            symbols.parent_gap,
        ],
        output=symbols.O_burden,
        method="state active-O construction burden as open operator gaps",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="O_problem_marker",
        scope="Group 27 active O construction",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g27_O_domain", "Define O domain"),
        ("g27_O_codomain", "Define O codomain"),
        ("g27_O_kernel", "Define O kernel"),
        ("g27_O_image", "Define O image"),
        ("g27_O_pairing", "Define no-overlap pairing or criterion"),
        ("g27_O_law", "Define projection/replacement/constraint law"),
        ("g27_O_div", "Derive O divergence behavior"),
        ("g27_O_boundary", "Derive O boundary/source/mass behavior"),
        ("g27_O_recovery", "Derive O recovery independence"),
        ("g27_O_no_downstream", "Keep insertion and parent gates closed"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g27_O_route"],
            description=(
                "Active O is not derived here. This obligation must be closed before O can be used as an operator."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g27_O_domain",
        "g27_O_codomain",
        "g27_O_kernel",
        "g27_O_image",
        "g27_O_pairing",
        "g27_O_law",
        "g27_O_div",
        "g27_O_boundary",
        "g27_O_recovery",
        "g27_O_no_downstream",
    ]

    ns.record_route(RouteRecord(
        route_id="g27_O_route",
        script_id=SCRIPT_ID,
        name="Group 27 active-O construction route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "O is treated as construction target, not tool",
            "domain, codomain, kernel, image, no-overlap criterion, algebraic law, divergence behavior, boundary/source behavior, and recovery independence remain open",
            "recovery and boundary/source failure do not select O",
            "insertion and parent gates remain closed",
        ],
    ))

    for branch_id in [
        "O_by_name",
        "O_magic_eraser",
        "O_recovery_selected",
        "O_repair_selected",
        "O_accounting_reservoir",
        "O_assumes_domain_codomain",
        "O_assumes_kernel_image",
        "O_assumes_pairing",
        "O_licenses_insertion",
        "O_opens_parent",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; active O must be constructed rather than invoked.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g27_O_problem_not_derived",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Active O construction target is explicit, but O is not derived. O must define domain, codomain, kernel, image, no-overlap criterion, "
            "algebraic law, divergence behavior, boundary/source/mass/current/support behavior, recovery independence, insertion separation, and parent-gate closure. "
            "O by name, magic eraser O, recovery-selected O, repair-selected O, insertion licensing, and parent opening are rejected."
        ),
        derivation_ids=["g27_O_problem"],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate O Problem Ledger")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    tasks = build_tasks()
    guardrails = build_guardrails()
    forbidden = build_forbidden_uses()
    boundaries = build_boundaries()

    case_0_problem_statement(out)
    case_1_symbol_ledger(symbols, out)
    case_2_tasks(tasks, out)
    case_3_guardrails(guardrails, out)
    case_4_forbidden_uses(forbidden, out)
    case_5_boundaries(boundaries, out)
    case_6_failure_controls(out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns, symbols)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
