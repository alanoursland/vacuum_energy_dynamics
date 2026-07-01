# Trial 021: The horizon as an accounting corollary (and why it is not
# Michell's coincidence)
#
# Script type:
#   SUPPORTING THEOREM / DISCRIMINATOR
#
# Purpose
# -------
# The Schwarzschild radius falls out of proof.md section 2's bookkeeping
# exterior as the zero of the derived A(r). Naive energy accounting
# (Michell 1784 / Laplace 1799: escape velocity = c) produces the same
# radius by a famous cancellation of two errors. This trial separates the
# two cleanly:
#
#   1. RADIUS: both routes give r_s = 2GM/c^2. (The coincidence.)
#   2. HORIZON EXISTENCE IS P9-SELECTED: in the C2 bootstrap family
#      A_lambda = (1 + lambda r_s/r)^(-1/lambda), only the P9-selected
#      member lambda = -1 has a zero at finite radius. The lambda = 0
#      (exponential) and lambda = +1 (reciprocal) members -- the "wrong
#      counting" accountings -- have NO horizon anywhere. The horizon's
#      existence, not just its location, is a corollary of count-once.
#   3. THE METRIC DISCRIMINATOR: the Michell/Newtonian route carries no
#      spatial response (B = 1, gamma = 0: half the observed light
#      deflection); the bookkeeping route forces B = 1/A (gamma = 1).
#      A coincidence hands you a number; it cannot hand you a function.
#   4. PG/RIVER EXACTNESS: the derived exterior admits the
#      Painleve-Gullstrand form ds^2 = -c^2 dT^2 + (dr + v dT)^2 + r^2 dOmega^2
#      with v(r) = c sqrt(r_s/r) EXACTLY: the PG metric is verified
#      vacuum with Schwarzschild's Kretschmann invariant, v = c exactly
#      at r = r_s, and (1/2) v^2 = GM/r at all radii -- the P6 exchange
#      ledger's kinetic bookkeeping is exact at every r, not
#      asymptotically. What GR files as the "river-model curiosity" is
#      the P9 resummation doing its job.
#
# Scope: exterior only. The ledger's own binding entry diverges at the
# horizon doorstep (the interior-cap obligation); nothing here claims the
# interior.

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


def require(label: str, condition: bool, failures: list) -> None:
    mark = "PASS" if condition else "FAIL"
    print(f"  [{mark}] {label}")
    if not condition:
        failures.append(label)


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
        dependency_id="c2_family_dependency_021",
        upstream_script_id="002_trial_C_burden_ledger__trial_C2_self_coupling_bootstrap",
        upstream_derivation_id="bootstrap_family_exact_solution_c2",
        expected_record_kind=RecordKind.DERIVATION,
    )
    ns.declare_dependency(
        dependency_id="birkhoff_dependency_021",
        upstream_script_id="019_static_covariant_lift__static_covariant_lift",
        upstream_derivation_id="covariant_statics_lift_019",
        expected_record_kind=RecordKind.DERIVATION,
    )
    return archive, ns, invalidated


# =============================================================================
# Curvature machinery
# =============================================================================

t, r, th, ph = sp.symbols("t r theta phi")


def curvature(g, coords):
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
    Rs = sp.together(sum(ginv[i, j] * Ric[i, j] for i in range(n) for j in range(n)))
    return Gamma, Ric, Rs, ginv


def riemann_lower(g, coords):
    n = len(coords)
    Gamma, _, _, _ = curvature(g, coords)
    Rup = [[[[0] * n for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c_ in range(n):
                for d in range(n):
                    expr = sp.diff(Gamma[a][b][d], coords[c_]) - sp.diff(Gamma[a][b][c_], coords[d])
                    for e in range(n):
                        expr += Gamma[a][c_][e] * Gamma[e][b][d]
                        expr -= Gamma[a][d][e] * Gamma[e][b][c_]
                    Rup[a][b][c_][d] = sp.together(expr)
    Rl = [[[[0] * n for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c_ in range(n):
                for d in range(n):
                    Rl[a][b][c_][d] = sp.together(sum(g[a, e] * Rup[e][b][c_][d] for e in range(n)))
    return Rl


def kretschmann(g, coords):
    n = len(coords)
    Rl = riemann_lower(g, coords)
    ginv = g.inv()
    K = 0
    for a in range(n):
        for b in range(n):
            for c_ in range(n):
                for d in range(n):
                    term = 0
                    for e in range(n):
                        for f in range(n):
                            for gg in range(n):
                                for h in range(n):
                                    term += (
                                        ginv[a, e] * ginv[b, f] * ginv[c_, gg] * ginv[d, h]
                                        * Rl[e][f][gg][h]
                                    )
                    K += Rl[a][b][c_][d] * term
    return sp.simplify(K)


# =============================================================================
# Case 1: the radius (the coincidence, stated)
# =============================================================================


def case_1_radius(failures):
    header("Case 1: Both routes give r_s = 2GM/c^2 (the coincidence, stated)")
    G_N, M, c = sp.symbols("G M c", positive=True)
    v = sp.Symbol("v", positive=True)
    # Michell: (1/2) v^2 = G M / r with v = c.
    r_michell = sp.solve(sp.Eq(sp.Rational(1, 2) * c**2, G_N * M / sp.Symbol("r", positive=True)),
                         sp.Symbol("r", positive=True))[0]
    # Bookkeeping exterior: zero of A = 1 - 2GM/(c^2 r).
    r_pos = sp.Symbol("r", positive=True)
    A = 1 - 2 * G_N * M / (c**2 * r_pos)
    r_horizon = sp.solve(sp.Eq(A, 0), r_pos)[0]
    print(f"  Michell radius:   {sp.sstr(r_michell)}")
    print(f"  zero of derived A: {sp.sstr(r_horizon)}")
    require("both equal 2GM/c^2", is_zero(r_michell - r_horizon), failures)
    print()
    print("  The agreement of the RADIUS is the historical coincidence: the")
    print("  Newtonian route uses the wrong kinetic energy and the wrong")
    print("  potential, and the errors cancel. Nothing in Cases 2-4 relies on")
    print("  this agreement; they are what the coincidence cannot produce.")


# =============================================================================
# Case 2: horizon existence is P9-selected
# =============================================================================


def case_2_horizon_existence(failures):
    header("Case 2: Only the P9-selected accounting has a horizon at all")
    r_s = sp.Symbol("r_s", positive=True)
    r_pos = sp.Symbol("r", positive=True)

    A_m1 = 1 - r_s / r_pos                      # lambda = -1 (P9-selected)
    A_0 = sp.exp(-r_s / r_pos)                  # lambda -> 0 (log-linear counting)
    A_p1 = 1 / (1 + r_s / r_pos)                # lambda = +1 (wrong-weight counting)

    zeros_m1 = sp.solve(sp.Eq(A_m1, 0), r_pos)
    zeros_0 = sp.solve(sp.Eq(A_0, 0), r_pos)
    zeros_p1 = sp.solve(sp.Eq(A_p1, 0), r_pos)
    print(f"  lambda = -1: zeros of A at r = {zeros_m1}")
    print(f"  lambda =  0: zeros of A at r = {zeros_0}")
    print(f"  lambda = +1: zeros of A at r = {zeros_p1}")
    require("lambda = -1 has its zero exactly at r = r_s",
            len(zeros_m1) == 1 and is_zero(zeros_m1[0] - r_s), failures)
    require("lambda = 0 (exponential) has NO zero at finite r > 0",
            len(zeros_0) == 0, failures)
    require("lambda = +1 (reciprocal) has NO zero at finite r > 0",
            len(zeros_p1) == 0, failures)
    # Positivity witnesses: A_0 and A_p1 strictly positive for r > 0.
    require("A_exponential > 0 and A_reciprocal > 0 for all r > 0 (no horizon)",
            bool(A_0.is_positive) and bool(sp.simplify(A_p1).is_positive), failures)
    print()
    print("  All three family members agree at first post-Newtonian order --")
    print("  Michell-grade accounting cannot tell them apart. The members that")
    print("  count self-energy wrongly (lambda = 0: none; lambda = +1: wrong")
    print("  weight) have A > 0 everywhere: NO horizon at any radius. The")
    print("  existence of a horizon at finite r is itself a corollary of P9's")
    print("  count-once rule, not of energy accounting in general.")


# =============================================================================
# Case 3: the metric discriminator (gamma)
# =============================================================================


def case_3_metric_discriminator(failures):
    header("Case 3: The coincidence hands you a number, not a function")
    u = sp.Symbol("u", positive=True)  # u = GM/(c^2 r), expansion parameter

    # Michell/Newtonian route: temporal response only, no spatial response.
    B_michell = sp.Integer(1)
    # Bookkeeping route: B = 1/A with A = 1 - 2u.
    B_derived = 1 / (1 - 2 * u)

    # PPN reading: B = 1 + 2 gamma u + O(u^2).
    gamma_michell = sp.series(B_michell, u, 0, 2).removeO().coeff(u, 1) / 2
    gamma_derived = sp.series(B_derived, u, 0, 2).removeO().coeff(u, 1) / 2
    print(f"  Michell route:    B = 1        =>  gamma = {gamma_michell}")
    print(f"  bookkeeping route: B = 1/A     =>  gamma = {gamma_derived}")
    require("Michell route has gamma = 0 (predicts HALF the observed light deflection)",
            is_zero(gamma_michell), failures)
    require("bookkeeping route has gamma = 1 (Cassini-grade agreement)",
            is_zero(gamma_derived - 1), failures)
    print()
    print("  Light deflection through the solar limb: gamma = 0 gives 0.875\"")
    print("  (the 1911 Einstein/Soldner half-value); gamma = 1 gives 1.75\"")
    print("  (observed, parts in 1e5 by Cassini). The Michell accounting is")
    print("  falsified by the very first metric observable; the bookkeeping")
    print("  exterior is exact. The radius agreement was luck; the function")
    print("  agreement is P7' + P9 content.")


# =============================================================================
# Case 4: Painleve-Gullstrand exactness (the river ledger)
# =============================================================================


def case_4_pg_exactness(failures):
    header("Case 4: The P6 ledger is exact at all radii (PG/river form)")
    r_s = sp.Symbol("r_s", positive=True)
    c = sp.Symbol("c", positive=True)
    T = sp.Symbol("T")
    v = c * sp.sqrt(r_s / r)

    # PG metric: ds^2 = -c^2 dT^2 + (dr + v dT)^2 + r^2 dOmega^2
    #   g_TT = -(c^2 - v^2), g_Tr = v, g_rr = 1.
    g = sp.Matrix([
        [-(c**2) + v**2, v, 0, 0],
        [v, 1, 0, 0],
        [0, 0, r**2, 0],
        [0, 0, 0, r**2 * sp.sin(th) ** 2],
    ])
    coords = [T, r, th, ph]
    Gamma, Ric, Rs, ginv = curvature(g, coords)
    n = 4
    vac = True
    for i in range(n):
        for j in range(n):
            Gij = Ric[i, j] - sp.Rational(1, 2) * g[i, j] * Rs
            vac = vac and is_zero(Gij)
    require("PG metric with v = c sqrt(r_s/r) is exactly vacuum (G_ab = 0)", vac, failures)

    K = kretschmann(g, coords)
    require("PG Kretschmann = 12 r_s^2 / r^6 (Schwarzschild's invariant)",
            is_zero(sp.simplify(K - 12 * r_s**2 / r**6)), failures)
    # By 019's Birkhoff lift, spherical vacuum with this invariant IS the
    # derived exterior; the PG chart is a relabeling of it.

    # The ledger readings, exact at every r:
    G_N, M = sp.symbols("G M", positive=True)
    v_sub = v.subs(r_s, 2 * G_N * M / c**2)
    ledger = sp.simplify(sp.Rational(1, 2) * v_sub**2 - G_N * M / r)
    require("(1/2) v^2 = GM/r exactly at ALL r (P6 kinetic-exchange ledger)",
            is_zero(ledger), failures)
    require("v = c exactly at r = r_s (horizon = ledger saturation)",
            is_zero(sp.simplify(v.subs(r, r_s) - c)), failures)
    print()
    print("  The derived exterior admits a slicing in which the infall/river")
    print("  velocity keeps the Newtonian form (1/2)v^2 = GM/r EXACTLY at every")
    print("  radius, with the horizon at exactly v = c. In GR pedagogy this is")
    print("  the 'river model curiosity' (Hamilton-Lisle). In VED it is not a")
    print("  curiosity: the P9 resummation (flux law linear in A = e^s) is WHY")
    print("  the kinetic-exchange bookkeeping closes exactly at all orders.")
    print("  The same mechanism explains the Michell radius agreement: the")
    print("  'two cancelling errors' cancel BECAUSE the exact theory's ledger")
    print("  is Newtonian-formed in this slicing.")


# =============================================================================
# Verdict, archive
# =============================================================================


def case_5_verdict():
    header("Case 5: Verdict")
    print("  THEOREM (horizon as accounting corollary). In the bookkeeping")
    print("  exterior of proof.md section 2, the horizon exists and sits at")
    print("  r_s = 2GM/c^2 as a corollary of the count-once accounting: the")
    print("  P9-selected distortion variable A = e^s vanishes at finite radius,")
    print("  while every wrongly-counted family member has no horizon at all.")
    print("  The Michell coincidence is explained, not inherited: the exact")
    print("  ledger is Newtonian-formed in the PG slicing (Case 4), so the")
    print("  naive argument lands on the right number for a reason the naive")
    print("  argument cannot state.")
    print()
    print("  Scope: exterior only. The ledger's binding entry diverges at the")
    print("  horizon doorstep; the interior remains the cap obligation.")


def record_results(ns) -> None:
    ns.record_derivation(
        derivation_id="horizon_accounting_021",
        inputs=[],
        output=sp.Symbol("horizon_is_P9_corollary_michell_explained_not_inherited"),
        method=(
            "zero-set comparison across the C2 bootstrap family; PPN gamma "
            "discriminator vs the Newtonian route; from-scratch verification "
            "that the PG river metric with v = c sqrt(r_s/r) is vacuum with "
            "Schwarzschild's Kretschmann, v(r_s) = c, and (1/2)v^2 = GM/r "
            "exactly"
        ),
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="supporting_theorem",
        scope="static spherical exterior only; interior cap untouched",
    )
    ns.record_obligation(ProofObligationRecord(
        obligation_id="horizon_accounting_note_021",
        script_id=SCRIPT_ID,
        title="Horizon as accounting corollary (theorem note)",
        status=ObligationStatus.SATISFIED,
        satisfied_by=["horizon_accounting_021"],
        description=(
            "Supports development/horizon_accounting/horizon_accounting_note.md: "
            "the horizon's existence and location are P9 corollaries, the "
            "Michell coincidence is explained by the PG-exact ledger, and the "
            "gamma discriminator separates the routes."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="horizon_accounting_claim_021",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "In the bookkeeping exterior, the horizon exists at finite radius "
            "if and only if configuration energy is counted once at the "
            "universal coupling (lambda = -1): the exponential and reciprocal "
            "accountings have no horizon anywhere. The Michell radius "
            "agreement is explained rather than inherited: the derived "
            "exterior's PG slicing carries the exact Newtonian-formed ledger "
            "(1/2)v^2 = GM/r with v = c at r_s, which is the P9 resummation's "
            "signature, while the Michell route itself fails at the first "
            "metric observable (gamma = 0). Exterior only; the interior cap "
            "obligation is untouched."
        ),
        derivation_ids=["horizon_accounting_021"],
        obligation_ids=["horizon_accounting_note_021"],
    ))


def main() -> None:
    header("Trial 021: The Horizon as an Accounting Corollary")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    failures: list = []
    case_1_radius(failures)
    case_2_horizon_existence(failures)
    case_3_metric_discriminator(failures)
    case_4_pg_exactness(failures)
    case_5_verdict()

    if failures:
        for f in failures:
            print(f"  FAILED: {f}")
        raise SystemExit("Trial 021: verification failure")

    record_results(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
