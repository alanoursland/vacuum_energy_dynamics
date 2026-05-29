# Vacuum Action Origin 44: Projection Boundary Current Roles

## Purpose

This proof classifies the allowed roles of a scalar projection boundary current
relative to the EH/GHY boundary term.

## Validated Checks

- if EH has target trace normalization, extra projection coefficient shifts it: passed
- projection can share normalization only as an explicit count-once partition: passed
- pure diagnostic boundary current does not vary the induced metric: passed
- promoted scalar boundary current changes the trace-sector variation: passed

## If EH Already Carries The Target

If:

```text
K_EH = K_target,
```

then adding an independent projection trace coefficient gives:

```text
K_total - K_target = K_proj.
```

So it shifts the boundary normalization unless:

```text
K_proj = 0.
```

## Count-Once Partition

A partition is allowed:

```text
K_EH = theta K_target
K_proj = (1-theta) K_target.
```

But then projection and EH are not independent copies. They are an explicit
count-once decomposition.

## Diagnostic Role

If the projection boundary current is a diagnostic:

```text
J_boundary
```

with no variation against the induced metric, it does not alter the action
normalization.

If promoted as:

```text
K_proj h,
```

it contributes:

```text
d/dh = K_proj.
```

and becomes part of the boundary variational problem.

## Interpretation

The scalar projection boundary current may be a diagnostic, a trace-sector
seed, or a count-once partition term. It cannot be an untracked extra GHY copy.
