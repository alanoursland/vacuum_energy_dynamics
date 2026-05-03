# Candidate field equation closure failure modes
#
# Purpose
# -------
# The parent identity template created a scaffold:
#
#   Div E_parent[A,W,h_TT,kappa]
#     = B_closed[T] + B_active[Sigma_creation] + B_relax[Gamma_relax]
#
# But it explicitly did not derive closure.
#
# This script lists ways full field-equation closure can fail.
#
# Goal:
#
#   protect the project from decorative ontology,
#   silent GR import,
#   scalar double-counting,
#   matched coefficients claimed as derived,
#   kappa repair-knob behavior,
#   and unearned observational claims.
#
# This is a failure audit, not a derivation.

from dataclasses import dataclass
from typing import List


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def status_line(label: str, status: str, detail: str = "") -> None:
    marks = {
        "FATAL": "FAIL",
        "MAJOR": "FAIL",
        "RISK": "WARN",
        "CONTROLLED": "PASS",
        "UNRESOLVED": "FAIL",
        "WATCH": "WARN",
    }
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")


@dataclass
class FailureMode:
    name: str
    description: str
    severity: str
    symptom: str
    prevention: str
    current_status: str
    next_check: str


def build_failures() -> List[FailureMode]:
    return [
        FailureMode(
            name="F1: Decorative parent identity",
            description="The parent identity merely renames the Bianchi identity without deriving it from vacuum ontology.",
            severity="FATAL",
            symptom="Div E_parent is asserted to vanish because GR does, not because the vacuum-curvature structure forces it.",
            prevention="Demand definitions of E_parent and B_source plus reduced-sector implications.",
            current_status="UNRESOLVED",
            next_check="candidate_parent_identity_reduced_implications.py",
        ),
        FailureMode(
            name="F2: Silent GR metric import",
            description="Metric recombination copies GR component structure while claiming reconstruction.",
            severity="MAJOR",
            symptom="g_tt, g_0i, g_ij are assigned GR forms before ontology-derived recombination.",
            prevention="Keep recombination map labeled reduced/structural/unfinished.",
            current_status="WATCH",
            next_check="candidate_metric_recombination_parent_requirements.py",
        ),
        FailureMode(
            name="F3: Scalar double-counting",
            description="rho or trace sources both A and an independent scalar/kappa channel.",
            severity="FATAL",
            symptom="A carries mass field while kappa also creates exterior 1/r response.",
            prevention="Enforce S_kappa[rho]=0 and Q_kappa=0 unless parent identity says otherwise.",
            current_status="CONTROLLED",
            next_check="candidate_no_double_counting_constraints.py",
        ),
        FailureMode(
            name="F4: Kappa repair knob",
            description="kappa is adjusted to fix contradictions without an equation/source identity.",
            severity="MAJOR",
            symptom="kappa absorbs every mismatch: pressure, boundary, scalar radiation, interior curvature, and metric trace.",
            prevention="Restrict kappa to non-inertial trace/minimum relaxation with exterior zero-flux rules.",
            current_status="WATCH",
            next_check="candidate_kappa_non_radiative_trace_identity.py",
        ),
        FailureMode(
            name="F5: Hidden breathing wave",
            description="kappa gains a second-order wave equation or independent momentum channel.",
            severity="FATAL",
            symptom="Box kappa = source, scalar radiation power, or exterior breathing polarization appears.",
            prevention="Forbid ordinary massless kappa propagation unless separately derived and controlled.",
            current_status="CONTROLLED",
            next_check="candidate_constraint_vs_evolution_split.py",
        ),
        FailureMode(
            name="F6: Tensor coupling matched but claimed derived",
            description="C_T or the tensor flux coefficient is imported from GR.",
            severity="MAJOR",
            symptom="2G/c^4, 16*pi*G/c^4, or c^3/(32*pi*G) appears as target matching.",
            prevention="Mark tensor coupling/flux as MATCHED until action stiffness derives them.",
            current_status="UNRESOLVED",
            next_check="candidate_tensor_action_stiffness_revisit.py",
        ),
        FailureMode(
            name="F7: Vector normalization matched but claimed derived",
            description="Frame-dragging coefficient is set to the Lense-Thirring value by hand.",
            severity="MAJOR",
            symptom="W_i shape is used to claim full frame-dragging recovery without beta_W and alpha_W/K_c derivation.",
            prevention="Separate vector shape from normalization.",
            current_status="UNRESOLVED",
            next_check="candidate_vector_normalization_closure.py",
        ),
        FailureMode(
            name="F8: Boundary smoothing tunes measured mass",
            description="kappa or joint-minimum smoothing changes exterior A flux.",
            severity="FATAL",
            symptom="near-boundary relaxation changes M_ext or exterior 1/r coefficient.",
            prevention="Require delta M_ext = 0 under kappa boundary relaxation.",
            current_status="WATCH",
            next_check="candidate_boundary_mass_preservation_identity.py",
        ),
        FailureMode(
            name="F9: Active-regime leakage",
            description="Sigma_creation enters ordinary closed gravity equations.",
            severity="MAJOR",
            symptom="ordinary matter sources include creation/exchange terms without active-regime trigger.",
            prevention="Set Sigma_creation=0 in ordinary closed regime.",
            current_status="CONTROLLED",
            next_check="candidate_active_regime_exclusion_rule.py",
        ),
        FailureMode(
            name="F10: Relaxation as energy loss",
            description="Gamma_relax is treated as damping that removes energy from the system.",
            severity="MAJOR",
            symptom="trace imbalance disappears without destination variable.",
            prevention="Require vacuum configuration energy accounting.",
            current_status="WATCH",
            next_check="candidate_relaxation_energy_accounting_identity.py",
        ),
        FailureMode(
            name="F11: Near-boundary deviation overclaim",
            description="A possible near-boundary deviation from GR is claimed before magnitude or observable is derived.",
            severity="RISK",
            symptom="theory advertises unmeasured prediction from spline/joint-minimum diagnostic alone.",
            prevention="Diagnostic before prediction; require weights, sigma, recombination map, observable.",
            current_status="CONTROLLED",
            next_check="candidate_near_boundary_observability_gate.py",
        ),
        FailureMode(
            name="F12: Sector ledger mistaken for closure",
            description="A well-organized sector table is treated as a closed field-equation theory.",
            severity="FATAL",
            symptom="inventory, source split, and constraints are described as derivation of full field equations.",
            prevention="Keep closure status MISSING until parent identity and recombination are derived.",
            current_status="WATCH",
            next_check="field_equation_closure_summary.md",
        ),
    ]


def print_failure(f: FailureMode) -> None:
    print()
    print("-" * 120)
    print(f.name)
    print("-" * 120)
    print(f"Description: {f.description}")
    status_line(f.name, f.severity, f.current_status)
    print(f"Symptom: {f.symptom}")
    print(f"Prevention: {f.prevention}")
    print(f"Next check: {f.next_check}")


def case_0_problem_statement():
    header("Case 0: Field equation closure failure modes problem")

    print("Question:")
    print()
    print("  How can the attempted field-equation closure fail?")
    print()
    print("Goal:")
    print()
    print("  list failure modes before attempting a stronger parent identity")
    print()
    print("Discipline:")
    print()
    print("  do not confuse scaffolds with derivations")
    print("  do not claim matched coefficients are derived")
    print("  do not let kappa become a repair knob")
    print("  do not let organized sectors masquerade as closure")

    status_line("closure failure problem posed", "RISK")


def case_1_failure_inventory(entries: List[FailureMode]):
    header("Case 1: Failure mode inventory")
    for entry in entries:
        print_failure(entry)


def case_2_compact_table(entries: List[FailureMode]):
    header("Case 2: Compact failure ledger")

    print("| Failure mode | Severity | Current status | Prevention |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.severity
            + " | "
            + e.current_status
            + " | "
            + e.prevention.replace("|", "/")
            + " |"
        )

    status_line("compact failure ledger produced", "RISK")


def case_3_most_dangerous_failures(entries: List[FailureMode]):
    header("Case 3: Most dangerous failures")

    fatal = [e for e in entries if e.severity == "FATAL"]

    print("Fatal closure failures:")
    print()
    for e in fatal:
        print(f"  {e.name}")
    print()
    print("These would invalidate the closure claim rather than merely delay it.")

    status_line("fatal failures identified", "FATAL", "closure claim unsafe until controlled")


def case_4_current_controls():
    header("Case 4: Current controls")

    print("Currently partially controlled:")
    print()
    print("  scalar double-counting")
    print("  hidden breathing wave")
    print("  active-regime leakage")
    print("  near-boundary deviation overclaim")
    print()
    print("Still unresolved:")
    print()
    print("  parent identity derivation")
    print("  tensor coupling")
    print("  vector normalization")
    print("  covariant recombination")
    print("  boundary mass theorem")
    print("  relaxation energy accounting")

    status_line("current controls summarized", "WATCH")


def case_5_next_tests():
    header("Case 5: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_field_equation_closure_failure_modes.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_closure_minimal_equation_set.py")
    print("   Assemble current minimal equation set with labels.")
    print()
    print("3. candidate_parent_identity_reduced_implications.py")
    print("   Test what the parent identity must imply in reduced sectors.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_closure_minimal_equation_set.py")
    print()
    print("Reason:")
    print("  The failure ledger is protective; now assemble the minimal current equation set with labels.")

    status_line("next test selected", "WATCH")


def final_interpretation():
    header("Final interpretation")

    print("The closure attempt can fail in three main ways:")
    print()
    print("  1. decorative identity")
    print("  2. silent GR import")
    print("  3. scalar/source double-counting")
    print()
    print("It can also fail through matched coefficients, kappa repair-knob behavior,")
    print("boundary mass tuning, active-regime leakage, and overclaimed predictions.")
    print()
    print("Possible next artifact:")
    print("  candidate_field_equation_closure_failure_modes.md")
    print()
    print("Possible next script:")
    print("  candidate_closure_minimal_equation_set.py")


def main():
    header("Candidate Field Equation Closure Failure Modes")
    case_0_problem_statement()
    entries = build_failures()
    case_1_failure_inventory(entries)
    case_2_compact_table(entries)
    case_3_most_dangerous_failures(entries)
    case_4_current_controls()
    case_5_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
