# Field Search Survivor Audit: Status After Proofs 1-5

## Purpose

This folder connects the archived `field_equation_candidates` search tree to
the focused proof chain in `projection_origin_probe`.

It is not a new field-equation search. It is an audit of what survived and how
that survivor has been used.

## Reports Checked

- `1_archive_survivor_guardrail_audit.md`
- `2_rk_discovery_trail_reconstruction.md`
- `3_moment_matrix_entry_formula.md`
- `4_source_signature_endpoint_formula.md`
- `5_candidate_tree_to_current_chain_map.md`

## What This Batch Proved

Proof `1` verifies the archive guardrails:

```text
field_equation_candidates is an archive;
projection_origin_probe is the focused successor;
the surviving object is the projection/admissibility hierarchy.
```

Proof `2` reconstructs the corrected provenance for the ratio:

```text
r_k = (2k - 1)/(2k + 3)
```

The historical route is:

```text
Group 88 moment-ratio identity:
I_k(P) = ((2k - 1)/(2k + 3)) I_(k-1)(P).
```

The later compact explanations are:

```text
primitive identity;
auxiliary same-row moment cancellation;
R=0 boundary-contact/admissibility ladder.
```

Proof `3` reconstructs the explicit moment matrix:

```text
A[k,j] = M(j+k) - r_k M(j+k-1)
```

and validates the closed rational formula plus positive determinants through
`N=6`.

Proof `4` reconstructs the endpoint/source-signature formula:

```text
-2(2kp + 6k - p - 4q - 3).
```

Proof `5` maps the archived search groups into the current proof chain,
including the corrected provenance:

```text
Group 88: original r_k route.
Groups 99/100: w=(1-x^2)^4 beta-moment/projection route.
Groups 52/53/54: source-safety guardrails.
```

It also preserves the no-overclaim guardrails.

## Current Interpretation

The old search tree did not prove a parent field equation.

It did produce:

```text
guardrails against false promotion;
the moment/projection object;
the r_k moment-ratio survivor;
the algebraically identified projection weight w=(1-x^2)^4;
the source-signature trends;
the reason to migrate into projection_origin_probe.
```

The current chain is therefore not searching blindly for `r_k`. It is using the
archived survivor as a seed:

```text
r_k
  -> endpoint-contact/admissibility ladder
  -> source-safety gates
  -> boundary-flux defect
  -> scalar field bridge
  -> metric lift
  -> EH/vacuum-action conditional chain.
```

Two source/origin gaps remain explicit:

```text
m=2 / R=0 is matched to the survivor ratio, not independently selected;
w=(1-x^2)^4 is algebraically identified, not physically derived.
```

## Next Step

The immediate source-safety guardrails have now been reconstructed in:

```text
source_safety_gate/
```

The next useful proof target is matter-source origin:

```text
derive why ordinary matter enters the A-sector once;
derive why residual/projection sectors remain source-neutral;
derive whether b_k(S) can attach to matter source without double counting.
```
