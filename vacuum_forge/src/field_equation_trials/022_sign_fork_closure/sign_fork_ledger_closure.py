# Trial 022: closing the C2 sign fork honestly
#
# Group:
#   022_sign_fork_closure
#
# Script type:
#   NO-GO THEOREM / SELECTOR CLOSURE / NARRATION CORRECTION
#
# Purpose
# -------
# Trial C2 resolved the P4 sign fork (lamda = -1, negative temporal-sector
# self-coupling) by EXACT AREAL SCHWARZSCHILD RECOVERY -- target-matching,
# recorded honestly as PROVISIONAL_CONVENTION. The section of record
# (proof.md section 2.3) later narrated the same step as "P9 selects
# lamda = -1 ... the sign is forced, not chosen," which is stronger than
# the archive supports: P9's own adoption record states "P9 does not fix
# the SIGN." This trial closes the fork properly, in four theorems:
#
#   THEOREM A (normalization emptiness). The C2 statement "|lamda| = 1 is
#     fixed by P6 universality" is definitional, not physical: writing
#     u_field = lamda c^4 (s')^2 / (8 pi G) makes "the field sources at
#     the universal coupling" an identity for EVERY lamda. Universality
#     has no selective power until u_field is derived independently.
#
#   THEOREM B (ledger no-go). The one invariant static accounting handle
#     -- the work ledger of quasi-static assembly, evaluated on the
#     interaction (cross) term of two concentric shells, where
#     self-energy and localization ambiguities drop out -- FORCES
#     |lamda| = 1/4 under a gradient-local density, with the SIGN
#     depending on the matter-counting convention:
#       rest-mass counting (the P6-natural ledger: the vacuum pays)
#         => lamda = -1/4;
#       redshift counting (matter pays) => lamda = +1/4.
#     Neither is -1. Corollary: C2 case 4's "the Newtonian field-energy
#     convention is recovered" is FALSE as stated -- the lamda = -1
#     self-source is exactly 4x the Newtonian density (the unexplained
#     "x (1/4)" in C2's case-4 narration is the scar). Static
#     density-level accounting CANNOT select lamda. This is a theorem,
#     not a lament: the sign fork is closed by other means (C, D) and
#     the accounting shortcut is retired with a proof of why.
#
#   THEOREM C (the observable face). On the P7' branch B = 1/A, the
#     family member A_lamda has PPN gamma = 1 for every lamda and
#     beta = lamda + 2, i.e.
#
#         beta - 1 = lamda + 1.
#
#     Every measurement of |beta - 1| bounds |lamda + 1| identically.
#     Current bounds (|beta - 1| <~ 1e-4, LLR Nordtvedt + Cassini;
#     classical Mercury alone gives ~1e-2) pin lamda = -1 empirically
#     and kill the ledger candidates (-1/4 => beta = 1.75, +1/4 =>
#     beta = 2.25, 0 => beta = 2, +1 => beta = 3) by three or more
#     orders of magnitude. Recorded as a post-derivation kill condition
#     in the section-7 sense, not as the derivation.
#
#   THEOREM D (the internal selector, exact and self-contained). With
#     the Einstein tensor computed from scratch (Christoffel -> Riemann
#     -> Ricci -> G), on the compensated branch B = 1/A_lamda the vacuum
#     tt-equation G^t_t = 0 holds as an identity in r IF AND ONLY IF
#     lamda = -1, at which point every component of G^a_b vanishes.
#     After the section-4 closure derives the response law (the 018
#     program -- verified here to contain no reference to the C2 family
#     or its selector, so no circularity), this selector is
#     unconditional and internal: the sign of the temporal-sector
#     self-coupling is a THEOREM of the derived dynamics, not of static
#     accounting.
#
# Net status shift: the P4 sign fork closes at lamda = -1 via Theorem D
# (internal, post-closure) with Theorem C as its standing empirical
# fence; the density-matching reading of P9 is retired by Theorem B; and
# proof.md section 2.3's narration must be re-scoped to match (doc
# alignment obligation recorded).
#
# Scope: static spherical temporal sector, second order (Theorems A-C);
# exact (Theorem D). Nothing here touches the radiative sector or the
# interior.

from pathlib import Path

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    BranchDecisionRecord,
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
        dependency_id="c2_family_dependency_022",
        upstream_script_id="002_trial_C_burden_ledger__trial_C2_self_coupling_bootstrap",
        upstream_derivation_id="bootstrap_family_exact_solution_c2",
        expected_record_kind=RecordKind.DERIVATION,
    )
    ns.declare_dependency(
        dependency_id="c3_reselection_dependency_022",
        upstream_script_id="002_trial_C_burden_ledger__trial_C3_spatial_bootstrap",
        upstream_derivation_id="family_spatial_reselection_c3",
        expected_record_kind=RecordKind.DERIVATION,
    )
    return archive, ns, invalidated


# =============================================================================
# Symbols
# =============================================================================

r = sp.Symbol("r", positive=True)
r_s = sp.Symbol("r_s", positive=True)
lam = sp.Symbol("lamda", real=True, nonzero=True)
G, c = sp.symbols("G c", positive=True)
m1, m2 = sp.symbols("m_1 m_2", positive=True)
a, b = sp.symbols("a b", positive=True)  # shell radii, a < b

x = r_s / r
A_lam = (1 + lam * x) ** (-1 / lam)


def areal_lap(f):
    return sp.diff(r**2 * sp.diff(f, r), r) / r**2


# =============================================================================
# Case 0
# =============================================================================


def case_0_problem(out: ScriptOutput) -> None:
    header("Case 0: The provenance gap this trial closes")
    print("C2's machine-checked selector for lamda = -1 is exact areal")
    print("Schwarzschild recovery (C2 case 3) -- target-matching, recorded as")
    print("PROVISIONAL_CONVENTION. P9's adoption record states 'P9 does not fix")
    print("the SIGN.' proof.md section 2.3 nevertheless narrates the sign as")
    print("'forced, not chosen' by count-once accounting. Locked-door question:")
    print()
    print("  Can static energy accounting select lamda at all? If not, prove")
    print("  it cannot (no-go), and close the fork by the selectors that do")
    print("  work: the derived response law (internal) and the PPN beta map")
    print("  (empirical fence).")

    with out.governance_assessments():
        out.line("Trial 022 opened", StatusMark.INFO,
                 "sign-fork closure: no-go + response selector + beta fence")


# =============================================================================
# Case 1: Theorem A -- the universality normalization is empty
# =============================================================================


def case_1_normalization_empty(out: ScriptOutput) -> None:
    header("Case 1: Theorem A -- '|lamda| = 1 by P6 universality' is definitional")
    s = sp.Function("s")(r)
    u_field = lam * c**4 * sp.diff(s, r) ** 2 / (8 * sp.pi * G)
    # The 'universal coupling' statement: Delta s = (8 pi G / c^4) u_field.
    # Substituting the DEFINITION of u_field, this is Delta s = lamda (s')^2
    # -- the bootstrap equation itself, for every lamda.
    residual = sp.simplify(
        (8 * sp.pi * G / c**4) * u_field - lam * sp.diff(s, r) ** 2
    )
    print("  u_field := lamda c^4 (s')^2 / (8 pi G)   (the C2 parametrization)")
    print("  'field sources at universal coupling':  Delta s = (8 pi G/c^4) u_field")
    print(f"  residual vs the bootstrap equation Delta s = lamda (s')^2: {sp.sstr(residual)}")
    print()
    print("  The identity holds for EVERY lamda: the parametrization absorbs the")
    print("  density normalization, so 'universal coupling, count once' selects")
    print("  nothing until u_field is derived from an independent ledger. The")
    print("  a-priori fork is the whole real line, not the two points +/-1.")

    with out.derived_results():
        out.line("universality normalization empty",
                 StatusMark.PASS if is_zero(residual) else StatusMark.FAIL,
                 "coupling-universality is an identity in lamda; no selective power without independent u_field")


# =============================================================================
# Case 2: Theorem B -- the invariant shell ledger forces |lamda| = 1/4
# =============================================================================


def case_2_ledger_no_go(out: ScriptOutput) -> None:
    header("Case 2: Theorem B -- invariant two-shell ledger: |lamda| = 1/4, sign ledger-dependent")
    print("Two concentric thin shells: m_1 at radius a, m_2 at radius b > a.")
    print("Weak field, second order; only CROSS (interaction) terms are used,")
    print("so shell self-energies and localization surface terms drop out.")
    print()

    # --- (0) first-order map: s = ln A -> 2 Phi / c^2 -----------------------
    s_weak = sp.log(A_lam)
    s_series = sp.series(s_weak, r_s, 0, 2).removeO()
    map_residual = sp.simplify(s_series - (-x))  # s -> -r_s/r = 2 Phi/c^2
    print(f"  weak-field map: s = ln A -> -r_s/r = 2 Phi/c^2  (residual {sp.sstr(map_residual)})")

    # --- (1) the invariant: quasi-static work ledger -------------------------
    # Bring shell 2 in from infinity over shell 1's exterior field.
    R = sp.Symbol("R", positive=True)
    W_extracted = sp.integrate(G * m1 * m2 / R**2, (R, b, sp.oo))
    E_int_target = -W_extracted
    print(f"  work extracted at infinity: W = {sp.sstr(W_extracted)}")
    print(f"  invariant interaction energy: E_int = -W = {sp.sstr(E_int_target)}")

    # --- (2) gradient-local field density, cross term ------------------------
    # u = lamda c^4 |grad s|^2 / (8 pi G), s = 2 Phi / c^2 at first order.
    # grad Phi_i = G m_i / r^2 outward, shell i's field zero inside it, so the
    # cross term lives only at r > b.
    s1p = 2 * G * m1 / (c**2 * r**2)
    s2p = 2 * G * m2 / (c**2 * r**2)
    cross_density = lam * c**4 / (8 * sp.pi * G) * 2 * s1p * s2p
    E_cross_field = sp.integrate(cross_density * 4 * sp.pi * r**2, (r, b, sp.oo))
    E_cross_field = sp.simplify(E_cross_field)
    print(f"  field-density cross term: E_cross = {sp.sstr(E_cross_field)}")
    ratio_ok = is_zero(E_cross_field - 4 * lam * G * m1 * m2 / b)

    # --- (3) ledger 1: rest-mass matter counting (the P6-natural ledger) -----
    # P6: the energy exchanged with matter moving in gradients is drawn from
    # the vacuum -- the vacuum reservoir pays; matter stays at rest energy.
    # Then the field cross term must carry ALL of E_int.
    lam_rest = sp.solve(sp.Eq(E_cross_field, E_int_target), lam)
    print(f"  rest-mass counting (vacuum pays):    lamda = {sp.sstr(lam_rest)}")

    # --- (4) ledger 2: redshift matter counting (matter pays) ----------------
    # Matter counted at redshifted energy m c^2 (1 + Phi_other/c^2):
    # cross piece m_2 Phi_1(b) + m_1 Phi_2(a) = -2 G m_1 m_2 / b
    # (Phi_2 is constant = -G m_2 / b inside shell 2).
    matter_cross = m2 * (-G * m1 / b) + m1 * (-G * m2 / b)
    lam_redshift = sp.solve(sp.Eq(matter_cross + E_cross_field, E_int_target), lam)
    print(f"  redshift counting (matter pays):     lamda = {sp.sstr(lam_redshift)}")

    # --- (4b) interpolation: matter at fraction f of the redshift ------------
    # The full convention range fills [-1/4, +1/4]; no convention reaches -1.
    f = sp.Symbol("f", real=True)
    lam_f = sp.solve(sp.Eq(f * matter_cross + E_cross_field, E_int_target), lam)
    lam_f_expr = sp.simplify(lam_f[0])
    interp_ok = (
        sp.simplify(lam_f_expr - (2 * f - 1) / 4) == 0
        and lam_f_expr.subs(f, 0) == sp.Rational(-1, 4)
        and lam_f_expr.subs(f, 1) == sp.Rational(1, 4)
    )
    # the price of leaving the operational range [0, 1]:
    f_at_schwarzschild = sp.solve(sp.Eq(lam_f_expr, -1), f)
    f_at_sign_boundary = sp.solve(sp.Eq(lam_f_expr, sp.Rational(-1, 4)), f)
    excursion_ok = (
        f_at_schwarzschild == [sp.Rational(-3, 2)]
        and f_at_sign_boundary == [0]
    )
    print(f"  interpolating conventions (fraction f of redshift): lamda = {sp.sstr(lam_f_expr)}")
    print("  => the convention range [0, 1] fills [-1/4, +1/4]; no f in [0, 1] reaches -1")
    print(f"  price of excursion: lamda = -1 requires f = {sp.sstr(f_at_schwarzschild)};")
    print(f"  even lamda < -1/4 (the Schwarzschild sign regime) requires f < {sp.sstr(f_at_sign_boundary[0])}")
    print()

    # --- (5) the factor of four ----------------------------------------------
    Phi_p = sp.Symbol("Phi_prime", real=True)
    u_minus_one = -c**4 * (2 * Phi_p / c**2) ** 2 / (8 * sp.pi * G)
    u_newton = -Phi_p**2 / (8 * sp.pi * G)
    factor = sp.simplify(u_minus_one / u_newton)
    print(f"  u(lamda=-1) / u_Newtonian = {sp.sstr(factor)}  (C2 case 4's 'x (1/4)' scar)")
    print()
    print("  CONCLUSION (no-go): a gradient-local density evaluated on the")
    print("  invariant work ledger forces |lamda| = 1/4 -- never 1 -- with the")
    print("  sign set by the matter-counting convention, not by physics. The")
    print("  lamda = -1 self-source is 4x the Newtonian density: it is NOT the")
    print("  ledger energy density, and 'the Newtonian convention is recovered'")
    print("  (C2 case 4) is corrected here. Static density-level accounting")
    print("  cannot select lamda. What IS ledger-invariant survives: the total")
    print("  reservoir is negative (binding deficit) in the P6 ledger -- the")
    print("  SIGN story at integral level -- but the equation weight does not")
    print("  follow from it.")

    with out.derived_results():
        out.line("weak-field map s -> 2 Phi/c^2",
                 StatusMark.PASS if is_zero(map_residual) else StatusMark.FAIL,
                 "first-order identification used by the cross-term ledger")
        out.line("invariant interaction energy = -G m1 m2 / b",
                 StatusMark.PASS if is_zero(E_int_target + G * m1 * m2 / b) else StatusMark.FAIL,
                 "quasi-static work ledger, concentric shells")
        out.line("field-density cross term = 4 lamda G m1 m2 / b",
                 StatusMark.PASS if ratio_ok else StatusMark.FAIL,
                 "gradient-local density integrated over r > b")
        out.line("rest-mass ledger selects lamda = -1/4",
                 StatusMark.PASS if lam_rest == [sp.Rational(-1, 4)] else StatusMark.FAIL,
                 "P6-natural counting (vacuum pays) -- NOT -1")
        out.line("redshift ledger selects lamda = +1/4",
                 StatusMark.PASS if lam_redshift == [sp.Rational(1, 4)] else StatusMark.FAIL,
                 "matter-pays counting -- NOT -1; sign is ledger-relative")
        out.line("interpolating conventions fill [-1/4, +1/4]",
                 StatusMark.PASS if interp_ok else StatusMark.FAIL,
                 "lamda = (2f-1)/4 for matter at fraction f of redshift; no f in [0, 1] reaches -1")
        out.line("excursion price: lamda = -1 needs f = -3/2",
                 StatusMark.PASS if excursion_ok else StatusMark.FAIL,
                 "outside the operational audits [0, 1]; even the Schwarzschild sign regime needs f < 0")
        out.line("u(lamda=-1) is 4x the Newtonian density",
                 StatusMark.PASS if is_zero(factor - 4) else StatusMark.FAIL,
                 "corrects C2 case 4's 'Newtonian convention recovered' narration")


# =============================================================================
# Case 3: Theorem C -- gamma(lamda) = 1, beta(lamda) = lamda + 2
# =============================================================================


def case_3_ppn_face(out: ScriptOutput) -> None:
    header("Case 3: Theorem C -- the fork's observable face: beta - 1 = lamda + 1")
    w = sp.Symbol("w", positive=True)  # w = r_s / rho (isotropic radial coord)
    k1, k2 = sp.symbols("k_1 k_2", real=True)

    # areal-gauge family to second order; a2 = (1 + lamda)/2
    xx = sp.Symbol("xx", positive=True)  # x = r_s / r
    A_x = (1 + lam * xx) ** (-1 / lam)
    A_ser = sp.series(A_x, xx, 0, 3).removeO()
    a2 = sp.simplify(A_ser.coeff(xx, 2))
    a2_ok = is_zero(a2 - (1 + lam) / 2)
    print(f"  areal second-order coefficient: a2 = {sp.sstr(a2)}")

    # transform to isotropic coordinates: r = rho (1 + k1 w + k2 w^2)
    rho = sp.Symbol("rho", positive=True)
    r_of_rho = rho * (1 + k1 * w + k2 * w**2)
    x_of_w = sp.series((r_s / r_of_rho).subs(r_s, w * rho), w, 0, 3).removeO()

    A_iso = (1 - x_of_w + a2 * x_of_w**2).expand()
    B_iso = sp.series(1 / (1 - x_of_w + a2 * x_of_w**2), w, 0, 3).removeO()

    dr_drho = sp.diff(r_of_rho.subs(r_s, w * rho), rho)  # careful: w depends on rho
    # do it explicitly: r(rho) = rho + k1 r_s + k2 r_s^2 / rho
    r_explicit = rho + k1 * r_s + k2 * r_s**2 / rho
    dr_drho = sp.diff(r_explicit, rho)

    # isotropy condition: B(r) (dr/drho)^2 = r^2 / rho^2
    lhs = (B_iso * dr_drho.subs(r_s, w * rho) ** 2).expand()
    rhs = ((r_explicit / rho) ** 2).subs(r_s, w * rho).expand()
    cond = sp.series(sp.expand(lhs - rhs), w, 0, 3).removeO()
    sol = sp.solve(
        [sp.expand(cond.coeff(w, 1)), sp.expand(cond.coeff(w, 2))], [k1, k2], dict=True
    )[0]
    print(f"  transform coefficients: k1 = {sp.sstr(sol[k1])}, k2 = {sp.sstr(sol[k2])}")

    # gamma: spatial factor f = r^2/rho^2 = 1 + 2 k1 w + ... = 1 + gamma w + ...
    gamma = sp.simplify(2 * sol[k1])
    # beta: A in w: 1 - w + (beta/2) w^2
    A_in_w = sp.series(A_iso.subs({k1: sol[k1], k2: sol[k2]}), w, 0, 3).removeO()
    c1_w = sp.simplify(A_in_w.coeff(w, 1))
    beta = sp.simplify(2 * A_in_w.coeff(w, 2))
    print(f"  gamma = {sp.sstr(gamma)}   (lamda-independent: gamma-degeneracy re-derived)")
    print(f"  first-order check: coefficient of w = {sp.sstr(c1_w)} (must be -1)")
    print(f"  beta  = {sp.sstr(beta)}   =>   beta - 1 = lamda + 1")
    print()
    print("  The fork's kill condition (post-derivation, section-7 sense):")
    print("    |beta - 1| <~ 1e-4  (LLR Nordtvedt + Cassini gamma; Will 2014)")
    print("    => |lamda + 1| <~ 1e-4.  Classical Mercury alone: |lamda+1| <~ 1e-2.")
    print("  Family members under the fence:")
    for lv, name in [(-1, "Schwarzschild"), (sp.Rational(-1, 4), "rest-ledger"),
                     (sp.Rational(1, 4), "redshift-ledger"), (0, "exponential"),
                     (1, "reciprocal")]:
        bv = sp.simplify(beta.subs(lam, lv)) if lv != 0 else sp.limit(beta, lam, 0)
        print(f"    lamda = {sp.sstr(sp.nsimplify(lv))}: beta = {sp.sstr(bv)}  ({name})")

    with out.derived_results():
        out.line("a2 = (1 + lamda)/2 re-derived",
                 StatusMark.PASS if a2_ok else StatusMark.FAIL,
                 "areal second-order coefficient of the family")
        out.line("gamma = 1 for every lamda",
                 StatusMark.PASS if is_zero(gamma - 1) else StatusMark.FAIL,
                 "gamma-degeneracy: light bending and time delay cannot see the fork; "
                 "beta is itself a 1PN parameter, so the fork lives inside 1PN")
        out.line("beta = lamda + 2 (so beta - 1 = lamda + 1)",
                 StatusMark.PASS if is_zero(beta - (lam + 2)) and is_zero(c1_w + 1) else StatusMark.FAIL,
                 "isotropic-gauge PPN map of the family; Schwarzschild check beta(-1)=1")
    with out.sample_results():
        out.line("ledger candidates killed by the fence",
                 StatusMark.PASS if is_zero(beta.subs(lam, sp.Rational(-1, 4)) - sp.Rational(7, 4)) else StatusMark.FAIL,
                 "lamda=-1/4 => beta=7/4; +1/4 => 9/4; 0 => 2; +1 => 3 -- all dead at >=3 orders of magnitude")


# =============================================================================
# Case 4: Theorem D -- the exact internal selector, from scratch
# =============================================================================


def einstein_mixed(A_expr, B_expr):
    """Einstein tensor G^a_b for ds^2 = -c^2 A dt^2 + B dr^2 + r^2 dOmega^2,
    computed from scratch: Christoffel -> Riemann -> Ricci -> G."""
    t, th, ph = sp.symbols("t theta phi")
    coords = [t, r, th, ph]
    g = sp.diag(-c**2 * A_expr, B_expr, r**2, r**2 * sp.sin(th) ** 2)
    ginv = g.inv()
    n = 4
    Gamma = [[[sp.S(0)] * n for _ in range(n)] for _ in range(n)]
    for aa in range(n):
        for bb in range(n):
            for cc in range(n):
                Gamma[aa][bb][cc] = sp.simplify(
                    sum(
                        ginv[aa, dd]
                        * (
                            sp.diff(g[dd, bb], coords[cc])
                            + sp.diff(g[dd, cc], coords[bb])
                            - sp.diff(g[bb, cc], coords[dd])
                        )
                        for dd in range(n)
                    )
                    / 2
                )
    ricci = sp.zeros(n)
    for bb in range(n):
        for dd in range(n):
            expr = sp.S(0)
            for aa in range(n):
                expr += sp.diff(Gamma[aa][bb][dd], coords[aa]) - sp.diff(
                    Gamma[aa][bb][aa], coords[dd]
                )
                for ee in range(n):
                    expr += (
                        Gamma[aa][aa][ee] * Gamma[ee][bb][dd]
                        - Gamma[aa][dd][ee] * Gamma[ee][bb][aa]
                    )
            ricci[bb, dd] = sp.simplify(expr)
    r_scalar = sp.simplify(sum(ginv[i, j] * ricci[i, j] for i in range(n) for j in range(n)))
    g_lower = ricci - r_scalar / 2 * g
    g_mixed = sp.simplify(ginv * g_lower)
    return g_mixed


def case_4_response_selector(out: ScriptOutput) -> None:
    header("Case 4: Theorem D -- G^t_t = 0 on the P7' branch selects lamda = -1 exactly")
    A_f = sp.Function("A")(r)
    B_f = sp.Function("B")(r)
    Gm = einstein_mixed(A_f, B_f)

    # (i) the tt-identity of section 2.4a, re-derived from scratch
    tt_identity = sp.simplify(
        Gm[0, 0] + sp.diff(r * (1 - 1 / B_f), r) / r**2
    )
    # (ii) the t-r block identity of section 2.2
    tr_identity = sp.simplify(
        (Gm[0, 0] - Gm[1, 1]) + sp.diff(sp.log(A_f * B_f), r) / (r * B_f)
    )
    print(f"  tt-identity residual   (G^t_t = -(1/r^2) d/dr[r(1-1/B)]): {sp.sstr(tt_identity)}")
    print(f"  t-r identity residual  (G^t_t - G^r_r = -(ln AB)'/(rB)):  {sp.sstr(tr_identity)}")

    # (iii) the exact selector on the compensated branch B = 1/A_lam
    flux = r * (1 - A_lam)  # G^t_t = 0 <=> this is r-independent
    flux_deriv = sp.simplify(sp.diff(flux, r))
    lead = sp.simplify(sp.series(flux_deriv, r_s, 0, 3).removeO().coeff(r_s, 2))
    sel = sp.solve(sp.Eq(lead, 0), lam)
    witness_p1 = sp.simplify(flux_deriv.subs(lam, 1))
    exact_m1 = sp.simplify(flux_deriv.subs(lam, -1))
    print(f"  d/dr[r(1 - A_lamda)] leading coefficient: {sp.sstr(lead)} * r_s^2  => zero iff lamda = {sp.sstr(sel)}")
    print(f"  witness lamda = +1: d/dr[r(1-A)] = {sp.sstr(witness_p1)}  (nonzero)")
    print(f"  exact lamda = -1:  d/dr[r(1-A)] = {sp.sstr(exact_m1)}")

    # (iv) full vacuum at lamda = -1
    A_m1 = 1 - x
    Gm_m1 = einstein_mixed(A_m1, 1 / A_m1)
    all_zero = all(is_zero(Gm_m1[i, j]) for i in range(4) for j in range(4))
    print(f"  all G^a_b components vanish at lamda = -1, B = 1/A: {all_zero}")

    # (v) non-circularity: the 018 closure program never references the family
    closure_dir = Path(__file__).resolve().parents[1] / "018_closure_uniqueness"
    tokens = ("lamda", "trial_C2", "A_lam", "self_coupling_bootstrap")
    hits = []
    for py in sorted(closure_dir.glob("*.py")):
        text = py.read_text(encoding="utf-8", errors="replace")
        for tok in tokens:
            if tok in text:
                hits.append(f"{py.name}:{tok}")
    print(f"  018 closure program references to the C2 family/selector: {hits or 'none'}")
    print()
    print("  READING: the response law derived in section 4 (018 program) is")
    print("  logically upstream-independent of the C2 selector; applying it to")
    print("  the family is therefore a non-circular internal closure of the")
    print("  sign fork. This is C3 case 3's re-selection, made exact and")
    print("  self-contained, and promoted from consistency-check to selector")
    print("  of record.")

    with out.derived_results():
        out.line("tt-identity re-derived from scratch",
                 StatusMark.PASS if is_zero(tt_identity) else StatusMark.FAIL,
                 "G^t_t = -(1/r^2) d/dr[r(1-1/B)] for arbitrary static spherical A, B")
        out.line("t-r block identity re-derived from scratch",
                 StatusMark.PASS if is_zero(tr_identity) else StatusMark.FAIL,
                 "G^t_t - G^r_r = -(ln AB)'/(rB) for arbitrary static spherical A, B")
        out.line("exact selector: G^t_t = 0 on B = 1/A_lamda iff lamda = -1",
                 StatusMark.PASS if sel == [-1] and not is_zero(witness_p1) and is_zero(exact_m1) else StatusMark.FAIL,
                 "r(1 - A_lamda) is r-independent only for the Schwarzschild member")
        out.line("full vacuum at lamda = -1",
                 StatusMark.PASS if all_zero else StatusMark.FAIL,
                 "every mixed Einstein component vanishes on the selected member")
    with out.sample_results():
        out.line("018 closure program is lamda-blind",
                 StatusMark.PASS if not hits else StatusMark.FAIL,
                 "no reference to the C2 family or selector: the internal closure is non-circular")


# =============================================================================
# Case 5: verdict
# =============================================================================


def case_5_verdict(out: ScriptOutput) -> None:
    header("Case 5: Trial 022 verdict")
    print("DERIVED (static spherical temporal sector):")
    print()
    print("  A. '|lamda| = 1 by universality' is definitional; the a-priori")
    print("     fork is the real line.")
    print("  B. The invariant shell ledger forces |lamda| = 1/4 under a")
    print("     gradient-local density, sign set by matter-counting convention.")
    print("     Density-level static accounting CANNOT select lamda (no-go);")
    print("     C2 case 4's 'Newtonian convention recovered' is corrected")
    print("     (factor 4).")
    print("  C. gamma = 1 for all lamda; beta - 1 = lamda + 1: the fork has an")
    print("     observable face, and |beta - 1| <~ 1e-4 pins lamda = -1")
    print("     empirically (kill condition, not derivation).")
    print("  D. The derived response law selects lamda = -1 exactly and")
    print("     non-circularly (018 is lamda-blind): the sign is a theorem of")
    print("     the closed dynamics.")
    print()
    print("STATUS SHIFTS:")
    print("  P4 sign fork (temporal/static): CLOSED at lamda = -1 by Theorem D,")
    print("    fenced by Theorem C. The C2 PROVISIONAL_CONVENTION is upgraded;")
    print("    the density-matching reading of P9 is retired by Theorem B.")
    print("  proof.md section 2.3: narration must be re-scoped ('the sign is")
    print("    forced by count-once accounting' -> 'the family and anchor are")
    print("    accounting; the sign is fixed by the derived response law, with")
    print("    beta - 1 = lamda + 1 as the standing fence'). Doc alignment")
    print("    obligation recorded.")
    print("  021_horizon_accounting: its 'horizon existence is P9-selected'")
    print("    framing inherits the same correction (selection is by the")
    print("    response law; P9 alone does not fix the sign).")
    print()
    print("NOT CLOSED HERE: whether a MULTI-CONFIGURATION ledger-rigidity")
    print("demand (one local matter coupling making the exact assembly ledger")
    print("consistent for ALL static configurations at third order) selects")
    print("lamda = -1 by accounting alone. Recorded as a candidate route: if")
    print("it lands, the accounting-only closure is rescued; if it fails, the")
    print("no-go extends beyond density level.")

    with out.governance_assessments():
        out.line("Trial 022 verdict: sign fork closed (response selector + beta fence); accounting no-go proved",
                 StatusMark.PASS,
                 "lamda = -1 is a theorem of the derived dynamics, not of static accounting")
    with out.unresolved_obligations():
        out.line("doc alignment: proof.md 2.3/7, P9 file, 021 narration",
                 StatusMark.OBLIGATION,
                 "re-scope 'sign forced by accounting' to 'sign from response law, beta fence standing'")
        out.line("ledger-rigidity route: accounting-only selector at third order",
                 StatusMark.OBLIGATION,
                 "multi-configuration consistency of one local matter coupling; open research question")


# =============================================================================
# Archive recording
# =============================================================================


def record_results(ns) -> None:
    ns.record_derivation(
        derivation_id="universality_normalization_empty_022",
        inputs=[lam],
        output=sp.Symbol("identity_for_all_lamda"),
        method="substitute u_field = lamda c^4 (s')^2/(8 pi G) into the universal-coupling statement",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="normalization_audit",
        scope="'|lamda| = 1 by P6' is definitional; the fork is a priori the real line",
    )
    ns.record_derivation(
        derivation_id="invariant_shell_ledger_no_go_022",
        inputs=[m1, m2, b],
        output=sp.FiniteSet(sp.Rational(-1, 4), sp.Rational(1, 4)),
        method="concentric-shell cross-term ledger vs quasi-static work invariant; endpoint conventions plus f-interpolation",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="exclusion",
        scope="gradient-local density confines lamda to [-1/4, +1/4] (lamda = (2f-1)/4 across matter conventions); static density accounting cannot select lamda = -1",
    )
    ns.record_derivation(
        derivation_id="newtonian_convention_factor_four_022",
        inputs=[],
        output=sp.Integer(4),
        method="u(lamda=-1) / u_Newtonian with s' = 2 Phi'/c^2",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="narration_correction",
        scope="corrects C2 case 4: the lamda = -1 self-source is 4x the Newtonian field-energy density, not equal to it",
    )
    ns.record_derivation(
        derivation_id="ppn_beta_map_022",
        inputs=[lam],
        output=sp.Eq(sp.Symbol("beta"), lam + 2),
        method="areal-to-isotropic transform of the family on the P7' branch, second order; gamma = 1 checked",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="observable_face",
        scope="beta - 1 = lamda + 1: every beta measurement bounds the sign fork identically",
    )
    ns.record_derivation(
        derivation_id="beta_fence_kill_condition_022",
        inputs=[],
        output=sp.Symbol("abs_lamda_plus_one_below_1e4"),
        method="LLR Nordtvedt + Cassini bound |beta-1| <~ 1e-4 applied to beta - 1 = lamda + 1",
        status=Status.OBSERVATIONAL_CONSTRAINT,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="kill_condition",
        scope="post-derivation fence: lamda = -1 +/- ~1e-4; ledger candidates +/-1/4, 0, +1 all excluded",
    )
    ns.record_derivation(
        derivation_id="response_selector_exact_022",
        inputs=[lam],
        output=sp.Eq(lam, -1),
        method="from-scratch Einstein tensor; G^t_t = 0 on B = 1/A_lamda iff lamda = -1; full vacuum at -1; 018 lamda-blindness scan",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="selector",
        scope="the derived response law closes the sign fork internally and non-circularly",
    )

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="temporal_sector_sign_closed_022",
        script_id=SCRIPT_ID,
        branch_id="p4_sign_fork_temporal_static_sector",
        status=GovernanceStatus.LICENSED_CLAIM,
        tier=ClaimTier.LICENSING,
        obligation_ids=["doc_alignment_sign_fork_022", "ledger_rigidity_route_022"],
        description=(
            "The P4 sign fork (temporal/static sector) is CLOSED at lamda = -1. "
            "Selector of record: the derived response law (Theorem D; exact, "
            "non-circular -- the 018 closure program is lamda-blind). Standing "
            "empirical fence: beta - 1 = lamda + 1 with |beta - 1| <~ 1e-4 "
            "(Theorem C). The C2 PROVISIONAL_CONVENTION (recovery-selected) is "
            "superseded; the density-matching reading of P9 is retired by the "
            "ledger no-go (Theorem B: gradient-local density forces |lamda| = "
            "1/4 with ledger-relative sign). What remains true of the accounting "
            "story: the total static reservoir is negative (binding deficit) in "
            "the P6 ledger, at integral level; the equation weight is fixed by "
            "the dynamics, not the ledger."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="doc_alignment_sign_fork_022",
        script_id=SCRIPT_ID,
        title="Re-scope proof.md 2.3/7, P9 'what it fixes', and 021 narration to the closed selector",
        status=ObligationStatus.OPEN,
        required_by=["temporal_sector_sign_closed_022"],
        description=(
            "proof.md section 2.3 must stop claiming the sign is 'forced' by "
            "count-once accounting; the honest chain is: accounting gives the "
            "family and the Newton anchor; the derived response law gives the "
            "sign; beta - 1 = lamda + 1 is the standing fence. P9's file "
            "already states the sign is not fixed by P9 alone and needs no "
            "change of content, only a pointer to this trial. "
            "021_horizon_accounting's 'P9-selected' phrasing inherits the "
            "correction."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="ledger_rigidity_route_022",
        script_id=SCRIPT_ID,
        title="Ledger-rigidity selector: can multi-configuration assembly consistency select lamda = -1 by accounting alone?",
        status=ObligationStatus.OPEN,
        required_by=[],
        description=(
            "Theorem B's no-go is at density level (single invariant per "
            "configuration class). A stronger accounting demand remains "
            "untested: require ONE local matter-coupling correction chi such "
            "that the exact quasi-static work ledger M_farfield = "
            "integral sqrt(A) dm holds for ALL static configurations "
            "(single shell fixes chi at second order, chi = redshift "
            "weighting; multi-shell configurations over-determine the system "
            "at third order). If consistency forces lamda = -1, the "
            "accounting-only closure is rescued; if a family survives, the "
            "no-go extends beyond density level. Either outcome resolves the "
            "question honestly."
        ),
    ))

    ns.record_route(RouteRecord(
        route_id="ledger_rigidity_selector_route_022",
        script_id=SCRIPT_ID,
        name="Ledger-rigidity selector (accounting-only closure attempt, third order)",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=["ledger_rigidity_route_022"],
        activation_conditions=[
            "third-order two-shell assembly ledger formalized with local coupling ansatz chi(V)",
            "kill condition declared before computation: a surviving lamda-family kills the route",
        ],
    ))

    ns.record_claim(ClaimRecord(
        claim_id="sign_fork_closure_022",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.LICENSING,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "The temporal-sector self-coupling sign lamda = -1 is a theorem of "
            "the derived response law (exact selector on the P7' branch; "
            "non-circular, the 018 closure being lamda-blind), with the "
            "standing empirical fence beta - 1 = lamda + 1, |beta - 1| <~ "
            "1e-4. Static density-level energy accounting cannot make this "
            "selection: the invariant concentric-shell work ledger forces "
            "|lamda| = 1/4 under any gradient-local density, with the sign "
            "set by the matter-counting convention (rest-mass counting: -1/4; "
            "redshift counting: +1/4). The lamda = -1 self-source is exactly "
            "4x the Newtonian field-energy density; C2 case 4's 'Newtonian "
            "convention recovered' narration is corrected accordingly. "
            "Horizon existence (A(r_s) = 0, lamda < 0 only) is therefore a "
            "corollary of the derived dynamics plus the beta fence, not of "
            "count-once accounting."
        ),
        derivation_ids=[
            "universality_normalization_empty_022",
            "invariant_shell_ledger_no_go_022",
            "newtonian_convention_factor_four_022",
            "ppn_beta_map_022",
            "beta_fence_kill_condition_022",
            "response_selector_exact_022",
        ],
        obligation_ids=[
            "doc_alignment_sign_fork_022",
            "ledger_rigidity_route_022",
        ],
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Trial 022: Closing the C2 Sign Fork -- Ledger No-Go, Beta Fence, Response Selector")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    case_0_problem(out)
    case_1_normalization_empty(out)
    case_2_ledger_no_go(out)
    case_3_ppn_face(out)
    case_4_response_selector(out)
    case_5_verdict(out)

    record_results(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
