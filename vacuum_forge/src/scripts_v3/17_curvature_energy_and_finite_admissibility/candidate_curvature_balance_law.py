# Candidate curvature balance law
#
# Group:
#   17_curvature_energy_and_finite_admissibility
#
# Purpose
# -------
# The J_curv definition requirements audit found:
#
#   J_curv is not defined yet.
#   A real J_curv requires domain, orientation, measure, covariance status,
#   admissibility role, boundary behavior, matter separation, and mass neutrality.
#
# It also found:
#
#   e_curv does not define J_curv.
#   zeta/volume coupling remains risky until no-overlap and insertion issues are solved.
#   H_curv remains deferred.
#
# This script tests whether curvature admissibility can be expressed as a balance law
# without becoming decorative continuity language.
#
# Locked-door question:
#
#   Can curvature admissibility be expressed as a balance law
#   without becoming decorative?
#
# This is a balance-law audit, not a current derivation.


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
class CurvatureBalanceEntry:
    name: str
    balance_form: str
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
        dependency_id="J_curv_definition_requirements_marker",
        upstream_script_id="17_curvature_energy_and_finite_admissibility__candidate_J_curv_definition_requirements",
        upstream_derivation_id="J_curv_definition_requirements_marker",
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


def build_entries() -> List[CurvatureBalanceEntry]:
    return [
        CurvatureBalanceEntry(
            name="CB1: curvature balance target",
            balance_form="curvature admissibility balance with defined current/source/relaxation/domain",
            role="core balance-law theorem target",
            allowed_if="balance is built from defined objects and not used to define them decoratively",
            forbidden_if="balance language is written before J_curv/source sides exist",
            status="THEOREM_TARGET",
            missing="J_curv, source side, relaxation side, domain, measure",
            consequence="decides whether curvature admissibility can become dynamical structure",
        ),
        CurvatureBalanceEntry(
            name="CB2: divergence balance candidate",
            balance_form="nabla_mu J_curv^mu = Sigma_curv - R_curv",
            role="continuity-style theorem target",
            allowed_if="J_curv, Sigma_curv, and R_curv are independently defined",
            forbidden_if="equation defines all symbols at once",
            status="THEOREM_TARGET",
            missing="J_curv, Sigma_curv, R_curv",
            consequence="strongest balance form if source sides become real",
        ),
        CurvatureBalanceEntry(
            name="CB3: inequality balance candidate",
            balance_form="nabla_mu J_curv^mu <= admissibility_bound",
            role="finite-admissibility control candidate",
            allowed_if="bound, measure, and domain are specified before solutions",
            forbidden_if="bound is chosen to make target solution admissible",
            status="CANDIDATE",
            missing="bound, measure, domain, current",
            consequence="could express finite admissibility without exact conservation",
        ),
        CurvatureBalanceEntry(
            name="CB4: boundary flux balance candidate",
            balance_form="Integral_boundary J_curv . dSigma controls Integral_D I_curv dV",
            role="boundary/admissibility candidate",
            allowed_if="boundary flux is diagnostic or structurally neutral, not repair",
            forbidden_if="boundary flux cancels singularity or hides mass shift",
            status="CANDIDATE",
            missing="boundary theorem, J_curv, I_curv",
            consequence="could link finite integral to boundary safety if not patch",
        ),
        CurvatureBalanceEntry(
            name="CB5: curvature-volume exchange candidate",
            balance_form="curvature admissibility exchange tied to zeta/volume response",
            role="curvature-volume bridge",
            allowed_if="does not reopen B_s/F_zeta, residual trace, or O problems",
            forbidden_if="zeta becomes hidden scalar source or repair channel",
            status="RISK",
            missing="zeta coupling, count-once, no-overlap, boundary neutrality",
            consequence="promising but dangerous until Group 16 bottlenecks are solved",
        ),
        CurvatureBalanceEntry(
            name="CB6: diagnostic-only branch",
            balance_form="no balance law; finite admissibility remains diagnostic / branch-filter",
            role="safe fallback",
            allowed_if="J_curv/source sides remain undefined",
            forbidden_if="stronger dynamical claim is made anyway",
            status="SAFE_IF",
            missing="dynamics/current",
            consequence="keeps anti-singularity claims limited but honest",
        ),
        CurvatureBalanceEntry(
            name="CB7: source side requirement",
            balance_form="Sigma_curv must be defined before appearing in balance",
            role="source-side guard",
            allowed_if="source has domain, measure, sign, and physical meaning",
            forbidden_if="Sigma_curv is whatever creates finite curvature",
            status="REQUIRED",
            missing="Sigma_curv operator",
            consequence="prevents source term from being repair label",
        ),
        CurvatureBalanceEntry(
            name="CB8: relaxation side requirement",
            balance_form="R_curv must be defined before appearing in balance",
            role="relaxation-side guard",
            allowed_if="relaxation/return has mechanism and cannot be tuned",
            forbidden_if="R_curv is chosen to erase divergence or singularity",
            status="REQUIRED",
            missing="R_curv operator",
            consequence="prevents R_curv from becoming cancellation knob",
        ),
        CurvatureBalanceEntry(
            name="CB9: admissibility-bound requirement",
            balance_form="admissibility_bound must be defined before balance test",
            role="inequality guard",
            allowed_if="bound follows from finite-admissibility condition",
            forbidden_if="bound is set by desired bounce or regular core",
            status="REQUIRED",
            missing="bound and relation to A_curv",
            consequence="prevents inequality from being solution-tailored",
        ),
        CurvatureBalanceEntry(
            name="CB10: domain and measure requirement",
            balance_form="balance law uses fixed D_curv, dV_phys, and boundary measure",
            role="mathematical well-posedness guard",
            allowed_if="domain/measure are structural",
            forbidden_if="domain/measure hide divergence or boundary leakage",
            status="REQUIRED",
            missing="D_curv and measures",
            consequence="prevents fake finite balance",
        ),
        CurvatureBalanceEntry(
            name="CB11: boundary neutrality requirement",
            balance_form="curvature balance has no boundary repair flux, exterior scalar charge, or M_ext shift",
            role="ordinary exterior guard",
            allowed_if="boundary behavior is structural and neutral",
            forbidden_if="boundary flux cancels blowup or changes mass",
            status="REQUIRED",
            missing="boundary neutrality theorem",
            consequence="protects exterior sector",
        ),
        CurvatureBalanceEntry(
            name="CB12: matter separation requirement",
            balance_form="curvature balance does not double-count T_mu_nu or alter ordinary matter coupling",
            role="source separation guard",
            allowed_if="matter source remains routed independently",
            forbidden_if="curvature balance fixes singularity by changing matter coupling",
            status="REQUIRED",
            missing="matter separation theorem",
            consequence="prevents matter repair behavior",
        ),
        CurvatureBalanceEntry(
            name="CB13: e_curv separation",
            balance_form="e_curv remains diagnostic/accounting unless source law is later derived",
            role="energy/current guard",
            allowed_if="balance law does not use e_curv as reservoir",
            forbidden_if="e_curv pays for curvature balance",
            status="REQUIRED",
            missing="source/recombination law",
            consequence="preserves curvature-energy fence",
        ),
        CurvatureBalanceEntry(
            name="CB14: H_curv deferred",
            balance_form="H_curv is not introduced as balance closure in Group 17",
            role="parent-correction deferral",
            allowed_if="H_curv waits for Group 19 divergence-safe audit",
            forbidden_if="H_curv is added to make balance close",
            status="DEFER",
            missing="H_curv audit",
            consequence="prevents premature correction tensor",
        ),
        CurvatureBalanceEntry(
            name="CB15: decorative continuity rejection",
            balance_form="nabla_mu J_curv^mu = Sigma_curv - R_curv written with all symbols undefined",
            role="forbidden decorative balance",
            allowed_if="never as result",
            forbidden_if="accepted as curvature balance law",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents painted conservation law",
        ),
        CurvatureBalanceEntry(
            name="CB16: repair balance rejection",
            balance_form="balance law chosen to cancel singularity, divergence, or boundary leakage",
            role="forbidden repair balance",
            allowed_if="never as mechanism",
            forbidden_if="accepted as anti-singularity balance",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents singularity-avoidance by cancellation label",
        ),
        CurvatureBalanceEntry(
            name="CB17: recovery-tuned balance rejection",
            balance_form="curvature balance chosen to pass gamma_like, AB, or exterior matching",
            role="forbidden recovery smuggling",
            allowed_if="never as mechanism",
            forbidden_if="balance chosen by recovery targets",
            status="REJECTED",
            missing="not pursued",
            consequence="keeps recovery downstream",
        ),
        CurvatureBalanceEntry(
            name="CB18: anti-singularity claim guard",
            balance_form="balance candidate does not license bounce/regular core without dynamics and solutions",
            role="overclaim guard",
            allowed_if="claim remains theorem target / branch filter",
            forbidden_if="dynamical avoidance claimed from balance form alone",
            status="REQUIRED",
            missing="claim audit",
            consequence="keeps anti-singularity claims honest",
        ),
        CurvatureBalanceEntry(
            name="CB19: balance failure",
            balance_form="no non-decorative balance can be written with current objects",
            role="branch failure / fallback condition",
            allowed_if="used to keep curvature admissibility diagnostic/branch-filter only",
            forbidden_if="patched by undefined source symbols",
            status="BRANCH_KILLED",
            missing="applies if demonstrated",
            consequence="J_curv balance cannot be used; continue diagnostic-only",
        ),
        CurvatureBalanceEntry(
            name="CB20: recommended next move",
            balance_form="if balance remains theorem target, audit curvature boundary and mass neutrality next",
            role="next local bottleneck",
            allowed_if="balance is not derived but safety requirements are clear",
            forbidden_if="jumping to anti-singularity claims before boundary/mass audit",
            status="RECOMMENDED",
            missing="boundary/mass neutrality audit",
            consequence="next script should be candidate_curvature_boundary_and_mass_neutrality.py",
        ),
    ]


def print_entry(e: CurvatureBalanceEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Balance form: {e.balance_form}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: Curvature balance law problem")

    print("Question:")
    print()
    print("  Can curvature admissibility be expressed as a balance law")
    print("  without becoming decorative?")
    print()
    print("Goal:")
    print()
    print("  test balance forms only after J_curv requirements are clear")
    print()
    print("Discipline:")
    print()
    print("  no decorative continuity law")
    print("  no undefined Sigma_curv / R_curv")
    print("  no repair balance")
    print("  no boundary flux patch")
    print("  no matter double-count")
    print("  no M_ext shift")
    print("  no e_curv source reservoir")
    print("  no H_curv yet")
    print("  no bounce/regular-core claim")

    status_line("curvature balance law problem posed", "REQUIRED")


def case_1_inventory(entries: List[CurvatureBalanceEntry]):
    header("Case 1: Curvature balance law inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[CurvatureBalanceEntry]):
    header("Case 2: Compact curvature balance ledger")

    print("| Entry | Balance form | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.balance_form.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    status_line("compact curvature balance ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[CurvatureBalanceEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Curvature balance can be stated only as theorem target unless J_curv and source sides are defined.")
    print("  Exact divergence balance is strongest but currently underdefined.")
    print("  Inequality and boundary flux balances are candidates if bounds/measures are structural.")
    print("  Diagnostic-only branch remains the safe fallback.")
    print("  H_curv remains deferred.")
    print("  Next gate is boundary and mass neutrality.")

    status_line("curvature balance law status count produced", "STRUCTURAL")


def case_4_balance_forms():
    header("Case 4: Candidate balance forms")

    print("Candidate balance forms:")
    print()
    print("1. exact divergence balance:")
    print("   nabla_mu J_curv^mu = Sigma_curv - R_curv")
    print()
    print("2. inequality balance:")
    print("   nabla_mu J_curv^mu <= admissibility_bound")
    print()
    print("3. boundary flux balance:")
    print("   boundary flux controls finite curvature integral")
    print()
    print("4. curvature-volume exchange:")
    print("   curvature admissibility tied to zeta/volume response")
    print()
    print("5. diagnostic-only branch:")
    print("   no balance law yet")

    status_line("candidate curvature balance forms listed", "RECOMMENDED")


def case_5_decision_tree():
    header("Case 5: Curvature balance decision tree")

    print("Decision tree:")
    print()
    print("1. J_curv + Sigma_curv + R_curv defined:")
    print("   exact divergence balance may proceed.")
    print()
    print("2. J_curv undefined but admissibility bound defined:")
    print("   inequality remains theorem target, not law.")
    print()
    print("3. Boundary flux defined structurally:")
    print("   boundary balance candidate may proceed to neutrality audit.")
    print()
    print("4. Zeta-volume coupling appears:")
    print("   high risk; must not reopen Group 16 bottlenecks.")
    print()
    print("5. All source sides undefined:")
    print("   diagnostic-only branch.")
    print()
    print("6. Balance cancels failure:")
    print("   rejected as repair.")

    status_line("curvature balance decision tree stated", "RECOMMENDED")


def case_6_good_failure():
    header("Case 6: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  No non-decorative balance law can be written because J_curv,")
    print("  Sigma_curv, R_curv, bounds, or measures are not defined.")
    print()
    print("Consequence:")
    print()
    print("  curvature admissibility remains diagnostic / branch-filter only.")
    print("  do not write balance law with placeholder symbols.")
    print()
    print("Bad failure:")
    print()
    print("  write nabla_mu J_curv^mu = Sigma_curv - R_curv and call it closure.")

    status_line("curvature balance law good failure stated", "DEFER")


def case_7_failure_controls():
    header("Case 7: Failure controls")

    print("Curvature balance law fails if:")
    print()
    print("1. J_curv is undefined")
    print("2. Sigma_curv is undefined")
    print("3. R_curv is undefined")
    print("4. admissibility bound is solution-tailored")
    print("5. domain/measure hide divergence")
    print("6. boundary flux repairs singularity or mass shift")
    print("7. matter source is double-counted or rerouted")
    print("8. e_curv becomes source reservoir")
    print("9. H_curv is introduced as closure")
    print("10. gamma_like / AB / recovery chooses the balance")
    print("11. bounce or regular core is claimed")

    status_line("curvature balance law failure controls stated", "RISK")


def case_8_next_tests():
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_curvature_balance_law.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_curvature_boundary_and_mass_neutrality.py")
    print("   Test whether curvature admissibility/J_curv alters exterior mass or boundary behavior.")
    print()
    print("3. candidate_curvature_balance_failure_summary.py")
    print("   Use if all balance forms collapse into decorative continuity.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_curvature_boundary_and_mass_neutrality.py")
    print()
    print("Reason:")
    print("  Even if curvature balance remains theorem-targeted, its safety burden is boundary/mass neutrality.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("Curvature balance remains a theorem target, not a law.")
    print()
    print("Strongest possible form:")
    print()
    print("  nabla_mu J_curv^mu = Sigma_curv - R_curv")
    print()
    print("But this is not usable until J_curv, Sigma_curv, R_curv, domain, and measure are defined.")
    print()
    print("Safe fallback:")
    print()
    print("  curvature admissibility remains diagnostic / branch-filter only.")
    print()
    print("Best next script:")
    print()
    print("  candidate_curvature_boundary_and_mass_neutrality.py")

    status_line("curvature balance law audit complete", "CLOSED")


def main():
    header("Candidate Curvature Balance Law")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_balance_forms()
    case_5_decision_tree()
    case_6_good_failure()
    case_7_failure_controls()
    case_8_next_tests()
    final_interpretation()

    ns.record_derivation(
        derivation_id="curvature_balance_law_marker",
        inputs=[],
        output=sp.Symbol("curvature_balance_law_complete"),
        method="curvature_balance_law",
        status=Status.DERIVED,
    )
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
