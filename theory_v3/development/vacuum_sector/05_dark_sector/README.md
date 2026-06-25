# Dark-Sector Excess

This folder is for vacuum-sector excess over the Lambda baseline.

It is downstream of the Lambda floor ledger. A candidate excess must not be
inserted as the constant `Lambda` baseline or as ordinary matter by declaration.

## Current Boundary

The Lambda selector sweep records:

```text
constant floor:
  belongs to the Lambda baseline ledger

excitations, defects, clustered or transportable densities:
  belong here only after source, conservation, clustering, and abundance
  bookkeeping are supplied
```

## Required Gates

Every dark-sector excess candidate must state:

```text
source split from the Lambda floor;
equation of state;
conservation or exchange law;
clustering behavior and sound speed;
production or formation mechanism;
abundance route before observation;
coupling to the closed metric response;
falsifier.
```

## Current Managed Ledger

```text
dark_excess_source_ledger.md
dark_excess_source_ledger_vacuumforge.md
dark_excess_clustering_conservation_probe.md
dark_excess_clustering_conservation_probe_vacuumforge.md
dark_excess_abundance_production_probe.md
dark_excess_abundance_production_probe_vacuumforge.md
```

## Next Work

The next deliverable is outside this folder: non-gravitational channel
quarantine.

```text
each non-gravitational vacuum channel must state its coupling object, source
ledger, metric quarantine, observable, and falsifier.
```
