# Vacuum Sector Scripts

This tree contains VacuumForge-managed scripts for the vacuum-sector work.

Use this area when a result needs more than a standalone SymPy check:

```text
archive records;
dependency checks;
governance claims;
open obligations;
later proof-chain dependencies.
```

Pure algebraic scratch checks can stay in the theory folder, but results that
are intended to become part of the project proof chain should be promoted here.

## Running Scripts

From the repository root, run with the local package on `PYTHONPATH`:

```powershell
$env:PYTHONPATH='E:\Projects\vacuum_energy_dynamics\vacuum_forge\src'
C:\Users\alano\anaconda3\python.exe vacuum_forge\src\vacuum_sector\001_strain_underdetermination\strain_underdetermination_witness.py
```

## Current Groups

```text
001_strain_underdetermination/
```

Validates that the same local Hessian can coexist with different strain
dynamics. SymPy supplies the algebraic checks; VacuumForge records the
derivation, claim, and open obligation boundary.
