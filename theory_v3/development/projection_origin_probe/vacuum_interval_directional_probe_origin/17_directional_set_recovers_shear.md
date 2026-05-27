# Vacuum Interval Directional Probe Origin 17: Directional Set Recovers Shear

## Purpose

This proof is the positive counterpart to the isotropic-average limitation.

Directional interval probes recover the shear components that averaging loses.

## Validated Checks

- axis difference recovers diagonal shear: passed
- pair probe recovers off-diagonal shear: passed
- axis sum recovers mean trace: passed

## Decomposition

Use:

```text
H = [[hmean+shear, off],
     [off, hmean-shear]]
```

Then:

```text
hmean = (Q(e1)+Q(e2))/2
shear = (Q(e1)-Q(e2))/2
off   = (Q(e1+e2)-Q(e1)-Q(e2))/2.
```

## Interpretation

The directional selector does more than trace recovery. It explicitly
separates mean, diagonal shear, and off-diagonal shear. This is the local data
type needed for a tensor boundary term.
