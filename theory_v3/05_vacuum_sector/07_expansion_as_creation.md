# 07 — Expansion As Creation

**STATUS: Decided (derivation 054, 2026-07-02). Under P10, cosmic
expansion is the creation of new packing cells at fixed scale — not
the stretching of existing ones. The rival reading is excluded twice
on existing data; the surviving reading is exactly self-funding
through the floor's equation of state; and the theory acquires a new
standing falsifier: $\dot G = 0$, exactly (register A6).**

## The Question

What *is* expansion, if space is a packing? Derivation 045 proved P6
and P10 consistent but left this underdetermined, with two candidate
readings:

```text
STRETCH   the graph is fixed; its cells dilate with the scale factor
          (edge length ℓ(t) = ℓ₀ a(t), cell count N constant)
GROWTH    the packing scale is fixed; new cells are created
          (ℓ = const, N ∝ a³)
```

Both give the same $a^3$ volume history and source the same dust
stress. **The closed metric sector cannot distinguish them and never
will** — Einstein's equations are identical under either bookkeeping.
The register (C3) expected the discrimination to wait on future
perturbed-cosmology measurements. It did not have to wait: the two
readings have different side effects on quantities the theory had
already *locked*, and existing data adjudicates.

## The Stretch Reading Dies Twice

**Kill 1 — it drags Newton's constant.** The floor-Newton lock ties
$G$ to the packing scale: $G \propto 1/(f'(\Delta_0)\,\ell)$. If cells
dilate with $a(t)$,

$$\frac{\dot G}{G} = -\frac{\dot\ell}{\ell} = -H \approx -7.2\times10^{-11}\,/\mathrm{yr},$$

while lunar laser ranging bounds $|\dot G/G| < 1.5\times10^{-13}$/yr.
**Excluded by a factor ~480.** A stretched packing cannot keep $G$
fixed; nature's $G$ does not drift.

**Kill 2 — the floor turns to dust.** Wedge energies are exactly
dilation-invariant (038; measured many-body in 041 E3). Under stretch
the total floor energy is constant while volume grows, so the floor's
pressure is $p = -dE/dV = 0$: **dustlike, $w = 0$, at Planck
density**. And a *diluting* density ($u \propto a^{-3}$) is precisely
what P3's sequestering does *not* protect — sequestering hides
constant density only. The stretched floor would gravitate as dark
matter at $\sim10^{122}$ times closure density, and would demolish
the sequestering architecture that `03_lambda_and_the_global_datum.md`
and register entries A1/B1 stand on. Instantly excluded, independently
of Kill 1.

## The Survivor Is Self-Funding

Under growth, everything locks together with zero tuning:

```text
ℓ = const           ⟹  G = const, EXACTLY (no drift mechanism remains)
floor intensive     ⟹  E = uV with u constant — MEASURED (051 E1)
                    ⟹  p = −dE/dV = −u:  w = −1 EXACTLY
                    ⟹  creation cost u·dV = negative-pressure work
                        −p·dV, term by term
```

The last line closes the oldest question this ontology carried: *where
does the energy for new space come from?* Answer: from the floor's own
negative-pressure work. **The first law funds expansion.** Creating a
cubic meter of frustrated vacuum costs exactly the work the vacuum's
$w = -1$ stress performs in opening that cubic meter — no reservoir,
no debt, no external supply. The measured intensivity of the floor
(051) *is* the $w = -1$ equation of state at the substance level; the
same result that makes the substance ledger consistent makes the
cosmology self-funding.

This also snaps the sector's pieces into one picture: the floor is
enormous but sequestered (06); its one dynamical job is to pay for its
own extension; and the Λ that gravity *does* see remains the untouched
global datum of `03`.

## The New Falsifier: $\dot G = 0$, Exactly

The surviving reading leaves the theory with **no mechanism for $G$
drift at all** — not small, none. This is pre-registered as register
entry A6:

```text
commitment:  Ġ/G = 0 at every epoch.
kills it:    any confirmed nonzero Ġ/G (LLR/ephemerides, currently
             ~1.5e-13/yr; pulsar timing; BBN/CMB consistency).
distinctive: scalar-tensor and varying-G rivals generically predict
             drift; VED forbids it outright.
pressure:    H₀ sits only ~480× above current LLR bounds and the
             bounds keep tightening — this null is under genuine,
             foreseeable experimental fire.
```

Note the structure: the same lock that *killed* the stretch reading
becomes the surviving reading's exposure. If $\dot G \neq 0$ is ever
confirmed, the creation reading dies, and with it P10's account of
expansion. The barrel is pointed before the data arrives, as the
register requires.

## The Vacuum-Flow Clause

The founding intuition of this ontology — mass constrains the local
vacuum; expansion's new space appears preferentially *outside* gravity
wells and is in effect pushed out of them — now has its formal seat.
Writing the local creation rate as

$$C = 3H\,(1 - \alpha\,\delta),$$

with $\delta$ the density contrast and $\alpha$ the suppression
coefficient: since $\langle\delta\rangle = 0$, the background is
**exactly** $\langle C\rangle = 3H$ for *any* $\alpha$. The clause is
invisible to the background, invisible to the metric sector (which
never cared about the substance bookkeeping), and therefore currently
unconstrained and unconstraining — it lives entirely in the
substance/perturbation sector. It would give the standard result that
bound systems do not expand a *mechanism* (creation migrates to the
voids), but no observable is claimed for it yet.

The coefficient $\alpha$ becomes computable exactly when O-P10-4's
Lorentzian dynamics exists: creation as a functional of local strain.
Recorded as the open obligation `creation_suppression_dynamics_054` —
the precise point where this ontology's oldest picture waits for its
newest mathematics.

## What This Document Does Not Claim

```text
- no metric observable distinguishes the readings; GR is untouched
  (both readings source identical dust stress; the kills act through
  side effects on locked quantities, not through new metric terms)
- no value for α; no void/well differential-expansion signal is
  licensed
- the initial-value formulation of the packing's evolution (O-P10-4
  proper) remains open; this document decides the READING, not the
  dynamics
```

## Verification

```text
054  cosmological_creation_face    the dichotomy, both kills, the
                                   self-funding identity, the clause
depends on: p6_p10_consistency_045, bulk_relaxation_phase2_051
            (intensivity), regge_delaunay_bridge_039 (the lock)
report: ../development/vacuum_sector/08_packing_microphysics/
        cosmological_creation_face_vacuumforge.md
```
