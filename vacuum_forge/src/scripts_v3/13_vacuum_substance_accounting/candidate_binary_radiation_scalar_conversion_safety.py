# Candidate binary radiation scalar conversion safety
#
# Purpose
# -------
# The mass-acceleration-gradient coupling audit found several possible couplings:
#
#   P_trace[T] -> delta zeta
#   nabla_mu(T^munu nabla_nu A)
#   T^munu nabla_mu nabla_nu A
#   geodesic identity / geometry bookkeeping
#
# But any candidate must pass the binary-radiation safety filter:
#
#   no extra far-zone scalar radiation,
#   no extra orbital damping beyond the TT channel,
#   no exterior zeta/kappa charge,
#   no duplicate A-sector mass source.
#
# This script asks:
#
#   Does scalar/trace conversion create an extra energy-loss channel in binaries?
#
# It is not a numerical pulsar calculation.
# It is a safety and failure-mode audit.

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
        "REQUIRED": "WARN",
        "MISSING": "FAIL",
        "UNRESOLVED": "FAIL",
        "RISK": "WARN",
        "FORBIDDEN": "PASS",
        "REJECTED": "WARN",
        "DANGER": "FAIL",
    }
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")


@dataclass
class SafetyEntry:
    name: str
    scenario: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str


def build_entries() -> List[SafetyEntry]:
    return [
        SafetyEntry(
            name="B1: conservative geodesic bookkeeping",
            scenario="scalar/trace conversion is just geometric bookkeeping of conservative motion",
            allowed_if="no net far-zone scalar flux and no secular orbital energy loss beyond TT",
            forbidden_if="conversion removes orbital energy as a separate dissipative channel",
            status="SAFE_IF",
            missing="explicit identity showing exchange is conservative/local",
        ),
        SafetyEntry(
            name="B2: local compact conversion",
            scenario="trace/volume conversion occurs only inside/near matter support",
            allowed_if="zeta/kappa support is compact or compensated and exterior zeta,kappa -> 0",
            forbidden_if="conversion produces exterior 1/r scalar charge",
            status="SAFE_IF",
            missing="boundary volume mode no exterior charge theorem",
        ),
        SafetyEntry(
            name="B3: far-zone scalar flux",
            scenario="scalar/trace mode propagates to infinity",
            allowed_if="never, for ordinary gravity",
            forbidden_if="A_rad, Box zeta, or Box kappa carries energy to far zone",
            status="FORBIDDEN",
            missing="parent proof of scalar-radiation exclusion",
        ),
        SafetyEntry(
            name="B4: raw rho v dot grad A coupling",
            scenario="reduced power-like coupling active during orbital motion",
            allowed_if="it is pure conservative bookkeeping or averages to boundary/constraint identity",
            forbidden_if="it produces secular orbital damping",
            status="DANGER",
            missing="orbit-average and conservation interpretation",
        ),
        SafetyEntry(
            name="B5: raw rho a dot grad A coupling",
            scenario="acceleration-gradient coupling active in binaries",
            allowed_if="a is a constrained/geometric relative acceleration and gives no extra loss",
            forbidden_if="coordinate acceleration creates frame-dependent damping",
            status="RISK",
            missing="definition of acceleration and frame",
        ),
        SafetyEntry(
            name="B6: proper-acceleration coupling",
            scenario="rho a^mu nabla_mu A with a^mu proper acceleration",
            allowed_if="used only for non-geodesic/internal stresses",
            forbidden_if="used to explain geodesic gravity exchange but vanishes for geodesics",
            status="RISK",
            missing="role of proper acceleration versus geodesic motion",
        ),
        SafetyEntry(
            name="B7: trace-volume projector coupling",
            scenario="P_trace[T] -> delta zeta",
            allowed_if="trace/volume conversion is compact/compensated and not radiative",
            forbidden_if="trace source leaks to far-zone scalar flux or exterior charge",
            status="SAFE_IF",
            missing="P_trace and compensation law",
        ),
        SafetyEntry(
            name="B8: stress-energy Hessian coupling",
            scenario="T^munu nabla_mu nabla_nu A",
            allowed_if="acts as local/tidal conservative configuration term",
            forbidden_if="creates higher-derivative radiative scalar source or double-counts A",
            status="RISK",
            missing="projection, integration by parts, boundary behavior",
        ),
        SafetyEntry(
            name="B9: divergence stress-gradient coupling",
            scenario="nabla_mu(T^munu nabla_nu A)",
            allowed_if="reduces to constraint/boundary bookkeeping with no far-zone flux",
            forbidden_if="is decorative or hides nonzero scalar flux",
            status="CANDIDATE",
            missing="relation to stress conservation and boundary terms",
        ),
        SafetyEntry(
            name="B10: TT-only ordinary loss rule",
            scenario="ordinary binary radiation loss",
            allowed_if="energy loss at infinity is carried by h_ij^TT only",
            forbidden_if="scalar/trace conversion adds independent far-zone power",
            status="REQUIRED",
            missing="parent derivation of TT-only radiation",
        ),
        SafetyEntry(
            name="B11: cumulative local geometry change",
            scenario="conversion deposits local vacuum-spacetime configuration near accelerating sources",
            allowed_if="bounded, reversible, periodic, or absorbed into conservative near-zone geometry",
            forbidden_if="secular accumulation changes exterior field or orbital dynamics beyond observed bounds",
            status="UNRESOLVED",
            missing="post-deposition dynamics of zeta/epsilon_vac_config",
        ),
        SafetyEntry(
            name="B12: observational constraint placeholder",
            scenario="binary pulsar / gravitational-wave agreement with quadrupole radiation",
            allowed_if="scalar conversion contributes zero or observationally negligible far-zone/secular loss",
            forbidden_if="predicts a generic extra scalar damping channel",
            status="REQUIRED",
            missing="quantitative bound once candidate coupling exists",
        ),
    ]


def print_entry(e: SafetyEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Scenario: {e.scenario}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")


def case_0_problem_statement():
    header("Case 0: Binary-radiation scalar-conversion safety problem")

    print("Question:")
    print()
    print("  Does scalar/trace conversion create an extra energy-loss channel in binaries?")
    print()
    print("Goal:")
    print()
    print("  classify scalar-conversion couplings by whether they are conservative, local, constrained, or dangerous")
    print()
    print("Discipline:")
    print()
    print("  ordinary far-zone radiation must remain TT-only")
    print("  no A_rad")
    print("  no Box zeta")
    print("  no Box kappa")
    print("  no secular scalar orbital damping")
    print("  no exterior zeta/kappa charge")

    status_line("binary-radiation safety problem posed", "REQUIRED")


def case_1_safety_inventory(entries: List[SafetyEntry]):
    header("Case 1: Binary safety inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[SafetyEntry]):
    header("Case 2: Compact binary safety ledger")

    print("| Entry | Scenario | Status | Forbidden if | Missing |")
    print("|---|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.scenario.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.forbidden_if.replace("|", "/")
            + " | "
            + e.missing.replace("|", "/")
            + " |"
        )

    status_line("compact binary safety ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[SafetyEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Scalar conversion is safe only if it is conservative, local/compact, or constrained.")
    print("  Far-zone scalar flux is forbidden.")
    print("  Raw reduced power-like couplings are dangerous until proven conservative.")
    print("  Boundary/exterior charge theorem is now central.")

    status_line("binary safety status count produced", "STRUCTURAL")


def case_4_safe_classes():
    header("Case 4: Safe classes")

    print("Safe or potentially safe classes:")
    print()
    print("1. Conservative geodesic bookkeeping:")
    print("   exchange is geometry, not dissipative loss.")
    print()
    print("2. Local compact conversion:")
    print("   zeta/kappa changes only inside or near matter support.")
    print()
    print("3. Compensated conversion:")
    print("   total exterior scalar charge vanishes.")
    print()
    print("4. Boundary/constraint bookkeeping:")
    print("   exchange appears as divergence or boundary identity with no far-zone scalar flux.")
    print()
    print("5. TT-only far-zone loss:")
    print("   radiated energy at infinity carried only by h_ij^TT.")

    status_line("safe classes stated", "CONSTRAINED")


def case_5_danger_classes():
    header("Case 5: Danger classes")

    print("Danger classes:")
    print()
    print("1. Box zeta or Box kappa.")
    print("2. A_rad ordinary scalar source.")
    print("3. rho v dot grad A as real dissipative power.")
    print("4. coordinate acceleration coupling with no frame rule.")
    print("5. exterior zeta/kappa 1/r tail.")
    print("6. cumulative local deposition that changes M_ext.")
    print("7. scalar conversion producing secular orbital damping.")

    status_line("danger classes stated", "RISK")


def case_6_required_next_theorem():
    header("Case 6: Required next theorem")

    print("The next concrete theorem target is:")
    print()
    print("  local trace/volume reconfiguration has zero exterior scalar charge.")
    print()
    print("Equivalent requirements:")
    print()
    print("  zeta_ext -> 0")
    print("  kappa_ext -> 0")
    print("  Q_volume = 0")
    print("  F_kappa(R+) = 0")
    print("  delta M_ext|volume/kappa reconfiguration = 0")
    print()
    print("Reason:")
    print()
    print("  Binary safety depends on scalar conversion not becoming far-zone scalar flux or extra exterior charge.")

    status_line("boundary/no-exterior-charge theorem target selected", "REQUIRED")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_binary_radiation_scalar_conversion_safety.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_boundary_volume_mode_no_exterior_charge.py")
    print("   Test local volume reconfiguration with zero exterior scalar charge.")
    print()
    print("3. candidate_vacuum_transport_current_constraints.py")
    print("   Constrain J_v if transport/redistribution is needed.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_boundary_volume_mode_no_exterior_charge.py")
    print()
    print("Reason:")
    print("  Binary safety reduces to the boundary/exterior charge problem for scalar/volume conversion.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("Scalar/trace conversion is binary-safe only if:")
    print()
    print("  it is conservative bookkeeping, local compact conversion, or compensated constraint response")
    print("  it carries no far-zone scalar flux")
    print("  it creates no exterior zeta/kappa charge")
    print("  it does not produce secular orbital damping")
    print("  ordinary far-zone radiation remains TT-only")
    print()
    print("Possible next artifact:")
    print("  candidate_binary_radiation_scalar_conversion_safety.md")
    print()
    print("Possible next script:")
    print("  candidate_boundary_volume_mode_no_exterior_charge.py")


def main():
    header("Candidate Binary Radiation Scalar Conversion Safety")
    case_0_problem_statement()
    entries = build_entries()
    case_1_safety_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_safe_classes()
    case_5_danger_classes()
    case_6_required_next_theorem()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
