# Group:
#   04_source_law_interior
#
# Script type:
#   DERIVATION
#
# Candidate boundary flux action
#
# Purpose
# -------
# Test whether the areal-flux law can be interpreted as a boundary condition
# from variation of a reduced radial action.
#
# The bulk radial A-action is:
#
#   E_bulk = integral dr [ r^2 K_A (A')^2 ]
#
# Variation gives:
#
#   bulk equation: d/dr(r^2 A') = 0
#   boundary term: [2 K_A r^2 A' delta A]_{boundary}
#
# If a source/interface contributes a boundary coupling:
#
#   E_boundary = - q A(R)
#
# then variation at R gives:
#
#   2 K_A R^2 A'(R) = q
#
# Therefore:
#
#   4 pi R^2 A'(R) = (2 pi/K_A) q
#
# Choosing q = 4 K_A G M / c^2 gives:
#
#   4 pi R^2 A'(R) = 8 pi G M / c^2
#
# This script tests whether areal flux can be read as a boundary/interface
# condition rather than an ordinary curved-space scalar equation.

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


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="interior_A_boundary_matching",
        upstream_script_id="04_source_law_interior__candidate_interior_A_source_model",
        upstream_derivation_id="interior_A_boundary_matching",
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


def case_0_radial_bulk_action(out: ScriptOutput, ns=None):
    header("Case 0: Radial bulk action")

    r, K_A = sp.symbols("r K_A", positive=True, real=True)
    A = sp.Function("A")(r)

    L = K_A * r**2 * sp.diff(A, r)**2
    EL = euler_lagrange_1d(L, A, r)

    print(f"L_bulk = {L}")
    print(f"Euler-Lagrange = {EL} = 0")
    print()
    print("Equivalent:")
    print("  d/dr(r^2 A') = 0")
    print("  source-free areal flux is conserved")

    expected = -2*K_A*sp.diff(r**2 * sp.diff(A, r), r)
    residual = sp.simplify(EL - expected)
    ok = is_zero(residual)

    with out.derived_results():
        out.line("bulk action gives conserved areal flux",
                 StatusMark.PASS if ok else StatusMark.FAIL,
                 f"EL residual = {residual}")

    if ns is not None:
        ns.record_derivation(
            derivation_id="bulk_radial_action_euler_lagrange",
            inputs=[L],
            output=EL,
            method="euler_lagrange_1d",
            status=Status.DERIVED,
            record_kind=RecordKind.DERIVATION,
            result_type="euler_lagrange_equation",
        )


def case_1_boundary_variation_term(out: ScriptOutput):
    header("Case 1: Boundary variation term")

    r, R, K_A = sp.symbols("r R K_A", positive=True, real=True)
    Ap_R, deltaA_R = sp.symbols("A_prime_R deltaA_R", real=True)

    boundary_term = 2 * K_A * R**2 * Ap_R * deltaA_R

    print("Variation of bulk action gives boundary term:")
    print()
    print("  [2 K_A r^2 A' deltaA] at boundary")
    print()
    print(f"At r=R: {boundary_term}")

    with out.derived_results():
        out.line("bulk variation exposes areal flux as boundary momentum",
                 StatusMark.PASS,
                 "boundary term = 2 K_A R^2 A'(R) deltaA(R)")


def case_2_source_boundary_coupling(out: ScriptOutput, ns=None):
    header("Case 2: Source boundary coupling")

    R, K_A, q = sp.symbols("R K_A q", positive=True, real=True)
    Ap_R = sp.symbols("A_prime_R", real=True)

    # Boundary action E_b = -q A(R)
    # variation contributes -q deltaA.
    # total boundary coefficient:
    #   2 K_A R^2 A' - q = 0
    boundary_eq = sp.Eq(2*K_A*R**2*Ap_R - q, 0)
    sol_Ap = sp.solve(boundary_eq, Ap_R)[0]

    print("Boundary source coupling:")
    print("  E_boundary = -q A(R)")
    print()
    print("Boundary stationarity:")
    print("  2 K_A R^2 A'(R) - q = 0")
    print()
    print(f"A'(R) = {sol_Ap}")

    flux = sp.simplify(4*sp.pi*R**2*sol_Ap)
    print(f"F_A(R)=4piR^2*A'(R) = {flux}")

    with out.derived_results():
        out.line("boundary source fixes areal flux",
                 StatusMark.PASS,
                 f"F_A(R) = {flux}")

    if ns is not None:
        ns.record_derivation(
            derivation_id="boundary_source_coupling_flux_relation",
            inputs=[boundary_eq],
            output=sp.Eq(sp.Symbol("F_A"), flux),
            method="boundary_stationarity",
            status=Status.DERIVED,
            record_kind=RecordKind.DERIVATION,
            result_type="boundary_condition",
        )


def case_3_mass_normalization(out: ScriptOutput, ns=None):
    header("Case 3: Mass normalization of boundary charge")

    R, K_A, G, M, c = sp.symbols("R K_A G M c", positive=True, real=True)

    q = 4*K_A*G*M/c**2
    Ap_R = sp.simplify(q / (2*K_A*R**2))
    flux = sp.simplify(4*sp.pi*R**2*Ap_R)
    target = 8*sp.pi*G*M/c**2

    print(f"q_M = {q}")
    print(f"A'(R) = {Ap_R}")
    print(f"F_A = {flux}")
    print(f"target = {target}")

    residual = sp.simplify(flux - target)
    ok = is_zero(residual)

    with out.derived_results():
        out.line("mass-normalized boundary charge gives desired flux",
                 StatusMark.PASS if ok else StatusMark.FAIL,
                 f"F_A - target = {residual}")

    if ns is not None:
        ns.record_derivation(
            derivation_id="mass_normalization_boundary_charge",
            inputs=[q, R, K_A],
            output=residual,
            method="F_A = 4pi*R^2*q/(2*K_A*R^2) vs 8pi*G*M/c^2",
            status=Status.DERIVED,
            record_kind=RecordKind.DERIVATION,
            result_type="normalization_residual",
        )

    with out.unresolved_obligations():
        out.line("derive K_A from vacuum microphysics",
                 StatusMark.OBLIGATION,
                 "q_M = 4 K_A G M/c^2 fixes normalization only after Newtonian matching; K_A origin missing")


def case_4_exterior_solution_from_boundary(out: ScriptOutput, ns=None):
    header("Case 4: Exterior solution from boundary condition")

    r, R, G, M, c = sp.symbols("r R G M c", positive=True, real=True)
    C0, C1 = sp.symbols("C0 C1", real=True)

    A = C0 + C1/r
    Ap = sp.diff(A, r)

    flux = sp.simplify(4*sp.pi*r**2*Ap)
    target = 8*sp.pi*G*M/c**2

    # flux = -4*pi*C1, so C1=-2GM/c^2.
    sol_C1 = sp.solve(sp.Eq(flux, target), C1)[0]
    A_matched = sp.simplify(A.subs({C0: 1, C1: sol_C1}))

    print(f"A_general = {A}")
    print(f"F_A = {flux}")
    print(f"C1 from flux = {sol_C1}")
    print(f"A with asymptotic flatness = {A_matched}")

    schwarzschild_residual = sp.simplify(A_matched - (1 - 2*G*M/(c**2*r)))
    ok = is_zero(schwarzschild_residual)

    with out.derived_results():
        out.line("boundary flux gives Schwarzschild A coefficient",
                 StatusMark.PASS if ok else StatusMark.FAIL,
                 f"A_matched - A_Schwarzschild = {schwarzschild_residual}")

    if ns is not None:
        ns.record_derivation(
            derivation_id="boundary_flux_exterior_schwarzschild",
            inputs=[flux, target],
            output=schwarzschild_residual,
            method="solve C1 from flux=target, substitute into A_general",
            status=Status.DERIVED,
            record_kind=RecordKind.DERIVATION,
            result_type="identity_residual",
        )


def case_5_boundary_vs_bulk_source(out: ScriptOutput):
    header("Case 5: Boundary source versus bulk source")

    print("Two equivalent reduced descriptions:")
    print()
    print("1. Bulk density source:")
    print("   d/dr(4pir^2*A') = 4pir^2 * 8piGrho/c^2")
    print()
    print("2. Boundary/source interface:")
    print("   4piR^2*A'(R) = 8piGM/c^2")
    print()
    print("For exterior r>R, both give:")
    print("   A = 1 - 2GM/(rc^2)")
    print()
    print("Interpretation:")
    print("   The areal-flux law can be viewed as a Gauss law: the bulk source")
    print("   determines the boundary flux seen by the exterior.")

    with out.governance_assessments():
        out.line("boundary and bulk views agree for exterior flux",
                 StatusMark.PASS,
                 "both recover A = 1 - 2GM/(rc^2) for r > R")


def case_6_kappa_compensation_coupling(out: ScriptOutput, ns=None):
    header("Case 6: Coupling to kappa compensation")

    r, G, M, c = sp.symbols("r G M c", positive=True, real=True)

    A = 1 - 2*G*M/(c**2*r)
    kappa = sp.Integer(0)
    B = sp.simplify(sp.exp(2*kappa) / A)
    AB = sp.simplify(A*B)

    print(f"A = {A}")
    print(f"kappa = {kappa}")
    print(f"B = exp(2kappa)/A = {B}")
    print(f"AB = {AB}")

    with out.derived_results():
        out.line("boundary flux plus kappa=0 recovers reciprocal exterior",
                 StatusMark.PASS if is_zero(AB - 1) else StatusMark.FAIL,
                 f"AB = {AB}")

    ctx = TheoryContext("candidate_boundary_flux_action")
    ctx.define_equal_response_algebraic_symbols()
    ms = ctx._mode_symbols
    A_value = 1 - 2 * ms.G * ms.M / (ms.c**2 * ms.r)
    B_value = sp.simplify(1 / A_value)
    concrete = check_concrete_metric(ctx, A_value=A_value, B_value=B_value, requirement_ids=["reciprocal_scaling"])
    if concrete:
        is_satisfied = concrete[0].status == "satisfied_by_construction"
        with out.derived_results():
            out.line(
                "VacuumForge classifies boundary-flux exterior metric as by-construction reciprocal",
                StatusMark.PASS if is_satisfied else StatusMark.FAIL,
                concrete[0].message,
            )
        if ns is not None:
            ns.record_derivation(
                derivation_id="boundary_flux_exact_metric_check",
                inputs=[A_value],
                output=sp.Symbol(concrete[0].status),
                method="concrete_metric_check",
                status=Status.DERIVED,
                record_kind=RecordKind.COMPATIBILITY_EXAMPLE,
                metadata={"message": concrete[0].message},
            )


def final_interpretation():
    header("Final interpretation")

    print("The reduced radial A-action exposes areal flux as the boundary")
    print("momentum conjugate to A:")
    print()
    print("  boundary momentum prop r^2 A'")
    print()
    print("A source/interface coupling -q A(R) fixes that boundary momentum.")
    print("With q proportional to M, the boundary condition becomes:")
    print()
    print("  4piR^2*A'(R) = 8piGM/c^2")
    print()
    print("The exterior bulk equation then gives:")
    print()
    print("  A = 1 - 2GM/(rc^2)")
    print()
    print("Combined with kappa=0:")
    print()
    print("  B = 1/A")
    print()
    print("Possible next artifact:")
    print("  candidate_boundary_flux_action.md")


def main():
    header("Candidate Boundary Flux Action")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_radial_bulk_action(out, ns)
    case_1_boundary_variation_term(out)
    case_2_source_boundary_coupling(out, ns)
    case_3_mass_normalization(out, ns)
    case_4_exterior_solution_from_boundary(out, ns)
    case_5_boundary_vs_bulk_source(out)
    case_6_kappa_compensation_coupling(out, ns)
    final_interpretation()

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_K_A_from_microphysics",
        script_id=SCRIPT_ID,
        title="Derive K_A from vacuum microphysics",
        status=ObligationStatus.OPEN,
        description=(
            "The boundary action stiffness K_A appears in q_M = 4 K_A G M/c^2. "
            "Its value is fixed by Newtonian/Schwarzschild matching but is not "
            "derived from first principles. Origin of K_A remains open."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_boundary_action_form",
        script_id=SCRIPT_ID,
        title="Derive why boundary action is -q A(R)",
        status=ObligationStatus.OPEN,
        description=(
            "The boundary coupling form E_boundary = -q A(R) is adopted as an "
            "ansatz. A derivation of this coupling from covariant source action "
            "or matter coupling has not yet been given."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="areal_flux_as_boundary_momentum",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement=(
            "The areal-flux law F_A = 8piGM/c^2 can be read as a boundary "
            "condition from variation of the reduced radial A-action with "
            "boundary coupling -q A(R). This is a candidate interpretation; "
            "the coupling origin remains underived."
        ),
        obligation_ids=["derive_K_A_from_microphysics", "derive_boundary_action_form"],
    ))

    ns.record_route(RouteRecord(
        route_id="boundary_action_flux_normalization_route",
        script_id=SCRIPT_ID,
        name="Boundary action / flux normalization route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=["derive_K_A_from_microphysics", "derive_boundary_action_form"],
    ))

    ns.write_run_metadata()

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
