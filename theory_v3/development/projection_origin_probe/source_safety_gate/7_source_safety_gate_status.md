# Source Safety Gate: Status After Proofs 1-6

## Purpose

This folder reconstructs the archived source-safety guardrails as small
symbolic proofs.

It does not promote the projection hierarchy into a field equation. It proves
the bookkeeping and reduced-flux gates that any later source-origin theorem
must satisfy.

## Proofs Completed

Proof `1` validates the count-once trace incidence gate:

```text
i_Bs + i_res = 1.
```

The clean B_s route is:

```text
i_Bs = 1
i_res = 0.
```

Proof `2` validates residual nonentry:

```text
i_res_metric = 0
i_res_source = 0.
```

Proof `3` validates ordinary source role-purity:

```text
i_A = 1
i_Bs = i_zeta = i_kappa = 0.
```

Proof `4` validates the scalar-tail flux witness:

```text
phi = C0 + C1/r
4*pi*r^2 phi' = -4*pi*C1.
```

Proof `5` validates the current-flux witness:

```text
J_r = I/(4*pi*r^2)
4*pi*r^2 J_r = I.
```

Proof `6` validates the reduced compact-support boundary-flux gate:

```text
phi0*(1-r/R)       -> nonzero boundary flux
phi0*(1-r/R)^2     -> zero boundary flux
phi0*(1-r^2/R^2)^2 -> zero boundary flux.
```

## Interpretation

The source side now has a crisp gate structure:

```text
ordinary matter must enter once;
residual terms must not re-enter as metric or source load;
non-A sectors must not duplicate ordinary source;
scalar tails and far-zone currents must be silent unless explicitly routed;
compact support requires at least flux-safe boundary contact.
```

## Remaining Gap

These proofs are necessary safety gates, not source-origin derivations.

The next proof target is a matter-source-origin theorem:

```text
derive why ordinary source enters the A-sector once,
derive why B_s/residual sectors are source-neutral,
derive why any projection-source vector is formal unless tied to that source law.
```
