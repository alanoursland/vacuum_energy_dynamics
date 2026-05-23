# Candidate O kernel image
#
# Group:
#   27_active_O_construction
#
# Script type:
#   OPERATOR STRUCTURE INVENTORY
#
# Purpose
# -------
# Test candidate kernel and image assignments for active O.
#
# Locked-door question:
#
#   What belongs in ker(O), and what belongs in im(O)?
#
# This script does not derive active O.
# It does not derive the no-overlap criterion.
# It does not prove O is a projection.
# It does not derive residual control.
# It does not derive B_s/F_zeta insertion.
# It does not open parent equation closure.
#
# Tiny goblin rule:
#
#   Do not call the pit a kernel until you know what falls in.

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
        "FORBIDDEN": StatusMark.FAIL,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "PARTIAL": StatusMark.INFO,
        "PRESERVE": StatusMark.OBLIGATION,
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
class KernelImageSymbols:
    zeta_Bs: sp.Symbol
    zeta_res: sp.Symbol
    kappa_res: sp.Symbol
    eps_acc: sp.Symbol
    ekappa_acc: sp.Symbol
    safe_trace: sp.Symbol
    inert_residual: sp.Symbol
    diagnostic_account: sp.Symbol
    projected_out: sp.Symbol
    kernel_gap: sp.Symbol
    image_gap: sp.Symbol
    pairing_gap: sp.Symbol
    ki_gap: sp.Expr
    ker_candidate: sp.Tuple
    im_candidate: sp.Tuple


@dataclass
class KernelCandidate:
    name: str
    candidate: str
    status: str
    allowed_if: str
    hazard: str


@dataclass
class ImageCandidate:
    name: str
    candidate: str
    status: str
    allowed_if: str
    hazard: str


@dataclass
class KernelImageAssignment:
    name: str
    assignment: str
    status: str
    works_if: str
    fails_if: str


@dataclass
class RejectedKernelImageShortcut:
    name: str
    shortcut: str
    status: str
    reason: str


@dataclass
class KernelImageConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


# =============================================================================
# Builders
# =============================================================================


def build_symbols() -> KernelImageSymbols:
    (
        zeta_Bs,
        zeta_res,
        kappa_res,
        eps_acc,
        ekappa_acc,
        safe_trace,
        inert_residual,
        diagnostic_account,
        projected_out,
        kernel_gap,
        image_gap,
        pairing_gap,
    ) = sp.symbols(
        "zeta_Bs zeta_res kappa_res eps_acc ekappa_acc safe_trace inert_residual diagnostic_account projected_out "
        "kernel_gap image_gap pairing_gap",
        real=True,
    )

    ker_candidate = sp.Tuple(zeta_res, kappa_res)
    im_candidate = sp.Tuple(safe_trace, inert_residual, diagnostic_account, projected_out)
    ki_gap = sp.simplify(kernel_gap + image_gap + pairing_gap)

    return KernelImageSymbols(
        zeta_Bs=zeta_Bs,
        zeta_res=zeta_res,
        kappa_res=kappa_res,
        eps_acc=eps_acc,
        ekappa_acc=ekappa_acc,
        safe_trace=safe_trace,
        inert_residual=inert_residual,
        diagnostic_account=diagnostic_account,
        projected_out=projected_out,
        kernel_gap=kernel_gap,
        image_gap=image_gap,
        pairing_gap=pairing_gap,
        ki_gap=ki_gap,
        ker_candidate=ker_candidate,
        im_candidate=im_candidate,
    )


def build_kernel_candidates() -> List[KernelCandidate]:
    return [
        KernelCandidate(
            name="K1: zeta residual in kernel",
            candidate="zeta_residual_metric in ker(O)",
            status="CANDIDATE",
            allowed_if="a structural no-overlap law sends zeta residual metric trace to zero/projected-out role",
            hazard="zeta residual is killed by declaration",
        ),
        KernelCandidate(
            name="K2: kappa residual in kernel",
            candidate="kappa_metric in ker(O)",
            status="CANDIDATE",
            allowed_if="a structural law prevents kappa from restoring zeta trace/source role",
            hazard="kappa is killed by diagnostic vocabulary",
        ),
        KernelCandidate(
            name="K3: accounting pair in kernel",
            candidate="epsilon_vac_metric and e_kappa_metric in ker(O)",
            status="UNDERDETERMINED",
            allowed_if="accounting variables are proven no-role and not needed in image",
            hazard="accounting pair hides residual geometry or source load",
        ),
        KernelCandidate(
            name="K4: boundary/source/support data in kernel",
            candidate="boundary/source/support data in ker(O)",
            status="REJECTED",
            allowed_if="not allowed as a blanket rule",
            hazard="O erases guardrail data and hides boundary/source/support failure",
        ),
        KernelCandidate(
            name="K5: zeta_Bs in kernel",
            candidate="zeta_Bs in ker(O)",
            status="REJECTED",
            allowed_if="not allowed if zeta_to_Bs is the safe trace target",
            hazard="O kills the safe scalar trace channel",
        ),
    ]


def build_image_candidates() -> List[ImageCandidate]:
    return [
        ImageCandidate(
            name="I1: safe trace in image",
            candidate="safe_trace_sector in im(O)",
            status="ADMISSIBLE_CANDIDATE",
            allowed_if="O preserves zeta_to_Bs as safe ordinary scalar trace",
            hazard="residuals also enter safe trace sector",
        ),
        ImageCandidate(
            name="I2: inert residual sector in image",
            candidate="inert_residual_sector in im(O)",
            status="UNDERDETERMINED",
            allowed_if="inert sector is derived as no metric/source/boundary/support/recovery/parent role",
            hazard="inert sector exists by label only",
        ),
        ImageCandidate(
            name="I3: diagnostic/accounting sector in image",
            candidate="diagnostic_account_sector in im(O)",
            status="UNDERDETERMINED",
            allowed_if="diagnostic/accounting sector is proven non-constructive",
            hazard="diagnostic output becomes construction data later",
        ),
        ImageCandidate(
            name="I4: projected-out remainder in image",
            candidate="projected_out_sector in im(O)",
            status="UNDERDETERMINED",
            allowed_if="projected-out sector is part of a defined replacement/projection law",
            hazard="projected-out means erased by name",
        ),
        ImageCandidate(
            name="I5: parent equation sector in image",
            candidate="parent field-equation sector in im(O)",
            status="REJECTED",
            allowed_if="not allowed in this group",
            hazard="O image opens parent equation",
        ),
    ]


def build_assignments() -> List[KernelImageAssignment]:
    return [
        KernelImageAssignment(
            name="A1: preserve safe trace",
            assignment="zeta_Bs in im(O), not ker(O)",
            status="CANDIDATE",
            works_if="O(zeta_Bs) preserves safe trace without duplication",
            fails_if="O kills or modifies zeta_Bs",
        ),
        KernelImageAssignment(
            name="A2: zeta residual kernel candidate",
            assignment="zeta_residual_metric in ker(O) or mapped to inert/projected sector",
            status="UNDERDETERMINED",
            works_if="kernel/image law and no-overlap criterion are derived",
            fails_if="zeta residual is simply named zero",
        ),
        KernelImageAssignment(
            name="A3: kappa residual kernel candidate",
            assignment="kappa_metric in ker(O) or mapped to inert/diagnostic/projected sector",
            status="UNDERDETERMINED",
            works_if="kappa no-reentry or diagnostic-sector law is derived",
            fails_if="kappa is made harmless by vocabulary",
        ),
        KernelImageAssignment(
            name="A4: accounting pair assignment",
            assignment="epsilon/e_kappa in diagnostic/accounting image or excluded from O action",
            status="UNDERDETERMINED",
            works_if="accounting sector cannot carry metric/source/support/recovery/parent roles",
            fails_if="accounting variables repair zeta/kappa geometry",
        ),
        KernelImageAssignment(
            name="A5: guardrail data preservation",
            assignment="boundary/source/support data not erased by kernel assignment",
            status="REQUIRED",
            works_if="guardrail data remains available for compatibility audit",
            fails_if="O kernel hides boundary/source/support failure",
        ),
        KernelImageAssignment(
            name="A6: parent image exclusion",
            assignment="parent readiness not in im(O)",
            status="REJECTED",
            works_if="not applicable",
            fails_if="O image is treated as parent closure",
        ),
    ]


def build_shortcuts() -> List[RejectedKernelImageShortcut]:
    return [
        RejectedKernelImageShortcut(
            name="S1: kernel by naming",
            shortcut="declare residuals are in ker(O)",
            status="REJECTED",
            reason="kernel membership must follow from an operator law",
        ),
        RejectedKernelImageShortcut(
            name="S2: image by naming",
            shortcut="declare O output is safe because it is in im(O)",
            status="REJECTED",
            reason="image safety must be derived",
        ),
        RejectedKernelImageShortcut(
            name="S3: zeta_Bs killed",
            shortcut="put zeta_Bs in kernel",
            status="REJECTED",
            reason="zeta_to_Bs is the safe scalar trace target",
        ),
        RejectedKernelImageShortcut(
            name="S4: boundary/source data killed",
            shortcut="put boundary/source/support failures in kernel",
            status="REJECTED",
            reason="O cannot hide guardrail failure",
        ),
        RejectedKernelImageShortcut(
            name="S5: accounting image as reservoir",
            shortcut="send residuals to accounting image that carries metric/source load",
            status="REJECTED",
            reason="accounting cannot repair geometry",
        ),
        RejectedKernelImageShortcut(
            name="S6: parent image",
            shortcut="put parent readiness in im(O)",
            status="REJECTED",
            reason="parent gate remains closed",
        ),
    ]


def build_conclusions() -> List[KernelImageConclusion]:
    return [
        KernelImageConclusion(
            name="C1: safe trace image",
            conclusion="zeta_Bs belongs in the preserved image candidate, not the kernel",
            status="CANDIDATE",
            meaning="safe trace preservation remains the cleanest image target",
        ),
        KernelImageConclusion(
            name="C2: zeta/kappa kernel",
            conclusion="zeta/kappa residual kernel membership is underdetermined",
            status="UNDERDETERMINED",
            meaning="kernel membership requires no-overlap criterion and operator law",
        ),
        KernelImageConclusion(
            name="C3: accounting assignment",
            conclusion="accounting pair assignment is underdetermined",
            status="UNDERDETERMINED",
            meaning="accounting cannot become residual reservoir",
        ),
        KernelImageConclusion(
            name="C4: guardrail data",
            conclusion="boundary/source/support data cannot be erased by kernel assignment",
            status="REQUIRED",
            meaning="O must preserve guardrail auditability",
        ),
        KernelImageConclusion(
            name="C5: next route",
            conclusion="derive no-overlap pairing/criterion before claiming kernel/image closure",
            status="OPEN",
            meaning="kernel/image inventory points to missing no-overlap mathematics",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: O kernel/image problem")
    print("Question:")
    print()
    print("  What belongs in ker(O), and what belongs in im(O)?")
    print()
    print("Reference discipline:")
    print()
    print("  Kernel membership is not a synonym for erased by name.")
    print("  Image membership is not a synonym for safe by label.")
    print("  Kernel/image classification requires a no-overlap criterion and operator law.")

    with out.governance_assessments():
        out.line(
            "O kernel/image inventory opened",
            StatusMark.INFO,
            "testing candidate kernel and image assignments without deriving O",
        )


def case_1_symbol_ledger(symbols: KernelImageSymbols, out: ScriptOutput) -> None:
    header("Case 1: Candidate kernel/image symbolic ledger")
    print("Candidate kernel:")
    print()
    print(f"  ker_candidate = {sp.sstr(symbols.ker_candidate)}")
    print()
    print("Candidate image:")
    print()
    print(f"  im_candidate = {sp.sstr(symbols.im_candidate)}")
    print()
    print("Kernel/image/pairing gap:")
    print()
    print(f"  L_kernel_image_gap = {sp.sstr(symbols.ki_gap)}")
    print()
    print("Interpretation:")
    print()
    print("  Kernel and image remain candidates.")
    print("  Pairing/no-overlap criterion is required before kernel/image can close.")

    with out.derived_results():
        out.line(
            "O kernel/image candidate ledger stated",
            StatusMark.OBLIGATION,
            f"ker_candidate = {sp.sstr(symbols.ker_candidate)} ; im_candidate = {sp.sstr(symbols.im_candidate)}",
        )


def case_2_kernel_candidates(items: List[KernelCandidate], out: ScriptOutput) -> None:
    header("Case 2: Candidate kernel entries")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Candidate: {item.candidate}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Allowed if: {item.allowed_if}")
        print(f"Hazard: {item.hazard}")

    with out.governance_assessments():
        out.line(
            "O kernel candidates classified",
            StatusMark.PASS,
            f"{len(items)} kernel candidates classified",
        )


def case_3_image_candidates(items: List[ImageCandidate], out: ScriptOutput) -> None:
    header("Case 3: Candidate image entries")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Candidate: {item.candidate}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Allowed if: {item.allowed_if}")
        print(f"Hazard: {item.hazard}")

    with out.governance_assessments():
        out.line(
            "O image candidates classified",
            StatusMark.PASS,
            f"{len(items)} image candidates classified",
        )


def case_4_assignments(items: List[KernelImageAssignment], out: ScriptOutput) -> None:
    header("Case 4: Candidate kernel/image assignments")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Assignment: {item.assignment}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Works if: {item.works_if}")
        print(f"Fails if: {item.fails_if}")

    with out.unresolved_obligations():
        out.line(
            "O kernel/image assignments classified",
            StatusMark.OBLIGATION,
            "safe trace image candidate exists; residual kernel/image assignments remain underdetermined",
        )


def case_5_shortcuts(items: List[RejectedKernelImageShortcut], out: ScriptOutput) -> None:
    header("Case 5: Rejected kernel/image shortcuts")
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
            "O kernel/image shortcuts rejected",
            StatusMark.FAIL,
            "kernel by naming, image by naming, zeta_Bs killed, guardrail data killed, accounting reservoir, and parent image are rejected",
        )


def case_6_conclusions(items: List[KernelImageConclusion], out: ScriptOutput) -> None:
    header("Case 6: Kernel/image conclusions")
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
            "O kernel/image conclusion stated",
            StatusMark.DEFER,
            "kernel/image remain underdetermined pending no-overlap pairing/criterion",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("O kernel/image result:")
    print()
    print("  zeta_Bs belongs in the preserved image candidate, not the kernel.")
    print("  zeta_residual_metric and kappa_metric are plausible kernel or inert/projected candidates, but membership is underdetermined.")
    print("  accounting pair assignment remains underdetermined and cannot hide geometry.")
    print("  boundary/source/support data cannot be erased.")
    print("  parent readiness is rejected as image.")
    print("  Kernel/image closure requires a no-overlap pairing/criterion and operator law.")
    print("  O is not derived by this script.")
    print()
    print("Possible next script:")
    print("  candidate_O_no_overlap_pairing.py")
    print()
    print("Tiny goblin label:")
    print("  Do not call the pit a kernel until you know what falls in.")

    with out.governance_assessments():
        out.line(
            "O kernel/image inventory complete",
            StatusMark.PASS,
            "kernel/image candidates classified; no-overlap pairing remains next",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, symbols: KernelImageSymbols) -> None:
    ns.record_derivation(
        derivation_id="g27_O_kernel_image",
        inputs=[
            symbols.zeta_Bs,
            symbols.zeta_res,
            symbols.kappa_res,
            symbols.eps_acc,
            symbols.ekappa_acc,
            symbols.pairing_gap,
        ],
        output=sp.Tuple(symbols.ker_candidate, symbols.im_candidate, symbols.ki_gap),
        method="state candidate active-O kernel and image inventories with pairing gap",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="O_kernel_image_marker",
        scope="Group 27 active O construction",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g27_ki_preserve_zeta", "Keep zeta_Bs out of kernel and in safe image candidate"),
        ("g27_ki_zeta_res", "Define zeta residual kernel/image status"),
        ("g27_ki_kappa_res", "Define kappa residual kernel/image status"),
        ("g27_ki_accounting", "Define accounting pair assignment without hidden reservoir"),
        ("g27_ki_guardrails", "Do not erase boundary/source/support data"),
        ("g27_ki_pairing", "Derive no-overlap pairing/criterion"),
        ("g27_ki_no_parent", "Exclude parent readiness from image"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g27_ki_route"],
            description=(
                "O kernel/image candidates are inventoried here, but O is not derived. No-overlap criterion and operator law remain open."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g27_ki_preserve_zeta",
        "g27_ki_zeta_res",
        "g27_ki_kappa_res",
        "g27_ki_accounting",
        "g27_ki_guardrails",
        "g27_ki_pairing",
        "g27_ki_no_parent",
    ]

    ns.record_route(RouteRecord(
        route_id="g27_ki_route",
        script_id=SCRIPT_ID,
        name="Group 27 O kernel/image route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "zeta_Bs is preserved in image candidate and not killed",
            "zeta/kappa kernel membership is not by naming",
            "accounting image is not hidden reservoir",
            "guardrail data is not erased",
            "parent readiness is not image",
            "no-overlap pairing remains next",
        ],
    ))

    for branch_id in [
        "kernel_by_naming",
        "image_safe_by_label",
        "zeta_Bs_in_kernel",
        "guardrail_data_in_kernel",
        "accounting_image_reservoir",
        "parent_in_image",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; O kernel/image must be constructed, not assumed.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g27_ki_not_operator",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Candidate active-O kernel/image assignments are inventoried. zeta_Bs belongs in the preserved image candidate, not the kernel. "
            "zeta/kappa residual kernel/image status and accounting assignment remain underdetermined pending no-overlap criterion and operator law. "
            "Boundary/source/support data cannot be erased, parent readiness is rejected as image, and this does not derive O."
        ),
        derivation_ids=["g27_O_kernel_image"],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate O Kernel Image")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    kernels = build_kernel_candidates()
    images = build_image_candidates()
    assignments = build_assignments()
    shortcuts = build_shortcuts()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_symbol_ledger(symbols, out)
    case_2_kernel_candidates(kernels, out)
    case_3_image_candidates(images, out)
    case_4_assignments(assignments, out)
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
