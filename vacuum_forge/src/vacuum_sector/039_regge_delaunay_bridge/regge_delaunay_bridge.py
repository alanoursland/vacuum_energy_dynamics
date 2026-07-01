#!/usr/bin/env python3
"""
regge_delaunay_bridge.py

The Regge/Delaunay bridge: the packing model's first theorems.

The model (08_packing_microphysics/regge_delaunay_model.md): the vacuum
configuration variable X is a Delaunay-type graph -- vertices, edges with
lengths -- and curvature lives as wedge (hinge) deficits. The frustration
energy is E = sum_e l_e f(delta_e) for a smooth per-wedge energy f. This
is Regge calculus with a frustrated ground state.

Five results:

  1. DISCRETE GAUSS-BONNET (2D witness). On the icosahedron, the vertex
     deficits sum exactly to 4 pi = 2 pi chi(S^2): deficit-angle
     curvature satisfies the discrete Gauss-Bonnet theorem. (12 vertices
     x (2 pi - 5 pi/3) = 4 pi, exact.)

  2. EDGE LENGTHS ENCODE CURVATURE. For an equilateral geodesic triangle
     of side s on the unit sphere, the angle sum computed FROM THE EDGE
     LENGTHS ALONE (spherical law of cosines) exceeds pi by
     (sqrt(3)/4) s^2 + O(s^4) = K x (flat area). Curvature is readable
     off the graph's edge lengths -- the Delaunay intuition, made exact.

  3. REGGE = EH AT THE COARSEST TRIANGULATION. Triangulating S^3 (unit
     circumradius) by the 600-cell's 720 flat regular tetrahedra of
     chord edge 1/phi, every edge carries deficit Delta_0 =
     2 pi - 5 arccos(1/3) exactly, and the Regge action
     S_R = sum_e l_e delta_e = 720 Delta_0/phi reproduces the continuum
     (1/2) integral R sqrt(g) = 6 pi^2 to 3.5 percent:
     ratio = 120 Delta_0/(pi^2 phi) ~ 0.9647. The frustration deficit IS
     the discrete Einstein-Hilbert integrand.

  4. THE EXPANSION-POINT THEOREM (why EH is generic). Expanding
     E = sum_e l_e f(delta_e) about the frustrated ground state
     delta_e = Delta_0:

       E = [sum_e l_e] f(Delta_0)                    -> the FLOOR
                                                        (substance energy,
                                                        sequestered, 038)
         + f'(Delta_0) sum_e l_e (delta_e - Delta_0) -> the REGGE ACTION
                                                        (discrete EH)
         + (1/2) f''(Delta_0) sum_e l_e (...)^2      -> curvature-squared
                                                        class, suppressed
                                                        by a^2 K per order

     Because the ground state sits at NONZERO deficit, the linear term
     is generic: any smooth wedge energy with f'(Delta_0) != 0 yields
     Einstein-Hilbert at leading order in curvature perturbations
     (delta - Delta_0 ~ a^2 K). An unfrustrated packing (ground state at
     delta = 0, energy minimum there, f'(0) = 0) would instead yield
     curvature-squared gravity. GEOMETRIC FRUSTRATION IS WHY GRAVITY IS
     EINSTEIN-HILBERT rather than R^2 -- the answer to roadmap path 1C's
     weighting question, conditional on the packing reading.

  5. THE FLOOR-NEWTON LOCK. Eliminating the stiffness kappa_w between
     the 038 floor density and the EH coefficient: in the harmonic model
     f(delta) = (kappa_w/2)(delta - 2 pi/5)^2 ... the general statement
     uses f directly:
       rho_v = c_e f(Delta_0)/a^3        (038 floor)
       EH coefficient  proportional to f'(Delta_0)   (this derivation)
     For the harmonic wedge model, f(Delta_0) = (kappa_w/2) Delta_0^2 and
     f'(Delta_0) = kappa_w Delta_0, so

       rho_v = (c_e Delta_0 / (2 a^3)) x f'(Delta_0):

     the floor density and the gravitational coupling are LOCKED by the
     exact deficit and the packing scale -- one stiffness serves both.
     kappa_w is eliminated; the model has one fewer free constant.

Honest tension, recorded: the quadratic term is R^2-class with
Planck-scale coefficient (~a^2), while P7' as adopted forces a = 0
exactly. Either the packing's f'' contribution cancels/routes into the
constraint sector, or P7' is the a -> 0 idealization of a Planck-
suppressed (utterly unobservable, but nonzero) scalaron. Recorded as an
obligation, not resolved.

Output:
    theory_v3/development/vacuum_sector/08_packing_microphysics/regge_delaunay_bridge_vacuumforge.md
"""

import math
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
    / "08_packing_microphysics"
    / "regge_delaunay_bridge_vacuumforge.md"
)

DEPENDENCIES = [
    (
        "relief_geometry_dependency_039",
        "037_relief_exact_geometry__relief_exact_geometry",
        "relief_exact_geometry_037",
    ),
    (
        "substance_identity_dependency_039",
        "038_substance_ledger_identity__substance_ledger_identity",
        "substance_ledger_identity_038",
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
# Check 1: discrete Gauss-Bonnet on the icosahedron
# =============================================================================


def check_1_discrete_gauss_bonnet(failures):
    header("Check 1: icosahedron vertex deficits sum to 2 pi chi(S^2) = 4 pi")
    # Icosahedron: 12 vertices, 5 equilateral triangles (angle pi/3) per vertex.
    vertex_deficit = 2 * sp.pi - 5 * (sp.pi / 3)
    total = 12 * vertex_deficit
    require("per-vertex deficit = pi/3 exactly",
            is_zero(sp.simplify(vertex_deficit - sp.pi / 3)), failures)
    require("sum of deficits = 4 pi = 2 pi chi(S^2) exactly",
            is_zero(sp.simplify(total - 4 * sp.pi)), failures)
    print()
    print("  Deficit-angle curvature obeys the discrete Gauss-Bonnet theorem:")
    print("  concentrated curvature on the graph's hinges carries the same")
    print("  topological content as the continuum integrand. This is the 2D")
    print("  anchor of the Regge correspondence the model builds on.")


# =============================================================================
# Check 2: edge lengths encode curvature (the Delaunay intuition)
# =============================================================================


def check_2_edge_length_encoding(failures):
    header("Check 2: angle excess from edge lengths = K x area + O(s^4)")
    s = sp.Symbol("s", positive=True)
    # Angle of an equilateral spherical triangle from its side length alone.
    alpha = sp.acos(sp.cos(s) / (1 + sp.cos(s)))
    excess = 3 * alpha - sp.pi
    series = sp.series(excess, s, 0, 4).removeO()
    flat_area = sp.sqrt(3) / 4 * s**2  # K = 1 on the unit sphere
    require("excess = (sqrt(3)/4) s^2 + O(s^4), i.e. = K x flat area",
            is_zero(sp.simplify(series - flat_area)), failures)
    print(f"  3 alpha(s) - pi = {sp.sstr(sp.simplify(series))} + O(s^4)")
    print()
    print("  Curvature is measurable from the graph's edge lengths alone: a")
    print("  triangle's angle sum, computed purely from its side lengths,")
    print("  exceeds the flat value by curvature times area. 'Different edge")
    print("  lengths representing curvature' -- the Delaunay graph intuition --")
    print("  is exact at leading order, with O(s^4) discretization error.")


# =============================================================================
# Check 3: Regge = EH on the 600-cell triangulation of S^3
# =============================================================================


def check_3_regge_eh_600cell(failures):
    header("Check 3: 600-cell Regge action vs continuum EH on S^3")
    phi = (1 + sp.sqrt(5)) / 2
    Delta0 = 2 * sp.pi - 5 * sp.acos(sp.Rational(1, 3))

    # 600-cell (unit circumradius): 720 edges, chord edge length 1/phi,
    # 5 flat regular tetrahedra around every edge => deficit Delta_0 each.
    S_regge = 720 * (1 / phi) * Delta0

    # Continuum: (1/2) int R sqrt(g) over unit S^3: R = 6, Vol = 2 pi^2.
    S_continuum = sp.Rational(1, 2) * 6 * 2 * sp.pi**2  # = 6 pi^2

    ratio = sp.simplify(S_regge / S_continuum)
    ratio_val = float(ratio)
    print(f"  S_Regge      = 720 Delta_0/phi = {float(S_regge):.4f}")
    print(f"  (1/2) int R  = 6 pi^2          = {float(S_continuum):.4f}")
    print(f"  ratio        = 120 Delta_0/(pi^2 phi) = {ratio_val:.4f}")
    require("ratio equals 120 Delta_0/(pi^2 phi) exactly",
            is_zero(sp.simplify(ratio - 120 * Delta0 / (sp.pi**2 * phi))), failures)
    require("coarsest-possible triangulation reproduces EH within 4 percent",
            0.96 < ratio_val < 1.0, failures)
    print()
    print("  The frustration deficit Delta_0 -- the same exact number that is")
    print("  the floor's geometric seed (037, 038) -- times the 600-cell's")
    print("  edge skeleton IS the discrete Einstein-Hilbert action of the")
    print("  3-sphere, to 3.5 percent at the coarsest triangulation that")
    print("  exists. (Regge convergence theory closes the gap under")
    print("  refinement; that continuum-limit lift is the recorded open")
    print("  obligation, not claimed here.)")


# =============================================================================
# Check 4: the expansion-point theorem (why EH is generic)
# =============================================================================


def check_4_expansion_point(failures):
    header("Check 4: frustration makes the linear (Regge/EH) term generic")
    f = sp.Function("f")
    Delta0, x, a_len, K = sp.symbols("Delta_0 x a K", positive=True)
    eps = sp.Symbol("epsilon")  # delta_e - Delta_0, the curvature perturbation

    # Taylor structure of the wedge energy about the frustrated ground state.
    expansion = sp.series(f(Delta0 + eps), eps, 0, 3).removeO()
    const_term = expansion.coeff(eps, 0)
    lin_coeff = expansion.coeff(eps, 1)
    quad_coeff = expansion.coeff(eps, 2)
    require("constant term = f(Delta_0) (the floor / substance energy)",
            is_zero(sp.simplify(const_term - f(Delta0))), failures)
    require("linear coefficient = f'(Delta_0) (the Regge/EH weighting)",
            is_zero(sp.simplify(lin_coeff - f(Delta0).diff(Delta0))), failures)
    require("quadratic coefficient = f''(Delta_0)/2 (curvature-squared class)",
            is_zero(sp.simplify(quad_coeff - f(Delta0).diff(Delta0, 2) / 2)), failures)

    # Curvature perturbation scaling: delta - Delta_0 ~ a^2 K (check 2's
    # excess scaling on hinges). Term ratio quadratic/linear:
    sub = a_len**2 * K
    lin_term = lin_coeff * sub
    quad_term = quad_coeff * sub**2
    suppression = sp.simplify(quad_term / lin_term)
    target = sp.simplify(f(Delta0).diff(Delta0, 2) / (2 * f(Delta0).diff(Delta0)) * a_len**2 * K)
    require("quadratic/linear ratio = (f''/2f') a^2 K: R^2-class is a^2-suppressed",
            is_zero(sp.simplify(suppression - target)), failures)

    # The unfrustrated contrast: ground state at delta = 0 with f'(0) = 0
    # (a minimum at zero deficit) has NO linear term: leading action is
    # quadratic in deficit = curvature-squared gravity.
    g_quad = sp.Rational(1, 2) * sp.Symbol("kappa_w", positive=True) * x**2  # f = k x^2/2
    lin_at_zero = sp.diff(g_quad, x).subs(x, 0)
    require("unfrustrated packing (minimum at delta = 0) has f'(0) = 0: no EH term",
            is_zero(lin_at_zero), failures)
    print()
    print("  THE RESULT: expanding any smooth wedge energy about the ground")
    print("  state, the linear-in-deficit (Regge -> Einstein-Hilbert) term")
    print("  has coefficient f'(ground). A frustrated ground state sits at")
    print("  NONZERO deficit Delta_0, where generically f'(Delta_0) != 0:")
    print("  EH gravity is the generic leading response. An unfrustrated")
    print("  packing would sit at its energy minimum delta = 0, where f' = 0")
    print("  necessarily: its leading response would be curvature-squared.")
    print()
    print("  Geometric frustration is WHY gravity is Einstein-Hilbert.")
    print("  This answers roadmap path 1C's weighting question (linear")
    print("  deficit vs squared mismatch): the frustrated expansion point")
    print("  supplies the linear weighting -- conditional on the packing")
    print("  reading, stated as such. The R^2-class correction is")
    print("  a^2-suppressed (Planck-scale), recorded against P7' as an")
    print("  honest tension, not resolved here.")


# =============================================================================
# Check 5: the floor-Newton lock
# =============================================================================


def check_5_floor_newton_lock(failures):
    header("Check 5: one stiffness serves both the floor and Newton's constant")
    kappa_w, a_len, c_e = sp.symbols("kappa_w a c_e", positive=True)
    Delta0 = 2 * sp.pi - 5 * sp.acos(sp.Rational(1, 3))

    f_harm = kappa_w / 2 * Delta0**2          # f(Delta_0), harmonic wedge model
    fprime_harm = kappa_w * Delta0            # f'(Delta_0)

    rho_v = c_e * f_harm / a_len**3           # 038 floor density
    lock = sp.simplify(rho_v - (c_e * Delta0 / (2 * a_len**3)) * fprime_harm)
    require("rho_v = (c_e Delta_0/(2 a^3)) f'(Delta_0): kappa_w eliminated",
            is_zero(lock), failures)
    print()
    print("  The same stiffness kappa_w sets both the floor density (through")
    print("  f(Delta_0), sequestered) and the gravitational coupling (through")
    print("  f'(Delta_0), the Regge/EH coefficient). Eliminating it locks")
    print("  them together with only the exact deficit and the packing scale:")
    print()
    print("      rho_v = (c_e Delta_0 / 2 a^3) x [EH coefficient].")
    print()
    print("  The model has one fewer free constant than it appears to: the")
    print("  substance energy of the vacuum and the strength of gravity are")
    print("  two readings of one wedge energy. With the EH coefficient")
    print("  anchored by Newton's G and a at the Planck scale, rho_v is")
    print("  Planckian -- and sequestered (038), so no observational conflict:")
    print("  gravity never sees it.")


# =============================================================================
# Report and archive
# =============================================================================


def write_report():
    md = """# VacuumForge: The Regge/Delaunay Bridge (packing microphysics, phase 1)

## Purpose

First theorems of the packing-microphysics program
(`regge_delaunay_model.md`): the Delaunay graph model's curvature
encoding, its correspondence with Regge calculus, and the
expansion-point theorem that makes Einstein-Hilbert the generic
gravitational response of a frustrated packing.

## Verified Results

```text
1. Discrete Gauss-Bonnet (2D anchor): icosahedron vertex deficits sum
   to 4 pi = 2 pi chi(S^2), exactly.

2. Edge lengths encode curvature: for an equilateral geodesic triangle
   of side s on the unit sphere, the angle sum computed from edge
   lengths alone exceeds pi by (sqrt(3)/4) s^2 + O(s^4) = K x area.
   The Delaunay intuition is exact at leading order.

3. Regge = EH at the coarsest triangulation: the 600-cell's 720 edges,
   each of chord length 1/phi with deficit exactly Delta_0
   = 2 pi - 5 arccos(1/3), give S_Regge = 720 Delta_0/phi
   = 0.9647 x (1/2) int R sqrt(g) on unit S^3. The frustration deficit
   IS the discrete EH integrand, within 3.5 percent at the coarsest
   possible mesh.

4. The expansion-point theorem: E = sum_e l_e f(delta_e) about the
   frustrated ground state delta = Delta_0 splits as
     floor (f(Delta_0): substance energy, sequestered, 038)
     + f'(Delta_0) x Regge action (discrete EH)
     + (f''/2) x curvature-squared class, suppressed by a^2 K.
   A frustrated ground state has f'(Delta_0) != 0 generically: EH is
   the generic leading response. An unfrustrated packing (minimum at
   delta = 0) has f'(0) = 0 necessarily: it would yield R^2 gravity.
   GEOMETRIC FRUSTRATION IS WHY GRAVITY IS EINSTEIN-HILBERT --
   the answer to roadmap path 1C's weighting question, conditional on
   the packing reading.

5. The floor-Newton lock: rho_v = (c_e Delta_0/(2 a^3)) f'(Delta_0) --
   the stiffness kappa_w is eliminated between the floor density and
   the EH coefficient. The vacuum's substance energy and the strength
   of gravity are two readings of one wedge energy.
```

## Classification

```text
result type: model-definition theorems + the expansion-point result
scope:       exact discrete geometry (checks 1-3, 5) and Taylor
             structure (check 4); the continuum limit of the Regge
             action and the 4D/Lorentzian lift are NOT proved here;
             the packing reading of P4/P5 remains a candidate ontology
conclusion:  the Delaunay/Regge model encodes curvature in edge data
             exactly; the frustrated expansion point makes EH the
             generic gravitational response and locks the floor density
             to the gravitational coupling
non-conclusion: no continuum-limit theorem; no Lorentzian/4D lift; the
             a^2-suppressed R^2 correction stands in recorded tension
             with exact P7'; nothing observational is claimed
```

## Honest Tension (recorded)

The quadratic term of the expansion is R^2-class with Planck-scale
coefficient (~a^2). P7' as adopted forces the four-derivative sector
exactly empty. Either the packing's f'' contribution cancels or routes
into the constraint sector (to be shown), or P7' is the a -> 0
idealization of a Planck-suppressed scalaron (unobservable at any
achievable range, but structurally nonzero). This is
`p7prime_packing_tension_039`, open. It moves no closed coefficient --
the tension lives entirely at Planck scale -- but honesty requires it
on the books.

## Newly Opened Obligations

```text
regge_continuum_limit_039:   lift check 3 from the coarsest-mesh data
                             point to a refinement/convergence theorem
                             (Regge convergence class), then to the
                             4D/Lorentzian statement.
p7prime_packing_tension_039: resolve the a^2-suppressed R^2 term
                             against exact P7' (cancellation, routing,
                             or scoped idealization).
(inherited) packing_stiffness_microphysics_038: now reduced by one
                             constant (kappa_w eliminated); remaining:
                             a, c_e.
```

## Verification

```text
vacuum_forge/src/vacuum_sector/039_regge_delaunay_bridge/regge_delaunay_bridge.py
```

Archive record: `regge_delaunay_bridge_039`.
"""
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(md, encoding="utf-8")
    print(f"[INFO] report written: {REPORT_PATH}")


def record_archive(ns):
    ns.record_derivation(
        derivation_id="regge_delaunay_bridge_039",
        inputs=[
            sp.Symbol("relief_exact_geometry_result"),
            sp.Symbol("substance_ledger_identity_result"),
        ],
        output=sp.Symbol("frustrated_expansion_point_makes_EH_generic_floor_newton_locked"),
        method=(
            "exact discrete Gauss-Bonnet on the icosahedron; edge-length "
            "curvature series; 600-cell Regge-vs-continuum EH comparison; "
            "Taylor structure of the wedge energy about the frustrated ground "
            "state with suppression bookkeeping; stiffness elimination between "
            "floor density and EH coefficient"
        ),
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="model_definition_theorems",
        scope=(
            "exact discrete geometry and Taylor structure; continuum limit and "
            "4D/Lorentzian lift open; packing reading remains candidate ontology"
        ),
    )
    ns.record_obligation(ProofObligationRecord(
        obligation_id="regge_continuum_limit_039",
        script_id=SCRIPT_ID,
        title="Continuum limit and 4D lift of the Regge correspondence",
        status=ObligationStatus.OPEN,
        required_by=["regge_delaunay_bridge_039"],
        description=(
            "Lift the coarsest-mesh 600-cell data point to a refinement/"
            "convergence statement and the 4D/Lorentzian form."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="p7prime_packing_tension_039",
        script_id=SCRIPT_ID,
        title="Resolve the a^2-suppressed R^2 term against exact P7'",
        status=ObligationStatus.OPEN,
        required_by=["regge_delaunay_bridge_039"],
        description=(
            "The expansion's quadratic term is Planck-suppressed R^2-class; "
            "P7' forces the four-derivative sector exactly empty. Show "
            "cancellation/routing, or record P7' as the a -> 0 idealization. "
            "No closed coefficient moves either way."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="regge_delaunay_bridge_claim_039",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "In the Delaunay/Regge packing model, curvature is exactly "
            "encoded in edge data (discrete Gauss-Bonnet; angle excess = "
            "K x area from edge lengths), the 600-cell's frustration deficit "
            "reproduces the Einstein-Hilbert action of S^3 to 3.5 percent at "
            "the coarsest mesh, and the expansion of any smooth wedge energy "
            "about the frustrated ground state yields: the sequestered floor "
            "(constant), the Regge/EH action (linear, generic because "
            "f'(Delta_0) != 0 at a frustrated point), and a^2-suppressed "
            "R^2-class corrections. Geometric frustration is why the "
            "gravitational response is Einstein-Hilbert rather than "
            "curvature-squared -- conditional on the packing reading. The "
            "floor density and the EH coefficient are locked: "
            "rho_v = (c_e Delta_0/2a^3) f'(Delta_0), eliminating kappa_w."
        ),
        derivation_ids=["regge_delaunay_bridge_039"],
        obligation_ids=[
            "regge_continuum_limit_039",
            "p7prime_packing_tension_039",
        ],
    ))


def main() -> None:
    header("Derivation 039: The Regge/Delaunay Bridge")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    failures: list = []
    check_1_discrete_gauss_bonnet(failures)
    check_2_edge_length_encoding(failures)
    check_3_regge_eh_600cell(failures)
    check_4_expansion_point(failures)
    check_5_floor_newton_lock(failures)

    header("Verdict")
    if failures:
        for f in failures:
            print(f"  FAILED: {f}")
        raise SystemExit("Derivation 039: verification failure")
    print("  The packing model's first theorems are in place: edge data")
    print("  encodes curvature exactly, the frustration deficit is the")
    print("  discrete EH integrand, the frustrated expansion point makes EH")
    print("  generic (roadmap 1C answered, conditionally), and the floor and")
    print("  Newton's constant are locked by one wedge energy. Open:")
    print("  continuum limit, 4D lift, and the P7' tension.")

    write_report()
    record_archive(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
