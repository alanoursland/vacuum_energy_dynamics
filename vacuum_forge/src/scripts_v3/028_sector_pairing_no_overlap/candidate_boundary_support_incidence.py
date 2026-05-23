# Candidate boundary support incidence
#
# Group:
#   28_sector_pairing_no_overlap
#
# Script type:
#   BOUNDARY / SUPPORT INCIDENCE AUDIT
#
# Purpose
# -------
# Audit whether boundary, current, shell, mass, and support/matching sectors can
# remain visible without selecting or hiding no-overlap geometry.
#
# Locked-door question:
#
#   Can no-overlap survive boundary, current, shell, and support/matching interfaces?
#
# This script does not derive a no-overlap theorem.
# It does not derive active O.
# It does not derive residual control.
# It does not derive B_s/F_zeta insertion.
# It does not derive parent equation closure.
#
# Tiny goblin rule:
#
#   No sweeping crumbs under the seam.

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
        "AUXILIARY_CANDIDATE": StatusMark.INFO,
        "CANDIDATE": StatusMark.DEFER,
        "INSUFFICIENT": StatusMark.DEFER,
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
class BoundarySupportSymbols:
    B_bdy: sp.Symbol
    J_cur: sp.Symbol
    M_A: sp.Symbol
    U_sup: sp.Symbol
    T_zeta: sp.Symbol
    R_zeta: sp.Symbol
    R_kappa: sp.Symbol
    tail_scalar: sp.Symbol
    flux_current: sp.Symbol
    shell_load: sp.Symbol
    support_load: sp.Symbol
    boundary_gap: sp.Symbol
    current_gap: sp.Symbol
    mass_gap: sp.Symbol
    shell_gap: sp.Symbol
    support_gap: sp.Symbol
    repair_gap: sp.Symbol
    bs_load: sp.Expr


@dataclass
class BoundarySupportCandidate:
    name: str
    candidate: str
    status: str
    works_if: str
    hazard: str


@dataclass
class BoundarySupportTest:
    name: str
    test: str
    status: str
    result: str
    implication: str


@dataclass
class BoundarySupportRequirement:
    name: str
    requirement: str
    status: str
    needed_for: str
    fails_if: str


@dataclass
class RejectedBoundarySupportShortcut:
    name: str
    shortcut: str
    status: str
    reason: str


@dataclass
class BoundarySupportConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_symbols() -> BoundarySupportSymbols:
    (
        B_bdy,
        J_cur,
        M_A,
        U_sup,
        T_zeta,
        R_zeta,
        R_kappa,
        tail_scalar,
        flux_current,
        shell_load,
        support_load,
        boundary_gap,
        current_gap,
        mass_gap,
        shell_gap,
        support_gap,
        repair_gap,
    ) = sp.symbols(
        "B_bdy J_cur M_A U_sup T_zeta R_zeta R_kappa tail_scalar flux_current shell_load support_load "
        "boundary_gap current_gap mass_gap shell_gap support_gap repair_gap",
        real=True,
    )

    bs_load = sp.simplify(boundary_gap + current_gap + mass_gap + shell_gap + support_gap + repair_gap)

    return BoundarySupportSymbols(
        B_bdy=B_bdy,
        J_cur=J_cur,
        M_A=M_A,
        U_sup=U_sup,
        T_zeta=T_zeta,
        R_zeta=R_zeta,
        R_kappa=R_kappa,
        tail_scalar=tail_scalar,
        flux_current=flux_current,
        shell_load=shell_load,
        support_load=support_load,
        boundary_gap=boundary_gap,
        current_gap=current_gap,
        mass_gap=mass_gap,
        shell_gap=shell_gap,
        support_gap=support_gap,
        repair_gap=repair_gap,
        bs_load=bs_load,
    )


def build_candidates() -> List[BoundarySupportCandidate]:
    return [
        BoundarySupportCandidate(
            name="B1: boundary audit sector",
            candidate="B_bdy records boundary scalar-tail and shell risks",
            status="AUXILIARY_CANDIDATE",
            works_if="boundary sector remains audit-only",
            hazard="boundary repair selects no-overlap geometry",
        ),
        BoundarySupportCandidate(
            name="B2: current audit sector",
            candidate="J_cur records current-flux leakage risk",
            status="AUXILIARY_CANDIDATE",
            works_if="current sector remains visible and not absorbed",
            hazard="current leakage hidden by sector split",
        ),
        BoundarySupportCandidate(
            name="B3: mass audit sector",
            candidate="M_A records A-sector mass-shift risk",
            status="AUXILIARY_CANDIDATE",
            works_if="mass sector is not used as residual cleanup reservoir",
            hazard="mass shift hides residual geometry",
        ),
        BoundarySupportCandidate(
            name="B4: support/matching audit sector",
            candidate="U_sup records support, smoothing, seam, transition, and matching risks",
            status="AUXILIARY_CANDIDATE",
            works_if="support sector remains audit-only",
            hazard="support layer hides no-overlap failure",
        ),
        BoundarySupportCandidate(
            name="B5: support-only no-overlap",
            candidate="support(T_zeta) disjoint from support(R_zeta/R_kappa)",
            status="INSUFFICIENT",
            works_if="also paired with boundary/current/divergence/source controls",
            hazard="transition/seam/shell terms reintroduce overlap",
        ),
        BoundarySupportCandidate(
            name="B6: repair-selected no-overlap",
            candidate="choose sector geometry to eliminate boundary/current/mass/support failure",
            status="REJECTED",
            works_if="never allowed",
            hazard="guardrail failure constructs the theorem",
        ),
    ]


def build_tests() -> List[BoundarySupportTest]:
    return [
        BoundarySupportTest(
            name="T1: boundary neutrality",
            test="is scalar-tail/shell neutrality derived for the sector split?",
            status="NOT_DERIVED",
            result="no; boundary neutrality remains open",
            implication="boundary sector can audit but not close no-overlap",
        ),
        BoundarySupportTest(
            name="T2: current neutrality",
            test="is current-flux neutrality derived for the sector split?",
            status="NOT_DERIVED",
            result="no; current neutrality remains open",
            implication="current sector can audit leakage risk only",
        ),
        BoundarySupportTest(
            name="T3: mass neutrality",
            test="is A-sector mass neutrality derived for the sector split?",
            status="NOT_DERIVED",
            result="no; mass neutrality remains open",
            implication="mass sector cannot hide residual cleanup",
        ),
        BoundarySupportTest(
            name="T4: support/matching neutrality",
            test="is support/matching neutrality derived?",
            status="NOT_DERIVED",
            result="no; seam/smoothing/transition behavior remains open",
            implication="support separation cannot close no-overlap alone",
        ),
        BoundarySupportTest(
            name="T5: support-only sufficiency",
            test="does support-only separation define no-overlap?",
            status="INSUFFICIENT",
            result="no; support-only separation cannot control trace/source/divergence reentry",
            implication="support can only be auxiliary",
        ),
        BoundarySupportTest(
            name="T6: repair selection",
            test="can boundary/current/mass/support failure select sector geometry?",
            status="REJECTED",
            result="no; failure may reject a candidate but cannot define it",
            implication="repair-selected no-overlap is forbidden",
        ),
        BoundarySupportTest(
            name="T7: downstream closure",
            test="does boundary/support incidence close active O or residual control?",
            status="REJECTED",
            result="no",
            implication="downstream gates remain closed",
        ),
    ]


def build_requirements() -> List[BoundarySupportRequirement]:
    return [
        BoundarySupportRequirement(
            name="R1: boundary visibility",
            requirement="scalar-tail, shell, and boundary loads must remain visible",
            status="REQUIRED",
            needed_for="guardrail auditability",
            fails_if="sector split hides boundary leakage",
        ),
        BoundarySupportRequirement(
            name="R2: current visibility",
            requirement="current-flux leakage must remain visible",
            status="REQUIRED",
            needed_for="current neutrality theorem",
            fails_if="sector split absorbs current leakage",
        ),
        BoundarySupportRequirement(
            name="R3: mass visibility",
            requirement="A-sector mass shifts must remain visible",
            status="REQUIRED",
            needed_for="mass neutrality theorem",
            fails_if="mass sector hides residual cleanup",
        ),
        BoundarySupportRequirement(
            name="R4: support/matching visibility",
            requirement="support, smoothing, seam, transition, and matching loads must remain visible",
            status="REQUIRED",
            needed_for="support/matching safety",
            fails_if="support layer hides no-overlap failure",
        ),
        BoundarySupportRequirement(
            name="R5: no repair selection",
            requirement="boundary/current/mass/support failure may reject but not select sector geometry",
            status="REQUIRED",
            needed_for="construction independence",
            fails_if="repair need chooses no-overlap",
        ),
        BoundarySupportRequirement(
            name="R6: divergence handoff",
            requirement="boundary/support-safe split still requires divergence audit",
            status="REQUIRED",
            needed_for="future field-equation use",
            fails_if="boundary/support audit is treated as divergence safety",
        ),
        BoundarySupportRequirement(
            name="R7: downstream separation",
            requirement="boundary/support incidence does not license active O, residual control, insertion, or parent closure",
            status="REQUIRED",
            needed_for="not overclaiming",
            fails_if="guardrail audit becomes theorem closure",
        ),
    ]


def build_shortcuts() -> List[RejectedBoundarySupportShortcut]:
    return [
        RejectedBoundarySupportShortcut(
            name="F1: boundary repair as geometry",
            shortcut="choose no-overlap geometry to cancel scalar-tail/shell failure",
            status="REJECTED",
            reason="boundary repair cannot define sector geometry",
        ),
        RejectedBoundarySupportShortcut(
            name="F2: current leak hidden",
            shortcut="hide current-flux leakage inside sector split",
            status="REJECTED",
            reason="current leakage must remain visible",
        ),
        RejectedBoundarySupportShortcut(
            name="F3: mass shift hidden",
            shortcut="hide residual cleanup as A-sector mass shift",
            status="REJECTED",
            reason="mass behavior must remain visible",
        ),
        RejectedBoundarySupportShortcut(
            name="F4: support layer hiding",
            shortcut="hide no-overlap failure in smoothing/support/matching layer",
            status="REJECTED",
            reason="support/matching loads must remain auditable",
        ),
        RejectedBoundarySupportShortcut(
            name="F5: support-only proof",
            shortcut="support disjointness treated as complete no-overlap",
            status="REJECTED",
            reason="support is insufficient alone",
        ),
        RejectedBoundarySupportShortcut(
            name="F6: guardrail audit as active O",
            shortcut="boundary/support audit treated as active O construction",
            status="REJECTED",
            reason="O remains separate and not constructed",
        ),
        RejectedBoundarySupportShortcut(
            name="F7: guardrail audit opens parent",
            shortcut="boundary/support audit treated as parent readiness",
            status="REJECTED",
            reason="parent equation remains closed",
        ),
    ]


def build_conclusions() -> List[BoundarySupportConclusion]:
    return [
        BoundarySupportConclusion(
            name="C1: boundary/current/mass/support sectors",
            conclusion="guardrail sectors remain auxiliary audit sectors",
            status="AUXILIARY_CANDIDATE",
            meaning="they preserve visibility but do not define no-overlap",
        ),
        BoundarySupportConclusion(
            name="C2: neutrality theorems",
            conclusion="boundary, current, mass, and support neutralities are not derived",
            status="NOT_DERIVED",
            meaning="guardrail compatibility remains open",
        ),
        BoundarySupportConclusion(
            name="C3: support-only separation",
            conclusion="support-only separation is insufficient",
            status="INSUFFICIENT",
            meaning="support cannot control trace/source/divergence reentry alone",
        ),
        BoundarySupportConclusion(
            name="C4: repair selection",
            conclusion="repair-selected sector geometry is rejected",
            status="REJECTED",
            meaning="guardrail failure may reject but cannot construct no-overlap",
        ),
        BoundarySupportConclusion(
            name="C5: next route",
            conclusion="divergence-safe sector split should be audited next",
            status="OPEN",
            meaning="sector geometry cannot be field-equation usable without divergence behavior",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Boundary/support incidence problem")
    print("Question:")
    print()
    print("  Can no-overlap survive boundary, current, shell, and support/matching interfaces?")
    print()
    print("Reference discipline:")
    print()
    print("  Guardrail sectors preserve visibility.")
    print("  They may reject a candidate no-overlap geometry.")
    print("  They may not select or hide one.")

    with out.governance_assessments():
        out.line(
            "boundary/support incidence audit opened",
            StatusMark.INFO,
            "testing guardrail visibility without deriving no-overlap theorem",
        )


def case_1_symbol_ledger(symbols: BoundarySupportSymbols, out: ScriptOutput) -> None:
    header("Case 1: Boundary/support symbolic ledger")
    print("Boundary/support symbols:")
    print()
    for name in [
        "tail_scalar",
        "flux_current",
        "shell_load",
        "support_load",
    ]:
        print(f"  {name} = {sp.sstr(getattr(symbols, name))}")
    print()
    print("Boundary/support incidence load:")
    print()
    print(f"  L_boundary_support = {sp.sstr(symbols.bs_load)}")
    print()
    print("Interpretation:")
    print()
    print("  Boundary/current/mass/support neutrality is not derived.")
    print("  Guardrail sectors can audit risk but cannot close no-overlap alone.")

    with out.derived_results():
        out.line(
            "boundary/support incidence load stated",
            StatusMark.OBLIGATION,
            f"L_boundary_support = {sp.sstr(symbols.bs_load)}",
        )


def case_2_candidates(items: List[BoundarySupportCandidate], out: ScriptOutput) -> None:
    header("Case 2: Boundary/support incidence candidates")
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
            "boundary/support incidence candidates classified",
            StatusMark.DEFER,
            f"{len(items)} boundary/support candidates classified",
        )


def case_3_tests(items: List[BoundarySupportTest], out: ScriptOutput) -> None:
    header("Case 3: Boundary/support incidence tests")
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
            "boundary/support incidence tests completed",
            StatusMark.DEFER,
            "guardrail neutralities not derived; repair-selected geometry rejected",
        )


def case_4_requirements(items: List[BoundarySupportRequirement], out: ScriptOutput) -> None:
    header("Case 4: Boundary/support incidence requirements")
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
            "boundary/support incidence requirements stated",
            StatusMark.OBLIGATION,
            f"{len(items)} guardrail requirements remain open",
        )


def case_5_shortcuts(items: List[RejectedBoundarySupportShortcut], out: ScriptOutput) -> None:
    header("Case 5: Rejected boundary/support shortcuts")
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
            "boundary/support shortcuts rejected",
            StatusMark.FAIL,
            "boundary repair, current hiding, mass hiding, support hiding, support-only proof, active-O upgrade, and parent readiness are rejected",
        )


def case_6_conclusions(items: List[BoundarySupportConclusion], out: ScriptOutput) -> None:
    header("Case 6: Boundary/support incidence conclusions")
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
            "boundary/support incidence conclusion stated",
            StatusMark.DEFER,
            "guardrail sectors remain auxiliary; divergence-safe sector split is next",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Boundary/support incidence result:")
    print()
    print("  Boundary/current/mass/support sectors remain auxiliary audit sectors.")
    print("  Boundary scalar-tail/shell neutrality is not derived.")
    print("  Current-flux neutrality is not derived.")
    print("  A-sector mass neutrality is not derived.")
    print("  Support/matching neutrality is not derived.")
    print("  Support-only separation is insufficient.")
    print("  Guardrail failure may reject but cannot select no-overlap geometry.")
    print("  No active O, residual control, insertion, or parent closure is licensed.")
    print()
    print("Possible next script:")
    print("  candidate_divergence_safe_sector_split.py")
    print()
    print("Tiny goblin label:")
    print("  No sweeping crumbs under the seam.")

    with out.governance_assessments():
        out.line(
            "boundary/support incidence audit complete",
            StatusMark.PASS,
            "guardrail neutralities remain open; divergence-safe sector split should be audited next",
        )


def record_derivations(ns, symbols: BoundarySupportSymbols) -> None:
    ns.record_derivation(
        derivation_id="g28_bdy_sup",
        inputs=[
            symbols.boundary_gap,
            symbols.current_gap,
            symbols.mass_gap,
            symbols.shell_gap,
            symbols.support_gap,
            symbols.repair_gap,
        ],
        output=symbols.bs_load,
        method="audit boundary/current/mass/support incidence and classify guardrail neutralities as open",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="boundary_support_incidence_marker",
        scope="Group 28 sector pairing/no-overlap geometry",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g28_bs_boundary", "Derive boundary scalar-tail/shell neutrality"),
        ("g28_bs_current", "Derive current-flux neutrality"),
        ("g28_bs_mass", "Derive A-sector mass neutrality"),
        ("g28_bs_support", "Derive support/matching neutrality"),
        ("g28_bs_no_repair", "Prevent repair-selected sector geometry"),
        ("g28_bs_div", "Audit divergence-safe sector split next"),
        ("g28_bs_downstream", "Keep O/residual/insertion/parent gates closed"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g28_bs_route"],
            description=(
                "Boundary/support incidence is audited here. Guardrail neutralities are not derived and repair-selected geometry is rejected."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g28_bs_boundary",
        "g28_bs_current",
        "g28_bs_mass",
        "g28_bs_support",
        "g28_bs_no_repair",
        "g28_bs_div",
        "g28_bs_downstream",
    ]

    ns.record_route(RouteRecord(
        route_id="g28_bs_route",
        script_id=SCRIPT_ID,
        name="Group 28 boundary/support incidence route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "guardrail sectors are auxiliary audits",
            "support-only separation is insufficient",
            "repair failure may reject but not select sector geometry",
            "divergence-safe sector split remains next",
            "downstream gates remain closed",
        ],
    ))

    for branch_id in [
        "boundary_repair_as_geometry",
        "current_leak_hidden",
        "mass_shift_hidden",
        "support_layer_hiding",
        "support_only_proof",
        "guardrail_audit_as_active_O",
        "guardrail_audit_opens_parent",
        "guardrail_audit_as_residual_control",
        "guardrail_audit_as_insertion",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; boundary/support incidence audit is not no-overlap theorem closure.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g28_bdy_sup_not_derived",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Boundary/current/mass/support sectors remain auxiliary audit sectors. Boundary scalar-tail/shell neutrality, current-flux neutrality, "
            "A-sector mass neutrality, and support/matching neutrality are not derived. Support-only separation is insufficient. Guardrail failure may reject "
            "but cannot select no-overlap geometry. No downstream gate is opened."
        ),
        derivation_ids=["g28_bdy_sup"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Boundary Support Incidence")
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
