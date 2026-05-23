# Candidate recovery independent sector geometry
#
# Group:
#   28_sector_pairing_no_overlap
#
# Script type:
#   RECOVERY-INDEPENDENCE AUDIT
#
# Purpose
# -------
# Audit whether sector geometry can be defined without being selected from
# AB=1, B=1/A, Schwarzschild, gamma, PPN, weak-field, kappa=0, or parent-fit closure.
#
# Locked-door question:
#
#   Can sector geometry be defined without recovery selection?
#
# This script does not derive a no-overlap theorem.
# It does not derive active O.
# It does not derive residual control.
# It does not derive B_s/F_zeta insertion.
# It does not derive parent equation closure.
#
# Tiny goblin rule:
#
#   A map may be tested by the treasure, but not drawn from the glitter.

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
        "CANDIDATE": StatusMark.DEFER,
        "CONDITIONALLY_SAFE": StatusMark.INFO,
        "NOT_DERIVED": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "UNDERDETERMINED": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        ("g28_div", "028_sector_pairing_no_overlap__candidate_divergence_safe_sector_split", "g28_div_safe", RecordKind.INVENTORY_MARKER),
        ("g28_bdy", "028_sector_pairing_no_overlap__candidate_boundary_support_incidence", "g28_bdy_sup", RecordKind.INVENTORY_MARKER),
        ("g28_as", "028_sector_pairing_no_overlap__candidate_accounting_source_incidence", "g28_acct_src", RecordKind.INVENTORY_MARKER),
        ("g28_tr", "028_sector_pairing_no_overlap__candidate_trace_residual_incidence", "g28_trace_res", RecordKind.INVENTORY_MARKER),
        ("g28_forms", "028_sector_pairing_no_overlap__candidate_pairing_incidence_forms", "g28_pair_forms", RecordKind.INVENTORY_MARKER),
        ("g28_mem", "028_sector_pairing_no_overlap__candidate_sector_membership_rules", "g28_membership", RecordKind.INVENTORY_MARKER),
        ("g28_inv", "028_sector_pairing_no_overlap__candidate_sector_inventory", "g28_sector_inventory", RecordKind.INVENTORY_MARKER),
        ("g28_prob", "028_sector_pairing_no_overlap__candidate_sector_problem_ledger", "g28_sector_problem", RecordKind.INVENTORY_MARKER),
        ("g27_summary", "027_active_O_construction__candidate_group_27_status_summary", "g27_status_summary", RecordKind.INVENTORY_MARKER),
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
class RecoveryGeometrySymbols:
    AB1: sp.Symbol
    B_inv_A: sp.Symbol
    Schw: sp.Symbol
    gamma: sp.Symbol
    PPN: sp.Symbol
    weak: sp.Symbol
    kappa0: sp.Symbol
    parent_fit: sp.Symbol
    T_zeta: sp.Symbol
    R_zeta: sp.Symbol
    R_kappa: sp.Symbol
    recovery_gap: sp.Symbol
    weak_gap: sp.Symbol
    schwarz_gap: sp.Symbol
    gamma_gap: sp.Symbol
    kappa_gap: sp.Symbol
    parent_fit_gap: sp.Symbol
    rec_load: sp.Expr


@dataclass
class RecoveryGeometryTarget:
    name: str
    target: str
    status: str
    allowed_as: str
    forbidden_as: str


@dataclass
class RecoveryGeometryTest:
    name: str
    test: str
    status: str
    result: str
    implication: str


@dataclass
class RecoveryGeometryRequirement:
    name: str
    requirement: str
    status: str
    needed_for: str
    fails_if: str


@dataclass
class RejectedRecoveryGeometryShortcut:
    name: str
    shortcut: str
    status: str
    reason: str


@dataclass
class RecoveryGeometryConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_symbols() -> RecoveryGeometrySymbols:
    (
        AB1,
        B_inv_A,
        Schw,
        gamma,
        PPN,
        weak,
        kappa0,
        parent_fit,
        T_zeta,
        R_zeta,
        R_kappa,
        recovery_gap,
        weak_gap,
        schwarz_gap,
        gamma_gap,
        kappa_gap,
        parent_fit_gap,
    ) = sp.symbols(
        "AB1 B_inv_A Schw gamma PPN weak kappa0 parent_fit T_zeta R_zeta R_kappa "
        "recovery_gap weak_gap schwarz_gap gamma_gap kappa_gap parent_fit_gap",
        real=True,
    )

    rec_load = sp.simplify(
        recovery_gap + weak_gap + schwarz_gap + gamma_gap + kappa_gap + parent_fit_gap
    )

    return RecoveryGeometrySymbols(
        AB1=AB1,
        B_inv_A=B_inv_A,
        Schw=Schw,
        gamma=gamma,
        PPN=PPN,
        weak=weak,
        kappa0=kappa0,
        parent_fit=parent_fit,
        T_zeta=T_zeta,
        R_zeta=R_zeta,
        R_kappa=R_kappa,
        recovery_gap=recovery_gap,
        weak_gap=weak_gap,
        schwarz_gap=schwarz_gap,
        gamma_gap=gamma_gap,
        kappa_gap=kappa_gap,
        parent_fit_gap=parent_fit_gap,
        rec_load=rec_load,
    )


def build_targets() -> List[RecoveryGeometryTarget]:
    return [
        RecoveryGeometryTarget(
            name="R1: AB=1",
            target="AB=1 exterior compensation",
            status="AUDIT_ONLY",
            allowed_as="downstream recovery check",
            forbidden_as="sector membership, pairing, incidence, routing, or divergence selector",
        ),
        RecoveryGeometryTarget(
            name="R2: B=1/A",
            target="reciprocal spatial factor",
            status="AUDIT_ONLY",
            allowed_as="downstream static exterior check",
            forbidden_as="sector split definition",
        ),
        RecoveryGeometryTarget(
            name="R3: Schwarzschild exterior",
            target="Schwarzschild-like exterior recovery",
            status="AUDIT_ONLY",
            allowed_as="downstream solution audit",
            forbidden_as="reason for no-overlap geometry",
        ),
        RecoveryGeometryTarget(
            name="R4: gamma / PPN",
            target="gamma-like or PPN gamma = 1",
            status="AUDIT_ONLY",
            allowed_as="phenomenological audit",
            forbidden_as="incidence or pairing criterion",
        ),
        RecoveryGeometryTarget(
            name="R5: weak-field success",
            target="weak-field recovery",
            status="AUDIT_ONLY",
            allowed_as="downstream linearized audit",
            forbidden_as="sector geometry construction rule",
        ),
        RecoveryGeometryTarget(
            name="R6: kappa=0 exterior",
            target="areal/static exterior kappa suppression",
            status="AUDIT_ONLY",
            allowed_as="downstream kappa audit",
            forbidden_as="residual-sector exclusion rule",
        ),
        RecoveryGeometryTarget(
            name="R7: parent-fit closure",
            target="parent equation fit or closure",
            status="REJECTED",
            allowed_as="not allowed in this group",
            forbidden_as="sector geometry construction target",
        ),
    ]


def build_tests() -> List[RecoveryGeometryTest]:
    return [
        RecoveryGeometryTest(
            name="T1: recovery audit permission",
            test="may recovery audit a completed sector geometry?",
            status="CONDITIONALLY_SAFE",
            result="yes, after construction",
            implication="recovery remains useful downstream",
        ),
        RecoveryGeometryTest(
            name="T2: recovery selection",
            test="may recovery choose sector membership or incidence?",
            status="REJECTED",
            result="no",
            implication="sector geometry must be structurally defined",
        ),
        RecoveryGeometryTest(
            name="T3: AB=1 / B=1/A selection",
            test="may AB=1 or B=1/A select sector geometry?",
            status="REJECTED",
            result="no",
            implication="exterior compensation cannot define no-overlap",
        ),
        RecoveryGeometryTest(
            name="T4: Schwarzschild/gamma/PPN selection",
            test="may Schwarzschild, gamma, or PPN success select sector geometry?",
            status="REJECTED",
            result="no",
            implication="phenomenology cannot define incidence",
        ),
        RecoveryGeometryTest(
            name="T5: weak-field selection",
            test="may weak-field success define sector split?",
            status="REJECTED",
            result="no",
            implication="weak-field recovery remains audit-only",
        ),
        RecoveryGeometryTest(
            name="T6: kappa=0 selection",
            test="may exterior kappa suppression define residual-sector exclusion?",
            status="REJECTED",
            result="no",
            implication="kappa recovery cannot define no-overlap",
        ),
        RecoveryGeometryTest(
            name="T7: parent-fit selection",
            test="may parent-fit closure select sector geometry?",
            status="REJECTED",
            result="no",
            implication="parent equation remains closed",
        ),
    ]


def build_requirements() -> List[RecoveryGeometryRequirement]:
    return [
        RecoveryGeometryRequirement(
            name="Q1: structural definition first",
            requirement="sector inventory, membership, incidence/routing, and divergence behavior must be structurally defined",
            status="REQUIRED",
            needed_for="recovery-independent sector geometry",
            fails_if="recovery target chooses structure",
        ),
        RecoveryGeometryRequirement(
            name="Q2: audit only",
            requirement="AB=1/B=1/A/Schwarzschild/gamma/PPN/weak-field/kappa=0 are audits only",
            status="REQUIRED",
            needed_for="anti-smuggling",
            fails_if="recovery result becomes construction rule",
        ),
        RecoveryGeometryRequirement(
            name="Q3: no parent fit",
            requirement="parent-fit closure cannot select sector geometry",
            status="REQUIRED",
            needed_for="parent gate closure",
            fails_if="parent readiness chooses no-overlap",
        ),
        RecoveryGeometryRequirement(
            name="Q4: no hidden insertion",
            requirement="recovery success cannot license B_s/F_zeta insertion",
            status="REQUIRED",
            needed_for="insertion separation",
            fails_if="recovery success becomes coefficient/insertion law",
        ),
        RecoveryGeometryRequirement(
            name="Q5: no active O upgrade",
            requirement="recovery-independent audit does not construct active O",
            status="REQUIRED",
            needed_for="active-O separation",
            fails_if="anti-smuggling result is upgraded to O theorem",
        ),
        RecoveryGeometryRequirement(
            name="Q6: no residual-control upgrade",
            requirement="recovery-independent audit does not close residual control",
            status="REQUIRED",
            needed_for="residual-control separation",
            fails_if="recovery rejection is treated as no-overlap theorem",
        ),
    ]


def build_shortcuts() -> List[RejectedRecoveryGeometryShortcut]:
    return [
        RejectedRecoveryGeometryShortcut(
            name="S1: AB=1 selected geometry",
            shortcut="choose sector split because AB=1 works",
            status="REJECTED",
            reason="AB=1 is downstream audit, not construction rule",
        ),
        RejectedRecoveryGeometryShortcut(
            name="S2: Schwarzschild selected geometry",
            shortcut="choose incidence because Schwarzschild exterior works",
            status="REJECTED",
            reason="Schwarzschild recovery may audit but not select incidence",
        ),
        RejectedRecoveryGeometryShortcut(
            name="S3: gamma selected geometry",
            shortcut="choose pairing because gamma/PPN works",
            status="REJECTED",
            reason="phenomenology cannot define no-overlap",
        ),
        RejectedRecoveryGeometryShortcut(
            name="S4: weak-field selected geometry",
            shortcut="choose sector geometry from weak-field success",
            status="REJECTED",
            reason="weak-field recovery is not sector-geometry derivation",
        ),
        RejectedRecoveryGeometryShortcut(
            name="S5: kappa=0 selected geometry",
            shortcut="choose residual exclusion because exterior kappa should vanish",
            status="REJECTED",
            reason="kappa recovery cannot define residual-sector exclusion",
        ),
        RejectedRecoveryGeometryShortcut(
            name="S6: parent-fit selected geometry",
            shortcut="choose sector geometry to make parent equation close",
            status="REJECTED",
            reason="parent gate remains closed",
        ),
        RejectedRecoveryGeometryShortcut(
            name="S7: recovery licenses insertion",
            shortcut="use recovery success as B_s/F_zeta insertion law",
            status="REJECTED",
            reason="coefficient origin and insertion remain separate",
        ),
    ]


def build_conclusions() -> List[RecoveryGeometryConclusion]:
    return [
        RecoveryGeometryConclusion(
            name="C1: recovery as audit",
            conclusion="recovery may audit completed sector geometry",
            status="CONDITIONALLY_SAFE",
            meaning="recovery remains downstream validation only",
        ),
        RecoveryGeometryConclusion(
            name="C2: recovery as construction",
            conclusion="recovery may not select sector geometry",
            status="REJECTED",
            meaning="sector geometry must be structurally defined",
        ),
        RecoveryGeometryConclusion(
            name="C3: parent/insertion",
            conclusion="parent-fit and insertion-by-recovery are rejected",
            status="REJECTED",
            meaning="parent and insertion gates remain closed",
        ),
        RecoveryGeometryConclusion(
            name="C4: construction status",
            conclusion="recovery independence alone does not construct no-overlap geometry",
            status="NOT_DERIVED",
            meaning="anti-smuggling is necessary but not sufficient",
        ),
        RecoveryGeometryConclusion(
            name="C5: next route",
            conclusion="sector geometry obstruction should be classified next",
            status="OPEN",
            meaning="the group is ready to summarize whether current objects construct no-overlap geometry",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Recovery-independent sector geometry problem")
    print("Question:")
    print()
    print("  Can sector geometry be defined without recovery selection?")
    print()
    print("Reference discipline:")
    print()
    print("  Recovery may audit after construction.")
    print("  Recovery may not choose membership, incidence, routing, divergence behavior, or parent closure.")

    with out.governance_assessments():
        out.line(
            "recovery-independent sector geometry audit opened",
            StatusMark.INFO,
            "testing anti-smuggling constraints for sector geometry",
        )


def case_1_symbol_ledger(symbols: RecoveryGeometrySymbols, out: ScriptOutput) -> None:
    header("Case 1: Recovery-selection symbolic ledger")
    print("Recovery target symbols:")
    print()
    for name in ["AB1", "B_inv_A", "Schw", "gamma", "PPN", "weak", "kappa0", "parent_fit"]:
        print(f"  {name} = {sp.sstr(getattr(symbols, name))}")
    print()
    print("Recovery-selection load:")
    print()
    print(f"  L_recovery_geometry = {sp.sstr(symbols.rec_load)}")
    print()
    print("Interpretation:")
    print()
    print("  Recovery can audit completed sector geometry.")
    print("  Recovery cannot construct sector geometry.")

    with out.derived_results():
        out.line(
            "recovery-selection load stated",
            StatusMark.OBLIGATION,
            f"L_recovery_geometry = {sp.sstr(symbols.rec_load)}",
        )


def case_2_targets(items: List[RecoveryGeometryTarget], out: ScriptOutput) -> None:
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
            "sector-geometry recovery targets classified",
            StatusMark.PASS,
            f"{len(items)} targets classified as audit-only or rejected",
        )


def case_3_tests(items: List[RecoveryGeometryTest], out: ScriptOutput) -> None:
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
            "sector-geometry recovery-independence tests completed",
            StatusMark.PASS,
            "recovery selection rejected; recovery audit remains conditionally safe",
        )


def case_4_requirements(items: List[RecoveryGeometryRequirement], out: ScriptOutput) -> None:
    header("Case 4: Recovery-independence requirements")
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
            "sector-geometry recovery-independence requirements stated",
            StatusMark.OBLIGATION,
            f"{len(items)} anti-smuggling requirements remain active",
        )


def case_5_shortcuts(items: List[RejectedRecoveryGeometryShortcut], out: ScriptOutput) -> None:
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
            "sector-geometry recovery shortcuts rejected",
            StatusMark.FAIL,
            "AB=1, Schwarzschild, gamma/PPN, weak-field, kappa=0, parent-fit, and insertion-by-recovery shortcuts are rejected",
        )


def case_6_conclusions(items: List[RecoveryGeometryConclusion], out: ScriptOutput) -> None:
    header("Case 6: Recovery-independent sector geometry conclusions")
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
            "sector-geometry recovery-independence conclusion stated",
            StatusMark.PASS,
            "recovery selection rejected; construction obstruction classifier is next",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Recovery-independent sector geometry result:")
    print()
    print("  Recovery may audit completed sector geometry.")
    print("  Recovery may not select sector geometry.")
    print("  AB=1, B=1/A, Schwarzschild, gamma, PPN, weak-field, and kappa=0 cannot define membership, incidence, routing, or divergence behavior.")
    print("  Parent-fit closure cannot define sector geometry.")
    print("  Recovery success cannot license B_s/F_zeta insertion.")
    print("  Anti-smuggling is necessary but does not construct no-overlap geometry.")
    print("  No active O, residual control, insertion, or parent closure is licensed.")
    print()
    print("Possible next script:")
    print("  candidate_sector_geometry_obstruction.py")
    print()
    print("Tiny goblin label:")
    print("  A map may be tested by the treasure, but not drawn from the glitter.")

    with out.governance_assessments():
        out.line(
            "recovery-independent sector geometry audit complete",
            StatusMark.PASS,
            "recovery selection rejected; sector geometry obstruction should be classified next",
        )


def record_derivations(ns, symbols: RecoveryGeometrySymbols) -> None:
    ns.record_derivation(
        derivation_id="g28_recovery",
        inputs=[
            symbols.recovery_gap,
            symbols.weak_gap,
            symbols.schwarz_gap,
            symbols.gamma_gap,
            symbols.kappa_gap,
            symbols.parent_fit_gap,
        ],
        output=symbols.rec_load,
        method="audit recovery-independent sector geometry and reject recovery-selected no-overlap",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="recovery_independent_sector_marker",
        scope="Group 28 sector pairing/no-overlap geometry",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g28_rec_structural", "Define sector geometry structurally"),
        ("g28_rec_audit_only", "Keep recovery targets audit-only"),
        ("g28_rec_no_parent", "Reject parent-fit sector geometry"),
        ("g28_rec_no_insertion", "Reject insertion-by-recovery"),
        ("g28_rec_no_O", "Do not upgrade recovery independence to active O"),
        ("g28_rec_no_residual", "Do not upgrade recovery independence to residual control"),
        ("g28_rec_next_obs", "Classify sector geometry obstruction next"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g28_rec_route"],
            description=(
                "Recovery selection is rejected. Recovery may audit completed sector geometry but cannot construct it."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g28_rec_structural",
        "g28_rec_audit_only",
        "g28_rec_no_parent",
        "g28_rec_no_insertion",
        "g28_rec_no_O",
        "g28_rec_no_residual",
        "g28_rec_next_obs",
    ]

    ns.record_route(RouteRecord(
        route_id="g28_rec_route",
        script_id=SCRIPT_ID,
        name="Group 28 recovery-independent sector geometry route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "recovery may audit but not select sector geometry",
            "AB=1/B=1/A/Schwarzschild/gamma/PPN/weak-field/kappa=0 cannot define sector geometry",
            "parent-fit cannot define sector geometry",
            "insertion and downstream gates remain closed",
            "sector geometry obstruction classifier is next",
        ],
    ))

    for branch_id in [
        "AB1_selected_geometry",
        "Schwarzschild_selected_geometry",
        "gamma_selected_geometry",
        "weak_field_selected_geometry",
        "kappa0_selected_geometry",
        "parent_fit_selected_geometry",
        "recovery_licenses_insertion",
        "recovery_constructs_active_O",
        "recovery_closes_residual_control",
        "recovery_opens_parent",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; recovery may audit but cannot construct sector geometry or open downstream gates.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g28_recovery_not_geometry",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Recovery may audit completed sector geometry but may not select sector geometry. AB=1, B=1/A, Schwarzschild, gamma, PPN, weak-field, and kappa=0 "
            "cannot define membership, incidence, routing, or divergence behavior. Parent-fit closure cannot define sector geometry. Recovery success cannot license "
            "B_s/F_zeta insertion. Anti-smuggling is necessary but does not construct no-overlap geometry."
        ),
        derivation_ids=["g28_recovery"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Recovery Independent Sector Geometry")
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
