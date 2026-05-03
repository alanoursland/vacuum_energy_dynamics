# Candidate parent identity exclusion constraints
#
# Purpose
# -------
# Group 12 begins here.
#
# Group 11 ended with:
#
#   current reduced field-equation system is coherent enough to state,
#   but it is not closed.
#
# The missing object is a parent conservation / recombination identity.
#
# This script does NOT try to write the parent identity.
#
# Instead it asks:
#
#   What can the parent identity NOT be?
#
# The purpose is to rule out decorative, unsafe, or GR-importing parent identity
# forms before trying to construct a positive parent.
#
# Canonical location:
#   theory_v3/development/field_equation_candidates/12_parent_identity_and_recombination/
#   scripts_v3/12_parent_identity_and_recombination/candidate_parent_identity_exclusion_constraints.py

from dataclasses import dataclass
from typing import List


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def status_line(label: str, status: str, detail: str = "") -> None:
    marks = {
        "EXCLUDED": "PASS",
        "FORBIDDEN": "PASS",
        "CONSTRAINED": "WARN",
        "RISK": "WARN",
        "UNRESOLVED": "FAIL",
        "FATAL": "FAIL",
        "WATCH": "WARN",
        "TEMPLATE": "WARN",
    }
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")


@dataclass
class Exclusion:
    name: str
    forbidden_form: str
    why_forbidden: str
    violated_result: str
    failure_mode: str
    status: str
    surviving_requirement: str


def build_exclusions() -> List[Exclusion]:
    return [
        Exclusion(
            name="X1: Decorative Bianchi restatement",
            forbidden_form="Div E_parent = 0 because GR has nabla_mu G^mu_nu = 0",
            why_forbidden="It merely renames the target identity without deriving it from vacuum-curvature exchange.",
            violated_result="Group 11: parent closure target is MISSING / TEMPLATE ONLY.",
            failure_mode="Decorative parent identity; sector ledger mistaken for closure.",
            status="EXCLUDED",
            surviving_requirement="Define E_parent and show its reduced projections force the known sectors.",
        ),
        Exclusion(
            name="X2: Ordinary scalar A wave",
            forbidden_form="Box A = scalar source as an ordinary long-range gravitational radiation equation",
            why_forbidden="A is currently a scalar constraint / mass-flux response, not an ordinary radiative scalar.",
            violated_result="Constraint/evolution split: A is constraint; A_rad ordinary massless source = 0.",
            failure_mode="Hidden scalar radiation / breathing mode.",
            status="FORBIDDEN",
            surviving_requirement="Parent identity must propagate the A constraint through source continuity, not Box A radiation.",
        ),
        Exclusion(
            name="X3: Ordinary Box kappa trace wave",
            forbidden_form="Box kappa = alpha * trace_or_pressure",
            why_forbidden="Kappa is non-inertial trace / volume relaxation with no independent momentum channel.",
            violated_result="Group 10/11: kappa relaxation is first-order; breathing radiation rejected.",
            failure_mode="Hidden breathing wave; kappa repair knob.",
            status="FORBIDDEN",
            surviving_requirement="Trace/pressure may shift kappa_min, followed by first-order relaxation only.",
        ),
        Exclusion(
            name="X4: Rho double-sourced into kappa",
            forbidden_form="rho sources both A and an independent long-range kappa scalar",
            why_forbidden="rho already sources A; independent kappa response would double-count scalar mass gravity.",
            violated_result="No-double-counting: S_kappa[rho] = 0 as independent long-range scalar source.",
            failure_mode="Scalar double-counting; exterior kappa 1/r tail.",
            status="FORBIDDEN",
            surviving_requirement="Parent identity must route rho to A and prevent rho-sourced kappa charge.",
        ),
        Exclusion(
            name="X5: Nonzero exterior kappa charge",
            forbidden_form="Integral S_kappa d^3x != 0 for ordinary closed matter",
            why_forbidden="A nonzero massless kappa charge would create exterior kappa ~ 1/r.",
            violated_result="Exterior kappa safety: Q_kappa = 0, kappa -> 0, F_kappa(R+) = 0.",
            failure_mode="Second scalar exterior field; scalar double-counting.",
            status="FORBIDDEN",
            surviving_requirement="Parent identity must enforce kappa charge neutrality/projection or boundary cancellation.",
        ),
        Exclusion(
            name="X6: Trace contamination of TT radiation",
            forbidden_form="trace or pressure source directly feeds h_ij^TT",
            why_forbidden="TT radiation must be trace-free; trace/pressure belongs to kappa_min or scalar constraints.",
            violated_result="Source ledger: source(h_TT)=P_TT S_ij, trace excluded.",
            failure_mode="Tensor/scalar double-counting; imported TT source identity.",
            status="FORBIDDEN",
            surviving_requirement="Parent identity must separate P_TT stress from trace stress.",
        ),
        Exclusion(
            name="X7: Longitudinal current sources W_i",
            forbidden_form="P_L j sources transverse vector W_i / frame dragging",
            why_forbidden="W_i is a transverse vector response; longitudinal current belongs to scalar continuity.",
            violated_result="Source ledger: source(W_i)=P_T j; P_L j -> continuity.",
            failure_mode="Scalar/vector source mixing.",
            status="FORBIDDEN",
            surviving_requirement="Parent identity must preserve current decomposition j = P_T j + P_L j.",
        ),
        Exclusion(
            name="X8: Free vector radiation imported by analogy",
            forbidden_form="W_i becomes a free propagating vector wave without derivation",
            why_forbidden="W_i is currently source-tied vector response, not an established radiative sector.",
            violated_result="Constraint/evolution split: W_i free vector radiation is not derived.",
            failure_mode="Electromagnetic analogy imported as gravity sector.",
            status="EXCLUDED",
            surviving_requirement="Any retarded W_i dynamics must be derived and must not add forbidden radiation modes.",
        ),
        Exclusion(
            name="X9: Boundary relaxation changes exterior mass",
            forbidden_form="kappa / joint-minimum boundary smoothing changes M_ext or the exterior 1/r coefficient",
            why_forbidden="Exterior mass flux is the A-sector charge and cannot be tuned by boundary smoothing.",
            violated_result="No-double-counting: delta M_ext under kappa boundary smoothing = 0.",
            failure_mode="Boundary smoothing tunes measured mass.",
            status="FORBIDDEN",
            surviving_requirement="Parent identity must preserve exterior A flux under kappa relaxation.",
        ),
        Exclusion(
            name="X10: Sigma_creation in ordinary closure",
            forbidden_form="Sigma_creation != 0 in ordinary closed gravity",
            why_forbidden="Creation/exchange regimes are special active regimes, not default ordinary gravity.",
            violated_result="Ordinary closed regime: Sigma_creation = 0.",
            failure_mode="Active-regime leakage; nonconservative field equations.",
            status="FORBIDDEN",
            surviving_requirement="Parent identity must separate ordinary closed regime from active creation regimes.",
        ),
        Exclusion(
            name="X11: Relaxation as energy loss",
            forbidden_form="Gamma_relax removes energy without a destination variable",
            why_forbidden="Relaxation must represent exchange/restoration into vacuum configuration, not disappearance.",
            violated_result="Kappa relaxation: energy imbalance must be accounted as vacuum configuration restoration.",
            failure_mode="Cosmetic damping; energy nonconservation.",
            status="EXCLUDED",
            surviving_requirement="Parent identity must include or imply vacuum configuration energy accounting.",
        ),
        Exclusion(
            name="X12: GR coefficient insertion as derivation",
            forbidden_form="Insert Lense-Thirring normalization, C_T, or tensor flux coefficient because GR has them",
            why_forbidden="Matched coefficients are not ontology-derived coefficients.",
            violated_result="GR audit: vector normalization and tensor coupling/flux remain MATCHED / UNKNOWN.",
            failure_mode="Silent GR import; matched coefficients claimed derived.",
            status="EXCLUDED",
            surviving_requirement="Parent identity may target GR coefficients, but must not claim them without derivation.",
        ),
        Exclusion(
            name="X13: Metric recombination copies GR by form",
            forbidden_form="g_tt, g_0i, g_ij assigned full GR weak-field form before parent recombination is derived",
            why_forbidden="Metric recombination is currently a reduced bookkeeping ansatz, not a covariant derivation.",
            violated_result="Metric recombination status: UNFINISHED.",
            failure_mode="Silent GR metric import.",
            status="EXCLUDED",
            surviving_requirement="Parent identity must produce a recombination map preserving source splits and constraints.",
        ),
        Exclusion(
            name="X14: Near-boundary deviation promoted before closure",
            forbidden_form="claim measured/predicted near-boundary GR deviation from joint-minimum diagnostic alone",
            why_forbidden="Deviation diagnostics exist, but weights, sigma, observable map, and closure are missing.",
            violated_result="Near-boundary result: PLAUSIBLE / DIAGNOSTIC ONLY.",
            failure_mode="Near-boundary deviation overclaim.",
            status="EXCLUDED",
            surviving_requirement="Keep diagnostic before prediction until recombination and magnitude are derived.",
        ),
    ]


def print_exclusion(x: Exclusion) -> None:
    print()
    print("-" * 120)
    print(x.name)
    print("-" * 120)
    print(f"Forbidden form: {x.forbidden_form}")
    print(f"Why forbidden: {x.why_forbidden}")
    print(f"Violated result: {x.violated_result}")
    print(f"Failure mode: {x.failure_mode}")
    status_line(x.name, x.status)
    print(f"Surviving requirement: {x.surviving_requirement}")


def case_0_problem_statement():
    header("Case 0: Parent identity exclusion problem")

    print("Question:")
    print()
    print("  What can the parent identity not be?")
    print()
    print("Goal:")
    print()
    print("  rule out false parent identities before attempting a positive parent identity")
    print()
    print("Discipline:")
    print()
    print("  do not crown the first shiny equation")
    print("  do not restate GR as if it were derived")
    print("  do not let scalar radiation or double-counting reappear")
    print("  do not use kappa as a repair knob")

    status_line("parent identity exclusion problem posed", "CONSTRAINED")


def case_1_exclusion_inventory(entries: List[Exclusion]):
    header("Case 1: Exclusion inventory")
    for entry in entries:
        print_exclusion(entry)


def case_2_compact_table(entries: List[Exclusion]):
    header("Case 2: Compact exclusion ledger")

    print("| Exclusion | Forbidden form | Status | Surviving requirement |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.forbidden_form.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.surviving_requirement.replace("|", "/")
            + " |"
        )

    status_line("compact exclusion ledger produced", "CONSTRAINED")


def case_3_status_counts(entries: List[Exclusion]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  The candidate parent space is already strongly constrained.")
    print("  Most false parents are forbidden because they reintroduce scalar radiation,")
    print("  double-count sources, tune mass, or import GR by hand.")

    status_line("exclusion count produced", "CONSTRAINED")


def case_4_surviving_parent_requirements(entries: List[Exclusion]):
    header("Case 4: Surviving parent requirements")

    print("Any surviving parent identity must:")
    print()
    print("1. Define E_parent and B_source rather than restating Bianchi compatibility.")
    print("2. Keep A as a scalar constraint, not ordinary scalar radiation.")
    print("3. Keep kappa first-order/non-inertial, not Box kappa.")
    print("4. Route rho to A without independent long-range kappa charge.")
    print("5. Preserve exterior A mass flux under boundary/kappa relaxation.")
    print("6. Split j into transverse vector source and longitudinal continuity.")
    print("7. Split TT stress from trace stress.")
    print("8. Exclude Sigma_creation in ordinary closed gravity.")
    print("9. Account for Gamma_relax as vacuum configuration exchange.")
    print("10. Derive or honestly label vector/tensor coefficients.")
    print("11. Produce recombination without scalar double-counting.")
    print("12. Keep near-boundary deviation diagnostic-only until magnitude is derived.")

    status_line("surviving parent requirements stated", "CONSTRAINED")


def case_5_hardest_exclusions():
    header("Case 5: Hardest exclusions")

    print("Hardest exclusions to make constructive:")
    print()
    print("1. Decorative Bianchi restatement.")
    print("   Need: actual definitions and reduced implications.")
    print()
    print("2. Scalar A not radiation.")
    print("   Need: constraint propagation from continuity.")
    print()
    print("3. Kappa not Box kappa.")
    print("   Need: trace-minimum relaxation identity.")
    print()
    print("4. Boundary relaxation preserves M_ext.")
    print("   Need: boundary mass theorem.")
    print()
    print("5. Metric recombination not GR import.")
    print("   Need: recombination map from sector identity.")

    status_line("hardest exclusions identified", "WATCH")


def case_6_possible_parent_space():
    header("Case 6: What remains possible")

    print("Still possible parent identity classes:")
    print()
    print("  A divergence/balance identity with explicit sector projectors.")
    print("  A constrained scalar sector plus TT radiative sector.")
    print("  A transverse current/vector response sector that is source-tied.")
    print("  A trace/minimum relaxation channel for kappa.")
    print("  A boundary/interface identity preserving exterior mass.")
    print("  A recombination map generated after source/projector splitting.")
    print()
    print("But none of these are derived yet.")

    status_line("surviving parent space described", "UNRESOLVED")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_parent_identity_exclusion_constraints.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_parent_identity_reduced_implications.py")
    print("   State what the parent identity must imply in each reduced sector.")
    print()
    print("3. candidate_projector_structure_for_parent_identity.py")
    print("   Work out scalar/vector/TT/trace projectors.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_parent_identity_reduced_implications.py")
    print()
    print("Reason:")
    print("  After ruling out false parents, define the reduced-sector tests for any surviving parent.")

    status_line("next test selected", "CONSTRAINED")


def final_interpretation():
    header("Final interpretation")

    print("The parent identity cannot be:")
    print()
    print("  a decorative Bianchi restatement")
    print("  an ordinary scalar A wave")
    print("  Box kappa")
    print("  rho double-sourced into kappa")
    print("  nonzero exterior kappa charge")
    print("  trace contamination of TT")
    print("  longitudinal current sourcing W_i")
    print("  boundary smoothing changing exterior mass")
    print("  Sigma_creation in ordinary closure")
    print("  GR coefficients inserted as derivation")
    print("  metric recombination copied from GR")
    print()
    print("Possible next artifact:")
    print("  candidate_parent_identity_exclusion_constraints.md")
    print()
    print("Possible next script:")
    print("  candidate_parent_identity_reduced_implications.py")


def main():
    header("Candidate Parent Identity Exclusion Constraints")
    case_0_problem_statement()
    entries = build_exclusions()
    case_1_exclusion_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_surviving_parent_requirements(entries)
    case_5_hardest_exclusions()
    case_6_possible_parent_space()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
