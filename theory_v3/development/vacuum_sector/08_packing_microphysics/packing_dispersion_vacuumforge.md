# VacuumForge: The Packing's Dispersion Relation (A5/C1)

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
