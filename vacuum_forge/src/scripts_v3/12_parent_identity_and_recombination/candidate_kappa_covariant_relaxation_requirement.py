# Candidate kappa covariant relaxation requirement
#
# Purpose
# -------
# The scalar constraint-not-radiation audit found:
#
#   A is protected as a constraint,
#   A_rad is rejected,
#   rho does not source long-range kappa,
#   trace shifts kappa_min without Box kappa,
#   scalar constraint propagation remains missing.
#
# The next gate is kappa:
#
#   kappa is currently first-order non-inertial trace / volume relaxation.
#
# But a dot(kappa) equation can hide a preferred frame unless we specify what
# derivative, frame, or flow defines relaxation.
#
# This script asks:
#
#   What must a frame-consistent or covariant kappa relaxation law require?
#
# This is not a derivation.
# It is a requirement audit.

from dataclasses import dataclass
from typing import List


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def status_line(label: str, status: str, detail: str = "") -> None:
    marks = {
        "STRUCTURAL": "WARN",
        "CONSTRAINED": "WARN",
        "REJECTED": "WARN",
        "MISSING": "FAIL",
        "UNRESOLVED": "FAIL",
        "RISK": "WARN",
        "REQUIRED": "WARN",
        "CANDIDATE": "WARN",
    }
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")


@dataclass
class KappaRequirement:
    name: str
    requirement: str
    candidate_form: str
    forbidden_form: str
    status: str
    risk: str
    missing: str


def build_requirements() -> List[KappaRequirement]:
    return [
        KappaRequirement(
            name="K1: replace dot(kappa) with a defined flow derivative",
            requirement="Kappa relaxation must specify the derivative direction.",
            candidate_form="u^mu nabla_mu kappa = -mu_kappa*K_kappa*(kappa-kappa_min)",
            forbidden_form="bare dot(kappa) with unspecified frame",
            status="CANDIDATE",
            risk="Preferred-frame ambiguity hidden in notation.",
            missing="Definition of u^mu or local vacuum frame.",
        ),
        KappaRequirement(
            name="K2: preserve first-order non-inertial relaxation",
            requirement="Kappa must not acquire an independent momentum channel.",
            candidate_form="u^mu nabla_mu kappa = -lambda_kappa*(kappa-kappa_min)",
            forbidden_form="Box kappa = alpha*S_trace",
            status="CONSTRAINED",
            risk="Hidden scalar breathing radiation.",
            missing="Parent reason for first-order rather than second-order operator.",
        ),
        KappaRequirement(
            name="K3: define kappa_min as a scalar or frame-compatible field",
            requirement="The local minimum must transform consistently.",
            candidate_form="kappa_min = chi_kappa*S_trace_effective, with S_trace_effective scalar/frame-defined",
            forbidden_form="kappa_min depends on coordinate pressure without frame definition",
            status="STRUCTURAL",
            risk="Kappa source law becomes gauge/frame artifact.",
            missing="Definition of S_trace_effective.",
        ),
        KappaRequirement(
            name="K4: define local vacuum/rest frame",
            requirement="Relaxation requires a physical or effective frame field if using u^mu.",
            candidate_form="u^mu = vacuum-substance flow / matter-comoving flow / normal to preferred foliation",
            forbidden_form="implicit universal time coordinate with no ontology",
            status="UNRESOLVED",
            risk="Unacknowledged preferred slicing.",
            missing="Choice and justification of frame field.",
        ),
        KappaRequirement(
            name="K5: exterior vacuum fixed point",
            requirement="In exterior ordinary vacuum, kappa_min=0 and kappa relaxes to zero.",
            candidate_form="S_trace_effective=0 -> kappa_min=0 -> kappa -> 0",
            forbidden_form="exterior kappa tail or nonzero exterior kappa attractor",
            status="CONSTRAINED",
            risk="Second scalar exterior charge.",
            missing="Boundary/projection identity enforcing Q_kappa=0.",
        ),
        KappaRequirement(
            name="K6: boundary flux condition preserved",
            requirement="Boundary relaxation must not leak kappa charge into exterior.",
            candidate_form="F_kappa(R+) = 0 and delta M_ext|kappa_relaxation = 0",
            forbidden_form="boundary smoothing changes exterior A flux or creates kappa 1/r tail",
            status="CONSTRAINED",
            risk="Boundary mass tuning or scalar double-counting.",
            missing="Boundary mass preservation theorem.",
        ),
        KappaRequirement(
            name="K7: relaxation energy accounting",
            requirement="Relaxation must transfer imbalance into vacuum configuration energy, not destroy it.",
            candidate_form="Gamma_relax -> Delta E_vac_config, total exchange balance conserved",
            forbidden_form="damping term with no energy destination",
            status="MISSING",
            risk="Cosmetic damping / energy nonconservation.",
            missing="Vacuum configuration energy variable and balance law.",
        ),
        KappaRequirement(
            name="K8: no direct rho source",
            requirement="Kappa relaxation source must exclude rho as independent long-range scalar source.",
            candidate_form="S_kappa[rho]=0; trace/pressure only shifts kappa_min under P_trace",
            forbidden_form="rho contributes to kappa_min as mass scalar charge",
            status="CONSTRAINED",
            risk="Scalar double-counting with A-sector.",
            missing="Parent source decomposition for trace vs mass.",
        ),
        KappaRequirement(
            name="K9: recombination role limited",
            requirement="Kappa may affect trace/volume matching but must not duplicate A's scalar mass response.",
            candidate_form="AB=e^(2*kappa) diagnostic; exterior kappa=0; scalar mass response counted by A",
            forbidden_form="kappa used as second metric scalar carrying mass response",
            status="STRUCTURAL",
            risk="Silent scalar double-counting in metric recombination.",
            missing="P_recombination map.",
        ),
        KappaRequirement(
            name="K10: causality / relaxation locality",
            requirement="First-order relaxation must be local along the chosen flow and not imply instantaneous nonlocal correction.",
            candidate_form="u^mu nabla_mu kappa local; kappa_min local or projection-defined with stated support",
            forbidden_form="global projection with hidden acausal adjustment, unless explicitly a constraint",
            status="RISK",
            risk="Acausal hidden constraint or nonlocal repair.",
            missing="Local versus constrained/nonlocal status of kappa_min projection.",
        ),
    ]


def print_requirement(k: KappaRequirement) -> None:
    print()
    print("-" * 120)
    print(k.name)
    print("-" * 120)
    print(f"Requirement: {k.requirement}")
    print(f"Candidate form: {k.candidate_form}")
    print(f"Forbidden form: {k.forbidden_form}")
    status_line(k.name, k.status)
    print(f"Risk: {k.risk}")
    print(f"Missing: {k.missing}")


def case_0_problem_statement():
    header("Case 0: Kappa covariant relaxation requirement problem")

    print("Question:")
    print()
    print("  What must kappa relaxation require to be frame-consistent or covariant?")
    print()
    print("Goal:")
    print()
    print("  preserve first-order trace relaxation without hiding a preferred-frame scalar wave")
    print()
    print("Discipline:")
    print()
    print("  do not allow Box kappa")
    print("  do not leave dot(kappa) frame-undefined")
    print("  do not let kappa carry rho")
    print("  do not let relaxation destroy energy")

    status_line("kappa covariant relaxation problem posed", "REQUIRED")


def case_1_requirement_inventory(entries: List[KappaRequirement]):
    header("Case 1: Kappa requirement inventory")
    for entry in entries:
        print_requirement(entry)


def case_2_compact_table(entries: List[KappaRequirement]):
    header("Case 2: Compact kappa relaxation ledger")

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

    status_line("compact kappa ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[KappaRequirement]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Kappa's first-order role is constrained/structural.")
    print("  The major unresolved issue is the frame field or derivative direction.")
    print("  Energy accounting remains missing.")

    status_line("kappa status count produced", "STRUCTURAL")


def case_4_candidate_covariantized_form():
    header("Case 4: Candidate covariantized form")

    print("Candidate frame-compatible relaxation form:")
    print()
    print("  u^mu nabla_mu kappa = -lambda_kappa (kappa - kappa_min)")
    print()
    print("where:")
    print()
    print("  lambda_kappa = mu_kappa K_kappa")
    print("  kappa_min = chi_kappa S_trace_effective")
    print()
    print("Exterior ordinary vacuum:")
    print()
    print("  S_trace_effective = 0")
    print("  kappa_min = 0")
    print("  kappa -> 0")
    print()
    print("This is not yet derived.")
    print("It is a requirement-shaped candidate.")

    status_line("candidate covariantized kappa form stated", "CANDIDATE")


def case_5_frame_options():
    header("Case 5: Possible frame choices")

    print("Possible choices for u^mu:")
    print()
    print("1. Matter-comoving frame.")
    print("   Pro: tied to source material.")
    print("   Risk: exterior vacuum frame unclear.")
    print()
    print("2. Vacuum-substance flow frame.")
    print("   Pro: ontology-native.")
    print("   Risk: q_v/J_v not yet defined.")
    print()
    print("3. Normal to constraint foliation.")
    print("   Pro: compatible with constraint/evolution split.")
    print("   Risk: explicit preferred slicing.")
    print()
    print("4. Effective local equilibrium frame.")
    print("   Pro: tied to kappa_min/restoring minimum.")
    print("   Risk: needs definition from parent identity.")
    print()
    print("No choice is final.")

    status_line("kappa frame options listed", "UNRESOLVED")


def case_6_failure_controls():
    header("Case 6: Failure controls")

    print("Kappa covariant relaxation fails if:")
    print()
    print("1. dot(kappa) remains frame-undefined.")
    print("2. Box kappa appears.")
    print("3. kappa_min is coordinate-defined rather than scalar/frame-defined.")
    print("4. exterior kappa does not relax to zero.")
    print("5. boundary kappa flux creates exterior charge.")
    print("6. relaxation removes energy without destination.")
    print("7. rho sources kappa as a second mass field.")
    print("8. recombination uses kappa as duplicate scalar response.")

    status_line("kappa failure controls stated", "RISK")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_kappa_covariant_relaxation_requirement.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_boundary_mass_preservation_identity.py")
    print("   Prove or require that kappa/boundary relaxation cannot change exterior mass.")
    print()
    print("3. candidate_recombination_without_double_counting.py")
    print("   Try a disciplined recombination map.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_boundary_mass_preservation_identity.py")
    print()
    print("Reason:")
    print("  Kappa relaxation is only safe if boundary/exterior mass preservation is enforced.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("Kappa can remain safe only if:")
    print()
    print("  dot(kappa) is replaced by a defined flow derivative")
    print("  kappa remains first-order")
    print("  kappa_min is scalar/frame-defined")
    print("  exterior kappa relaxes to zero")
    print("  boundary kappa flux vanishes")
    print("  relaxation energy is accounted")
    print("  rho does not source kappa")
    print("  recombination does not use kappa as duplicate scalar mass response")
    print()
    print("Possible next artifact:")
    print("  candidate_kappa_covariant_relaxation_requirement.md")
    print()
    print("Possible next script:")
    print("  candidate_boundary_mass_preservation_identity.py")


def main():
    header("Candidate Kappa Covariant Relaxation Requirement")
    case_0_problem_statement()
    entries = build_requirements()
    case_1_requirement_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_candidate_covariantized_form()
    case_5_frame_options()
    case_6_failure_controls()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
