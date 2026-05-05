# Candidate kappa as projected zeta mismatch
#
# Purpose
# -------
# The kappa-zeta map inventory found that the strongest next target is:
#
#   kappa = P_trace(zeta - zeta_min)
#
# or possibly:
#
#   kappa = P_relax P_trace(zeta - zeta_min)
#
# Reason:
#
#   Projection is the best current chance to relate kappa to zeta while
#   preserving exterior neutrality and avoiding double-counting.
#
# This script audits what P_trace must do for the projected map to be safe.
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
    }
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")


@dataclass
class ProjectedMapEntry:
    name: str
    condition: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str


def build_entries() -> List[ProjectedMapEntry]:
    return [
        ProjectedMapEntry(
            name="PZ1: raw projected map",
            condition="kappa = P_trace(zeta - zeta_min)",
            role="defines kappa as the trace/volume part of zeta displacement",
            allowed_if="P_trace is a constraint/projector and not a wave operator",
            forbidden_if="P_trace is identity and creates raw exterior scalar charge",
            status="CANDIDATE",
            missing="definition of P_trace",
        ),
        ProjectedMapEntry(
            name="PZ2: relaxed projected map",
            condition="kappa = P_relax P_trace(zeta - zeta_min)",
            role="adds first-order relaxation filter after trace projection",
            allowed_if="P_relax preserves no-wave, no-overshoot kappa behavior",
            forbidden_if="P_relax becomes second-order scalar dynamics",
            status="CANDIDATE",
            missing="P_relax definition and relation to Gamma_relax",
        ),
        ProjectedMapEntry(
            name="PZ3: compensation requirement",
            condition="integral P_trace(zeta - zeta_min) d^3x = 0 or Q_kappa=0",
            role="removes exterior monopole / scalar charge",
            allowed_if="compensation follows from parent projector or boundary law",
            forbidden_if="compensation is imposed ad hoc for each source",
            status="REQUIRED",
            missing="Q_kappa / Q_volume relation and parent origin",
        ),
        ProjectedMapEntry(
            name="PZ4: exterior fixed point",
            condition="zeta_ext=0, zeta_min_ext=0, kappa_ext=0",
            role="keeps ordinary exterior vacuum scalar-neutral",
            allowed_if="projector maps exterior vacuum to zero",
            forbidden_if="projector permits kappa_ext ~ 1/r",
            status="REQUIRED",
            missing="exterior stability theorem",
        ),
        ProjectedMapEntry(
            name="PZ5: zero boundary flux",
            condition="F_kappa(R+)=0 and F_zeta(R+)=0",
            role="prevents projected trace/volume residual from leaking outside",
            allowed_if="P_trace includes or cooperates with P_boundary",
            forbidden_if="nonzero boundary flux seeds exterior scalar tail",
            status="REQUIRED",
            missing="P_boundary relation",
        ),
        ProjectedMapEntry(
            name="PZ6: A-sector mass separation",
            condition="delta M_ext|projected zeta/kappa = 0",
            role="protects exterior mass from volume/trace reconfiguration",
            allowed_if="P_trace excludes A_flux / rho mass charge",
            forbidden_if="zeta/kappa changes the A-sector 1/r coefficient",
            status="REQUIRED",
            missing="boundary mass theorem and scalar constraint propagation",
        ),
        ProjectedMapEntry(
            name="PZ7: epsilon/e_kappa accounting",
            condition="epsilon_zeta and e_kappa counted separately; no K_lock energy",
            role="preserves group-13 double-counting convention",
            allowed_if="kappa is residual/diagnostic projection and not duplicate zeta energy",
            forbidden_if="projected map makes e_kappa identical to epsilon_zeta displacement",
            status="SAFE_IF",
            missing="whether e_kappa is residual energy or should be absorbed later",
        ),
        ProjectedMapEntry(
            name="PZ8: diagnostic versus energetic projection",
            condition="P_trace map may be diagnostic, energetic, or constraint-defining",
            role="decides whether kappa has independent energy",
            allowed_if="status is explicitly labeled",
            forbidden_if="same projection is used both as identity and energy term",
            status="UNRESOLVED",
            missing="degree-of-freedom count",
        ),
        ProjectedMapEntry(
            name="PZ9: trace/TT separation",
            condition="P_trace h_TT = 0 and P_TT P_trace = 0",
            role="prevents trace/volume projection from contaminating TT radiation",
            allowed_if="projectors are orthogonal at least in the reduced/linear sense",
            forbidden_if="trace residual sources h_TT or TT changes zeta",
            status="CONSTRAINED",
            missing="nonlinear/covariant projector structure",
        ),
        ProjectedMapEntry(
            name="PZ10: no scalar wave promotion",
            condition="no Box kappa, no Box zeta",
            role="keeps projected map non-radiative",
            allowed_if="projection/relaxation remains elliptic/constraint/first-order",
            forbidden_if="projected residual is promoted to a hyperbolic scalar field",
            status="FORBIDDEN",
            missing="parent proof of no scalar inertia",
        ),
        ProjectedMapEntry(
            name="PZ11: recombination compatibility",
            condition="A, zeta, kappa assembled once into g_ij",
            role="prevents A spatial response, zeta volume response, and kappa trace response from triple-counting",
            allowed_if="P_recombination defines one trace/volume contribution",
            forbidden_if="g_ij includes scalar_spatial_response(A) + zeta + kappa as independent volume terms",
            status="REQUIRED",
            missing="P_recombination",
        ),
        ProjectedMapEntry(
            name="PZ12: recommended projected convention",
            condition="kappa = P_relax P_trace(zeta - zeta_min), with K_lock diagnostic only",
            role="best provisional projected map",
            allowed_if="P_trace removes exterior charge and P_relax stays first-order",
            forbidden_if="projection fails exterior neutrality or double-counting",
            status="RECOMMENDED",
            missing="definitions of P_trace, P_relax, P_boundary",
        ),
    ]


def print_entry(e: ProjectedMapEntry) -> None:
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


def case_0_problem_statement():
    header("Case 0: Kappa as projected zeta mismatch problem")

    print("Question:")
    print()
    print("  Can kappa be defined safely as P_trace(zeta-zeta_min)?")
    print()
    print("Goal:")
    print()
    print("  test whether projection can relate kappa to zeta while preserving exterior neutrality and avoiding double-counting")
    print()
    print("Discipline:")
    print()
    print("  P_trace must not be a wave operator")
    print("  P_trace must not duplicate A-sector mass")
    print("  projected kappa must have zero exterior charge")
    print("  e_kappa and epsilon_zeta must not count the same mismatch twice")
    print("  K_lock remains diagnostic only")
    print("  recombination must count trace/volume response once")

    status_line("projected kappa-zeta problem posed", "REQUIRED")


def case_1_inventory(entries: List[ProjectedMapEntry]):
    header("Case 1: Projected map inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[ProjectedMapEntry]):
    header("Case 2: Compact projected-map ledger")

    print("| Entry | Condition | Status | Missing |")
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
            + e.missing.replace("|", "/")
            + " |"
        )

    status_line("compact projected-map ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[ProjectedMapEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Projected kappa is promising, but only if P_trace also supports compensation/exterior neutrality.")
    print("  The relaxed projected map is safer than raw equality.")
    print("  The main unresolved issue is whether the projection is diagnostic, energetic, or constraint-defining.")

    status_line("projected-map status count produced", "STRUCTURAL")


def case_4_minimal_projected_map():
    header("Case 4: Minimal projected map")

    print("Minimal map:")
    print()
    print("  kappa = P_trace(zeta-zeta_min)")
    print()
    print("Safer relaxed map:")
    print()
    print("  kappa = P_relax P_trace(zeta-zeta_min)")
    print()
    print("Required exterior conditions:")
    print()
    print("  zeta_ext -> 0")
    print("  kappa_ext -> 0")
    print("  Q_volume = 0")
    print("  Q_kappa = 0")
    print("  F_zeta(R+) = 0")
    print("  F_kappa(R+) = 0")
    print("  delta M_ext = 0")
    print()
    print("Accounting:")
    print()
    print("  epsilon_zeta counted separately")
    print("  e_kappa counted separately only if kappa is a residual")
    print("  K_lock not counted as physical energy")

    status_line("minimal projected map stated", "CANDIDATE")


def case_5_projector_requirements():
    header("Case 5: P_trace requirements")

    print("P_trace must:")
    print()
    print("1. extract trace/volume mismatch")
    print("2. remove or compensate exterior monopole")
    print("3. exclude A-sector mass charge")
    print("4. annihilate TT modes")
    print("5. cooperate with P_boundary")
    print("6. avoid becoming a wave operator")
    print("7. support first-order relaxation if P_relax is included")
    print("8. leave recombination with only one trace/volume contribution")

    status_line("P_trace requirements stated", "REQUIRED")


def case_6_failure_controls():
    header("Case 6: Failure controls")

    print("The projected map fails if:")
    print()
    print("1. P_trace is just identity on zeta-zeta_min and exterior charge survives.")
    print("2. P_trace is raw pressure/trace source and duplicates A-sector mass.")
    print("3. kappa_ext or zeta_ext has a 1/r tail.")
    print("4. e_kappa duplicates epsilon_zeta displacement.")
    print("5. K_lock becomes physical energy before derivation.")
    print("6. Box kappa or Box zeta reappears.")
    print("7. TT modes alter zeta through projector leakage.")
    print("8. recombination counts A spatial response, zeta, and kappa separately.")

    status_line("projected-map failure controls stated", "RISK")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_kappa_as_projected_zeta_mismatch.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_trace_projector_definition.py")
    print("   Define P_trace directly.")
    print()
    print("3. candidate_kappa_as_zeta_mismatch.py")
    print("   Test direct equality for comparison.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_trace_projector_definition.py")
    print()
    print("Reason:")
    print("  The projected map is only as good as P_trace. Define the projector next.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("Projected kappa is the best current relation target:")
    print()
    print("  kappa = P_trace(zeta-zeta_min)")
    print()
    print("Safer version:")
    print()
    print("  kappa = P_relax P_trace(zeta-zeta_min)")
    print()
    print("This is safe only if:")
    print()
    print("  P_trace removes exterior charge")
    print("  P_trace excludes A-sector mass")
    print("  P_trace annihilates TT")
    print("  P_boundary enforces zero flux")
    print("  P_recombination counts trace/volume once")
    print()
    print("Possible next artifact:")
    print("  candidate_kappa_as_projected_zeta_mismatch.md")
    print()
    print("Possible next script:")
    print("  candidate_trace_projector_definition.py")


def main():
    header("Candidate Kappa As Projected Zeta Mismatch")
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_minimal_projected_map()
    case_5_projector_requirements()
    case_6_failure_controls()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
