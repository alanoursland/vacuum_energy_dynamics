# Data Gate Protocol

## What This Document Is

This document fixes the rules for confronting trial candidates with
observational data, so that every data gate is structured, repeatable, and
auditable. It extends `00_introduction.md` (gates G21–G28).

The core principle:

```text
Data enters the archive exactly once, through a registry script,
with provenance attached. Confrontation scripts consume registry
records through forge dependencies. Nobody hardcodes a number twice.
```

---

## 1. The Three Layers

```text
Layer 1  DATASETS      vacuum_forge/src/dataexp/datasets/ -- one module per
                       dataset, ML-style: provenance, fetch/ensure logic,
                       loaders, checksums. Raw artifacts cache into
                       vacuum_forge/src/dataexp/.data/ (gitignored, never
                       committed). Where automated download is impossible
                       (e.g. curves that must be digitized from figures),
                       the module carries detailed instructions and a file
                       schema, and load() reports what is missing.

Layer 2  CONVERSION    symbolically derived formulas that translate between
                       the experiment's reporting language (e.g. Yukawa
                       alpha-lambda) and candidate predictions (e.g. plate
                       pressure). Validated in sympy, archived as forge
                       derivations.

Layer 3  CONFRONTATION dataexp/experiments/ scripts (and forge trial
                       scripts) that compare a candidate's prediction
                       against loaded datasets, producing constraint
                       surfaces or kills. All code runs from
                       vacuum_forge/src with PYTHONPATH=. .
```

Updating a bound (new experiment, better limit) touches Layer 1 only; every
experiment downstream re-runs against the new value. That is the
repeatability mechanism. Data is treated like ML datasets: versioned modules,
cached artifacts, manifest + checksum, deterministic loaders.

## 2. Provenance Requirements (Layer 1)

Every registered constraint must carry:

```text
value + confidence level + validity range
journal reference (journal, volume, page, year)
arXiv identifier where it exists
verification status:
  VERIFIED_FROM_ABSTRACT   value read from the paper's abstract/conclusion
  VERIFIED_FROM_FULL_TEXT  value read from the paper body/tables
  DIGITIZED_FROM_FIGURE    curve extracted from a published figure
  FROM_MEMORY_UNVERIFIED   forbidden in confrontations; placeholder only
retrieval date
```

A confrontation may only consume `VERIFIED_*` or `DIGITIZED_*` records.
`FROM_MEMORY_UNVERIFIED` records exist only to mark work needed.

## 3. Discipline Rules

```text
D1  Data bounds parameters; data never selects them (G30).
D2  Constraint values live in registry scripts only; confrontation
    scripts reference them through the archive.
D3  Conversion formulas are derived symbolically in the open, never
    imported as folklore. (Example: the Yukawa plane-pressure formula
    is a three-integral derivation; it is validated in the registry.)
D4  An exclusion claim is stated at the experiment's confidence level
    and validity range, never extrapolated outside it.
D5  Superseded bounds stay in the registry marked SUPERSEDED; history
    is part of the record.
D6  Negative space is recorded: where parameter space is NOT excluded
    is as much a result as where it is.
```

## 4. Current Registry Contents (anchors verified 2026-06)

Short-range gravity (gate G25), Yukawa parameterization
V(r) = -(G m1 m2 / r)(1 + alpha * exp(-r/lambda)):

```text
Lee et al. 2020 (Eot-Wash), PRL 124, 101101, arXiv:2002.11761
  |alpha| = 1 excluded for lambda >= 38.6 microns (95% CL)
  separations tested: 52 microns - 3.0 mm
  status: VERIFIED_FROM_ABSTRACT

Tan et al. 2020 (HUST), PRL 124, 051301
  |alpha| <= 1 holds down to lambda = 48 microns (95% CL)
  strongest alpha bounds in 40-350 microns; ~3x improvement at ~70 microns
  status: VERIFIED_FROM_ABSTRACT (secondary anchor; independent group)

Kapner et al. 2007 (Eot-Wash), PRL 98, 021101, hep-ph/0611184
  |alpha| = 1 excluded for lambda >= 56 microns
  status: SUPERSEDED by Lee 2020; retained as history
```

Open registry work:

```text
digitize full alpha(lambda) exclusion curves from Lee 2020 / Tan 2020
  figures (needed for quantitative UFFT constraint surface below the
  alpha = 1 crossing);
add Casimir-regime constraints (0.1-10 microns; Decca-class experiments)
  for the lower edge of the UFFT window.
```

## 5. The Strategic Fact

UFFT's own crossover scale is a_Lambda = (pi^2 hbar c / (720 rho_Lambda))^(1/4)
= 29.9 microns. The strongest current gravitational-strength exclusion
crossing is 38.6 microns. Therefore:

```text
The candidate's predicted scale sits in the narrow window BELOW the
|alpha| = 1 exclusion crossing. The data gate is a quantitative
constraint-surface computation, not an instant kill -- and conversely,
the next generation of experiments probes exactly this window.
```

This is the correct shape for a falsifiable candidate: alive, cornered, and
addressable by measurement.
