# 05 — The Vacuum Sector: Overview

**STATUS: The strain-axiom question is closed. Under P10 (the packing
axiom, adopted 2026-07-01), the vacuum sector has a microphysics: the
vacuum is a frustrated packing, its substance energy is the strain of
being three-dimensional, its gravitational response is Einstein–Hilbert
because the ground state is pre-tensioned, and Λ is a global datum
decoupled from the vacuum's own energy. This section is the record of
the theory P10 implies.**

## What This Section Is

`04_field_equations/` closed the gravitational response: Einstein's
equations, derived. This section holds what comes *after* — the physics
of the vacuum itself, which the closed metric response could never see.
Until 2026-07-01 this directory held only a TODO; the vacuum-sector
program (development ledger: `../development/vacuum_sector/`) ran
derivations 001–043, killed every mechanism that deserved killing, and
converged on one adopted answer. These documents are that answer,
promoted from the development tier to the section of record.

The controlling rule is unchanged: **nothing here reopens the field
equations.** Every coefficient of `04_field_equations/` stands. The
vacuum sector's physics lives in what gravity cannot see (the substance
ledger), in what fixes the one constant gravity permits but does not
value (Λ), and in what may yet be seen in non-metric channels (the
excursion ledger).

## The Story in Four Documents

| document | content | one line |
|---|---|---|
| `01_substance_energy.md` | what the vacuum's energy *is* | being 3D space costs strain; that strain is P1's energy, and gravity cannot see it |
| `02_gravitational_response.md` | why the response is Einstein–Hilbert | the ground state is pre-tensioned; loaded springs respond at first order |
| `03_lambda_and_the_global_datum.md` | Λ's status, meaning, sign, value | integration constant; ground-state curvature; conditionally positive; value external |
| `04_excursions_and_exchange.md` | what gravity *does* see | strain variations: wells, waves, defects; the P6 pipeline with its exact ledger |

Plus `05_open_obligations.md`: the adopted postulate's debts,
falsifiers, and the handoff to future work.

## The Postulate

P10 (`../01_postulates/p10_packing_axiom.md`): the vacuum substance is
a packing — an edge-length graph whose geometry is piecewise-flat with
hinge-deficit curvature, whose energy is a smooth per-hinge function of
the closure mismatch, and whose ground state is flat with the
irreducible tetrahedral frustration $\Delta_0 = 2\pi - 5\arccos\tfrac13$
realized as uniform strain. P10 implements P1–P5 rather than adding to
them; its fence, falsifiers, and obligations are in the postulate file.

## Epistemic Standing

Everything stated as a result in this section is forge-verified
(derivations 033–043, all green, archive under
`vacuum_forge/src/vacuum_sector/`); everything that is an
interpretation licensed by P10 is stated as such; everything still
gated (dark-excess abundance, non-gravitational channels, interior
cap, matter-as-defect) is explicitly marked NOT LICENSED. The
falsifiers are standing kill conditions: F-P10-1 (volume-mode
restoring force), F-P10-2 (floor/conversion-factor split), and the
inherited P7′ null test.

## Reading Pointers

```text
../01_postulates/p10_packing_axiom.md            the adopted axiom
../development/vacuum_sector/                     the full development
                                                  ledger (001-043) and
                                                  the adoption briefing
../development/vacuum_sector/08_packing_microphysics/
                                                  the model, theorems,
                                                  lab, and reports
vacuum_forge/src/vacuum_sector/                   the forge archive
```
