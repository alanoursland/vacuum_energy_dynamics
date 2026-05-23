# candidate_source_structure_problem — Analysis Note

## Result

`candidate_source_structure_problem.py` opens Group 102 as a formal source-vector structure scan.

It imports the Group 101 state correctly:

```text
source-vector formula b_k(S)=2∫psi_k S w dx derived;
simple source probes completed;
physical source not identified;
boundary conditions not derived.
```

The group target is:

```text
scan formal source families and identify useful sign signatures without selecting a physical source.
```

The script also correctly blocks overclaims:

```text
source family as physical source:
  not licensed

source vector as matter source:
  ordinary matter separation not derived

boundary conditions:
  not derived.
```

## Interpretation

This is the right next step after Group 101.

Group 101 derived the formal source-vector map:

```text
b_k(S)=2∫psi_k(x)S(x)w(x)dx.
```

Group 102 asks what this map does to families of candidate source profiles. That is useful because the sign-changing `psi_k` tests mean source vectors are not simple positive mass moments. They encode signed structure relative to moving row roots.

This group is still formal. It should not select a physical `S(x)`.

## What Changed

The project moves from isolated source probes to systematic source-family classification.

## What Did Not Change

No physical source is identified.

No boundary condition is derived.

No ledger assignment is licensed.

## Carry-forward status

```text
SOURCE_VECTOR_STRUCTURE_SCAN_OPENED
FORMAL_SOURCE_FAMILY_SCAN_TARGET_DEFINED
PHYSICAL_SOURCE_SELECTION_BLOCKED
MATTER_SOURCE_INTERPRETATION_BLOCKED
BOUNDARY_CONDITIONS_NOT_DERIVED
```
