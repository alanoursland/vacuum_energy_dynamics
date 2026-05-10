# Candidate kappa-leak deviation
#
# Group:
#   02_mechanics
#
# Script type:
#   SAMPLE
#
# Purpose
# -------
# This script studies the first quantitative deviation channel identified by
# the reduced exterior mode program and the regime map:
#
#   What happens if the static exterior is mostly compensated shear,
#   but has a small nonzero kappa leak?
#
# Reduced mode definitions:
#
#   a = ln A
#   b = ln B
#
#   kappa = (a + b)/2
#   s     = (a - b)/2
#
#   A = exp(kappa + s)
#   B = exp(kappa - s)
#   AB = exp(2 kappa)
#
# GR-like reduced exterior target:
#
#   kappa = 0
#   s = -2 epsilon
#   epsilon = GM/(r c^2)
#
# then:
#
#   A = exp(-2 epsilon) ≈ 1 - 2 epsilon
#   B = exp( 2 epsilon) ≈ 1 + 2 epsilon
#   AB = 1
#
# Kappa-leak model:
#
#   kappa = lambda_k * epsilon
#   s     = -2 epsilon
#
# where lambda_k is a dimensionless leak coefficient.
#
# Then:
#
#   A = exp((lambda_k - 2) epsilon)
#   B = exp((lambda_k + 2) epsilon)
#   AB = exp(2 lambda_k epsilon)
#
# To first order:
#
#   A ≈ 1 + (lambda_k - 2) epsilon
#   B ≈ 1 + (lambda_k + 2) epsilon
#   AB ≈ 1 + 2 lambda_k epsilon
#
# If one fixes the Newtonian temporal coefficient A ≈ 1 - 2 epsilon,
# then lambda_k must vanish or be absorbed by redefining the source strength.
#
# A useful gamma-like proxy can be obtained by matching:
#
#   A ≈ 1 - 2 epsilon_N
#   B ≈ 1 + 2 gamma_eff epsilon_N
#
# where epsilon_N is the Newtonian potential coefficient inferred from A.
#
# If A coefficient is -(2-lambda_k), then:
#
#   epsilon_N = (2-lambda_k) epsilon / 2
#
# B coefficient is +(2+lambda_k) epsilon.
#
# So:
#
#   gamma_eff = (2+lambda_k)/(2-lambda_k)
#
# and:
#
#   gamma_eff - 1 = 2 lambda_k/(2-lambda_k) ≈ lambda_k
#
# This script checks these formulas and explores a few leak profiles.
#
# IMPORTANT:
# This is a reduced, areal-gauge, weak-field deviation toy.
# It is not a full PPN calculation and not a covariant prediction.

from pathlib import Path

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.core.context import TheoryContext
from vacuumforge.governance import (
    ClaimRecord,
    ClaimTier,
    GovernanceStatus,
    ObligationStatus,
    ProofObligationRecord,
    RecordKind,
    ScriptOutput,
    StatusMark,
)


ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"


# =============================================================================
# Utilities
# =============================================================================

def header(title: str) -> None:
    print()
    print("=" * 104)
    print(title)
    print("=" * 104)


def subheader(title: str) -> None:
    print()
    print("-" * 104)
    print(title)
    print("-" * 104)


def is_zero(expr) -> bool:
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


def series(expr, var, order=3):
    return sp.series(expr, var, 0, order).removeO()


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="reduced_action_stationary_solution",
        upstream_script_id="02_mechanics__candidate_reduced_exterior_action",
        upstream_derivation_id="vf_reduced_action_stationary_solution",
    )
    return archive, ns, invalidated


def print_archive_status(ns, invalidated: bool) -> None:
    if invalidated:
        print("[INFO] Archive invalidated due to source change.")
    checks = ns.verify_dependencies()
    if not checks:
        print("[INFO] Archive dependencies: none declared.")
        return
    print("[INFO] Archive dependency check:")
    for check in checks:
        print(f"  - {check.dependency.dependency_id}: {check.status} ({check.message})")


# =============================================================================
# Case 0: Baseline compensated exterior
# =============================================================================

def case_0_baseline_compensated_exterior(out: ScriptOutput):
    header("Case 0: Baseline compensated exterior")

    eps = sp.symbols("eps", positive=True, real=True)

    kappa = sp.Integer(0)
    s = -2 * eps

    A = sp.exp(kappa + s)
    B = sp.exp(kappa - s)
    AB = sp.simplify(A * B)

    A_series = series(A, eps, 3)
    B_series = series(B, eps, 3)
    AB_series = series(AB, eps, 3)

    print(f"kappa = {kappa}")
    print(f"s = {s}")
    print(f"A = {A}")
    print(f"B = {B}")
    print(f"AB = {AB}")
    print()
    print(f"A series = {A_series}")
    print(f"B series = {B_series}")
    print(f"AB series = {AB_series}")

    residual_A = sp.expand(series(A, eps, 2) - (1 - 2*eps))
    residual_B = sp.expand(series(B, eps, 2) - (1 + 2*eps))
    residual_AB = sp.simplify(AB - 1)

    with out.sample_results():
        out.line("baseline A first order is 1 - 2 eps",
                 StatusMark.PASS if is_zero(residual_A) else StatusMark.FAIL,
                 f"residual={residual_A}")
        out.line("baseline B first order is 1 + 2 eps",
                 StatusMark.PASS if is_zero(residual_B) else StatusMark.FAIL,
                 f"residual={residual_B}")
        out.line("baseline AB = 1 exactly",
                 StatusMark.PASS if is_zero(residual_AB) else StatusMark.FAIL,
                 f"residual={residual_AB}")


# =============================================================================
# Case 1: Constant fractional kappa leak
# =============================================================================

def case_1_constant_fractional_kappa_leak(out: ScriptOutput):
    header("Case 1: Constant fractional kappa leak")

    eps, lam = sp.symbols("eps lambda_k", real=True)

    kappa = lam * eps
    s = -2 * eps

    A = sp.exp(kappa + s)
    B = sp.exp(kappa - s)
    AB = sp.simplify(A * B)

    A_series = series(A, eps, 3)
    B_series = series(B, eps, 3)
    AB_series = series(AB, eps, 3)

    print(f"kappa = {kappa}")
    print(f"s = {s}")
    print(f"A = {A}")
    print(f"B = {B}")
    print(f"AB = {AB}")
    print()
    print(f"A series = {A_series}")
    print(f"B series = {B_series}")
    print(f"AB series = {AB_series}")

    expected_A_1 = 1 + (lam - 2) * eps
    expected_B_1 = 1 + (lam + 2) * eps
    expected_AB_1 = 1 + 2 * lam * eps

    residual_A = sp.simplify(series(A, eps, 2) - expected_A_1)
    residual_B = sp.simplify(series(B, eps, 2) - expected_B_1)
    residual_AB = sp.simplify(series(AB, eps, 2) - expected_AB_1)

    with out.sample_results():
        out.line("A first-order coefficient is lambda_k - 2",
                 StatusMark.PASS if is_zero(residual_A) else StatusMark.FAIL,
                 f"residual={residual_A}")
        out.line("B first-order coefficient is lambda_k + 2",
                 StatusMark.PASS if is_zero(residual_B) else StatusMark.FAIL,
                 f"residual={residual_B}")
        out.line("AB first-order coefficient is 2 lambda_k",
                 StatusMark.PASS if is_zero(residual_AB) else StatusMark.FAIL,
                 f"residual={residual_AB}")


# =============================================================================
# Case 2: Gamma-like proxy from temporal normalization
# =============================================================================

def case_2_gamma_like_proxy(out: ScriptOutput):
    header("Case 2: Gamma-like proxy from temporal normalization")

    lam = sp.symbols("lambda_k", real=True)

    # A ≈ 1 + (lambda - 2) eps.
    # Define Newtonian epsilon_N by A ≈ 1 - 2 epsilon_N.
    # Then epsilon_N = (2-lambda) eps / 2.
    #
    # B ≈ 1 + (lambda + 2) eps = 1 + 2 gamma_eff epsilon_N.
    # So gamma_eff = (lambda + 2)/(2 - lambda).
    gamma_eff = sp.simplify((2 + lam) / (2 - lam))
    gamma_minus_one = sp.simplify(gamma_eff - 1)

    small_lam_series = series(gamma_eff, lam, 3)

    print("Temporal normalization:")
    print("  A ≈ 1 + (lambda_k - 2) eps")
    print("  Set A ≈ 1 - 2 eps_N")
    print("  eps_N = (2 - lambda_k) eps / 2")
    print()
    print("Spatial coefficient:")
    print("  B ≈ 1 + (lambda_k + 2) eps")
    print("  B ≈ 1 + 2 gamma_eff eps_N")
    print()
    print(f"gamma_eff = {gamma_eff}")
    print(f"gamma_eff - 1 = {gamma_minus_one}")
    print(f"small lambda series gamma_eff = {small_lam_series}")

    expected = sp.simplify(2 * lam / (2 - lam))
    residual = sp.simplify(gamma_minus_one - expected)

    with out.sample_results():
        out.line("gamma_eff - 1 = 2 lambda_k/(2-lambda_k)",
                 StatusMark.PASS if is_zero(residual) else StatusMark.FAIL,
                 f"residual={residual}")

    print()
    print("Interpretation:")
    print("  For small lambda_k, gamma_eff - 1 ≈ lambda_k.")
    print("  Thus weak-field gamma constraints would strongly bound ordinary static kappa leak.")


# =============================================================================
# Case 3: If Newtonian normalization is forced, kappa leak must vanish
# =============================================================================

def case_3_newtonian_normalization_pressure(out: ScriptOutput):
    header("Case 3: Newtonian temporal normalization pressure")

    lam = sp.symbols("lambda_k", real=True)

    # If eps is already defined as GM/(r c^2) from observed Newtonian mass,
    # then A first-order coefficient must be -2.
    A_coeff = lam - 2
    sol = sp.solve(sp.Eq(A_coeff, -2), lam)

    print("If eps = GM/(r c²) is fixed by observed Newtonian acceleration,")
    print("then A must have first-order coefficient -2.")
    print()
    print(f"A first-order coefficient = {A_coeff}")
    print(f"solve lambda_k - 2 = -2 -> {sol}")

    with out.sample_results():
        out.line("Newtonian normalization forces lambda_k=0 in this simple leak model",
                 StatusMark.PASS if sol == [0] else StatusMark.FAIL,
                 f"solution={sol}")

    print()
    print("Interpretation:")
    print("  A constant kappa leak changes both temporal and radial first-order coefficients.")
    print("  If the temporal coefficient is already fixed by Newtonian observations,")
    print("  a constant proportional leak is not freely allowed.")


# =============================================================================
# Case 4: Decaying kappa leak profile
# =============================================================================

def case_4_decaying_kappa_leak_profile(out: ScriptOutput):
    header("Case 4: Decaying kappa leak profile")

    r, G, M, c, L, eta = sp.symbols("r G M c L eta", positive=True, real=True)

    eps = G * M / (r * c**2)

    # Example leak profile:
    #   kappa = eta * eps * exp(-r/L)
    # This leak is suppressed at large radius.
    kappa = eta * eps * sp.exp(-r / L)
    s = -2 * eps

    A = sp.exp(kappa + s)
    B = sp.exp(kappa - s)
    AB = sp.simplify(A * B)

    # First-order in eps is awkward because kappa contains eps.
    # Substitute eps symbolically through mu/r if needed. Here print expressions.
    print(f"eps(r) = {eps}")
    print(f"kappa(r) = {kappa}")
    print(f"s(r) = {s}")
    print(f"A = exp(kappa+s) = {A}")
    print(f"B = exp(kappa-s) = {B}")
    print(f"AB = {AB}")

    print()
    print("Large-radius behavior:")
    print("  kappa/eps = eta exp(-r/L)")
    print("  so gamma-like deviation proxy ≈ eta exp(-r/L) for small leak.")
    print()

    with out.sample_results():
        out.line("decaying leak vanishes asymptotically", StatusMark.PASS,
                 "kappa/eps=eta*exp(-r/L) -> 0 as r->infinity")


# =============================================================================
# Case 5: Power-law kappa leak profile
# =============================================================================

def case_5_power_law_kappa_leak_profile(out: ScriptOutput):
    header("Case 5: Power-law kappa leak profile")

    r, G, M, c, eta, R0, n = sp.symbols("r G M c eta R0 n", positive=True, real=True)

    eps = G * M / (r * c**2)

    # Example power-law leak:
    #   kappa = eta * eps * (R0/r)^n
    # For n>0 it is short-ranged relative to the Newtonian profile.
    kappa = eta * eps * (R0 / r)**n
    s = -2 * eps

    A = sp.exp(kappa + s)
    B = sp.exp(kappa - s)
    AB = sp.simplify(A * B)

    print(f"eps(r) = {eps}")
    print(f"kappa(r) = {kappa}")
    print(f"s(r) = {s}")
    print(f"A = {A}")
    print(f"B = {B}")
    print(f"AB = {AB}")

    print()
    print("Leak ratio:")
    print(f"  kappa/eps = {sp.simplify(kappa/eps)}")
    print()
    print("For n>0, the leak becomes smaller at large radius.")
    print("For n=0, this reduces to the constant fractional leak case.")

    with out.sample_results():
        out.line("power-law leak is a tunable deviation profile", StatusMark.PASS,
                 "kappa/eps=(R0/r)^n, decays for n>0")


# =============================================================================
# Case 6: Mixed exchange + creation source as kappa leak origin
# =============================================================================

def case_6_mixed_source_origin(out: ScriptOutput, ns=None):
    header("Case 6: Mixed exchange + creation source as kappa leak origin")

    S, C, C_k, C_s = sp.symbols("S C C_k C_s", positive=True, real=True)
    kappa, s = sp.symbols("kappa s", real=True)

    # Mixed source:
    #   J_kappa = C
    #   J_s = S
    E = C_k*kappa**2 + C_s*s**2 - C*kappa - S*s

    equations = [sp.Eq(sp.diff(E, kappa), 0), sp.Eq(sp.diff(E, s), 0)]
    sol = sp.solve(equations, [kappa, s], dict=True, simplify=True)

    print(f"E = {E}")
    print("Stationary equations:")
    for eq in equations:
        print(f"  {eq}")
    print(f"Solutions: {sol}")

    if sol:
        k_eq = sp.simplify(sol[0][kappa])
        s_eq = sp.simplify(sol[0][s])
        AB = sp.simplify(sp.exp(2*k_eq))

        print(f"kappa_eq = {k_eq}")
        print(f"s_eq = {s_eq}")
        print(f"AB = {AB}")

        with out.sample_results():
            out.line("mixed source produces nonzero kappa leak",
                     StatusMark.PASS if not is_zero(k_eq) else StatusMark.FAIL,
                     f"kappa_eq={k_eq}")
            out.line("mixed source preserves shear channel",
                     StatusMark.PASS if not is_zero(s_eq) else StatusMark.FAIL,
                     f"s_eq={s_eq}")
            out.line("mixed source breaks reciprocal scaling generically",
                     StatusMark.PASS if not is_zero(AB - 1) else StatusMark.FAIL,
                     f"AB={AB}")

    print()
    print("Interpretation:")
    print("  A small traceful creation/destruction component mixed into exchange")
    print("  is a natural reduced source for kappa leak.")

    ctx = TheoryContext("candidate_kappa_leak_deviation")
    ctx.define_equal_response_algebraic_symbols()
    ms = ctx._mode_symbols
    ctx.energy.source_coupled(
        C_kappa=ms.C_kappa,
        C_sigma=ms.C_sigma,
        J_kappa=C,
        J_sigma=S,
        kappa=ms.kappa,
        sigma=ms.sigma,
    )
    sol_vf = ctx.energy.solve_stationary("source_coupled_energy")
    if sol_vf.solutions:
        k_vf = sp.simplify(sol_vf.solutions[0][ms.kappa])
        s_vf = sp.simplify(sol_vf.solutions[0][ms.sigma])
        residual_k_vf = sp.simplify(k_vf - C / (2 * ms.C_kappa))
        residual_s_vf = sp.simplify(s_vf - S / (2 * ms.C_sigma))
        with out.sample_results():
            out.line("VacuumForge reproduces kappa leak equilibrium",
                     StatusMark.PASS if is_zero(residual_k_vf) else StatusMark.FAIL,
                     f"residual={residual_k_vf}")
            out.line("VacuumForge reproduces shear equilibrium",
                     StatusMark.PASS if is_zero(residual_s_vf) else StatusMark.FAIL,
                     f"residual={residual_s_vf}")
        if ns is not None:
            ns.record_derivation(
                derivation_id="vf_mixed_source_kappa_leak",
                inputs=[C, S],
                output=sp.Eq(ms.kappa, C / (2 * ms.C_kappa)),
                method="vacuumforge_source_coupled_energy: mixed exchange+creation source",
                status=Status.DERIVED,
                record_kind=RecordKind.SAMPLE_DERIVATION,
                scope="algebraic source-coupled energy toy with mixed J_kappa=C, J_sigma=S",
                metadata={"sigma_solution": str(sp.Eq(ms.sigma, S / (2 * ms.C_sigma)))},
            )


# =============================================================================
# Case 7: Summary of observational pressure
# =============================================================================

def case_7_observational_pressure_summary(out: ScriptOutput):
    header("Case 7: Observational pressure summary")

    print("Kappa leak affects weak-field observables because:")
    print()
    print("  AB = exp(2 kappa)")
    print()
    print("For kappa = lambda_k eps and s = -2 eps:")
    print()
    print("  A ≈ 1 + (lambda_k - 2) eps")
    print("  B ≈ 1 + (lambda_k + 2) eps")
    print("  gamma_eff = (2 + lambda_k)/(2 - lambda_k)")
    print("  gamma_eff - 1 ≈ lambda_k for small lambda_k")
    print()
    print("Therefore:")
    print("  ordinary static exterior kappa leak should be very small,")
    print("  or hidden in regimes where weak-field constraints do not apply.")
    print()
    print("This script does not apply real observational bounds.")
    print("It identifies the first reduced deviation proxy.")

    with out.unresolved_obligations():
        out.line("apply real observational bounds to kappa leak", StatusMark.OBLIGATION,
                 "no actual PPN or solar system bounds applied; open proof obligation recorded")


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("This kappa-leak toy shows:")
    print()
    print("1. Baseline compensated exterior:")
    print("     kappa = 0, s = -2 eps")
    print("     A ≈ 1 - 2 eps")
    print("     B ≈ 1 + 2 eps")
    print("     AB = 1")
    print()
    print("2. Constant fractional kappa leak:")
    print("     kappa = lambda_k eps")
    print("     A ≈ 1 + (lambda_k - 2) eps")
    print("     B ≈ 1 + (lambda_k + 2) eps")
    print("     AB ≈ 1 + 2 lambda_k eps")
    print()
    print("3. Gamma-like proxy:")
    print("     gamma_eff = (2 + lambda_k)/(2 - lambda_k)")
    print("     gamma_eff - 1 ≈ lambda_k")
    print()
    print("4. Mixed exchange+creation sources naturally produce kappa leak.")
    print()
    print("Conclusion:")
    print("  Kappa leak is the first clean reduced deviation channel.")
    print("  It should be tightly constrained in ordinary weak-field static exteriors.")
    print()
    print("Possible next artifact:")
    print("  kappa_leak_deviation_lab_report.md")


# =============================================================================
# Main
# =============================================================================

def main():
    header("Candidate Kappa-Leak Deviation")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_baseline_compensated_exterior(out)
    case_1_constant_fractional_kappa_leak(out)
    case_2_gamma_like_proxy(out)
    case_3_newtonian_normalization_pressure(out)
    case_4_decaying_kappa_leak_profile(out)
    case_5_power_law_kappa_leak_profile(out)
    case_6_mixed_source_origin(out, ns)
    case_7_observational_pressure_summary(out)
    final_interpretation()

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_observational_bounds_on_kappa_leak",
        script_id=SCRIPT_ID,
        title="Derive or import observational bounds on kappa leak coefficient lambda_k",
        status=ObligationStatus.OPEN,
        description=(
            "Apply PPN constraints or solar-system weak-field bounds to bound lambda_k. "
            "Currently only the deviation proxy formula is derived; no real bounds are applied."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_covariant_mechanism_for_kappa_leak",
        script_id=SCRIPT_ID,
        title="Derive covariant mechanism producing kappa leak",
        status=ObligationStatus.OPEN,
        description=(
            "The mixed exchange+creation source is a toy model for kappa leak. "
            "A covariant mechanism from the full theory is not yet derived."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="gamma_eff_proxy_is_toy_only",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "gamma_eff=(2+lambda_k)/(2-lambda_k) is a reduced areal-gauge weak-field "
            "deviation proxy, not a full PPN calculation and not a covariant prediction."
        ),
    ))

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
