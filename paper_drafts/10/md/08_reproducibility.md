# 8. Reproducibility

Every equation in this paper is elementary enough to check by hand,
and all of them have also been verified symbolically. Two computer
algebra scripts accompany the paper as supplementary material. The
first verifies the family: the resummation identity of Sec. 2.1, the
Bernoulli solution and its special members, the series coefficients,
the two-shell ledger integrals of Sec. 4 under both matter
conventions, the factor-of-four corollary, the isotropic transform
with $\gamma = 1$ and $\beta = \lambda + 2$, and the horizon zero-set
(17 checks). The second verifies the Painlevé–Gullstrand material of
Sec. 6: that the metric with $v = c\sqrt{r_s/r}$ is an exact vacuum
solution with the Schwarzschild curvature invariant, that
$\tfrac12 v^2 = GM/r$ holds at every radius, that $v = c$ at $r_s$,
and the $\gamma$ discriminator against the escape-velocity route
(11 checks). The scripts use SymPy, run from a clean environment in
under a few minutes, and re-derive their results from scratch on each
execution rather than replaying stored values.

[Archive DOI and repository reference to be inserted at submission;
see TODO. An AI-assistance disclosure conforming to the venue's policy
will be included here.]
