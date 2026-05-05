# Candidate source-driven volume creation law
#
# Purpose
# -------
# The F_zeta companion map inventory found:
#
#   algebraic maps are risky patches,
#   differential maps need an exchange operator,
#   source-driven maps need Sigma_V[A,T].
#
# The best non-fitting F_zeta route is source-driven volume creation.
#
# This script inventories possible Sigma_V[A,T] forms before using them
# to drive zeta and then B_s.
#
# It is not a derivation.

from dataclasses import dataclass
from typing import List


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
    }
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")


@dataclass
class SigmaVolumeEntry:
    name: str
    sigma_form: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def build_entries() -> List[SigmaVolumeEntry]:
    return [
        SigmaVolumeEntry(
            name="SV1: source-driven volume creation target",
            sigma_form="Sigma_V[A,T] drives zeta before F_zeta maps zeta to B_s",
            role="core missing mechanism for source-driven companion branch",
            allowed_if="Sigma_V is expressed before recovery checks",
            forbidden_if="Sigma_V is chosen to repair A_spatial/gamma",
            status="THEOREM_TARGET",
            missing="explicit Sigma_V[A,T]",
            consequence="decides whether source-driven zeta companion branch is real",
        ),
        SigmaVolumeEntry(
            name="SV2: rho acceleration-gradient candidate",
            sigma_form="Sigma_V ~ chi rho a^mu nabla_mu A",
            role="closest expression to mass accelerating across a gradient",
            allowed_if="a^mu and frame/projection are defined covariantly",
            forbidden_if="chi is tuned to gamma_like",
            status="CANDIDATE",
            missing="definition of a^mu, frame field, and chi origin",
            consequence="postulate-facing but needs covariant structure",
        ),
        SigmaVolumeEntry(
            name="SV3: stress-energy Hessian candidate",
            sigma_form="Sigma_V ~ chi T^{mu nu} nabla_mu nabla_nu A",
            role="covariant-looking source/field curvature coupling",
            allowed_if="does not import GR equations or higher-derivative scalar radiation",
            forbidden_if="chosen only because it is covariant-looking",
            status="RISK",
            missing="operator origin and radiation safety",
            consequence="may create unwanted scalar dynamics if not constrained",
        ),
        SigmaVolumeEntry(
            name="SV4: flux-gradient candidate",
            sigma_form="Sigma_V ~ chi J_m^mu nabla_mu A",
            role="matter-flow version of source-driven volume creation",
            allowed_if="J_m is conserved/defined and frame-safe",
            forbidden_if="uses coordinate velocity without covariant meaning",
            status="CANDIDATE",
            missing="matter current and frame projection",
            consequence="could express motion across gradient without raw coordinate velocity",
        ),
        SigmaVolumeEntry(
            name="SV5: rho v dot grad A toy form",
            sigma_form="Sigma_V ~ chi rho v^i partial_i A",
            role="noncovariant diagnostic toy",
            allowed_if="used only as reduced toy / diagnostic",
            forbidden_if="accepted as parent law",
            status="CONSTRAINED",
            missing="covariant lift",
            consequence="useful intuition but not acceptable parent expression",
        ),
        SigmaVolumeEntry(
            name="SV6: pure density source",
            sigma_form="Sigma_V ~ chi rho or chi T",
            role="simple source-volume coupling",
            allowed_if="it does not create static scalar charge and has boundary neutrality proof",
            forbidden_if="creates volume for static density without gradient/coupling trigger",
            status="RISK",
            missing="neutrality theorem and trigger principle",
            consequence="likely creates forbidden scalar exterior charge if used directly",
        ),
        SigmaVolumeEntry(
            name="SV7: coefficient-origin requirement",
            sigma_form="chi fixed by postulate/ontology before gamma/AB checks",
            role="prevents source-driven creation from becoming tuning",
            allowed_if="chi has prior normalization or exchange-law origin",
            forbidden_if="chi chosen to recover gamma_like or q",
            status="REQUIRED",
            missing="chi origin",
            consequence="Sigma_V fails as derivation if chi remains free fit",
        ),
        SigmaVolumeEntry(
            name="SV8: zeta residual-kill/no-overlap",
            sigma_form="source-driven zeta enters metric only through B_s, or residual trace killed",
            role="keeps companion branch from double-counting",
            allowed_if="residual kill/non-metric theorem is attached",
            forbidden_if="source-driven zeta also remains residual metric scalar",
            status="REQUIRED",
            missing="residual-kill and overlap theorem",
            consequence="mandatory if Sigma_V is used for companion branch",
        ),
        SigmaVolumeEntry(
            name="SV9: boundary neutrality",
            sigma_form="Q_ext[Sigma_V independent zeta] = 0 or contribution absorbed into B_s",
            role="protects no exterior scalar charge",
            allowed_if="neutrality theorem is explicit",
            forbidden_if="Sigma_V creates independent exterior scalar charge",
            status="REQUIRED",
            missing="boundary neutrality proof",
            consequence="prevents source-driven volume from becoming scalar gravity",
        ),
        SigmaVolumeEntry(
            name="SV10: recovery checks downstream",
            sigma_form="after Sigma_V and F_zeta fixed, test gamma_like=1 and AB->1",
            role="ordinary-regime recovery target",
            allowed_if="checked after source law is fixed",
            forbidden_if="used to choose Sigma_V or chi",
            status="RECOVERY_TARGET",
            missing="solutions after Sigma_V/F_zeta",
            consequence="tests but does not define source law",
        ),
        SigmaVolumeEntry(
            name="SV11: source-patch failure",
            sigma_form="Sigma_V inserted only to fix q, gamma, or AB",
            role="rejected shortcut",
            allowed_if="used only as no-go diagnosis",
            forbidden_if="accepted as derivation",
            status="REJECTED",
            missing="not pursued",
            consequence="kills source-driven branch if no independent Sigma_V exists",
        ),
        SigmaVolumeEntry(
            name="SV12: recommended next move",
            sigma_form="test rho a·grad A candidate first, with covariant/frame and chi-origin requirements",
            role="best current concrete candidate",
            allowed_if="treated as candidate, not final law",
            forbidden_if="using noncovariant toy as parent equation",
            status="RECOMMENDED",
            missing="covariant acceleration-gradient inventory",
            consequence="next script should test acceleration-gradient source law and frame requirements",
        ),
    ]


def print_entry(e: SigmaVolumeEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Sigma form: {e.sigma_form}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: Source-driven volume creation law problem")

    print("Question:")
    print()
    print("  Can Sigma_V[A,T] be written without becoming a repair spell?")
    print()
    print("Goal:")
    print()
    print("  inventory source-driven volume creation expressions before using them in F_zeta")
    print()
    print("Discipline:")
    print()
    print("  do not choose Sigma_V from gamma_like or AB")
    print("  do not accept noncovariant velocity toy as parent law")
    print("  define frame/current/acceleration if used")
    print("  preserve residual-kill/no-overlap")
    print("  preserve boundary neutrality")
    print("  keep recovery checks downstream")

    status_line("source-driven volume creation problem posed", "REQUIRED")


def case_1_inventory(entries: List[SigmaVolumeEntry]):
    header("Case 1: Source-driven volume creation inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[SigmaVolumeEntry]):
    header("Case 2: Compact source-driven creation ledger")

    print("| Entry | Sigma form | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.sigma_form.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    status_line("compact source-driven creation ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[SigmaVolumeEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  The acceleration-gradient candidate is the closest postulate-facing form.")
    print("  Flux-gradient forms may be acceptable if the current and frame are defined.")
    print("  Pure density source is dangerous because it likely creates static scalar charge.")
    print("  rho v dot grad A remains a toy until covariantly lifted.")
    print("  Chi origin, residual-kill, and boundary neutrality are mandatory.")

    status_line("source-driven creation status count produced", "STRUCTURAL")


def case_4_candidate_decision_tree():
    header("Case 4: Source law decision tree")

    print("Decision tree:")
    print()
    print("1. rho a·grad A?")
    print("   Best postulate-facing candidate; needs covariant acceleration and frame.")
    print()
    print("2. T^{mu nu} nabla_mu nabla_nu A?")
    print("   Covariant-looking but high risk of unwanted scalar dynamics.")
    print()
    print("3. J_m·grad A?")
    print("   Candidate if matter current and projection are defined.")
    print()
    print("4. rho v·grad A?")
    print("   Toy only until covariantly lifted.")
    print()
    print("5. pure rho/T?")
    print("   Dangerous; likely scalar charge unless neutralized.")

    status_line("source-law decision tree stated", "RECOMMENDED")


def case_5_good_failure():
    header("Case 5: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  no Sigma_V[A,T] expression can be written that is covariant/frame-safe,")
    print("  coefficient-fixed, boundary-neutral, and no-overlap compatible.")
    print()
    print("Consequence:")
    print()
    print("  source-driven zeta companion branch fails for now.")
    print("  A_spatial remains recovery theorem target,")
    print("  and zeta may remain residual only under P_relax if neutral/non-radiative.")
    print()
    print("Bad failure:")
    print("  use rho v·grad A as parent law because it has the right intuition.")

    status_line("source-driven creation good failure stated", "DEFER")


def case_6_failure_controls():
    header("Case 6: Failure controls")

    print("Source-driven volume creation fails if:")
    print()
    print("1. Sigma_V is chosen from gamma_like")
    print("2. Sigma_V is chosen from AB")
    print("3. coordinate velocity is used as parent law")
    print("4. acceleration/frame field is undefined")
    print("5. chi remains free recovery fit")
    print("6. pure density source creates exterior scalar charge")
    print("7. source-driven zeta remains independent residual trace")
    print("8. boundary neutrality is absent")
    print("9. no-overlap theorem is absent")

    status_line("source-driven creation failure controls stated", "RISK")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_source_driven_volume_creation_law.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_acceleration_gradient_volume_creation.py")
    print("   Test Sigma_V ~ rho a^mu nabla_mu A and frame/covariance requirements.")
    print()
    print("3. candidate_kappa_diagnostic_or_residual_after_zeta.py")
    print("   Clean up kappa after zeta companion decision if this branch survives.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_acceleration_gradient_volume_creation.py")
    print()
    print("Reason:")
    print("  The acceleration-gradient candidate is closest to the postulate. Test it explicitly before trying broader tensor expressions.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("Source-driven volume creation has one best candidate:")
    print()
    print("  Sigma_V ~ chi rho a^mu nabla_mu A")
    print()
    print("But it is only viable if acceleration, frame/projection, chi-origin, boundary neutrality, and no-overlap are all defined.")
    print()
    print("Best next test:")
    print("  candidate_acceleration_gradient_volume_creation.py")


def main():
    header("Candidate Source-Driven Volume Creation Law")
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_candidate_decision_tree()
    case_5_good_failure()
    case_6_failure_controls()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
