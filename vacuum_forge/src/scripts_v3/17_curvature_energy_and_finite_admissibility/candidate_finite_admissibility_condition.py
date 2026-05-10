# Candidate finite admissibility condition
#
# Group:
#   17_curvature_energy_and_finite_admissibility
#
# Script type:
#   SIEVE
#
# Purpose
# -------
# The curvature admissibility object inventory found:
#
#   Diagnostic scalar and finite-admissibility inequality are safest starting points.
#   Curvature energy is risky unless fenced as diagnostic/accounting only.
#   J_curv remains theorem target until domain, direction, balance, and boundary behavior are defined.
#
# This script defines what "finite admissibility" could mean as a condition,
# without merely declaring singularities inadmissible.
#
# Locked-door question:
#
#   What does finite admissibility mean as a condition,
#   without merely declaring singularities inadmissible?
#
# This is a condition inventory, not an anti-singularity theorem.


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
    ProofObligationRecord,
    ObligationStatus,
    RecordKind,
    ScriptOutput,
)


ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def status_line(label: str, status: str, detail: str = "") -> ScriptOutput:
    marks = {
        "DERIVED_REDUCED": "PASS",
        "SAFE_IF": "WARN",
        "CANDIDATE": "WARN",
        "STRUCTURAL": "WARN",
        "CONSTRAINED": "WARN",
        "RECOMMENDED": "PASS",
        "REQUIRED": "WARN",
        "MISSING": "FAIL",
        "UNRESOLVED": "FAIL",
        "RISK": "WARN",
        "FORBIDDEN": "PASS",
        "REJECTED": "WARN",
        "DANGER": "FAIL",
        "THEOREM_TARGET": "WARN",
        "RECOVERY_TARGET": "WARN",
        "BRANCH_KILLED": "FAIL",
        "DEFER": "WARN",
        "CLOSED": "PASS",
    }
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")
    return ScriptOutput(label=label, status=mark, detail=detail or status)


@dataclass
class FiniteAdmissibilityEntry:
    name: str
    condition: str
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
        dependency_id="curvature_admissibility_object_inventory_marker",
        upstream_script_id="17_curvature_energy_and_finite_admissibility__candidate_curvature_admissibility_object_inventory",
        upstream_derivation_id="curvature_admissibility_object_inventory_marker",
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


def build_entries() -> List[FiniteAdmissibilityEntry]:
    return [
        FiniteAdmissibilityEntry(
            name="FA1: finite-admissibility target",
            condition="A_curv[g, matter, vacuum] < infinity or <= A_max on defined domain",
            role="core finite-admissibility theorem target",
            allowed_if="condition is stated before solutions and has domain, measure, and branch-kill rule",
            forbidden_if="condition is introduced only to reject singular solutions after the fact",
            status="THEOREM_TARGET",
            missing="definition of A_curv, domain, measure, threshold",
            consequence="turns anti-singularity language into a testable branch condition",
        ),
        FiniteAdmissibilityEntry(
            name="FA2: bounded scalar invariant",
            condition="I_curv(x) finite everywhere in admissible domain",
            role="local diagnostic condition",
            allowed_if="I_curv is specified and not chosen only because a target solution passes",
            forbidden_if="scalar is selected after solution to avoid a blowup",
            status="CANDIDATE",
            missing="choice of invariant and admissible domain",
            consequence="supports diagnostic or branch-filter claim, not dynamics alone",
        ),
        FiniteAdmissibilityEntry(
            name="FA3: bounded invariant set",
            condition="{K, R, R_mu_nu R^mu_nu, Weyl^2, ...} finite or controlled",
            role="multi-scalar diagnostic condition",
            allowed_if="set is defined structurally and coordinate/gauge safe",
            forbidden_if="set omits known divergent invariant to pass target solution",
            status="CANDIDATE",
            missing="minimal invariant set",
            consequence="stronger diagnostic than single scalar but still not dynamics",
        ),
        FiniteAdmissibilityEntry(
            name="FA4: integrable curvature",
            condition="Integral_D I_curv dV_phys < infinity",
            role="finite total curvature/admissibility measure",
            allowed_if="D and dV_phys are structural and cutoff-free",
            forbidden_if="domain cutoff hides singularity or boundary divergence",
            status="CANDIDATE",
            missing="I_curv, D, measure, cutoff-free criterion",
            consequence="may allow localized high curvature if total admissibility remains finite",
        ),
        FiniteAdmissibilityEntry(
            name="FA5: bounded curvature energy diagnostic",
            condition="Integral_D e_curv dV_phys finite, with e_curv diagnostic/accounting only",
            role="curvature energy admissibility candidate",
            allowed_if="e_curv is not a source reservoir and does not shift M_ext",
            forbidden_if="e_curv is used as bounce energy or tuning source",
            status="RISK",
            missing="e_curv definition and accounting fence",
            consequence="useful only if fenced before source role",
        ),
        FiniteAdmissibilityEntry(
            name="FA6: finite curvature flux",
            condition="Integral_boundary J_curv . dSigma finite or zero under defined orientation",
            role="current/boundary admissibility candidate",
            allowed_if="J_curv is defined independently with orientation and boundary law",
            forbidden_if="flux is chosen to cancel blowup or boundary leakage",
            status="THEOREM_TARGET",
            missing="J_curv, orientation, boundary law",
            consequence="needed before current-based anti-singularity claims",
        ),
        FiniteAdmissibilityEntry(
            name="FA7: finite volume response",
            condition="zeta / volume response remains finite and count-once",
            role="curvature-volume bridge candidate",
            allowed_if="does not reopen B_s insertion, residual trace, or no-overlap issues",
            forbidden_if="zeta becomes hidden scalar source or repair channel",
            status="RISK",
            missing="relation to zeta, B_s, O, and boundary neutrality",
            consequence="promising but dangerous because metric insertion remains theorem target",
        ),
        FiniteAdmissibilityEntry(
            name="FA8: finite parent correction target",
            condition="future H_curv finite and divergence-safe if introduced",
            role="future parent-correction constraint",
            allowed_if="kept deferred until admissibility/J_curv source structure exists",
            forbidden_if="H_curv introduced to enforce finite admissibility now",
            status="DEFER",
            missing="H_curv source/divergence structure",
            consequence="sets future Group 19 burden without introducing H_curv early",
        ),
        FiniteAdmissibilityEntry(
            name="FA9: geodesic completeness proxy",
            condition="diagnostic proxy flags incomplete curves or trapped finite-admissibility failure",
            role="claim classifier",
            allowed_if="kept diagnostic unless linked to equations",
            forbidden_if="used to claim dynamical singularity avoidance",
            status="SAFE_IF",
            missing="link to equations / evolution theorem",
            consequence="useful for claim audit, not current dynamics",
        ),
        FiniteAdmissibilityEntry(
            name="FA10: branch-kill rule",
            condition="if finite-admissibility condition fails, branch is excluded from candidate solution class",
            role="honest consequence rule",
            allowed_if="condition is stated before branch is tested",
            forbidden_if="branch-kill applied selectively to unwanted solutions",
            status="REQUIRED",
            missing="formal branch-kill criterion",
            consequence="makes finite admissibility operational",
        ),
        FiniteAdmissibilityEntry(
            name="FA11: no boundary hiding",
            condition="finite admissibility cannot be restored by boundary counterterm, cutoff, or surface repair",
            role="boundary safety guard",
            allowed_if="boundary terms are diagnostic or structurally neutral",
            forbidden_if="boundary term hides divergence or mass shift",
            status="REQUIRED",
            missing="boundary neutrality theorem",
            consequence="prevents finite condition from becoming boundary patch",
        ),
        FiniteAdmissibilityEntry(
            name="FA12: no exterior mass shift",
            condition="finite-admissibility object does not alter M_ext independently of A-sector",
            role="mass neutrality guard",
            allowed_if="curvature admissibility remains diagnostic or coupled through derived source law",
            forbidden_if="admissibility changes measured exterior mass as repair",
            status="REQUIRED",
            missing="mass neutrality theorem",
            consequence="protects strongest reduced A-sector result",
        ),
        FiniteAdmissibilityEntry(
            name="FA13: no ordinary matter rerouting",
            condition="finite-admissibility condition does not change ordinary matter coupling without source theorem",
            role="ordinary matter decoupling guard",
            allowed_if="T_mu_nu is not double-counted or modified",
            forbidden_if="matter coupling is altered to avoid singular behavior",
            status="REQUIRED",
            missing="source separation theorem",
            consequence="prevents finite admissibility from becoming matter repair",
        ),
        FiniteAdmissibilityEntry(
            name="FA14: no anti-singularity by declaration",
            condition="singularities are not simply declared inadmissible without object/condition",
            role="overclaim rejection",
            allowed_if="claim follows object support level",
            forbidden_if="condition is slogan rather than functional/inequality",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents magic anti-singularity claim",
        ),
        FiniteAdmissibilityEntry(
            name="FA15: no solution-after-the-fact selection",
            condition="admissibility functional is not chosen after seeing target solution behavior",
            role="selection-bias guard",
            allowed_if="functional precedes solution test",
            forbidden_if="functional is tailored to pass/fail preferred solutions",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents diagnostic cherry-picking",
        ),
        FiniteAdmissibilityEntry(
            name="FA16: no curvature energy reservoir",
            condition="finite energy bound does not provide free positive/negative source",
            role="source-reservoir rejection",
            allowed_if="energy remains diagnostic/accounting only",
            forbidden_if="used to tune bounce, mass, boundary, or recovery",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents curvature energy from becoming repair money",
        ),
        FiniteAdmissibilityEntry(
            name="FA17: admissibility claim level",
            condition="diagnostic condition licenses diagnostic/branch-filter claim only; dynamics require evolution law",
            role="anti-overclaim guard",
            allowed_if="claim strength matches object strength",
            forbidden_if="bounce/regular core claimed from diagnostic condition",
            status="REQUIRED",
            missing="claim audit",
            consequence="keeps anti-singularity claims honest",
        ),
        FiniteAdmissibilityEntry(
            name="FA18: recommended next move",
            condition="test curvature energy density role only after finite-admissibility condition is fenced",
            role="next local bottleneck",
            allowed_if="finite condition remains diagnostic/branch-filter",
            forbidden_if="jumping directly to J_curv or H_curv",
            status="RECOMMENDED",
            missing="curvature energy role audit",
            consequence="next script should be candidate_curvature_energy_density_role.py",
        ),
    ]


def print_entry(e: FiniteAdmissibilityEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Condition: {e.condition}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: Finite-admissibility condition problem")

    print("Question:")
    print()
    print("  What does finite admissibility mean as a condition,")
    print("  without merely declaring singularities inadmissible?")
    print()
    print("Goal:")
    print()
    print("  turn anti-singularity language into a branch condition / theorem target")
    print()
    print("Discipline:")
    print()
    print("  condition before solution selection")
    print("  no boundary hiding")
    print("  no M_ext shift")
    print("  no matter rerouting")
    print("  no curvature energy reservoir")
    print("  no bounce or regular-core claim from diagnostic only")

    status_line("finite-admissibility condition problem posed", "REQUIRED")


def case_1_inventory(entries: List[FiniteAdmissibilityEntry]):
    header("Case 1: Finite-admissibility condition inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[FiniteAdmissibilityEntry]):
    header("Case 2: Compact finite-admissibility ledger")

    print("| Entry | Condition | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.condition.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    status_line("compact finite-admissibility ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[FiniteAdmissibilityEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Finite admissibility can be stated as a theorem target or branch filter.")
    print("  Bounded scalar and integrable curvature are the safest candidate conditions.")
    print("  Curvature energy and volume response remain risky until fenced.")
    print("  J_curv flux and H_curv remain deferred/theorem-targeted.")
    print("  Anti-singularity remains diagnostic/branch-filter only unless dynamics are later derived.")
    print("  Next gate is curvature energy role, fenced as diagnostic/accounting.")

    status_line("finite-admissibility condition status count produced", "STRUCTURAL")


def case_4_condition_classes():
    header("Case 4: Finite-admissibility condition classes")

    print("Candidate condition classes:")
    print()
    print("1. bounded local curvature scalar")
    print("2. bounded invariant set")
    print("3. integrable curvature measure")
    print("4. bounded curvature energy diagnostic")
    print("5. finite curvature flux")
    print("6. finite volume response")
    print("7. finite parent correction target")
    print("8. geodesic completeness proxy")
    print()
    print("Safe starting point:")
    print()
    print("  bounded diagnostic or integrable measure")
    print()
    print("Dangerous starting point:")
    print()
    print("  curvature energy as source or current as repair")

    status_line("finite-admissibility condition classes listed", "RECOMMENDED")


def case_4b_sample_integrable_measure(ns):
    header("Case 4b: Sample integrable curvature measure")

    r, alpha = sp.symbols("r alpha", positive=True)
    integrand = 4 * sp.pi * r**2 * alpha / (1 + r**2) ** 3
    total_measure = sp.simplify(sp.integrate(integrand, (r, 0, sp.oo)))

    print(f"Sample radial density = alpha / (1 + r^2)^3")
    print(f"3D measure integrand = {integrand}")
    print(f"Integral_0^inf 4*pi*r^2*alpha/(1+r^2)^3 dr = {total_measure}")

    if total_measure == sp.pi**2 * alpha / 4:
        status_line(
            "sample integrable curvature measure",
            "DERIVED_REDUCED",
            f"Integral_D I_curv dV_phys = {total_measure}",
        )
    else:
        status_line("sample integrable curvature measure", "RISK", "unexpected sample integral result")

    ns.record_derivation(
        derivation_id="finite_admissibility_sample_integrable_measure",
        inputs=[integrand],
        output=total_measure,
        method="symbolic sample integrability check",
        status=Status.DERIVED,
    )


def case_5_decision_tree():
    header("Case 5: Finite-admissibility decision tree")

    print("Decision tree:")
    print()
    print("1. Bounded scalar / invariant set:")
    print("   safest diagnostic condition.")
    print()
    print("2. Integrable curvature:")
    print("   promising if domain/measure are fixed and cutoff-free.")
    print()
    print("3. Curvature energy:")
    print("   only diagnostic/accounting for now.")
    print()
    print("4. J_curv flux:")
    print("   theorem target until J_curv exists.")
    print()
    print("5. H_curv finite:")
    print("   deferred until parent correction audit.")
    print()
    print("6. Anti-singularity claim:")
    print("   cannot exceed diagnostic/branch-filter level yet.")

    status_line("finite-admissibility decision tree stated", "RECOMMENDED")


def case_6_good_failure():
    header("Case 6: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  finite admissibility can only be stated as diagnostic / branch-filter.")
    print()
    print("Consequence:")
    print()
    print("  no dynamical avoidance, bounce, or regular core claim is licensed.")
    print("  J_curv and e_curv remain future theorem targets.")
    print()
    print("Bad failure:")
    print()
    print("  declare singularities inadmissible without a functional, measure, or branch-kill rule.")

    status_line("finite-admissibility good failure stated", "DEFER")


def case_7_failure_controls():
    header("Case 7: Failure controls")

    print("Finite-admissibility condition fails if:")
    print()
    print("1. condition is chosen after solution behavior")
    print("2. divergent region is removed by cutoff")
    print("3. boundary term hides blowup")
    print("4. M_ext shifts independently of A")
    print("5. ordinary matter coupling is modified")
    print("6. e_curv becomes source reservoir")
    print("7. J_curv flux is invoked before J_curv exists")
    print("8. bounce or regular core is claimed from diagnostic condition only")

    status_line("finite-admissibility failure controls stated", "RISK")


def case_8_next_tests():
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_finite_admissibility_condition.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_curvature_energy_density_role.py")
    print("   Fence curvature energy as diagnostic/accounting before any current/source role.")
    print()
    print("3. candidate_curvature_admissibility_early_status_summary.py")
    print("   Use if finite admissibility cannot be stated non-decoratively.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_curvature_energy_density_role.py")
    print()
    print("Reason:")
    print("  Once finite admissibility is fenced as a condition, the next risk is")
    print("  curvature energy becoming a hidden source reservoir.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("Finite admissibility can currently be stated only as a theorem target / branch filter.")
    print()
    print("Safest candidate forms:")
    print()
    print("  bounded scalar diagnostic")
    print("  bounded invariant set")
    print("  integrable curvature measure")
    print()
    print("Still not licensed:")
    print()
    print("  dynamical singularity avoidance")
    print("  bounce")
    print("  regular core")
    print("  curvature current")
    print("  curvature source energy")
    print()
    print("Best next script:")
    print()
    print("  candidate_curvature_energy_density_role.py")

    status_line("finite-admissibility condition audit complete", "CLOSED")


def main():
    header("Candidate Finite Admissibility Condition")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_condition_classes()
    case_4b_sample_integrable_measure(ns)
    case_5_decision_tree()
    case_6_good_failure()
    case_7_failure_controls()
    case_8_next_tests()
    final_interpretation()

    with archive:
        ns.record_obligation(ProofObligationRecord(
            obligation_id="formalize_A_curv_condition_in_17_finite_admissibility",
            script_id=SCRIPT_ID,
            title="Formalize finite-admissibility condition A_curv",
            status=ObligationStatus.OPEN,
            description="A_curv must be stated with domain, measure, invariant/function, and branch-kill rule before anti-singularity claims can become technical.",
        ))
        ns.record_obligation(ProofObligationRecord(
            obligation_id="formalize_branch_kill_rule_in_17_finite_admissibility",
            script_id=SCRIPT_ID,
            title="Formalize branch-kill rule for finite admissibility",
            status=ObligationStatus.OPEN,
            description="If the finite-admissibility condition fails, branches must be excluded from the candidate solution class before solutions are tested.",
        ))
        ns.record_obligation(ProofObligationRecord(
            obligation_id="prove_boundary_neutrality_in_17_finite_admissibility",
            script_id=SCRIPT_ID,
            title="Prove boundary neutrality for finite admissibility",
            status=ObligationStatus.OPEN,
            description="Finite admissibility cannot be restored by boundary counterterm, cutoff, or surface repair.",
        ))
        ns.record_claim(ClaimRecord(
            claim_id="finite_admissibility_diagnostic_branch_filter_in_17",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.CANDIDATE_ROUTE,
            statement="Finite admissibility can currently be stated only as a diagnostic / branch-filter condition, not as a dynamical avoidance theorem.",
        ))
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id="reject_anti_singularity_by_declaration_in_17",
            script_id=SCRIPT_ID,
            branch_id="anti_singularity_by_declaration",
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=[],
        ))
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id="reject_curvature_energy_reservoir_in_17_finite_admissibility",
            script_id=SCRIPT_ID,
            branch_id="curvature_energy_source_reservoir",
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=[],
        ))
        ns.record_derivation(
            derivation_id="finite_admissibility_condition_marker",
            inputs=[],
            output=sp.Symbol("finite_admissibility_condition_complete"),
            method="finite_admissibility_condition",
            status=Status.DERIVED,
        )
        ns.write_run_metadata()


if __name__ == "__main__":
    main()
