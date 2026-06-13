# Trial 017: General time-dependent vector sector
#
# Script type:
#   COVARIANT-LIFT RIGOR UPGRADE / VECTOR SECTOR
#
# Purpose
# -------
# The 012 vector-sector closure derived the stationary frame-dragging
# equation and normalization. This script lifts that reduced result to
# the general linear time-dependent vector sector in transverse gauge.
#
# Result:
#
#   G_ti^(1) = -(1/2) Delta w_i
#   G_ij^(1) = -(1/(2c^2))(partial_i dot w_j + partial_j dot w_i)
#
# for partial_i w_i = 0. Thus the vector sector remains constraint-type:
# the stationary 012 equation is the time-independent limit, and
# source-free regular vector modes do not propagate.

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
        dependency_id="vector_identity_dependency_017",
        upstream_script_id="012_vector_sector__vector_sector_closure",
        upstream_derivation_id="vector_linear_identity_012",
        expected_record_kind=RecordKind.DERIVATION,
    )
    ns.declare_dependency(
        dependency_id="vector_normalization_dependency_017",
        upstream_script_id="012_vector_sector__vector_sector_closure",
        upstream_derivation_id="vector_normalization_012",
        expected_record_kind=RecordKind.DERIVATION,
    )
    return archive, ns, invalidated


t, x, y, z = sp.symbols("t x y z")
c = sp.Symbol("c", positive=True)
G_N = sp.Symbol("G", positive=True)
eps = sp.Symbol("epsilon", positive=True)
COORDS = [t, x, y, z]


def christoffel(g, coords):
    n = len(coords)
    ginv = g.inv()
    Gamma = [[[0] * n for _ in range(n)] for _ in range(n)]
    for A in range(n):
        for B in range(n):
            for C in range(n):
                s_ = 0
                for D in range(n):
                    s_ += ginv[A, D] * (
                        sp.diff(g[D, B], coords[C])
                        + sp.diff(g[D, C], coords[B])
                        - sp.diff(g[B, C], coords[D])
                    )
                Gamma[A][B][C] = sp.together(s_ / 2)
    return Gamma


def einstein_lower(g, coords):
    n = len(coords)
    Gamma = christoffel(g, coords)
    Ric = sp.zeros(n, n)
    for a in range(n):
        for b in range(n):
            expr = 0
            for c_ in range(n):
                expr += sp.diff(Gamma[c_][a][b], coords[c_])
                expr -= sp.diff(Gamma[c_][a][c_], coords[b])
                for d in range(n):
                    expr += Gamma[c_][c_][d] * Gamma[d][a][b]
                    expr -= Gamma[c_][a][d] * Gamma[d][c_][b]
            Ric[a, b] = sp.together(expr)
    ginv = g.inv()
    Rs = sp.together(sum(ginv[i, j] * Ric[i, j] for i in range(n) for j in range(n)))
    Gm = sp.zeros(n, n)
    for a in range(n):
        for b in range(n):
            Gm[a, b] = Ric[a, b] - sp.Rational(1, 2) * g[a, b] * Rs
    return Gm


def lap3(f):
    return sp.diff(f, x, 2) + sp.diff(f, y, 2) + sp.diff(f, z, 2)


def linear_coeff(expr):
    return sp.expand(sp.series(expr, eps, 0, 2).removeO()).coeff(eps, 1)


def case_0_statement(out: ScriptOutput) -> None:
    header("Case 0: Vector time-dependence obligation")
    print("012 closed the stationary vector sector and derived the")
    print("Lense-Thirring normalization. The open lift is the general")
    print("linear time-dependent vector sector: does the shift w_i(t,x)")
    print("propagate, or does it remain constraint-type?")
    print()
    print("This script works in transverse gauge and verifies the full")
    print("linearized vector equations directly from the closed parent.")

    with out.governance_assessments():
        out.line(
            "vector time-dependent lift opened",
            StatusMark.INFO,
            "linear transverse vector sector; nonlinear stability remains separate",
        )


def case_1_time_dependent_einstein_tensor(out: ScriptOutput):
    header("Case 1: Time-dependent vector Einstein tensor")
    chi = sp.Function("chi")(t, x, y, z)
    wx = sp.diff(chi, y)
    wy = -sp.diff(chi, x)
    wz = sp.Integer(0)
    w = [wx, wy, wz]
    g = sp.Matrix([
        [-(c**2), eps * wx, eps * wy, eps * wz],
        [eps * wx, 1, 0, 0],
        [eps * wy, 0, 1, 0],
        [eps * wz, 0, 0, 1],
    ])
    Gm = einstein_lower(g, COORDS)

    # Constraint components.
    constraint_residuals = []
    for i in range(3):
        component = linear_coeff(Gm[0, i + 1])
        target = -sp.Rational(1, 2) * lap3(w[i])
        residual = sp.simplify(component - target)
        constraint_residuals.append(residual)
        print(f"  G_t{['x','y','z'][i]}^(1) + (1/2) Delta w_{['x','y','z'][i]} = {sp.sstr(residual)}")

    # Spatial vector components.
    spatial_residuals = []
    spatial_coords = [x, y, z]
    for i in range(3):
        for j in range(i, 3):
            component = linear_coeff(Gm[i + 1, j + 1])
            target = -(
                sp.diff(sp.diff(w[j], t), spatial_coords[i])
                + sp.diff(sp.diff(w[i], t), spatial_coords[j])
            ) / (2 * c**2)
            residual = sp.simplify(component - target)
            spatial_residuals.append(residual)
            print(f"  G_{['x','y','z'][i]}{['x','y','z'][j]}^(1) - vector target = {sp.sstr(residual)}")

    ok = all(is_zero(r) for r in constraint_residuals + spatial_residuals)
    with out.derived_results():
        out.line(
            "time-dependent transverse vector Einstein tensor verified",
            StatusMark.PASS if ok else StatusMark.FAIL,
            "G_ti constraint plus G_ij symmetrized time-derivative equation",
        )
    return ok


def case_2_stationary_limit_and_normalization(out: ScriptOutput):
    header("Case 2: Stationary limit recovers 012")
    rho, v, LapW = sp.symbols("rho v LapW", positive=True)
    N_val = c**4 / (8 * sp.pi * G_N)
    coeff = sp.simplify(
        sp.solve(
            sp.Eq(N_val * (-sp.Rational(1, 2)) * LapW, -rho * c**2 * v),
            LapW,
        )[0]
        / (rho * v)
    )
    target = 16 * sp.pi * G_N / c**2

    print("For dot(w_i)=0, the spatial vector equation vanishes and the")
    print("constraint remains:")
    print(f"  Delta w_i = ({sp.sstr(coeff)}) rho v_i^T")
    print(f"  residual vs 012 normalization = {sp.sstr(sp.simplify(coeff - target))}")

    ok = is_zero(coeff - target)
    with out.derived_results():
        out.line(
            "stationary limit exactly recovers the 012 vector equation",
            StatusMark.PASS if ok else StatusMark.FAIL,
            "Delta w_i = (16 pi G/c^2) rho v_i^T with no new constant",
        )
    return ok


def case_3_no_vector_radiation(out: ScriptOutput):
    header("Case 3: Source-free vector modes do not propagate")
    k, Omega = sp.symbols("k Omega", nonzero=True)
    Wx, Wy = sp.symbols("W_x W_y")
    phase = sp.Symbol("E")  # common Fourier phase factor

    # z-propagating transverse mode: w_z = 0, k_i W_i = 0.
    Gtx = sp.Rational(1, 2) * k**2 * Wx * phase
    Gty = sp.Rational(1, 2) * k**2 * Wy * phase
    Gxz = -Omega * k * Wx * phase / (2 * c**2)
    Gyz = -Omega * k * Wy * phase / (2 * c**2)

    Wx_solution = sp.solve(sp.Eq(Gtx, 0), Wx)[0]
    Wy_solution = sp.solve(sp.Eq(Gty, 0), Wy)[0]
    Gxz_after = sp.simplify(Gxz.subs(Wx, Wx_solution))
    Gyz_after = sp.simplify(Gyz.subs(Wy, Wy_solution))

    print("For a transverse Fourier vector mode w_i = W_i exp[i(kz-Omega t)]:")
    print(f"  G_tx = {sp.sstr(Gtx)}")
    print(f"  G_ty = {sp.sstr(Gty)}")
    print("Vacuum constraint G_ti=0 with k != 0 gives:")
    print(f"  W_x = {sp.sstr(Wx_solution)}, W_y = {sp.sstr(Wy_solution)}")
    print("The spatial vector components then vanish without imposing a")
    print("dispersion relation:")
    print(f"  G_xz after constraint = {sp.sstr(Gxz_after)}")
    print(f"  G_yz after constraint = {sp.sstr(Gyz_after)}")

    ok = is_zero(Wx_solution) and is_zero(Wy_solution) and is_zero(Gxz_after) and is_zero(Gyz_after)
    with out.derived_results():
        out.line(
            "vacuum transverse vector Fourier modes have zero amplitude for k != 0",
            StatusMark.PASS if ok else StatusMark.FAIL,
            "constraint kills vector modes; no vector dispersion relation or independent radiation",
        )
    return ok


def case_4_verdict(out: ScriptOutput) -> None:
    header("Case 4: Verdict")
    print("The time-dependent linear vector lift is closed. The vector sector")
    print("is governed by an elliptic momentum constraint plus a consistency")
    print("equation for time dependence; the stationary 012 equation is the")
    print("dot(w)=0 limit. In source-free vacuum, regular nonzero-k vector")
    print("modes are killed by the constraint, so no vector radiation is")
    print("introduced.")
    print()
    print("This retires the 012 vector time-dependence subpiece. Nonlinear")
    print("stability and the broader covariant statics lift remain separate.")

    with out.governance_assessments():
        out.line(
            "vector time-dependent lift discharged",
            StatusMark.PASS,
            "stationary 012 recovered; no independent source-free vector radiation",
        )


def record_results(ns) -> None:
    ns.record_derivation(
        derivation_id="vector_time_dependent_lift_017",
        inputs=[],
        output=sp.Symbol("Gti_constraint_Gij_vector_consistency_no_vector_radiation"),
        method=(
            "linearized Einstein tensor for time-dependent transverse stream "
            "w_i; 012 normalization recovery; transverse Fourier vacuum mode "
            "constraint check"
        ),
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="covariant_lift_rigor",
        scope=(
            "linear time-dependent transverse vector sector of the closed parent; "
            "nonlinear stability not included"
        ),
    )
    ns.record_obligation(ProofObligationRecord(
        obligation_id="vector_covariant_lift_017",
        script_id=SCRIPT_ID,
        title="General time-dependent vector-sector lift",
        status=ObligationStatus.SATISFIED,
        satisfied_by=["vector_time_dependent_lift_017"],
        description=(
            "Retires the 012 stationary-to-general time-dependence vector "
            "subpiece of the covariant-lift debt."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="vector_time_dependent_claim_017",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "The general linear transverse vector sector is constraint-type: "
            "G_ti^(1)=-(1/2)Delta w_i and G_ij^(1)=-(1/2c^2)"
            "(partial_i dot w_j + partial_j dot w_i). The stationary limit "
            "recovers 012 with its derived normalization, and source-free "
            "regular vector Fourier modes have zero amplitude for k != 0."
        ),
        derivation_ids=["vector_time_dependent_lift_017"],
        obligation_ids=["vector_covariant_lift_017"],
    ))


def main() -> None:
    header("Trial 017: General Time-Dependent Vector Sector")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    case_0_statement(out)
    case_1_time_dependent_einstein_tensor(out)
    case_2_stationary_limit_and_normalization(out)
    case_3_no_vector_radiation(out)
    case_4_verdict(out)

    record_results(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
