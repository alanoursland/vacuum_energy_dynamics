# Candidate boundary volume mode no exterior charge
#
# Purpose
# -------
# The binary-radiation scalar-conversion safety audit found:
#
#   scalar/trace conversion is safe only if it is conservative, local/compact,
#   or compensated, with no far-zone scalar flux and no exterior zeta/kappa charge.
#
# The required next theorem target is:
#
#   local trace/volume reconfiguration has zero exterior scalar charge.
#
# Equivalent requirements:
#
#   zeta_ext -> 0
#   kappa_ext -> 0
#   Q_volume = 0
#   F_kappa(R+) = 0
#   delta M_ext|volume/kappa reconfiguration = 0
#
# This script tests the boundary/no-exterior-charge theorem target.
#
# It is not a proof yet.
# It is a theorem-candidate and no-go audit.

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
        "THEOREM_TARGET": "WARN",
    }
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")


@dataclass
class BoundaryVolumeEntry:
    name: str
    condition: str
    allowed_meaning: str
    forbidden_failure: str
    status: str
    missing: str


def build_entries() -> List[BoundaryVolumeEntry]:
    return [
        BoundaryVolumeEntry(
            name="VQ1: compact support volume reconfiguration",
            condition="zeta(r)=0 for r>=R or zeta has compact support",
            allowed_meaning="local vacuum-spacetime volume reconfiguration remains interior/local",
            forbidden_failure="zeta_ext has long-range 1/r scalar tail",
            status="SAFE_IF",
            missing="physical reason for compact support from parent projector",
        ),
        BoundaryVolumeEntry(
            name="VQ2: zero exterior volume charge",
            condition="Q_volume = integral S_volume d^3x = 0",
            allowed_meaning="volume/trace source is compensated and produces no exterior monopole",
            forbidden_failure="Q_volume != 0 produces exterior scalar charge",
            status="THEOREM_TARGET",
            missing="definition of S_volume and compensation law",
        ),
        BoundaryVolumeEntry(
            name="VQ3: zero boundary flux",
            condition="F_zeta(R+) = 4*pi*R^2*zeta_prime(R+) = 0",
            allowed_meaning="no scalar volume flux enters exterior vacuum",
            forbidden_failure="nonzero exterior flux seeds zeta_ext ~ 1/r",
            status="REQUIRED",
            missing="boundary/interface law",
        ),
        BoundaryVolumeEntry(
            name="VQ4: kappa exterior neutrality",
            condition="kappa_ext -> 0 and F_kappa(R+) = 0",
            allowed_meaning="kappa remains trace/volume matching variable, not exterior scalar field",
            forbidden_failure="kappa_ext ~ 1/r or nonzero exterior attractor",
            status="CONSTRAINED",
            missing="kappa-zeta relation and boundary projector",
        ),
        BoundaryVolumeEntry(
            name="VQ5: A-sector exterior mass protected",
            condition="delta M_ext|volume/kappa reconfiguration = 0",
            allowed_meaning="A_flux carries exterior mass; volume mode does not tune measured gravity",
            forbidden_failure="boundary volume smoothing changes exterior A 1/r coefficient",
            status="REQUIRED",
            missing="boundary mass preservation theorem",
        ),
        BoundaryVolumeEntry(
            name="VQ6: compensated source projection",
            condition="P_0 S = S - <S> over support, so integral P_0 S d^3x = 0",
            allowed_meaning="nonlocal constraint projection removes exterior scalar monopole",
            forbidden_failure="uncompensated trace/volume source",
            status="CANDIDATE",
            missing="whether projection is parent-derived or merely imposed",
        ),
        BoundaryVolumeEntry(
            name="VQ7: smooth compact profile",
            condition="zeta(R)=0, zeta_prime(R)=0, possibly zeta_double_prime(R)=0",
            allowed_meaning="toy boundary profile avoids flux/shell artifacts",
            forbidden_failure="hidden shell source at boundary",
            status="STRUCTURAL",
            missing="required smoothness from action/interface law",
        ),
        BoundaryVolumeEntry(
            name="VQ8: divergence/boundary identity",
            condition="integral div J_volume d^3x = surface J_volume dot dS = 0",
            allowed_meaning="conversion can be local or constrained with no exterior leakage",
            forbidden_failure="J_volume carries scalar flux to infinity",
            status="CANDIDATE",
            missing="definition of J_volume / J_v and support",
        ),
        BoundaryVolumeEntry(
            name="VQ9: exterior vacuum fixed point",
            condition="S_trace_effective=0 -> zeta_min=0, kappa_min=0, zeta,kappa -> 0",
            allowed_meaning="ordinary exterior vacuum has no volume-mode scalar field",
            forbidden_failure="nonzero exterior volume-form attractor",
            status="CONSTRAINED",
            missing="relaxation law and exterior stability proof",
        ),
        BoundaryVolumeEntry(
            name="VQ10: no binary scalar flux",
            condition="dE_scalar_far/dt = 0 for volume/kappa mode",
            allowed_meaning="binary scalar conversion remains local/conservative/compensated",
            forbidden_failure="far-zone scalar energy flux or secular orbital damping",
            status="REQUIRED",
            missing="radiation safety proof after coupling is selected",
        ),
        BoundaryVolumeEntry(
            name="VQ11: nonlinear determinant caveat",
            condition="linear zeta control extended or replaced by nonlinear volume condition",
            allowed_meaning="trace/volume neutrality survives beyond linear perturbation",
            forbidden_failure="linear volume neutrality overclaimed",
            status="RISK",
            missing="nonlinear determinant / covariant volume-form theorem",
        ),
        BoundaryVolumeEntry(
            name="VQ12: parent projector origin",
            condition="P_boundary P_trace enforces exterior neutrality",
            allowed_meaning="zero exterior charge follows from parent structure",
            forbidden_failure="boundary neutrality imposed by hand at each case",
            status="MISSING",
            missing="parent identity / projector derivation",
        ),
    ]


def print_entry(e: BoundaryVolumeEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Condition: {e.condition}")
    print(f"Allowed meaning: {e.allowed_meaning}")
    print(f"Forbidden failure: {e.forbidden_failure}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")


def case_0_problem_statement():
    header("Case 0: Boundary volume mode no exterior charge problem")

    print("Question:")
    print()
    print("  Can local trace/volume reconfiguration have zero exterior scalar charge?")
    print()
    print("Goal:")
    print()
    print("  test compact support, compensation, zero flux, and mass-preservation requirements")
    print()
    print("Discipline:")
    print()
    print("  no exterior zeta 1/r tail")
    print("  no exterior kappa 1/r tail")
    print("  no change to M_ext")
    print("  no far-zone scalar flux")
    print("  no boundary mass tuning")
    print("  do not overclaim linear/toy profiles as parent theorem")

    status_line("boundary volume no-charge problem posed", "REQUIRED")


def case_1_inventory(entries: List[BoundaryVolumeEntry]):
    header("Case 1: Boundary volume/no-charge inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[BoundaryVolumeEntry]):
    header("Case 2: Compact boundary volume ledger")

    print("| Entry | Condition | Status | Forbidden failure | Missing |")
    print("|---|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.condition.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.forbidden_failure.replace("|", "/")
            + " | "
            + e.missing.replace("|", "/")
            + " |"
        )

    status_line("compact boundary volume ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[BoundaryVolumeEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  The boundary/no-charge theorem has clear necessary conditions.")
    print("  Compact support, zero flux, compensation, and A-flux protection are the core.")
    print("  Parent projector origin remains missing.")

    status_line("boundary volume status count produced", "STRUCTURAL")


def case_4_candidate_theorem_statement():
    header("Case 4: Candidate theorem statement")

    print("Candidate theorem:")
    print()
    print("  If the trace/volume mode zeta is compactly supported or compensated,")
    print("  and the boundary flux vanishes,")
    print("  then the exterior volume scalar charge vanishes.")
    print()
    print("Reduced conditions:")
    print()
    print("  Q_volume = 0")
    print("  F_zeta(R+) = 0")
    print("  zeta_ext -> 0")
    print("  kappa_ext -> 0")
    print("  delta M_ext|volume/kappa = 0")
    print()
    print("Interpretation:")
    print()
    print("  local vacuum-volume reconfiguration changes interior spacetime configuration")
    print("  without adding a second exterior scalar field.")
    print()
    print("Current status:")
    print("  theorem target, not theorem.")

    status_line("candidate no-exterior-charge theorem stated", "THEOREM_TARGET")


def case_5_toy_profile_tests():
    header("Case 5: Toy profile tests")

    print("Example compact profile:")
    print()
    print("  zeta(r) = zeta0 * (1 - r^2/R^2)^n for r <= R")
    print("  zeta(r) = 0 for r > R")
    print()
    print("For n >= 2:")
    print()
    print("  zeta(R) = 0")
    print("  zeta_prime(R) = 0")
    print()
    print("For n >= 3:")
    print()
    print("  zeta_double_prime(R) = 0")
    print()
    print("Use:")
    print()
    print("  toy check for boundary flux and shell artifacts")
    print()
    print("Do not use as:")
    print()
    print("  parent-derived physical profile")

    status_line("toy compact profile tests stated", "STRUCTURAL")


def case_6_failure_controls():
    header("Case 6: Failure controls")

    print("The boundary volume theorem fails if:")
    print()
    print("1. zeta_ext has a 1/r tail.")
    print("2. kappa_ext has a 1/r tail.")
    print("3. Q_volume != 0.")
    print("4. F_zeta(R+) or F_kappa(R+) is nonzero.")
    print("5. delta M_ext changes under volume/kappa reconfiguration.")
    print("6. compensation is imposed by hand without parent origin.")
    print("7. hidden shell sources appear at the boundary.")
    print("8. binary scalar flux becomes nonzero.")
    print("9. linear determinant logic is overclaimed as nonlinear theorem.")

    status_line("boundary volume failure controls stated", "RISK")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_boundary_volume_mode_no_exterior_charge.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_vacuum_transport_current_constraints.py")
    print("   Constrain J_v if transport/redistribution is needed.")
    print()
    print("3. candidate_vacuum_accounting_parent_balance.py")
    print("   Write a more concrete vacuum-substance accounting balance.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_vacuum_transport_current_constraints.py")
    print()
    print("Reason:")
    print("  If volume conversion is compact/compensated, we need to know whether J_v is local, constrained, or transport.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("Boundary volume-mode safety requires:")
    print()
    print("  zeta_ext -> 0")
    print("  kappa_ext -> 0")
    print("  Q_volume = 0")
    print("  F_zeta(R+) = 0")
    print("  F_kappa(R+) = 0")
    print("  delta M_ext|volume/kappa = 0")
    print()
    print("This is the central theorem target for scalar-conversion safety.")
    print()
    print("Possible next artifact:")
    print("  candidate_boundary_volume_mode_no_exterior_charge.md")
    print()
    print("Possible next script:")
    print("  candidate_vacuum_transport_current_constraints.py")


def main():
    header("Candidate Boundary Volume Mode No Exterior Charge")
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_candidate_theorem_statement()
    case_5_toy_profile_tests()
    case_6_failure_controls()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
