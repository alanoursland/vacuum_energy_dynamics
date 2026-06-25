# Minimal Strain Axiom Contract

## Purpose

This contract states what a new strain axiom must provide before it can be used
to license nonbaseline vacuum-sector physics.

It does not adopt a new axiom.

It is paired with:

```text
minimal_strain_axiom_contract_vacuumforge.md
```

## Required Fields

Any proposed strain axiom must state:

```text
X:
  the vacuum configuration variable

metric response map:
  how X produces Q_p(v) and the metric/Hessian branch

neighboring mismatch:
  how X(p) and X(q) are compared

K_strain:
  the invariant, scalar, derivative order, and variational object

boundary data:
  fixed data, counterterms, and differentiability rule

conservation/source identity:
  Noether/Bianchi route and source-ledger purity

mode and hyperbolicity route:
  radiative modes, principal symbol, weak-field residuals

epsilon classification:
  epsilon = 0, controlled epsilon != 0, failed, or underdetermined

falsifier:
  kill condition or operational test
```

## Current Route Ledger

```text
no new axiom / baseline:
  allowed as epsilon = 0 only

primitive nonmetric X axiom:
  open, but missing the full contract

primitive mismatch axiom:
  open, but missing X, invariant, boundary, conservation, and mode routing

nonlocal relaxation axiom:
  deferred until local GR limit and source quarantine are supplied

boundary/global axiom:
  can constrain classes but cannot supply K_strain alone

mechanism-fit axiom:
  rejected
```

## Rejected Move

Do not choose an axiom merely to rescue:

```text
nonzero Lambda;
dark excess;
Casimir/UFFT or material channels;
substance-frame observables;
interior caps;
observed compactness or density targets.
```

Those ledgers can constrain or motivate work only after the strain axiom exists
independently.

## Current Conclusion

The only currently complete route is:

```text
no new axiom, retain EH/GHY baseline at epsilon = 0.
```

A nonbaseline route remains possible only as an explicit future axiom that
satisfies this contract.

## Next Obligation

The next obligation is:

```text
strain_axiom_candidate_sieve_required_031
```
