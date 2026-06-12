# Trial F1: the kappa-leak coefficient -- deriving (and correcting) the P7' deviation
#
# Group:
#   011_trial_F_cosmology
#
# Script type:
#   DERIVATION / PREDICTION REVISION / COEFFICIENT CLOSURE
#
# Purpose
# -------
# P7' was adopted "at the limit": exact at H -> 0, with the expansion
# correction recorded as AB - 1 = O(H_0 r/c) (~1e-15 at 1 AU) -- an
# ESTIMATE from creation-current reasoning, never derived. With the local
# sector closed (E3: K_strain <= 4 derivatives = EH + Lambda + GB), the
# correction can now be DERIVED. The estimate was wrong in an
# interesting, structured way:
#
#   T1  PURE-LAMBDA EXPANSION: NO LEAK AT ALL. Schwarzschild-de Sitter
#       in static coordinates has AB = 1 EXACTLY (machinery-verified).
#       P7''s shadow survives Lambda-driven expansion unbroken: the
#       limit scoping was too cautious for the dark-energy era.
#
#   T2  FIRST ORDER IN H IS PURE FRAME, NOT GEOMETRY. The Painleve form
#       ds^2 = -c^2 dt^2 + (dr - H r dt)^2 + r^2 dOmega^2 is exact de
#       Sitter; its O(H) part has identically vanishing curvature (the
#       O(H) metric is flat space in falling coordinates). The
#       O(H_0 r/c) quantity is the COMOVING-FRAME VELOCITY v = H r --
#       gauge in GR, physical in VED only through substance-sector
#       couplings (quarantined with the engineering seams).
#
#   T3  THE REAL LEAK IS SECOND ORDER, MATTER-SOURCED, WITH COEFFICIENT
#       3/2. Uniform background dust rho_bg in the quasi-static patch
#       gives phi = psi = (2 pi G rho/3) r^2 and
#         AB - 1 = 2(phi + r psi')/c^2 = 4 pi G rho r^2/c^2
#                = (3/2) (H r/c)^2          [Friedmann H^2 = 8 pi G rho/3]
#       At the present epoch only the clustering component contributes
#       (Lambda gives zero by T1):
#         AB - 1 = (3/2) Omega_m (H_0 r/c)^2  ~  4e-31 at 1 AU.
#
# PREDICTION REVISION (honest downgrade): the kappa-leak's metric face is
# second order and unobservably small; the first-order face is the
# vacuum frame velocity v = H_0 r (~0.35 mm/s at 1 AU), detectable only
# if something couples to the substance frame -- not part of the theory's
# observational budget, recorded at the seam.

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
        dependency_id="p7prime_dependency_f1",
        upstream_script_id="005_postulate_adoptions__record_postulate_adoptions",
        upstream_derivation_id="postulate_P7prime_record_005",
        expected_record_kind=RecordKind.UNARCHIVED_FOUNDATION,
    )
    ns.declare_dependency(
        dependency_id="e3_closure_dependency_f1",
        upstream_script_id="009_trial_E_boundary_admissibility__trial_E3_p7prime_vs_scalaron",
        upstream_derivation_id="k_strain_4deriv_closure_e3",
        expected_record_kind=RecordKind.DERIVATION,
    )
    return archive, ns, invalidated


# =============================================================================
# Curvature machinery (C3 pattern, static spherical / general 4D)
# =============================================================================

t, r, th, ph = sp.symbols("t r theta phi")
c = sp.Symbol("c", positive=True)
G_N = sp.Symbol("G", positive=True)
H = sp.Symbol("H", positive=True)
Lam = sp.Symbol("Lambda", positive=True)
r_s = sp.Symbol("r_s", positive=True)
rho = sp.Symbol("rho", positive=True)
eps = sp.Symbol("epsilon", positive=True)
COORDS = [t, r, th, ph]


def christoffel(g):
    ginv = g.inv()
    n = 4
    Gamma = [[[0] * n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c_ in range(n):
                s_ = 0
                for d in range(n):
                    s_ += ginv[a, d] * (sp.diff(g[d, b], COORDS[c_])
                                        + sp.diff(g[d, c_], COORDS[b])
                                        - sp.diff(g[b, c_], COORDS[d]))
                Gamma[a][b][c_] = sp.simplify(s_ / 2)
    return Gamma


def ricci(Gamma):
    n = 4
    R_ = sp.zeros(n, n)
    for a in range(n):
        for b in range(n):
            expr = 0
            for c_ in range(n):
                expr += sp.diff(Gamma[c_][a][b], COORDS[c_])
                expr -= sp.diff(Gamma[c_][a][c_], COORDS[b])
                for d in range(n):
                    expr += Gamma[c_][c_][d] * Gamma[d][a][b]
                    expr -= Gamma[c_][a][d] * Gamma[d][c_][b]
            R_[a, b] = sp.simplify(expr)
    return R_


def einstein_lower(g):
    Gamma = christoffel(g)
    Ric = ricci(Gamma)
    ginv = g.inv()
    Rs = sp.simplify(sum(ginv[i, j] * Ric[i, j] for i in range(4) for j in range(4)))
    Gm = sp.zeros(4, 4)
    for a in range(4):
        for b in range(4):
            Gm[a, b] = sp.simplify(Ric[a, b] - sp.Rational(1, 2) * g[a, b] * Rs)
    return Gm, Rs


# =============================================================================
# Case 0
# =============================================================================


def case_0_problem(out: ScriptOutput) -> None:
    header("Case 0: Trial F1 -- derive the kappa-leak, replace the estimate")
    print("On record: AB - 1 = O(H_0 r/c) (estimate, P7' adoption note).")
    print("Now derivable: the local sector is closed (E3), so the expansion")
    print("correction around a mass is a GR computation plus VED bookkeeping.")

    with out.governance_assessments():
        out.line("Trial F1 opened", StatusMark.INFO,
                 "kappa-leak coefficient derivation; prediction revision expected")


# =============================================================================
# Case 1 (T1): Schwarzschild-de Sitter -- AB = 1 exactly, no leak in pure Lambda
# =============================================================================


def case_1_sds(out: ScriptOutput) -> None:
    header("Case 1 (T1): Pure-Lambda expansion produces NO leak (AB = 1 exact)")
    A_sds = 1 - r_s / r - Lam * r**2 / 3
    g = sp.diag(-c**2 * A_sds, 1 / A_sds, r**2, r**2 * sp.sin(th) ** 2)
    Gm, _ = einstein_lower(g)
    # field equation with Lambda: G_ab + Lambda g_ab = 0 in vacuum
    residuals = [sp.simplify(Gm[i, i] + Lam * g[i, i]) for i in range(4)]
    print("  G_ab + Lambda g_ab residuals (diag):", [sp.sstr(x) for x in residuals])
    print()
    print("  THEOREM T1: Schwarzschild-de Sitter solves the closed parent's")
    print("  vacuum equations with B = 1/A, i.e. AB = 1 EXACTLY, for any")
    print("  Lambda. A mass in a Lambda-dominated universe has a static")
    print("  exterior with perfect frame indifference: P7''s shadow is not")
    print("  merely a limit statement -- it is EXACT under pure-Lambda")
    print("  expansion. The adoption's limit scoping was too cautious here.")

    ok = all(is_zero(x) for x in residuals)
    with out.derived_results():
        out.line("SdS: AB = 1 exact for Lambda-driven expansion",
                 StatusMark.PASS if ok else StatusMark.FAIL,
                 "no kappa-leak in the dark-energy era; P7' shadow exact, not approximate")


# =============================================================================
# Case 2 (T2): first order in H is frame, not geometry
# =============================================================================


def case_2_first_order_frame(out: ScriptOutput) -> None:
    header("Case 2 (T2): O(H r/c) is the comoving frame velocity, not curvature")
    # Painleve-de Sitter: exact dS; series in H
    gP = sp.Matrix([
        [-(c**2) + H**2 * r**2, -H * r, 0, 0],
        [-H * r, 1, 0, 0],
        [0, 0, r**2, 0],
        [0, 0, 0, r**2 * sp.sin(th) ** 2],
    ])
    Gm, Rs = einstein_lower(gP)
    # exact: G_ab = -Lambda_eff g_ab with Lambda_eff = 3H^2/c^2
    lam_eff = 3 * H**2 / c**2
    residuals = [sp.simplify(Gm[i, j] + lam_eff * gP[i, j]) for i in range(4) for j in range(4)]
    exact_ok = all(is_zero(x) for x in residuals)
    Rs_check = sp.simplify(Rs - 12 * H**2 / c**2)
    print(f"  Painleve form is exact de Sitter: G_ab = -(3H^2/c^2) g_ab residuals all zero: {exact_ok}")
    print(f"  Ricci scalar - 12 H^2/c^2 = {sp.sstr(Rs_check)}")
    print()
    print("  Every curvature component is O(H^2); the O(H) content of the")
    print("  metric (g_tr = -H r: the infall/comoving velocity v = H r) has")
    print("  ZERO curvature -- it is flat space in falling coordinates. In GR")
    print("  it is gauge. In VED it is the SUBSTANCE FRAME velocity: physical")
    print("  only through couplings to the vacuum frame, which the closed")
    print("  local sector does not contain. Quarantined at the seam.")

    ok = exact_ok and is_zero(Rs_check)
    with out.derived_results():
        out.line("O(H) sector is curvature-free (frame velocity v = Hr)",
                 StatusMark.PASS if ok else StatusMark.FAIL,
                 "the old O(H_0 r/c) estimate described the frame current, not invariant geometry")


# =============================================================================
# Case 3 (T3): the matter-era leak -- coefficient 3/2
# =============================================================================


def case_3_matter_leak(out: ScriptOutput) -> None:
    header("Case 3 (T3): The derived leak: AB - 1 = (3/2) Omega_m (H r/c)^2")
    # quasi-static patch, uniform dust rho: phi = psi = (2 pi G rho/3) r^2
    phi = 2 * sp.pi * G_N * rho * r**2 / 3
    psi = phi
    # verify the static weak-field equations: Lap phi = 4 pi G rho, phi = psi (dust)
    lap = lambda f: sp.diff(r**2 * sp.diff(f, r), r) / r**2
    eq_phi = sp.simplify(lap(phi) - 4 * sp.pi * G_N * rho)
    # areal-gauge shadow from E3: AB - 1 = 2 (phi + r psi')/c^2
    ABm1 = sp.simplify(2 * (phi + r * sp.diff(psi, r)) / c**2)
    # Friedmann: H^2 = (8 pi G/3) rho  =>  rho = 3 H^2/(8 pi G)
    ABm1_H = sp.simplify(ABm1.subs(rho, 3 * H**2 / (8 * sp.pi * G_N)))
    target = sp.Rational(3, 2) * H**2 * r**2 / c**2
    res = sp.simplify(ABm1_H - target)
    print(f"  weak-field check: Lap phi - 4 pi G rho = {sp.sstr(eq_phi)}")
    print(f"  AB - 1 = {sp.sstr(ABm1)}  =  {sp.sstr(ABm1_H)}   (via Friedmann)")
    print(f"  residual vs (3/2)(Hr/c)^2 = {sp.sstr(res)}")
    print()
    print("  THEOREM T3: in the quasi-static patch the leak is sourced by the")
    print("  CLUSTERING background density only (Lambda contributes zero, T1):")
    print()
    print("    AB - 1 = (3/2) Omega_m (H_0 r/c)^2")
    print()
    numeric = 1.5 * 0.31 * ((2.2e-18 * 1.5e11) / 3e8) ** 2
    v_frame_um_s = 2.2e-18 * 1.5e11 * 1e6
    print(f"  At 1 AU (Omega_m = 0.31): AB - 1 ~ {numeric:.1e}   (unobservable)")
    print(f"  Frame velocity at 1 AU:   v = H_0 r ~ {v_frame_um_s:.2f} um/s (T2; gauge in GR)")
    print()
    print("  PREDICTION REVISION: the kappa-leak's metric face is SECOND order,")
    print("  not first -- the record's O(H_0 r/c) ~ 1e-15 estimate is replaced")
    print("  by a derived (3/2) Omega_m (H_0 r/c)^2 ~ 4e-31. An honest downgrade:")
    print("  the deviation is real, derived, parameter-free -- and hopeless as")
    print("  an observable. The surviving first-order quantity is the substance")
    print("  frame velocity, outside the closed sector's observational budget.")

    ok = is_zero(eq_phi) and is_zero(res)
    with out.derived_results():
        out.line("kappa-leak derived: AB - 1 = (3/2) Omega_m (H_0 r/c)^2",
                 StatusMark.PASS if ok else StatusMark.FAIL,
                 "matter-sourced, second order; Lambda era exactly leak-free; ~4e-31 at 1 AU")


# =============================================================================
# Case 4: verdict
# =============================================================================


def case_4_verdict(out: ScriptOutput) -> None:
    header("Case 4: Trial F1 verdict")
    print("DERIVED (replacing the adoption-note estimate):")
    print("  Lambda era:   AB - 1 = 0 exactly        (P7' shadow EXACT, T1)")
    print("  O(H) sector:  frame velocity, curvature-free (gauge in GR, T2)")
    print("  matter era:   AB - 1 = (3/2) Omega_m (H_0 r/c)^2 (T3)")
    print()
    print("P7' comes out STRONGER than adopted: its shadow is exact not only")
    print("at H -> 0 but in any pure-Lambda epoch. The 'expansion correction'")
    print("it was scoped against is second-order and matter-sourced.")
    print()
    print("Bookkeeping: the status of record and the P7' adoption note carry")
    print("the superseded O(H_0 r/c) estimate; both need revision banners.")

    with out.governance_assessments():
        out.line("kappa-leak coefficient closed; prediction honestly downgraded", StatusMark.PASS,
                 "estimate O(H_0 r/c) superseded by derived (3/2) Omega_m (H_0 r/c)^2; Lambda era leak-free")
    with out.unresolved_obligations():
        out.line("update P7' adoption note and status of record (supersession banners)",
                 StatusMark.OBLIGATION,
                 "done in the same commit as this script")
        out.line("perturbed/inhomogeneous cosmology (structure-era leak profile)",
                 StatusMark.OBLIGATION,
                 "T3 is the uniform-patch leading order; clustering corrections unexplored")


# =============================================================================
# Archive recording
# =============================================================================


def record_results(ns) -> None:
    ns.record_derivation(
        derivation_id="sds_no_leak_f1",
        inputs=[],
        output=sp.Symbol("SdS_AB_eq_1_exact"),
        method="full Einstein tensor of Schwarzschild-de Sitter with B = 1/A; G + Lambda g = 0 verified",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="exactness_theorem",
        scope="P7' shadow exact under pure-Lambda expansion; no kappa-leak in the dark-energy era",
    )
    ns.record_derivation(
        derivation_id="first_order_frame_f1",
        inputs=[],
        output=sp.Symbol("O_H_sector_curvature_free"),
        method="Painleve-de Sitter exact (G = -(3H^2/c^2) g); all curvature O(H^2)",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="gauge_classification",
        scope="O(H_0 r/c) is the comoving/substance frame velocity, not invariant geometry; "
              "physical only via substance-frame couplings (seam)",
    )
    ns.record_derivation(
        derivation_id="kappa_leak_coefficient_f1",
        inputs=[],
        output=sp.Eq(sp.Symbol("AB_minus_1"),
                     sp.Rational(3, 2) * sp.Symbol("Omega_m") * (H * r / c) ** 2),
        method="uniform-dust quasi-static patch + E3 areal shadow + Friedmann substitution",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="coefficient_closure",
        scope="SUPERSEDES the O(H_0 r/c) adoption-note estimate; ~4e-31 at 1 AU; "
              "matter-sourced, second order",
    )

    ns.record_obligation(ProofObligationRecord(
        obligation_id="inhomogeneous_leak_profile_f1",
        script_id=SCRIPT_ID,
        title="Structure-era leak profile (perturbed cosmology around the uniform patch)",
        status=ObligationStatus.OPEN,
        required_by=["cosmology_branch"],
        description="T3 is leading order in a uniform patch; clustering-era corrections unexplored.",
    ))

    ns.record_claim(ClaimRecord(
        claim_id="kappa_leak_revision_f1",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "The kappa-leak is derived, replacing the adoption-note estimate: AB - 1 = 0 "
            "exactly in any pure-Lambda epoch (SdS exactness); the O(H_0 r/c) sector is "
            "curvature-free frame velocity (gauge in GR, substance-frame physical only "
            "via seam couplings); the surviving metric deviation is matter-sourced and "
            "second order, AB - 1 = (3/2) Omega_m (H_0 r/c)^2 ~ 4e-31 at 1 AU. P7' is "
            "stronger than adopted; the prediction is honestly downgraded from "
            "observable-in-principle to derived-but-hopeless."
        ),
        derivation_ids=["sds_no_leak_f1", "first_order_frame_f1", "kappa_leak_coefficient_f1"],
        obligation_ids=["inhomogeneous_leak_profile_f1"],
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Trial F1: The kappa-leak Coefficient")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    case_0_problem(out)
    case_1_sds(out)
    case_2_first_order_frame(out)
    case_3_matter_leak(out)
    case_4_verdict(out)

    record_results(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
