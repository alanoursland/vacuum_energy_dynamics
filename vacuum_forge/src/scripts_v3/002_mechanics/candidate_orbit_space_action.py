# Candidate orbit-space action
#
# Group:
#   02_mechanics
#
# Script type:
#   SAMPLE
#
# Purpose
# -------
# This script follows the exact static spherical recovery result.
#
# The exact recovery suggested:
#
#   A = exp(s)
#
# is the better source variable, not s itself.
#
# Candidate exact static spherical source law:
#
#   ∇²A = 8πG rho / c²
#
# In source-free exterior:
#
#   ∇²A = 0
#
# In terms of s:
#
#   ∇² exp(s) = 0
#   ∇²s + |∇s|² = 0
#
# This script tests candidate variational principles:
#
#   1. Linear weak-field s-action:
#        E_s = ∫ [K_s |∇s|² + alpha rho s] d³x
#
#      gives:
#        ∇²s = alpha rho / (2K_s)
#
#   2. Exact candidate A-action:
#        E_A = ∫ [K_A |∇A|² + beta rho A] d³x
#
#      gives:
#        ∇²A = beta rho / (2K_A)
#
#   3. Nonlinear s-action induced by A=exp(s):
#        E_s_exact = ∫ [K_A exp(2s)|∇s|² + beta rho exp(s)] d³x
#
#      should be equivalent to the A-action under A=exp(s).
#
#   4. Source-free exterior exact equation:
#        ∇²A = 0
#      recovers:
#        A = 1 - r_s/r
#        s = ln(1-r_s/r)
#        B = 1/A under kappa=0
#
#   5. Orbit-space compensation condition:
#        A = |∇R|²
#      connects the action variable A to the geometric reduced condition.
#
# IMPORTANT:
# This is a reduced static spherical variational toy.
# It is not a covariant action for the full theory.

from pathlib import Path

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    ClaimRecord,
    ClaimTier,
    GovernanceStatus,
    ObligationStatus,
    ProofObligationRecord,
    RecordKind,
    RouteRecord,
    ScriptOutput,
    StatusMark,
)


ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"


def header(title: str) -> None:
    print()
    print("=" * 108)
    print(title)
    print("=" * 108)


def is_zero(expr) -> bool:
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


def euler_lagrange_1d(L, field, x):
    f = field
    fp = sp.diff(f, x)
    return sp.simplify(sp.diff(L, f) - sp.diff(sp.diff(L, fp), x))


def radial_laplacian(expr, r):
    return sp.simplify((1 / r**2) * sp.diff(r**2 * sp.diff(expr, r), r))


def radial_grad_sq(expr, r):
    return sp.simplify(sp.diff(expr, r)**2)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="exact_metric_recovery",
        upstream_script_id="002_mechanics__candidate_static_spherical_exact_recovery",
        upstream_derivation_id="exact_schwarzschild_concrete_metric_check",
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


def case_0_recap_exact_source_variable(out: ScriptOutput, ns=None):
    header("Case 0: Recap exact source variable")

    r, r_s = sp.symbols("r r_s", positive=True, real=True)

    A = 1 - r_s / r
    s = sp.log(A)
    B = sp.exp(-s)

    lap_A = radial_laplacian(A, r)
    nonlinear_s = sp.simplify(radial_laplacian(s, r) + radial_grad_sq(s, r))

    print(f"A_exact = {A}")
    print(f"s_exact = ln(A) = {s}")
    print(f"B = exp(-s) = {B}")
    print(f"AB = {sp.simplify(A*B)}")
    print()
    print(f"∇²A = {lap_A}")
    print(f"∇²s + |∇s|² = {nonlinear_s}")

    residual_AB = sp.simplify(A * B - 1)

    with out.derived_results():
        out.line("A is harmonic outside source",
                 StatusMark.PASS if is_zero(lap_A) else StatusMark.FAIL,
                 f"residual={lap_A}")
        out.line("s satisfies nonlinear source-free equation",
                 StatusMark.PASS if is_zero(nonlinear_s) else StatusMark.FAIL,
                 f"residual={nonlinear_s}")
        out.line("kappa=0 gives AB=1",
                 StatusMark.PASS if is_zero(residual_AB) else StatusMark.FAIL,
                 f"residual={residual_AB}")


def case_1_weak_field_s_action(out: ScriptOutput, ns=None):
    header("Case 1: Weak-field linear s-action")

    x = sp.symbols("x", real=True)
    K_s, alpha = sp.symbols("K_s alpha", positive=True, real=True)
    rho = sp.Function("rho")(x)
    s = sp.Function("s")(x)

    L = K_s * sp.diff(s, x)**2 + alpha * rho * s
    EL = euler_lagrange_1d(L, s, x)

    print(f"L_s = {L}")
    print(f"Euler-Lagrange = {EL} = 0")
    print()
    print("Rearranged:")
    print("  s'' = alpha rho / (2 K_s)")
    print()
    print("This is the weak-field linear action used earlier.")

    expected = alpha * rho - 2 * K_s * sp.diff(s, (x, 2))
    residual = sp.simplify(EL - expected)

    with out.sample_results():
        out.line("linear s-action gives Poisson equation for s",
                 StatusMark.PASS if is_zero(residual) else StatusMark.FAIL,
                 f"residual={residual}")

    if ns is not None:
        ns.record_derivation(
            derivation_id="weak_field_s_action_el_equation",
            inputs=[L, s],
            output=EL,
            method="Euler-Lagrange of K_s*(s')^2 + alpha*rho*s",
            status=Status.DERIVED,
            record_kind=RecordKind.SAMPLE_DERIVATION,
            scope="1D toy model; not covariant",
        )


def case_2_exact_A_action(out: ScriptOutput, ns=None):
    header("Case 2: Exact candidate A-action")

    x = sp.symbols("x", real=True)
    K_A, beta = sp.symbols("K_A beta", positive=True, real=True)
    rho = sp.Function("rho")(x)
    A = sp.Function("A")(x)

    L = K_A * sp.diff(A, x)**2 + beta * rho * A
    EL = euler_lagrange_1d(L, A, x)

    print(f"L_A = {L}")
    print(f"Euler-Lagrange = {EL} = 0")
    print()
    print("Rearranged:")
    print("  A'' = beta rho / (2 K_A)")
    print()
    print("To match:")
    print("  ∇²A = 8πG rho / c²")
    print("choose:")
    print("  beta/(2K_A) = 8πG/c²")
    print("  beta = 16πG K_A/c²")

    G, c = sp.symbols("G c", positive=True, real=True)
    beta_sol = 16 * sp.pi * G * K_A / c**2
    print(f"beta = {beta_sol}")

    expected = beta * rho - 2 * K_A * sp.diff(A, (x, 2))
    residual = sp.simplify(EL - expected)

    with out.sample_results():
        out.line("A-action gives Poisson equation for A",
                 StatusMark.PASS if is_zero(residual) else StatusMark.FAIL,
                 f"residual={residual}")

    if ns is not None:
        ns.record_derivation(
            derivation_id="exact_a_action_el_equation",
            inputs=[L, A],
            output=EL,
            method="Euler-Lagrange of K_A*(A')^2 + beta*rho*A",
            status=Status.DERIVED,
            record_kind=RecordKind.SAMPLE_DERIVATION,
            scope="1D toy model; not covariant",
        )


def case_3_nonlinear_s_action_from_A(out: ScriptOutput, ns=None):
    header("Case 3: Nonlinear s-action induced by A=exp(s)")

    x = sp.symbols("x", real=True)
    K_A, beta = sp.symbols("K_A beta", positive=True, real=True)
    rho = sp.Function("rho")(x)
    s = sp.Function("s")(x)

    A = sp.exp(s)
    Ap = sp.diff(A, x)

    L_s_exact = sp.simplify(K_A * Ap**2 + beta * rho * A)
    EL_s = sp.simplify(euler_lagrange_1d(L_s_exact, s, x))

    print(f"A = exp(s)")
    print(f"A' = {Ap}")
    print(f"L_s_exact = {L_s_exact}")
    print(f"Euler-Lagrange wrt s = {EL_s}")

    EL_A_sub = beta * rho - 2 * K_A * sp.diff(A, (x, 2))
    expected = sp.simplify(EL_A_sub * sp.exp(s))

    print()
    print(f"Expected EL_s = exp(s) * [beta rho - 2K_A A''] = {expected}")

    residual = sp.simplify(EL_s - expected)

    with out.sample_results():
        out.line("nonlinear s-action is equivalent to A-action under A=exp(s)",
                 StatusMark.PASS if is_zero(residual) else StatusMark.FAIL,
                 f"residual={residual}")

    if ns is not None:
        ns.record_derivation(
            derivation_id="nonlinear_s_action_equivalence_to_a_action",
            inputs=[L_s_exact, s],
            output=EL_s,
            method="Euler-Lagrange of K_A*(e^s*s')^2 + beta*rho*e^s; verify = e^s*EL_A",
            status=Status.DERIVED,
            record_kind=RecordKind.SAMPLE_DERIVATION,
            scope="1D toy; equivalence under A=exp(s) substitution",
        )


def case_4_radial_source_free_A_equation(out: ScriptOutput):
    header("Case 4: Radial source-free A equation")

    r, r_s = sp.symbols("r r_s", positive=True, real=True)
    A = 1 - r_s / r
    s = sp.log(A)

    lap_A = radial_laplacian(A, r)
    nonlinear_s = sp.simplify(radial_laplacian(s, r) + radial_grad_sq(s, r))

    print(f"A = {A}")
    print(f"s = ln(A) = {s}")
    print(f"∇²A = {lap_A}")
    print(f"∇²s + |∇s|² = {nonlinear_s}")

    with out.derived_results():
        out.line("A=1-r_s/r solves radial source-free A equation",
                 StatusMark.PASS if is_zero(lap_A) else StatusMark.FAIL,
                 f"residual={lap_A}")
        out.line("s=ln(1-r_s/r) solves nonlinear s equation",
                 StatusMark.PASS if is_zero(nonlinear_s) else StatusMark.FAIL,
                 f"residual={nonlinear_s}")


def case_5_radial_A_action_with_measure(out: ScriptOutput, ns=None):
    header("Case 5: Radial A-action with spherical measure")

    r = sp.symbols("r", positive=True, real=True)
    K_A, beta = sp.symbols("K_A beta", positive=True, real=True)
    rho = sp.Function("rho")(r)
    A = sp.Function("A")(r)

    L_radial = r**2 * (K_A * sp.diff(A, r)**2 + beta * rho * A)
    EL = euler_lagrange_1d(L_radial, A, r)

    print(f"L_radial = {L_radial}")
    print(f"Euler-Lagrange = {EL} = 0")

    expected = sp.simplify(r**2 * beta * rho - 2 * K_A * sp.diff(r**2 * sp.diff(A, r), r))
    print(f"Expected = {expected}")

    residual = sp.simplify(EL - expected)

    with out.sample_results():
        out.line("radial A-action gives spherical Poisson equation",
                 StatusMark.PASS if is_zero(residual) else StatusMark.FAIL,
                 f"residual={residual}")

    print()
    print("Rearranged:")
    print("  (1/r²)(r² A')' = beta rho/(2K_A)")
    print("  ∇²A = beta rho/(2K_A)")

    if ns is not None:
        ns.record_derivation(
            derivation_id="radial_a_action_spherical_poisson",
            inputs=[L_radial, A],
            output=EL,
            method="Euler-Lagrange of r^2*(K_A*(A')^2+beta*rho*A) with spherical measure",
            status=Status.DERIVED,
            record_kind=RecordKind.SAMPLE_DERIVATION,
            scope="radial 1D reduction; not covariant",
        )


def case_6_flux_normalization(out: ScriptOutput):
    header("Case 6: Flux normalization")

    r, r_s, G, M, c = sp.symbols("r r_s G M c", positive=True, real=True)

    A = 1 - r_s / r
    flux = sp.simplify(4 * sp.pi * r**2 * sp.diff(A, r))
    target = 8 * sp.pi * G * M / c**2
    sol = sp.solve(sp.Eq(flux, target), r_s)

    print(f"A = {A}")
    print(f"4πr² A' = {flux}")
    print(f"target = {target}")
    print(f"r_s solution = {sol}")

    passes = bool(sol) and is_zero(sol[0] - 2*G*M/c**2)

    with out.sample_results():
        out.line("flux normalization gives Schwarzschild radius",
                 StatusMark.PASS if passes else StatusMark.FAIL,
                 f"solution={sol}")


def case_7_combine_with_kappa_suppression(out: ScriptOutput):
    header("Case 7: Combine A-action with kappa suppression toy")

    x = sp.symbols("x", real=True)
    K_k, M_k, K_A, beta = sp.symbols("K_k M_k K_A beta", positive=True, real=True)
    rho = sp.Function("rho")(x)
    kappa = sp.Function("kappa")(x)
    A = sp.Function("A")(x)

    L = (
        K_k * sp.diff(kappa, x)**2
        + M_k**2 * kappa**2
        + K_A * sp.diff(A, x)**2
        + beta * rho * A
    )

    EL_k = euler_lagrange_1d(L, kappa, x)
    EL_A = euler_lagrange_1d(L, A, x)

    print(f"L = {L}")
    print()
    print(f"EL_kappa = {EL_k} = 0")
    print(f"EL_A     = {EL_A} = 0")

    expected_k = 2*M_k**2*kappa - 2*K_k*sp.diff(kappa, (x,2))
    expected_A = beta*rho - 2*K_A*sp.diff(A, (x,2))

    residual_k = sp.simplify(EL_k - expected_k)
    residual_A = sp.simplify(EL_A - expected_A)

    with out.sample_results():
        out.line("kappa equation gives suppression when unsourced",
                 StatusMark.PASS if is_zero(residual_k) else StatusMark.FAIL,
                 f"residual={residual_k}")
        out.line("A equation gives source law",
                 StatusMark.PASS if is_zero(residual_A) else StatusMark.FAIL,
                 f"residual={residual_A}")


def case_8_orbit_space_compensation(out: ScriptOutput):
    header("Case 8: Orbit-space compensation reminder")

    X = sp.symbols("X", positive=True, real=True)
    T = sp.Function("T")(X)
    Q = sp.Function("Q")(X)
    S = sp.Function("S")(X)

    gradR2 = sp.simplify(sp.diff(S, X)**2 / Q)
    kappa_orbit = sp.simplify(sp.Rational(1,2) * sp.log(T / gradR2))

    print("Static spherical orbit-space metric:")
    print("  ds² = -T(X)c²dt² + Q(X)dX² + S(X)²dΩ²")
    print()
    print(f"|∇R|² = {gradR2}")
    print(f"kappa = 1/2 ln(A/|∇R|²) = {kappa_orbit}")
    print()
    print("Compensation kappa=0 gives:")
    print("  A = |∇R|²")
    print("  T Q = S'²")
    print()
    print("Exact Schwarzschild exterior satisfies this with A=1-r_s/r.")

    with out.governance_assessments():
        out.line("orbit-space condition supplies geometric compensation target", StatusMark.PASS,
                 "kappa=0 gives A=|∇R|², connecting A-action variable to geometric reduction")


def case_9_summary_classification():
    header("Case 9: Summary classification")

    print("Results:")
    print()
    print("1. The weak-field s-action gives:")
    print("     ∇²s = alpha rho/(2K_s)")
    print()
    print("2. The exact candidate A-action gives:")
    print("     ∇²A = beta rho/(2K_A)")
    print()
    print("3. Choosing:")
    print("     beta = 16πG K_A/c²")
    print("   gives:")
    print("     ∇²A = 8πG rho/c²")
    print()
    print("4. Under A=exp(s), the A-action becomes nonlinear in s:")
    print("     exp(2s)|∇s|² + rho exp(s)")
    print()
    print("5. Source-free exterior gives:")
    print("     ∇²A = 0")
    print("   or:")
    print("     ∇²s + |∇s|² = 0")
    print()
    print("6. The combined toy has:")
    print("     kappa suppression + A sourcing")
    print()
    print("This is a reduced exact static spherical action candidate,")
    print("not a full covariant action.")


def final_interpretation():
    header("Final interpretation")

    print("This action probe supports the exact-recovery refinement:")
    print()
    print("  The linear weak-field action should be written in s.")
    print("  The exact static spherical candidate is cleaner in A=exp(s).")
    print()
    print("Candidate exact reduced action sector:")
    print()
    print("  E_A = ∫ [K_A |∇A|² + beta rho A] d³x")
    print()
    print("with:")
    print()
    print("  beta = 16πG K_A/c²")
    print()
    print("gives:")
    print()
    print("  ∇²A = 8πG rho/c²")
    print()
    print("Under A=exp(s), this becomes a nonlinear s-action and yields:")
    print()
    print("  ∇²s + |∇s|² = 0")
    print()
    print("in source-free exterior.")
    print()
    print("Combining with kappa suppression gives the reduced exact-sector toy:")
    print()
    print("  kappa suppressed")
    print("  A=e^s sourced")
    print("  B=1/A when kappa=0")
    print()
    print("Possible next artifact:")
    print("  candidate_orbit_space_action.md")


def main():
    header("Candidate Orbit-Space Action")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_recap_exact_source_variable(out, ns)
    case_1_weak_field_s_action(out, ns)
    case_2_exact_A_action(out, ns)
    case_3_nonlinear_s_action_from_A(out, ns)
    case_4_radial_source_free_A_equation(out)
    case_5_radial_A_action_with_measure(out, ns)
    case_6_flux_normalization(out)
    case_7_combine_with_kappa_suppression(out)
    case_8_orbit_space_compensation(out)
    case_9_summary_classification()
    final_interpretation()

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_covariant_parent_of_orbit_space_action",
        script_id=SCRIPT_ID,
        title="Derive covariant parent action for the exact A-action candidate",
        status=ObligationStatus.OPEN,
        description=(
            "The exact candidate A-action E_A=∫[K_A|∇A|²+beta*rho*A]d³x is a reduced "
            "static spherical toy. Its covariant parent in the full theory is not derived."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_beta_coefficient_from_first_principles",
        script_id=SCRIPT_ID,
        title="Derive beta=16πG K_A/c² from first principles",
        status=ObligationStatus.OPEN,
        description=(
            "The coupling beta=16πG K_A/c² is fixed by matching to the Poisson normalization. "
            "Its origin from a deeper variational or geometric principle is not derived."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="orbit_space_action_is_toy_only",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "The candidate A-action and orbit-space compensation toy are reduced static "
            "spherical candidates, not a full covariant action for the theory."
        ),
    ))

    ns.record_route(RouteRecord(
        route_id="exact_a_action_candidate_route",
        script_id=SCRIPT_ID,
        name="Exact candidate A-action for static spherical exterior",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        description=(
            "E_A=∫[K_A|∇A|²+beta*rho*A]d³x with beta=16πG K_A/c² is a candidate reduced "
            "exact action. Recovers Schwarzschild exterior under kappa=0. Requires covariant "
            "parent derivation."
        ),
        required_obligations=[
            "derive_covariant_parent_of_orbit_space_action",
            "derive_beta_coefficient_from_first_principles",
        ],
    ))

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
