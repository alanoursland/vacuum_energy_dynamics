# Lab Report: Gate G20 (beta health) -- One Ghost-Safe Realization, and It Has No Free Choices Left

## Experiment

**Script:** `vacuum_forge/src/field_equation_trials/010_gate_G20_beta_health/gate_G20_beta_health.py`
**Experiment type:** Gate derivation / channel classification / coefficient closure (armchair, linear order)
**Gate:** G20 (higher-curvature ghost health), run for the Trial E smooth-boundary route
**Status:** GATE RUN COMPLETE -- scalaron class PASSES, Weyl class KILLED, $\alpha = +1/3$ derived
**Run environment:** `cd vacuum_forge/src; PYTHONPATH=. ; python field_equation_trials/010_gate_G20_beta_health/gate_G20_beta_health.py`
**Run date:** 2026-06-12
**Dependencies verified:** E1 beta-smoothing mechanism; E2 Yukawa-face identity; G03 TT positivity.

## Purpose

E1 reduced the smooth-boundary intuition to $\beta\neq0$ in
$K_{\text{strain}}$ and flagged the Ostrogradsky/G20 gate. E2 showed the
same $\beta$ is a bench-top Yukawa and left the amplitude $\alpha$ as an
obligation ("naive scalar gives $-1$, f(R)-class gives $+1/3$; the parent
must say which"). This script runs the gate and closes the obligation:
the parent does not get to choose -- the gate chooses.

## Results

**T1 (linearized identities + scalaron health).** From scratch:
$R^{(1)}_{tt}=\Delta\phi$ and
$R^{(1)}=\tfrac{2}{c^2}(2\Delta\psi-\Delta\phi)$ for the static
weak-field metric. The $R+aR^2$ trace equation is
$(1-6a\Delta)R^{(1)}=\kappa\rho c^2$: a **healthy massive scalar** (the
scalaron) with $m^2=1/(6a)$ for $a>0$; $a<0$ is a tachyon (flat-vacuum
instability, G02-class kill). E1's toy maps as $\beta_{\rm eff}=6a$,
$\ell^*=\sqrt{6a}$.

**T2 (the one-third, exactly).** Solving the closed linear system for a
point source -- away-from-origin residuals and delta bookkeeping (flux
lemmas) all verified exactly:
$$\phi(r)=-\frac{GM}{r}\Big[1+\tfrac13 e^{-r/\ell^*}\Big],\qquad
\psi(r)=-\frac{GM}{r}\Big[1-\tfrac13 e^{-r/\ell^*}\Big].$$
$$\boxed{\alpha=+\tfrac13\ \text{exactly, POSITIVE (attractive excess)}}$$
Bonus signature: $\gamma_{\rm eff}=\psi/\phi\to\tfrac12$ inside $\ell^*$
(the classic f(R) value), screened to $1$ outside -- solar-system safe
because $\ell^*<38.6\,\mu$m.

**T3 (radiative sector untouched).** $R^{(1)}$ of a TT perturbation
vanishes identically, so $R^2$ adds nothing to the TT propagator: the
derived $K_T$ and the G03 positivity/stability results carry over
unchanged. The scalaron smooths boundaries *without touching the healthy
positive sector*.

**T4 (Weyl class killed).** Any quadratic-curvature term that reaches
the TT channel gives the quartic propagator whose massive spin-2 pole
has residue $-1$ (the E2 partial fraction) in a sector that **is**
dynamical (G03): a genuine ghost, excluded by the same stability
argument that caged the temporal sector. Gauss-Bonnet is the inert
exception (topological in 4D). Recorded FAILED_BY_WITNESS.

## Verdict

```text
G20: the smooth-boundary route survives in EXACTLY ONE form.
  realization:  a R^2 (a > 0) + Gauss-Bonnet
  scalaron:     healthy, m^2 = 1/(6a)
  smoothing:    ell* = sqrt(6a)
  bench-top:    alpha = +1/3 exactly, positive sign
  bound:        ell* < the alpha = 1/3 crossing of the exclusion curves
  radiative:    untouched
  PPN:          gamma_eff = 1/2 inside ell*, screened outside
```

**Falsifiers now attached to the route:**
1. a bench-top Yukawa detection with *negative* $\alpha$ at micron range
   (would kill the ghost-safe realization -- and a negative-$\alpha$
   signal is itself a ghost diagnostic);
2. the $\alpha=+1/3$ exclusion pushed below the parent's natural $\ell^*$;
3. any required quartic TT content in the parent.

E2's obligation `parent_alpha_value_e2` is **discharged** (SATISFIED,
conditional on ghost safety).

## Honesty ledger

- Linear order throughout; the bench-top reading assumes an unscreened
  scalaron. Chameleon-type screening for pure $R^2$ is registered as an
  open obligation before the $\alpha=1/3$ crossing is treated as exact.
- The Weyl-class kill is reduced-level (propagator residue + G03
  dynamics); the covariant statement rides with the K_strain lifts.

## Relation to the program

The Trial E arc is now a complete pipeline from intuition to experiment:
E1 (intuition $\to$ $\beta$), E2 ($\beta$ $\to$ bench-top window), G20
($\beta$ $\to$ unique realization with fixed $\alpha$, sign, and
signatures). $K_{\text{strain}}$'s constraint ledger after this gate:
static normalization $N=c^4/8\pi G$; TT weight $K_T=c^4/16\pi G$;
quadratic-curvature content restricted to $aR^2\,(a>0)$ + Gauss-Bonnet,
with the single remaining freedom $a$ bounded by bench-top data and
carrying the entire smooth-boundary question. The unwritten parent now
has remarkably little room to be anything.

## Next steps

1. $\alpha(\lambda)$ digitization: read the $\alpha=1/3$ crossing -- now
   the precise cap on $\ell^*$ for the unique surviving realization.
2. Scalaron screening estimate for pure $R^2$ (bound-reading rigor).
3. With the quadratic sector this constrained, a first candidate
   $K_{\text{strain}}$ write-down is becoming feasible: EH + $aR^2$ +
   the B1 measure structure is nearly forced at two-derivative and
   four-derivative order.
