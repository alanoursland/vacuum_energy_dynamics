# Candidate boundary mass preservation identity
#
# Purpose
# -------
# The kappa covariant relaxation audit found:
#
#   kappa relaxation is only safe if boundary/exterior mass preservation is enforced.
#
# This script asks:
#
#   Can kappa / boundary relaxation modify local trace or volume matching
#   without changing the exterior A-sector mass flux?
#
# It does not prove the theorem.
# It builds the required boundary mass preservation identity.
#
# Key target:
#
#   delta M_ext | kappa relaxation = 0
#
# and:
#
#   F_kappa(R+) = 0
#
# This is a requirement audit, not a derivation.

from dataclasses import dataclass
from typing import List


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def status_line(label: str, status: str, detail: str = "") -> None:
    marks = {
        "DERIVED_REDUCED": "PASS",
        "STRUCTURAL": "WARN",
        "CONSTRAINED": "WARN",
        "REQUIRED": "WARN",
        "MISSING": "FAIL",
        "UNRESOLVED": "FAIL",
        "RISK": "WARN",
        "FORBIDDEN": "PASS",
        "CANDIDATE": "WARN",
    }
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")


@dataclass
class BoundaryRequirement:
    name: str
    requirement: str
    candidate_form: str
    forbidden_form: str
    status: str
    risk: str
    missing: str


def build_requirements() -> List[BoundaryRequirement]:
    return [
        BoundaryRequirement(
            name="B1: exterior mass is A-sector flux",
            requirement="Exterior mass must be defined by the A-sector flux / exterior 1/r coefficient.",
            candidate_form="A_ext = 1 - 2*G*M_ext/(c^2*r)",
            forbidden_form="M_ext adjusted by kappa boundary smoothing",
            status="DERIVED_REDUCED",
            risk="Measured mass becomes tunable by interface choice.",
            missing="Parent flux-charge definition.",
        ),
        BoundaryRequirement(
            name="B2: kappa boundary relaxation preserves M_ext",
            requirement="Kappa relaxation may change local trace/volume matching but not exterior mass.",
            candidate_form="delta M_ext|kappa_relaxation = 0",
            forbidden_form="delta M_ext != 0 from smoothing or kappa interface adjustment",
            status="REQUIRED",
            risk="Boundary smoothing tunes measured gravity.",
            missing="Boundary mass preservation theorem.",
        ),
        BoundaryRequirement(
            name="B3: exterior kappa charge vanishes",
            requirement="Kappa must not create an exterior 1/r scalar tail.",
            candidate_form="Q_kappa = integral S_kappa d^3x = 0",
            forbidden_form="kappa_ext ~ q_kappa/r",
            status="CONSTRAINED",
            risk="Second exterior scalar charge.",
            missing="Projection or boundary cancellation identity.",
        ),
        BoundaryRequirement(
            name="B4: exterior kappa flux vanishes",
            requirement="No kappa flux may cross into exterior vacuum as scalar charge.",
            candidate_form="F_kappa(R+) = 4*pi*R^2*kappa_prime(R+) = 0",
            forbidden_form="F_kappa(R+) != 0",
            status="CONSTRAINED",
            risk="Exterior kappa tail and scalar double-counting.",
            missing="Interface law enforcing zero flux.",
        ),
        BoundaryRequirement(
            name="B5: exterior vacuum fixed point",
            requirement="Outside ordinary matter, kappa_min=0 and kappa relaxes to zero.",
            candidate_form="S_trace_effective=0 -> kappa_min=0 -> kappa -> 0",
            forbidden_form="nonzero exterior kappa attractor",
            status="CONSTRAINED",
            risk="Persistent exterior scalar state.",
            missing="Exterior vacuum relaxation proof.",
        ),
        BoundaryRequirement(
            name="B6: A flux and kappa flux are independent charges",
            requirement="Kappa interface conditions must not modify the A-sector Gauss/flux charge.",
            candidate_form="delta integral grad A dot dS | kappa = 0",
            forbidden_form="kappa boundary condition changes integral grad A dot dS",
            status="REQUIRED",
            risk="Scalar mass double-counting through boundary coupling.",
            missing="Parent separation of A flux and kappa boundary condition.",
        ),
        BoundaryRequirement(
            name="B7: joint-minimum smoothing is diagnostic only",
            requirement="Near-boundary smoothing may be modeled, but cannot be used to claim mass change.",
            candidate_form="f_joint diagnostics with fixed exterior M_ext",
            forbidden_form="joint-minimum fit changes exterior mass coefficient",
            status="CONSTRAINED",
            risk="Near-boundary deviation overclaim or mass retuning.",
            missing="Weights, sigma, recombination, observable map.",
        ),
        BoundaryRequirement(
            name="B8: source compactness condition",
            requirement="Kappa relaxation support must be compact or compensated for ordinary isolated bodies.",
            candidate_form="support(S_kappa_eff) compact and/or integral S_kappa_eff d^3x = 0",
            forbidden_form="uncompensated trace source leaking into exterior",
            status="STRUCTURAL",
            risk="Long-range kappa scalar field.",
            missing="Definition of S_kappa_eff and compensation law.",
        ),
        BoundaryRequirement(
            name="B9: recombination preserves exterior Schwarzschild",
            requirement="Metric recombination must preserve exterior A/B result when kappa=0.",
            candidate_form="kappa_ext=0 -> recombination gives exterior Schwarzschild reduced form",
            forbidden_form="recombination reintroduces scalar trace outside",
            status="REQUIRED",
            risk="Silent GR import or scalar double-counting.",
            missing="P_recombination identity.",
        ),
        BoundaryRequirement(
            name="B10: relaxation energy does not alter M_ext by disappearance",
            requirement="Energy moved by Gamma_relax must be accounted without changing exterior mass incorrectly.",
            candidate_form="Delta E_relax -> Delta E_vac_config with total exterior charge preserved",
            forbidden_form="energy damping changes mass without source accounting",
            status="MISSING",
            risk="Energy nonconservation or hidden mass tuning.",
            missing="Vacuum configuration energy balance.",
        ),
    ]


def print_requirement(b: BoundaryRequirement) -> None:
    print()
    print("-" * 120)
    print(b.name)
    print("-" * 120)
    print(f"Requirement: {b.requirement}")
    print(f"Candidate form: {b.candidate_form}")
    print(f"Forbidden form: {b.forbidden_form}")
    status_line(b.name, b.status)
    print(f"Risk: {b.risk}")
    print(f"Missing: {b.missing}")


def case_0_problem_statement():
    header("Case 0: Boundary mass preservation problem")

    print("Question:")
    print()
    print("  Can kappa/boundary relaxation occur without changing exterior mass?")
    print()
    print("Goal:")
    print()
    print("  formalize the boundary mass preservation requirement")
    print()
    print("Discipline:")
    print()
    print("  exterior mass belongs to A-sector flux")
    print("  kappa cannot add a second exterior scalar charge")
    print("  boundary smoothing cannot tune measured gravity")
    print("  near-boundary diagnostics are not predictions yet")

    status_line("boundary mass preservation problem posed", "REQUIRED")


def case_1_requirement_inventory(entries: List[BoundaryRequirement]):
    header("Case 1: Boundary requirement inventory")
    for entry in entries:
        print_requirement(entry)


def case_2_compact_table(entries: List[BoundaryRequirement]):
    header("Case 2: Compact boundary ledger")

    print("| Requirement | Candidate form | Forbidden form | Status | Missing |")
    print("|---|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.candidate_form.replace("|", "/")
            + " | "
            + e.forbidden_form.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.missing.replace("|", "/")
            + " |"
        )

    status_line("compact boundary ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[BoundaryRequirement]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Exterior A mass is reduced-derived.")
    print("  Boundary preservation is required but not proven.")
    print("  Relaxation energy accounting remains missing.")

    status_line("boundary status count produced", "STRUCTURAL")


def case_4_candidate_boundary_identity():
    header("Case 4: Candidate boundary identity")

    print("Candidate boundary preservation identity:")
    print()
    print("  delta M_ext|kappa_relaxation = 0")
    print()
    print("with:")
    print()
    print("  M_ext proportional to exterior A flux")
    print("  F_kappa(R+) = 0")
    print("  Q_kappa = 0")
    print("  kappa_ext -> 0")
    print()
    print("Equivalent reduced reading:")
    print()
    print("  kappa can smooth/relax local trace-volume matching,")
    print("  but it cannot change the coefficient of 1/r in A_ext.")
    print()
    print("This is currently a requirement, not a theorem.")

    status_line("candidate boundary identity stated", "REQUIRED")


def case_5_failure_controls():
    header("Case 5: Failure controls")

    print("Boundary mass preservation fails if:")
    print()
    print("1. Kappa smoothing changes M_ext.")
    print("2. F_kappa(R+) is nonzero.")
    print("3. Q_kappa is nonzero.")
    print("4. Exterior kappa has a nonzero attractor.")
    print("5. A flux and kappa flux mix without parent identity.")
    print("6. Near-boundary diagnostics are advertised as measured predictions.")
    print("7. Relaxation energy disappears or changes exterior mass without accounting.")

    status_line("boundary failure controls stated", "RISK")


def case_6_next_tests():
    header("Case 6: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_boundary_mass_preservation_identity.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_recombination_without_double_counting.py")
    print("   Try a disciplined recombination map.")
    print()
    print("3. candidate_relaxation_energy_accounting_identity.py")
    print("   Define the energy destination for Gamma_relax.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_recombination_without_double_counting.py")
    print()
    print("Reason:")
    print("  Boundary mass is protected by requirements; now recombination must avoid reintroducing scalar double-counting.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("Boundary/kappa relaxation can remain safe only if:")
    print()
    print("  exterior mass is A-sector flux")
    print("  delta M_ext from kappa relaxation is zero")
    print("  Q_kappa is zero")
    print("  F_kappa(R+) is zero")
    print("  exterior kappa relaxes to zero")
    print("  recombination preserves exterior Schwarzschild")
    print("  relaxation energy is accounted")
    print()
    print("Possible next artifact:")
    print("  candidate_boundary_mass_preservation_identity.md")
    print()
    print("Possible next script:")
    print("  candidate_recombination_without_double_counting.py")


def main():
    header("Candidate Boundary Mass Preservation Identity")
    case_0_problem_statement()
    entries = build_requirements()
    case_1_requirement_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_candidate_boundary_identity()
    case_5_failure_controls()
    case_6_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
