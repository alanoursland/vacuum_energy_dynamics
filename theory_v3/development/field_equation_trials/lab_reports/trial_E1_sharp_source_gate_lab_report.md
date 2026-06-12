# Lab Report: Trial E1 -- Sharp-Source Gate (Boundary Admissibility)

## Experiment

**Script:** `vacuum_forge/src/field_equation_trials/009_trial_E_boundary_admissibility/trial_E1_sharp_source_gate.py`
**Experiment type:** Gate derivation + dichotomy theorem (armchair, reduced level)
**Trial:** E (boundary admissibility), registered 2026-06-12 in the charter
**Gates:** E-G1 (sharp-source admissibility), E-G2 (GR control), E-G3 (mechanism classification)
**Status:** VERDICT REACHED -- **UNDERDETERMINED** (constraint-recording, as forecast)
**Run environment:** `cd vacuum_forge/src; PYTHONPATH=. ; python field_equation_trials/009_trial_E_boundary_admissibility/trial_E1_sharp_source_gate.py`
**Run date:** 2026-06-12

## Purpose

Theory-owner intuition under test: *"curvature at mass boundaries must be
smooth in VED because of curvature energy; GR allows non-smooth curvature
but does not require it."* Convert this from an intuition into either a
theorem, a kill, or a sharp question with a kill condition.

## Results

**E1-a (sharp source, reduced VED): ADMITTED.** Solving the derived
areal-flux law with a step density: $[A]=[A']=0$,
$[A'']=-\tfrac{8\pi G}{c^2}\rho_0$ exactly; the derived field energy
$\propto(s')^2$ is continuous and finite across the jump (exterior
integral closed-form finite for $R>r_s$). Nothing in the adopted reduced
theory smooths, forbids, or even notices the edge. **The intuition is not
yet in the theory.**

**E1-b (GR control): verified from scratch.** Interior Schwarzschild
junction at the stellar surface: $[A]=[A']=[B]=0$,
$[B']=3r_s/(R-r_s)^2\neq0$, $G^r{}_r(R^-)=0$ (surface pressure vanishes),
$G^t{}_t$ jumps from $-3r_s/R^3$ to $0$. GR handles the sharp boundary
with no layer and no shell.

**E1-c (dichotomy):**

* **(c1) Transcription theorem.** The C2 self-coupling form
  $\Delta_{\text{areal}}s+(s')^2=\kappa\rho/A$ is identically the areal
  law; any second-order response algebraic in the source *requires*
  $[s'']\neq0$ given a sharp source and yields smooth curvature given a
  smooth source. **At this level reduced VED and GR are identical:
  curvature smoothness equals source smoothness, both ways, in both
  theories.** (This settles the Opus discussion: "GR requires the jump"
  is true *given* sharp matter; neither theory constrains the matter edge
  itself -- and currently neither does VED.)
* **(c2) No energy barrier.** Smoothing a curvature kink over width
  $\ell$ changes the derived $(s')^2$ energy by $\Delta E = 4\ell^3/15
  \to 0$. The derived energy cannot dynamically prefer smooth boundaries;
  P5 has no lever, and the static sector is source-slaved anyway (G02).
* **(c3) The mechanism.** Add a curvature-energy term $\beta(s'')^2$ and
  the response becomes fourth order; for the curvature $v=s''$ the
  equation is $\beta v''-v=\kappa\rho$, whose bounded solution across a
  step source has $v$ and $v'$ **continuous**, transitioning over the
  derived width
  $$\ell^* = \sqrt{\beta}.$$
  The smooth-boundary intuition is *exactly* the statement $\beta\neq0$
  in $K_{\text{strain}}$. Cost: fourth-order dynamics faces the
  Ostrogradsky/G20 ghost gate (healthy only for degenerate structures --
  the $f(R)$-class loophole).

## Verdict

```text
Trial E1: UNDERDETERMINED at reduced level (constraint-recording).
The intuition is neither earned nor killed. It is now EQUIVALENT to
one sharp question: does K_strain contain higher-curvature energy?
  beta != 0  =>  minimum smoothing scale ell* = sqrt(beta) at matter
                 boundaries (testable deviation from GR) + G20 gate
  beta  = 0  =>  intuition dies honestly; VED = GR at boundaries
```

## Record correction

The old transition-layer program (groups 052--065) was quarantined
diagnostic-only (065) and the boundary-lift route adopted no axiom
(078--080): **the old corpus never derived a forced layer.** Earlier
chat statements suggesting "covariant conservation forced finite-width
profiles" overstated it. The intuition's formal support is the (c3)
mechanism derived here, not the old program. Separately: the projection
ladder's proved selection ($m=2$) sits at $R=0$ -- boundedness, the
weakest regularity rung -- so the ladder forces *admissibility*, not
smoothness.

## Relation to the program

Third exported constraint on $K_{\text{strain}}$ in two days (after the
static normalization and the shear/TT relative weight): its
higher-curvature content now carries a physical meaning -- it *is* the
boundary-smoothness question -- and a prediction shape ($\ell^*$) in the
κ-leak family of parameter-free-or-derived deviations. Obligations
registered: the $\beta$ decision; G20 health if $\beta\neq0$; the
unexplored matter-side route (P6 back-reaction smoothing $\rho$ itself
rather than the response).

## Next steps

1. When candidate $K_{\text{strain}}$ forms are written, evaluate
   $\beta$ first -- it is the cheapest physical discriminator the parent
   now owes.
2. If $\beta\neq0$ survives G20, estimate $\ell^*$ against the
   short-range data gates (the same Casimir-sector apparatus as the
   UFFT squeeze).
3. Matter-side smoothing route (P6 edge back-reaction): currently
   unexplored; would smooth $\rho$ rather than the response.
