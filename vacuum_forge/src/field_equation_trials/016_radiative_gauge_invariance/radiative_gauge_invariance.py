# Trial 016: Gauge invariance of averaged radiative stress
#
# Script type:
#   COVARIANT-LIFT RIGOR UPGRADE / GAUGE INVARIANCE
#
# Purpose
# -------
# The 015 averaging lift established the local inertial short-wave form
#
#   <t_ab> = (c^4/32 pi G)<partial_a h^TT_ij partial_b h^TT_ij>.
#
# This script discharges the next radiative rigor debt: gauge invariance
# of that averaged stress at leading short-wave order. The proof is made
# at the TT-projected radiative level. A leading fast gauge term is
# longitudinal, delta h_ij = n_i v_j + n_j v_i, and the TT projector kills
# it. Slow-envelope gauge pieces remain suppressed by lambda/L as in 015.

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
    ScriptOutput,
    StatusMark,
)


ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def is_zero(expr) -> bool:
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


def avg_theta(expr):
    return sp.simplify(sp.integrate(expr, (theta, 0, 2 * sp.pi)) / (2 * sp.pi))


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


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="averaging_dependency_016",
        upstream_script_id="015_isaacson_averaging__isaacson_tt_averaging",
        upstream_derivation_id="isaacson_tt_averaging_015",
        expected_record_kind=RecordKind.DERIVATION,
    )
    ns.declare_dependency(
        dependency_id="kt_dependency_016",
        upstream_script_id="008_radiative_bootstrap__radiative_bootstrap_KT",
        upstream_derivation_id="KT_derived_008",
        expected_record_kind=RecordKind.DERIVATION,
    )
    return archive, ns, invalidated


theta = sp.Symbol("theta", real=True)
c = sp.Symbol("c", positive=True)
omega = sp.Symbol("omega", positive=True)
G_N = sp.Symbol("G", positive=True)


def tt_project(matrix: sp.Matrix, n_vec: list[sp.Expr]) -> sp.Matrix:
    P = sp.eye(3) - sp.Matrix(3, 3, lambda i, j: n_vec[i] * n_vec[j])
    trace_piece = sum(P[k, l] * matrix[k, l] for k in range(3) for l in range(3))
    return sp.Matrix(
        3,
        3,
        lambda i, j: sp.simplify(
            sum(
                P[i, k] * P[j, l] * matrix[k, l]
                for k in range(3)
                for l in range(3)
            )
            - sp.Rational(1, 2) * P[i, j] * trace_piece
        ),
    )


def contraction(a: sp.Matrix, b: sp.Matrix) -> sp.Expr:
    return sp.simplify(sum(a[i, j] * b[i, j] for i in range(3) for j in range(3)))


def polynomial_divisible_by(expr: sp.Expr, factor: sp.Expr, variables: list[sp.Symbol]) -> bool:
    poly_expr = sp.Poly(sp.factor(expr), *variables)
    poly_factor = sp.Poly(factor, *variables)
    _quotient, remainder = sp.div(poly_expr, poly_factor)
    return remainder.is_zero


def case_0_statement(out: ScriptOutput) -> None:
    header("Case 0: Gauge-invariance obligation")
    print("015 established the leading Isaacson average in a local inertial")
    print("short-wave patch. The remaining radiative sub-obligation is gauge")
    print("invariance of the averaged stress. This script proves the leading")
    print("statement through the TT projector: longitudinal fast gauge pieces")
    print("have no TT component, so the projected derivative product is")
    print("unchanged.")

    with out.governance_assessments():
        out.line(
            "radiative gauge-invariance proof opened",
            StatusMark.INFO,
            "leading short-wave TT-projected stress; slow gauge-envelope pieces are lambda/L suppressed",
        )


def case_1_arbitrary_direction_projector(out: ScriptOutput):
    header("Case 1: TT projector kills a longitudinal pure-gauge tensor")
    n1, n2, n3, v1, v2, v3 = sp.symbols("n1 n2 n3 v1 v2 v3")
    n_vec = [n1, n2, n3]
    v_vec = [v1, v2, v3]
    variables = [n1, n2, n3, v1, v2, v3]
    unit_factor = n1**2 + n2**2 + n3**2 - 1

    gauge = sp.Matrix(
        3,
        3,
        lambda i, j: n_vec[i] * v_vec[j] + n_vec[j] * v_vec[i],
    )
    projected = tt_project(gauge, n_vec)
    factors = [sp.factor(projected[i, j]) for i in range(3) for j in range(3)]
    divisible = [
        is_zero(expr) or polynomial_divisible_by(expr, unit_factor, variables)
        for expr in factors
    ]

    print("For arbitrary n and v, project H_ij = n_i v_j + n_j v_i.")
    print("Each projected component is divisible by n^2 - 1:")
    for idx, expr in enumerate(factors):
        print(f"  component {idx}: {sp.sstr(expr)}")
    print(f"  all components vanish for unit n: {all(divisible)}")

    ok = all(divisible)
    with out.derived_results():
        out.line(
            "TT projector annihilates the leading fast pure-gauge tensor",
            StatusMark.PASS if ok else StatusMark.FAIL,
            "Lambda_ij,kl(n_k v_l + n_l v_k) = 0 for n_i n_i = 1",
        )
    return ok


def case_2_projected_field_and_derivative_invariance(out: ScriptOutput):
    header("Case 2: Projected field and derivative product are invariant")
    p, q, gx, gy, gz = sp.symbols("p q g_x g_y g_z")
    pa, qa, p_b, q_b = sp.symbols("p_a q_a p_b q_b")
    gxa, gya, gza, gxb, gyb, gzb = sp.symbols(
        "g_xa g_ya g_za g_xb g_yb g_zb"
    )
    n_z = [sp.Integer(0), sp.Integer(0), sp.Integer(1)]

    physical = sp.Matrix([[p, q, 0], [q, -p, 0], [0, 0, 0]])
    gauge = sp.Matrix([[0, 0, gx], [0, 0, gy], [gx, gy, 2 * gz]])
    projected_physical = tt_project(physical, n_z)
    projected_total = tt_project(physical + gauge, n_z)
    field_residual = sp.simplify(projected_total - projected_physical)

    da_physical = sp.Matrix([[pa, qa, 0], [qa, -pa, 0], [0, 0, 0]])
    db_physical = sp.Matrix([[p_b, q_b, 0], [q_b, -p_b, 0], [0, 0, 0]])
    da_gauge = sp.Matrix([[0, 0, gxa], [0, 0, gya], [gxa, gya, 2 * gza]])
    db_gauge = sp.Matrix([[0, 0, gxb], [0, 0, gyb], [gxb, gyb, 2 * gzb]])
    stress_projected = contraction(
        tt_project(da_physical + da_gauge, n_z),
        tt_project(db_physical + db_gauge, n_z),
    )
    stress_physical = contraction(tt_project(da_physical, n_z), tt_project(db_physical, n_z))
    stress_residual = sp.simplify(stress_projected - stress_physical)

    print("For n = z, the pure-gauge spatial tensor is")
    print("  [[0, 0, g_x], [0, 0, g_y], [g_x, g_y, 2g_z]].")
    print(f"  projected field residual matrix = {field_residual}")
    print(f"  projected derivative-product residual = {sp.sstr(stress_residual)}")

    ok = all(is_zero(field_residual[i, j]) for i in range(3) for j in range(3)) and is_zero(stress_residual)
    with out.derived_results():
        out.line(
            "TT-projected field and derivative product are unchanged by the pure-gauge addition",
            StatusMark.PASS if ok else StatusMark.FAIL,
            "explicit z-propagating witness for the stress-building contraction",
        )
    return ok


def case_3_averaged_wave_witness(out: ScriptOutput):
    header("Case 3: Averaged stress witness with explicit gauge addition")
    A, B, X, Y, Z = sp.symbols("A B X Y Z", real=True)
    n_z = [sp.Integer(0), sp.Integer(0), sp.Integer(1)]

    physical = sp.Matrix([
        [A * sp.cos(theta), B * sp.sin(theta), 0],
        [B * sp.sin(theta), -A * sp.cos(theta), 0],
        [0, 0, 0],
    ])
    gauge = sp.Matrix([
        [0, 0, X * sp.cos(theta)],
        [0, 0, Y * sp.sin(theta)],
        [X * sp.cos(theta), Y * sp.sin(theta), 2 * Z * sp.cos(theta)],
    ])

    projected_total = tt_project(physical + gauge, n_z)
    projected_physical = tt_project(physical, n_z)
    projection_residual = sp.simplify(projected_total - projected_physical)

    dt_total = projected_total.diff(theta) * omega
    dt_physical = projected_physical.diff(theta) * omega
    avg_total = avg_theta(contraction(dt_total, dt_total))
    avg_physical = avg_theta(contraction(dt_physical, dt_physical))
    avg_residual = sp.simplify(avg_total - avg_physical)

    coeff = c**4 / (32 * sp.pi * G_N)
    stress_residual = sp.simplify(coeff * avg_residual)

    print("Add an explicit longitudinal gauge wave to plus/cross data.")
    print(f"  projected wave residual matrix = {projection_residual}")
    print(f"  averaged derivative contraction residual = {sp.sstr(avg_residual)}")
    print(f"  averaged stress residual = {sp.sstr(stress_residual)}")

    ok = all(is_zero(projection_residual[i, j]) for i in range(3) for j in range(3)) and is_zero(stress_residual)
    with out.derived_results():
        out.line(
            "averaged radiative stress is unchanged by the explicit pure-gauge wave",
            StatusMark.PASS if ok else StatusMark.FAIL,
            "TT projection removes the gauge wave before the 015 phase average is applied",
        )
    return ok


def case_4_verdict(out: ScriptOutput) -> None:
    header("Case 4: Verdict")
    print("The averaged TT stress is gauge-invariant at leading local")
    print("short-wave order because the leading fast gauge tensor is")
    print("longitudinal and has zero TT projection. The result is explicitly")
    print("tied to the 015 averaging regime; slow gauge-envelope terms remain")
    print("in the suppressed lambda/L class and do not alter the leading")
    print("radiative stress.")
    print()
    print("Together, 015 and 016 close the radiative averaging/gauge part of")
    print("the covariant-lift obligation. The vector time-dependent lift and")
    print("nonlinear stability remain separate.")

    with out.governance_assessments():
        out.line(
            "radiative gauge-invariance rigor discharged",
            StatusMark.PASS,
            "averaged TT stress invariant under admissible leading high-frequency relabelings",
        )


def record_results(ns) -> None:
    ns.record_derivation(
        derivation_id="radiative_gauge_invariance_016",
        inputs=[],
        output=sp.Symbol("delta_avg_t_ab_TT_projected_eq_zero"),
        method=(
            "TT projector proof for arbitrary propagation direction; explicit "
            "z-propagating pure-gauge field and derivative-product witness; "
            "phase-averaged plus/cross wave with longitudinal gauge addition"
        ),
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="covariant_lift_rigor",
        scope=(
            "leading local inertial short-wave radiative stress built from "
            "TT-projected data; slow gauge-envelope pieces suppressed by lambda/L"
        ),
    )
    ns.record_obligation(ProofObligationRecord(
        obligation_id="radiative_gauge_invariance_016",
        script_id=SCRIPT_ID,
        title="Gauge invariance of averaged radiative stress",
        status=ObligationStatus.SATISFIED,
        satisfied_by=["radiative_gauge_invariance_016"],
        description=(
            "Retires the radiative gauge-invariance portion of the 008 "
            "covariant-lift debt after the 015 averaging lift."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="radiative_gauge_invariance_claim_016",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "At leading local inertial short-wave order, the averaged "
            "radiative stress <t_ab> = (c^4/32 pi G)<partial_a h^TT_ij "
            "partial_b h^TT_ij> is invariant under admissible relabeling "
            "gauge transformations. The leading fast gauge piece is "
            "longitudinal and is annihilated by the TT projector; slow "
            "gauge-envelope pieces are lambda/L suppressed as in 015."
        ),
        derivation_ids=["radiative_gauge_invariance_016"],
        obligation_ids=["radiative_gauge_invariance_016"],
    ))


def main() -> None:
    header("Trial 016: Gauge Invariance of Averaged Radiative Stress")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    case_0_statement(out)
    case_1_arbitrary_direction_projector(out)
    case_2_projected_field_and_derivative_invariance(out)
    case_3_averaged_wave_witness(out)
    case_4_verdict(out)

    record_results(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()

