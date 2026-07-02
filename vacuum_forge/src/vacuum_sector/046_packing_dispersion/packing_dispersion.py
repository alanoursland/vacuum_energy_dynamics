#!/usr/bin/env python3
"""
packing_dispersion.py

The packing's dispersion relation -- the A5/C1 computation, and the
sharpest currently-computable way P10 could die.

THE THREAT (predictions register A5). A naive "lattice at scale a in
the substance frame" generically suggests linear-in-(E/E_Planck)
modifications to propagation, omega = ck(1 +/- xi ka). Linear
Lorentz-violation is already EXCLUDED past the Planck scale by GRB
time-of-flight bounds. If the packing produces a linear term, P10 is
dead against existing data.

THE RESULT (computed below). It does not -- and not by accident. For
ANY harmonic network whose energy is a real quadratic form with
finite-range couplings (pair springs, angle/wedge energies, arbitrary
multi-body -- P10's entire class), the dynamical matrix satisfies

    D(-k) = D(k)*        (reality of the force constants)
    D(k)^dagger = D(k)   (symmetry of second derivatives)

so its characteristic polynomial has real coefficients and is EVEN in
k: the spectrum omega^2(k) is an even function of k along every
direction. Therefore

    omega(k) = c k (1 + c2 (ka)^2 + O(k^4 a^4)):

NO LINEAR TERM EXISTS, exactly, for any graph, any couplings, with no
lattice point symmetry required. The leading modification is quadratic
and Planck-suppressed: effective E_QG,2 ~ sqrt(1/|c2|) E_Planck, which
sits ~8-9 orders of magnitude beyond current quadratic GRB bounds.

P10 SURVIVES ITS SHARPEST TEST -- protected by the same structural
fact that underlies everything else in the sector: the strain energy
is a real energy.

Five checks:

  1. THE EXACT MONATOMIC WITNESS. The 1D chain's exact dispersion
     omega = (2/a) sqrt(kappa/m) |sin(ka/2)|: series
     ck (1 - (ka)^2/24 + O(k^4)) -- zero linear term, exact quadratic
     coefficient -1/24, subluminal.

  2. THE EVENNESS THEOREM, GENERIC WITNESS. For a two-band model with
     ARBITRARY real force-constant blocks (Phi(0) = S symmetric,
     Phi(R) = A arbitrary, Phi(-R) = A^T -- the general real-energy
     structure, covering multi-body couplings and lattices with NO
     inversion symmetry): trace and determinant of D(k) are exactly
     even in k, symbolically, for fully symbolic S and A. The 2x2
     spectrum is determined by (trace, det), hence even. This is the
     theorem's load-bearing witness.

  3. THE PHYSICAL NO-SYMMETRY WITNESS. The diatomic chain with
     alternating masses AND alternating springs (m1 != m2,
     kappa1 != kappa2: no inversion symmetry): both invariants even in
     k exactly; the acoustic branch's small-k series has zero k^3
     term and the standard quadratic-corrected sound speed.

  4. THE NUMBERS AGAINST THE BOUNDS. With c2 = -1/24 (witness value;
     model-dependent O(1)): effective quadratic scale
     E_QG,2 = sqrt(24) E_Planck ~ 6e19 GeV vs current GRB quadratic
     bounds ~1e11 GeV: a safety margin of ~6e8. And the linear scale
     is INFINITE -- the theorem, not a large number.

  5. SCOPE AND ESCAPE ROUTES (recorded honestly). The theorem covers
     every real, finite-range, harmonic action on the packing --
     the TT (graviton) modes directly, and any matter field whose
     discretization inherits real couplings. Escape routes that would
     evade it, hence remain kill surfaces: (i) time-reversal-breaking
     (complex/chiral) couplings in the matter discretization;
     (ii) non-analytic force constants (infinite range);
     (iii) anharmonic corrections at extreme amplitudes. None is
     present in P10 as adopted; each is a recorded watch item.

Output:
    theory_v3/development/vacuum_sector/08_packing_microphysics/packing_dispersion_vacuumforge.md
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
    / "packing_dispersion_vacuumforge.md"
)

DEPENDENCIES = [
    ("p10_adoption_dep_046", "044_p10_adoption__p10_adoption",
     "p10_adoption_record_044"),
    ("lift_dep_046", "043_lorentzian_4d_lift__lorentzian_4d_lift",
     "lorentzian_4d_lift_043"),
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
    print("[INFO] Archive dependency check:")
    for check in checks:
        print(f"  - {check.dependency.dependency_id}: {check.status} ({check.message})")


# =============================================================================
# Check 1: the exact monatomic witness
# =============================================================================


def check_1_monatomic(failures):
    header("Check 1: 1D chain, exact: omega = ck(1 - (ka)^2/24 + O(k^4))")
    k, a, kap, m = sp.symbols("k a kappa m", positive=True)
    omega = 2 * sp.sqrt(kap / m) * sp.sin(k * a / 2)
    c_s = a * sp.sqrt(kap / m)
    series = sp.series(omega, k, 0, 6).removeO()
    lin = sp.simplify(series.coeff(k, 1) - c_s)
    quad = sp.simplify(series.coeff(k, 2))
    cub = sp.simplify(series.coeff(k, 3) + c_s * a**2 / 24)
    require("linear coefficient = c exactly (relativistic limit recovered)",
            is_zero(lin), failures)
    require("NO k^2 term (no even-power term in omega itself)",
            is_zero(quad), failures)
    require("k^3 coefficient = -c a^2/24 exactly: quadratic correction, subluminal",
            is_zero(cub), failures)
    print()
    print("  omega/ck = 1 - (ka)^2/24 + O(k^4): the exact chain shows the")
    print("  pattern the theorem below makes universal -- corrections START")
    print("  at (ka)^2, and are subluminal in this witness.")


# =============================================================================
# Check 2: the evenness theorem, generic two-band witness
# =============================================================================


def check_2_evenness_theorem(failures):
    header("Check 2: generic real force constants => spectrum EVEN in k (the theorem)")
    k = sp.Symbol("k", real=True)
    # Fully symbolic real blocks: S symmetric (on-site), A arbitrary
    # (neighbor); the general structure of ANY real harmonic energy:
    # D(k) = S + A e^{ika} + A^T e^{-ika}.
    s11, s12, s22 = sp.symbols("s11 s12 s22", real=True)
    a11, a12, a21, a22 = sp.symbols("a11 a12 a21 a22", real=True)
    S = sp.Matrix([[s11, s12], [s12, s22]])
    A = sp.Matrix([[a11, a12], [a21, a22]])
    D = S + A * sp.exp(sp.I * k) + A.T * sp.exp(-sp.I * k)

    Dm = D.subs(k, -k)
    require("D(-k) = D(k)* (reality of force constants), symbolically",
            all(is_zero(sp.simplify(Dm[i, j] - sp.conjugate(D[i, j]).rewrite(sp.exp)))
                for i in range(2) for j in range(2)), failures)
    require("D(k) is Hermitian (energy is a real quadratic form), symbolically",
            all(is_zero(sp.simplify(D[i, j] - sp.conjugate(D[j, i]).rewrite(sp.exp)))
                for i in range(2) for j in range(2)), failures)

    tr = sp.simplify(D.trace().rewrite(sp.cos))
    det = sp.simplify(D.det().rewrite(sp.cos))
    require("trace D(k) even in k, exactly (fully symbolic couplings)",
            is_zero(sp.simplify(tr - tr.subs(k, -k))), failures)
    require("det D(k) even in k, exactly (fully symbolic couplings)",
            is_zero(sp.simplify(det - det.subs(k, -k))), failures)
    print()
    print("  The 2x2 spectrum is a function of (trace, det) alone; both are")
    print("  exactly even in k for ARBITRARY real couplings -- multi-body,")
    print("  no inversion symmetry, any graph. Hence omega^2(k) is even:")
    print("  a linear term in omega(k) = ck(1 + xi ka + ...) CANNOT EXIST.")
    print("  The protection is the reality of the strain energy -- the same")
    print("  structural fact behind the whole sector -- not a lattice")
    print("  symmetry that a messy packing might lack.")


# =============================================================================
# Check 3: the physical no-symmetry witness (diatomic chain)
# =============================================================================


def check_3_diatomic(failures):
    header("Check 3: diatomic chain (no inversion symmetry): acoustic branch even")
    k, a = sp.symbols("k a", positive=True)
    k1, k2, m1, m2 = sp.symbols("kappa1 kappa2 m1 m2", positive=True)
    # Mass-weighted dynamical matrix; unit cell (m1, m2), springs k1
    # (intra-cell), k2 (inter-cell): generic k1 != k2, m1 != m2 has no
    # inversion center.
    D = sp.Matrix([
        [(k1 + k2) / m1, -(k1 + k2 * sp.exp(-sp.I * k * a)) / sp.sqrt(m1 * m2)],
        [-(k1 + k2 * sp.exp(sp.I * k * a)) / sp.sqrt(m1 * m2), (k1 + k2) / m2],
    ])
    tr = sp.simplify(D.trace())
    det = sp.simplify(D.det().rewrite(sp.cos))
    require("trace even in k (exactly)",
            is_zero(sp.simplify(tr - tr.subs(k, -k))), failures)
    require("det = 2 kappa1 kappa2 (1 - cos ka)/(m1 m2): even in k (exactly)",
            is_zero(sp.simplify(det - 2 * k1 * k2 * (1 - sp.cos(k * a)) / (m1 * m2))),
            failures)

    # Acoustic branch small-k series from the invariants:
    # omega^2_ac = (tr - sqrt(tr^2 - 4 det))/2; expand in k.
    disc = sp.sqrt(tr**2 - 4 * det)
    w2_ac = sp.simplify((tr - disc) / 2)
    ser = sp.series(w2_ac, k, 0, 5).removeO()
    c2_sound = sp.simplify(ser.coeff(k, 2))
    target_c2 = k1 * k2 * a**2 / ((k1 + k2) * (m1 + m2))
    require("sound speed^2 = kappa1 kappa2 a^2/((kappa1+kappa2)(m1+m2)) exactly",
            is_zero(sp.simplify(c2_sound - target_c2)), failures)
    require("NO k^3 term in omega^2_acoustic (evenness realized)",
            is_zero(sp.simplify(ser.coeff(k, 3))), failures)
    print()
    print("  A chain with NO inversion symmetry still has exactly even")
    print("  dispersion: the theorem needs only reality, and the physical")
    print("  witness confirms it with the textbook sound speed emerging in")
    print("  the continuum limit.")


# =============================================================================
# Check 4: the numbers against the bounds
# =============================================================================


def check_4_numbers(failures):
    header("Check 4: quadratic LIV at Planck scale vs existing bounds")
    E_P = 1.22e19          # GeV, Planck energy
    c2_mag = sp.Rational(1, 24)  # witness quadratic coefficient (model O(1))
    E_QG2_packing = math.sqrt(1 / float(c2_mag)) * E_P
    E_QG2_bound = 1e11     # GeV: current GRB quadratic-order bounds (order of magnitude)
    margin = E_QG2_packing / E_QG2_bound
    print(f"  linear-order scale:      INFINITE (theorem: no linear term exists)")
    print(f"  quadratic scale (packing, c2 = -1/24 witness): "
          f"E_QG,2 ~ {E_QG2_packing:.2e} GeV")
    print(f"  current quadratic bounds:                      "
          f"E_QG,2 > ~{E_QG2_bound:.0e} GeV")
    print(f"  safety margin: ~{margin:.1e}")
    require("packing sits >= 1e6 beyond current quadratic bounds",
            margin > 1e6, failures)
    # Concreteness: a 1 TeV photon's fractional speed shift.
    E = 1e3  # GeV
    dv = (E / E_QG2_packing) ** 2
    print(f"  a 1 TeV photon's |dv/c| ~ {dv:.1e} -- unobservable for the")
    print(f"  foreseeable future.")
    require("1 TeV fractional speed shift below 1e-30", dv < 1e-30, failures)


# =============================================================================
# Check 5: scope and escape routes
# =============================================================================


def check_5_scope():
    header("Check 5: scope and the recorded escape routes")
    print("  The theorem covers every real, finite-range, harmonic action on")
    print("  the packing: the TT (graviton) modes directly, and any matter")
    print("  field whose discretization inherits real couplings. The escape")
    print("  routes -- hence the remaining kill surfaces for A5 -- are:")
    print()
    print("    (i)   time-reversal-breaking (complex/chiral) couplings in a")
    print("          matter discretization: would permit odd terms. Not")
    print("          present in P10 as adopted; any future matter-ontology")
    print("          work (e.g. matter-as-defect) must re-run this check.")
    print("    (ii)  non-analytic / infinite-range force constants: excluded")
    print("          by P10's locality.")
    print("    (iii) anharmonic corrections at extreme amplitudes: irrelevant")
    print("          to GRB propagation (linear regime).")
    print()
    print("  Frame remark: the dispersion is defined in the substance frame;")
    print("  observer boosts (~1e-3 c vs the CMB) modify the comparison to")
    print("  bounds at relative order 1e-3 -- immaterial at margin 1e8.")


# =============================================================================
# Report and archive
# =============================================================================


def write_report():
    md = """# VacuumForge: The Packing's Dispersion Relation (A5/C1)

## Purpose

Executes the predictions register's highest-priority self-threat: does
the packing's discreteness produce linear-in-(E/E_Planck) dispersion,
which existing GRB bounds already exclude? If yes, P10 dies against
existing data. Computed: it does not, and cannot.

## The Theorem

For ANY harmonic network whose energy is a real quadratic form with
finite-range couplings (pair, angle/wedge, arbitrary multi-body -- the
entire P10 class), the dynamical matrix satisfies D(-k) = D(k)* and
D(k)^dagger = D(k). Its characteristic polynomial therefore has real
coefficients and is even in k: the spectrum omega^2(k) is an even
function of k along every direction, so

```text
omega(k) = c k (1 + c2 (ka)^2 + O(k^4 a^4)) -- NO LINEAR TERM EXISTS,
```

for any graph, with no lattice point symmetry required. The protection
is the REALITY OF THE STRAIN ENERGY -- the same structural fact that
underlies the sector -- not a symmetry a disordered packing might lack.

## Verified

```text
1. exact monatomic chain: omega/ck = 1 - (ka)^2/24 + O(k^4)
   (zero linear term; exact -1/24; subluminal witness)
2. generic two-band model, FULLY SYMBOLIC real couplings (covers
   multi-body, no inversion symmetry): D(-k) = D(k)*, D Hermitian,
   trace and det exactly even in k => spectrum even (the theorem's
   load-bearing witness)
3. diatomic chain (physically no inversion symmetry): invariants even
   exactly; acoustic branch has the textbook sound speed and zero k^3
   term
4. numbers: linear scale INFINITE; quadratic scale ~ sqrt(24) E_P ~
   6e19 GeV vs current quadratic GRB bounds ~1e11 GeV: margin ~6e8;
   a 1 TeV photon's |dv/c| ~ 3e-34
5. scope: covers all real finite-range harmonic actions (TT modes
   directly; matter under the real-couplings assumption); escape
   routes recorded as watch items (chiral matter couplings;
   non-locality; anharmonicity)
```

## Verdict

```text
P10 SURVIVES ITS SHARPEST TEST. The packing predicts:
  - exactly NO linear Lorentz violation (theorem-grade), and
  - quadratic, Planck-suppressed dispersion (~(E/E_P)^2, coefficient
    model-dependent O(1), subluminal in the computed witnesses),
    ~8-9 orders below current quadratic bounds.

Register update: A5 is resolved from "self-threat" to "sharpened
prediction": any CONFIRMED linear-order LIV now falsifies P10 outright
(it cannot be accommodated), and quadratic-order LIV detection at
scales far below E_P would do the same. The watch items (chiral matter
couplings under any future matter-ontology work) are recorded.
```

## Verification

```text
vacuum_forge/src/vacuum_sector/046_packing_dispersion/packing_dispersion.py
```

Archive record: `packing_dispersion_046`.
"""
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(md, encoding="utf-8")
    print(f"[INFO] report written: {REPORT_PATH}")


def record_archive(ns):
    ns.record_derivation(
        derivation_id="packing_dispersion_046",
        inputs=[
            sp.Symbol("p10_adoption_record"),
            sp.Symbol("lorentzian_4d_lift_result"),
        ],
        output=sp.Symbol("no_linear_LIV_theorem_quadratic_planck_suppressed"),
        method=(
            "exact monatomic chain series; evenness theorem via D(-k) = D(k)* "
            "on a fully symbolic generic two-band model; diatomic no-inversion "
            "witness with exact sound speed; bounds comparison"
        ),
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="dispersion_theorem",
        scope=(
            "all real finite-range harmonic actions on the packing; chiral "
            "matter couplings and anharmonicity recorded as watch items"
        ),
    )
    ns.record_obligation(ProofObligationRecord(
        obligation_id="packing_dispersion_computed_046",
        script_id=SCRIPT_ID,
        title="A5/C1 resolved: no linear LIV (theorem); quadratic Planck-suppressed",
        status=ObligationStatus.SATISFIED,
        satisfied_by=["packing_dispersion_046"],
        description=(
            "The register's highest-priority self-threat is resolved in P10's "
            "favor: linear dispersion cannot exist for any real harmonic "
            "action on the packing; the leading modification is quadratic at "
            "the Planck scale, ~8-9 orders beyond current bounds."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="chiral_matter_dispersion_watch_046",
        script_id=SCRIPT_ID,
        title="Watch item: chiral matter discretizations re-open the linear channel",
        status=ObligationStatus.OPEN,
        required_by=["packing_dispersion_046"],
        description=(
            "Any future matter-ontology work (e.g. matter-as-defect) that "
            "introduces time-reversal-breaking couplings must re-run the "
            "dispersion check: complex couplings evade the evenness theorem."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="packing_dispersion_claim_046",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "The packing produces exactly no linear-order Lorentz violation: "
            "for every real, finite-range, harmonic action (the P10 class), "
            "D(-k) = D(k)* forces the spectrum even in k, so "
            "omega = ck(1 + c2 (ka)^2 + ...) with no linear term, for any "
            "graph and no required symmetry. The leading modification is "
            "quadratic and Planck-suppressed (E_QG,2 ~ sqrt(1/|c2|) E_P ~ "
            "6e19 GeV for the witness c2 = -1/24), ~8-9 orders beyond current "
            "GRB quadratic bounds. P10 survives its sharpest test; a "
            "confirmed linear LIV would now falsify it outright, and chiral "
            "matter couplings are the recorded watch item."
        ),
        derivation_ids=["packing_dispersion_046"],
        obligation_ids=[
            "packing_dispersion_computed_046",
            "chiral_matter_dispersion_watch_046",
        ],
    ))


def main() -> None:
    header("Derivation 046: The Packing's Dispersion Relation")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    failures: list = []
    check_1_monatomic(failures)
    check_2_evenness_theorem(failures)
    check_3_diatomic(failures)
    check_4_numbers(failures)
    check_5_scope()

    header("Verdict")
    if failures:
        for f in failures:
            print(f"  FAILED: {f}")
        raise SystemExit("Derivation 046: verification failure")
    print("  NO linear Lorentz violation exists for any real harmonic action")
    print("  on the packing (theorem); the leading modification is quadratic")
    print("  and Planck-suppressed, ~8-9 orders beyond current bounds. P10")
    print("  survives its sharpest currently-computable test. Watch item:")
    print("  chiral matter couplings.")

    write_report()
    record_archive(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
