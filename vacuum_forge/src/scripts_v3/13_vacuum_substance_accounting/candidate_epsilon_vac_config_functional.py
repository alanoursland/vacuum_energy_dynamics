# Candidate epsilon_vac_config functional
#
# Purpose
# -------
# The vacuum accounting parent balance audit produced the first concrete skeleton:
#
#   u^mu nabla_mu epsilon_vac_config + nabla_mu J_v^mu
#     = Sigma_exchange - Gamma_relax
#
# with ordinary constraints:
#
#   Sigma_creation = 0
#   boundary J_v flux = 0
#   Q_volume = 0
#   delta M_ext = 0
#   F_scalar_far = 0
#
# The next missing object is:
#
#   epsilon_vac_config = F(zeta, zeta_min, gradients, kappa, ...)
#
# This script audits candidate functional forms for epsilon_vac_config.
#
# It is not a derivation.

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
class FunctionalEntry:
    name: str
    term: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str


def build_entries() -> List[FunctionalEntry]:
    return [
        FunctionalEntry(
            name="F1: volume displacement energy",
            term="1/2 K_zeta (zeta - zeta_min)^2",
            role="local cost of volume-form displacement from equilibrium",
            allowed_if="zeta is the geometric volume variable and does not carry A-sector mass",
            forbidden_if="used as independent exterior scalar charge",
            status="CANDIDATE",
            missing="K_zeta, zeta_min, frame/measure",
        ),
        FunctionalEntry(
            name="F2: gradient/interface stiffness",
            term="1/2 L_zeta gamma^ij partial_i zeta partial_j zeta",
            role="penalizes sharp volume-form interfaces and shell artifacts",
            allowed_if="compact/support boundary behavior remains zero-flux",
            forbidden_if="creates propagating scalar wave or exterior tail",
            status="CANDIDATE",
            missing="L_zeta and whether gradient term is spatial/constraint-only",
        ),
        FunctionalEntry(
            name="F3: kappa mismatch energy",
            term="1/2 K_kappa (kappa - kappa_min)^2",
            role="existing trace/volume relaxation energy candidate",
            allowed_if="kappa is tied to zeta mismatch and first-order relaxation",
            forbidden_if="adds independent kappa scalar momentum/radiation",
            status="STRUCTURAL",
            missing="precise kappa-zeta map",
        ),
        FunctionalEntry(
            name="F4: kappa-zeta locking term",
            term="1/2 K_lock (kappa - (zeta - zeta_min))^2",
            role="prevents kappa and zeta from becoming independent scalar charges",
            allowed_if="used as constraint/diagnostic relation",
            forbidden_if="introduces extra scalar degree of freedom",
            status="CANDIDATE",
            missing="whether kappa equals, approximates, or projects zeta mismatch",
        ),
        FunctionalEntry(
            name="F5: compact-support boundary term",
            term="B_boundary[zeta] enforcing zeta(R)=0 and flux zero",
            role="protects exterior neutrality and no shell artifacts",
            allowed_if="derived from interface law or projector",
            forbidden_if="boundary condition imposed by hand for each case",
            status="CANDIDATE",
            missing="P_boundary origin and interface law",
        ),
        FunctionalEntry(
            name="F6: compensated-source constraint",
            term="lambda_Q (integral S_volume d^3x)",
            role="enforces Q_volume=0 when compensation is required",
            allowed_if="constraint origin is parent-derived",
            forbidden_if="used as arbitrary projection repair",
            status="RISK",
            missing="S_volume definition and parent projector",
        ),
        FunctionalEntry(
            name="F7: forbidden A-mass term",
            term="M_ext or A_flux included in epsilon_vac_config",
            role="none",
            allowed_if="never",
            forbidden_if="epsilon_vac_config changes exterior mass",
            status="FORBIDDEN",
            missing="not pursued",
        ),
        FunctionalEntry(
            name="F8: forbidden coefficient tuning term",
            term="terms adjusted to fit alpha_W/K_c, beta_W, C_T, K_T",
            role="none",
            allowed_if="never",
            forbidden_if="functional becomes coefficient repair knob",
            status="FORBIDDEN",
            missing="not pursued",
        ),
        FunctionalEntry(
            name="F9: optional nonlinear volume strain",
            term="U(exp(zeta)) or U(sqrt(gamma)/sqrt(gamma_ref))",
            role="nonlinear extension beyond quadratic displacement",
            allowed_if="reduces to quadratic form at small strain and preserves neutrality",
            forbidden_if="nonlinear term creates exterior volume charge",
            status="UNRESOLVED",
            missing="nonlinear determinant/volume theorem",
        ),
        FunctionalEntry(
            name="F10: minimal candidate functional",
            term="epsilon_vac_config = 1/2 K_zeta (zeta-zeta_min)^2 + 1/2 L_zeta |grad zeta|^2 + 1/2 K_lock (kappa-(zeta-zeta_min))^2",
            role="first combined candidate functional",
            allowed_if="treated as scaffold with unknown coefficients and no scalar radiation",
            forbidden_if="advertised as derived or covariant",
            status="CANDIDATE",
            missing="coefficients, measure, frame, boundary law, parent derivation",
        ),
        FunctionalEntry(
            name="F11: measure factor",
            term="epsilon_vac_config sqrt(gamma) d^3x",
            role="integrates local density over physical volume",
            allowed_if="slice/frame is specified",
            forbidden_if="treated as covariant action without 4D formulation",
            status="REQUIRED",
            missing="measure convention and covariant extension",
        ),
        FunctionalEntry(
            name="F12: no kinetic scalar term",
            term="no 1/2 (u^mu nabla_mu zeta)^2 unless derived",
            role="prevents second-order scalar wave",
            allowed_if="scalar/trace channel remains conversion/constraint/relaxation-mediated",
            forbidden_if="creates Box zeta ordinary radiation",
            status="CONSTRAINED",
            missing="parent reason for no scalar inertia",
        ),
    ]


def print_entry(e: FunctionalEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Term: {e.term}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")


def case_0_problem_statement():
    header("Case 0: epsilon_vac_config functional problem")

    print("Question:")
    print()
    print("  What functional form could epsilon_vac_config have?")
    print()
    print("Goal:")
    print()
    print("  test candidate local, gradient, kappa-locking, and boundary terms")
    print()
    print("Discipline:")
    print()
    print("  geometric functional, not reservoir")
    print("  no A-sector mass term")
    print("  no coefficient tuning")
    print("  no scalar kinetic wave term")
    print("  no exterior scalar charge")
    print("  no claim of derivation")

    status_line("epsilon_vac_config functional problem posed", "REQUIRED")


def case_1_inventory(entries: List[FunctionalEntry]):
    header("Case 1: Functional term inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[FunctionalEntry]):
    header("Case 2: Compact functional ledger")

    print("| Entry | Term | Status | Forbidden if | Missing |")
    print("|---|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.term.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.forbidden_if.replace("|", "/")
            + " | "
            + e.missing.replace("|", "/")
            + " |"
        )

    status_line("compact functional ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[FunctionalEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  A minimal functional can be written, but it is not derived.")
    print("  A-sector mass and coefficient tuning are explicitly forbidden.")
    print("  The scalar kinetic term remains excluded unless separately derived.")

    status_line("functional status count produced", "STRUCTURAL")


def case_4_minimal_functional():
    header("Case 4: Minimal candidate functional")

    print("Minimal candidate:")
    print()
    print("  epsilon_vac_config =")
    print("    1/2 K_zeta (zeta-zeta_min)^2")
    print("    + 1/2 L_zeta |grad zeta|^2")
    print("    + 1/2 K_lock (kappa-(zeta-zeta_min))^2")
    print()
    print("with:")
    print()
    print("  zeta = ln sqrt(gamma)")
    print()
    print("and no:")
    print()
    print("  A_flux term")
    print("  M_ext term")
    print("  coefficient tuning term")
    print("  scalar kinetic wave term")
    print()
    print("This is a scaffold functional, not a derived action.")

    status_line("minimal candidate functional stated", "CANDIDATE")


def case_5_exchange_with_relaxation():
    header("Case 5: Exchange with relaxation")

    print("Existing relaxation energy:")
    print()
    print("  e_kappa = 1/2 K_kappa (kappa-kappa_min)^2")
    print()
    print("Possible accounting relation:")
    print()
    print("  d e_kappa/dtau + d epsilon_vac_config/dtau = 0")
    print()
    print("But if epsilon_vac_config already contains the kappa mismatch term,")
    print("avoid double-counting e_kappa.")
    print()
    print("Two allowed options:")
    print()
    print("1. e_kappa is a sector piece outside epsilon_vac_config.")
    print("2. e_kappa is included inside epsilon_vac_config and not counted again.")
    print()
    print("This must be fixed by recombination/accounting.")

    status_line("relaxation exchange accounting stated", "RISK")


def case_6_failure_controls():
    header("Case 6: Failure controls")

    print("The epsilon_vac_config functional fails if:")
    print()
    print("1. It includes A_flux or M_ext.")
    print("2. It tunes vector/tensor coefficients.")
    print("3. It adds scalar kinetic energy and Box zeta by accident.")
    print("4. It creates exterior zeta/kappa charge.")
    print("5. It double-counts e_kappa.")
    print("6. It imposes compensation by hand without parent origin.")
    print("7. It is claimed covariant without frame/measure.")
    print("8. It becomes a repair reservoir.")

    status_line("functional failure controls stated", "RISK")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_epsilon_vac_config_functional.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_epsilon_kappa_double_counting_check.py")
    print("   Decide whether e_kappa is inside or outside epsilon_vac_config.")
    print()
    print("3. vacuum_substance_accounting_summary.md")
    print("   Summarize group 13 after the functional audit.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_epsilon_kappa_double_counting_check.py")
    print()
    print("Reason:")
    print("  The functional risks double-counting e_kappa; fix that accounting before summary.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("The minimal candidate functional is:")
    print()
    print("  epsilon_vac_config =")
    print("    1/2 K_zeta (zeta-zeta_min)^2")
    print("    + 1/2 L_zeta |grad zeta|^2")
    print("    + 1/2 K_lock (kappa-(zeta-zeta_min))^2")
    print()
    print("This is only a scaffold.")
    print()
    print("It must not include:")
    print("  A_flux, M_ext, coefficient tuning, scalar kinetic wave terms.")
    print()
    print("Possible next artifact:")
    print("  candidate_epsilon_vac_config_functional.md")
    print()
    print("Possible next script:")
    print("  candidate_epsilon_kappa_double_counting_check.py")


def main():
    header("Candidate Epsilon Vac Config Functional")
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_minimal_functional()
    case_5_exchange_with_relaxation()
    case_6_failure_controls()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
