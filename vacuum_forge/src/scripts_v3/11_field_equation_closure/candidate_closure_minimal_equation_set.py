# Candidate closure minimal equation set
#
# Purpose
# -------
# The failure-mode audit identified how closure can fail.
#
# The next step is constructive but cautious:
#
#   assemble the current minimal equation set,
#   with every piece labeled.
#
# This script presents the smallest current field-equation set that reflects
# the project honestly:
#
#   A scalar constraint
#   B/kappa reduced relation
#   W_i transverse vector response
#   h_ij^TT tensor radiation
#   kappa non-inertial trace relaxation
#   scalar-radiation rejection
#   source no-double-counting constraints
#   closure status
#
# This is not a final theory.
# It is a current-status equation set.

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
        "REJECTED": "WARN",
        "UNFINISHED": "FAIL",
        "RISK": "WARN",
    }
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")


@dataclass
class EquationEntry:
    name: str
    equation: str
    role: str
    source: str
    status: str
    missing: str
    caveat: str


def build_equations() -> List[EquationEntry]:
    return [
        EquationEntry(
            name="E1: A-sector scalar constraint",
            equation="Delta_areal A = 8*pi*G*rho/c^2",
            role="scalar monopole / mass flux constraint",
            source="rho, M_enc",
            status="DERIVED_REDUCED",
            missing="full nonlinear nonspherical parent equation",
            caveat="valid strongest in static spherical/reduced scalar sector",
        ),
        EquationEntry(
            name="E2: exterior A solution",
            equation="A(r) = 1 - 2*G*M/(c^2*r)",
            role="static spherical exterior scalar factor",
            source="M = integral rho dV",
            status="DERIVED_REDUCED",
            missing="general exterior/nonspherical nonlinear form",
            caveat="main real reconstruction result",
        ),
        EquationEntry(
            name="E3: B/kappa areal relation",
            equation="A*B = exp(2*kappa); exterior kappa=0 -> B=1/A",
            role="radial reciprocal companion / kappa diagnostic",
            source="exterior vacuum target kappa=0",
            status="DERIVED_REDUCED",
            missing="covariant gauge/physical split",
            caveat="reduced areal-gauge relation, not full parent metric",
        ),
        EquationEntry(
            name="E4: weak scalar multipole limit",
            equation="A ~= 1 + 2*Phi/c^2; nabla^2 Phi = 4*pi*G*rho",
            role="weak scalar/Newtonian limit",
            source="rho",
            status="DERIVED_REDUCED",
            missing="full nonlinear nonspherical closure",
            caveat="supports weak multipoles and reduced gamma=1, not full PPN audit",
        ),
        EquationEntry(
            name="E5: vector current response",
            equation="curl curl W = -(alpha_W/(2*K_c))*j_T; div W=0",
            role="transverse vector / frame-dragging shape",
            source="j_T = P_T(rho*v)",
            status="STRUCTURAL",
            missing="alpha_W/K_c, beta_W, normalization",
            caveat="far-field shape/J dependence supported; coefficient not derived",
        ),
        EquationEntry(
            name="E6: tensor radiation equation",
            equation="Box h_ij^TT = -C_T*S_ij^TT",
            role="ordinary long-range gravitational radiation",
            source="TT stress / quadrupole source",
            status="STRUCTURAL",
            missing="C_T, TT source identity, tensor action stiffness",
            caveat="TT role structural; coupling coefficient not derived",
        ),
        EquationEntry(
            name="E7: tensor radiation energy flux",
            equation="F_T ~ K_T <dot(h_ij^TT) dot(h_ij^TT)>",
            role="tensor radiation energy accounting",
            source="TT wave strain",
            status="MATCHED",
            missing="K_T from vacuum action/stiffness",
            caveat="absolute GR flux coefficient not derived",
        ),
        EquationEntry(
            name="E8: kappa non-inertial relaxation",
            equation="dot(kappa) = -mu_kappa*K_kappa*(kappa-kappa_min)",
            role="trace / vacuum-volume relaxation",
            source="kappa_min = chi_kappa*S_trace_effective",
            status="STRUCTURAL",
            missing="K_kappa, mu_kappa, chi_kappa, S_trace_effective, covariant origin",
            caveat="not a wave equation; no independent momentum channel",
        ),
        EquationEntry(
            name="E9: exterior kappa safety",
            equation="kappa -> 0; kappa_min -> 0; F_kappa(R+) = 0",
            role="no exterior scalar/kappa charge",
            source="vacuum minimum / boundary projection",
            status="CONSTRAINED",
            missing="boundary/interface theorem",
            caveat="required to avoid scalar tail and mass tuning",
        ),
        EquationEntry(
            name="E10: scalar radiation rejection",
            equation="source(A_rad ordinary massless) = 0; Box kappa ordinary scalar rejected",
            role="TT-only ordinary radiation safety",
            source="scalar-radiation hazard",
            status="REJECTED",
            missing="parent mechanism proving exclusion",
            caveat="constraint, not yet derivation",
        ),
        EquationEntry(
            name="E11: ordinary closed regime",
            equation="Sigma_creation = 0",
            role="ordinary conservative closure",
            source="active-regime exclusion",
            status="CONSTRAINED",
            missing="active-regime trigger/exclusion law",
            caveat="creation/exchange regimes not part of ordinary gravity closure by default",
        ),
        EquationEntry(
            name="E12: parent closure target",
            equation="Div E_parent[A,W,h_TT,kappa] = B_closed[T] + B_relax[Gamma_relax]",
            role="candidate parent identity target",
            source="source balance / vacuum exchange",
            status="MISSING",
            missing="E_parent, B_closed, B_relax definitions and proof",
            caveat="template only; not closure",
        ),
    ]


def print_equation(e: EquationEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Equation: {e.equation}")
    print(f"Role: {e.role}")
    print(f"Source: {e.source}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")
    print(f"Caveat: {e.caveat}")


def case_0_problem_statement():
    header("Case 0: Minimal closure equation set problem")

    print("Question:")
    print()
    print("  What is the smallest honest current field-equation set?")
    print()
    print("Goal:")
    print()
    print("  assemble the current equations with labels and caveats")
    print()
    print("Discipline:")
    print()
    print("  do not hide matched coefficients")
    print("  do not claim closure")
    print("  keep kappa non-radiative")
    print("  keep parent identity marked missing")

    status_line("minimal equation set problem posed", "CONSTRAINED")


def case_1_equation_inventory(entries: List[EquationEntry]):
    header("Case 1: Minimal equation inventory")
    for entry in entries:
        print_equation(entry)


def case_2_compact_table(entries: List[EquationEntry]):
    header("Case 2: Compact minimal equation table")

    print("| Equation | Role | Status | Missing |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.role.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.missing.replace("|", "/")
            + " |"
        )

    status_line("compact minimal equation table produced", "STRUCTURAL")


def case_3_status_counts(entries: List[EquationEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  The minimal set has strong reduced scalar equations, structural vector/tensor/kappa rules,")
    print("  constrained scalar-radiation safety, one matched tensor energy coefficient, and missing parent closure.")

    status_line("minimal equation status count produced", "STRUCTURAL")


def case_4_minimal_reduced_system():
    header("Case 4: Minimal reduced system")

    print("Minimal current reduced system:")
    print()
    print("  Delta_areal A = 8*pi*G*rho/c^2")
    print("  A_ext = 1 - 2*G*M/(c^2*r)")
    print("  A*B = exp(2*kappa), exterior kappa=0 -> B=1/A")
    print("  curl curl W = -(alpha_W/(2*K_c))*j_T")
    print("  Box h_TT = -C_T*S_TT")
    print("  dot(kappa) = -mu_kappa*K_kappa*(kappa-kappa_min)")
    print("  kappa_min = chi_kappa*S_trace_effective")
    print("  source(A_rad ordinary massless) = 0")
    print("  Sigma_creation = 0 in ordinary closed regime")
    print()
    print("Parent closure target:")
    print()
    print("  Div E_parent = B_closed + B_relax")

    status_line("minimal reduced system stated", "CONSTRAINED")


def case_5_gr_recovery_status():
    header("Case 5: GR recovery status")

    print("Recovered strongly/reduced:")
    print("  static spherical exterior A")
    print("  B=1/A once exterior kappa=0")
    print("  weak scalar/Newtonian limit")
    print()
    print("Supported structurally:")
    print("  vector frame-dragging shape")
    print("  TT tensor radiation sector")
    print("  kappa non-radiative trace relaxation")
    print()
    print("Matched or missing:")
    print("  vector normalization")
    print("  tensor coupling")
    print("  tensor energy flux coefficient")
    print("  parent conservation identity")
    print("  covariant recombination")

    status_line("GR recovery status restated", "CONSTRAINED")


def case_6_failure_controls():
    header("Case 6: Failure controls")

    print("This minimal set fails if:")
    print()
    print("1. Parent closure target is advertised as derived.")
    print("2. Tensor/vector coefficients are advertised as derived.")
    print("3. Kappa becomes a second scalar gravity field.")
    print("4. Boundary smoothing changes exterior M.")
    print("5. A_rad or Box kappa scalar radiation appears.")
    print("6. Sigma_creation enters ordinary closed regime.")
    print("7. Recombination silently copies GR.")

    status_line("minimal set failure controls stated", "RISK")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_closure_minimal_equation_set.md")
    print("   Artifact for this script.")
    print()
    print("2. field_equation_closure_summary.md")
    print("   Summarize group 11.")
    print()
    print("3. candidate_parent_identity_reduced_implications.py")
    print("   Test reduced implications of the parent identity template.")
    print()
    print("Recommended next:")
    print()
    print("  field_equation_closure_summary.md")
    print()
    print("Reason:")
    print("  Group 11 has reached a natural summary point after inventory, recombination, sources, constraints,")
    print("  evolution split, GR audit, parent scaffold, failure modes, and minimal equation set.")

    status_line("next test selected", "CONSTRAINED")


def final_interpretation():
    header("Final interpretation")

    print("The current minimal equation set is coherent enough to state.")
    print()
    print("It is not closed.")
    print()
    print("Strongest result:")
    print("  reduced Schwarzschild exterior from A-sector")
    print()
    print("Main missing result:")
    print("  parent conservation/recombination identity")
    print()
    print("Possible next artifact:")
    print("  candidate_closure_minimal_equation_set.md")
    print()
    print("Recommended next:")
    print("  field_equation_closure_summary.md")


def main():
    header("Candidate Closure Minimal Equation Set")
    case_0_problem_statement()
    entries = build_equations()
    case_1_equation_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_minimal_reduced_system()
    case_5_gr_recovery_status()
    case_6_failure_controls()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
