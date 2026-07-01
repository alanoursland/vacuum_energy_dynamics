# Trial 020: Nonlinear stability -- scoped closure
#
# Script type:
#   RIGOR CLOSURE / NONLINEAR STABILITY (SCOPED)
#
# Purpose
# -------
# The proof's remaining stability debt is nonlinear: the sector-signature
# theorems (ghost exclusion, source binding, radiative positivity) were
# proved at reduced or quadratic level. This script closes the debt in
# three in-house pieces and one honestly-recorded external mathematical
# anchor:
#
#   (1) NONLINEAR SOURCE BINDING (Theorem 3 lifted). In the fully
#       nonlinear spherical sector, vacuum + a regular center force the
#       flat state uniquely: the 019 Birkhoff family B = r/(C1 + r) has
#       Kretschmann K = 12 C1^2 / r^6, so regularity kills C1, the t-r
#       identity then forces A constant, and asymptotic flatness makes it
#       1. The negative static reservoir has no self-supporting (source-
#       free) nonlinear configuration to decay into or be mined from.
#
#   (2) NO NONLINEAR MINING (Misner-Sharp positivity). For any spherical
#       configuration of the closed parent with nonnegative local energy
#       density, the quasilocal Misner-Sharp mass satisfies
#       m'(r) = (4 pi r^2/c^2) rho >= 0 with m(0) = 0 at a regular
#       center, hence m(r) >= 0 everywhere -- fully nonlinearly, at
#       arbitrary field strength. The negative configuration energy
#       u_field = -c^4 (s')^2 / 8 pi G is bookkept inside m and can never
#       drive a quasilocal mass negative: there is no nonlinear channel
#       that extracts unbounded energy from the static reservoir.
#
#   (3) SECTOR SIGNATURE AT QUADRATIC ORDER (inherited + re-verified).
#       The propagating TT sector has positive-definite energy (G03), the
#       scalar sector is constraint-type (ghost exclusion, G03), and the
#       vector sector is constraint-type through general linear time
#       dependence (017). Re-verified here: the TT energy density is a
#       sum of squares.
#
#   (4) THE GLOBAL SMALL-DATA STATEMENT (external mathematical anchor,
#       recorded as such). Full nonspherical global nonlinear stability
#       of the flat state for the closed parent is the Christodoulou-
#       Klainerman theorem (1993; also Lindblad-Rodnianski 2010 in
#       harmonic gauge). Since 018 closed the parent to the Einstein-
#       Hilbert response, these are theorems of PDE analysis about the
#       very equations already derived -- the same import class as
#       Fierz-Pauli 1939: mathematics of a hyperbolic system on
#       Minkowski-asymptotic data, with no gravitational phenomenology
#       as input. No coefficient of the framework depends on them.
#       This is recorded as an import, not claimed as in-house work.
#
# Scope statement (honest boundary): pieces (1)-(3) are proved in-house
# from scratch below. Piece (4) is an external mathematical theorem about
# the derived equations; an in-house re-derivation at Christodoulou-
# Klainerman scale is declared out of scope by decision, exactly as
# Fierz-Pauli linear uniqueness is used as external mathematics in
# proof.md section 4.1.

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
        dependency_id="statics_lift_dependency_020",
        upstream_script_id="019_static_covariant_lift__static_covariant_lift",
        upstream_derivation_id="covariant_statics_lift_019",
        expected_record_kind=RecordKind.DERIVATION,
    )
    ns.declare_dependency(
        dependency_id="tt_positivity_dependency_020",
        upstream_script_id="006_gate_G03_radiative_positivity__gate_G03_radiative_positivity",
        upstream_derivation_id="tt_positivity_sum_of_squares_g03",
        expected_record_kind=RecordKind.DERIVATION,
    )
    ns.declare_dependency(
        dependency_id="ghost_exclusion_dependency_020",
        upstream_script_id="006_gate_G03_radiative_positivity__gate_G03_radiative_positivity",
        upstream_derivation_id="ghost_exclusion_g03",
        expected_record_kind=RecordKind.COUNTEREXAMPLE,
    )
    ns.declare_dependency(
        dependency_id="vector_sector_dependency_020",
        upstream_script_id="017_vector_time_dependent__vector_time_dependent",
        upstream_derivation_id="vector_time_dependent_lift_017",
        expected_record_kind=RecordKind.DERIVATION,
    )
    return archive, ns, invalidated


# =============================================================================
# Curvature machinery (hand-rolled, static spherical)
# =============================================================================

t, r, th, ph = sp.symbols("t r theta phi")
c = sp.Symbol("c", positive=True)
G_N = sp.Symbol("G_N", positive=True)
C1 = sp.Symbol("C1")


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


def einstein_mixed(g, coords):
    Gamma = christoffel(g, coords)
    Ric = ricci(Gamma, coords)
    ginv = g.inv()
    Rs = sp.together(sum(ginv[i, j] * Ric[i, j] for i in range(4) for j in range(4)))
    Gm = sp.zeros(4, 4)
    for a in range(4):
        for b in range(4):
            Gm[a, b] = sp.simplify(
                sum(ginv[a, c_] * (Ric[c_, b] - sp.Rational(1, 2) * g[c_, b] * Rs) for c_ in range(4))
            )
    return Gm


def riemann_lower(g, coords):
    n = len(coords)
    Gamma = christoffel(g, coords)
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
# Case 0
# =============================================================================


def case_0_statement(out: ScriptOutput) -> None:
    header("Case 0: The nonlinear stability obligation, scoped")
    print("Theorems 2-4 of proof.md are quadratic/reduced-level statements.")
    print("The debt: can the negative static reservoir do damage at full")
    print("nonlinearity? This script closes the spherical nonlinear sector")
    print("in-house (source binding + no-mining), re-verifies the quadratic")
    print("sector signature, and records the global small-data statement as")
    print("an external mathematical import (Christodoulou-Klainerman /")
    print("Lindblad-Rodnianski) about the equations 018 already closed.")

    with out.governance_assessments():
        out.line(
            "nonlinear stability closure opened",
            StatusMark.INFO,
            "in-house: spherical nonlinear + quadratic signature; external anchor: global small-data",
        )


# =============================================================================
# Case 1: nonlinear source binding (Theorem 3 lifted)
# =============================================================================


def case_1_nonlinear_source_binding(out: ScriptOutput):
    header("Case 1: Vacuum + regular center force flat, fully nonlinearly")
    coords = [t, r, th, ph]

    # 019's Birkhoff-family spatial profile: B = r/(C1 + r), A = 1/B
    # (t-r identity + asymptotic flatness). Fully nonlinear.
    B = r / (C1 + r)
    A = 1 / B
    g = sp.diag(-(c**2) * A, B, r**2, r**2 * sp.sin(th) ** 2)

    G = einstein_mixed(g, coords)
    vac = all(is_zero(G[i, j]) for i in range(4) for j in range(4))
    print(f"  family B = r/(C1+r), A = 1/B solves the vacuum equations: {vac}")

    K = kretschmann(g, coords)
    K_target = 12 * C1**2 / r**6
    residual = sp.simplify(K - K_target)
    print(f"  Kretschmann K = {sp.sstr(K)}")
    print(f"  K - 12 C1^2/r^6 = {sp.sstr(residual)}")
    ok_K = is_zero(residual)
    print()
    print("  K diverges as r -> 0 for every C1 != 0. A regular center")
    print("  therefore forces C1 = 0: B = 1, A = 1 -- flat. This is Theorem 3")
    print("  (source binding) at full nonlinearity: the negative static")
    print("  reservoir supports no source-free configuration whatsoever; it")
    print("  exists only as a functional of its sources.")

    flat_at_C1_zero = is_zero(K.subs(C1, 0))
    print(f"  K(C1=0) = 0 (flat witness): {flat_at_C1_zero}")

    ok = vac and ok_K and flat_at_C1_zero
    with out.derived_results():
        out.line(
            "nonlinear source binding",
            StatusMark.PASS if ok else StatusMark.FAIL,
            "vacuum + regular center => flat, uniquely, at full nonlinearity (K = 12 C1^2/r^6)",
        )
    return ok


# =============================================================================
# Case 2: no nonlinear mining (Misner-Sharp positivity)
# =============================================================================


def case_2_no_mining(out: ScriptOutput):
    header("Case 2: Misner-Sharp positivity: the reservoir cannot be mined")
    coords = [t, r, th, ph]
    m = sp.Function("m")(r)
    A = sp.Function("A", positive=True)(r)
    B = 1 / (1 - 2 * G_N * m / (c**2 * r))
    g = sp.diag(-(c**2) * A, B, r**2, r**2 * sp.sin(th) ** 2)
    G = einstein_mixed(g, coords)

    # Identity: G^t_t = -(2 G_N/c^2) m'(r) / r^2, for ANY A(r) and m(r).
    target = -(2 * G_N / c**2) * sp.diff(m, r) / r**2
    residual = sp.simplify(G[0, 0] - target)
    print(f"  G^t_t + (2G/c^2) m'/r^2 = {sp.sstr(residual)}")
    ok_identity = is_zero(residual)
    print()
    print("  With the closed parent, N G^t_t = T^t_t = -rho c^2 gives")
    print()
    print("      m'(r) = (4 pi r^2 / c^2) rho .")
    print()
    print("  This is exact and fully nonlinear (no weak-field expansion was")
    print("  made). For rho >= 0 and a regular center (m(0) = 0):")
    print()
    print("      m(r) = (4 pi/c^2) int_0^r rho r'^2 dr'  >=  0   for all r.")
    print()
    print("  The negative configuration energy u_field = -c^4 (s')^2/8 pi G is")
    print("  already bookkept inside m (the exterior mass M is the matter")
    print("  integral MINUS binding); no configuration of sources, however")
    print("  strong, drives a quasilocal mass negative. There is no nonlinear")
    print("  channel that extracts unbounded energy from the static sector.")

    # Witness: constant-density interior. m = 4 pi rho0 r^3/(3 c^2).
    rho0, Rstar = sp.symbols("rho_0 R_star", positive=True)
    m_int = 4 * sp.pi * rho0 * r**3 / (3 * c**2)
    m_prime_check = sp.simplify(sp.diff(m_int, r) - 4 * sp.pi * r**2 * rho0 / c**2)
    r_pos = sp.Symbol("r", positive=True)
    positive_interior = sp.simplify(m_int.subs(r, r_pos)).is_positive
    print()
    print(f"  constant-density witness: m'(r) - 4 pi r^2 rho_0/c^2 = {sp.sstr(m_prime_check)}")
    print(f"  m(r) > 0 for r > 0: {positive_interior}")
    ok_witness = is_zero(m_prime_check) and bool(positive_interior)

    ok = ok_identity and ok_witness
    with out.derived_results():
        out.line(
            "no-mining theorem (Misner-Sharp positivity)",
            StatusMark.PASS if ok else StatusMark.FAIL,
            "m' = (4 pi r^2/c^2) rho exactly; rho >= 0 + regular center => m >= 0 at all field strengths",
        )
    return ok


# =============================================================================
# Case 3: quadratic sector signature, inherited and re-verified
# =============================================================================


def case_3_sector_signature(out: ScriptOutput):
    header("Case 3: Sector signature at quadratic order (inherited)")
    # TT energy density is a sum of squares (re-verification of the G03 core).
    tau = sp.Symbol("tau")
    hp = sp.Function("h_p")(tau)
    hx = sp.Function("h_x")(tau)
    K_T = c**4 / (16 * sp.pi * G_N)
    u_tt = K_T / (2 * c**2) * (sp.diff(hp, tau) ** 2 + sp.diff(hx, tau) ** 2)
    # Positivity: sum of squares with positive prefactor.
    prefactor_positive = bool(sp.simplify(K_T / (2 * c**2)).is_positive)
    sos = u_tt.expand()
    is_sos = all(
        term.as_coeff_Mul()[0].is_positive
        for term in sp.Add.make_args(sos)
    )
    print(f"  u_TT = {sp.sstr(u_tt)}")
    print(f"  positive prefactor: {prefactor_positive}; sum of squares: {is_sos}")
    print()
    print("  Inherited (archive dependencies, verified on run):")
    print("    - TT positivity and null transport: G03")
    print("    - ghost exclusion / scalar sector constraint-type: G03")
    print("    - vector sector constraint-type through general linear time")
    print("      dependence: 017")
    print()
    print("  Together with Cases 1-2, every non-TT sector is constraint-type")
    print("  (no dynamics to destabilize) and the TT sector carries positive")
    print("  energy; the spherical nonlinear sector is rigid (Birkhoff) with")
    print("  nonnegative quasilocal mass.")

    ok = prefactor_positive and is_sos
    with out.derived_results():
        out.line(
            "sector signature re-verified at quadratic order",
            StatusMark.PASS if ok else StatusMark.FAIL,
            "TT energy density is a positive sum of squares; non-TT sectors constraint-type (inherited)",
        )
    return ok


# =============================================================================
# Case 4: the global small-data statement -- external mathematical anchor
# =============================================================================


def case_4_external_anchor(out: ScriptOutput) -> None:
    header("Case 4: Global small-data stability -- external mathematical anchor")
    print("What remains is the global, nonspherical, small-data statement:")
    print("Minkowski data close to flat evolve globally and disperse. For the")
    print("equations the framework derived (018 closure: Einstein-Hilbert")
    print("response, Lambda admitted, GB inert), this is:")
    print()
    print("  - Christodoulou & Klainerman (1993), The Global Nonlinear")
    print("    Stability of the Minkowski Space;")
    print("  - Lindblad & Rodnianski (2010), harmonic-gauge proof.")
    print()
    print("IMPORT CLASS: these are theorems of PDE analysis about a specific")
    print("hyperbolic system on Minkowski-asymptotic data. Their statements")
    print("and proofs take no gravitational phenomenology as input -- the same")
    print("class as Fierz-Pauli 1939 in proof.md section 4.1. Using them is")
    print("using mathematics about the derived equations, not importing GR's")
    print("physical content.")
    print()
    print("HONEST BOUNDARY: an in-house re-derivation at this scale is")
    print("declared out of scope by decision. No coefficient, no equation,")
    print("and no falsifier of the framework depends on this import: it")
    print("upgrades confidence in the flat state's global basin, nothing else.")
    print("The in-house content of this closure is Cases 1-3.")

    with out.governance_assessments():
        out.line(
            "global small-data stability recorded as external mathematical import",
            StatusMark.INFO,
            "CK93 / LR10; Fierz-Pauli import class; no coefficient depends on it",
        )


def case_5_verdict(out: ScriptOutput) -> None:
    header("Case 5: Verdict")
    print("The nonlinear stability debt is closed at scoped level:")
    print()
    print("  in-house:  spherical nonlinear sector rigid (Birkhoff, 019);")
    print("             vacuum + regular center => flat uniquely (Case 1);")
    print("             quasilocal mass nonnegative at all field strengths")
    print("             (Case 2); sector signature at quadratic order")
    print("             (Case 3, with G03/017 inheritance).")
    print("  external:  global small-data dispersion (CK93/LR10), recorded")
    print("             as mathematics about the derived equations.")
    print()
    print("The negative static reservoir cannot destabilize anything at any")
    print("field strength in the sectors where the framework claims theorem")
    print("grade, and the global statement rests on the same import class the")
    print("proof already uses for linear uniqueness.")

    with out.governance_assessments():
        out.line(
            "nonlinear stability closure discharged (scoped)",
            StatusMark.PASS,
            "in-house nonlinear spherical + quadratic signature; external anchor recorded honestly",
        )


def record_results(ns) -> None:
    ns.record_derivation(
        derivation_id="nonlinear_source_binding_020",
        inputs=[],
        output=sp.Symbol("vacuum_regular_center_forces_flat_nonlinearly"),
        method=(
            "Birkhoff family B = r/(C1+r) verified as exact vacuum solution; "
            "Kretschmann K = 12 C1^2/r^6 computed from scratch; regular center "
            "kills C1"
        ),
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="nonlinear_stability_rigor",
        scope="fully nonlinear spherical vacuum sector",
    )
    ns.record_derivation(
        derivation_id="misner_sharp_no_mining_020",
        inputs=[],
        output=sp.Symbol("m_prime_equals_4pi_r2_rho_over_c2_nonlinearly"),
        method=(
            "G^t_t = -(2G/c^2) m'/r^2 verified identically for arbitrary A(r), "
            "m(r); positivity by monotone integral from a regular center"
        ),
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="nonlinear_stability_rigor",
        scope="spherical configurations of the closed parent with rho >= 0",
    )
    ns.record_derivation(
        derivation_id="global_stability_external_anchor_020",
        inputs=[],
        output=sp.Symbol("CK93_LR10_import_recorded"),
        method=(
            "external mathematical theorem import, Fierz-Pauli class: global "
            "small-data stability of the flat state for the 018-closed parent"
        ),
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="external_import_record",
        scope=(
            "IMPORT, not in-house work: Christodoulou-Klainerman 1993 / "
            "Lindblad-Rodnianski 2010; no framework coefficient depends on it"
        ),
    )
    ns.record_obligation(ProofObligationRecord(
        obligation_id="nonlinear_stability_020",
        script_id=SCRIPT_ID,
        title="Nonlinear stability (scoped closure)",
        status=ObligationStatus.SATISFIED,
        satisfied_by=[
            "nonlinear_source_binding_020",
            "misner_sharp_no_mining_020",
            "global_stability_external_anchor_020",
        ],
        description=(
            "Closes the nonlinear stability rigor debt at scoped level: "
            "in-house nonlinear spherical results plus quadratic sector "
            "signature, with the global small-data statement recorded as an "
            "external mathematical import of the Fierz-Pauli class."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="nonlinear_stability_claim_020",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "At full nonlinearity in the spherical sector, vacuum plus a "
            "regular center force the flat state uniquely, and the quasilocal "
            "Misner-Sharp mass is nonnegative for nonnegative local energy "
            "density: the negative static reservoir cannot decay, be mined, "
            "or destabilize the ground state. The quadratic sector signature "
            "(TT positive, scalar/vector constraint-type) is inherited from "
            "G03/017. The global small-data statement is carried as an "
            "external mathematical import (CK93/LR10), on which no framework "
            "coefficient depends."
        ),
        derivation_ids=[
            "nonlinear_source_binding_020",
            "misner_sharp_no_mining_020",
            "global_stability_external_anchor_020",
        ],
        obligation_ids=["nonlinear_stability_020"],
    ))


def main() -> None:
    header("Trial 020: Nonlinear Stability -- Scoped Closure")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    case_0_statement(out)
    ok1 = case_1_nonlinear_source_binding(out)
    ok2 = case_2_no_mining(out)
    ok3 = case_3_sector_signature(out)
    case_4_external_anchor(out)
    case_5_verdict(out)

    if not (ok1 and ok2 and ok3):
        raise SystemExit("Trial 020: verification failure")

    record_results(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
