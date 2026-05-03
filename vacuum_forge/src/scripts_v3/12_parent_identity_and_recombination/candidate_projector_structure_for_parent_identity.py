# Candidate projector structure for parent identity
#
# Purpose
# -------
# The reduced-implication test suite showed that any parent identity must imply:
#
#   A scalar constraint,
#   transverse W_i sourcing,
#   TT-only radiation,
#   kappa trace relaxation,
#   exterior kappa neutrality,
#   boundary mass preservation,
#   recombination without scalar double-counting.
#
# These implications require projectors.
#
# This script audits the projector structure needed for a parent identity:
#
#   P_scalar
#   P_L
#   P_T
#   P_TT
#   P_trace
#   P_relax
#   P_boundary
#   P_recombination
#
# It does not derive the projectors covariantly.
# It builds a projector requirement ledger.

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
        "FORMAL": "WARN",
        "MISSING": "FAIL",
        "UNRESOLVED": "FAIL",
        "RISK": "WARN",
    }
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")


@dataclass
class ProjectorEntry:
    name: str
    acts_on: str
    feeds: str
    excludes: str
    schematic_form: str
    status: str
    risk: str
    missing: str


def build_projectors() -> List[ProjectorEntry]:
    return [
        ProjectorEntry(
            name="P_scalar",
            acts_on="density / scalar source content",
            feeds="A-sector scalar constraint",
            excludes="ordinary scalar radiation A_rad and independent kappa charge",
            schematic_form="P_scalar[T] -> rho_eff -> C_A[A,rho]",
            status="STRUCTURAL",
            risk="Scalar source leaks into A_rad or kappa.",
            missing="Parent definition of scalar charge and areal operator.",
        ),
        ProjectorEntry(
            name="P_L",
            acts_on="matter current j",
            feeds="scalar continuity / density redistribution",
            excludes="transverse W_i source",
            schematic_form="P_L j = grad Delta^{-1} div j",
            status="DERIVED_REDUCED",
            risk="Longitudinal current contaminates frame dragging.",
            missing="Covariant or curved-background generalization.",
        ),
        ProjectorEntry(
            name="P_T",
            acts_on="matter current j",
            feeds="W_i transverse vector response",
            excludes="scalar continuity source",
            schematic_form="P_T = I - k k^T/k^2 in Fourier space",
            status="DERIVED_REDUCED",
            risk="Vector sector receives gauge/longitudinal current.",
            missing="Parent current projection and normalization.",
        ),
        ProjectorEntry(
            name="P_TT",
            acts_on="spatial stress / quadrupole source S_ij",
            feeds="h_ij^TT tensor radiation",
            excludes="trace stress, pressure, scalar/kappa response",
            schematic_form="P_TT S_ij = transverse trace-free projection",
            status="STRUCTURAL",
            risk="Trace contamination of TT radiation.",
            missing="Parent TT source identity and tensor coupling C_T.",
        ),
        ProjectorEntry(
            name="P_trace",
            acts_on="stress trace / pressure / volume imbalance",
            feeds="kappa_min shift",
            excludes="A-sector rho source, h_TT, Box kappa radiation",
            schematic_form="P_trace[T] -> S_trace_effective -> kappa_min",
            status="STRUCTURAL",
            risk="Trace becomes a scalar wave or repair knob.",
            missing="S_trace_effective and chi_kappa.",
        ),
        ProjectorEntry(
            name="P_relax",
            acts_on="kappa - kappa_min imbalance",
            feeds="first-order kappa relaxation / vacuum restoration",
            excludes="second-order kappa momentum channel",
            schematic_form="P_relax: kappa-kappa_min -> dot kappa = -mu K (kappa-kappa_min)",
            status="CONSTRAINED",
            risk="Hidden breathing wave or energy loss.",
            missing="Vacuum configuration energy accounting.",
        ),
        ProjectorEntry(
            name="P_boundary",
            acts_on="boundary / interface relaxation data",
            feeds="local smoothing or kappa boundary condition",
            excludes="change in exterior A mass flux",
            schematic_form="P_boundary enforces delta M_ext = 0 and F_kappa(R+) = 0",
            status="CONSTRAINED",
            risk="Boundary smoothing tunes measured mass.",
            missing="Boundary mass preservation theorem.",
        ),
        ProjectorEntry(
            name="P_closed",
            acts_on="active-regime source balance",
            feeds="ordinary closed gravity sector",
            excludes="Sigma_creation",
            schematic_form="P_closed: Sigma_creation -> 0 in ordinary regime",
            status="CONSTRAINED",
            risk="Active-regime leakage into ordinary gravity.",
            missing="Active-regime trigger/exclusion law.",
        ),
        ProjectorEntry(
            name="P_recombination",
            acts_on="sector fields A, W_i, h_TT, kappa",
            feeds="metric / geometry-like recombination map",
            excludes="scalar double-counting and GR form-copying",
            schematic_form="R[A,W,h_TT,kappa] -> g-like object",
            status="UNRESOLVED",
            risk="Silent GR metric import.",
            missing="Covariant or reduced parent recombination identity.",
        ),
        ProjectorEntry(
            name="P_coeff",
            acts_on="parent action / stiffness constants",
            feeds="alpha_W/K_c, beta_W, C_T, K_T",
            excludes="coefficient matching by hand",
            schematic_form="parent stiffness/coupling projection -> observable coefficients",
            status="MISSING",
            risk="GR coefficients inserted as derivation.",
            missing="Action/stiffness derivation.",
        ),
    ]


def print_projector(p: ProjectorEntry) -> None:
    print()
    print("-" * 120)
    print(p.name)
    print("-" * 120)
    print(f"Acts on: {p.acts_on}")
    print(f"Feeds: {p.feeds}")
    print(f"Excludes: {p.excludes}")
    print(f"Schematic form: {p.schematic_form}")
    status_line(p.name, p.status)
    print(f"Risk: {p.risk}")
    print(f"Missing: {p.missing}")


def case_0_problem_statement():
    header("Case 0: Projector structure problem")

    print("Question:")
    print()
    print("  What projector structure is required for a parent identity?")
    print()
    print("Goal:")
    print()
    print("  make source/sector routing explicit before trying a parent identity")
    print()
    print("Discipline:")
    print()
    print("  projectors are not derivations")
    print("  projectors must prevent forbidden overlaps")
    print("  recombination must come after source splitting")

    status_line("projector structure problem posed", "STRUCTURAL")


def case_1_projector_inventory(entries: List[ProjectorEntry]):
    header("Case 1: Projector inventory")
    for entry in entries:
        print_projector(entry)


def case_2_compact_table(entries: List[ProjectorEntry]):
    header("Case 2: Compact projector ledger")

    print("| Projector | Feeds | Excludes | Status | Missing |")
    print("|---|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.feeds.replace("|", "/")
            + " | "
            + e.excludes.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.missing.replace("|", "/")
            + " |"
        )

    status_line("compact projector ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[ProjectorEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Reduced current projectors P_L and P_T are the clearest.")
    print("  Scalar, TT, trace, and relaxation projectors are structural.")
    print("  Recombination and coefficient projectors remain unresolved/missing.")

    status_line("projector status count produced", "STRUCTURAL")


def case_4_required_decomposition():
    header("Case 4: Required source decomposition")

    print("Parent source decomposition must route:")
    print()
    print("  rho / scalar charge -> P_scalar -> A")
    print("  longitudinal current -> P_L -> scalar continuity")
    print("  transverse current -> P_T -> W_i")
    print("  TT stress -> P_TT -> h_ij^TT")
    print("  trace / pressure -> P_trace -> kappa_min")
    print("  kappa imbalance -> P_relax -> first-order relaxation")
    print("  boundary data -> P_boundary -> M_ext preservation and kappa exterior safety")
    print("  active-regime terms -> P_closed -> Sigma_creation=0 in ordinary regime")
    print("  sector fields -> P_recombination -> geometry without double-counting")

    status_line("required source decomposition stated", "CONSTRAINED")


def case_5_projector_consistency_tests():
    header("Case 5: Projector consistency tests")

    print("Projector tests:")
    print()
    print("1. P_scalar rho must not feed A_rad.")
    print("2. P_scalar rho must not feed long-range kappa.")
    print("3. P_T j must be divergence-free/transverse.")
    print("4. P_L j must not feed curl W.")
    print("5. P_TT S must be trace-free.")
    print("6. P_trace T must not feed h_TT.")
    print("7. P_trace T must not create Box kappa.")
    print("8. P_boundary must preserve M_ext.")
    print("9. P_closed must set Sigma_creation=0 in ordinary gravity.")
    print("10. P_recombination must count scalar response exactly once.")

    status_line("projector consistency tests stated", "CONSTRAINED")


def case_6_hardest_projectors():
    header("Case 6: Hardest projectors")

    print("Hardest projectors:")
    print()
    print("1. P_scalar:")
    print("   must explain A as constraint rather than scalar radiation.")
    print()
    print("2. P_trace / P_relax:")
    print("   must explain kappa relaxation rather than Box kappa.")
    print()
    print("3. P_boundary:")
    print("   must preserve exterior mass under boundary smoothing.")
    print()
    print("4. P_recombination:")
    print("   must produce geometry without silent GR import.")
    print()
    print("5. P_coeff:")
    print("   must derive vector/tensor coefficients rather than matching them.")

    status_line("hardest projectors identified", "RISK")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_projector_structure_for_parent_identity.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_scalar_constraint_not_radiation_identity.py")
    print("   Focus on why A constrains rather than radiates.")
    print()
    print("3. candidate_kappa_covariant_relaxation_requirement.py")
    print("   Focus on kappa's first-order relaxation and frame/covariance issue.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_scalar_constraint_not_radiation_identity.py")
    print()
    print("Reason:")
    print("  P_scalar is the hardest immediate gate: the parent must explain scalar constraint, not scalar radiation.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("The parent identity needs projectors before it can be meaningful.")
    print()
    print("Current clearest projectors:")
    print("  P_L")
    print("  P_T")
    print()
    print("Current structural projectors:")
    print("  P_scalar")
    print("  P_TT")
    print("  P_trace")
    print("  P_relax")
    print("  P_boundary")
    print()
    print("Current unresolved/missing projectors:")
    print("  P_recombination")
    print("  P_coeff")
    print()
    print("Possible next artifact:")
    print("  candidate_projector_structure_for_parent_identity.md")
    print()
    print("Possible next script:")
    print("  candidate_scalar_constraint_not_radiation_identity.py")


def main():
    header("Candidate Projector Structure for Parent Identity")
    case_0_problem_statement()
    entries = build_projectors()
    case_1_projector_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_required_decomposition()
    case_5_projector_consistency_tests()
    case_6_hardest_projectors()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
