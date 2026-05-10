# Candidate current-split projection operator
#
# Group:
#   20_no_overlap_and_projection_operators
#
# Script type:
#   REQUIREMENTS / DIAGNOSTIC
#
# Purpose
# -------
# Test whether projection language can make the J_V / J_sub / J_exch split
# operator-level without first defining J_V, source sides, neutrality, and
# boundary behavior.
#
# Locked-door question:
#
#   Can O make J_sub/J_exch or J_V split operator-level?


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


@dataclass
class CurrentProjectionEntry:
    name: str
    candidate: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="source_sector_projection_operator_marker",
        upstream_script_id="20_no_overlap_and_projection_operators__candidate_source_sector_projection_operator",
        upstream_derivation_id="source_sector_projection_operator_marker",
    )
    return archive, ns, invalidated


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


def entry_status_mark(status: str) -> StatusMark:
    return {
        "CANDIDATE": StatusMark.INFO,
        "DEFER": StatusMark.DEFER,
        "RECOMMENDED": StatusMark.PASS,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "RISK": StatusMark.WARN,
        "SAFE_IF": StatusMark.INFO,
        "THEOREM_TARGET": StatusMark.DEFER,
        "UNRESOLVED": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def build_entries() -> List[CurrentProjectionEntry]:
    return [
        CurrentProjectionEntry(
            name="C1: current-split projection target",
            candidate="O_current makes J_V -> J_sub + J_exch operator-level",
            role="core Group 20 current target",
            allowed_if="J_V, split criterion, domains, source sides, and boundary behavior are defined first",
            forbidden_if="projection defines the current split by naming subroles",
            status="THEOREM_TARGET",
            missing="J_V, O_current, split criterion, source sides",
            consequence="current split remains theorem target",
        ),
        CurrentProjectionEntry(
            name="C2: unresolved umbrella J_V",
            candidate="J_V remains unresolved umbrella notation",
            role="safe fallback",
            allowed_if="no operator split criterion is derived",
            forbidden_if="J_V is used as a physical current or repair current",
            status="SAFE_IF",
            missing="physical J_V flux law",
            consequence="projection cannot split an undefined current into defined parts",
        ),
        CurrentProjectionEntry(
            name="C3: support-based split",
            candidate="J_sub and J_exch separated by support/domain",
            role="candidate split class",
            allowed_if="support domains are structural and boundary-neutral",
            forbidden_if="support is chosen after leakage or recovery failure appears",
            status="CANDIDATE",
            missing="support law and boundary theorem",
            consequence="possible only after current support is real",
        ),
        CurrentProjectionEntry(
            name="C4: divergence-based split",
            candidate="J_sub divergence-free, J_exch carries source/relaxation divergence",
            role="candidate split class",
            allowed_if="divergence identities and Sigma/R operators are independently defined",
            forbidden_if="divergence labels define Sigma/R or hide exchange tuning",
            status="THEOREM_TARGET",
            missing="divergence identity, Sigma/R operators",
            consequence="cannot proceed while Sigma/R remain role-level",
        ),
        CurrentProjectionEntry(
            name="C5: pure-wind neutral subspace",
            candidate="J_sub lies in a pure-wind neutral subspace",
            role="J_sub safety target",
            allowed_if="pure wind neutrality, matter decoupling, M_ext neutrality, and scalar neutrality are derived",
            forbidden_if="J_sub gravitates by existence or becomes preferred-frame force",
            status="THEOREM_TARGET",
            missing="pure wind neutrality theorem",
            consequence="J_sub remains theorem target only",
        ),
        CurrentProjectionEntry(
            name="C6: active-exchange support subspace",
            candidate="J_exch lives only where exchange source/relaxation operators are active",
            role="J_exch safety target",
            allowed_if="source side and relaxation side are real and not repair",
            forbidden_if="J_exch cancels boundary leakage, singularity behavior, or recovery mismatch",
            status="THEOREM_TARGET",
            missing="J_exch source/support law",
            consequence="J_exch remains theorem target only",
        ),
        CurrentProjectionEntry(
            name="C7: zero-net ordinary-sector projection",
            candidate="project ordinary sector onto Sigma_V - R_V = 0 branch",
            role="ordinary-sector safety candidate",
            allowed_if="zero-net condition follows from source/relaxation laws",
            forbidden_if="zero-net condition hides undefined active exchange",
            status="CANDIDATE",
            missing="ordinary-sector exchange neutrality theorem",
            consequence="zero-net branch remains live but not derived",
        ),
        CurrentProjectionEntry(
            name="C8: zero-creation ordinary-sector projection",
            candidate="project ordinary sector onto Sigma_V = R_V = 0 branch",
            role="strong ordinary-sector safety candidate",
            allowed_if="curvature changes are attributed to constraint/warping rather than creation/destruction",
            forbidden_if="creation language is still used as ordinary source",
            status="CANDIDATE",
            missing="zero-creation theorem",
            consequence="zero-creation branch remains a safe candidate",
        ),
        CurrentProjectionEntry(
            name="C9: timelike/domain projection",
            candidate="restrict u_vac normalization to D_V = {J_V^2 < 0, J_V != 0}",
            role="domain guard",
            allowed_if="J_V exists and domain is structural",
            forbidden_if="domain excludes problematic regions by convenience",
            status="REQUIRED",
            missing="J_V domain theorem",
            consequence="u_vac remains unresolved and domain-limited",
        ),
        CurrentProjectionEntry(
            name="C10: remainder-current split",
            candidate="define J_sub = J_V - J_exch or J_exch = J_V - J_sub",
            role="forbidden split shortcut",
            allowed_if="never without an independent split criterion",
            forbidden_if="leftover bookkeeping becomes ontology",
            status="REJECTED",
            missing="not pursued",
            consequence="current split cannot be defined by remainder",
        ),
        CurrentProjectionEntry(
            name="C11: repair-current projection",
            candidate="projection chooses current subspace to cancel leakage, mass shift, or scalar charge",
            role="forbidden repair branch",
            allowed_if="never as mechanism",
            forbidden_if="current projection is selected after failure appears",
            status="REJECTED",
            missing="not pursued",
            consequence="current projection cannot repair boundary or recovery failures",
        ),
        CurrentProjectionEntry(
            name="C12: current-split decision",
            candidate="O_current cannot make J_sub/J_exch operator-level until J_V and source sides exist",
            role="current branch decision",
            allowed_if="future current scripts keep split role-level until prerequisites are derived",
            forbidden_if="projection language is treated as current definition",
            status="RECOMMENDED",
            missing="J_V/source/operator split derivation",
            consequence="next script should test projection commutation and divergence",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Current-split projection problem")
    print("Question:")
    print()
    print("  Can O make J_sub/J_exch or J_V split operator-level?")
    print()
    print("Goal:")
    print()
    print("  test whether projection can strengthen the Group 18 role-level split")
    print()
    print("Discipline:")
    print()
    print("  J_V must be defined first, or split remains role-level")
    print("  J_sub is not a remainder current")
    print("  J_exch is not repair")
    print("  Sigma/R are not tuning knobs")
    print("  ordinary matter decoupling required")
    print("  M_ext neutrality required")
    print("  scalar trace neutrality required")
    print("  boundary neutrality required")
    with out.unresolved_obligations():
        out.line("current-split projection problem posed", StatusMark.OBLIGATION, "O_current not yet defined")


def case_1_inventory(entries: List[CurrentProjectionEntry]) -> None:
    header("Case 1: Current-split projection inventory")
    for entry in entries:
        print()
        print("-" * 120)
        print(entry.name)
        print("-" * 120)
        print(f"Candidate: {entry.candidate}")
        print(f"Role: {entry.role}")
        print(f"Allowed if: {entry.allowed_if}")
        print(f"Forbidden if: {entry.forbidden_if}")
        print(f"[{entry_status_mark(entry.status).value}] {entry.name}: {entry.status}")
        print(f"Missing: {entry.missing}")
        print(f"Consequence: {entry.consequence}")


def case_2_compact_table(entries: List[CurrentProjectionEntry], out: ScriptOutput) -> None:
    header("Case 2: Compact current-split ledger")
    print("| Entry | Candidate | Status | Consequence |")
    print("|---|---|---|---|")
    for entry in entries:
        print(f"| {entry.name} | {entry.candidate} | {entry.status} | {entry.consequence} |")
    with out.governance_assessments():
        out.line("compact current-split projection ledger produced", StatusMark.INFO, "current O remains theorem target")


def case_3_status_counts(entries: List[CurrentProjectionEntry], out: ScriptOutput) -> None:
    header("Case 3: Status counts")
    counts = {}
    for entry in entries:
        counts[entry.status] = counts.get(entry.status, 0) + 1
    for status in sorted(counts):
        print(f"{status}: {counts[status]}")
    print()
    print("Interpretation:")
    print("  O_current cannot make J_sub/J_exch operator-level until J_V and source sides exist.")
    print("  Zero-net and zero-creation ordinary-sector branches remain useful candidates.")
    print("  Remainder-current and repair-current projections are rejected.")
    with out.governance_assessments():
        out.line("current-split status count produced", StatusMark.INFO, str(counts))


def case_4_toy_split_check(out: ScriptOutput) -> None:
    header("Case 4: Toy current split check")
    j_sub, j_exch = sp.symbols("j_sub j_exch")
    j_vec = sp.Matrix([j_sub, j_exch])
    P_sub = sp.diag(1, 0)
    P_exch = sp.diag(0, 1)
    overlap = P_sub * P_exch * j_vec
    sum_split = P_sub * j_vec + P_exch * j_vec
    print("Toy role-level current vector:")
    print()
    print("  J_role = [J_sub, J_exch]^T")
    print()
    print(f"P_sub J_role = {P_sub * j_vec}")
    print(f"P_exch J_role = {P_exch * j_vec}")
    print(f"P_sub P_exch J_role = {overlap}")
    print(f"P_sub J_role + P_exch J_role = {sum_split}")
    print()
    print("Interpretation:")
    print("  A toy block split can label roles without overlap.")
    print("  It does not define physical J_V, J_sub, J_exch, Sigma/R, or boundary behavior.")
    with out.sample_results():
        out.line("toy current role split has zero algebraic overlap", StatusMark.PASS, "diagnostic role vector only")
    with out.governance_assessments():
        out.line("toy current split insufficient for O_current", StatusMark.DEFER, "physical currents and source sides missing")


def case_5_failure_controls(out: ScriptOutput) -> None:
    header("Case 5: Failure controls")
    print("Current-split projection fails if:")
    print()
    print("1. J_V is assumed defined.")
    print("2. J_sub is whatever remains after J_exch.")
    print("3. J_exch is repair current.")
    print("4. Sigma/R become tuning knobs.")
    print("5. J_sub/J_exch become ordinary matter channels.")
    print("6. current projection shifts M_ext.")
    print("7. current projection leaks scalar trace or boundary charge.")
    print("8. u_vac is normalized outside a timelike/nonzero J_V domain.")
    with out.counterexamples():
        out.line("remainder-current split rejected", StatusMark.FAIL, "no independent split criterion")
        out.line("repair-current projection rejected", StatusMark.FAIL, "current subspace cannot be selected after leakage")
        out.line("undefined J_V split rejected", StatusMark.FAIL, "projection cannot split undefined physical current")


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Current-split projection is not solved.")
    print()
    print("Allowed current status:")
    print()
    print("  J_V remains unresolved umbrella notation")
    print("  J_sub/J_exch remains role-level bookkeeping")
    print("  zero-net exchange branch remains candidate")
    print("  zero-creation ordinary-sector branch remains candidate")
    print("  u_vac remains domain-limited theorem target")
    print()
    print("Rejected:")
    print()
    print("  remainder-current split")
    print("  repair-current projection")
    print("  projection as definition of J_V or source sides")
    print()
    print("Missing before O_current can be real:")
    print()
    print("  physical J_V flux law")
    print("  J_sub/J_exch split criterion")
    print("  Sigma/R operators")
    print("  pure wind neutrality")
    print("  ordinary matter decoupling")
    print("  M_ext/scalar/boundary neutrality")
    print()
    print("Possible next artifact:")
    print("  candidate_current_split_projection_operator.md")
    print()
    print("Possible next script:")
    print("  candidate_projection_commutation_and_divergence.py")
    with out.governance_assessments():
        out.line("current-split O remains theorem target", StatusMark.DEFER, "J_sub/J_exch remains role-level")


def record_governance(ns) -> None:
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_O_current_20",
        script_id=SCRIPT_ID,
        title="Derive current-split projection operator",
        status=ObligationStatus.OPEN,
        required_by=["current_split_projection_route_20"],
        description="Define O_current with domain, kernel, image, current split criterion, and boundary behavior.",
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_J_V_flux_law_20",
        script_id=SCRIPT_ID,
        title="Derive physical J_V flux law",
        status=ObligationStatus.OPEN,
        required_by=["current_split_projection_route_20"],
        description="Define J_V as a physical flux/current before promoting any J_sub/J_exch split.",
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_J_sub_J_exch_split_criterion_20",
        script_id=SCRIPT_ID,
        title="Derive J_sub/J_exch split criterion",
        status=ObligationStatus.OPEN,
        required_by=["current_split_projection_route_20"],
        description="Show a non-remainder criterion distinguishing substrate current from exchange current.",
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_current_neutrality_theorems_20",
        script_id=SCRIPT_ID,
        title="Derive current neutrality theorems",
        status=ObligationStatus.OPEN,
        required_by=["current_split_projection_route_20"],
        description="Show pure wind neutrality, ordinary matter decoupling, M_ext neutrality, scalar neutrality, and boundary neutrality.",
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_Sigma_R_current_operators_20",
        script_id=SCRIPT_ID,
        title="Derive Sigma/R current operators",
        status=ObligationStatus.OPEN,
        required_by=["current_split_projection_route_20"],
        description="Define source and relaxation operators before treating J_exch as active exchange current.",
    ))

    ns.record_route(RouteRecord(
        route_id="current_split_projection_route_20",
        script_id=SCRIPT_ID,
        name="Current-split projection theorem route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=[
            "derive_O_current_20",
            "derive_J_V_flux_law_20",
            "derive_J_sub_J_exch_split_criterion_20",
            "derive_current_neutrality_theorems_20",
            "derive_Sigma_R_current_operators_20",
        ],
        activation_conditions=[
            "J_V is physically defined",
            "J_sub/J_exch split is non-remainder",
            "Sigma/R operators are defined",
            "ordinary matter, mass, scalar, and boundary neutrality are proved",
        ],
    ))
    ns.record_route(RouteRecord(
        route_id="role_level_current_split_route_20",
        script_id=SCRIPT_ID,
        name="Role-level current split fallback",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=[],
        activation_conditions=[
            "J_V remains unresolved",
            "J_sub/J_exch are bookkeeping labels only",
            "labels are not used as physical currents",
        ],
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_O_current_20",
        script_id=SCRIPT_ID,
        branch_id="current_split_projection_operator",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=[
            "derive_O_current_20",
            "derive_J_V_flux_law_20",
            "derive_J_sub_J_exch_split_criterion_20",
            "derive_current_neutrality_theorems_20",
            "derive_Sigma_R_current_operators_20",
        ],
        description="O_current remains deferred because J_V, J_sub/J_exch split criterion, Sigma/R, and neutrality theorems are missing.",
    ))
    for decision_id, branch_id, description in [
        (
            "reject_remainder_current_split_20",
            "remainder_current_split",
            "Reject J_sub or J_exch definition as the leftover after subtracting the other current.",
        ),
        (
            "reject_repair_current_projection_20",
            "repair_current_projection",
            "Reject current projection selected to cancel leakage, scalar charge, mass shift, or recovery mismatch.",
        ),
        (
            "reject_undefined_J_V_operator_split_20",
            "undefined_J_V_operator_split",
            "Reject operator-level split of J_V before J_V is physically defined.",
        ),
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=decision_id,
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            description=description,
        ))

    ns.record_claim(ClaimRecord(
        claim_id="current_split_projection_summary",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.HEURISTIC,
        statement=(
            "O_current cannot make J_sub/J_exch operator-level until J_V and source sides are defined. "
            "The current split remains role-level bookkeeping; zero-net and zero-creation ordinary-sector "
            "branches remain candidate safety routes."
        ),
        obligation_ids=[
            "derive_O_current_20",
            "derive_J_V_flux_law_20",
            "derive_J_sub_J_exch_split_criterion_20",
            "derive_current_neutrality_theorems_20",
            "derive_Sigma_R_current_operators_20",
        ],
    ))


def main():
    header("Candidate Current-Split Projection Operator")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    case_0_problem_statement(out)
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries, out)
    case_3_status_counts(entries, out)
    case_4_toy_split_check(out)
    case_5_failure_controls(out)
    final_interpretation(out)

    record_governance(ns)
    ns.record_derivation(
        derivation_id="current_split_projection_operator_marker",
        inputs=[],
        output=sp.Symbol("current_split_projection_operator_complete"),
        method="current_split_projection_operator",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
