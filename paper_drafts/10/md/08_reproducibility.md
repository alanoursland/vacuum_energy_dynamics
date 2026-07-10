# 8. Reproducibility

Every equation in this paper is elementary enough to check by hand,
and the principal results have also been verified symbolically. Two
standalone computer-algebra scripts accompany the paper. The first
verifies the resummation identity and family of Sec. 2, its special
members and horizon dichotomy, the complete two-shell ledger of
Sec. 4, the factor-of-four corollary, the isotropic transformation and
PPN dictionary, and the vacuum response selector (21 checks). The
second independently verifies the Michell radius, the family-wide
horizon dichotomy, the $\gamma$ discriminator, and the
Painlevé–Gullstrand results of Sec. 6: vacuum curvature, the
Schwarzschild invariant, $\tfrac12v^2=GM/r$, and $v(r_s)=c$
(11 checks).

The scripts require only Python 3.11 or newer and SymPy 1.12 or newer.
They rederive all results on each execution, write no files, and are
provided with a requirements file and run instructions in
`supplement/`.

[Archive DOI and repository reference to be inserted at submission;
see TODO. An AI-assistance disclosure conforming to the venue's policy
will be included here.]
