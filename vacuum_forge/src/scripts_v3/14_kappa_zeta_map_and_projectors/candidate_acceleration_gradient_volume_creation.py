# Candidate acceleration-gradient volume creation
#
# Purpose
# -------
# The source-driven volume creation law audit found one best candidate:
#
#   Sigma_V ~ chi rho a^mu nabla_mu A
#
# It is closest to the postulate-facing idea:
#
#   mass/source response across an A-gradient creates or destroys vacuum volume.
#
# But it is only viable if acceleration, frame/projection, chi-origin,
# boundary neutrality, and no-overlap are all defined.
#
# This script tests that candidate explicitly.
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
class AccelGradientEntry:
    name: str
    form: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def build_entries() -> List[AccelGradientEntry]:
    return [
        AccelGradientEntry(
            name="AG1: acceleration-gradient target",
            form="Sigma_V = chi rho a^mu nabla_mu A",
            role="closest postulate-facing source-driven volume creation candidate",
            allowed_if="a^mu, rho, projection, and chi are defined before recovery checks",
            forbidden_if="coefficient or projection chosen from gamma_like/AB",
            status="THEOREM_TARGET",
            missing="covariant acceleration, frame/projection, chi origin",
            consequence="decides whether source-driven companion branch has a real source law",
        ),
        AccelGradientEntry(
            name="AG2: covariant acceleration definition",
            form="a^mu = u^nu nabla_nu u^mu",
            role="standard covariant acceleration candidate",
            allowed_if="u^mu is a physical matter/vacuum flow field, not arbitrary gauge",
            forbidden_if="u^mu is chosen to make Sigma_V work",
            status="CANDIDATE",
            missing="physical definition of u^mu",
            consequence="candidate becomes meaningful only after frame field is specified",
        ),
        AccelGradientEntry(
            name="AG3: vacuum rest-frame projection",
            form="a_perp^mu = P^{mu}_{nu}(u_vac) a^nu, grad_perp A = P nabla A",
            role="frame-safe version using local vacuum rest frame",
            allowed_if="u_vac^mu is defined by ontology or zeta/vacuum substance",
            forbidden_if="vacuum frame is invented as fitting device",
            status="RISK",
            missing="u_vac^mu definition",
            consequence="ties directly to earlier missing vacuum frame field",
        ),
        AccelGradientEntry(
            name="AG4: matter-flow projection",
            form="rho a_m^mu nabla_mu A using matter congruence u_m^mu",
            role="matter-based version of acceleration-gradient source",
            allowed_if="valid for dust/fluid source and not coordinate velocity",
            forbidden_if="used for static matter where a_m is coordinate artifact",
            status="CANDIDATE",
            missing="matter model and source current definition",
            consequence="may be local but source-model dependent",
        ),
        AccelGradientEntry(
            name="AG5: static-source safety",
            form="Sigma_V = 0 or boundary-neutral for static equilibrium sources unless real acceleration exists",
            role="prevents pure density scalar charge",
            allowed_if="static mass does not create independent exterior zeta charge",
            forbidden_if="static rho in gradient creates scalar gravity",
            status="REQUIRED",
            missing="static-source neutrality proof",
            consequence="ordinary-sector viability depends on this",
        ),
        AccelGradientEntry(
            name="AG6: sign/orientation ambiguity",
            form="a^mu nabla_mu A may create or destroy volume depending on sign convention",
            role="tracks physical interpretation of creation versus destruction",
            allowed_if="sign is fixed by postulate or exchange law before recovery",
            forbidden_if="sign chosen to recover gamma_like",
            status="UNRESOLVED",
            missing="creation/destruction sign convention",
            consequence="must be resolved before numerical or recovery claims",
        ),
        AccelGradientEntry(
            name="AG7: chi-origin requirement",
            form="chi fixed by ontology/source coupling before gamma/AB checks",
            role="prevents acceleration-gradient law from becoming tuning",
            allowed_if="chi has prior normalization or exchange-law origin",
            forbidden_if="chi chosen to fix q or gamma_like",
            status="REQUIRED",
            missing="chi origin",
            consequence="Sigma_V remains candidate only while chi is not recovery-fit",
        ),
        AccelGradientEntry(
            name="AG8: coordinate velocity toy rejection",
            form="rho v^i partial_i A is diagnostic only",
            role="prevents toy from becoming parent law",
            allowed_if="used only in reduced simulations or intuition",
            forbidden_if="used as covariant source law",
            status="REJECTED",
            missing="not pursued as parent law",
            consequence="forces covariant/frame-safe expression",
        ),
        AccelGradientEntry(
            name="AG9: residual-kill/no-overlap",
            form="source-driven zeta enters metric only through B_s or residual trace killed/non-metric",
            role="protects zeta companion branch",
            allowed_if="residual-kill/no-overlap theorem is attached",
            forbidden_if="source-driven zeta remains independent residual metric trace",
            status="REQUIRED",
            missing="overlap/residual theorem",
            consequence="prevents zeta from doing both jobs",
        ),
        AccelGradientEntry(
            name="AG10: boundary neutrality",
            form="Q_ext[Sigma_V independent zeta] = 0 or contribution absorbed into B_s",
            role="protects no exterior scalar charge",
            allowed_if="neutrality theorem is explicit",
            forbidden_if="Sigma_V creates independent exterior scalar charge",
            status="REQUIRED",
            missing="boundary neutrality proof",
            consequence="prevents acceleration-gradient branch from becoming scalar gravity",
        ),
        AccelGradientEntry(
            name="AG11: recovery checks downstream",
            form="after Sigma_V/F_zeta fixed, test gamma_like=1 and AB->1",
            role="ordinary-regime recovery target",
            allowed_if="checked after source law and coefficient are fixed",
            forbidden_if="used to choose a^mu, projection, or chi",
            status="RECOVERY_TARGET",
            missing="solutions after Sigma_V",
            consequence="tests but does not define acceleration-gradient law",
        ),
        AccelGradientEntry(
            name="AG12: recommended next move",
            form="define the frame field u^mu/u_vac^mu before refining Sigma_V",
            role="best current bottleneck",
            allowed_if="frame is treated as structural prerequisite",
            forbidden_if="continuing with undefined acceleration",
            status="RECOMMENDED",
            missing="candidate frame-field inventory",
            consequence="next script should inventory frame-field choices for a^mu and projection",
        ),
    ]


def print_entry(e: AccelGradientEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Form: {e.form}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: Acceleration-gradient volume creation problem")

    print("Question:")
    print()
    print("  Can acceleration across gradient be made covariant, or is it only a good cave-picture?")
    print()
    print("Goal:")
    print()
    print("  test Sigma_V = chi rho a^mu nabla_mu A as a source-driven volume creation candidate")
    print()
    print("Discipline:")
    print()
    print("  define acceleration and frame/projection")
    print("  do not choose chi from recovery")
    print("  protect static-source neutrality")
    print("  reject coordinate-velocity parent laws")
    print("  preserve residual-kill/no-overlap")
    print("  preserve boundary neutrality")
    print("  keep recovery checks downstream")

    status_line("acceleration-gradient volume creation problem posed", "REQUIRED")


def case_1_inventory(entries: List[AccelGradientEntry]):
    header("Case 1: Acceleration-gradient inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[AccelGradientEntry]):
    header("Case 2: Compact acceleration-gradient ledger")

    print("| Entry | Form | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.form.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    status_line("compact acceleration-gradient ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[AccelGradientEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  The acceleration-gradient candidate is live but depends on frame definition.")
    print("  u^mu or u_vac^mu is now the bottleneck.")
    print("  Static-source safety, chi-origin, no-overlap, and boundary neutrality are mandatory.")
    print("  Coordinate velocity remains rejected as a parent law.")

    status_line("acceleration-gradient status count produced", "STRUCTURAL")


def case_4_minimal_form():
    header("Case 4: Minimal candidate form")

    print("Candidate:")
    print()
    print("  Sigma_V = chi rho a^mu nabla_mu A")
    print()
    print("with:")
    print()
    print("  a^mu = u^nu nabla_nu u^mu")
    print()
    print("Open choices:")
    print()
    print("1. Is u^mu matter flow or vacuum rest frame?")
    print("2. Is the contraction fully spacetime or spatially projected?")
    print("3. What fixes chi?")
    print("4. What makes static sources neutral?")
    print("5. How does zeta enter B_s without residual trace overlap?")

    status_line("minimal acceleration-gradient form stated", "CANDIDATE")


def case_5_good_failure():
    header("Case 5: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  Sigma_V = chi rho a^mu nabla_mu A cannot be made frame-defined,")
    print("  coefficient-fixed, static-neutral, and no-overlap compatible.")
    print()
    print("Consequence:")
    print()
    print("  acceleration-gradient branch fails for now.")
    print("  Return to source-driven map as theorem target or test broader tensor candidates.")
    print()
    print("Bad failure:")
    print("  keep using acceleration-gradient language while u^mu and chi remain undefined.")

    status_line("acceleration-gradient good failure stated", "DEFER")


def case_6_failure_controls():
    header("Case 6: Failure controls")

    print("Acceleration-gradient branch fails if:")
    print()
    print("1. u^mu is not defined")
    print("2. vacuum frame is invented to fit recovery")
    print("3. chi is chosen from gamma_like")
    print("4. AB diagnostic chooses sign or coefficient")
    print("5. coordinate velocity replaces covariant acceleration")
    print("6. static density produces independent exterior scalar charge")
    print("7. zeta residual trace remains metric-active")
    print("8. boundary neutrality is absent")
    print("9. no-overlap theorem is absent")

    status_line("acceleration-gradient failure controls stated", "RISK")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_acceleration_gradient_volume_creation.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_volume_creation_frame_field_inventory.py")
    print("   Inventory matter-flow, vacuum-flow, and projected-frame choices for a^mu nabla_mu A.")
    print()
    print("3. candidate_stress_energy_hessian_volume_creation.py")
    print("   Test broader T^{mu nu} nabla_mu nabla_nu A candidate if frame branch fails.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_volume_creation_frame_field_inventory.py")
    print()
    print("Reason:")
    print("  The acceleration-gradient branch cannot proceed until u^mu/u_vac^mu and projection are defined.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("Acceleration-gradient volume creation is the best postulate-facing source law candidate.")
    print()
    print("But the current bottleneck is not the scalar form; it is the frame:")
    print()
    print("  what is u^mu, and what projection defines a^mu nabla_mu A?")
    print()
    print("Best next test:")
    print("  candidate_volume_creation_frame_field_inventory.py")


def main():
    header("Candidate Acceleration-Gradient Volume Creation")
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_minimal_form()
    case_5_good_failure()
    case_6_failure_controls()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
