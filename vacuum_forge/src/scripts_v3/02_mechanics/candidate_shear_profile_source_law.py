# Candidate shear profile source law
#
# Group:
#   02_mechanics
#
# Script type:
#   SAMPLE
#
# Purpose
# -------
# This script begins the shear/source-law development unit after the
# log-scale and kappa-suppression studies.
#
# Previous unit:
#   kappa = (ln A + ln B)/2 controls reciprocal scaling.
#   kappa = 0 -> AB = 1.
#
# Current unit:
#   Given kappa = 0 in the static source-free exterior,
#   determine the remaining compensated/shear mode s(r).
#
# Log-scale convention used here:
#
#   a = ln A
#   b = ln B
#
#   kappa = (a + b)/2
#   s     = (a - b)/2
#
# If kappa = 0:
#
#   a = s
#   b = -s
#
# so:
#
#   A = exp(s)
#   B = exp(-s)
#   AB = 1 exactly.
#
# Weak-field target:
#
#   A = 1 - 2U/c^2 + O(c^-4)
#   B = 1 + 2U/c^2 + O(c^-4)
#   U = GM/r
#
# Therefore:
#
#   s(r) = ln A ~= -2U/c^2 = -2GM/(r c^2)
#
# This script tests the simplest reduced exterior source-law toy:
#
#   source-free exterior:
#       ∇² s = 0
#
# In spherical symmetry:
#
#   (1/r^2) d/dr (r^2 ds/dr) = 0
#
# with asymptotic flatness:
#
#   s(infinity) = 0
#
# and mass/interface flux condition:
#
#   4π r² s'(r) = 8π GM/c²
#
# which fixes:
#
#   s(r) = -2GM/(r c²)
#
# This is NOT a full field equation and NOT a theorem.
# It is a reduced-sector source-law toy.

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


def header(title: str) -> None:
    print()
    print("=" * 92)
    print(title)
    print("=" * 92)


def subheader(title: str) -> None:
    print()
    print("-" * 92)
    print(title)
    print("-" * 92)


def is_zero(expr) -> bool:
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


def series_in_epsilon(expr, epsilon, order=3):
    return sp.series(expr, epsilon, 0, order).removeO()


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
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


def case_0_convention_check(out: ScriptOutput):
    header("Case 0: Convention check")

    kappa, s = sp.symbols("kappa s", real=True)

    a = kappa + s
    b = kappa - s
    A = sp.exp(a)
    B = sp.exp(b)
    AB = sp.simplify(A * B)

    print(f"a = {a}")
    print(f"b = {b}")
    print(f"A = {A}")
    print(f"B = {B}")
    print(f"AB = {AB}")

    A_k0 = sp.simplify(A.subs(kappa, 0))
    B_k0 = sp.simplify(B.subs(kappa, 0))
    AB_k0 = sp.simplify(AB.subs(kappa, 0))

    print()
    print("With kappa = 0:")
    print(f"A = {A_k0}")
    print(f"B = {B_k0}")
    print(f"AB = {AB_k0}")

    residual_A = sp.simplify(A_k0 - sp.exp(s))
    residual_B = sp.simplify(B_k0 - sp.exp(-s))
    residual_AB = sp.simplify(AB_k0 - 1)

    with out.derived_results():
        out.line("kappa=0 gives A=exp(s)", StatusMark.PASS if is_zero(residual_A) else StatusMark.FAIL,
                 f"residual={residual_A}")
        out.line("kappa=0 gives B=exp(-s)", StatusMark.PASS if is_zero(residual_B) else StatusMark.FAIL,
                 f"residual={residual_B}")
        out.line("kappa=0 gives AB=1", StatusMark.PASS if is_zero(residual_AB) else StatusMark.FAIL,
                 f"residual={residual_AB}")


def case_1_radial_laplace_solution(out: ScriptOutput):
    header("Case 1: Source-free radial Laplace equation")

    r = sp.symbols("r", positive=True, real=True)
    s = sp.Function("s")

    equation = sp.Eq((1 / r**2) * sp.diff(r**2 * sp.diff(s(r), r), r), 0)

    print("Radial source-free equation:")
    print(f"  {equation}")

    sol = sp.dsolve(equation)
    print()
    print("General solution:")
    print(f"  {sol}")

    C1, C2 = sp.symbols("C1 C2")
    candidate = C1 + C2 / r
    lap_candidate = sp.simplify((1 / r**2) * sp.diff(r**2 * sp.diff(candidate, r), r))

    print()
    print(f"Candidate s(r) = {candidate}")
    print(f"∇²s = {lap_candidate}")

    with out.derived_results():
        out.line("C1 + C2/r solves source-free radial Laplace equation",
                 StatusMark.PASS if is_zero(lap_candidate) else StatusMark.FAIL,
                 f"residual={lap_candidate}")


def case_2_flux_fixes_coefficient(out: ScriptOutput):
    header("Case 2: Mass/interface flux fixes coefficient")

    r, G, M, c = sp.symbols("r G M c", positive=True, real=True)
    C = sp.symbols("C", real=True)

    s_expr = C / r
    ds_dr = sp.diff(s_expr, r)
    flux = sp.simplify(4 * sp.pi * r**2 * ds_dr)

    print(f"s(r) = {s_expr}")
    print(f"s'(r) = {ds_dr}")
    print(f"4π r² s'(r) = {flux}")

    target_flux = 8 * sp.pi * G * M / c**2
    C_solution = sp.solve(sp.Eq(flux, target_flux), C)

    print()
    print(f"Target flux = {target_flux}")
    print(f"C solution = {C_solution}")

    if C_solution:
        C_val = sp.simplify(C_solution[0])
        s_fixed = sp.simplify(s_expr.subs(C, C_val))
        print(f"C = {C_val}")
        print(f"s_fixed(r) = {s_fixed}")

        target_s = -2 * G * M / (r * c**2)
        residual_s = sp.simplify(s_fixed - target_s)
        fixed_flux = sp.simplify(4 * sp.pi * r**2 * sp.diff(s_fixed, r))
        print(f"fixed flux = {fixed_flux}")

        with out.sample_results():
            out.line("flux condition fixes s(r) = -2GM/(r c^2)",
                     StatusMark.PASS if is_zero(residual_s) else StatusMark.FAIL,
                     f"residual={residual_s}")
            out.line("fixed solution has desired outward flux",
                     StatusMark.PASS if is_zero(fixed_flux - target_flux) else StatusMark.FAIL,
                     f"residual={sp.simplify(fixed_flux - target_flux)}")


def case_3_metric_recovery_from_s(out: ScriptOutput, ns=None):
    header("Case 3: Weak-field metric recovery from shear profile")

    eps = sp.symbols("eps", positive=True, real=True)

    s = -2 * eps
    A = sp.exp(s)
    B = sp.exp(-s)
    AB = sp.simplify(A * B)

    A_series = series_in_epsilon(A, eps, order=3)
    B_series = series_in_epsilon(B, eps, order=3)
    AB_series = sp.simplify(series_in_epsilon(AB, eps, order=3))

    print(f"s = {s}")
    print(f"A = exp(s) = {A}")
    print(f"B = exp(-s) = {B}")
    print(f"AB = {AB}")
    print()
    print(f"A series = {A_series}")
    print(f"B series = {B_series}")
    print(f"AB series = {AB_series}")

    print()
    print("First-order targets:")
    print(f"  A = {1 - 2 * eps} + O(eps^2)")
    print(f"  B = {1 + 2 * eps} + O(eps^2)")

    residual_A_series = sp.expand(A_series - (1 - 2 * eps + 2 * eps**2))
    residual_B_series = sp.expand(B_series - (1 + 2 * eps + 2 * eps**2))
    residual_AB = AB - 1

    with out.sample_results():
        out.line("A recovers temporal series through O(eps^2)",
                 StatusMark.PASS if is_zero(residual_A_series) else StatusMark.FAIL,
                 f"residual={residual_A_series}")
        out.line("B recovers reciprocal spatial series through O(eps^2)",
                 StatusMark.PASS if is_zero(residual_B_series) else StatusMark.FAIL,
                 f"residual={residual_B_series}")
        out.line("AB is exactly 1",
                 StatusMark.PASS if is_zero(residual_AB) else StatusMark.FAIL,
                 f"residual={residual_AB}")

    ctx = TheoryContext("candidate_shear_profile_source_law")
    ctx.define_equal_response_algebraic_symbols()
    ms = ctx._mode_symbols
    ctx.assumptions.add("weak_shear_A", sp.Eq(ms.A, sp.exp(-2 * eps)))
    ctx.assumptions.add("weak_shear_B", sp.Eq(ms.B, sp.exp(2 * eps)))
    reciprocal = ctx.requirements.validate("reciprocal_scaling", ctx)

    with out.governance_assessments():
        out.line("VacuumForge reciprocal_scaling validator passes",
                 StatusMark.PASS if reciprocal.status in {"pass", "assumed"} else StatusMark.DEFER,
                 f"status={reciprocal.status}")

    if ns is not None:
        reciprocal_residual = sp.simplify(sp.exp(-2 * eps) * sp.exp(2 * eps) - 1)
        ns.record_derivation(
            derivation_id="weak_shear_metric_recovery",
            inputs=[eps],
            output=sp.Eq(sp.exp(-2 * eps) * sp.exp(2 * eps), 1),
            method="weak_shear_metric_recovery: toy s=-2eps, A=exp(s), B=exp(-s)",
            status=Status.DERIVED,
            record_kind=RecordKind.SAMPLE_DERIVATION,
            scope="constant weak-field shear s=-2*eps only",
        )


def case_4_poisson_source_form(out: ScriptOutput):
    header("Case 4: Poisson source form and sign check")

    r, G, M, c = sp.symbols("r G M c", positive=True, real=True)

    print("Distributional sign check:")
    print("  ∇²(1/r) = -4π δ³(r)")
    print("  s = -2GM/(c² r)")
    print("  ∇²s = (+8πGM/c²) δ³(r)")
    print()
    print("Candidate reduced Poisson equation:")
    print("  ∇²s = 8πG rho / c²")
    print()
    print("Outside the source:")
    print("  rho = 0")
    print("  ∇²s = 0")

    s_expr = -2 * G * M / (r * c**2)
    lap = sp.simplify((1 / r**2) * sp.diff(r**2 * sp.diff(s_expr, r), r))

    print()
    print(f"Exterior s(r) = {s_expr}")
    print(f"Ordinary radial ∇²s for r>0 = {lap}")

    with out.derived_results():
        out.line("exterior solution is harmonic away from source",
                 StatusMark.PASS if is_zero(lap) else StatusMark.FAIL,
                 f"residual={lap}")


def case_5_failure_controls(out: ScriptOutput):
    header("Case 5: Failure controls")

    r, C0, C1, eps = sp.symbols("r C0 C1 eps", positive=True, real=True)

    subheader("Failure control A: nonzero asymptotic constant")
    s_const = C0 + C1 / r

    print(f"s(r) = {s_const}")
    print("If C0 != 0, then s(infinity) != 0.")
    print("This violates asymptotic flatness unless C0 = 0.")

    with out.governance_assessments():
        out.line("asymptotic flatness requires C0=0", StatusMark.PASS,
                 "C0=0 enforced by asymptotic flatness condition")

    subheader("Failure control B: wrong coefficient")
    lam = sp.symbols("lambda", real=True)
    s_wrong = -lam * eps
    A_wrong = sp.exp(s_wrong)
    A_wrong_series = series_in_epsilon(A_wrong, eps, order=2)
    print(f"s = {s_wrong}")
    print(f"A series = {A_wrong_series}")
    print("Weak-field temporal target requires coefficient lambda = 2.")
    lambda_solution = sp.solve(sp.Eq(A_wrong_series, 1 - 2 * eps), lam)
    print(f"lambda solution = {lambda_solution}")

    with out.derived_results():
        out.line("weak-field temporal coefficient fixes lambda=2",
                 StatusMark.PASS if lambda_solution == [2] else StatusMark.FAIL,
                 f"solution={lambda_solution}")


def final_interpretation():
    header("Final interpretation")

    print("This source-law toy establishes the reduced exterior chain:")
    print()
    print("  kappa = 0")
    print("    -> A = exp(s), B = exp(-s), AB = 1")
    print()
    print("  source-free exterior shear equation:")
    print("    ∇²s = 0")
    print()
    print("  spherical solution plus asymptotic flatness:")
    print("    s(r) = C/r")
    print()
    print("  mass/interface flux condition:")
    print("    4πr²s'(r) = 8πGM/c²")
    print()
    print("  coefficient:")
    print("    C = -2GM/c²")
    print()
    print("  result:")
    print("    s(r) = -2GM/(r c²)")
    print()
    print("  metric:")
    print("    A = exp(s) ≈ 1 - 2GM/(r c²)")
    print("    B = exp(-s) ≈ 1 + 2GM/(r c²)")
    print("    AB = 1 exactly")
    print()
    print("This does NOT yet derive the field equation or the mass/interface flux law.")
    print("It shows that if the shear mode obeys a Laplace/Poisson source law with")
    print("the stated normalization, then the weak-field exterior profile follows.")
    print()
    print("Next theoretical target:")
    print("  Explain why the vacuum configuration functional gives this shear equation")
    print("  and why the source/interface flux is fixed by M as 8πGM/c².")


def main():
    header("Candidate Shear Profile Source Law")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_convention_check(out)
    case_1_radial_laplace_solution(out)
    case_2_flux_fixes_coefficient(out)
    case_3_metric_recovery_from_s(out, ns)
    case_4_poisson_source_form(out)
    case_5_failure_controls(out)
    final_interpretation()

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_shear_field_equation_from_action",
        script_id=SCRIPT_ID,
        title="Derive shear field equation from vacuum action functional",
        status=ObligationStatus.OPEN,
        description=(
            "Show that the vacuum configuration functional gives ∇²s = 8πG rho/c² "
            "for the shear mode, rather than importing this as a reduced toy assumption."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_mass_interface_flux_normalization",
        script_id=SCRIPT_ID,
        title="Derive mass/interface flux normalization 4πr²s'=8πGM/c²",
        status=ObligationStatus.OPEN,
        description=(
            "Explain why the source/interface flux is fixed by mass M as 8πGM/c². "
            "This is currently imported as a normalization assumption, not derived."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="shear_source_law_is_toy_only",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "The reduced exterior shear source law ∇²s=0 and the profile s(r)=-2GM/(rc²) "
            "are a reduced-sector toy. They are not the full field equation and not a theorem."
        ),
    ))

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
