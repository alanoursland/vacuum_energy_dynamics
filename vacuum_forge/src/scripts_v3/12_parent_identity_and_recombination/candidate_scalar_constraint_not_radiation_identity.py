# Candidate scalar constraint not radiation identity
#
# Purpose
# -------
# The projector audit found that P_scalar is the hardest immediate gate.
#
# The parent identity must explain:
#
#   A is a scalar constraint / mass-flux response,
#   not an ordinary propagating scalar radiation field.
#
# This script focuses on the scalar sector:
#
#   Why does rho feed A?
#   Why does rho not feed A_rad?
#   Why does rho not feed long-range kappa?
#   How can A update with source continuity without becoming Box A?
#
# This is not a derivation.
# It is an identity-requirement and failure audit.

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
        "REJECTED": "WARN",
        "MISSING": "FAIL",
        "UNRESOLVED": "FAIL",
        "RISK": "WARN",
        "REQUIRED": "WARN",
    }
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")


@dataclass
class ScalarRequirement:
    name: str
    requirement: str
    target_form: str
    forbidden_form: str
    status: str
    risk: str
    missing: str


def build_requirements() -> List[ScalarRequirement]:
    return [
        ScalarRequirement(
            name="S1: scalar source routes to A",
            requirement="rho / scalar charge feeds the A-sector constraint.",
            target_form="P_scalar[T] -> rho_eff -> Delta_areal A = 8*pi*G*rho/c^2",
            forbidden_form="rho feeds A_rad or independent kappa charge.",
            status="DERIVED_REDUCED",
            risk="Scalar source leaks into forbidden scalar sectors.",
            missing="Parent definition of rho_eff and P_scalar.",
        ),
        ScalarRequirement(
            name="S2: A is constraint, not Box A",
            requirement="A must remain elliptic/constraint-like in ordinary gravity.",
            target_form="C_A[A,rho]=0 with constraint propagation from continuity",
            forbidden_form="Box A = alpha*rho",
            status="CONSTRAINED",
            risk="Ordinary scalar gravitational radiation appears.",
            missing="Continuity-compatible constraint propagation identity.",
        ),
        ScalarRequirement(
            name="S3: A_rad ordinary massless source vanishes",
            requirement="The ordinary long-range scalar radiative channel is absent.",
            target_form="source(A_rad ordinary massless)=0",
            forbidden_form="Box A_rad = source",
            status="REJECTED",
            risk="Breathing radiation channel.",
            missing="Parent mechanism proving scalar radiation exclusion.",
        ),
        ScalarRequirement(
            name="S4: rho does not source long-range kappa",
            requirement="rho must not create independent exterior kappa charge.",
            target_form="S_kappa[rho]=0 and Q_kappa=0",
            forbidden_form="kappa_ext ~ 1/r from rho",
            status="CONSTRAINED",
            risk="Scalar double-counting and second exterior scalar field.",
            missing="Parent projection or boundary cancellation identity.",
        ),
        ScalarRequirement(
            name="S5: trace does not become scalar radiation",
            requirement="Trace/pressure may shift kappa_min but must not source Box kappa or A_rad.",
            target_form="trace -> kappa_min; dot kappa = -mu*K*(kappa-kappa_min)",
            forbidden_form="Box kappa = alpha*trace",
            status="STRUCTURAL",
            risk="Hidden breathing mode.",
            missing="P_trace/P_relax parent identity.",
        ),
        ScalarRequirement(
            name="S6: scalar continuity drives constraint update",
            requirement="Time-dependent rho updates A through continuity, not through scalar radiation.",
            target_form="partial_t C_A[A,rho] implied by partial_t rho + div j_L = 0",
            forbidden_form="add scalar wave dynamics to make A causal by hand",
            status="MISSING",
            risk="Constraint becomes inconsistent for moving sources.",
            missing="Reduced or parent constraint-propagation equation.",
        ),
        ScalarRequirement(
            name="S7: exterior scalar charge equals A-sector mass",
            requirement="The only ordinary exterior scalar charge is M_ext in A.",
            target_form="A_ext = 1 - 2*G*M_ext/(c^2*r)",
            forbidden_form="additional scalar 1/r tails from A_rad or kappa",
            status="DERIVED_REDUCED",
            risk="Multiple scalar charges in exterior vacuum.",
            missing="Parent mass-flux charge conservation.",
        ),
        ScalarRequirement(
            name="S8: scalar projector survives weak multipoles",
            requirement="P_scalar must support weak nonspherical Newtonian multipoles without scalar radiation.",
            target_form="A ~= 1 + 2*Phi/c^2; nabla^2 Phi = 4*pi*G*rho",
            forbidden_form="weak scalar waves sourced by ordinary matter",
            status="DERIVED_REDUCED",
            risk="Static weak multipoles confused with scalar radiation.",
            missing="Full nonspherical parent constraint.",
        ),
        ScalarRequirement(
            name="S9: scalar sector recombination counted once",
            requirement="A's scalar response must not be duplicated in kappa or spatial metric trace.",
            target_form="P_recombination counts scalar response exactly once",
            forbidden_form="A and kappa both represent the same scalar mass response",
            status="UNRESOLVED",
            risk="Silent scalar double-counting in metric map.",
            missing="Recombination projector.",
        ),
    ]


def print_requirement(r: ScalarRequirement) -> None:
    print()
    print("-" * 120)
    print(r.name)
    print("-" * 120)
    print(f"Requirement: {r.requirement}")
    print(f"Target form: {r.target_form}")
    print(f"Forbidden form: {r.forbidden_form}")
    status_line(r.name, r.status)
    print(f"Risk: {r.risk}")
    print(f"Missing: {r.missing}")


def case_0_problem_statement():
    header("Case 0: Scalar constraint-not-radiation problem")

    print("Question:")
    print()
    print("  Why does scalar source produce A as a constraint, rather than scalar radiation?")
    print()
    print("Goal:")
    print()
    print("  isolate the scalar-sector identity requirements")
    print()
    print("Discipline:")
    print()
    print("  do not allow Box A")
    print("  do not allow A_rad")
    print("  do not allow rho-sourced kappa")
    print("  do not confuse static multipoles with scalar radiation")

    status_line("scalar constraint-not-radiation problem posed", "REQUIRED")


def case_1_requirement_inventory(entries: List[ScalarRequirement]):
    header("Case 1: Scalar requirement inventory")
    for entry in entries:
        print_requirement(entry)


def case_2_compact_table(entries: List[ScalarRequirement]):
    header("Case 2: Compact scalar constraint ledger")

    print("| Requirement | Target form | Forbidden form | Status | Missing |")
    print("|---|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.target_form.replace("|", "/")
            + " | "
            + e.forbidden_form.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.missing.replace("|", "/")
            + " |"
        )

    status_line("compact scalar ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[ScalarRequirement]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  The static/reduced scalar sector is strong.")
    print("  The missing piece is scalar constraint propagation for time-dependent sources.")
    print("  Recombination remains unresolved.")

    status_line("scalar status count produced", "STRUCTURAL")


def case_4_candidate_identity_shape():
    header("Case 4: Candidate scalar identity shape")

    print("A useful scalar parent implication would have the shape:")
    print()
    print("  P_scalar Div(E_parent) -> constraint propagation")
    print()
    print("with reduced content:")
    print()
    print("  C_A[A,rho] = 0")
    print("  partial_t C_A[A,rho] follows from partial_t rho + div j_L = 0")
    print("  source(A_rad ordinary massless) = 0")
    print("  S_kappa[rho] = 0")
    print()
    print("This would make scalar non-radiation structural rather than imposed.")
    print()
    print("This is currently a target, not a derivation.")

    status_line("candidate scalar identity shape stated", "MISSING")


def case_5_failure_controls():
    header("Case 5: Failure controls")

    print("The scalar sector fails if:")
    print()
    print("1. Box A appears as an ordinary matter-sourced wave equation.")
    print("2. A_rad becomes active ordinary radiation.")
    print("3. rho sources long-range kappa.")
    print("4. trace/pressure creates Box kappa.")
    print("5. scalar constraint cannot update with moving sources.")
    print("6. weak static multipoles are used to justify scalar waves.")
    print("7. recombination counts scalar response twice.")

    status_line("scalar failure controls stated", "RISK")


def case_6_next_tests():
    header("Case 6: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_scalar_constraint_not_radiation_identity.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_kappa_covariant_relaxation_requirement.py")
    print("   Focus on kappa relaxation and frame/covariance issue.")
    print()
    print("3. candidate_scalar_constraint_propagation_toy_model.py")
    print("   Try a reduced continuity-compatible scalar constraint update.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_kappa_covariant_relaxation_requirement.py")
    print()
    print("Reason:")
    print("  Scalar A is protected by constraints; now kappa's first-order relaxation must be frame/covariance audited.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("The scalar sector can remain safe if:")
    print()
    print("  rho routes only to A")
    print("  A remains a constraint")
    print("  A_rad has no ordinary massless source")
    print("  rho does not source long-range kappa")
    print("  trace shifts kappa_min without Box kappa")
    print("  moving sources update A through continuity")
    print("  recombination counts scalar response once")
    print()
    print("The missing scalar piece is:")
    print("  continuity-compatible scalar constraint propagation.")
    print()
    print("Possible next artifact:")
    print("  candidate_scalar_constraint_not_radiation_identity.md")
    print()
    print("Possible next script:")
    print("  candidate_kappa_covariant_relaxation_requirement.py")


def main():
    header("Candidate Scalar Constraint Not Radiation Identity")
    case_0_problem_statement()
    entries = build_requirements()
    case_1_requirement_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_candidate_identity_shape()
    case_5_failure_controls()
    case_6_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
