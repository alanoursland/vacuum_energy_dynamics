# Lab Report: Trial E3 -- P7' Kills the Smooth-Boundary Route; the Four-Derivative Sector Closes

## Experiment

**Script:** `vacuum_forge/src/field_equation_trials/009_trial_E_boundary_admissibility/trial_E3_p7prime_vs_scalaron.py`
**Experiment type:** Candidate parent write-down + contradiction theorem + sector closure
**Trial:** E (boundary admissibility), conclusion of the E1/E2/G20 arc
**Status:** VERDICT REACHED -- smooth-boundary route **KILLED_BY_CONTRADICTION** (with P7'); $K_{\text{strain}}$ at $\le4$ derivatives **CLOSED**
**Run environment:** `cd vacuum_forge/src; PYTHONPATH=. ; python field_equation_trials/009_trial_E_boundary_admissibility/trial_E3_p7prime_vs_scalaron.py`
**Run date:** 2026-06-12
**Dependencies verified:** C3 t-r block identity; P7' adoption record; G20 $\alpha=1/3$ solution; E1 fourth-order matching.

## Purpose

Write down the first ledger-assembled candidate parent at $\le4$-derivative
order and test it against the *adopted postulates* -- not just the gates:

$$K_1:\quad S=\frac{c^4}{16\pi G}\!\int\!\sqrt{-g}\,(R-2\Lambda)
\;+\;a\!\int\!\sqrt{-g}\,R^2\;(+\,\text{Gauss-Bonnet})$$

By 008 and G20 this is the *only* shape allowed, with one free
coefficient: $a$, the smooth-boundary coefficient.

## Results

**T1 (the hair violates P7''s shadow).** The areal-gauge identity at
linear order is $AB-1 = 2(\phi+r\psi')/c^2$ (transform verified from
scratch). On the GR exterior ($\phi=\psi=-GM/r$): exactly zero. On the
G20 scalaron exterior: **nonzero everywhere within $\ell^*$ of the
surface** (strictly negative, $\propto e^{-r/\ell^*}$). By C3's
response-independent identity ($G^t{}_t-G^r{}_r = -(\ln AB)'/(rB)$ for
*any* static spherical metric), the hair region is a static vacuum
configuration with a preferred t-r frame. The violator is the $R^2$
response term itself: $D^t{}_t-D^r{}_r=-R''$ -- the same scalar-gradient
anisotropy pattern C3-2 used to kill explicit-source placement.

**T2 (the hair is mandatory).** Fourth-order matching (R and R'
continuous, from E1-c3) admits no hairless exterior: eliminating the
interior constant requires $x\cosh x=\sinh x$ for $x=mR_b>0$, impossible
since $h(x)=x\cosh x-\sinh x$ has $h(0)=0$, $h'=x\sinh x>0$. **Every
static star leaks scalaron hair for any $a\neq0$.** The P7' violation is
not a choice the theory can decline; it comes with the coefficient.

**T3 (the contradiction).**
$$\text{P7}' \;(\text{adopted, exact at } H\to0)\;+\;\text{T1}\;+\;\text{T2}
\;\Longrightarrow\; a=0.$$
The smooth-boundary route -- E1's $\beta$ mechanism, E2's bench-top face,
G20's surviving scalaron class -- dies **by postulate**: not by data, not
by ghosts. The theory's own frame-indifference statement forbids the
hair that smoothing requires.

**T4 (sector closure).** With $a=0$:
$$\boxed{\;K_{\text{strain}}\ (\le4\ \text{derivatives})
=\frac{c^4}{16\pi G}\,(R-2\Lambda)\;+\;\text{Gauss-Bonnet}\quad\text{exactly}\;}$$
Zero free coefficients. All local gravitational physics of VED = GR:
statics, radiation, stability, and now boundaries.

## Verdict

```text
Trial E RESOLVED (was UNDERDETERMINED at E1):
  VED boundary behavior is IDENTICAL to GR. Curvature jumps at sharp
  matter edges are transcribed, not smoothed. The smooth-boundary
  intuition is KILLED -- by P7', the theory's own adopted postulate.

Candidate K1 RESOLVED: the parent's <= 4-derivative sector is closed,
  every coefficient derived. VED's novelty budget now lives entirely in:
  (1) the kappa-leak channel AB - 1 = O(H_0 r/c)   [P7' at the limit]
  (2) Lambda's origin                              [frustration floor]
  (3) the B2 measure/matter sector
  (4) the interior cap                             [engineering seam]
  (5) the dark sector as excess EoS                [Trial D2]
```

**P7' gains a second observable face.** VED-with-P7' predicts **no**
gravitational-strength Yukawa at *any* range: the micron window becomes
a null test. A bench-top $|\alpha|\sim O(1)$ detection would force the
P7' appeal. (The UFFT squeeze is unaffected: $a_{\rm disc}$ is a
Casimir-sector parameter, not a gravitational Yukawa.)

## The appeal path (theory-owner decision, default = kill stands)

P7' could be re-scoped (to the two-derivative sector, or to
$r\gg\ell^*$) to save the smoothing route. Recorded as an open
obligation, with the cost stated: P7' was adopted as an ontology
statement about the static vacuum, and the hair *is* static vacuum -- a
carve-out without independent grounding would be recovery-shaped, the
exact failure mode the trials program was built to avoid.

## Relation to the program

This is the program's first kill **by adopted postulate** -- the
strongest kind, because it demonstrates the postulates have nontrivial
consequences (a postulate set that never forbids anything isn't a
theory). It is also the first time a candidate parent was written down
and a sector of it fully closed. Arc summary: E1 turned an intuition
into a coefficient; E2 bounded the coefficient with existing data; G20
reduced it to one realization; E3 showed the adopted ontology sets it to
zero. Four scripts from intuition to resolution, with every step either
a theorem or a recorded decision.

## Next steps

1. Theory-owner: P7' scope review (the standing appeal; default kill).
2. With the local sector closed, the live frontier is items (1)-(5)
   above; Trial B2 (the measure bridge's physical identity) is the most
   theory-shaped, and the kappa-leak/cosmology branch is where P7' at
   the limit does new work.
3. Data program unchanged in priority: alpha(lambda) digitization now
   serves the UFFT squeeze AND the P7' null test.
