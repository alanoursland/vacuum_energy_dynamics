# Candidate constraint versus evolution split
#
# Purpose
# -------
# The no-double-counting constraints identified which sources must not be
# counted twice.
#
# The next closure question is:
#
#   which fields are constraints?
#   which fields relax?
#   which fields propagate?
#
# This script classifies:
#
#   A       -> scalar constraint / monopole field
#   W_i     -> transverse vector constraint / stationary response, possibly retarded in dynamics
#   h_TT    -> true propagating tensor radiation
#   kappa   -> non-inertial trace relaxation / constrained variable
#   A_rad   -> rejected ordinary scalar radiation
#
# This is an audit script, not a derivation.

from dataclasses import dataclass
from typing import List


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def status_line(label: str, status: str, detail: str = "") -> None:
    marks = {
        "DERIVED": "PASS",
        "DERIVED_REDUCED": "PASS",
        "STRUCTURAL": "WARN",
        "CONSTRAINED": "WARN",
        "MATCHED": "WARN",
        "MISSING": "FAIL",
        "RISK": "WARN",
        "REJECTED": "WARN",
        "UNFINISHED": "FAIL",
    }
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")


@dataclass
class DynamicsEntry:
    field: str
    sector: str
    classification: str
    schematic_equation: str
    propagates: str
    status: str
    risk: str
    missing: str


def build_entries() -> List[DynamicsEntry]:
    return [
        DynamicsEntry(
            field="A",
            sector="scalar monopole / areal flux",
            classification="constraint / elliptic-like scalar sector",
            schematic_equation="Delta_areal A = 8*pi*G*rho/c^2",
            propagates="No ordinary long-range scalar radiation; static/constraint field.",
            status="DERIVED_REDUCED",
            risk="Turning static scalar constraint into a propagating scalar wave.",
            missing="Full nonlinear nonspherical constraint propagation.",
        ),
        DynamicsEntry(
            field="B",
            sector="radial reciprocal scalar metric piece",
            classification="gauge-conditioned companion to A in exterior",
            schematic_equation="AB = exp(2*kappa); exterior kappa=0 -> B=1/A",
            propagates="No independent propagation in current reduced exterior.",
            status="DERIVED_REDUCED",
            risk="Treating gauge relation as independent dynamics.",
            missing="Covariant gauge/physical split.",
        ),
        DynamicsEntry(
            field="W_i",
            sector="transverse vector / frame dragging",
            classification="transverse vector constraint in stationary limit; possible retarded response dynamically",
            schematic_equation="curl curl W = -(alpha_W/(2K_c)) j_T",
            propagates="Not currently a free radiation sector; source-tied vector response.",
            status="STRUCTURAL",
            risk="Importing electromagnetic-like vector waves or GR shift dynamics by hand.",
            missing="Dynamic propagation/retardation law and normalization.",
        ),
        DynamicsEntry(
            field="h_ij^TT",
            sector="tensor radiation",
            classification="true propagating radiative degree of freedom",
            schematic_equation="Box h_ij^TT = -C_T S_ij^TT",
            propagates="Yes: ordinary long-range gravitational radiation.",
            status="STRUCTURAL",
            risk="Correct form but coefficient/source identity matched to GR.",
            missing="C_T and action stiffness derivation.",
        ),
        DynamicsEntry(
            field="kappa",
            sector="trace / volume relaxation",
            classification="non-inertial relaxation / constrained trace response",
            schematic_equation="dot kappa = -mu_kappa K_kappa (kappa-kappa_min)",
            propagates="No: no independent momentum channel; no ordinary breathing wave.",
            status="STRUCTURAL",
            risk="Becoming a hidden scalar wave or repair knob.",
            missing="K_kappa, mu_kappa, chi_kappa, S_trace_effective, covariant origin.",
        ),
        DynamicsEntry(
            field="A_rad",
            sector="scalar radiation hazard",
            classification="rejected ordinary massless scalar radiation sector",
            schematic_equation="source(A_rad ordinary massless) = 0",
            propagates="No; rejected unless separately derived and controlled.",
            status="REJECTED",
            risk="Breathing/scalar radiation contradicts safety constraints.",
            missing="Parent identity proving absence/suppression.",
        ),
        DynamicsEntry(
            field="Sigma_creation",
            sector="active regimes",
            classification="excluded from ordinary closed-gravity evolution",
            schematic_equation="Sigma_creation = 0 in ordinary closed regime",
            propagates="Not a field; source/regime switch.",
            status="CONSTRAINED",
            risk="Nonconservative source contaminates ordinary closure.",
            missing="Active-regime trigger and accounting.",
        ),
        DynamicsEntry(
            field="Gamma_relax",
            sector="vacuum relaxation / kappa equilibration",
            classification="energy-transfer / restoration term, not propagating mode",
            schematic_equation="Gamma_relax acts on trace imbalance, not A_mass_flux",
            propagates="No; local restoration/accounting term.",
            status="STRUCTURAL",
            risk="Cosmetic damping or energy disappearance.",
            missing="Vacuum energy destination / parent balance.",
        ),
    ]


def print_entry(e: DynamicsEntry) -> None:
    print()
    print("-" * 120)
    print(f"Field: {e.field}")
    print("-" * 120)
    print(f"Sector: {e.sector}")
    print(f"Classification: {e.classification}")
    print(f"Schematic equation: {e.schematic_equation}")
    print(f"Propagates? {e.propagates}")
    status_line(e.field, e.status)
    print(f"Risk: {e.risk}")
    print(f"Missing: {e.missing}")


def case_0_problem_statement():
    header("Case 0: Constraint versus evolution split problem")

    print("Question:")
    print()
    print("  Which fields are constraints, which relax, and which propagate?")
    print()
    print("Goal:")
    print()
    print("  avoid accidentally turning constraint sectors into radiative fields")
    print()
    print("Discipline:")
    print()
    print("  A is not scalar radiation")
    print("  kappa is not breathing radiation")
    print("  W_i is not automatically a free vector wave")
    print("  h_ij^TT is the true long-range radiation sector")

    status_line("constraint/evolution split problem posed", "CONSTRAINED")


def case_1_dynamics_inventory(entries: List[DynamicsEntry]):
    header("Case 1: Dynamics inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[DynamicsEntry]):
    header("Case 2: Compact dynamics ledger")

    print("| Field | Classification | Propagates? | Status |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.field.replace("|", "/")
            + " | "
            + e.classification.replace("|", "/")
            + " | "
            + e.propagates.replace("|", "/")
            + " | "
            + e.status
            + " |"
        )

    status_line("compact dynamics ledger produced", "STRUCTURAL")


def case_3_true_radiation_rule():
    header("Case 3: True radiation rule")

    print("Current radiation rule:")
    print()
    print("  ordinary long-range gravitational radiation is TT-only.")
    print()
    print("Allowed:")
    print("  h_ij^TT propagates.")
    print()
    print("Constrained/rejected:")
    print("  A_rad ordinary scalar radiation is rejected.")
    print("  kappa breathing radiation is rejected.")
    print("  W_i free vector radiation is not currently derived.")
    print()
    print("This rule can be changed only by a separate derivation and observational control.")

    status_line("TT-only ordinary radiation rule stated", "CONSTRAINED")


def case_4_constraint_fields():
    header("Case 4: Constraint fields")

    print("Constraint-like fields:")
    print()
    print("  A:")
    print("    scalar mass/monopole constraint")
    print()
    print("  B:")
    print("    reduced gauge-conditioned reciprocal companion to A")
    print()
    print("  W_i:")
    print("    transverse vector response in stationary/current sector")
    print()
    print("  kappa:")
    print("    non-inertial trace/volume relaxation constraint")
    print()
    print("These may have time-dependent source response, but they are not currently")
    print("ordinary free radiative degrees of freedom.")

    status_line("constraint-like fields listed", "CONSTRAINED")


def case_5_evolution_fields():
    header("Case 5: Evolution fields")

    print("Evolving/radiating fields:")
    print()
    print("  h_ij^TT:")
    print("    propagating tensor radiation")
    print()
    print("Possibly dynamic but not yet radiative:")
    print("  W_i:")
    print("    may require retardation/dynamic source response")
    print()
    print("  kappa:")
    print("    first-order relaxation toward local minimum")
    print()
    print("Rejected as ordinary radiative fields:")
    print("  A_rad")
    print("  kappa breathing wave")

    status_line("evolution fields classified", "STRUCTURAL")


def case_6_failure_controls():
    header("Case 6: Failure controls")

    print("Constraint/evolution split fails if:")
    print()
    print("1. A is promoted to a free scalar radiation field.")
    print("2. kappa gains a second-order Box equation and momentum channel.")
    print("3. W_i is treated as a free vector radiation field without derivation.")
    print("4. h_ij^TT coupling is copied from GR while claimed derived.")
    print("5. Gamma_relax hides energy loss rather than vacuum exchange.")
    print("6. Sigma_creation appears in ordinary closed gravity.")
    print("7. constraint propagation is not compatible with source conservation.")

    status_line("constraint/evolution failure controls stated", "RISK")


def case_7_parent_identity_requirements():
    header("Case 7: Parent identity requirements")

    print("The parent identity must explain:")
    print()
    print("  how constraints propagate consistently")
    print("  why TT modes alone carry ordinary radiation")
    print("  why scalar trace relaxes but does not radiate")
    print("  why vector current response is transverse")
    print("  how energy/source conservation is maintained")
    print()
    print("Without this, the split is disciplined but not derived.")

    status_line("parent identity requirements stated", "UNFINISHED")


def case_8_next_tests():
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_constraint_vs_evolution_split.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_conservation_identity_requirements.py")
    print("   List the parent identities needed to justify the constraints.")
    print()
    print("3. candidate_gr_limit_recovery_audit.py")
    print("   Audit where GR recovery is derived versus matched.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_conservation_identity_requirements.py")
    print()
    print("Reason:")
    print("  The split is now clear; the next gap is the identity that enforces it.")

    status_line("next test selected", "CONSTRAINED")


def final_interpretation():
    header("Final interpretation")

    print("Current split:")
    print()
    print("  A: constraint")
    print("  B: reduced gauge-conditioned companion")
    print("  W_i: transverse vector response, not free radiation")
    print("  h_ij^TT: true propagating radiation")
    print("  kappa: non-inertial trace relaxation, not breathing radiation")
    print("  A_rad: rejected ordinary scalar radiation")
    print()
    print("Possible next artifact:")
    print("  candidate_constraint_vs_evolution_split.md")
    print()
    print("Possible next script:")
    print("  candidate_conservation_identity_requirements.py")


def main():
    header("Candidate Constraint Versus Evolution Split")
    case_0_problem_statement()
    entries = build_entries()
    case_1_dynamics_inventory(entries)
    case_2_compact_table(entries)
    case_3_true_radiation_rule()
    case_4_constraint_fields()
    case_5_evolution_fields()
    case_6_failure_controls()
    case_7_parent_identity_requirements()
    case_8_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
