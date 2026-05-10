# Candidate minimal A-constraint closure ansatz
#
# Group:
#   14_kappa_zeta_map_and_projectors
#
# Script type:
#   SAMPLE
#
# Purpose
# -------
# The minimal A-constraint closure/no-go audit found:
#
#   The A-sector-local propagation branch now has a sharp test:
#
#     write an explicit non-GR closure ansatz,
#     or kill the branch.
#
# Surviving closure form families:
#
#   differential compatibility,
#   conservation-current closure,
#   elliptic compatibility,
#   zeta-assisted closure with no-overlap.
#
# This script writes minimal symbolic ansatz families and classifies which are
# real tests versus renamed missing equations.
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
class ClosureAnsatzEntry:
    name: str
    ansatz: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def build_entries() -> List[ClosureAnsatzEntry]:
    return [
        ClosureAnsatzEntry(
            name="CA1: starting A constraint",
            ansatz="Delta_A A = S_A[rho]",
            role="reduced scalar mass-response constraint",
            allowed_if="treated as starting constraint only",
            forbidden_if="claimed to derive A_spatial alone",
            status="STRUCTURAL",
            missing="parent embedding and companion closure",
            consequence="A remains strong but incomplete",
        ),
        ClosureAnsatzEntry(
            name="CA2: algebraic closure ansatz",
            ansatz="A_spatial = F(A)",
            role="minimal closure shell",
            allowed_if="F is derived later from a parent principle",
            forbidden_if="F is chosen as GR spatial metric, B=1/A, or gamma tuning",
            status="RISK",
            missing="non-GR derivation of F",
            consequence="as-is, algebraic closure is too easy to smuggle GR",
        ),
        ClosureAnsatzEntry(
            name="CA3: differential compatibility ansatz",
            ansatz="C[A,A_spatial,S_A] = alpha1 L1[A_spatial] + alpha2 L2[A] + alpha3 S_A = 0",
            role="explicit local compatibility family",
            allowed_if="operators L1/L2 are defined independently of GR metric copying",
            forbidden_if="coefficients are selected to force gamma=1",
            status="CANDIDATE",
            missing="operator definitions and coefficient principle",
            consequence="best local closure family if coefficients/operators can be justified",
        ),
        ClosureAnsatzEntry(
            name="CA4: conservation-current ansatz",
            ansatz="div J_A = 0, J_A = J_A[A,A_spatial,T]",
            role="closure via source/current consistency",
            allowed_if="J_A is specified and links A to spatial companion",
            forbidden_if="div J_A=0 is decorative with no current",
            status="CANDIDATE",
            missing="current definition and conservation law",
            consequence="bridges toward conservation/Bianchi-like parent identity",
        ),
        ClosureAnsatzEntry(
            name="CA5: elliptic compatibility ansatz",
            ansatz="L_spatial[A_spatial] = H[A,S_A]",
            role="non-radiative boundary-value closure",
            allowed_if="L_spatial and H are specified and boundary data do not impose GR",
            forbidden_if="boundary data are Schwarzschild/AB=1 in disguise",
            status="CANDIDATE",
            missing="elliptic operator, source functional, admissible boundary data",
            consequence="could derive static spatial companion without scalar wave channel",
        ),
        ClosureAnsatzEntry(
            name="CA6: zeta-assisted closure ansatz",
            ansatz="C[A,A_spatial,zeta] = 0 with overlap(A_spatial,zeta_residual)=0",
            role="ontology-native closure using vacuum-volume configuration",
            allowed_if="zeta is either A_spatial companion or residual, not both",
            forbidden_if="zeta patches A_spatial while remaining independent residual trace",
            status="RISK",
            missing="zeta-A_spatial map and accounting revision",
            consequence="may force zeta convention revision or kill residual trace",
        ),
        ClosureAnsatzEntry(
            name="CA7: no-overlap operator requirement",
            ansatz="O[A_spatial, zeta/kappa_residual] = 0",
            role="prevents closure from double-counting scalar trace",
            allowed_if="O is defined or residual is proven zero/non-metric",
            forbidden_if="overlap condition is asserted without operator",
            status="THEOREM_TARGET",
            missing="overlap operator O",
            consequence="decides whether zeta/kappa survive as metric residuals",
        ),
        ClosureAnsatzEntry(
            name="CA8: gamma-like recovery test",
            ansatz="weak-field output satisfies gamma_like = 1",
            role="recovery check",
            allowed_if="emerges from closure ansatz",
            forbidden_if="used to choose alpha coefficients",
            status="RECOVERY_TARGET",
            missing="weak-field expansion",
            consequence="tests but does not construct the ansatz",
        ),
        ClosureAnsatzEntry(
            name="CA9: AB diagnostic test",
            ansatz="exterior output satisfies kappa_areal -> 0, AB -> 1",
            role="reduced exterior recovery check",
            allowed_if="emerges from exterior solution",
            forbidden_if="used as closure equation",
            status="RECOVERY_TARGET",
            missing="exterior solution from ansatz",
            consequence="keeps AB as diagnostic only",
        ),
        ClosureAnsatzEntry(
            name="CA10: shortcut collapse",
            ansatz="ansatz reduces to B=1/A, GR metric, Einstein constraint, or tuned gamma",
            role="branch-kill detector",
            allowed_if="used only as no-go diagnosis",
            forbidden_if="accepted as closure",
            status="REJECTED",
            missing="not pursued",
            consequence="if all ansatz families collapse here, local branch is killed",
        ),
        ClosureAnsatzEntry(
            name="CA11: local branch killed",
            ansatz="no explicit C, J_A, L_spatial, or zeta-assisted ansatz survives shortcut tests",
            role="good failure outcome",
            allowed_if="moves search to action/stiffness or broader parent identity",
            forbidden_if="patched with GR import",
            status="BRANCH_KILLED",
            missing="ansatz test result",
            consequence="kills A-sector-local closure route if confirmed",
        ),
        ClosureAnsatzEntry(
            name="CA12: recommended next test",
            ansatz="test differential compatibility family C first",
            role="most local explicit closure attempt",
            allowed_if="operators/coefficient roles are exposed",
            forbidden_if="C only renames A_spatial equation",
            status="RECOMMENDED",
            missing="minimal differential operator inventory",
            consequence="next script should inventory allowed L1/L2 operators and coefficient constraints",
        ),
    ]


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="minimal_A_constraint_closure_no_go_marker",
        upstream_script_id="14_kappa_zeta_map_and_projectors__candidate_minimal_A_constraint_closure_no_go",
        upstream_derivation_id="minimal_A_constraint_closure_no_go_marker",
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


def print_entry(e: ClosureAnsatzEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Ansatz: {e.ansatz}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    print(f"Status: {e.status}")
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement(out: ScriptOutput):
    header("Case 0: Minimal A-constraint closure ansatz problem")

    print("Question:")
    print()
    print("  Can explicit symbolic closure ansatz families be written without collapsing to GR shortcuts?")
    print()
    print("Goal:")
    print()
    print("  expose closure forms C, J_A, L_spatial, and zeta-assisted closure")
    print("  enough to choose the next concrete test or kill the branch")
    print()
    print("Discipline:")
    print()
    print("  do not hide missing equations behind symbols")
    print("  do not tune coefficients to gamma=1")
    print("  do not use AB=1 as closure")
    print("  do not impose GR boundary data")
    print("  do not let zeta be both companion and residual")
    print("  require branch-kill criteria")

    with out.governance_assessments():
        out.line("minimal A-constraint closure ansatz problem posed", StatusMark.WARN, "open risk")


def case_1_inventory(entries: List[ClosureAnsatzEntry]):
    header("Case 1: Minimal closure ansatz inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[ClosureAnsatzEntry], out: ScriptOutput):
    header("Case 2: Compact closure-ansatz ledger")

    print("| Entry | Ansatz | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.ansatz.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    with out.governance_assessments():
        out.line("compact closure-ansatz ledger produced", StatusMark.WARN, "structural inventory")


def case_3_status_counts(entries: List[ClosureAnsatzEntry], out: ScriptOutput):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Explicit ansatz families can be written, but none is derived yet.")
    print("  Differential compatibility is the most local next test.")
    print("  Conservation-current closure may be broader than the A-local branch.")
    print("  Zeta-assisted closure is risky because it may erase independent residual status.")
    print("  If all explicit ansatz families require shortcuts, kill the local branch.")

    with out.governance_assessments():
        out.line("closure-ansatz status count produced", StatusMark.WARN, "structural")


def case_4_ansatz_sample(ns) -> None:
    header("Case 4: Ansatz family shapes (sample derivation)")

    print("Surviving symbolic families:")
    print()
    print("1. Differential compatibility:")
    print("   alpha1 L1[A_spatial] + alpha2 L2[A] + alpha3 S_A = 0")
    print()
    print("2. Conservation-current:")
    print("   div J_A[A,A_spatial,T] = 0")
    print()
    print("3. Elliptic compatibility:")
    print("   L_spatial[A_spatial] = H[A,S_A]")
    print()
    print("4. Zeta-assisted:")
    print("   C[A,A_spatial,zeta] = 0")
    print("   overlap(A_spatial,zeta_residual) = 0")
    print()
    print("All are provisional ansatz shells, not derived equations.")
    print()
    print("Minimal differential compatibility collapse (sample):")

    alpha1, alpha2, alpha3 = sp.symbols("alpha1 alpha2 alpha3", nonzero=True)
    S_A = sp.Symbol("S_A")
    # With Delta A = S_A the differential family collapses to:
    # alpha1 Delta A_spatial + (alpha2 + alpha3) S_A = 0
    # => Delta A_spatial = q S_A
    q_ansatz = sp.simplify(-(alpha2 + alpha3) / alpha1)

    print(f"  With Delta A = S_A: Delta A_spatial = q S_A,  q = {q_ansatz}")
    print()
    print("  This is an ansatz form for the coefficient ratio, not a derivation.")

    ns.record_derivation(
        derivation_id="minimal_A_closure_ansatz_differential_family_sample",
        inputs=[alpha1, alpha2, alpha3, S_A],
        output=q_ansatz,
        method="differential compatibility ansatz collapse to coefficient ratio",
        status=Status.DERIVED,
        record_kind=RecordKind.SAMPLE_DERIVATION,
        scope="ansatz sample only, not a derived closure law",
    )


def case_5_differential_next_requirements(out: ScriptOutput):
    header("Case 5: Differential compatibility next requirements")

    print("To test the differential compatibility family next, define:")
    print()
    print("1. allowed operators L1 on A_spatial")
    print("2. allowed operators L2 on A")
    print("3. source placement S_A")
    print("4. coefficient origin / stiffness relation")
    print("5. weak-field output gamma_like")
    print("6. exterior AB diagnostic")
    print("7. no-overlap with residual trace")
    print("8. branch-kill shortcut checks")
    print()
    print("If L1/L2/coefficient choices only reproduce GR by hand, kill or defer to action/stiffness route.")

    with out.unresolved_obligations():
        out.line("derive differential closure operators L1/L2 and coefficient origin", StatusMark.OBLIGATION, "open proof obligation recorded")


def case_6_failure_controls(out: ScriptOutput):
    header("Case 6: Failure controls")

    print("Closure ansatz test fails if:")
    print()
    print("1. C, J_A, or L_spatial are just names for missing equations")
    print("2. F[A] is secretly B=1/A")
    print("3. coefficients are selected to force gamma=1")
    print("4. elliptic boundary data impose Schwarzschild")
    print("5. current conservation has no current")
    print("6. zeta supplies A_spatial and remains independent residual")
    print("7. overlap operator is absent")
    print("8. no branch-kill outcome is allowed")

    with out.governance_assessments():
        out.line("closure-ansatz failure controls stated", StatusMark.WARN, "open risk")


def case_7_next_tests(out: ScriptOutput):
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_minimal_A_constraint_closure_ansatz.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_differential_A_spatial_closure_operator_inventory.py")
    print("   Inventory allowed L1/L2 operators for differential compatibility.")
    print()
    print("3. candidate_parent_action_stiffness_identity.py")
    print("   Move to action/stiffness if operator inventory collapses to coefficient tuning.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_differential_A_spatial_closure_operator_inventory.py")
    print()
    print("Reason:")
    print("  Differential compatibility is the most local explicit ansatz. Test its operator content next.")

    with out.governance_assessments():
        out.line("next test selected", StatusMark.WARN, "structural guidance")


def final_interpretation():
    header("Final interpretation")

    print("Explicit closure ansatz shells can be written.")
    print()
    print("The most local survivor is:")
    print("  C[A,A_spatial,S_A] = alpha1 L1[A_spatial] + alpha2 L2[A] + alpha3 S_A = 0")
    print()
    print("But it is not yet a derivation.")
    print()
    print("Best next test:")
    print("  candidate_differential_A_spatial_closure_operator_inventory.py")


def main():
    header("Candidate Minimal A-Constraint Closure Ansatz")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    case_0_problem_statement(out)
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries, out)
    case_3_status_counts(entries, out)
    case_4_ansatz_sample(ns)
    case_5_differential_next_requirements(out)
    case_6_failure_controls(out)
    case_7_next_tests(out)
    final_interpretation()

    if True:

        ns.record_obligation(ProofObligationRecord(
            obligation_id="derive_differential_closure_operators_and_coefficient_origin_in_14",
            script_id=SCRIPT_ID,
            title="Derive differential closure operators L1/L2 and coefficient origin",
            status=ObligationStatus.OPEN,
            description=(
                "The differential compatibility ansatz C[A,A_spatial,S_A] = alpha1 L1[A_spatial] "
                "+ alpha2 L2[A] + alpha3 S_A = 0 collapses to Delta A_spatial = q S_A. "
                "The operators L1, L2 and the coefficient ratio q = -(alpha2+alpha3)/alpha1 must be "
                "derived before gamma recovery checks. No local pre-recovery principle for q is known."
            ),
        ))

        ns.record_claim(ClaimRecord(
            claim_id="minimal_closure_ansatz_families_provisional",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.PROVISIONAL_CONVENTION,
            statement=(
                "Four closure ansatz families survive GR-shortcut rejection: differential compatibility, "
                "conservation-current, elliptic compatibility, and zeta-assisted closure. "
                "All are provisional ansatz shells. None is derived. The most local next test is "
                "differential compatibility with explicit L1/L2 operator inventory."
            ),
        ))

        ns.record_derivation(
            derivation_id="minimal_A_constraint_closure_ansatz_marker",
            inputs=[],
            output=sp.Symbol("minimal_A_constraint_closure_ansatz_audited"),
            method="minimal_A_constraint_closure_ansatz_audit",
            status=Status.DERIVED,
            record_kind=RecordKind.INVENTORY_MARKER,
            is_placeholder=True,
        )

        ns.write_run_metadata()


if __name__ == "__main__":
    main()
