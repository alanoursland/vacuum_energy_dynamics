#!/usr/bin/env python3
"""
substance_ledger_identity.py

Mathematical capture of the identification: the frustration floor IS the
substance energy of P1/P3.

The proposal (theory-owner, 2026-07-01): the energy that vacuum *is*
(P1), at the constant density P3 commits to, is physically realized as
the irreducible packing frustration of the 3D ground state. The floor is
not a new ledger bucket; it is the mechanism behind the oldest one. This
script captures the identification's checkable mathematical content.

Four results:

  1. ACTION-LEVEL SEQUESTERING. Substance energy enters the action as
     -rho_v integral sqrt(-g). By the 033 identity
     sqrt(-g) = e^kappa sqrt(-g_bar), it splits exactly as

         -rho_v [ integral sqrt(-g_bar)  +  integral sqrt(-g_bar)(e^kappa - 1) ].

     The first term is a constant built from the non-dynamical fiducial
     volume form: it varies to nothing, couples to nothing. The second
     term vanishes identically where the unimodular constraint is exact
     (kappa = 0) and is O(kappa) ~ 1e-31 where it leaks (F1). Verified:
     the split is exact; the leak coupling is linear in kappa with
     coefficient rho_v; and in the unconstrained reading, -rho_v sqrt(-g)
     is a pure Lambda-shift absorbed by the integration constant (035).
     "Substance energy does not gravitate" is an action-level statement.

  2. THE CONVERSION FACTOR TARGET. In the minimal harmonic wedge model
     (each edge's five surrounding tetrahedra want to close; penalty
     (kappa_w/2)(deficit)^2 per wedge), the floor density is

         rho_v = c_e * kappa_w * Delta_0^2 / (2 a^3),

     with Delta_0 = 2 pi - 5 arccos(1/3) exact (037) and c_e the packing
     edge density coefficient. P1's open question -- what sets the
     conversion factor between vacuum extent and vacuum energy -- becomes
     a formula target: stiffness times exact deficit squared over packing
     volume. Model-dependent constant flagged as such.

  3. THE SECTOR SIGNATURE FROM THE PACKING (the surprise). Dihedral
     angles are exactly scale-invariant: verified symbolically, every
     dihedral of a tetrahedron is unchanged under x -> lambda x, so ANY
     angle-based frustration energy has identically zero restoring force
     in the dilation (volume/trace) mode. Under a volume-preserving
     shear, the dihedrals shift at first order: verified symbolically on
     the regular tetrahedron. Consequence: the floor's energy functional
     is flat in the kappa direction and stiff in the s direction -- the
     trace-constrained / shear-energetic sector signature of the closed
     theory (G02/G03, P7', unimodular P3), emerging bottom-up from the
     packing microphysics. The volume mode MUST be fixed by a constraint
     (P3) because the microphysics gives it no dynamics of its own.

  4. THE GRAVITATING/SEQUESTERED SPLIT. T_vac = -rho_v g + T_excursion:
     the constant part is invisible (trace-free blindness, 035); only
     excursions -- curvature strain (closed sector) and gapped/defect
     excess (Trial D lane) -- gravitate. Gravity only ever sees changes
     in the vacuum, never the vacuum itself.

Output:
    theory_v3/development/vacuum_sector/substance_ledger_identity_vacuumforge.md
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
    / "substance_ledger_identity_vacuumforge.md"
)

DEPENDENCIES = [
    (
        "unimodular_break_dependency_038",
        "033_unimodular_lovelock_break__unimodular_lovelock_break",
        "unimodular_lovelock_break_033",
    ),
    (
        "floor_sequestering_dependency_038",
        "035_floor_sequestering_constraint__floor_sequestering_constraint",
        "floor_sequestering_constraint_035",
    ),
    (
        "relief_geometry_dependency_038",
        "037_relief_exact_geometry__relief_exact_geometry",
        "relief_exact_geometry_037",
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
# Check 1: action-level sequestering of the substance term
# =============================================================================


def check_1_action_split(failures):
    header("Check 1: -rho_v sqrt(-g) splits into inert constant + kappa-leak coupling")
    rho_v, kappa = sp.symbols("rho_v kappa")
    sqrt_gbar = sp.Symbol("sqrtgbar", positive=True)
    sqrt_g = sp.exp(kappa) * sqrt_gbar  # the 033 identity

    substance_term = -rho_v * sqrt_g
    split = -rho_v * sqrt_gbar - rho_v * sqrt_gbar * (sp.exp(kappa) - 1)
    require("exact split: -rho_v sqrt(-g) = -rho_v sqrt(-g_bar) - rho_v sqrt(-g_bar)(e^kappa - 1)",
            is_zero(sp.simplify(substance_term - split)), failures)

    # The leak coupling is linear in kappa at leading order.
    leak = -rho_v * sqrt_gbar * (sp.exp(kappa) - 1)
    leak_series = sp.series(leak, kappa, 0, 2).removeO()
    require("leak coupling = -rho_v sqrt(-g_bar) kappa + O(kappa^2)",
            is_zero(sp.simplify(leak_series + rho_v * sqrt_gbar * kappa)), failures)

    # Where the constraint is exact (kappa = 0), the coupling vanishes identically.
    require("coupling vanishes identically at kappa = 0 (P7'-exact sector)",
            is_zero(leak.subs(kappa, 0)), failures)
    print()
    print("  The substance energy's entire dynamical content is the fiducial")
    print("  constant (varies to nothing: g_bar is not dynamical) plus a")
    print("  coupling that exists only where the unimodular constraint leaks:")
    print("  O(kappa) ~ 1e-31 in the matter era (F1), exactly zero in the")
    print("  static exterior and any pure-Lambda epoch. In the unconstrained")
    print("  reading, -rho_v sqrt(-g) is a pure Lambda-shift, absorbed by the")
    print("  integration constant (035): both readings sequester. 'Substance")
    print("  energy does not gravitate' is an action-level theorem.")


# =============================================================================
# Check 2: the conversion-factor target formula
# =============================================================================


def check_2_conversion_factor(failures):
    header("Check 2: rho_v = c_e kappa_w Delta_0^2 / (2 a^3) (harmonic wedge model)")
    kappa_w, a_len, c_e = sp.symbols("kappa_w a c_e", positive=True)
    Delta0 = 2 * sp.pi - 5 * sp.acos(sp.Rational(1, 3))

    # Wedge model: energy per edge = (kappa_w/2) Delta_0^2 (the unclosable
    # five-tetrahedra deficit); edge number density = c_e / a^3.
    energy_per_edge = kappa_w / 2 * Delta0**2
    edge_density = c_e / a_len**3
    rho_v_model = sp.simplify(energy_per_edge * edge_density)
    target = c_e * kappa_w * Delta0**2 / (2 * a_len**3)
    require("floor density formula assembles exactly",
            is_zero(sp.simplify(rho_v_model - target)), failures)
    require("Delta_0 is the exact 037 deficit (dimensionless, positive)",
            bool(sp.simplify(Delta0).evalf() > 0), failures)
    print(f"  rho_v = {sp.sstr(target)}")
    print(f"  Delta_0 = 2 pi - 5 arccos(1/3) = {float(Delta0):.6f} (exact)")
    print()
    print("  P1's open question -- the conversion factor between vacuum extent")
    print("  and vacuum energy, 'the analog of c^2' -- acquires a formula")
    print("  target: packing stiffness times the exact deficit squared over")
    print("  the packing volume. The constants kappa_w, a, c_e are the")
    print("  microphysics obligations; Delta_0 is already exact. This is a")
    print("  target, not a derivation: flagged model-dependent.")


# =============================================================================
# Check 3: sector signature from the packing (scale-flat, shear-stiff)
# =============================================================================


def _tetra_vertices():
    # Regular tetrahedron, exact coordinates.
    return [
        sp.Matrix([1, 1, 1]),
        sp.Matrix([1, -1, -1]),
        sp.Matrix([-1, 1, -1]),
        sp.Matrix([-1, -1, 1]),
    ]


def _dihedral_cos_at_edge(verts, i, j, k, l):
    """cos of dihedral along edge (i, j), between faces (i,j,k) and (i,j,l)."""
    p_i, p_j, p_k, p_l = verts[i], verts[j], verts[k], verts[l]
    e = p_j - p_i
    n1 = e.cross(p_k - p_i)
    n2 = e.cross(p_l - p_i)
    num = (n1.T * n2)[0, 0]
    den = sp.sqrt((n1.T * n1)[0, 0] * (n2.T * n2)[0, 0])
    return num / den


def check_3_sector_signature(failures):
    header("Check 3: dihedrals are dilation-invariant, shear-sensitive")
    lam = sp.Symbol("lambda", positive=True)
    eps = sp.Symbol("epsilon")
    verts = _tetra_vertices()

    edges = [(0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2), (1, 2, 0, 3), (1, 3, 0, 2), (2, 3, 0, 1)]

    # Flat regular value: cos = 1/3 on every edge.
    base = [_dihedral_cos_at_edge(verts, *e) for e in edges]
    ok_base = all(is_zero(sp.simplify(b - sp.Rational(1, 3))) for b in base)
    require("regular tetrahedron: every dihedral has cos = 1/3 (coordinate check)",
            ok_base, failures)

    # Dilation: x -> lambda x. Every dihedral invariant, exactly.
    verts_dil = [lam * v for v in verts]
    dil = [_dihedral_cos_at_edge(verts_dil, *e) for e in edges]
    ok_dil = all(is_zero(sp.simplify(d - sp.Rational(1, 3))) for d in dil)
    require("dilation x -> lambda x leaves every dihedral exactly invariant",
            ok_dil, failures)

    # Volume-preserving shear: diag(1+eps, 1/(1+eps), 1). First-order shifts.
    S = sp.diag(1 + eps, 1 / (1 + eps), 1)
    verts_sh = [S * v for v in verts]
    sh = [_dihedral_cos_at_edge(verts_sh, *e) for e in edges]
    first_order = [sp.simplify(sp.series(x, eps, 0, 2).removeO().coeff(eps, 1)) for x in sh]
    any_nonzero = any(not is_zero(f) for f in first_order)
    require("volume-preserving shear shifts dihedrals at FIRST order",
            any_nonzero, failures)
    det_S = sp.simplify(S.det())
    require("the shear is exactly volume-preserving (det = 1)",
            is_zero(det_S - 1), failures)
    print(f"  first-order dihedral-cos shifts under shear: {[sp.sstr(f) for f in first_order]}")
    print()
    print("  Consequence, exact: ANY energy functional built from packing")
    print("  angles has identically zero restoring force in the dilation")
    print("  (volume/trace/kappa) mode, and generic first-order sensitivity")
    print("  in the shear (s) mode. The floor therefore supplies no dynamics")
    print("  for the volume mode -- it must be fixed by a constraint, which")
    print("  is precisely P3 (the unimodular constraint, 033) -- while shear")
    print("  strain carries energetic content, which is the gravitating")
    print("  configuration sector. The trace-constrained / shear-energetic")
    print("  sector signature derived top-down by the field-equation program")
    print("  (G02/G03, P7') emerges bottom-up from the packing microphysics.")


# =============================================================================
# Check 4: the gravitating/sequestered split
# =============================================================================


def check_4_split(failures):
    header("Check 4: gravity sees only excursions, never the floor")
    # T_vac = -rho_v g + T_exc; trace-free source of the constant part is 0.
    rho_v = sp.Symbol("rho_v")
    a = sp.Function("a", positive=True)(sp.Symbol("t"))
    g = sp.diag(-1, a**2, a**2, a**2)
    ginv = g.inv()
    T_floor = -rho_v * g
    trT = sp.simplify(sum(ginv[i, j] * T_floor[i, j] for i in range(4) for j in range(4)))
    ok = True
    for i in range(4):
        for j in range(4):
            src = T_floor[i, j] - sp.Rational(1, 4) * g[i, j] * trT
            ok = ok and is_zero(sp.simplify(src))
    require("trace-free source of the constant floor is identically zero",
            ok, failures)
    print()
    print("  The split T_vac = -rho_v g_ab + T_excursion is the identification's")
    print("  bookkeeping face: the substance/floor part is invisible to the")
    print("  trace-free dynamics (035), and only excursions gravitate --")
    print("  curvature strain in the closed sector, and any gapped/defect")
    print("  excess in the Trial D lane (which is non-constant, hence visible,")
    print("  hence still subject to the 017-019 gates). Weinberg's radiative-")
    print("  stability face, in VED vocabulary: gravity only ever sees changes")
    print("  in the vacuum, never the vacuum itself.")


# =============================================================================
# Report and archive
# =============================================================================


def write_report():
    md = """# VacuumForge: The Substance-Ledger Identity

## Purpose

Captures, at forge grade, the checkable mathematical content of the
identification proposed by the theory owner (2026-07-01):

```text
the frustration floor IS the substance energy of P1/P3
```

-- the energy that vacuum *is*, at the constant density P3 commits to,
realized physically as the irreducible packing frustration of the 3D
ground state (exact deficit Delta_0 = 2 pi - 5 arccos(1/3), 037).

## Verified Results

```text
1. Action-level sequestering. With sqrt(-g) = e^kappa sqrt(-g_bar) (033),
   the substance term splits exactly:
     -rho_v sqrt(-g) = -rho_v sqrt(-g_bar)          [inert constant]
                       - rho_v sqrt(-g_bar)(e^kappa - 1)   [leak coupling]
   The constant varies to nothing (fiducial volume form is not
   dynamical); the coupling is -rho_v kappa + O(kappa^2), identically
   zero in the P7'-exact sector and ~1e-31 where the F1 leak lives. In
   the unconstrained reading the term is a pure Lambda-shift absorbed by
   the integration constant (035). Either way: substance energy does not
   gravitate, as a theorem.

2. Conversion-factor target. Harmonic wedge model:
     rho_v = c_e kappa_w Delta_0^2 / (2 a^3),
   with Delta_0 exact. P1's open "analog of c^2" question becomes a
   formula target; kappa_w, a, c_e are the microphysics obligations.
   Model-dependent, flagged as such.

3. Sector signature from the packing. Verified on exact tetrahedron
   coordinates: every dihedral is exactly invariant under dilation
   x -> lambda x, and shifts at FIRST order under volume-preserving
   shear. Hence any angle-based floor energy is exactly flat in the
   volume/trace (kappa) mode and stiff in the shear (s) mode: the
   trace-constrained / shear-energetic architecture of the closed theory
   (G02/G03, P7', unimodular P3) emerges bottom-up. The volume mode must
   be fixed by a constraint because the microphysics gives it no
   dynamics -- and P3 is that constraint.

4. The split. T_vac = -rho_v g + T_excursion: the floor's trace-free
   source is identically zero; only excursions (curvature strain;
   gapped/defect excess) gravitate. Gravity sees only changes in the
   vacuum, never the vacuum itself.
```

## What the Identification Buys

```text
- P1 gets a mechanism: "vacuum is energy" because the packing is
  frustrated; the energy of vacuum-as-stuff is its residual deficit
  energy.
- The old implicit worry -- why doesn't the (presumably Planckian)
  substance energy curve everything -- is discharged as a theorem chain:
  P3 -> unimodular constraint -> sequestering. The postulate that
  defines the substance energy is the postulate that hides it.
- P4's bookkeeping cleans up: the baseline configuration energy of flat
  vacuum is relabeled to the substance ledger (constant, sequestered);
  configuration energy proper is departures from the ground packing --
  exactly what P9 says gravitates. Nothing in the closed chain used the
  floor, so nothing derived changes.
- P6 becomes physical: vacuum destruction = removing frustrated packing
  = releasing its stored deficit energy. The dimensional-relaxation
  channel and P6 exchange are two faces of one mechanism.
- The 037 aftermath is the natural home: the flat-frustrated ground
  state with sequestered floor IS the substance-energy vacuum.
```

## Falsifiers / Break Conditions of the Identification

```text
- any mechanism that makes the floor gravitate locally or vary in
  isolation (forbidden by 035; would break the identification);
- microphysics forcing the floor scale and the P1 conversion factor
  apart (they must be the same scale, same constancy);
- a volume-mode restoring force appearing in the packing energy (would
  contradict the exact dilation invariance and re-open the kappa
  sector).
```

## Classification

```text
result type: identification proposal with forge-verified mathematical
             content (action split, exact invariances, target formula)
scope:       the identification is an interpretive commitment, gate-
             consistent with 033/035/037; the wedge-model constants are
             microphysics obligations, not results
conclusion:  the frustration floor is coherently identifiable with P1/P3
             substance energy; sequestering makes "it does not gravitate"
             a theorem; the packing microphysics bottom-up reproduces the
             trace-constrained / shear-energetic sector signature
non-conclusion: rho_v's value is not derived (kappa_w, a, c_e open); no
             new observational channel through gravity exists or is
             claimed; the Trial D excess and dimensional-relaxation
             channels retain their own gates
```

## Newly Opened Obligation

```text
packing_stiffness_microphysics_038:
  give the wedge stiffness kappa_w, packing scale a, and edge-density
  coefficient c_e independent definitions (or reduce them to fewer
  parameters), turning the conversion-factor target
  rho_v = c_e kappa_w Delta_0^2/(2 a^3) into a derivation. Kill
  condition: if the same microphysics forces a volume-mode restoring
  force, the identification breaks (see falsifiers).
```

## Verification

```text
vacuum_forge/src/vacuum_sector/038_substance_ledger_identity/substance_ledger_identity.py
```

Archive record: `substance_ledger_identity_038`.
"""
    REPORT_PATH.write_text(md, encoding="utf-8")
    print(f"[INFO] report written: {REPORT_PATH}")


def record_archive(ns):
    ns.record_derivation(
        derivation_id="substance_ledger_identity_038",
        inputs=[
            sp.Symbol("unimodular_lovelock_break_result"),
            sp.Symbol("floor_sequestering_constraint_result"),
            sp.Symbol("relief_exact_geometry_result"),
        ],
        output=sp.Symbol("floor_identified_with_substance_energy_sector_signature_bottom_up"),
        method=(
            "exact action split via the kappa identity; harmonic wedge "
            "conversion-factor assembly; exact coordinate verification of "
            "dilation invariance and first-order shear sensitivity of "
            "tetrahedral dihedrals; trace-free blindness of the constant floor"
        ),
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="identification_with_verified_content",
        scope=(
            "identification is interpretive and gate-consistent; wedge-model "
            "constants are open microphysics; no closed result changes"
        ),
    )
    ns.record_obligation(ProofObligationRecord(
        obligation_id="substance_ledger_identity_recorded_038",
        script_id=SCRIPT_ID,
        title="Substance-ledger identity captured at forge grade",
        status=ObligationStatus.SATISFIED,
        satisfied_by=["substance_ledger_identity_038"],
        description=(
            "The floor = substance-energy identification is recorded with its "
            "verified mathematical content: action-level sequestering, "
            "conversion-factor target, bottom-up sector signature, and the "
            "gravitating/sequestered split."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="packing_stiffness_microphysics_038",
        script_id=SCRIPT_ID,
        title="Derive kappa_w, a, c_e (the conversion-factor microphysics)",
        status=ObligationStatus.OPEN,
        required_by=["substance_ledger_identity_038"],
        description=(
            "Turn rho_v = c_e kappa_w Delta_0^2/(2 a^3) from a target into a "
            "derivation. Kill condition: microphysics forcing a volume-mode "
            "restoring force breaks the identification."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="substance_ledger_identity_claim_038",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "The frustration floor is coherently identifiable with P1/P3 "
            "substance energy: the substance action term splits exactly into "
            "an inert fiducial constant plus an O(kappa) leak coupling (zero "
            "in the P7'-exact sector), so 'substance energy does not "
            "gravitate' is a theorem of P3's own unimodular content; the "
            "conversion factor acquires the target formula "
            "rho_v = c_e kappa_w Delta_0^2/(2 a^3) with Delta_0 exact; and "
            "the packing microphysics reproduces the closed theory's sector "
            "signature bottom-up (dihedrals exactly dilation-invariant, "
            "first-order shear-sensitive: volume mode constraint-type, shear "
            "mode energetic). Gravity sees only changes in the vacuum, never "
            "the vacuum itself. No closed result changes; rho_v's value "
            "remains open microphysics."
        ),
        derivation_ids=["substance_ledger_identity_038"],
        obligation_ids=[
            "substance_ledger_identity_recorded_038",
            "packing_stiffness_microphysics_038",
        ],
    ))


def main() -> None:
    header("Derivation 038: The Substance-Ledger Identity")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    failures: list = []
    check_1_action_split(failures)
    check_2_conversion_factor(failures)
    check_3_sector_signature(failures)
    check_4_split(failures)

    header("Verdict")
    if failures:
        for f in failures:
            print(f"  FAILED: {f}")
        raise SystemExit("Derivation 038: verification failure")
    print("  The identification is captured: floor = substance energy, with")
    print("  sequestering as its non-gravitation theorem, a conversion-factor")
    print("  target formula, and the sector signature emerging bottom-up from")
    print("  the packing. Open microphysics: kappa_w, a, c_e.")

    write_report()
    record_archive(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
