#!/usr/bin/env python3
"""
interior_cap_scale.py

Derivation 055: the interior cap scale from P10's compression limits.

The interior-cap lane stalled at derivations 025-028 with an honest
negative: exterior preservation does not derive a cap scale, imposed
strain bounds are hand-inserted, and compactness backsolves are
forbidden. The missing ingredient was microphysics. P10 supplies it,
and the bound comes from COMBINATORICS, not from an imported kappa_max:

  (1) THE COORDINATION FLOOR. An interior edge (hinge) of a 3D
      simplicial complex is shared by at least THREE cells. The
      deficit ladder delta(n) = 2 pi - n arccos(1/3) is strictly
      decreasing in n, so the deficit of a near-regular packing is
      BOUNDED ABOVE by
          delta_max = 2 pi - 3 arccos(1/3) = 2.590 rad (148.41 deg).
      No configuration of near-regular cells can concentrate more
      curvature on a hinge: the packing has a maximum sectional
      curvature.

  (2) THE CURVATURE CAP. By the Regge encoding (039), the local
      curvature is (2 x hinge-length-density x deficit); with the
      derived edge density c_e (052) and edge length a,
          R_max = 2 c_e delta_max / a^2
                = 144 theta3 (2 pi - 3 theta3) / (sqrt 2 pi a^2)
                = 51.67 / a^2        (theta3 = arccos(1/3)).
      Exact, a function of arccos(1/3) alone -- the same sole input
      as Delta_0, the mixtures, and c_e.

  (3) THE CAP RADIUS. Inside a Schwarzschild region the sectional
      curvature scale is sqrt(K) = 4 sqrt(3) G M/(c^2 r^3)
      (Kretschmann K = 48 G^2 M^2/(c^4 r^6)). The packing saturates
      at r_cap where this reaches R_max:
          r_cap = [4 sqrt(3) G M / (c^2 R_max)]^(1/3)
                = 0.4062 (r_s a^2)^(1/3)
      The (r_s a^2)^(1/3) scaling is the Planck-star scaling
      (Rovelli-Vidotto), here with a DERIVED coefficient.

  (4) THE CAP IS DEEP INSIDE THE HORIZON. For a solar-mass hole at
      Planck packing, r_cap ~ 4e-23 m ~ 1e-26 r_s: the exterior
      matching lemma (026) applies with room to spare, the exterior
      is exactly GR, and -- the observable face -- the A4 echo caveat
      RESOLVES TO A NULL: no echoes, for any astrophysical mass. The
      cap only reaches the horizon when r_s ~ a: the Planck-mass
      endpoint (a remnant-scale statement, recorded as an endpoint
      marker, not a claim about evaporation dynamics).

CONTRACT COMPLIANCE (the 025-028 contract, field by field):
  exterior data preserved: all (cap far inside horizon; matching
    lemma applies; fixed charges).
  matching rule: curvature-scale matching at r_cap (a SCALE
    identification; the junction/collapse dynamics is NOT solved and
    is opened as cap_junction_dynamics_055).
  bounded strain quantity: the hinge deficit (<= delta_max), hence
    sectional curvature (<= R_max).
  admissibility rule: the coordination floor n >= 3 (combinatorial,
    not imposed) + near-regular cells (the 050/052 mean-field class).
  derived scale: R_max = 51.67/a^2; r_cap = coeff (r_s a^2)^(1/3);
    all exact in arccos(1/3), one unknown (a) as everywhere.
  observable face: NO echoes (the caveat resolves); the exterior
    stays exactly GR (A4 sharpened, not weakened).
  kill/reroute: a confirmed echo from an astrophysical-mass merger
    kills this derivation's cap placement; a derived sub-horizon cap
    at LARGER radius would need new physics through the front door.

FENCES: near-regular mean-field (strained cells can trade deficit
against cell distortion -- the degenerate-cell witness in check 2
shows the trade exists; its energy cost makes it subleading for
f''> 0, stated not proven); static curvature matching only (no
collapse solution, no interior metric); a underived (results are
functions of a; Planck-a numbers marked as the standing assumption).
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
)


SCRIPT_PATH = Path(__file__).resolve()
SCRIPT_ID = f"{SCRIPT_PATH.parent.name}__{SCRIPT_PATH.stem}"
ARCHIVE_ROOT = SCRIPT_PATH.parents[1] / ".vacuumforge_archive"
REPO_ROOT = SCRIPT_PATH.parents[4]
REPORT_PATH = (REPO_ROOT / "theory_v3" / "development" / "vacuum_sector"
               / "07_interior_cap" / "interior_cap_scale_vacuumforge.md")

DEPENDENCIES = [
    ("edge_density_dep_055", "052_edge_density__edge_density", "edge_density_052"),
    ("bridge_dep_055", "039_regge_delaunay_bridge__regge_delaunay_bridge",
     "regge_delaunay_bridge_039"),
    ("matching_dep_055", "026_exterior_matching_lemma__exterior_matching_lemma",
     "exterior_matching_lemma_026"),
]

THETA3 = sp.acos(sp.Rational(1, 3))
L_PLANCK = 1.616e-35
G_N = 6.674e-11
C = 299792458.0
M_SUN = 1.989e30


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


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
    print("[INFO] Archive dependency check:")
    for check in checks:
        print(f"  - {check.dependency.dependency_id}: {check.status} ({check.message})")


def check_1_coordination_floor(failures):
    header("Check 1: the coordination floor bounds the deficit")
    deltas = {n: sp.simplify(2 * sp.pi - n * THETA3) for n in range(3, 8)}
    require("delta(n) strictly decreasing in n (each extra cell removes theta3)",
            all(float(deltas[n].evalf(50)) > float(deltas[n + 1].evalf(50))
                for n in range(3, 7)), failures)
    delta_max = deltas[3]
    dmax_num = float(delta_max.evalf(50))
    print(f"  delta_max = 2 pi - 3 arccos(1/3) = {dmax_num:.6f} rad "
          f"= {math.degrees(dmax_num):.2f} deg")
    require("delta_max = 2 pi - 3 arccos(1/3), positive and < 2 pi",
            0 < dmax_num < float((2 * sp.pi).evalf(50)), failures)
    print("  An interior hinge of a 3D simplicial complex is shared by at")
    print("  least three cells (two cells cannot close around an edge in an")
    print("  embedded complex). Near-regular cells therefore cannot put more")
    print("  than delta_max of deficit on any hinge: curvature concentration")
    print("  has a combinatorial ceiling. This is the admissibility rule the")
    print("  finite-strain probe (027) said was 'possible but absent' -- it")
    print("  was in the coordination number all along.")
    return delta_max


def check_2_degenerate_witness(failures):
    header("Check 2: the fence, witnessed -- strained cells can trade, at cost")
    # Cayley-Menger: 288 V^2 = CM determinant for a tetrahedron.
    def cm_det(d2):
        M = sp.Matrix([
            [0, 1, 1, 1, 1],
            [1, 0, d2[(0, 1)], d2[(0, 2)], d2[(0, 3)]],
            [1, d2[(0, 1)], 0, d2[(1, 2)], d2[(1, 3)]],
            [1, d2[(0, 2)], d2[(1, 2)], 0, d2[(2, 3)]],
            [1, d2[(0, 3)], d2[(1, 3)], d2[(2, 3)], 0],
        ])
        return M.det()

    reg = {p: 1 for p in [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]}
    det_reg = sp.simplify(cm_det(reg))
    require("regular unit tetrahedron: CM det = 4 (=> 288 V^2, V = sqrt(2)/12)",
            det_reg == 4, failures)
    # Degenerate witness: vertex 3 pushed into the plane of 0,1,2
    # (equilateral base, apex at centroid): distances to centroid = 1/sqrt(3).
    degen = dict(reg)
    for k in [(0, 3), (1, 3), (2, 3)]:
        degen[k] = sp.Rational(1, 3)
    det_degen = sp.simplify(cm_det(degen))
    require("flattened witness (apex in base plane): CM det = 0 exactly",
            det_degen == 0, failures)
    print("  Cells CAN flatten (dihedral -> pi), so three strained cells can")
    print("  close an edge with less deficit than delta_max -- the bound is a")
    print("  NEAR-REGULAR (mean-field) statement, the same class as 050/052.")
    print("  The trade costs cell-distortion energy (second-order stiff about")
    print("  the ground shape, 041 E3); for any f'' > 0 the near-regular")
    print("  bound is the energetically relevant one. Stated as the fence,")
    print("  not proven as a theorem: the degenerate direction is where a")
    print("  future refutation would enter.")


def check_3_curvature_cap_and_radius(delta_max, failures):
    header("Check 3: the maximum curvature and the cap radius")
    a = sp.Symbol("a", positive=True)
    c_e = 36 * THETA3 / (sp.sqrt(2) * sp.pi)
    # Regge encoding (039, 3D): sum_h ell_h delta_h = (1/2) Int R dV
    # => local R = 2 x (hinge length per volume) x delta = 2 (c_e/a^2) delta.
    R_max = sp.simplify(2 * c_e * delta_max / a**2)
    R_max_closed = sp.simplify(72 * THETA3 * (2 * sp.pi - 3 * THETA3)
                               / (sp.sqrt(2) * sp.pi * a**2))
    require("R_max = 2 c_e delta_max/a^2 = 72 theta3(2pi - 3 theta3)/(sqrt2 pi a^2) exactly",
            sp.simplify(R_max - R_max_closed) == 0, failures)
    chi = float((R_max * a**2).evalf(50))
    print(f"  R_max = {chi:.4f} / a^2   (exact in arccos(1/3))")
    require("dimensionless cap curvature chi in a sane window (30, 80)",
            30 < chi < 80, failures)

    # Schwarzschild interior curvature scale: sqrt(K) = 4 sqrt(3) GM/(c^2 r^3).
    r, M_, G_, c_ = sp.symbols("r M G c", positive=True)
    K = 48 * G_**2 * M_**2 / (c_**4 * r**6)
    sqrtK = sp.sqrt(K)
    r_cap = sp.solve(sp.Eq(sqrtK, R_max), r)[0]
    r_cap_closed = (4 * sp.sqrt(3) * G_ * M_ * a**2 / (c_**2 * chi)) ** sp.Rational(1, 3)
    require("r_cap = [4 sqrt3 GM a^2/(chi c^2)]^(1/3) (curvature-scale matching)",
            abs(float((r_cap / r_cap_closed).evalf(subs={G_: 1, M_: 1, c_: 1, a: 1}))
                - 1) < 1e-9, failures)
    # Express against r_s = 2GM/c^2:  r_cap = [2 sqrt3/chi]^(1/3) (r_s a^2)^(1/3).
    coeff = float((2 * sp.sqrt(3) / chi).evalf(50)) ** (1.0 / 3.0)
    print(f"  r_cap = {coeff:.4f} x (r_s a^2)^(1/3)   -- the Planck-star scaling,")
    print("  with the coefficient DERIVED (Rovelli-Vidotto posited r ~ (r_s l_P^2)^(1/3)).")
    require("coefficient of (r_s a^2)^(1/3) is O(0.1-1)", 0.1 < coeff < 1.0, failures)
    return chi, coeff


def check_4_placement_and_endpoint(chi, coeff, failures):
    header("Check 4: the cap is deep inside the horizon; the observable face is a null")
    a_num = L_PLANCK  # ASSUMPTION, marked: Planck packing
    rows = []
    for label, M in [("1 M_sun", M_SUN), ("10 M_sun", 10 * M_SUN),
                     ("Sgr A* (4e6 M_sun)", 4e6 * M_SUN)]:
        r_s = 2 * G_N * M / C**2
        r_cap = coeff * (r_s * a_num**2) ** (1.0 / 3.0)
        rows.append((label, r_s, r_cap, r_cap / r_s))
        print(f"    {label:22s}: r_s = {r_s:.3e} m, r_cap = {r_cap:.3e} m, "
              f"r_cap/r_s = {r_cap / r_s:.2e}")
    require("cap deep inside the horizon for all astrophysical masses (ratio < 1e-20)",
            all(rr < 1e-20 for _, _, _, rr in rows), failures)
    print("  The exterior matching lemma (026) applies with ~20+ orders of room:")
    print("  the exterior is exactly GR, and the A4 echo caveat RESOLVES TO A")
    print("  NULL -- no echoes, for any astrophysical mass. A confirmed echo")
    print("  now KILLS this cap placement (new falsifier face).")

    # Endpoint: cap meets horizon when r_cap = r_s => r_s = coeff^(3/2) a.
    r_s_end = coeff ** 1.5 * a_num
    M_end = C**2 * r_s_end / (2 * G_N)
    m_planck = 2.176e-8
    print(f"  endpoint: r_cap = r_s at r_s = {r_s_end:.3e} m "
          f"=> M = {M_end:.3e} kg = {M_end / m_planck:.3f} M_Planck")
    require("the cap-meets-horizon endpoint is Planck-scale (0.01-10 M_Planck)",
            0.01 < M_end / m_planck < 10, failures)
    print("  A remnant-scale endpoint marker: at ~0.1 M_Planck the cap and")
    print("  horizon coincide and the semiclassical picture ends. Recorded as")
    print("  a marker ONLY -- no evaporation dynamics is claimed.")
    return rows, M_end


def record(ns):
    ns.record_derivation(
        derivation_id="interior_cap_scale_055",
        inputs=[sp.Symbol("coordination_floor_n3"), sp.Symbol("edge_density_052"),
                sp.Symbol("regge_encoding_039"), sp.Symbol("exterior_matching_026")],
        output=sp.Symbol("R_max_51p67_over_a2_r_cap_planck_star_scaling_derived_coeff"),
        method=(
            "combinatorial deficit ceiling delta_max = 2 pi - 3 arccos(1/3) "
            "(coordination floor); R_max = 2 c_e delta_max/a^2 = 51.67/a^2 "
            "exact via the Regge encoding and derived edge density; "
            "curvature-scale matching against the Schwarzschild Kretschmann "
            "scale gives r_cap = 0.406 (r_s a^2)^(1/3); placement and "
            "Planck-mass endpoint computed; degenerate-cell fence witnessed "
            "via Cayley-Menger"
        ),
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="cap_scale_derivation",
        scope=(
            "near-regular mean-field bound (the 050/052 class; the "
            "degenerate-cell trade is the fence); static curvature-scale "
            "matching only -- junction/collapse dynamics NOT solved "
            "(cap_junction_dynamics_055); a underived, Planck-a numbers "
            "marked as assumption; exterior untouched by construction"
        ),
    )
    ns.record_obligation(ProofObligationRecord(
        obligation_id="cap_scale_derived_055",
        script_id=SCRIPT_ID,
        title="Interior cap scale DERIVED from P10's compression limits (mean-field)",
        status=ObligationStatus.SATISFIED,
        satisfied_by=["interior_cap_scale_055"],
        description=(
            "Resolves the finite-strain probe's missing bound (027): the "
            "admissibility rule is the coordination floor n >= 3, giving "
            "delta_max = 2.590 rad, R_max = 51.67/a^2, and r_cap = "
            "0.406 (r_s a^2)^(1/3) -- the Planck-star scaling with a derived "
            "coefficient, exact in arccos(1/3). Cap deep inside the horizon "
            "for all astrophysical masses; A4's echo caveat resolves to a "
            "null; Planck-mass endpoint marker recorded."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="cap_junction_dynamics_055",
        script_id=SCRIPT_ID,
        title="Cap junction and collapse dynamics (the contract's remaining fields)",
        status=ObligationStatus.OPEN,
        required_by=["interior_cap_scale_055"],
        description=(
            "The scale is derived; the interior METRIC is not: junction/"
            "source bookkeeping at r_cap, the capped interior solution, and "
            "the collapse dynamics remain open (joint with O-P10-4). Also "
            "open: the degenerate-cell trade's energetics (the fence) -- "
            "prove the near-regular bound is energetically enforced for "
            "f'' > 0 rather than stating it."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="interior_cap_claim_055",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "P10 bounds curvature combinatorially: an interior hinge carries "
            "at least three cells, so the near-regular deficit is at most "
            "2 pi - 3 arccos(1/3) and the sectional curvature at most "
            "R_max = 51.67/a^2. Matching the Schwarzschild interior "
            "curvature scale gives a capped core at r_cap = 0.406 "
            "(r_s a^2)^(1/3) -- the Planck-star scaling with a derived, "
            "parameter-free coefficient (given a). The cap sits ~26 orders "
            "inside a stellar-mass horizon: exteriors stay exactly GR, no "
            "echoes are predicted for any astrophysical mass (A4's caveat "
            "resolves to a null and a confirmed echo becomes a falsifier of "
            "the placement), and the cap meets the horizon only at the "
            "~0.1 Planck-mass endpoint. Fences: mean-field near-regular; "
            "scale only, no interior solution; a underived."
        ),
        derivation_ids=["interior_cap_scale_055"],
        obligation_ids=["cap_scale_derived_055"],
    ))


def write_report(chi, coeff, rows, M_end):
    rows_txt = "\n".join(
        f"    {label:22s} r_s = {rs:.3e} m   r_cap = {rc:.3e} m   "
        f"r_cap/r_s = {rr:.1e}" for label, rs, rc, rr in rows)
    md = f"""# The Interior Cap Scale from P10's Compression Limits -- VacuumForge Record

## Status

```text
result type:   cap-scale derivation, mean-field (2026-07-03,
               derivation 055)
conclusion:    the packing bounds curvature COMBINATORIALLY:
               delta_max = 2 pi - 3 arccos(1/3) (the coordination
               floor), R_max = 2 c_e delta_max/a^2 = {chi:.2f}/a^2,
               and curvature-scale matching gives
                   r_cap = {coeff:.3f} (r_s a^2)^(1/3)
               -- the Planck-star scaling with a DERIVED coefficient,
               exact in arccos(1/3), one unknown (a) as everywhere.
resolves:      the finite-strain probe's missing admissibility bound
               (027): it was the coordination number all along.
opens:         cap_junction_dynamics_055 (interior solution, junction
               bookkeeping, collapse dynamics; the fence's energetics)
verification:  vacuum_forge/src/vacuum_sector/055_interior_cap_scale/
```

## The Argument in Four Steps

```text
1. COORDINATION FLOOR: an interior hinge is shared by >= 3 cells;
   delta(n) decreasing => near-regular deficit <= 2 pi - 3 arccos(1/3)
   = 2.590 rad. Curvature concentration has a combinatorial ceiling.
2. CURVATURE CAP: Regge encoding (039) + derived edge density (052):
   R_max = 2 c_e delta_max / a^2 = {chi:.2f}/a^2.
3. CAP RADIUS: Schwarzschild interior curvature scale sqrt(K) =
   4 sqrt3 GM/(c^2 r^3) saturates R_max at
   r_cap = {coeff:.3f} (r_s a^2)^(1/3).
4. PLACEMENT (Planck packing, a = l_P -- the standing ASSUMPTION):
{rows_txt}
   Cap-meets-horizon endpoint: M ~ {M_end:.2e} kg ~ 0.1 M_Planck
   (marker only; no evaporation dynamics claimed).
```

## Contract Compliance (the 025-028 contract)

```text
exterior data preserved   all -- cap ~26 orders inside the horizon;
                          matching lemma (026) applies; charges fixed
matching rule             curvature-SCALE matching at r_cap (a scale
                          identification, not a junction solution)
bounded strain quantity   hinge deficit (<= delta_max) => sectional
                          curvature (<= R_max)
admissibility rule        the coordination floor n >= 3 --
                          combinatorial, NOT imposed -- plus the
                          near-regular mean-field class (050/052)
derived scale             R_max = {chi:.2f}/a^2; r_cap above; exact in
                          arccos(1/3); sole unknown a
observable face           A NULL: no echoes at any astrophysical mass
                          (register A4's caveat RESOLVES; a confirmed
                          echo now falsifies this placement)
kill/reroute              confirmed echoes kill the placement; a
                          larger-radius cap needs front-door physics
```

## Convergence Note

The (r_s a^2)^(1/3) core scaling is the Planck-star radius
(Rovelli & Vidotto 2014), reached there from loop-quantum-cosmology
bounce arguments. Here it drops out of tetrahedral combinatorics plus
the derived edge density, with the coefficient computed. Independent
routes to the same scaling deserve recording; neither validates the
other.

## Fences

```text
- NEAR-REGULAR MEAN-FIELD: strained cells can flatten (Cayley-Menger
  witness verified: apex-in-plane => det 0) and trade deficit against
  distortion; for f'' > 0 the trade costs energy and the near-regular
  bound should be the relevant one -- STATED, not proven (the open
  energetics face of cap_junction_dynamics_055).
- SCALE ONLY: no capped interior metric, no junction solution, no
  collapse dynamics. The contract's remaining fields stay open.
- a UNDERIVED: all physical numbers assume Planck packing and say so.
```

## Ledger

```text
derivation:  interior_cap_scale_055
satisfies:   cap_scale_derived_055 (the 027 missing bound)
opens:       cap_junction_dynamics_055
depends on:  edge_density_052, regge_delaunay_bridge_039,
             exterior_matching_lemma_026
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")
    print(f"[INFO] report written: {REPORT_PATH}")


def main() -> None:
    header("Derivation 055: The Interior Cap Scale from P10's Compression Limits")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    failures: list = []
    delta_max = check_1_coordination_floor(failures)
    check_2_degenerate_witness(failures)
    chi, coeff = check_3_curvature_cap_and_radius(delta_max, failures)
    rows, M_end = check_4_placement_and_endpoint(chi, coeff, failures)

    header("Verdict")
    if failures:
        for f in failures:
            print(f"  FAILED: {f}")
        raise SystemExit("Derivation 055: FAILED")
    print("  THE CAP SCALE IS DERIVED (mean-field): the coordination floor")
    print(f"  bounds curvature at R_max = {chi:.2f}/a^2, giving the Planck-star")
    print(f"  scaling r_cap = {coeff:.3f}(r_s a^2)^(1/3) with a computed")
    print("  coefficient. Cap deep inside every astrophysical horizon; the A4")
    print("  echo caveat resolves to a null; Planck-mass endpoint marked.")
    print("  Opened: junction/collapse dynamics + the fence's energetics.")

    record(ns)
    write_report(chi, coeff, rows, M_end)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
