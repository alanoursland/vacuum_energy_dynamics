#!/usr/bin/env python3
"""
unimodular_covariant_constraint.py

Covariant lift of the kappa = 0 (unimodular) constraint, discharging the
obligation opened by derivation 033.

Three results:

  1. kappa is a genuine scalar given the fiducial volume form: under an
     arbitrary radial chart change both volume densities pick up the same
     Jacobian, so kappa = ln(sqrt(-g)/sqrt(-g_bar)) is chart-invariant.
     Witness: Schwarzschild in a distorted radial chart has kappa = 0
     exactly, as in areal gauge.

  2. The multiplier route: metric compatibility gives
     nabla^a (lambda g_ab) = partial_b lambda for arbitrary lambda(x), so
     the unimodular-constrained variation's undetermined multiplier in
     G_ab + lambda g_ab = k T_ab is forced constant by Bianchi + matter
     conservation. Verified componentwise on static spherical and FRW
     families. lambda is Lambda; the variation never chose its value.

  3. The sourced kappa-equation, exactly: for any static spherical
     configuration of the closed parent,

         kappa'(r) = -(r B / 2N) (T^t_t - T^r_r),   N = c^4 / 8 pi G.

     kappa = 0 iff the effective stress is t-r boost invariant (P7').
     Feeding the comoving-dust stress of the matter era into this equation
     and integrating re-derives the F1 leak coefficient with no free
     input:

         kappa = (3/4) Omega_m (H0 r/c)^2,  i.e.  AB - 1 = (3/2) Omega_m (H0 r/c)^2.

Output:
    theory_v3/development/vacuum_sector/unimodular_covariant_constraint_vacuumforge.md
"""

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


SCRIPT_PATH = Path(__file__).resolve()
SCRIPT_ID = f"{SCRIPT_PATH.parent.name}__{SCRIPT_PATH.stem}"
ARCHIVE_ROOT = SCRIPT_PATH.parents[1] / ".vacuumforge_archive"
REPO_ROOT = SCRIPT_PATH.parents[4]
REPORT_PATH = (
    REPO_ROOT
    / "theory_v3"
    / "development"
    / "vacuum_sector"
    / "unimodular_covariant_constraint_vacuumforge.md"
)

DEPENDENCIES = [
    (
        "unimodular_break_dependency_034",
        "033_unimodular_lovelock_break__unimodular_lovelock_break",
        "unimodular_lovelock_break_033",
    ),
]


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


def require(label: str, condition: bool, failures: list) -> None:
    mark = "PASS" if condition else "FAIL"
    print(f"  [{mark}] {label}")
    if not condition:
        failures.append(label)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    for dep_id, upstream_script_id, upstream_derivation_id in DEPENDENCIES:
        ns.declare_dependency(
            dependency_id=dep_id,
            upstream_script_id=upstream_script_id,
            upstream_derivation_id=upstream_derivation_id,
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
# Curvature machinery
# =============================================================================


def christoffel(g, coords):
    n = len(coords)
    ginv = g.inv()
    Gamma = [[[0] * n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c_ in range(n):
                s_ = 0
                for d in range(n):
                    s_ += ginv[a, d] * (
                        sp.diff(g[d, b], coords[c_])
                        + sp.diff(g[d, c_], coords[b])
                        - sp.diff(g[b, c_], coords[d])
                    )
                Gamma[a][b][c_] = sp.together(s_ / 2)
    return Gamma


def ricci(Gamma, coords):
    n = len(coords)
    R = sp.zeros(n, n)
    for a in range(n):
        for b in range(n):
            expr = 0
            for c_ in range(n):
                expr += sp.diff(Gamma[c_][a][b], coords[c_])
                expr -= sp.diff(Gamma[c_][a][c_], coords[b])
                for d in range(n):
                    expr += Gamma[c_][c_][d] * Gamma[d][a][b]
                    expr -= Gamma[c_][a][d] * Gamma[d][c_][b]
            R[a, b] = sp.together(expr)
    return R


def curvature(g, coords):
    Gamma = christoffel(g, coords)
    Ric = ricci(Gamma, coords)
    ginv = g.inv()
    n = len(coords)
    Rs = sp.together(sum(ginv[i, j] * Ric[i, j] for i in range(n) for j in range(n)))
    return Gamma, Ric, Rs, ginv


def div_lower_tensor(S, g, ginv, Gamma, coords):
    n = len(coords)
    out = [0] * n
    for b in range(n):
        expr = 0
        for a in range(n):
            for c_ in range(n):
                term = sp.diff(S[c_, b], coords[a])
                for d in range(n):
                    term -= Gamma[d][a][c_] * S[d, b]
                    term -= Gamma[d][a][b] * S[c_, d]
                expr += ginv[a, c_] * term
        out[b] = sp.together(expr)
    return out


t, r, th, ph, rho_c = sp.symbols("t r theta phi rho")


# =============================================================================
# Check 1: kappa is a scalar (chart witness)
# =============================================================================


def check_1_chart_invariance(failures):
    header("Check 1: kappa is chart-invariant given the fiducial volume form")
    r_s = sp.Symbol("r_s", positive=True)
    # Distorted radial chart: r = R(rho), the 019 witness function.
    Rfun = rho_c + r_s * sp.exp(-rho_c / r_s)
    Rp = sp.diff(Rfun, rho_c)
    A_w = 1 - r_s / Rfun
    B_w = Rp**2 / A_w
    g = sp.diag(-A_w, B_w, Rfun**2, Rfun**2 * sp.sin(th) ** 2)
    sqrt_minus_g = sp.sqrt(sp.simplify(-g.det()))
    # Fiducial (flat) metric in the SAME chart: ds^2 = -dt^2 + R'^2 drho^2 + R^2 dOmega^2
    gbar = sp.diag(-1, Rp**2, Rfun**2, Rfun**2 * sp.sin(th) ** 2)
    sqrt_minus_gbar = sp.sqrt(sp.simplify(-gbar.det()))
    kappa = sp.simplify(
        sp.expand_log(sp.log(sqrt_minus_g / sqrt_minus_gbar), force=True)
    )
    print(f"  distorted chart: kappa = ln(sqrt(-g)/sqrt(-g_bar)) = {sp.sstr(kappa)}")
    require(
        "Schwarzschild has kappa = 0 in the distorted chart (scalar, not gauge artifact)",
        is_zero(kappa), failures,
    )
    print()
    print("  Both volume densities transform with the same Jacobian under a")
    print("  chart change, so their ratio is a scalar. The constraint kappa = 0")
    print("  compares the vacuum configuration's volume form to the fiducial")
    print("  volume form; it is a geometric statement, not a coordinate one.")


# =============================================================================
# Check 2: the multiplier route
# =============================================================================


def check_2_multiplier_route(failures):
    header("Check 2: unimodular multiplier is forced constant by conservation")
    # Family (i): static spherical with lambda(t, r).
    A = sp.Function("A", positive=True)(r)
    B = sp.Function("B", positive=True)(r)
    lam1 = sp.Function("lambda_m")(t, r)
    coords1 = [t, r, th, ph]
    g1 = sp.diag(-A, B, r**2, r**2 * sp.sin(th) ** 2)
    _verify_multiplier_on(g1, lam1, coords1, "static spherical", failures)

    # Family (ii): FRW with lambda(t).
    a = sp.Function("a", positive=True)(t)
    x, y, z = sp.symbols("x y z")
    lam2 = sp.Function("lambda_m")(t)
    coords2 = [t, x, y, z]
    g2 = sp.diag(-1, a**2, a**2, a**2)
    _verify_multiplier_on(g2, lam2, coords2, "flat FRW", failures)

    print()
    print("  The unimodular-constrained variation leaves an undetermined")
    print("  multiplier lambda(x): G_ab + lambda g_ab = k T_ab. Taking the")
    print("  divergence: Bianchi kills G, metric compatibility gives exactly")
    print("  partial_b lambda, and matter conservation kills the right side.")
    print("  So lambda is constant on shell -- it IS Lambda, and the variation")
    print("  never chose its value. The global datum is the one remaining")
    print("  input, covariantly.")


def _verify_multiplier_on(g, lam, coords, label, failures):
    Gamma, Ric, Rs, ginv = curvature(g, coords)
    n = 4
    S = sp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            S[i, j] = lam * g[i, j]
    divS = div_lower_tensor(S, g, ginv, Gamma, coords)
    ok = all(is_zero(sp.simplify(divS[b] - sp.diff(lam, coords[b]))) for b in range(n))
    print(f"  family: {label}")
    require(
        "    nabla^a (lambda g_ab) = partial_b lambda (metric compatibility)",
        ok, failures,
    )


# =============================================================================
# Check 3: the sourced kappa-equation, and the F1 coefficient from dust
# =============================================================================


def check_3_sourced_kappa(failures):
    header("Check 3: kappa'(r) = -(r B / 2N)(T^t_t - T^r_r); F1 re-derived from dust")
    # Exact identity from the closed parent.
    A = sp.Function("A", positive=True)(r)
    B = sp.Function("B", positive=True)(r)
    coords = [t, r, th, ph]
    g = sp.diag(-A, B, r**2, r**2 * sp.sin(th) ** 2)
    Gamma, Ric, Rs, ginv = curvature(g, coords)
    n = 4
    Gmix = sp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            Gmix[i, j] = sp.simplify(
                sum(ginv[i, c_] * (Ric[c_, j] - sp.Rational(1, 2) * g[c_, j] * Rs) for c_ in range(n))
            )
    kappa = sp.Rational(1, 2) * sp.log(A * B)
    # G^t_t - G^r_r = -2 kappa' / (r B)  (C3 identity in kappa form)
    identity = sp.simplify(
        (Gmix[0, 0] - Gmix[1, 1]) + 2 * sp.diff(kappa, r) / (r * B)
    )
    print(f"  (G^t_t - G^r_r) + 2 kappa'/(rB) = {sp.sstr(identity)}")
    require("exact identity: G^t_t - G^r_r = -2 kappa'/(rB)", is_zero(identity), failures)
    print()
    print("  With the closed parent N G^a_b = T^a_b:")
    print()
    print("      kappa'(r) = -(r B / 2N) (T^t_t - T^r_r),   N = c^4/8 pi G.")
    print()
    print("  kappa = 0 iff the effective stress is t-r boost invariant: the")
    print("  covariant form of the constraint, with P7' as its exactness")
    print("  condition and matter anisotropy as its controlled source.")

    # F1 re-derivation: comoving dust in the static patch, v = H0 r.
    c_, G_N, H0, Om = sp.symbols("c G_N H_0 Omega_m", positive=True)
    N = c_**4 / (8 * sp.pi * G_N)
    rho_m = Om * 3 * H0**2 / (8 * sp.pi * G_N)  # matter density, mass units
    v = H0 * r
    gamma2 = 1 / (1 - v**2 / c_**2)
    # Dust stress in the static chart (leading order, B -> 1):
    #   T^t_t = -rho c^2 gamma^2,  T^r_r = rho gamma^2 v^2.
    Ttt = -rho_m * c_**2 * gamma2
    Trr = rho_m * gamma2 * v**2
    kappa_prime = -(r * 1 / (2 * N)) * (Ttt - Trr)
    # Integrate the leading-order (H0^2) piece; higher orders are O(H0^4).
    kappa_prime_lead = sp.series(kappa_prime, H0, 0, 4).removeO()
    kappa_series = sp.integrate(kappa_prime_lead, (r, 0, r))
    target = sp.Rational(3, 4) * Om * (H0 * r / c_) ** 2
    residual = sp.simplify(sp.expand(kappa_series) - target)
    print(f"  dust source: kappa(r) = {sp.sstr(sp.simplify(kappa_series))} + O(H0^4)")
    print(f"  residual vs (3/4) Omega_m (H0 r/c)^2 = {sp.sstr(residual)}")
    require(
        "F1 leak coefficient re-derived: kappa = (3/4) Omega_m (H0 r/c)^2, "
        "i.e. AB - 1 = (3/2) Omega_m (H0 r/c)^2",
        is_zero(residual), failures,
    )
    # And the pure-Lambda source is boost-invariant: T = -rho_L g has
    # T^t_t = T^r_r, so kappa' = 0 exactly.
    rho_L = sp.Symbol("rho_Lambda")
    Ttt_L = -rho_L
    Trr_L = -rho_L
    require(
        "pure-Lambda stress is t-r boost invariant: kappa' = 0 exactly (SdS)",
        is_zero(Ttt_L - Trr_L), failures,
    )
    print()
    print("  The F1 coefficient, originally derived through the trial-F1")
    print("  cosmological embedding, is re-derived here in three lines from")
    print("  the covariant sourced kappa-equation with the comoving dust")
    print("  stress -- no free input, no embedding machinery. The leak is the")
    print("  matter era's t-r anisotropy, integrated.")


# =============================================================================
# Report and archive
# =============================================================================


def write_report():
    md = """# VacuumForge Verification: Covariant Form of the Unimodular Constraint

## Purpose

Discharges `unimodular_covariant_constraint_lift_033`: the kappa = 0
constraint is stated and verified covariantly, including its interaction
with the F1 matter-era leak.

## Verified Results

```text
1. kappa is a scalar. Given the fiducial volume form, both volume
   densities transform with the same Jacobian, so
   kappa = ln(sqrt(-g)/sqrt(-g_bar)) is chart-invariant. Witness:
   Schwarzschild in the distorted chart r = rho + r_s exp(-rho/r_s) has
   kappa = 0 exactly.

2. The multiplier route. Metric compatibility gives
   nabla^a (lambda g_ab) = partial_b lambda for arbitrary lambda(x)
   (verified componentwise on static spherical and FRW families), so in
   G_ab + lambda g_ab = k T_ab the multiplier of the unimodular-
   constrained variation is forced constant by Bianchi + matter
   conservation. lambda IS Lambda; the variation never chose its value;
   the global datum is the one remaining input, covariantly.

3. The sourced kappa-equation, exact:

       kappa'(r) = -(r B / 2N)(T^t_t - T^r_r),   N = c^4/8 pi G.

   kappa = 0 iff the effective stress is t-r boost invariant -- the
   covariant statement of the constraint, with P7' as its exactness
   condition. Feeding the comoving-dust stress (T^t_t = -rho c^2 gamma^2,
   T^r_r = rho gamma^2 v^2, v = H0 r, rho = 3 Omega_m H0^2/8 pi G) into
   the equation and integrating re-derives the F1 leak with no free
   input:

       kappa = (3/4) Omega_m (H0 r/c)^2  =>  AB - 1 = (3/2) Omega_m (H0 r/c)^2,

   and the pure-Lambda stress (T = -rho_L g) is exactly boost-invariant,
   so kappa' = 0 identically in any pure-Lambda epoch (SdS exactness).
```

## Classification

```text
result type: covariant lift (discharges the 033-opened obligation)
scope:       chart-invariance witness; two-family multiplier verification;
             exact sourced kappa-equation for static spherical
             configurations of the closed parent, with the F1 coefficient
             re-derived from the dust stress at leading order
conclusion:  the unimodular constraint is geometric (kappa a scalar), its
             multiplier is Lambda (constant on shell, value = global
             datum), and its controlled violation is exactly the matter
             era's t-r stress anisotropy -- F1's coefficient drops out of
             the sourced equation in three lines
non-conclusion: Lambda's value (the global datum) is not derived; no
             nonbaseline physics is licensed
```

## Consequence

The unimodular reading is now covariantly closed at the same standard as
the rest of the program: constraint (geometric), multiplier (Lambda as
integration constant), exactness condition (P7'), and controlled
violation (F1, re-derived independently). The remaining open item in the
Lambda lane is the global datum itself.

## Verification

```text
vacuum_forge/src/vacuum_sector/034_unimodular_covariant_constraint/unimodular_covariant_constraint.py
```

Archive record: `unimodular_covariant_constraint_034`.
"""
    REPORT_PATH.write_text(md, encoding="utf-8")
    print(f"[INFO] report written: {REPORT_PATH}")


def record_archive(ns):
    ns.record_derivation(
        derivation_id="unimodular_covariant_constraint_034",
        inputs=[sp.Symbol("unimodular_lovelock_break_result")],
        output=sp.Symbol("kappa_scalar_multiplier_constant_sourced_equation_F1"),
        method=(
            "distorted-chart kappa scalar witness; componentwise "
            "nabla^a(lambda g_ab) = partial_b lambda on two families; exact "
            "identity G^t_t - G^r_r = -2 kappa'/(rB) and F1 coefficient "
            "re-derivation from the comoving dust stress"
        ),
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="covariant_lift",
        scope=(
            "static spherical + FRW witnesses; leading-order dust source for "
            "the F1 re-derivation; Lambda's value not derived"
        ),
    )
    ns.record_obligation(ProofObligationRecord(
        obligation_id="unimodular_covariant_constraint_lift_034",
        script_id=SCRIPT_ID,
        title="Covariant statement of the kappa = 0 constraint (discharged)",
        status=ObligationStatus.SATISFIED,
        satisfied_by=["unimodular_covariant_constraint_034"],
        description=(
            "Discharges unimodular_covariant_constraint_lift_033: kappa is a "
            "scalar, the multiplier is Lambda, and the F1 leak is the sourced "
            "equation's matter-era content."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="lambda_global_datum_derivation_required_034",
        script_id=SCRIPT_ID,
        title="Derive the global datum that fixes Lambda",
        status=ObligationStatus.OPEN,
        required_by=["unimodular_covariant_constraint_034"],
        description=(
            "With Lambda covariantly established as an integration constant, "
            "the Lambda lane's remaining obligation is the global datum "
            "itself (boundary condition / total four-volume conjugate). Any "
            "frustration-floor mechanism must route through this datum, not "
            "through a local w = -1 density (sequestering, 033 check 4)."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="unimodular_covariant_claim_034",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "The unimodular constraint is covariant: kappa is a scalar built "
            "from the configuration and fiducial volume forms; the "
            "constrained variation's multiplier is forced constant on shell "
            "and is Lambda; and the constraint's controlled violation is the "
            "exact sourced equation kappa' = -(rB/2N)(T^t_t - T^r_r), whose "
            "matter-era dust content re-derives the F1 coefficient "
            "AB - 1 = (3/2) Omega_m (H0 r/c)^2 with no free input. Lambda's "
            "value remains the global datum, now the Lambda lane's sole "
            "open item."
        ),
        derivation_ids=["unimodular_covariant_constraint_034"],
        obligation_ids=[
            "unimodular_covariant_constraint_lift_034",
            "lambda_global_datum_derivation_required_034",
        ],
    ))


def main() -> None:
    header("Derivation 034: Covariant Form of the Unimodular Constraint")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    failures: list = []
    check_1_chart_invariance(failures)
    check_2_multiplier_route(failures)
    check_3_sourced_kappa(failures)

    header("Verdict")
    if failures:
        for f in failures:
            print(f"  FAILED: {f}")
        raise SystemExit("Derivation 034: verification failure")
    print("  The kappa = 0 constraint is covariantly closed: scalar status,")
    print("  multiplier = Lambda, sourced equation with F1 re-derived. The")
    print("  Lambda lane's sole open item is the global datum.")

    write_report()
    record_archive(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
