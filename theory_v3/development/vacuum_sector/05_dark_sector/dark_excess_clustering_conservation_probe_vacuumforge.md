# VacuumForge Dark Excess Clustering/Conservation Probe

## Purpose

This report tests the first clustering and conservation gates for dustlike
vacuum-sector excess. It does not derive dark matter abundance or halo
phenomenology.

This report depends on:

```text
dark_excess_source_ledger_017
```

It satisfies:

```text
dark_excess_clustering_conservation_required_017
```

## Symbolic Checks

Dust conservation:

```text
rho_dust = rho0/a**3
a d rho_dust/da + 3 rho_dust = 0
```

Constant-w conservation form:

```text
rho(a,w) = a**(-3*w - 3)*rho0
a d rho/da + 3(1+w)rho = 0
```

Pressure and growth proxies:

```text
pressure term = c_s2*k**2/a**2
pressure term at c_s^2 = 0 = 0
matter-era delta=a growth residual = 0
```

## Gate Ledger

| row | candidate | symbolic result | gate status | disposition | next obligation |
| --- | --- | --- | --- | --- | --- |
| conserved_pressureless_dust | w = 0, c_s^2 = 0, separately conserved excess | rho = rho0/a^3, continuity residual = 0, pressure term = 0 | passes clustering readiness proxy | dark-sector excess candidate, not yet abundance-licensed | derive production and abundance before claiming dark matter |
| pressure_supported_excess | w = 0 but c_s^2 != 0 | pressure term = c_s2*k**2/a**2 | blocked pending small-sound-speed route | not CDM-like until pressure support is routed or bounded | supply sound-speed bound or microphysical cold limit |
| exchanging_excess | excess exchanges with floor or another sector | continuity residual = Q | blocked pending exchange ledger | requires paired conservation with the floor or source sector | write exchange law and prove total conservation |
| ordinary_matter_insertion | declare excess as ordinary matter source | no independent vacuum-sector source ledger | rejected route | source double-counting unless independently derived | do not insert into T_ab without production/source route |

## Current Conclusion

A separately conserved, pressureless `w = 0` excess has the minimum
clustering-readiness face, but it is still not a dark-sector model. It needs a
production mechanism, abundance calculation, and source ledger before it can be
used as dark matter. Pressure-supported or exchanging excess rows require
their own routing. Ordinary matter insertion is rejected as source
double-counting.

## Classification

```text
result type: dark-excess clustering/conservation probe
scope: dustlike excess readiness after source/equation-of-state ledger
conclusion: conserved pressureless dust is a candidate only; abundance and production remain open
non-conclusion: no dark matter abundance, halo model, or particle identity is derived
```

The next technical target is:

```text
dark_excess_abundance_production_required_018
```
