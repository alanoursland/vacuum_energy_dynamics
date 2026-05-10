# Candidate differential A_spatial closure operator inventory
#
# Group:
#   14_kappa_zeta_map_and_projectors
#
# Script type:
#   INVENTORY
#
# Purpose
# -------
# The minimal A-constraint closure ansatz audit found the most local survivor:
#
#   C[A,A_spatial,S_A]
#     = alpha1 L1[A_spatial] + alpha2 L2[A] + alpha3 S_A = 0
#
# But this is only an ansatz shell.
#
# This script inventories possible L1/L2 operators and coefficient constraints
# to decide whether the differential compatibility branch is real or just
# GR in a mask.
#
# It is not a derivation.

from dataclasses import dataclass
from pathlib import Path
from typing import List

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    ClaimRecord,
    ClaimTier,
    GovernanceStatus,
    ObligationStatus,
    ProofObligationRecord,
    RecordKind,
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
class OperatorEntry:
    name: str
    operator: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def build_entries() -> List[OperatorEntry]:
    return [
        OperatorEntry(
            name="DO1: differential closure shell",
            operator="C = alpha1 L1[A_spatial] + alpha2 L2[A] + alpha3 S_A = 0",
            role="starting differential compatibility family",
            allowed_if="operators and coefficients are separately justified",
            forbidden_if="used as decorative notation for missing A_spatial equation",
            status="STRUCTURAL",
            missing="L1, L2, alpha constraints",
            consequence="branch remains open only if operator content is non-decorative",
        ),
        OperatorEntry(
            name="DO2: Laplacian-like L1 on A_spatial",
            operator="L1[A_spatial] = Delta A_spatial",
            role="minimal elliptic local operator for spatial companion",
            allowed_if="operator follows from non-radiative constraint structure",
            forbidden_if="chosen only because it reproduces Poisson/GR-like spatial response",
            status="CANDIDATE",
            missing="constraint/stiffness origin of L1",
            consequence="could make A_spatial elliptic and non-radiative",
        ),
        OperatorEntry(
            name="DO3: mass-source coupling through S_A",
            operator="alpha3 S_A[rho]",
            role="routes A-sector source into closure",
            allowed_if="source placement follows from same A constraint/source routing",
            forbidden_if="source coefficient is tuned to force gamma_like=1",
            status="CANDIDATE",
            missing="source normalization principle",
            consequence="determines whether gamma-like recovery is output or tuning",
        ),
        OperatorEntry(
            name="DO4: A-derivative L2 operator",
            operator="L2[A] = Delta A or radial compatibility derivative of A",
            role="couples lapse scalar response to spatial companion",
            allowed_if="operator is not equivalent to imposing B=1/A",
            forbidden_if="L2 secretly encodes Schwarzschild/AB relation",
            status="RISK",
            missing="non-GR compatibility origin",
            consequence="danger junction for GR smuggling",
        ),
        OperatorEntry(
            name="DO5: gradient-square nonlinear correction",
            operator="L2[A] includes |grad A|^2 or nonlinear derivative terms",
            role="possible nonlinear correction beyond weak field",
            allowed_if="coefficient derives from action/stiffness or closure",
            forbidden_if="term is chosen to match Schwarzschild expansion",
            status="CANDIDATE",
            missing="nonlinear coefficient origin",
            consequence="may be deferred until linear closure is understood",
        ),
        OperatorEntry(
            name="DO6: coefficient-origin constraint",
            operator="alpha1:alpha2:alpha3 fixed by identity, not fit",
            role="prevents gamma tuning",
            allowed_if="ratio follows from conservation/action/constraint closure",
            forbidden_if="ratio is selected to make gamma_like=1",
            status="REQUIRED",
            missing="coefficient principle",
            consequence="without this, differential closure is tuning not derivation",
        ),
        OperatorEntry(
            name="DO7: gamma-like weak-field check",
            operator="linearized closure output gives gamma_like=1",
            role="recovery test",
            allowed_if="emerges from operator/coefficient principle",
            forbidden_if="used to choose alpha ratios",
            status="RECOVERY_TARGET",
            missing="linearized solution of closure",
            consequence="tests closure after operator inventory",
        ),
        OperatorEntry(
            name="DO8: AB exterior diagnostic check",
            operator="exterior solution yields kappa_areal -> 0 / AB -> 1",
            role="reduced exterior recovery test",
            allowed_if="emerges from solved closure",
            forbidden_if="used as boundary condition or closure equation",
            status="RECOVERY_TARGET",
            missing="exterior solution and boundary data rule",
            consequence="keeps AB diagnostic-only",
        ),
        OperatorEntry(
            name="DO9: no-overlap operator",
            operator="O[A_spatial, trace_residual] = 0",
            role="ensures differential closure does not double-count zeta/kappa trace",
            allowed_if="O is defined or residual is killed/non-metric",
            forbidden_if="overlap=0 is asserted without operator or consequence",
            status="THEOREM_TARGET",
            missing="operator O or residual-kill theorem",
            consequence="decides whether zeta/kappa survive as metric residuals",
        ),
        OperatorEntry(
            name="DO10: zeta-dependent operator",
            operator="L2[A,zeta] or C[A,A_spatial,zeta]",
            role="possible volume-assisted compatibility",
            allowed_if="zeta becomes companion or residual by no-overlap identity",
            forbidden_if="zeta both supplies A_spatial and remains independent residual",
            status="RISK",
            missing="zeta role decision and accounting revision",
            consequence="may move branch from A-local to volume-exchange identity",
        ),
        OperatorEntry(
            name="DO11: GR shortcut collapse",
            operator="operator choice equivalent to B=1/A, copied GR metric, Einstein constraint, or tuned gamma",
            role="branch-kill detector",
            allowed_if="used as no-go diagnosis only",
            forbidden_if="accepted as closure",
            status="REJECTED",
            missing="not pursued",
            consequence="if all operator choices collapse here, differential branch dies",
        ),
        OperatorEntry(
            name="DO12: recommended operator test",
            operator="test linear elliptic L1/L2/source closure before nonlinear or zeta-assisted branches",
            role="least decorated local test",
            allowed_if="coefficient-origin and shortcut checks are explicit",
            forbidden_if="linear test is tuned to pass recovery targets",
            status="RECOMMENDED",
            missing="minimal linear operator closure script",
            consequence="next script should test linear closure algebra and branch-kill criteria",
        ),
    ]


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="minimal_A_constraint_closure_ansatz_marker",
        upstream_script_id="14_kappa_zeta_map_and_projectors__candidate_minimal_A_constraint_closure_ansatz",
        upstream_derivation_id="minimal_A_constraint_closure_ansatz_marker",
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


def print_entry(e: OperatorEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Operator: {e.operator}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    print(f"Status: {e.status}")
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement(out: ScriptOutput):
    header("Case 0: Differential A_spatial closure operator inventory problem")

    print("Question:")
    print()
    print("  What L1/L2 operators can make differential compatibility real rather than decorative?")
    print()
    print("Goal:")
    print()
    print("  inventory operator choices and expose coefficient / shortcut risks")
    print()
    print("Discipline:")
    print()
    print("  do not tune alpha ratios to gamma=1")
    print("  do not encode B=1/A in L2")
    print("  do not copy GR spatial metric")
    print("  do not assert overlap=0 without operator/consequence")
    print("  do not let zeta be both A_spatial companion and residual")
    print("  require branch-kill if all operators are shortcuts")

    with out.governance_assessments():
        out.line("differential operator inventory problem posed", StatusMark.WARN, "open risk")


def case_1_inventory(entries: List[OperatorEntry]):
    header("Case 1: Differential operator inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[OperatorEntry], out: ScriptOutput):
    header("Case 2: Compact differential-operator ledger")

    print("| Entry | Operator | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.operator.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    with out.governance_assessments():
        out.line("compact differential-operator ledger produced", StatusMark.WARN, "structural inventory")


def case_3_status_counts(entries: List[OperatorEntry], out: ScriptOutput):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  A linear elliptic closure is the least decorated local test.")
    print("  The danger is coefficient tuning: without alpha origin, gamma-like recovery is not derived.")
    print("  L2[A] is the GR-smuggling danger junction.")
    print("  Zeta-dependent operators likely leave the A-local branch and move toward volume-exchange identity.")

    with out.governance_assessments():
        out.line("differential-operator status count produced", StatusMark.WARN, "structural")


def case_4_minimal_linear_operator_test(out: ScriptOutput):
    header("Case 4: Minimal linear operator test")

    print("Least decorated test form:")
    print()
    print("  alpha1 Delta A_spatial + alpha2 Delta A + alpha3 S_A = 0")
    print()
    print("Using the A constraint:")
    print()
    print("  Delta A = S_A")
    print()
    print("This collapses to:")
    print()
    print("  alpha1 Delta A_spatial + (alpha2 + alpha3) S_A = 0")
    print()
    print("Therefore:")
    print()
    print("  Delta A_spatial = -((alpha2 + alpha3)/alpha1) S_A")
    print()
    print("Danger:")
    print("  choosing the ratio to recover gamma_like=1 is coefficient tuning unless alpha ratios are derived.")

    with out.governance_assessments():
        out.line("minimal linear operator test stated", StatusMark.WARN, "candidate closure form")


def case_5_branch_kill_or_defer(out: ScriptOutput):
    header("Case 5: Branch-kill or defer criteria")

    print("Kill or defer the differential branch if:")
    print()
    print("1. the only viable L1/L2 pair is Laplacian with tuned coefficient ratio")
    print("2. L2[A] encodes B=1/A or Schwarzschild expansion")
    print("3. source placement is chosen only to force gamma_like=1")
    print("4. overlap with zeta/kappa residual is unresolved")
    print("5. no coefficient-origin principle is available")
    print()
    print("If killed/deferred, move to:")
    print("  parent action/stiffness identity for coefficient origin,")
    print("  conservation/Bianchi-like identity for closure origin,")
    print("  or volume-exchange identity for zeta participation.")

    with out.governance_assessments():
        out.line("differential branch-kill/defer criteria stated", StatusMark.FAIL, "branch kill if operator choices all GR shortcuts")


def case_6_failure_controls(out: ScriptOutput):
    header("Case 6: Failure controls")

    print("Differential operator inventory fails if:")
    print()
    print("1. operator inventory pretends alpha ratios are derived")
    print("2. gamma_like=1 is used to pick coefficients")
    print("3. AB=1 appears inside L2 or boundary data")
    print("4. L1 is just copied from GR constraint form")
    print("5. nonlinear terms are tuned to Schwarzschild expansion")
    print("6. zeta-dependent closure keeps zeta as independent residual")
    print("7. no-overlap theorem is not represented")
    print("8. branch cannot be killed or deferred despite coefficient-origin failure")

    with out.governance_assessments():
        out.line("differential operator failure controls stated", StatusMark.WARN, "open risk")


def case_7_next_tests(out: ScriptOutput):
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_differential_A_spatial_closure_operator_inventory.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_linear_A_spatial_closure_coefficient_origin.py")
    print("   Test whether alpha ratios can be derived or whether the branch is tuning.")
    print()
    print("3. candidate_parent_action_stiffness_identity.py")
    print("   Move to action/stiffness for coefficient origin.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_linear_A_spatial_closure_coefficient_origin.py")
    print()
    print("Reason:")
    print("  The minimal linear closure reduces to a coefficient-ratio problem. Test whether that ratio can be derived, not fit.")

    with out.governance_assessments():
        out.line("next test selected", StatusMark.WARN, "structural guidance")


def final_interpretation():
    header("Final interpretation")

    print("The differential closure branch reduces quickly to coefficient origin.")
    print()
    print("Minimal form:")
    print("  alpha1 Delta A_spatial + alpha2 Delta A + alpha3 S_A = 0")
    print()
    print("With Delta A = S_A:")
    print("  Delta A_spatial = -((alpha2 + alpha3)/alpha1) S_A")
    print()
    print("This is useful only if the ratio is derived, not chosen.")
    print()
    print("Best next test:")
    print("  candidate_linear_A_spatial_closure_coefficient_origin.py")


def main():
    header("Candidate Differential A_spatial Closure Operator Inventory")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    case_0_problem_statement(out)
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries, out)
    case_3_status_counts(entries, out)
    case_4_minimal_linear_operator_test(out)
    case_5_branch_kill_or_defer(out)
    case_6_failure_controls(out)
    case_7_next_tests(out)
    final_interpretation()

    with archive.with_project_namespace(SCRIPT_ID) as ns:

        ns.record_obligation(ProofObligationRecord(
            obligation_id="derive_L1_L2_operator_origin_for_differential_closure_in_14",
            script_id=SCRIPT_ID,
            title="Derive L1/L2 operator origin for differential closure",
            status=ObligationStatus.OPEN,
            description=(
                "The differential compatibility family requires non-decorative operators L1[A_spatial] "
                "and L2[A] with a coefficient ratio alpha1:alpha2:alpha3 that is derived before gamma "
                "recovery checks. The minimal elliptic form (Laplacian L1, Laplacian L2) is a structural "
                "candidate but its coefficient ratio remains free. L2[A] is a GR-smuggling danger junction "
                "if it encodes B=1/A or Schwarzschild expansion."
            ),
        ))

        ns.record_claim(ClaimRecord(
            claim_id="differential_closure_operator_inventory_provisional",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.PROVISIONAL_CONVENTION,
            statement=(
                "The differential closure branch survives only if L1, L2 operators and coefficient ratio "
                "q = -(alpha2+alpha3)/alpha1 are derived without gamma/AB recovery targets. "
                "The minimal Laplacian form is a provisional structural candidate. "
                "The branch must defer to action/stiffness or conservation identity if q cannot be derived locally."
            ),
        ))

        ns.record_derivation(
            derivation_id="differential_A_spatial_closure_operator_inventory_marker",
            inputs=[],
            output=sp.Symbol("differential_A_spatial_closure_operator_inventory_audited"),
            method="differential_A_spatial_closure_operator_inventory_audit",
            status=Status.DERIVED,
            record_kind=RecordKind.INVENTORY_MARKER,
            is_placeholder=True,
        )

        ns.write_run_metadata()


if __name__ == "__main__":
    main()
