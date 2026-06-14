# 9. Kill Conditions and Empirical Checks

Only Newton's constant is used as an empirical normalization. The remaining
observational anchors enter after derivation as kill conditions.

| channel | derived content | possible failure |
|---|---|---|
| Newtonian limit | fixes `G` normalization | wrong inverse-square limit |
| weak-field metric | `gamma = 1`, `beta = 1` | light deflection, Shapiro, perihelion mismatch |
| gravitational radiation | quadrupole coefficient `G/5c^5` | binary-pulsar or GW energy-loss mismatch |
| vector sector | Lense-Thirring normalization | GPB/LAGEOS-class frame-dragging mismatch |
| four-derivative sector | no `a R^2` scalaron | gravitational-strength Yukawa detection |
| boundary behavior | no smoothing scale | observed static boundary smoothing |
| kappa leak | cosmological trace correction tiny | honesty entry, not practical target |

The short-range gravity channel is especially important conceptually. The
four-derivative scalar would have produced a Yukawa correction with scalaron
coupling `alpha = 1/3`. P7-prime eliminates that route, so the theory predicts
no gravitational-strength Yukawa signal from this sector. The current
`ShortRangeGravity` v1 data gate contains two validated 95%-CL curves:
Lee 2020 [Lee et al., 2020] gives the `alpha = 1/3` crossing at `54.03 um`,
and Tan 2020 [Tan et al., 2020] gives `57.29 um`. Lee is binding in this
window. The earlier vector-path extraction from Lee Fig. 5 [Lee et al., 2020]
gave `54.05 um`, so the supplemental-table value is cross-checked at the
level relevant here. The theory's prediction is a null result, not a
near-threshold signal.

This structure makes the empirical posture unusual but clean. The theory does
not currently advertise an accessible gravitational deviation from GR. Its
tested gravitational sector is GR. The empirical risk lies in null tests of
the commitments that closed the theory.
