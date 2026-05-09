# Candidate curvature admissibility object inventory
#
# Group:
#   17_curvature_energy_and_finite_admissibility
#
# Purpose
# -------
# Group 17 starts from the locked-door question:
#
#   Can J_curv or an equivalent curvature-admissibility object be defined
#   covariantly enough to support finite-admissibility / anti-singularity claims
#   without becoming a repair current, hidden energy reservoir, or GR rewrite?
#
# This first script does not define J_curv.
#
# It inventories which kind of object is allowed to carry finite-admissibility:
#
#   diagnostic scalar,
#   finite-admissibility inequality,
#   curvature energy density,
#   curvature current,
#   boundary functional,
#   parent correction tensor seed.
#
# It rejects:
#
#   GR rewrite diagnostics,
#   repair currents,
#   curvature energy as source reservoir,
#   anti-singularity by declaration.
#
# This is a sieve, not a derivation.

from dataclasses import dataclass
from pathlib import Path
from typing import List

import sympy as sp

from vacuumforge import ProjectArchive, Status


ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def status_line(label: str, status: str, detail: str = "") -> None:
    marks = {
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


@dataclass
class CurvatureObjectEntry:
    name: str
    object_form: str
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
        dependency_id="metric_insertion_group_status_summary_marker",
        upstream_script_id="16_metric_insertion_and_no_overlap__candidate_metric_insertion_group_status_summary",
        upstream_derivation_id="metric_insertion_group_status_summary_marker",
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


def build_entries() -> List[CurvatureObjectEntry]:
    return [
        CurvatureObjectEntry(
            name="CA1: curvature admissibility object target",
            object_form="A_curv[g, matter, vacuum] with finite-admissibility role",
            role="core Group 17 target",
            allowed_if="object is defined before anti-singularity claims and has clear domain/measure",
            forbidden_if="object is chosen after the fact to reject singular solutions",
            status="THEOREM_TARGET",
            missing="definition of admissibility object",
            consequence="decides whether anti-singularity language can become technical",
        ),
        CurvatureObjectEntry(
            name="CA2: scalar curvature diagnostic",
            object_form="K, R, R_mu_nu R^mu_nu, Weyl^2, or bounded invariant combination",
            role="safest diagnostic branch",
            allowed_if="used to flag curvature behavior, not as source or current",
            forbidden_if="diagnostic is promoted to dynamics without transport/source law",
            status="CANDIDATE",
            missing="which scalar, measure, and threshold",
            consequence="can support diagnostic/branch-filter claims but not dynamics alone",
        ),
        CurvatureObjectEntry(
            name="CA3: finite-admissibility inequality",
            object_form="A_curv[g, matter, vacuum] < infinity or <= A_max",
            role="branch-filter / admissible-solution condition",
            allowed_if="condition is stated before solutions and has a defined measure/domain",
            forbidden_if="inequality is declared only to exclude unwanted singularities",
            status="CANDIDATE",
            missing="functional, measure, bound, branch-kill rule",
            consequence="can make anti-singularity a theorem target rather than slogan",
        ),
        CurvatureObjectEntry(
            name="CA4: integrable curvature measure",
            object_form="Integral_D I_curv dV_phys finite",
            role="finite total curvature/admissibility candidate",
            allowed_if="domain D and physical measure are fixed structurally",
            forbidden_if="integration domain or cutoff is chosen to hide divergence",
            status="CANDIDATE",
            missing="invariant I_curv, domain, cutoff-free criterion",
            consequence="could support finite-admissible interior branch",
        ),
        CurvatureObjectEntry(
            name="CA5: curvature energy density diagnostic",
            object_form="e_curv = functional of curvature invariants / gradients",
            role="curvature accounting candidate",
            allowed_if="diagnostic/accounting only until recombination/source law exists",
            forbidden_if="used as source reservoir, bounce energy, or coefficient knob",
            status="RISK",
            missing="energy definition, measure, recombination status",
            consequence="dangerous but potentially useful if fenced as diagnostic",
        ),
        CurvatureObjectEntry(
            name="CA6: curvature current candidate",
            object_form="J_curv^mu with domain, orientation, balance law, and boundary behavior",
            role="possible transport/admissibility current",
            allowed_if="direction, divergence/balance, measure, and boundary behavior are defined",
            forbidden_if="J_curv is whatever cancels singularity, divergence, or boundary leakage",
            status="THEOREM_TARGET",
            missing="definition of J_curv and transport/balance law",
            consequence="needed for strong current-based anti-singularity claims",
        ),
        CurvatureObjectEntry(
            name="CA7: boundary functional",
            object_form="B_curv[partial D] controlling admissible boundary flux / compactness",
            role="boundary-admissibility candidate",
            allowed_if="boundary functional is structural and cannot hide mass shift or repair flux",
            forbidden_if="boundary term is chosen to cancel curvature blowup or singularity",
            status="CANDIDATE",
            missing="boundary measure, orientation, neutrality theorem",
            consequence="could support boundary-safe admissibility if not repair",
        ),
        CurvatureObjectEntry(
            name="CA8: curvature-volume admissibility object",
            object_form="A_curv[g,zeta] linking curvature intensity to finite volume response",
            role="possible bridge to vacuum-volume ontology",
            allowed_if="zeta coupling is count-once and does not reopen metric insertion",
            forbidden_if="zeta becomes hidden scalar source or residual trace again",
            status="RISK",
            missing="relation to zeta, no-overlap, and boundary neutrality",
            consequence="promising but dangerous because Group 16 insertion remains theorem target",
        ),
        CurvatureObjectEntry(
            name="CA9: parent correction tensor seed",
            object_form="future H_curv seeded by admissibility object",
            role="future Group 19 handoff",
            allowed_if="H_curv is not introduced until source/divergence safety is known",
            forbidden_if="H_curv appears before admissibility/J_curv is defined",
            status="DEFER",
            missing="J_curv/admissibility object and divergence-safe source",
            consequence="prevents correction tensor from being decorative",
        ),
        CurvatureObjectEntry(
            name="CA10: geodesic completeness proxy",
            object_form="diagnostic proxy for incomplete curves / trapped finite-admissibility failure",
            role="diagnostic only unless linked to equations",
            allowed_if="kept as claim classifier, not dynamics",
            forbidden_if="used to claim singularity avoidance without evolution law",
            status="SAFE_IF",
            missing="link to equations or admissibility theorem",
            consequence="useful for claim audit but not current mechanism",
        ),
        CurvatureObjectEntry(
            name="CA11: GR-rewrite diagnostic",
            object_form="admissibility defined by rearranging Einstein equation or known GR singularity condition",
            role="forbidden GR rewrite",
            allowed_if="only as comparison diagnostic",
            forbidden_if="presented as Vacuum Dynamics derivation",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents importing GR as hidden parent equation",
        ),
        CurvatureObjectEntry(
            name="CA12: repair current",
            object_form="J_curv chosen to cancel divergence, blowup, boundary leakage, or singularity",
            role="forbidden repair mechanism",
            allowed_if="never as definition",
            forbidden_if="accepted as anti-singularity current",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents anti-singularity by painted current",
        ),
        CurvatureObjectEntry(
            name="CA13: curvature energy source reservoir",
            object_form="e_curv inserted as free positive/negative source to force finite behavior",
            role="forbidden source-reservoir branch",
            allowed_if="never unless recombination/source law is derived first",
            forbidden_if="used to tune bounce, mass, boundary, or recovery",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents curvature energy from becoming repair money",
        ),
        CurvatureObjectEntry(
            name="CA14: exterior mass neutrality requirement",
            object_form="delta M_ext|curv = 0 unless coupled through A-sector source law",
            role="ordinary-sector mass protection",
            allowed_if="curvature admissibility cannot shift measured mass independently",
            forbidden_if="curvature accounting changes M_ext as repair or hidden source",
            status="REQUIRED",
            missing="mass neutrality theorem",
            consequence="protects strongest reduced A-sector result",
        ),
        CurvatureObjectEntry(
            name="CA15: boundary repair neutrality requirement",
            object_form="no curvature boundary term hides blowup, leakage, or mass shift",
            role="boundary safety guard",
            allowed_if="boundary object is diagnostic or structurally neutral",
            forbidden_if="boundary term cancels singularity after the fact",
            status="REQUIRED",
            missing="boundary neutrality theorem",
            consequence="prevents finite-admissibility from becoming boundary patch",
        ),
        CurvatureObjectEntry(
            name="CA16: ordinary matter decoupling guard",
            object_form="curvature admissibility does not modify ordinary matter coupling without theorem",
            role="source separation guard",
            allowed_if="ordinary T_mu_nu is not double-counted or rerouted",
            forbidden_if="curvature object changes matter coupling to fix singular behavior",
            status="REQUIRED",
            missing="source separation theorem",
            consequence="prevents matter-sector repair behavior",
        ),
        CurvatureObjectEntry(
            name="CA17: anti-singularity claim guard",
            object_form="allowed claim level <= object support level",
            role="overclaim prevention",
            allowed_if="diagnostic object gives diagnostic claim; dynamics required for dynamical claim",
            forbidden_if="bounce/regular-core claim made from diagnostic only",
            status="REQUIRED",
            missing="claim-class audit",
            consequence="keeps anti-singularity claims honest",
        ),
        CurvatureObjectEntry(
            name="CA18: recommended next move",
            object_form="define finite-admissibility condition before curvature energy/current",
            role="next local bottleneck",
            allowed_if="object inventory does not derive J_curv",
            forbidden_if="jumping to J_curv/H_curv before admissibility condition",
            status="RECOMMENDED",
            missing="finite-admissibility condition",
            consequence="next script should be candidate_finite_admissibility_condition.py",
        ),
    ]


def print_entry(e: CurvatureObjectEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Object form: {e.object_form}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: Curvature admissibility object problem")

    print("Question:")
    print()
    print("  What kind of object can carry finite-admissibility claims:")
    print("  diagnostic scalar, inequality, energy density, current, or boundary functional?")
    print()
    print("Goal:")
    print()
    print("  separate object classes before choosing one")
    print()
    print("Discipline:")
    print()
    print("  do not assert anti-singularity by declaration")
    print("  do not define J_curv as repair current")
    print("  do not treat curvature energy as source reservoir")
    print("  do not shift M_ext independently of A")
    print("  do not use curvature bounds for recovery tuning")
    print("  do not hide singularity avoidance in boundary terms")
    print("  do not import GR equations as admissibility definition")

    status_line("curvature admissibility object problem posed", "REQUIRED")


def case_1_inventory(entries: List[CurvatureObjectEntry]):
    header("Case 1: Curvature admissibility object inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[CurvatureObjectEntry]):
    header("Case 2: Compact curvature admissibility object ledger")

    print("| Entry | Object form | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.object_form.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    status_line("compact object ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[CurvatureObjectEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Diagnostic scalar and finite-admissibility inequality are safest starting points.")
    print("  Curvature energy is risky unless fenced as diagnostic/accounting only.")
    print("  J_curv remains theorem target until domain, direction, balance, and boundary behavior are defined.")
    print("  Boundary functionals may help only if not repair terms.")
    print("  GR rewrite, repair current, and source-reservoir curvature energy are rejected.")
    print("  Next gate is to define finite admissibility as a condition.")

    status_line("curvature admissibility object status count produced", "STRUCTURAL")


def case_4_object_classes():
    header("Case 4: Object-class distinctions")

    print("Object classes:")
    print()
    print("1. curvature diagnostic")
    print("   measures curvature/admissibility but does not source equations")
    print()
    print("2. finite-admissibility inequality")
    print("   filters admissible branches if domain/measure are defined")
    print()
    print("3. curvature energy")
    print("   accounting only unless recombination/source law is derived")
    print()
    print("4. curvature current J_curv")
    print("   requires direction, balance law, domain, measure, and boundary behavior")
    print()
    print("5. boundary functional")
    print("   useful only if it does not hide repair or mass shift")
    print()
    print("6. parent correction seed")
    print("   deferred until admissibility/J_curv is real")

    status_line("object classes distinguished", "RECOMMENDED")


def case_5_decision_tree():
    header("Case 5: Curvature object decision tree")

    print("Decision tree:")
    print()
    print("1. Start with diagnostic / inequality:")
    print("   safest.")
    print()
    print("2. Curvature energy:")
    print("   allowed only as diagnostic/accounting until source law exists.")
    print()
    print("3. J_curv:")
    print("   candidate only after domain/direction/balance/boundary are specified.")
    print()
    print("4. Boundary functional:")
    print("   candidate only if not repair.")
    print()
    print("5. H_curv:")
    print("   deferred until admissibility object exists.")
    print()
    print("6. Repair current / GR rewrite / source reservoir:")
    print("   rejected.")

    status_line("curvature object decision tree stated", "RECOMMENDED")


def case_6_good_failure():
    header("Case 6: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  No current or energy object can be defined without repair behavior")
    print("  or source-reservoir ambiguity.")
    print()
    print("Consequence:")
    print()
    print("  curvature admissibility remains diagnostic / branch-filter only.")
    print("  anti-singularity claims remain theorem targets.")
    print()
    print("Bad failure:")
    print()
    print("  Call a diagnostic scalar a current, or use curvature energy as bounce money.")

    status_line("curvature object good failure stated", "DEFER")


def case_7_failure_controls():
    header("Case 7: Failure controls")

    print("Curvature admissibility object fails if:")
    print()
    print("1. anti-singularity is asserted by declaration")
    print("2. J_curv is defined as repair current")
    print("3. e_curv becomes source reservoir")
    print("4. M_ext shifts independently of A")
    print("5. boundary term hides blowup or mass shift")
    print("6. ordinary matter coupling is altered without theorem")
    print("7. GR equations are imported as admissibility definition")
    print("8. H_curv is introduced before admissibility object")

    status_line("curvature admissibility object failure controls stated", "RISK")


def case_8_next_tests():
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_curvature_admissibility_object_inventory.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_finite_admissibility_condition.py")
    print("   Define what finite admissibility means as a condition.")
    print()
    print("3. candidate_curvature_energy_early_failure_summary.py")
    print("   Use if all object classes collapse into repair/source behavior.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_finite_admissibility_condition.py")
    print()
    print("Reason:")
    print("  Before defining curvature energy or J_curv, the finite-admissibility")
    print("  condition itself must be stated without anti-singularity by declaration.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("The safest starting objects are diagnostic scalar and finite-admissibility inequality.")
    print()
    print("Curvature energy is dangerous unless fenced as diagnostic/accounting.")
    print()
    print("J_curv is a theorem target, not yet a current.")
    print()
    print("Current best interpretation:")
    print()
    print("  define finite admissibility first;")
    print("  only then test e_curv or J_curv.")
    print()
    print("Best next script:")
    print()
    print("  candidate_finite_admissibility_condition.py")

    status_line("curvature admissibility object inventory complete", "CLOSED")


def main():
    header("Candidate Curvature Admissibility Object Inventory")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_object_classes()
    case_5_decision_tree()
    case_6_good_failure()
    case_7_failure_controls()
    case_8_next_tests()
    final_interpretation()

    ns.record_derivation(
        derivation_id="curvature_admissibility_object_inventory_marker",
        inputs=[],
        output=sp.Symbol("curvature_admissibility_object_inventory_complete"),
        method="curvature_admissibility_object_inventory",
        status=Status.DERIVED,
    )
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
