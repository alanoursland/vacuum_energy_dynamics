# Torsion Defect Exclusion 1: Torsion Norm And Source Variation

## Purpose

This proof restates the reduced torsion mode inside the selector folder.

The goal is to make the torsion-free branch a local theorem of this chain,
not an imported assumption.

## Validated Checks

- reduced torsion norm is 24 tau^2: passed
- source-coupled torsion energy reduces to 12 mu tau^2 - J tau: passed
- torsion variation is 24 mu tau - J: passed
- stationary torsion is J/(24 mu): passed

## Reduced Torsion Mode

Use the metric-compatible reduced connection component:

```text
Gamma^a_bc = tau epsilon_abc.
```

Then:

```text
T^a_bc = Gamma^a_bc - Gamma^a_cb.
```

Sympy verifies:

```text
T^a_bc T_a^bc = 24*tau**2.
```

## Source-Coupled Energy

With stiffness `mu` and source `J`:

```text
E_T = (mu/2) T^2 - J tau
    = -tau*(J - 12*mu*tau).
```

The variation is:

```text
dE_T/dtau = -J + 24*mu*tau.
```

Therefore:

```text
tau = J/(24 mu).
```

## Interpretation

Torsion is not removed by algebra. It is controlled by its source. The
torsion-free branch can only be selected after the torsion source is absent or
structurally canceled.
