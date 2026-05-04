# Candidate volume form configuration variable
#
# Purpose
# -------
# The vacuum substance accounting inventory found:
#
#   E_vac_config must be geometric or tightly constrained bookkeeping.
#   The best immediate geometric targets are sqrt_gamma and ln_sqrt_gamma.
#
# This script tests whether vacuum-spacetime configuration can be represented
# by a volume-form variable.
#
# Corrected ontology:
#
#   vacuum is spacetime.
#   creating vacuum creates spacetime.
#   changing local spacetime creates curvature.
#
# Therefore a natural candidate is:
#
#   physical volume element = sqrt(gamma) d^3x
#
# and a natural local strain variable is:
#
#   zeta = ln sqrt(gamma)
#
# This script is not a derivation.
# It is a candidate-variable audit.

from dataclasses import dataclass
from typing import List


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def status_line(label: str, status: str, detail: str = "") -> None:
    marks = {
        "CANDIDATE": "WARN",
        "STRUCTURAL": "WARN",
        "CONSTRAINED": "WARN",
        "REQUIRED": "WARN",
        "MISSING": "FAIL",
        "UNRESOLVED": "FAIL",
        "RISK": "WARN",
        "FORBIDDEN": "PASS",
        "REJECTED": "WARN",
        "DERIVED_REDUCED": "PASS",
    }
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")


@dataclass
class VolumeCandidate:
    name: str
    candidate_form: str
    role: str
    allowed_use: str
    forbidden_use: str
    status: str
    missing: str
    next_test: str


def build_candidates() -> List[VolumeCandidate]:
    return [
        VolumeCandidate(
            name="V1: physical volume element",
            candidate_form="dV_phys = sqrt(gamma) d^3x",
            role="Geometric expression of local vacuum/spacetime amount in a chosen slice.",
            allowed_use="candidate basis for epsilon_vac_config",
            forbidden_use="treated as gauge-invariant observable without slicing/frame definition",
            status="CANDIDATE",
            missing="choice of spatial metric gamma_ij and foliation/frame",
            next_test="trace_vs_TT_split",
        ),
        VolumeCandidate(
            name="V2: logarithmic volume strain",
            candidate_form="zeta = ln sqrt(gamma)",
            role="Additive local trace/volume configuration variable.",
            allowed_use="candidate scalar/trace conversion variable",
            forbidden_use="duplicate A-sector mass response or exterior scalar charge",
            status="CANDIDATE",
            missing="reference volume / background subtraction and relation to kappa",
            next_test="trace_vs_TT_split",
        ),
        VolumeCandidate(
            name="V3: perturbative trace relation",
            candidate_form="delta zeta = 1/2 gamma^ij delta gamma_ij",
            role="Shows that volume change is trace part of spatial metric perturbation.",
            allowed_use="separate trace/volume channel from TT shear",
            forbidden_use="allowing trace to source h_TT or scalar radiation",
            status="STRUCTURAL",
            missing="parent projector P_trace",
            next_test="candidate_trace_vs_tt_geometric_split.py",
        ),
        VolumeCandidate(
            name="V4: TT volume preservation",
            candidate_form="gamma^ij h_ij^TT = 0 -> delta zeta|TT = 0",
            role="Candidate reason TT modes propagate without vacuum creation/destruction.",
            allowed_use="theorem target behind TT-only radiation",
            forbidden_use="claiming theorem before parent projector derivation",
            status="CANDIDATE",
            missing="full nonlinear/covariant statement and TT source identity",
            next_test="candidate_trace_vs_tt_geometric_split.py",
        ),
        VolumeCandidate(
            name="V5: 1D toy analog",
            candidate_form="ds = e^phi dx, so zeta_1D = phi",
            role="Concrete analog: local expansion field multiplies physical length.",
            allowed_use="intuition and toy diagnostic for volume-form accounting",
            forbidden_use="importing the toy's irreversible reservoir R as theory",
            status="STRUCTURAL",
            missing="higher-dimensional generalization and conservative exchange law",
            next_test="scalar_conversion_not_damping",
        ),
        VolumeCandidate(
            name="V6: kappa relation candidate",
            candidate_form="kappa ~ zeta - zeta_min or kappa = 1/2 ln(AB) in reduced areal gauge",
            role="Relates kappa to volume/trace mismatch rather than independent scalar field.",
            allowed_use="kappa as constrained trace/volume relaxation diagnostic",
            forbidden_use="kappa as rho-sourced exterior scalar charge",
            status="CANDIDATE",
            missing="precise map between kappa and volume-form strain",
            next_test="candidate_scalar_conversion_not_damping.py",
        ),
        VolumeCandidate(
            name="V7: epsilon_vac_config candidate",
            candidate_form="epsilon_vac_config = F(zeta, zeta_min, grad zeta, ...)",
            role="Geometric local configuration density built from volume strain.",
            allowed_use="destination/source for scalar/trace conversion",
            forbidden_use="bottomless reservoir or coefficient tuning functional",
            status="CANDIDATE",
            missing="functional form F and stiffness coefficients",
            next_test="vacuum_accounting_parent_balance",
        ),
        VolumeCandidate(
            name="V8: A-sector separation",
            candidate_form="M_ext determined by A_flux, not by integral zeta",
            role="Protects exterior mass from volume-form relaxation.",
            allowed_use="volume reconfiguration may be compact/compensated while A_flux remains fixed",
            forbidden_use="using volume strain integral to alter exterior mass",
            status="CONSTRAINED",
            missing="boundary volume mode no exterior charge theorem",
            next_test="candidate_boundary_volume_mode_no_exterior_charge.py",
        ),
        VolumeCandidate(
            name="V9: exterior neutrality",
            candidate_form="zeta_ext -> 0, kappa_ext -> 0, Q_volume = 0",
            role="Prevents volume-form scalar tail outside ordinary matter.",
            allowed_use="compact or compensated trace/volume reconfiguration",
            forbidden_use="zeta_ext ~ 1/r scalar charge",
            status="CONSTRAINED",
            missing="projection/boundary theorem",
            next_test="candidate_boundary_volume_mode_no_exterior_charge.py",
        ),
        VolumeCandidate(
            name="V10: slicing/frame caveat",
            candidate_form="zeta = ln sqrt(gamma) depends on spatial decomposition",
            role="Flags that volume-form accounting needs a frame/foliation or covariant replacement.",
            allowed_use="temporary reduced/3+1 candidate",
            forbidden_use="pretending zeta is fully covariant without extra structure",
            status="UNRESOLVED",
            missing="frame u^mu, foliation, or covariant volume current",
            next_test="candidate_vacuum_transport_current_constraints.py",
        ),
    ]


def print_candidate(v: VolumeCandidate) -> None:
    print()
    print("-" * 120)
    print(v.name)
    print("-" * 120)
    print(f"Candidate form: {v.candidate_form}")
    print(f"Role: {v.role}")
    print(f"Allowed use: {v.allowed_use}")
    print(f"Forbidden use: {v.forbidden_use}")
    status_line(v.name, v.status)
    print(f"Missing: {v.missing}")
    print(f"Next test: {v.next_test}")


def case_0_problem_statement():
    header("Case 0: Volume-form configuration variable problem")

    print("Question:")
    print()
    print("  Can vacuum-spacetime configuration be represented by a volume-form variable?")
    print()
    print("Goal:")
    print()
    print("  test sqrt(gamma) and ln sqrt(gamma) as geometric candidates for epsilon_vac_config")
    print()
    print("Discipline:")
    print()
    print("  volume form is geometric but slicing/frame dependent")
    print("  volume strain must not duplicate A-sector mass")
    print("  TT modes should be volume-preserving")
    print("  scalar/trace modes should be conversion-limited")
    print("  do not import the 1D toy's one-way reservoir as theory")

    status_line("volume-form problem posed", "REQUIRED")


def case_1_candidate_inventory(entries: List[VolumeCandidate]):
    header("Case 1: Volume-form candidate inventory")
    for entry in entries:
        print_candidate(entry)


def case_2_compact_table(entries: List[VolumeCandidate]):
    header("Case 2: Compact volume-form ledger")

    print("| Candidate | Role | Status | Forbidden use | Missing |")
    print("|---|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.candidate_form.replace("|", "/")
            + " | "
            + e.role.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.forbidden_use.replace("|", "/")
            + " | "
            + e.missing.replace("|", "/")
            + " |"
        )

    status_line("compact volume-form ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[VolumeCandidate]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  The volume-form candidate is promising but not covariant yet.")
    print("  The key structural fact is that TT perturbations are trace-free, hence volume-preserving at linear order.")
    print("  The key risk is duplicating A-sector scalar mass response.")

    status_line("volume-form status count produced", "STRUCTURAL")


def case_4_minimal_candidate_definition():
    header("Case 4: Minimal candidate definition")

    print("Minimal candidate:")
    print()
    print("  zeta = ln sqrt(gamma)")
    print()
    print("Perturbative variation:")
    print()
    print("  delta zeta = 1/2 gamma^ij delta gamma_ij")
    print()
    print("TT perturbation:")
    print()
    print("  gamma^ij h_ij^TT = 0")
    print()
    print("Therefore:")
    print()
    print("  delta zeta|TT = 0")
    print()
    print("Interpretation:")
    print()
    print("  trace/volume modes change vacuum-spacetime amount")
    print("  TT modes are volume-preserving shear")
    print()
    print("This is a linear structural observation, not a full theorem.")

    status_line("minimal volume-form candidate stated", "CANDIDATE")


def case_5_relation_to_1d_toy():
    header("Case 5: Relation to 1D toy model")

    print("The 1D toy has:")
    print()
    print("  ds = e^phi dx")
    print()
    print("so:")
    print()
    print("  phi = ln(ds/dx)")
    print()
    print("This is the 1D analog of:")
    print()
    print("  zeta = ln sqrt(gamma)")
    print()
    print("Useful extraction:")
    print()
    print("  physical length/volume is coordinate measure multiplied by a vacuum-configuration factor")
    print()
    print("Rejected extraction:")
    print()
    print("  a one-way thermodynamic reservoir R as final theory")
    print()
    print("Reinterpreted extraction:")
    print()
    print("  scalar/trace conversion changes the geometry/volume-form variable itself")

    status_line("1D toy relation stated", "STRUCTURAL")


def case_6_failure_controls():
    header("Case 6: Failure controls")

    print("The volume-form candidate fails if:")
    print()
    print("1. zeta duplicates A-sector exterior mass.")
    print("2. zeta produces an exterior 1/r scalar tail.")
    print("3. zeta is treated as gauge-invariant without frame/foliation.")
    print("4. kappa and zeta become independent scalar charges.")
    print("5. TT modes accidentally change volume.")
    print("6. scalar conversion becomes far-zone scalar radiation.")
    print("7. epsilon_vac_config becomes a coefficient tuning reservoir.")

    status_line("volume-form failure controls stated", "RISK")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_volume_form_configuration_variable.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_trace_vs_tt_geometric_split.py")
    print("   Formalize why trace/volume modes convert while TT modes propagate.")
    print()
    print("3. candidate_scalar_conversion_not_damping.py")
    print("   Replace damping language with conversion-limited scalar dynamics.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_trace_vs_tt_geometric_split.py")
    print()
    print("Reason:")
    print("  The volume-form candidate points directly to the trace/TT split as the possible TT-only radiation theorem.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("The best current geometric candidate is:")
    print()
    print("  zeta = ln sqrt(gamma)")
    print()
    print("with:")
    print()
    print("  dV_phys = sqrt(gamma) d^3x")
    print("  delta zeta = 1/2 gamma^ij delta gamma_ij")
    print("  delta zeta|TT = 0")
    print()
    print("Interpretation:")
    print()
    print("  trace/volume modes change vacuum-spacetime amount")
    print("  TT modes are volume-preserving shear")
    print()
    print("Possible next artifact:")
    print("  candidate_volume_form_configuration_variable.md")
    print()
    print("Possible next script:")
    print("  candidate_trace_vs_tt_geometric_split.py")


def main():
    header("Candidate Volume Form Configuration Variable")
    case_0_problem_statement()
    entries = build_candidates()
    case_1_candidate_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_minimal_candidate_definition()
    case_5_relation_to_1d_toy()
    case_6_failure_controls()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
