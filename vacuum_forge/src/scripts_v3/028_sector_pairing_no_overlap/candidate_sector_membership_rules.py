# Candidate sector membership rules
#
# Group:
#   28_sector_pairing_no_overlap
#
# Script type:
#   SECTOR MEMBERSHIP AUDIT
#
# Purpose
# -------
# Test candidate rules for assigning objects to the sector inventory.
#
# Locked-door question:
#
#   What makes an object belong to a sector?
#
# This script does not derive a no-overlap pairing.
# It does not derive active O.
# It does not derive residual control.
# It does not derive B_s/F_zeta insertion.
# It does not derive parent equation closure.
#
# Tiny goblin rule:
#
#   A room needs a door rule, not just a nameplate.

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
        "AUXILIARY_CANDIDATE": StatusMark.INFO,
        "CANDIDATE": StatusMark.DEFER,
        "CONDITIONALLY_SAFE": StatusMark.INFO,
        "DIAGNOSTIC_CANDIDATE": StatusMark.INFO,
        "INSUFFICIENT": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "PARENT_EXCLUDED": StatusMark.FAIL,
        "PRESERVE": StatusMark.OBLIGATION,
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
        (
            "g27_ob",
            "027_active_O_construction__candidate_O_obligations",
            "g27_O_obligations",
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
class MembershipSymbols:
    X: sp.Symbol
    zeta_Bs: sp.Symbol
    zeta_res: sp.Symbol
    kappa_res: sp.Symbol
    eps_acc: sp.Symbol
    ekappa_acc: sp.Symbol
    role_trace: sp.Symbol
    role_metric: sp.Symbol
    role_source: sp.Symbol
    role_boundary: sp.Symbol
    role_current: sp.Symbol
    role_support: sp.Symbol
    role_recovery: sp.Symbol
    coeff_origin: sp.Symbol
    membership_gap: sp.Symbol
    role_gap: sp.Symbol
    coefficient_gap: sp.Symbol
    routing_gap: sp.Symbol
    membership_load: sp.Expr


@dataclass
class MembershipRuleCandidate:
    name: str
    rule: str
    status: str
    works_if: str
    hazard: str


@dataclass
class MembershipAssignment:
    name: str
    assignment: str
    status: str
    allowed_if: str
    failure_if: str


@dataclass
class MembershipTest:
    name: str
    test: str
    status: str
    result: str
    implication: str


@dataclass
class RejectedMembershipShortcut:
    name: str
    shortcut: str
    status: str
    reason: str


@dataclass
class MembershipConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


# =============================================================================
# Builders
# =============================================================================


def build_symbols() -> MembershipSymbols:
    (
        X,
        zeta_Bs,
        zeta_res,
        kappa_res,
        eps_acc,
        ekappa_acc,
        role_trace,
        role_metric,
        role_source,
        role_boundary,
        role_current,
        role_support,
        role_recovery,
        coeff_origin,
        membership_gap,
        role_gap,
        coefficient_gap,
        routing_gap,
    ) = sp.symbols(
        "X zeta_Bs zeta_res kappa_res eps_acc ekappa_acc "
        "role_trace role_metric role_source role_boundary role_current role_support role_recovery coeff_origin "
        "membership_gap role_gap coefficient_gap routing_gap",
        real=True,
    )

    membership_load = sp.simplify(membership_gap + role_gap + coefficient_gap + routing_gap)

    return MembershipSymbols(
        X=X,
        zeta_Bs=zeta_Bs,
        zeta_res=zeta_res,
        kappa_res=kappa_res,
        eps_acc=eps_acc,
        ekappa_acc=ekappa_acc,
        role_trace=role_trace,
        role_metric=role_metric,
        role_source=role_source,
        role_boundary=role_boundary,
        role_current=role_current,
        role_support=role_support,
        role_recovery=role_recovery,
        coeff_origin=coeff_origin,
        membership_gap=membership_gap,
        role_gap=role_gap,
        coefficient_gap=coefficient_gap,
        routing_gap=routing_gap,
        membership_load=membership_load,
    )


def build_rule_candidates() -> List[MembershipRuleCandidate]:
    return [
        MembershipRuleCandidate(
            name="R1: symbol-origin rule",
            rule="sector(X) determined by which variable or symbol produced X",
            status="INSUFFICIENT",
            works_if="symbol origin uniquely determines role and no-reentry behavior",
            hazard="zeta-origin objects can split between safe trace and residual roles",
        ),
        MembershipRuleCandidate(
            name="R2: trace-role rule",
            rule="sector(X) determined by ordinary metric trace role",
            status="CANDIDATE",
            works_if="trace role is derived independently of recovery and residual labels",
            hazard="residual metric trace reentry is hidden",
        ),
        MembershipRuleCandidate(
            name="R3: source-role rule",
            rule="sector(X) determined by ordinary source or source-routing role",
            status="AUXILIARY_CANDIDATE",
            works_if="source role is audited without defining full no-overlap",
            hazard="source routing treated as complete trace/residual separation",
        ),
        MembershipRuleCandidate(
            name="R4: boundary/current/support role rule",
            rule="sector(X) determined by boundary, current, shell, or support behavior",
            status="AUXILIARY_CANDIDATE",
            works_if="used as compatibility audit only",
            hazard="guardrail failure selects the sector geometry",
        ),
        MembershipRuleCandidate(
            name="R5: coefficient-origin rule",
            rule="sector(X) determined by B_s/F_zeta coefficient origin or insertion law",
            status="UNDERDETERMINED",
            works_if="coefficient origin is derived separately",
            hazard="insertion law is smuggled into sector membership",
        ),
        MembershipRuleCandidate(
            name="R6: recovery-role rule",
            rule="sector(X) determined by AB=1, Schwarzschild, gamma, PPN, weak-field, or kappa=0 success",
            status="REJECTED",
            works_if="never allowed as construction rule",
            hazard="recovery selects sector geometry",
        ),
        MembershipRuleCandidate(
            name="R7: parent-fit rule",
            rule="sector(X) determined by parent field-equation closure",
            status="REJECTED",
            works_if="never allowed",
            hazard="parent equation selects sector geometry",
        ),
    ]


def build_assignments() -> List[MembershipAssignment]:
    return [
        MembershipAssignment(
            name="A1: zeta_Bs to T_zeta",
            assignment="zeta_Bs belongs to candidate safe trace sector T_zeta",
            status="CANDIDATE",
            allowed_if="zeta_Bs is the zeta_to_Bs safe trace route and residual reentry is excluded by future criterion",
            failure_if="T_zeta also admits zeta_res/kappa_res metric residuals",
        ),
        MembershipAssignment(
            name="A2: zeta_res to R_zeta",
            assignment="zeta_residual_metric belongs to candidate residual sector R_zeta",
            status="CANDIDATE",
            allowed_if="R_zeta is classified as unresolved residual sector, not inert/killed sector",
            failure_if="R_zeta label makes residual harmless",
        ),
        MembershipAssignment(
            name="A3: kappa_res to R_kappa",
            assignment="kappa_metric belongs to candidate residual sector R_kappa",
            status="CANDIDATE",
            allowed_if="R_kappa is classified as unresolved residual sector, not diagnostic by label",
            failure_if="R_kappa label kills kappa reentry",
        ),
        MembershipAssignment(
            name="A4: epsilon/e_kappa to accounting sectors",
            assignment="epsilon_vac and e_kappa belong to A_eps/A_kappa only as accounting sectors",
            status="UNDERDETERMINED",
            allowed_if="accounting sectors are proven non-reservoir",
            failure_if="accounting membership hides residual geometry",
        ),
        MembershipAssignment(
            name="A5: source/boundary/current/support audit sectors",
            assignment="source, boundary, current, mass, and support objects belong to audit sectors only",
            status="AUXILIARY_CANDIDATE",
            allowed_if="audit sectors do not define no-overlap by themselves",
            failure_if="audit membership becomes repair-selected geometry",
        ),
        MembershipAssignment(
            name="A6: parent sector",
            assignment="parent field-equation data belongs to no construction sector",
            status="REJECTED",
            allowed_if="not allowed",
            failure_if="parent data selects or validates membership",
        ),
    ]


def build_tests() -> List[MembershipTest]:
    return [
        MembershipTest(
            name="T1: symbol-origin sufficiency",
            test="is symbol origin enough to define membership?",
            status="INSUFFICIENT",
            result="no; zeta-origin objects include both safe trace and residual candidates",
            implication="membership needs role or incidence structure",
        ),
        MembershipTest(
            name="T2: trace-role sufficiency",
            test="is ordinary trace role enough to define T_zeta?",
            status="UNDERDETERMINED",
            result="not yet; trace role must be separated from residual metric trace",
            implication="trace membership needs no-overlap criterion",
        ),
        MembershipTest(
            name="T3: residual membership sufficiency",
            test="does placing zeta/kappa in residual sectors control them?",
            status="NOT_DERIVED",
            result="no; residual membership is classification only",
            implication="residual control is not gained",
        ),
        MembershipTest(
            name="T4: coefficient-origin sufficiency",
            test="can coefficient origin define membership now?",
            status="UNDERDETERMINED",
            result="not yet; B_s/F_zeta coefficient origin is still open",
            implication="coefficient-origin handoff remains relevant",
        ),
        MembershipTest(
            name="T5: recovery-selection test",
            test="can recovery success define sector membership?",
            status="REJECTED",
            result="no; recovery can audit but not select membership",
            implication="AB=1/Schwarzschild/gamma/PPN/weak-field cannot define sectors",
        ),
        MembershipTest(
            name="T6: parent-selection test",
            test="can parent-fit closure define sector membership?",
            status="REJECTED",
            result="no; parent equation remains closed",
            implication="parent-fit membership is forbidden",
        ),
    ]


def build_shortcuts() -> List[RejectedMembershipShortcut]:
    return [
        RejectedMembershipShortcut(
            name="F1: symbol name as membership",
            shortcut="object belongs to sector because its symbol name matches",
            status="REJECTED",
            reason="symbol origin is insufficient for zeta safe/residual split",
        ),
        RejectedMembershipShortcut(
            name="F2: trace label as safe",
            shortcut="object belongs to safe trace sector because it is called trace",
            status="REJECTED",
            reason="residual metric trace reentry remains unresolved",
        ),
        RejectedMembershipShortcut(
            name="F3: residual label as inert",
            shortcut="object belongs to residual sector and is therefore harmless",
            status="REJECTED",
            reason="residual membership is not inertness",
        ),
        RejectedMembershipShortcut(
            name="F4: accounting label as reservoir",
            shortcut="accounting membership absorbs metric/source residual load",
            status="REJECTED",
            reason="accounting cannot hide geometry",
        ),
        RejectedMembershipShortcut(
            name="F5: guardrail role as selector",
            shortcut="boundary/source/current/support failure defines membership",
            status="REJECTED",
            reason="repair need cannot select sector geometry",
        ),
        RejectedMembershipShortcut(
            name="F6: recovery as membership rule",
            shortcut="recovery target defines sector membership",
            status="REJECTED",
            reason="recovery selection is forbidden",
        ),
        RejectedMembershipShortcut(
            name="F7: parent as membership rule",
            shortcut="parent-fit closure defines sector membership",
            status="REJECTED",
            reason="parent equation remains closed",
        ),
    ]


def build_conclusions() -> List[MembershipConclusion]:
    return [
        MembershipConclusion(
            name="C1: membership rule",
            conclusion="no complete sector membership rule is derived",
            status="NOT_DERIVED",
            meaning="membership remains a theorem target",
        ),
        MembershipConclusion(
            name="C2: zeta_Bs membership",
            conclusion="zeta_Bs -> T_zeta remains candidate",
            status="CANDIDATE",
            meaning="safe trace membership is plausible but needs residual exclusion criterion",
        ),
        MembershipConclusion(
            name="C3: residual membership",
            conclusion="zeta_res/kappa_res -> residual sectors remains classification only",
            status="CANDIDATE",
            meaning="classification does not kill or inert residuals",
        ),
        MembershipConclusion(
            name="C4: coefficient origin",
            conclusion="coefficient-origin membership rule is underdetermined",
            status="UNDERDETERMINED",
            meaning="B_s/F_zeta coefficient origin may be needed later",
        ),
        MembershipConclusion(
            name="C5: next route",
            conclusion="pairing/incidence forms should be tested next",
            status="OPEN",
            meaning="membership alone does not define overlap",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Sector membership problem")
    print("Question:")
    print()
    print("  What makes an object belong to a sector?")
    print()
    print("Reference discipline:")
    print()
    print("  A named sector is not a membership rule.")
    print("  Symbol origin is not enough.")
    print("  Recovery and parent-fit cannot select membership.")

    with out.governance_assessments():
        out.line(
            "sector membership audit opened",
            StatusMark.INFO,
            "testing candidate sector membership rules without deriving no-overlap pairing",
        )


def case_1_symbol_ledger(symbols: MembershipSymbols, out: ScriptOutput) -> None:
    header("Case 1: Membership symbolic ledger")
    print("Membership role symbols:")
    print()
    for name in [
        "role_trace",
        "role_metric",
        "role_source",
        "role_boundary",
        "role_current",
        "role_support",
        "role_recovery",
        "coeff_origin",
    ]:
        print(f"  {name} = {sp.sstr(getattr(symbols, name))}")
    print()
    print("Membership load:")
    print()
    print(f"  L_membership = {sp.sstr(symbols.membership_load)}")
    print()
    print("Interpretation:")
    print()
    print("  Membership requires role, coefficient, or routing rules.")
    print("  No complete rule is derived here.")

    with out.derived_results():
        out.line(
            "sector membership load stated",
            StatusMark.OBLIGATION,
            f"L_membership = {sp.sstr(symbols.membership_load)}",
        )


def case_2_rule_candidates(items: List[MembershipRuleCandidate], out: ScriptOutput) -> None:
    header("Case 2: Candidate membership rules")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Rule: {item.rule}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Works if: {item.works_if}")
        print(f"Hazard: {item.hazard}")

    with out.governance_assessments():
        out.line(
            "sector membership rule candidates classified",
            StatusMark.DEFER,
            f"{len(items)} membership-rule candidates classified",
        )


def case_3_assignments(items: List[MembershipAssignment], out: ScriptOutput) -> None:
    header("Case 3: Candidate membership assignments")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Assignment: {item.assignment}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Allowed if: {item.allowed_if}")
        print(f"Failure if: {item.failure_if}")

    with out.governance_assessments():
        out.line(
            "candidate membership assignments classified",
            StatusMark.DEFER,
            "safe trace and residual assignments remain candidate/classification only",
        )


def case_4_tests(items: List[MembershipTest], out: ScriptOutput) -> None:
    header("Case 4: Membership tests")
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
            "sector membership tests completed",
            StatusMark.DEFER,
            "no complete membership rule derived; pairing/incidence remains next",
        )


def case_5_shortcuts(items: List[RejectedMembershipShortcut], out: ScriptOutput) -> None:
    header("Case 5: Rejected membership shortcuts")
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
            "sector membership shortcuts rejected",
            StatusMark.FAIL,
            "symbol-name, trace-label, residual-label, accounting-reservoir, guardrail-selector, recovery, and parent membership shortcuts are rejected",
        )


def case_6_conclusions(items: List[MembershipConclusion], out: ScriptOutput) -> None:
    header("Case 6: Membership conclusions")
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
            "sector membership conclusion stated",
            StatusMark.DEFER,
            "membership remains not derived; pairing/incidence forms should be tested next",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Sector membership result:")
    print()
    print("  No complete sector membership rule is derived.")
    print("  Symbol-origin membership is insufficient.")
    print("  zeta_Bs -> T_zeta remains a candidate safe-trace assignment.")
    print("  zeta_res/kappa_res -> residual sectors remains classification only.")
    print("  residual membership does not kill or inert residuals.")
    print("  accounting membership cannot hide residual geometry.")
    print("  source/boundary/current/support roles are auxiliary audits only.")
    print("  coefficient-origin membership is underdetermined.")
    print("  recovery and parent-fit membership rules are rejected.")
    print("  Pairing/incidence forms should be tested next.")
    print()
    print("Possible next script:")
    print("  candidate_pairing_incidence_forms.py")
    print()
    print("Tiny goblin label:")
    print("  A room needs a door rule, not just a nameplate.")

    with out.governance_assessments():
        out.line(
            "sector membership audit complete",
            StatusMark.PASS,
            "membership rule not derived; pairing/incidence forms remain next",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, symbols: MembershipSymbols) -> None:
    ns.record_derivation(
        derivation_id="g28_membership",
        inputs=[
            symbols.membership_gap,
            symbols.role_gap,
            symbols.coefficient_gap,
            symbols.routing_gap,
        ],
        output=symbols.membership_load,
        method="audit candidate sector membership rules and classify incompleteness",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="sector_membership_marker",
        scope="Group 28 sector pairing/no-overlap geometry",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g28_mem_rule", "Derive complete sector membership rule"),
        ("g28_mem_trace", "Define safe trace membership without residual reentry"),
        ("g28_mem_residual", "Classify residual membership without inertness by label"),
        ("g28_mem_accounting", "Prevent accounting membership as reservoir"),
        ("g28_mem_guardrail", "Keep source/boundary/current/support roles auxiliary"),
        ("g28_mem_coeff", "Resolve coefficient-origin membership if used"),
        ("g28_mem_pairing", "Test pairing/incidence forms next"),
        ("g28_mem_parent", "Reject parent-fit membership"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g28_mem_route"],
            description=(
                "Sector membership rules are not fully derived here. Pairing/incidence forms remain next."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g28_mem_rule",
        "g28_mem_trace",
        "g28_mem_residual",
        "g28_mem_accounting",
        "g28_mem_guardrail",
        "g28_mem_coeff",
        "g28_mem_pairing",
        "g28_mem_parent",
    ]

    ns.record_route(RouteRecord(
        route_id="g28_mem_route",
        script_id=SCRIPT_ID,
        name="Group 28 sector membership route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "membership is not derived from symbol name alone",
            "residual sectors are not inert by label",
            "accounting sectors are not reservoirs",
            "recovery and parent-fit do not select membership",
            "pairing/incidence forms remain next",
        ],
    ))

    for branch_id in [
        "symbol_name_as_membership",
        "trace_label_as_safe",
        "residual_label_as_inert",
        "accounting_label_as_reservoir",
        "guardrail_role_as_selector",
        "recovery_as_membership",
        "parent_as_membership",
        "membership_as_pairing",
        "membership_as_active_O",
        "membership_as_residual_control",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; membership classification does not derive pairing, active O, residual control, or parent closure.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g28_membership_not_pairing",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "No complete sector membership rule is derived. Symbol-origin membership is insufficient. zeta_Bs -> T_zeta remains candidate; "
            "zeta_res/kappa_res -> residual sectors remains classification only and does not kill or inert residuals. Accounting membership cannot hide residual geometry. "
            "Coefficient-origin membership is underdetermined. Recovery and parent-fit membership rules are rejected. Pairing/incidence forms should be tested next."
        ),
        derivation_ids=["g28_membership"],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Sector Membership Rules")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    rule_candidates = build_rule_candidates()
    assignments = build_assignments()
    tests = build_tests()
    shortcuts = build_shortcuts()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_symbol_ledger(symbols, out)
    case_2_rule_candidates(rule_candidates, out)
    case_3_assignments(assignments, out)
    case_4_tests(tests, out)
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
