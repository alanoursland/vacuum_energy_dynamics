# Candidate reduced exterior action
#
# Group:
#   02_mechanics
#
# Script type:
#   SAMPLE
#
# Purpose
# -------
# This script tests whether one reduced variational toy can unify the two
# successful reduced exterior mechanisms:
#
#   1. kappa suppression:
#        kappa = 0  ->  AB = 1
#
#   2. shear source law:
#        ∇²s = 8πG rho / c²
#        spherical exterior -> s(r) = -2GM/(r c²)
#
# This follows the reduced exterior mode program:
#
#   a = ln A
#   b = ln B
#
#   kappa = (a + b)/2
#   s     = (a - b)/2
#
#   A = exp(kappa + s)
#   B = exp(kappa - s)
#   AB = exp(2*kappa)
#
# Candidate reduced energy/action density:
#
#   L = K_k |∇kappa|² + M_k² kappa²
#       + K_s |∇s|²
#       + alpha rho s
#
# The sign of alpha is chosen so that variation gives:
#
#   ∇²s = 8πG rho / c²
#
# depending on the normalization of K_s.
#
# IMPORTANT:
# This is NOT the full theory, not a covariant action, and not a theorem.
# It is a reduced-sector variational toy.

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
    RouteRecord,
    ScriptOutput,
    StatusMark,
)


ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"


def header(title: str) -> None:
    print()
    print("=" * 96)
    print(title)
    print("=" * 96)


def is_zero(expr) -> bool:
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


def euler_lagrange_density(L, field, coord):
    f = field
    fp = sp.diff(f, coord)
    return sp.simplify(sp.diff(L, f) - sp.diff(sp.diff(L, fp), coord))


def radial_laplacian(expr, r):
    return sp.simplify((1 / r**2) * sp.diff(r**2 * sp.diff(expr, r), r))


def series_in_epsilon(expr, epsilon, order=3):
    return sp.series(expr, epsilon, 0, order).removeO()


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="shear_profile_metric_recovery",
        upstream_script_id="02_mechanics__candidate_shear_profile_source_law",
        upstream_derivation_id="weak_shear_metric_recovery",
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


def case_0_log_scale_algebra(out: ScriptOutput):
    header("Case 0: Log-scale algebra")

    kappa, s = sp.symbols("kappa s", real=True)

    A = sp.exp(kappa + s)
    B = sp.exp(kappa - s)
    AB = sp.simplify(A * B)

    print(f"A  = {A}")
    print(f"B  = {B}")
    print(f"AB = {AB}")

    residual_AB = sp.simplify(AB - sp.exp(2 * kappa))
    residual_AB_k0 = sp.simplify(AB.subs(kappa, 0) - 1)

    with out.derived_results():
        out.line("AB = exp(2*kappa)",
                 StatusMark.PASS if is_zero(residual_AB) else StatusMark.FAIL,
                 f"residual={residual_AB}")
        out.line("kappa=0 gives AB=1",
                 StatusMark.PASS if is_zero(residual_AB_k0) else StatusMark.FAIL,
                 f"residual={residual_AB_k0}")


def case_1_reduced_el_equations_1d(out: ScriptOutput):
    header("Case 1: Reduced Euler-Lagrange equations in one coordinate")

    x = sp.symbols("x", real=True)
    Kk, Mk, Ks, alpha = sp.symbols("K_k M_k K_s alpha", positive=True, real=True)
    rho = sp.Function("rho")(x)

    kappa = sp.Function("kappa")(x)
    s = sp.Function("s")(x)

    L = Kk * sp.diff(kappa, x)**2 + Mk**2 * kappa**2 + Ks * sp.diff(s, x)**2 + alpha * rho * s

    EL_k = euler_lagrange_density(L, kappa, x)
    EL_s = euler_lagrange_density(L, s, x)

    print(f"L = {L}")
    print()
    print("Euler-Lagrange equations:")
    print(f"  EL_kappa = {EL_k} = 0")
    print(f"  EL_s     = {EL_s} = 0")

    EL_k_ext = sp.simplify(EL_k.subs({
        kappa: 0,
        sp.diff(kappa, x): 0,
        sp.diff(kappa, (x, 2)): 0,
    }))

    print()
    print(f"EL_kappa | kappa=0 = {EL_k_ext}")

    with out.sample_results():
        out.line("kappa=0 solves source-free kappa equation",
                 StatusMark.PASS if is_zero(EL_k_ext) else StatusMark.FAIL,
                 f"residual={EL_k_ext}")

    print()
    print("Shear equation rearranged:")
    print("  alpha*rho - 2*K_s*s'' = 0")
    print("  s'' = alpha*rho/(2*K_s)")
    print()
    print("To match the reduced Poisson normalization in Cartesian form, choose:")
    print("  alpha/(2*K_s) = 8πG/c²")


def case_2_3d_variation_target(out: ScriptOutput):
    header("Case 2: 3D reduced variation target and normalization")

    G, c, Ks, alpha = sp.symbols("G c K_s alpha", positive=True, real=True)

    alpha_solution = sp.solve(sp.Eq(alpha / (2 * Ks), 8 * sp.pi * G / c**2), alpha)

    print("Variation of:")
    print("  E_s = ∫ [K_s |∇s|² + alpha rho s] d³x")
    print("gives:")
    print("  ∇²s = alpha rho/(2K_s)")
    print()
    print("Desired:")
    print("  ∇²s = 8πG rho/c²")
    print()
    print(f"alpha solution = {alpha_solution}")

    ok = bool(alpha_solution) and is_zero(alpha_solution[0] - 16 * sp.pi * G * Ks / c**2)

    with out.sample_results():
        out.line("normalization alpha = 16πG K_s/c²",
                 StatusMark.PASS if ok else StatusMark.FAIL,
                 f"solution={alpha_solution}")


def case_3_exterior_spherical_solution(out: ScriptOutput):
    header("Case 3: Exterior spherical solution from reduced source law")

    r, G, M, c = sp.symbols("r G M c", positive=True, real=True)
    C = sp.symbols("C", real=True)

    s_expr = C / r
    lap = radial_laplacian(s_expr, r)

    print(f"s(r) = {s_expr}")
    print(f"∇²s for r>0 = {lap}")

    flux = sp.simplify(4 * sp.pi * r**2 * sp.diff(s_expr, r))
    target_flux = 8 * sp.pi * G * M / c**2
    C_solution = sp.solve(sp.Eq(flux, target_flux), C)

    print()
    print(f"4πr²s'(r) = {flux}")
    print(f"target flux = {target_flux}")
    print(f"C solution = {C_solution}")

    with out.sample_results():
        out.line("C/r is harmonic outside source",
                 StatusMark.PASS if is_zero(lap) else StatusMark.FAIL,
                 f"residual={lap}")

    if C_solution:
        C_val = sp.simplify(C_solution[0])
        s_fixed = sp.simplify(s_expr.subs(C, C_val))
        print(f"s_fixed(r) = {s_fixed}")
        residual_s = sp.simplify(s_fixed + 2 * G * M / (r * c**2))
        with out.sample_results():
            out.line("source flux fixes s=-2GM/(rc²)",
                     StatusMark.PASS if is_zero(residual_s) else StatusMark.FAIL,
                     f"residual={residual_s}")


def case_4_metric_recovery(out: ScriptOutput):
    header("Case 4: Metric recovery")

    eps = sp.symbols("eps", positive=True, real=True)

    kappa = sp.Integer(0)
    s = -2 * eps

    A = sp.exp(kappa + s)
    B = sp.exp(kappa - s)
    AB = sp.simplify(A * B)

    A_series = series_in_epsilon(A, eps, 3)
    B_series = series_in_epsilon(B, eps, 3)

    print(f"kappa = {kappa}")
    print(f"s = {s}")
    print(f"A = {A}")
    print(f"B = {B}")
    print(f"AB = {AB}")
    print()
    print(f"A series = {A_series}")
    print(f"B series = {B_series}")

    residual_A = sp.simplify(A_series - (1 - 2 * eps + 2 * eps**2))
    residual_B = sp.simplify(B_series - (1 + 2 * eps + 2 * eps**2))
    residual_AB = sp.simplify(AB - 1)

    with out.sample_results():
        out.line("A = 1 - 2eps + 2eps² + ...",
                 StatusMark.PASS if is_zero(residual_A) else StatusMark.FAIL,
                 f"residual={residual_A}")
        out.line("B = 1 + 2eps + 2eps² + ...",
                 StatusMark.PASS if is_zero(residual_B) else StatusMark.FAIL,
                 f"residual={residual_B}")
        out.line("AB = 1 exactly",
                 StatusMark.PASS if is_zero(residual_AB) else StatusMark.FAIL,
                 f"residual={residual_AB}")


def case_5_kappa_source_failure_control(out: ScriptOutput):
    header("Case 5: Failure control — direct kappa source")

    x = sp.symbols("x", real=True)
    Kk, Mk, Jk = sp.symbols("K_k M_k J_k", positive=True, real=True)

    kappa = sp.Function("kappa")(x)

    Lk = Kk * sp.diff(kappa, x)**2 + Mk**2 * kappa**2 - Jk * kappa
    EL_k = euler_lagrange_density(Lk, kappa, x)

    print(f"L_k = {Lk}")
    print(f"EL_kappa = {EL_k} = 0")

    k0 = sp.symbols("k0", real=True)
    algebraic = sp.simplify(EL_k.subs({
        kappa: k0,
        sp.diff(kappa, x): 0,
        sp.diff(kappa, (x, 2)): 0,
    }))
    k0_solution = sp.solve(sp.Eq(algebraic, 0), k0)

    print()
    print(f"constant equilibrium equation = {algebraic} = 0")
    print(f"kappa constant solutions = {k0_solution}")

    if k0_solution:
        k_eq = sp.simplify(k0_solution[0])
        AB = sp.simplify(sp.exp(2 * k_eq))
        print(f"kappa_eq = {k_eq}")
        print(f"AB = {AB}")
        with out.governance_assessments():
            out.line("kappa source makes kappa nonzero generically",
                     StatusMark.PASS if k_eq != 0 else StatusMark.FAIL,
                     f"kappa_eq={k_eq}")
            out.line("reciprocal scaling fails generically",
                     StatusMark.PASS if not is_zero(AB - 1) else StatusMark.FAIL,
                     f"AB={AB}")


def case_5b_vacuumforge_energy_crosscheck(out: ScriptOutput, ns=None):
    header("Case 5b: VacuumForge energy cross-check")

    ctx = TheoryContext("candidate_reduced_exterior_action")
    ctx.define_equal_response_algebraic_symbols()
    ms = ctx._mode_symbols
    Jk, Js = sp.symbols("J_k J_s", real=True)

    ctx.energy.source_coupled(
        C_kappa=ms.C_kappa,
        C_sigma=ms.C_sigma,
        J_kappa=Jk,
        J_sigma=Js,
        kappa=ms.kappa,
        sigma=ms.sigma,
    )
    sol = ctx.energy.solve_stationary("source_coupled_energy")
    print(f"Stationary equations: {sol.equations}")
    print(f"Solutions: {sol.solutions}")

    if sol.solutions:
        k_eq = sp.simplify(sol.solutions[0][ms.kappa])
        s_eq = sp.simplify(sol.solutions[0][ms.sigma])
        print(f"kappa_eq = {k_eq}")
        print(f"s_eq = {s_eq}")

        residual_k = sp.simplify(k_eq - Jk / (2 * ms.C_kappa))
        residual_s = sp.simplify(s_eq - Js / (2 * ms.C_sigma))

        with out.sample_results():
            out.line("VacuumForge gives kappa_eq = J_k/(2 C_kappa)",
                     StatusMark.PASS if is_zero(residual_k) else StatusMark.FAIL,
                     f"residual={residual_k}")
            out.line("VacuumForge gives sigma_eq = J_s/(2 C_sigma)",
                     StatusMark.PASS if is_zero(residual_s) else StatusMark.FAIL,
                     f"residual={residual_s}")

        if ns is not None:
            ns.record_derivation(
                derivation_id="vf_reduced_action_stationary_solution",
                inputs=[Jk, Js],
                output=sp.Eq(ms.kappa, Jk / (2 * ms.C_kappa)),
                method="vacuumforge_source_coupled_energy stationary solution",
                status=Status.DERIVED,
                record_kind=RecordKind.SAMPLE_DERIVATION,
                scope="algebraic source-coupled energy toy; not covariant field equation",
                metadata={"sigma_solution": str(sp.Eq(ms.sigma, Js / (2 * ms.C_sigma)))},
            )


def case_6_wrong_shear_coefficient_control(out: ScriptOutput):
    header("Case 6: Failure control — wrong shear coefficient")

    eps, lam = sp.symbols("eps lambda", real=True)

    s = -lam * eps
    A = sp.exp(s)
    A_series = series_in_epsilon(A, eps, 2)

    print(f"s = {s}")
    print(f"A series = {A_series}")

    sol = sp.solve(sp.Eq(A_series, 1 - 2 * eps), lam)
    print(f"lambda solution = {sol}")

    with out.derived_results():
        out.line("weak-field temporal coefficient fixes lambda=2",
                 StatusMark.PASS if sol == [2] else StatusMark.FAIL,
                 f"solution={sol}")


def final_interpretation():
    header("Final interpretation")

    print("This reduced action toy unifies the previous two mechanisms:")
    print()
    print("1. Kappa suppression:")
    print("   K_k |∇kappa|² + M_k² kappa²")
    print("   gives kappa=0 as the relaxed source-free exterior solution.")
    print()
    print("2. Shear source law:")
    print("   K_s |∇s|² + alpha rho s")
    print("   gives ∇²s = alpha rho/(2K_s).")
    print()
    print("Choosing:")
    print("   alpha = 16πG K_s/c²")
    print("gives:")
    print("   ∇²s = 8πG rho/c².")
    print()
    print("For a spherical mass M:")
    print("   s(r) = -2GM/(r c²).")
    print()
    print("With kappa=0:")
    print("   A = exp(s), B = exp(-s), AB = 1.")
    print()
    print("Weak field:")
    print("   A ≈ 1 - 2GM/(r c²)")
    print("   B ≈ 1 + 2GM/(r c²)")
    print()
    print("This is still only a reduced-sector variational toy.")
    print("The next theoretical step is to find the covariant parent of this action")
    print("and explain the origin of the kappa suppression and shear-source coupling.")


def main():
    header("Candidate Reduced Exterior Action")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_log_scale_algebra(out)
    case_1_reduced_el_equations_1d(out)
    case_2_3d_variation_target(out)
    case_3_exterior_spherical_solution(out)
    case_4_metric_recovery(out)
    case_5_kappa_source_failure_control(out)
    case_5b_vacuumforge_energy_crosscheck(out, ns)
    case_6_wrong_shear_coefficient_control(out)
    final_interpretation()

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_covariant_parent_of_reduced_action",
        script_id=SCRIPT_ID,
        title="Derive covariant parent action for reduced kappa-s sector",
        status=ObligationStatus.OPEN,
        description=(
            "Find the full covariant action whose static spherical reduction gives "
            "K_k|∇kappa|²+M_k²kappa²+K_s|∇s|²+alpha*rho*s. "
            "Currently only the reduced-sector toy is available."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_kappa_suppression_mechanism",
        script_id=SCRIPT_ID,
        title="Derive origin of kappa suppression term M_k²kappa²",
        status=ObligationStatus.OPEN,
        description=(
            "Explain why the kappa mode has a mass-like suppression M_k²kappa² "
            "in the reduced action. The coefficient M_k is not derived here."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_shear_source_coupling_coefficient_alpha",
        script_id=SCRIPT_ID,
        title="Derive shear-source coupling coefficient alpha",
        status=ObligationStatus.OPEN,
        description=(
            "The coefficient alpha=16πG K_s/c² is fixed by matching to the Poisson normalization. "
            "Its origin from a deeper principle is not yet derived."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="reduced_exterior_action_is_toy_only",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "The reduced exterior action L=K_k|∇kappa|²+M_k²kappa²+K_s|∇s|²+alpha*rho*s "
            "is a reduced-sector variational toy, not a full covariant action and not a theorem."
        ),
    ))

    ns.record_route(RouteRecord(
        route_id="kappa_s_unified_reduced_action_route",
        script_id=SCRIPT_ID,
        name="Unified kappa-s reduced action candidate",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        description=(
            "The kappa-suppression plus shear-source reduced action candidate unifies "
            "both exterior mechanisms in one toy functional. Requires a covariant parent derivation."
        ),
        required_obligations=[
            "derive_covariant_parent_of_reduced_action",
            "derive_kappa_suppression_mechanism",
            "derive_shear_source_coupling_coefficient_alpha",
        ],
    ))

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
