# Candidate static spherical exact recovery
#
# Group:
#   02_mechanics
#
# Script type:
#   SAMPLE
#
# Purpose
# -------
# This script tests whether the reduced static spherical exterior program can
# be upgraded from weak-field recovery to exact Schwarzschild exterior recovery.
#
# Previous reduced result:
#
#   kappa = 0
#   A = exp(s)
#   B = exp(-s)
#   AB = 1
#
# Weak-field source-law toy used:
#
#   s_weak(r) = - r_s/r
#   where r_s = 2GM/c^2
#
# giving:
#
#   A = exp(-r_s/r) ≈ 1 - r_s/r
#
# This matches Schwarzschild only to first order.
#
# Exact Schwarzschild exterior in areal gauge has:
#
#   A_exact = 1 - r_s/r
#   B_exact = 1/A_exact
#   AB = 1
#
# Therefore exact compensated shear would be:
#
#   s_exact = ln(A_exact) = ln(1 - r_s/r)
#
# Question:
#   What source-free equation does s_exact satisfy?
#
# Since A = exp(s), if A is harmonic:
#
#   ∇²A = 0
#
# then:
#
#   ∇² exp(s) = exp(s) [∇²s + |∇s|²] = 0
#
# so:
#
#   ∇²s + |∇s|² = 0
#
# This script tests:
#
#   1. exact Schwarzschild satisfies kappa=0 and AB=1;
#   2. s_weak is harmonic outside source but only weakly matches A_exact;
#   3. s_exact is not harmonic under the flat radial Laplacian;
#   4. A_exact is harmonic outside source;
#   5. s_exact satisfies the nonlinear equation ∇²s + |∇s|² = 0;
#   6. the nonlinear equation linearizes to ∇²s = 0 in weak field;
#   7. flux normalization recovers r_s=2GM/c²;
#   8. the exact redshift factor emerges from A=1-r_s/r.
#
# IMPORTANT:
# This is still a reduced areal-gauge static spherical toy.
# It is not a derivation of Einstein's equations.

from pathlib import Path

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.core.context import TheoryContext
from vacuumforge.metric.concrete_check import check_concrete_metric
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
    print("=" * 108)
    print(title)
    print("=" * 108)


def subheader(title: str) -> None:
    print()
    print("-" * 108)
    print(title)
    print("-" * 108)


def is_zero(expr) -> bool:
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


def radial_laplacian(expr, r):
    """Flat 3D radial Laplacian for spherical scalar f(r)."""
    return sp.simplify((1 / r**2) * sp.diff(r**2 * sp.diff(expr, r), r))


def radial_grad_sq(expr, r):
    """Flat radial |grad f|^2 for spherical scalar f(r)."""
    return sp.simplify(sp.diff(expr, r)**2)


def series_at_infinity(expr, r, order=4):
    """Series in x=1/r around x=0."""
    x = sp.symbols("x", positive=True, real=True)
    expr_x = sp.simplify(expr.subs(r, 1/x))
    ser_x = sp.series(expr_x, x, 0, order).removeO()
    return sp.simplify(ser_x.subs(x, 1/r))


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="kappa_leak_mixed_source",
        upstream_script_id="002_mechanics__candidate_kappa_leak_deviation",
        upstream_derivation_id="vf_mixed_source_kappa_leak",
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
# Case 0: Exact Schwarzschild compensated exterior
# =============================================================================

def case_0_exact_schwarzschild_compensated(out: ScriptOutput):
    header("Case 0: Exact Schwarzschild compensated exterior")

    r, r_s = sp.symbols("r r_s", positive=True, real=True)

    A = 1 - r_s / r
    B = sp.simplify(1 / A)
    kappa = sp.simplify(sp.Rational(1, 2) * sp.log(A * B))
    s_from_definition = sp.simplify(sp.Rational(1, 2) * sp.log(A / B))
    s_exact = sp.log(A)

    print(f"A_exact = {A}")
    print(f"B_exact = {B}")
    print(f"A B = {sp.simplify(A*B)}")
    print(f"kappa = {kappa}")
    print(f"s from 1/2 ln(A/B) = {s_from_definition}")
    print(f"s_exact = ln(A) = {s_exact}")
    print()
    print("For r > r_s, 1/2 ln(A/B) = ln(A).")

    residual_AB = sp.simplify(A * B - 1)
    residual_B_from_s = sp.simplify(sp.exp(-s_exact) - B)

    with out.derived_results():
        out.line("exact Schwarzschild has AB=1",
                 StatusMark.PASS if is_zero(residual_AB) else StatusMark.FAIL,
                 f"residual={residual_AB}")
        out.line("exact Schwarzschild has kappa=0",
                 StatusMark.PASS if is_zero(residual_AB) else StatusMark.FAIL,
                 "AB=1 implies kappa=0")
        out.line("s=ln(A) reconstructs B=1/A",
                 StatusMark.PASS if is_zero(residual_B_from_s) else StatusMark.FAIL,
                 f"residual={residual_B_from_s}")


# =============================================================================
# Case 1: Weak shear versus exact shear
# =============================================================================

def case_1_weak_vs_exact_shear(out: ScriptOutput):
    header("Case 1: Weak shear versus exact shear")

    r, r_s = sp.symbols("r r_s", positive=True, real=True)

    s_weak = -r_s / r
    A_weak_exp = sp.exp(s_weak)

    A_exact = 1 - r_s / r
    s_exact = sp.log(A_exact)

    print(f"s_weak = {s_weak}")
    print(f"A_from_s_weak = exp(s_weak) = {A_weak_exp}")
    print(f"A_exact = {A_exact}")
    print(f"s_exact = ln(A_exact) = {s_exact}")

    print()
    print("Large-r expansions:")
    print(f"A_from_s_weak = {series_at_infinity(A_weak_exp, r, 4)}")
    print(f"A_exact       = {series_at_infinity(A_exact, r, 4)}")
    print(f"s_exact       = {series_at_infinity(s_exact, r, 4)}")
    print(f"s_weak        = {s_weak}")

    first_order_match = sp.simplify(series_at_infinity(A_weak_exp - A_exact, r, 3))
    print()
    print(f"A_weak_exp - A_exact through order 1/r² = {first_order_match}")

    residual_first = sp.expand(series_at_infinity(A_weak_exp - A_exact, r, 2))
    residual_second = sp.expand(series_at_infinity(A_weak_exp - A_exact, r, 3))

    with out.sample_results():
        out.line("weak exponential A matches exact A at first order",
                 StatusMark.PASS if is_zero(residual_first) else StatusMark.FAIL,
                 f"residual={residual_first}")
        out.line("weak exponential differs at second order",
                 StatusMark.PASS if not is_zero(residual_second) else StatusMark.FAIL,
                 f"residual={residual_second}")


# =============================================================================
# Case 2: Harmonic tests for weak and exact shear
# =============================================================================

def case_2_harmonic_tests(out: ScriptOutput):
    header("Case 2: Harmonic tests for weak and exact shear")

    r, r_s = sp.symbols("r r_s", positive=True, real=True)

    s_weak = -r_s / r
    A_exact = 1 - r_s / r
    s_exact = sp.log(A_exact)

    lap_s_weak = radial_laplacian(s_weak, r)
    lap_s_exact = sp.simplify(radial_laplacian(s_exact, r))
    lap_A_exact = radial_laplacian(A_exact, r)

    print(f"∇² s_weak = {lap_s_weak}")
    print(f"∇² s_exact = {lap_s_exact}")
    print(f"∇² A_exact = {lap_A_exact}")

    with out.derived_results():
        out.line("s_weak is harmonic for r>0",
                 StatusMark.PASS if is_zero(lap_s_weak) else StatusMark.FAIL,
                 f"residual={lap_s_weak}")
        out.line("s_exact is not harmonic under flat radial Laplacian",
                 StatusMark.PASS if not is_zero(lap_s_exact) else StatusMark.FAIL,
                 f"lap_s_exact={lap_s_exact}")
        out.line("A_exact is harmonic for r>0",
                 StatusMark.PASS if is_zero(lap_A_exact) else StatusMark.FAIL,
                 f"residual={lap_A_exact}")

    print()
    print("Interpretation:")
    print("  The weak-field source law ∇²s=0 is linearized.")
    print("  Exact Schwarzschild suggests the source-free harmonic variable is A=e^s,")
    print("  not s itself.")


# =============================================================================
# Case 3: Nonlinear s equation
# =============================================================================

def case_3_nonlinear_s_equation(out: ScriptOutput, ns=None):
    header("Case 3: Nonlinear s equation from harmonic A=e^s")

    r, r_s = sp.symbols("r r_s", positive=True, real=True)

    A_exact = 1 - r_s / r
    s_exact = sp.log(A_exact)

    lap_s = radial_laplacian(s_exact, r)
    grad_s_sq = radial_grad_sq(s_exact, r)

    nonlinear = sp.simplify(lap_s + grad_s_sq)

    print(f"s_exact = {s_exact}")
    print(f"∇²s = {lap_s}")
    print(f"|∇s|² = {grad_s_sq}")
    print(f"∇²s + |∇s|² = {nonlinear}")

    with out.derived_results():
        out.line("s_exact satisfies nonlinear source-free equation",
                 StatusMark.PASS if is_zero(nonlinear) else StatusMark.FAIL,
                 f"residual={nonlinear}")

    print()
    print("Equation:")
    print("  ∇²s + |∇s|² = 0")
    print()
    print("Equivalent:")
    print("  ∇² exp(s) = 0")

    if ns is not None:
        ns.record_derivation(
            derivation_id="nonlinear_s_equation_from_exact_schwarzschild",
            inputs=[s_exact, r_s],
            output=nonlinear,
            method="compute ∇²s + |∇s|² for s=ln(1-r_s/r) via flat radial Laplacian",
            status=Status.DERIVED,
            record_kind=RecordKind.DERIVATION,
            result_type="identity_residual",
        )


# =============================================================================
# Case 4: Linearization of nonlinear s equation
# =============================================================================

def case_4_linearization(out: ScriptOutput, ns=None):
    header("Case 4: Linearization of nonlinear s equation")

    r, eps = sp.symbols("r eps", positive=True, real=True)
    u = sp.Function("u")(r)

    s = eps * u

    lap_s = radial_laplacian(s, r)
    grad_s_sq = radial_grad_sq(s, r)
    nonlinear = sp.expand(lap_s + grad_s_sq)

    first_order = sp.series(nonlinear, eps, 0, 2).removeO()
    second_order = sp.series(nonlinear, eps, 0, 3).removeO()

    print(f"s = eps*u(r)")
    print(f"∇²s + |∇s|² = {nonlinear}")
    print(f"first order in eps = {first_order}")
    print(f"through second order in eps = {second_order}")

    expected_first = eps * radial_laplacian(u, r)
    residual = sp.simplify(first_order - expected_first)

    with out.derived_results():
        out.line("linearized nonlinear equation is ∇²u=0",
                 StatusMark.PASS if is_zero(residual) else StatusMark.FAIL,
                 f"residual={residual}")

    print()
    print("Interpretation:")
    print("  The earlier shear Laplace law is the first-order approximation")
    print("  to the nonlinear exact candidate equation.")

    if ns is not None:
        ns.record_derivation(
            derivation_id="nonlinear_s_equation_linearization",
            inputs=[s, eps],
            output=first_order,
            method="series expansion of ∇²s+|∇s|² in eps to first order",
            status=Status.DERIVED,
            record_kind=RecordKind.DERIVATION,
            result_type="linearization_residual",
        )


# =============================================================================
# Case 5: Flux normalization for A
# =============================================================================

def case_5_flux_normalization_for_A(out: ScriptOutput, ns=None):
    header("Case 5: Flux normalization for A")

    r, r_s, G, M, c = sp.symbols("r r_s G M c", positive=True, real=True)

    A = 1 - r_s / r
    dA = sp.diff(A, r)
    flux_A = sp.simplify(4 * sp.pi * r**2 * dA)

    target_flux = 8 * sp.pi * G * M / c**2
    sol_rs = sp.solve(sp.Eq(flux_A, target_flux), r_s)

    print(f"A = {A}")
    print(f"A' = {dA}")
    print(f"4πr² A' = {flux_A}")
    print(f"target flux = {target_flux}")
    print(f"r_s solution = {sol_rs}")

    passes = bool(sol_rs) and is_zero(sol_rs[0] - 2 * G * M / c**2)

    with out.sample_results():
        out.line("A-flux normalization gives r_s=2GM/c²",
                 StatusMark.PASS if passes else StatusMark.FAIL,
                 f"solution={sol_rs}")

    print()
    print("Note:")
    print("  This parallels the earlier s-flux normalization in weak field,")
    print("  but the exact harmonic variable is A rather than s.")

    if ns is not None and passes:
        ns.record_derivation(
            derivation_id="a_flux_normalization_gives_schwarzschild_radius",
            inputs=[flux_A, target_flux],
            output=sp.Eq(r_s, 2 * G * M / c**2),
            method="solve 4πr²A'=8πGM/c² for r_s with A=1-r_s/r",
            status=Status.DERIVED,
            record_kind=RecordKind.SAMPLE_DERIVATION,
            scope="areal-gauge static spherical toy; flux normalization assumption",
        )


# =============================================================================
# Case 6: Poisson form for A and nonlinear form for s
# =============================================================================

def case_6_poisson_form_for_A(out: ScriptOutput):
    header("Case 6: Poisson form for A and nonlinear form for s")

    print("Candidate exact reduced source law:")
    print()
    print("  ∇²A = 8πG rho / c²")
    print()
    print("with:")
    print()
    print("  A = exp(s)")
    print()
    print("In source-free exterior:")
    print()
    print("  ∇²A = 0")
    print()
    print("Equivalent s equation:")
    print()
    print("  ∇²s + |∇s|² = 0")
    print()
    print("In weak field, |∇s|² is second order, so:")
    print()
    print("  ∇²s ≈ 0")
    print()

    with out.governance_assessments():
        out.line("candidate exact law reduces to weak shear Laplace law", StatusMark.PASS,
                 "linearization shows ∇²s+|∇s|²=0 reduces to ∇²s=0 at first order in s")


# =============================================================================
# Case 7: Exact metric recovery
# =============================================================================

def case_7_exact_metric_recovery(out: ScriptOutput, ns=None):
    header("Case 7: Exact metric recovery")

    r, r_s = sp.symbols("r r_s", positive=True, real=True)

    A = 1 - r_s / r
    s = sp.log(A)
    kappa = sp.Integer(0)
    B = sp.exp(kappa - s)
    AB = sp.simplify(A * B)

    print(f"A = {A}")
    print(f"s = ln(A) = {s}")
    print(f"kappa = {kappa}")
    print(f"B = exp(-s) = {B}")
    print(f"AB = {AB}")

    residual_B = sp.simplify(B - 1/A)
    residual_AB = sp.simplify(AB - 1)

    with out.derived_results():
        out.line("B equals 1/A",
                 StatusMark.PASS if is_zero(residual_B) else StatusMark.FAIL,
                 f"residual={residual_B}")
        out.line("AB=1 exactly",
                 StatusMark.PASS if is_zero(residual_AB) else StatusMark.FAIL,
                 f"residual={residual_AB}")

    print()
    print("Result:")
    print("  kappa=0 and s=ln(1-r_s/r) recover exact Schwarzschild")
    print("  areal-gauge exterior metric factors.")

    ctx = TheoryContext("candidate_static_spherical_exact_recovery")
    ctx.define_equal_response_algebraic_symbols()
    ms = ctx._mode_symbols
    A_value = 1 - 2 * ms.G * ms.M / (ms.r * ms.c**2)
    B_value = sp.simplify(1 / A_value)
    concrete = check_concrete_metric(ctx, A_value=A_value, B_value=B_value, requirement_ids=["reciprocal_scaling"])
    if concrete:
        with out.governance_assessments():
            out.line(
                "VacuumForge classifies exact Schwarzschild reciprocal scaling as by-construction",
                StatusMark.PASS if concrete[0].status == "satisfied_by_construction" else StatusMark.DEFER,
                concrete[0].message,
            )
        if ns is not None:
            ns.record_derivation(
                derivation_id="exact_schwarzschild_concrete_metric_check",
                inputs=[A_value],
                output=sp.Symbol(concrete[0].status),
                method="concrete_metric_check: reciprocal_scaling requirement",
                status=Status.DERIVED,
                record_kind=RecordKind.COMPATIBILITY_EXAMPLE,
                result_type="compatibility_check",
                metadata={"message": concrete[0].message},
            )


# =============================================================================
# Case 8: Comparison of source-law candidates
# =============================================================================

def case_8_compare_source_law_candidates(out: ScriptOutput):
    header("Case 8: Compare source-law candidates")

    print("Weak-field candidate:")
    print("  ∇²s = 0 outside source")
    print("  s = -r_s/r")
    print("  A = exp(s) = exp(-r_s/r)")
    print("  matches Schwarzschild only at first order")
    print()
    print("Exact candidate:")
    print("  ∇²A = 0 outside source")
    print("  A = 1 - r_s/r")
    print("  s = ln(A)")
    print("  equivalently ∇²s + |∇s|² = 0")
    print("  recovers exact Schwarzschild exterior factors under kappa=0")
    print()
    print("Interpretation:")
    print("  The earlier shear Poisson law may be the linearized form of a")
    print("  nonlinear exact law for A=e^s.")

    with out.governance_assessments():
        out.line("exact candidate A-harmonic law subsumes weak-field shear Laplace law",
                 StatusMark.PASS,
                 "nonlinear ∇²A=0 linearizes to ∇²s=0 at first order")


# =============================================================================
# Case 9: Summary classification
# =============================================================================

def case_9_summary_classification():
    header("Case 9: Summary classification")

    print("Results:")
    print()
    print("1. Exact Schwarzschild in areal gauge has:")
    print("     A = 1 - r_s/r")
    print("     B = 1/A")
    print("     AB = 1")
    print("     kappa = 0")
    print()
    print("2. Therefore exact shear is:")
    print("     s_exact = ln(1 - r_s/r)")
    print()
    print("3. The weak shear:")
    print("     s_weak = -r_s/r")
    print("   matches only to first order.")
    print()
    print("4. s_exact is not harmonic:")
    print("     ∇²s_exact != 0")
    print()
    print("5. A_exact is harmonic:")
    print("     ∇²A_exact = 0")
    print()
    print("6. Therefore s_exact satisfies:")
    print("     ∇²s + |∇s|² = 0")
    print()
    print("7. The nonlinear s equation linearizes to:")
    print("     ∇²s = 0")
    print()
    print("8. The A-flux normalization gives:")
    print("     r_s = 2GM/c²")


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("This exact-recovery toy suggests a refinement:")
    print()
    print("  The weak-field shear source law ∇²s = 0 is probably linearized.")
    print()
    print("For exact static spherical recovery, the better source-free variable may be:")
    print()
    print("  A = exp(s)")
    print()
    print("with exact exterior equation:")
    print()
    print("  ∇²A = 0")
    print()
    print("or equivalently:")
    print()
    print("  ∇²s + |∇s|² = 0")
    print()
    print("Then:")
    print()
    print("  A = 1 - r_s/r")
    print("  s = ln(1 - r_s/r)")
    print("  B = 1/A")
    print("  kappa = 0")
    print()
    print("This recovers exact Schwarzschild exterior metric factors in areal gauge.")
    print()
    print("This is still not a derivation of Einstein's equations.")
    print("It is a reduced exact static spherical candidate.")
    print()
    print("Possible next artifact:")
    print("  candidate_static_spherical_exact_recovery.md")


# =============================================================================
# Main
# =============================================================================

def main():
    header("Candidate Static Spherical Exact Recovery")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_exact_schwarzschild_compensated(out)
    case_1_weak_vs_exact_shear(out)
    case_2_harmonic_tests(out)
    case_3_nonlinear_s_equation(out, ns)
    case_4_linearization(out, ns)
    case_5_flux_normalization_for_A(out, ns)
    case_6_poisson_form_for_A(out)
    case_7_exact_metric_recovery(out, ns)
    case_8_compare_source_law_candidates(out)
    case_9_summary_classification()
    final_interpretation()

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_covariant_field_equation_for_exact_recovery",
        script_id=SCRIPT_ID,
        title="Derive covariant field equation producing ∇²A=0 in exterior",
        status=ObligationStatus.OPEN,
        description=(
            "The exact exterior equation ∇²A=0 (equivalently ∇²s+|∇s|²=0) is found "
            "by checking Schwarzschild, but the covariant field equation from which it "
            "follows has not been derived. This is not a derivation of Einstein's equations."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_areal_flux_normalization_mechanism",
        script_id=SCRIPT_ID,
        title="Derive mechanism that fixes A-flux normalization to 8πGM/c²",
        status=ObligationStatus.OPEN,
        description=(
            "The flux normalization 4πr²A'=8πGM/c² is imposed by matching to the "
            "Schwarzschild radius. Its origin from a source/interface law is not derived."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="exact_static_spherical_recovery_is_toy",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "The exact Schwarzschild exterior recovery via kappa=0 and ∇²A=0 is a reduced "
            "areal-gauge static spherical toy. It is not a derivation of Einstein's equations."
        ),
    ))

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
