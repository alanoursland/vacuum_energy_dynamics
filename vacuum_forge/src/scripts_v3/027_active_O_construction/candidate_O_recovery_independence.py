# Candidate O recovery independence
#
# Group:
#   27_active_O_construction
#
# Script type:
#   RECOVERY-INDEPENDENCE AUDIT
#
# Purpose
# -------
# Audit whether candidate active O can be defined without being selected from
# weak-field, Schwarzschild, AB=1, B=1/A, gamma, PPN, areal-kappa, or parent-fit
# recovery targets.
#
# Locked-door question:
#
#   Can O be defined without being selected from recovery?
#
# This script does not derive active O.
# It does not derive residual control.
# It does not derive B_s/F_zeta insertion.
# It does not derive parent equation closure.
#
# Tiny goblin rule:
#
#   The lock may fit the key, but the lock did not forge the key.

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
        "AUDIT_ONLY": StatusMark.INFO,
        "BLOCKED": StatusMark.FAIL,
        "CANDIDATE": StatusMark.DEFER,
        "CONDITIONALLY_SAFE": StatusMark.INFO,
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
        ("g27_O_problem", "027_active_O_construction__candidate_O_problem_ledger", "g27_O_problem", RecordKind.INVENTORY_MARKER),
        ("g27_dc", "027_active_O_construction__candidate_O_domain_codomain", "g27_O_domain_codomain", RecordKind.INVENTORY_MARKER),
        ("g27_ki", "027_active_O_construction__candidate_O_kernel_image", "g27_O_kernel_image", RecordKind.INVENTORY_MARKER),
        ("g27_pair", "027_active_O_construction__candidate_O_no_overlap_pairing", "g27_O_pairing", RecordKind.INVENTORY_MARKER),
        ("g27_alg", "027_active_O_construction__candidate_O_projection_law", "g27_O_alg_law", RecordKind.INVENTORY_MARKER),
        ("g27_div", "027_active_O_construction__candidate_O_divergence_commutation", "g27_O_divergence", RecordKind.INVENTORY_MARKER),
        ("g27_bsm", "027_active_O_construction__candidate_O_boundary_source_mass", "g27_O_bsm", RecordKind.INVENTORY_MARKER),
        ("g26_summary", "026_residual_control_theorem_attempt__candidate_group_26_status_summary", "g26_status_summary", RecordKind.INVENTORY_MARKER),
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
    for attr in ("routes_path", "branch_decisions_path", "claims_path", "obligations_path", "derivations_path", "governance_path"):
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
class RecoverySymbols:
    O: sp.Symbol
    AB1: sp.Symbol
    BinvA: sp.Symbol
    Schw: sp.Symbol
    gamma: sp.Symbol
    PPN: sp.Symbol
    kappa0: sp.Symbol
    weak: sp.Symbol
    parent_fit: sp.Symbol
    recovery_gap: sp.Symbol
    weak_gap: sp.Symbol
    schwarz_gap: sp.Symbol
    gamma_gap: sp.Symbol
    kappa_gap: sp.Symbol
    parent_fit_gap: sp.Symbol
    recovery_selection_load: sp.Expr


@dataclass
class RecoveryTarget:
    name: str
    target: str
    status: str
    allowed_as: str
    forbidden_as: str


@dataclass
class RecoveryTest:
    name: str
    test: str
    status: str
    result: str
    implication: str


@dataclass
class RecoveryRequirement:
    name: str
    requirement: str
    status: str
    required_for: str
    fails_if: str


@dataclass
class RejectedRecoveryShortcut:
    name: str
    shortcut: str
    status: str
    reason: str


@dataclass
class RecoveryConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_symbols() -> RecoverySymbols:
    (
        O,
        AB1,
        BinvA,
        Schw,
        gamma,
        PPN,
        kappa0,
        weak,
        parent_fit,
        recovery_gap,
        weak_gap,
        schwarz_gap,
        gamma_gap,
        kappa_gap,
        parent_fit_gap,
    ) = sp.symbols(
        "O AB1 BinvA Schw gamma PPN kappa0 weak parent_fit "
        "recovery_gap weak_gap schwarz_gap gamma_gap kappa_gap parent_fit_gap",
        real=True,
    )

    recovery_selection_load = sp.simplify(
        recovery_gap + weak_gap + schwarz_gap + gamma_gap + kappa_gap + parent_fit_gap
    )

    return RecoverySymbols(
        O=O,
        AB1=AB1,
        BinvA=BinvA,
        Schw=Schw,
        gamma=gamma,
        PPN=PPN,
        kappa0=kappa0,
        weak=weak,
        parent_fit=parent_fit,
        recovery_gap=recovery_gap,
        weak_gap=weak_gap,
        schwarz_gap=schwarz_gap,
        gamma_gap=gamma_gap,
        kappa_gap=kappa_gap,
        parent_fit_gap=parent_fit_gap,
        recovery_selection_load=recovery_selection_load,
    )


def build_targets() -> List[RecoveryTarget]:
    return [
        RecoveryTarget(
            name="R1: AB=1",
            target="AB = 1 exterior compensation",
            status="AUDIT_ONLY",
            allowed_as="downstream recovery check",
            forbidden_as="definition or selector for O",
        ),
        RecoveryTarget(
            name="R2: B=1/A",
            target="reciprocal spatial factor",
            status="AUDIT_ONLY",
            allowed_as="downstream weak/static exterior check",
            forbidden_as="operator selection rule",
        ),
        RecoveryTarget(
            name="R3: Schwarzschild exterior",
            target="Schwarzschild-like exterior recovery",
            status="AUDIT_ONLY",
            allowed_as="downstream solution audit",
            forbidden_as="reason O exists or has its law",
        ),
        RecoveryTarget(
            name="R4: gamma / PPN",
            target="gamma_like or PPN gamma = 1",
            status="AUDIT_ONLY",
            allowed_as="phenomenological audit",
            forbidden_as="criterion defining no-overlap",
        ),
        RecoveryTarget(
            name="R5: areal kappa = 0",
            target="areal/static exterior kappa suppression",
            status="AUDIT_ONLY",
            allowed_as="recovery check after O construction",
            forbidden_as="kernel/image or divergence selector",
        ),
        RecoveryTarget(
            name="R6: parent-fit closure",
            target="parent equation fit or closure",
            status="REJECTED",
            allowed_as="not allowed in this group",
            forbidden_as="operator construction target",
        ),
    ]


def build_tests() -> List[RecoveryTest]:
    return [
        RecoveryTest(
            name="T1: recovery can audit O",
            test="can recovery be used after O construction to check consequences?",
            status="CONDITIONALLY_SAFE",
            result="yes; recovery may audit a previously constructed O",
            implication="recovery checks remain useful downstream",
        ),
        RecoveryTest(
            name="T2: recovery can select O",
            test="can recovery targets choose O domain/codomain/kernel/image/law?",
            status="REJECTED",
            result="no; this would smuggle recovery into construction",
            implication="O must be defined structurally",
        ),
        RecoveryTest(
            name="T3: AB=1 selects O",
            test="can AB=1 be used to choose O?",
            status="REJECTED",
            result="no; AB=1 is recovery/compensation behavior, not operator definition",
            implication="exterior compensation cannot construct O",
        ),
        RecoveryTest(
            name="T4: Schwarzschild/gamma selects O",
            test="can Schwarzschild or gamma recovery choose O?",
            status="REJECTED",
            result="no; observational fit cannot choose the theorem object",
            implication="O must remain recovery-independent",
        ),
        RecoveryTest(
            name="T5: parent fit selects O",
            test="can parent-fit closure choose O?",
            status="REJECTED",
            result="no; parent equation remains closed",
            implication="O construction cannot be parent-fit driven",
        ),
        RecoveryTest(
            name="T6: recovery independence derived",
            test="is O recovery independence fully derived here?",
            status="NOT_DERIVED",
            result="no; this audit rejects recovery selection but does not derive O",
            implication="construction obstruction summary remains needed",
        ),
    ]


def build_requirements() -> List[RecoveryRequirement]:
    return [
        RecoveryRequirement(
            name="Q1: structural definition first",
            requirement="O domain/codomain/kernel/image/law must be defined before recovery audit",
            status="REQUIRED",
            required_for="recovery independence",
            fails_if="recovery chooses operator structure",
        ),
        RecoveryRequirement(
            name="Q2: weak-field audit only",
            requirement="weak-field, AB=1, and B=1/A are downstream audits only",
            status="REQUIRED",
            required_for="weak-field anti-smuggling",
            fails_if="weak-field recovery selects O",
        ),
        RecoveryRequirement(
            name="Q3: Schwarzschild/gamma audit only",
            requirement="Schwarzschild, gamma, and PPN may test but not define O",
            status="REQUIRED",
            required_for="observational anti-smuggling",
            fails_if="phenomenology constructs O",
        ),
        RecoveryRequirement(
            name="Q4: kappa recovery audit only",
            requirement="areal kappa suppression cannot choose residual action",
            status="REQUIRED",
            required_for="kappa discipline",
            fails_if="kappa=0 recovery selects kernel/image",
        ),
        RecoveryRequirement(
            name="Q5: no parent fit",
            requirement="parent-fit closure cannot choose O",
            status="REQUIRED",
            required_for="parent-gate closure",
            fails_if="parent readiness selects O",
        ),
        RecoveryRequirement(
            name="Q6: no insertion license",
            requirement="recovery independence audit does not license B_s/F_zeta insertion",
            status="REQUIRED",
            required_for="insertion separation",
            fails_if="recovery success becomes insertion law",
        ),
    ]


def build_shortcuts() -> List[RejectedRecoveryShortcut]:
    return [
        RejectedRecoveryShortcut(
            name="S1: AB=1 selected O",
            shortcut="choose O because it makes AB=1 work",
            status="REJECTED",
            reason="AB=1 may be recovered or audited, but cannot construct O",
        ),
        RejectedRecoveryShortcut(
            name="S2: Schwarzschild selected O",
            shortcut="choose O because it recovers Schwarzschild exterior",
            status="REJECTED",
            reason="Schwarzschild recovery is downstream audit",
        ),
        RejectedRecoveryShortcut(
            name="S3: gamma selected O",
            shortcut="choose O because gamma or PPN works",
            status="REJECTED",
            reason="observational success cannot define operator structure",
        ),
        RejectedRecoveryShortcut(
            name="S4: kappa=0 selected O",
            shortcut="choose O because exterior kappa should vanish",
            status="REJECTED",
            reason="kappa recovery target cannot choose kernel/image",
        ),
        RejectedRecoveryShortcut(
            name="S5: weak-field selected O",
            shortcut="choose O from weak-field fit",
            status="REJECTED",
            reason="weak-field recovery is not field-equation derivation",
        ),
        RejectedRecoveryShortcut(
            name="S6: parent-fit selected O",
            shortcut="choose O to make parent equation close",
            status="REJECTED",
            reason="parent gate remains closed",
        ),
        RejectedRecoveryShortcut(
            name="S7: recovery licenses insertion",
            shortcut="use recovery success as B_s/F_zeta insertion law",
            status="REJECTED",
            reason="insertion law remains separate",
        ),
    ]


def build_conclusions() -> List[RecoveryConclusion]:
    return [
        RecoveryConclusion(
            name="C1: recovery as audit",
            conclusion="recovery may audit a constructed O",
            status="CONDITIONALLY_SAFE",
            meaning="recovery remains useful after construction",
        ),
        RecoveryConclusion(
            name="C2: recovery as construction",
            conclusion="recovery may not select O",
            status="REJECTED",
            meaning="O must be structurally defined",
        ),
        RecoveryConclusion(
            name="C3: weak-field / AB=1",
            conclusion="AB=1, B=1/A, and weak-field success cannot define O",
            status="REJECTED",
            meaning="field-equation construction remains distinct from recovery",
        ),
        RecoveryConclusion(
            name="C4: parent/insertion",
            conclusion="recovery independence does not license insertion or parent closure",
            status="REQUIRED",
            meaning="downstream gates remain closed",
        ),
        RecoveryConclusion(
            name="C5: next route",
            conclusion="construction obstruction summary is now ready",
            status="OPEN",
            meaning="all major O burden ledgers have been audited enough to summarize construction status",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: O recovery-independence problem")
    print("Question:")
    print()
    print("  Can O be defined without being selected from recovery?")
    print()
    print("Reference discipline:")
    print()
    print("  Recovery may audit O after construction.")
    print("  Recovery may not define O, choose O, or license insertion/parent closure.")

    with out.governance_assessments():
        out.line(
            "O recovery-independence audit opened",
            StatusMark.INFO,
            "testing whether recovery targets are only audits and not operator selectors",
        )


def case_1_symbol_ledger(symbols: RecoverySymbols, out: ScriptOutput) -> None:
    header("Case 1: Recovery-selection symbolic ledger")
    print("Recovery target symbols:")
    print()
    print(f"  AB1        = {sp.sstr(symbols.AB1)}")
    print(f"  BinvA      = {sp.sstr(symbols.BinvA)}")
    print(f"  Schw       = {sp.sstr(symbols.Schw)}")
    print(f"  gamma      = {sp.sstr(symbols.gamma)}")
    print(f"  PPN        = {sp.sstr(symbols.PPN)}")
    print(f"  kappa0     = {sp.sstr(symbols.kappa0)}")
    print(f"  weak       = {sp.sstr(symbols.weak)}")
    print(f"  parent_fit = {sp.sstr(symbols.parent_fit)}")
    print()
    print("Recovery-selection load:")
    print()
    print(f"  L_O_recovery_select = {sp.sstr(symbols.recovery_selection_load)}")

    with out.derived_results():
        out.line(
            "O recovery-selection load stated",
            StatusMark.OBLIGATION,
            f"L_O_recovery_select = {sp.sstr(symbols.recovery_selection_load)}",
        )


def case_2_targets(items: List[RecoveryTarget], out: ScriptOutput) -> None:
    header("Case 2: Recovery targets")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Target: {item.target}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Allowed as: {item.allowed_as}")
        print(f"Forbidden as: {item.forbidden_as}")

    with out.governance_assessments():
        out.line(
            "O recovery targets classified",
            StatusMark.PASS,
            f"{len(items)} recovery targets classified as audit-only or rejected",
        )


def case_3_tests(items: List[RecoveryTest], out: ScriptOutput) -> None:
    header("Case 3: Recovery-independence tests")
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
            "O recovery-independence tests completed",
            StatusMark.PASS,
            "recovery selection rejected; recovery audit remains conditionally safe",
        )


def case_4_requirements(items: List[RecoveryRequirement], out: ScriptOutput) -> None:
    header("Case 4: Recovery-independence requirements")
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
            "O recovery-independence requirements stated",
            StatusMark.OBLIGATION,
            f"{len(items)} recovery-independence requirements remain active",
        )


def case_5_shortcuts(items: List[RejectedRecoveryShortcut], out: ScriptOutput) -> None:
    header("Case 5: Rejected recovery shortcuts")
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
            "O recovery shortcuts rejected",
            StatusMark.FAIL,
            "AB=1, Schwarzschild, gamma/PPN, kappa=0, weak-field, parent-fit, and insertion shortcuts are rejected",
        )


def case_6_conclusions(items: List[RecoveryConclusion], out: ScriptOutput) -> None:
    header("Case 6: Recovery-independence conclusions")
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
            "O recovery-independence conclusion stated",
            StatusMark.PASS,
            "recovery selection rejected; construction obstruction summary is next",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("O recovery-independence result:")
    print()
    print("  Recovery may audit a constructed O.")
    print("  Recovery may not select O.")
    print("  AB=1, B=1/A, Schwarzschild, gamma, PPN, weak-field success, and kappa=0 cannot define O.")
    print("  Parent-fit closure cannot define O.")
    print("  Recovery independence does not license insertion or parent closure.")
    print("  This audit does not derive O.")
    print("  Construction obstruction summary is now ready.")
    print()
    print("Possible next script:")
    print("  candidate_O_construction_obstruction.py")
    print()
    print("Tiny goblin label:")
    print("  The lock may fit the key, but the lock did not forge the key.")

    with out.governance_assessments():
        out.line(
            "O recovery-independence audit complete",
            StatusMark.PASS,
            "recovery selection rejected; O remains not derived",
        )


def record_derivations(ns, symbols: RecoverySymbols) -> None:
    ns.record_derivation(
        derivation_id="g27_O_recovery",
        inputs=[
            symbols.recovery_gap,
            symbols.weak_gap,
            symbols.schwarz_gap,
            symbols.gamma_gap,
            symbols.kappa_gap,
            symbols.parent_fit_gap,
        ],
        output=symbols.recovery_selection_load,
        method="state active-O recovery-selection load and reject recovery-selected O",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="O_recovery_marker",
        scope="Group 27 active O construction",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g27_rec_struct_first", "Define O structurally before recovery audit"),
        ("g27_rec_weak_audit", "Keep weak-field/AB=1/B=1/A audit-only"),
        ("g27_rec_schw_audit", "Keep Schwarzschild/gamma/PPN audit-only"),
        ("g27_rec_kappa_audit", "Keep kappa=0 audit-only"),
        ("g27_rec_no_parent_fit", "Reject parent-fit selected O"),
        ("g27_rec_no_downstream", "Keep insertion and parent gates closed"),
        ("g27_rec_next_obstruction", "Summarize O construction obstruction next"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g27_rec_route"],
            description=(
                "Recovery selection is rejected. Recovery may audit a constructed O but cannot construct O."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g27_rec_struct_first",
        "g27_rec_weak_audit",
        "g27_rec_schw_audit",
        "g27_rec_kappa_audit",
        "g27_rec_no_parent_fit",
        "g27_rec_no_downstream",
        "g27_rec_next_obstruction",
    ]

    ns.record_route(RouteRecord(
        route_id="g27_rec_route",
        script_id=SCRIPT_ID,
        name="Group 27 O recovery-independence route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "recovery may audit but not select O",
            "AB=1/B=1/A/weak-field/Schwarzschild/gamma/PPN/kappa=0 cannot define O",
            "parent-fit closure cannot define O",
            "insertion and parent gates remain closed",
            "construction obstruction summary is next",
        ],
    ))

    for branch_id in [
        "AB1_selected_O",
        "Schwarzschild_selected_O",
        "gamma_selected_O",
        "kappa0_selected_O",
        "weak_field_selected_O",
        "parent_fit_selected_O",
        "recovery_licenses_insertion",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; recovery may audit O but cannot construct it.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g27_rec_not_derived",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Recovery may audit a constructed O but may not select O. AB=1, B=1/A, weak-field, Schwarzschild, gamma/PPN, kappa=0, "
            "and parent-fit closure cannot define O. Recovery independence does not license insertion or parent closure. This audit does not derive O."
        ),
        derivation_ids=["g27_O_recovery"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate O Recovery Independence")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    targets = build_targets()
    tests = build_tests()
    requirements = build_requirements()
    shortcuts = build_shortcuts()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_symbol_ledger(symbols, out)
    case_2_targets(targets, out)
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
