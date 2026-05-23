# Candidate accounting source incidence
#
# Group:
#   28_sector_pairing_no_overlap
#
# Script type:
#   ACCOUNTING / SOURCE INCIDENCE AUDIT
#
# Purpose
# -------
# Audit whether accounting sectors and source sectors can be included in
# sector geometry without becoming residual reservoirs or source-duplication
# channels.
#
# Locked-door question:
#
#   Can accounting sectors be prevented from becoming hidden source or metric reservoirs?
#
# This script does not derive a no-overlap theorem.
# It does not derive active O.
# It does not derive residual control.
# It does not derive B_s/F_zeta insertion.
# It does not derive parent equation closure.
#
# Tiny goblin rule:
#
#   No hiding bones in the bookkeeping drawer.

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
            "g28_tr",
            "028_sector_pairing_no_overlap__candidate_trace_residual_incidence",
            "g28_trace_res",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g28_forms",
            "028_sector_pairing_no_overlap__candidate_pairing_incidence_forms",
            "g28_pair_forms",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g28_mem",
            "028_sector_pairing_no_overlap__candidate_sector_membership_rules",
            "g28_membership",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g28_inv",
            "028_sector_pairing_no_overlap__candidate_sector_inventory",
            "g28_sector_inventory",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g28_prob",
            "028_sector_pairing_no_overlap__candidate_sector_problem_ledger",
            "g28_sector_problem",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g27_summary",
            "027_active_O_construction__candidate_group_27_status_summary",
            "g27_status_summary",
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
class AccountingSourceSymbols:
    A_eps: sp.Symbol
    A_kappa: sp.Symbol
    S_src: sp.Symbol
    R_zeta: sp.Symbol
    R_kappa: sp.Symbol
    I_Ae_Rz: sp.Symbol
    I_Ak_Rk: sp.Symbol
    I_A_src: sp.Symbol
    E_Rz_src: sp.Symbol
    E_Rk_src: sp.Symbol
    reservoir_gap: sp.Symbol
    source_gap: sp.Symbol
    accounting_gap: sp.Symbol
    edge_gap: sp.Symbol
    audit_gap: sp.Symbol
    as_load: sp.Expr


@dataclass
class AccountingSourceCandidate:
    name: str
    candidate: str
    status: str
    works_if: str
    hazard: str


@dataclass
class AccountingSourceTest:
    name: str
    test: str
    status: str
    result: str
    implication: str


@dataclass
class AccountingSourceRequirement:
    name: str
    requirement: str
    status: str
    needed_for: str
    fails_if: str


@dataclass
class RejectedAccountingSourceShortcut:
    name: str
    shortcut: str
    status: str
    reason: str


@dataclass
class AccountingSourceConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_symbols() -> AccountingSourceSymbols:
    (
        A_eps,
        A_kappa,
        S_src,
        R_zeta,
        R_kappa,
        I_Ae_Rz,
        I_Ak_Rk,
        I_A_src,
        E_Rz_src,
        E_Rk_src,
        reservoir_gap,
        source_gap,
        accounting_gap,
        edge_gap,
        audit_gap,
    ) = sp.symbols(
        "A_eps A_kappa S_src R_zeta R_kappa I_Ae_Rz I_Ak_Rk I_A_src E_Rz_src E_Rk_src "
        "reservoir_gap source_gap accounting_gap edge_gap audit_gap",
        real=True,
    )

    as_load = sp.simplify(reservoir_gap + source_gap + accounting_gap + edge_gap + audit_gap)

    return AccountingSourceSymbols(
        A_eps=A_eps,
        A_kappa=A_kappa,
        S_src=S_src,
        R_zeta=R_zeta,
        R_kappa=R_kappa,
        I_Ae_Rz=I_Ae_Rz,
        I_Ak_Rk=I_Ak_Rk,
        I_A_src=I_A_src,
        E_Rz_src=E_Rz_src,
        E_Rk_src=E_Rk_src,
        reservoir_gap=reservoir_gap,
        source_gap=source_gap,
        accounting_gap=accounting_gap,
        edge_gap=edge_gap,
        audit_gap=audit_gap,
        as_load=as_load,
    )


def build_candidates() -> List[AccountingSourceCandidate]:
    return [
        AccountingSourceCandidate(
            name="A1: accounting as audit sector",
            candidate="A_eps and A_kappa are diagnostic/accounting sectors only",
            status="CANDIDATE",
            works_if="they carry no hidden metric/source/boundary/recovery role",
            hazard="accounting label hides residual geometry",
        ),
        AccountingSourceCandidate(
            name="A2: accounting no-reservoir incidence",
            candidate="I(A_eps/A_kappa, R_zeta/R_kappa) is audit-only, not absorption",
            status="UNDERDETERMINED",
            works_if="non-reservoir law is derived",
            hazard="residuals are moved into accounting drawer",
        ),
        AccountingSourceCandidate(
            name="A3: residual-to-source exclusion",
            candidate="no directed edge R_zeta/R_kappa -> S_src",
            status="UNDERDETERMINED",
            works_if="source-routing edge law is derived",
            hazard="ordinary source duplication is assumed absent",
        ),
        AccountingSourceCandidate(
            name="A4: accounting-to-source exclusion",
            candidate="no directed edge A_eps/A_kappa -> S_src",
            status="UNDERDETERMINED",
            works_if="accounting variables are proven non-source",
            hazard="accounting term becomes hidden source",
        ),
        AccountingSourceCandidate(
            name="A5: source audit sector",
            candidate="S_src audits source duplication but does not define no-overlap alone",
            status="AUXILIARY_CANDIDATE",
            works_if="source sector remains audit-only",
            hazard="source routing is promoted to full no-overlap",
        ),
        AccountingSourceCandidate(
            name="A6: accounting/source repair-selected geometry",
            candidate="choose incidence to cancel source or accounting failure",
            status="REJECTED",
            works_if="never allowed",
            hazard="repair need constructs sector geometry",
        ),
    ]


def build_tests() -> List[AccountingSourceTest]:
    return [
        AccountingSourceTest(
            name="T1: accounting audit-only",
            test="can A_eps/A_kappa be treated as audit/accounting sectors?",
            status="CANDIDATE",
            result="yes as candidates, if non-reservoir discipline is preserved",
            implication="accounting sectors can stay in inventory but do not solve residuals",
        ),
        AccountingSourceTest(
            name="T2: accounting reservoir exclusion",
            test="is accounting no-reservoir theorem derived now?",
            status="NOT_DERIVED",
            result="no; accounting non-reservoir law is not derived",
            implication="accounting cannot yet be trusted as safe quotient/diagnostic sector",
        ),
        AccountingSourceTest(
            name="T3: residual-to-source edge exclusion",
            test="can R_zeta/R_kappa -> S_src edges be excluded now?",
            status="NOT_DERIVED",
            result="no; source-routing edge law is not derived",
            implication="source no-double-counting remains open",
        ),
        AccountingSourceTest(
            name="T4: accounting-to-source edge exclusion",
            test="can A_eps/A_kappa -> S_src edges be excluded now?",
            status="UNDERDETERMINED",
            result="not yet; accounting/source role law is missing",
            implication="accounting-source leakage remains a risk",
        ),
        AccountingSourceTest(
            name="T5: source audit sufficiency",
            test="does source audit alone define no-overlap?",
            status="INSUFFICIENT",
            result="no; source routing does not by itself control metric trace or divergence reentry",
            implication="source audit is auxiliary only",
        ),
        AccountingSourceTest(
            name="T6: downstream closure",
            test="does accounting/source incidence close residual control or active O?",
            status="REJECTED",
            result="no",
            implication="downstream gates remain closed",
        ),
    ]


def build_requirements() -> List[AccountingSourceRequirement]:
    return [
        AccountingSourceRequirement(
            name="R1: no accounting reservoir",
            requirement="prove A_eps/A_kappa carry no hidden residual metric/source load",
            status="REQUIRED",
            needed_for="safe accounting sector",
            fails_if="accounting absorbs residual geometry",
        ),
        AccountingSourceRequirement(
            name="R2: source no-double-counting",
            requirement="derive source-routing rule preventing residual/source duplication",
            status="REQUIRED",
            needed_for="source safety",
            fails_if="residuals or accounting variables become ordinary source",
        ),
        AccountingSourceRequirement(
            name="R3: no quotient hiding",
            requirement="quotient or diagnostic use of accounting sectors must be no-reservoir",
            status="REQUIRED",
            needed_for="safe quotient relation",
            fails_if="quotient hides metric/source content",
        ),
        AccountingSourceRequirement(
            name="R4: guardrail auditability",
            requirement="source/accounting incidence must preserve boundary/current/support visibility",
            status="REQUIRED",
            needed_for="future boundary/support audit",
            fails_if="accounting/source incidence hides guardrail failure",
        ),
        AccountingSourceRequirement(
            name="R5: recovery independence",
            requirement="accounting/source incidence cannot be selected from recovery success",
            status="REQUIRED",
            needed_for="anti-smuggling",
            fails_if="AB=1/Schwarzschild/gamma selects accounting/source roles",
        ),
        AccountingSourceRequirement(
            name="R6: downstream separation",
            requirement="accounting/source incidence does not license active O, residual control, insertion, or parent closure",
            status="REQUIRED",
            needed_for="not overclaiming",
            fails_if="accounting/source audit becomes theorem closure",
        ),
    ]


def build_shortcuts() -> List[RejectedAccountingSourceShortcut]:
    return [
        RejectedAccountingSourceShortcut(
            name="F1: accounting drawer",
            shortcut="move residual geometry into A_eps/A_kappa",
            status="REJECTED",
            reason="accounting cannot hide residual metric/source load",
        ),
        RejectedAccountingSourceShortcut(
            name="F2: diagnostic by label",
            shortcut="accounting/diagnostic label makes sector harmless",
            status="REJECTED",
            reason="diagnostic status requires non-reservoir law",
        ),
        RejectedAccountingSourceShortcut(
            name="F3: source edge absent by desire",
            shortcut="delete residual-to-source edge because source no-double-counting needs it",
            status="REJECTED",
            reason="edge rules must be derived",
        ),
        RejectedAccountingSourceShortcut(
            name="F4: source routing as full no-overlap",
            shortcut="source no-duplication treated as complete trace/residual no-overlap",
            status="REJECTED",
            reason="source routing does not control metric trace or divergence alone",
        ),
        RejectedAccountingSourceShortcut(
            name="F5: repair-selected accounting/source incidence",
            shortcut="choose incidence to cancel accounting/source failure",
            status="REJECTED",
            reason="repair need cannot select sector geometry",
        ),
        RejectedAccountingSourceShortcut(
            name="F6: recovery-selected accounting/source incidence",
            shortcut="choose accounting/source incidence because recovery succeeds",
            status="REJECTED",
            reason="recovery may audit but not construct",
        ),
        RejectedAccountingSourceShortcut(
            name="F7: accounting/source opens parent",
            shortcut="accounting/source incidence treated as parent readiness",
            status="REJECTED",
            reason="parent equation remains closed",
        ),
    ]


def build_conclusions() -> List[AccountingSourceConclusion]:
    return [
        AccountingSourceConclusion(
            name="C1: accounting sectors",
            conclusion="A_eps/A_kappa remain candidate audit/accounting sectors only",
            status="CANDIDATE",
            meaning="they are not safe reservoirs or quotient sectors yet",
        ),
        AccountingSourceConclusion(
            name="C2: accounting no-reservoir",
            conclusion="accounting no-reservoir theorem is not derived",
            status="NOT_DERIVED",
            meaning="accounting cannot hide zeta/kappa residual geometry",
        ),
        AccountingSourceConclusion(
            name="C3: residual-to-source",
            conclusion="residual-to-source edge exclusion is not derived",
            status="NOT_DERIVED",
            meaning="source no-double-counting remains open",
        ),
        AccountingSourceConclusion(
            name="C4: source audit",
            conclusion="source sector is auxiliary only",
            status="INSUFFICIENT",
            meaning="source routing cannot be full no-overlap by itself",
        ),
        AccountingSourceConclusion(
            name="C5: next route",
            conclusion="boundary/support incidence should be audited next",
            status="OPEN",
            meaning="source/accounting risks point to guardrail interface audit",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Accounting/source incidence problem")
    print("Question:")
    print()
    print("  Can accounting sectors be prevented from becoming hidden source or metric reservoirs?")
    print()
    print("Reference discipline:")
    print()
    print("  Accounting sectors cannot hide residual geometry.")
    print("  Source routing cannot be promoted to full no-overlap.")
    print("  Repair and recovery may not select accounting/source incidence.")

    with out.governance_assessments():
        out.line(
            "accounting/source incidence audit opened",
            StatusMark.INFO,
            "testing accounting reservoir and source duplication risks",
        )


def case_1_symbol_ledger(symbols: AccountingSourceSymbols, out: ScriptOutput) -> None:
    header("Case 1: Accounting/source symbolic ledger")
    print("Accounting/source incidence symbols:")
    print()
    for name in [
        "I_Ae_Rz",
        "I_Ak_Rk",
        "I_A_src",
        "E_Rz_src",
        "E_Rk_src",
    ]:
        print(f"  {name} = {sp.sstr(getattr(symbols, name))}")
    print()
    print("Accounting/source incidence load:")
    print()
    print(f"  L_accounting_source = {sp.sstr(symbols.as_load)}")
    print()
    print("Interpretation:")
    print()
    print("  Accounting no-reservoir and source no-double-counting are not derived.")
    print("  Accounting/source sectors can audit risk but cannot close no-overlap alone.")

    with out.derived_results():
        out.line(
            "accounting/source incidence load stated",
            StatusMark.OBLIGATION,
            f"L_accounting_source = {sp.sstr(symbols.as_load)}",
        )


def case_2_candidates(items: List[AccountingSourceCandidate], out: ScriptOutput) -> None:
    header("Case 2: Accounting/source incidence candidates")
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
            "accounting/source incidence candidates classified",
            StatusMark.DEFER,
            f"{len(items)} accounting/source incidence candidates classified",
        )


def case_3_tests(items: List[AccountingSourceTest], out: ScriptOutput) -> None:
    header("Case 3: Accounting/source incidence tests")
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
            "accounting/source incidence tests completed",
            StatusMark.DEFER,
            "accounting no-reservoir and residual-to-source edge exclusion are not derived",
        )


def case_4_requirements(items: List[AccountingSourceRequirement], out: ScriptOutput) -> None:
    header("Case 4: Accounting/source incidence requirements")
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
            "accounting/source incidence requirements stated",
            StatusMark.OBLIGATION,
            f"{len(items)} requirements remain open for accounting/source safety",
        )


def case_5_shortcuts(items: List[RejectedAccountingSourceShortcut], out: ScriptOutput) -> None:
    header("Case 5: Rejected accounting/source shortcuts")
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
            "accounting/source shortcuts rejected",
            StatusMark.FAIL,
            "accounting drawer, diagnostic by label, source edge absent by desire, source routing as full no-overlap, repair/recovery selection, and parent readiness are rejected",
        )


def case_6_conclusions(items: List[AccountingSourceConclusion], out: ScriptOutput) -> None:
    header("Case 6: Accounting/source incidence conclusions")
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
            "accounting/source incidence conclusion stated",
            StatusMark.DEFER,
            "accounting/source safety not derived; boundary/support incidence should be audited next",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Accounting/source incidence result:")
    print()
    print("  A_eps/A_kappa remain candidate audit/accounting sectors only.")
    print("  Accounting no-reservoir theorem is not derived.")
    print("  Accounting cannot hide zeta/kappa residual geometry.")
    print("  Residual-to-source edge exclusion is not derived.")
    print("  Source no-double-counting remains open.")
    print("  Source audit is auxiliary only and not full no-overlap.")
    print("  Repair-selected and recovery-selected accounting/source incidence are rejected.")
    print("  No active O, residual control, insertion, or parent closure is licensed.")
    print()
    print("Possible next script:")
    print("  candidate_boundary_support_incidence.py")
    print()
    print("Tiny goblin label:")
    print("  No hiding bones in the bookkeeping drawer.")

    with out.governance_assessments():
        out.line(
            "accounting/source incidence audit complete",
            StatusMark.PASS,
            "accounting no-reservoir and source edge exclusion remain open",
        )


def record_derivations(ns, symbols: AccountingSourceSymbols) -> None:
    ns.record_derivation(
        derivation_id="g28_acct_src",
        inputs=[
            symbols.reservoir_gap,
            symbols.source_gap,
            symbols.accounting_gap,
            symbols.edge_gap,
            symbols.audit_gap,
        ],
        output=symbols.as_load,
        method="audit accounting/source incidence and classify reservoir/source risks as open",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="accounting_source_incidence_marker",
        scope="Group 28 sector pairing/no-overlap geometry",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g28_as_reservoir", "Derive accounting no-reservoir theorem"),
        ("g28_as_src_edge", "Derive residual-to-source edge rule"),
        ("g28_as_acc_src", "Derive accounting-to-source role rule"),
        ("g28_as_quotient", "Prevent quotient/diagnostic hiding"),
        ("g28_as_guardrail", "Preserve boundary/current/support visibility"),
        ("g28_as_recovery", "Reject recovery-selected accounting/source incidence"),
        ("g28_as_downstream", "Keep O/residual/insertion/parent gates closed"),
        ("g28_as_next_bdy", "Audit boundary/support incidence next"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g28_as_route"],
            description=(
                "Accounting/source incidence is audited here. Accounting no-reservoir and source-edge exclusion are not derived."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g28_as_reservoir",
        "g28_as_src_edge",
        "g28_as_acc_src",
        "g28_as_quotient",
        "g28_as_guardrail",
        "g28_as_recovery",
        "g28_as_downstream",
        "g28_as_next_bdy",
    ]

    ns.record_route(RouteRecord(
        route_id="g28_as_route",
        script_id=SCRIPT_ID,
        name="Group 28 accounting/source incidence route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "accounting sectors are audit-only unless non-reservoir law is derived",
            "residual-to-source edges are not deleted by desire",
            "source routing is not full no-overlap",
            "repair and recovery do not select incidence",
            "downstream gates remain closed",
        ],
    ))

    for branch_id in [
        "accounting_drawer",
        "diagnostic_by_label",
        "source_edge_absent_by_desire",
        "source_routing_as_full_no_overlap",
        "repair_selected_accounting_source",
        "recovery_selected_accounting_source",
        "accounting_source_opens_parent",
        "accounting_source_as_active_O",
        "accounting_source_as_residual_control",
        "accounting_source_as_insertion",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; accounting/source incidence audit is not no-overlap theorem closure.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g28_acct_src_not_derived",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "A_eps/A_kappa remain candidate audit/accounting sectors only. Accounting no-reservoir theorem is not derived, so accounting cannot hide "
            "zeta/kappa residual geometry. Residual-to-source and accounting-to-source edge exclusions are not derived. Source audit is auxiliary only, "
            "repair/recovery-selected accounting/source incidence is rejected, and no downstream gate is opened."
        ),
        derivation_ids=["g28_acct_src"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Accounting Source Incidence")
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
