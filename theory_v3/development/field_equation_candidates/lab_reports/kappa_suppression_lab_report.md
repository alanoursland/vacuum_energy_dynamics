# Lab Report: Kappa-Suppression Functional Studies

## Experiments

**Scripts:**

```text
candidate_kappa_suppression_functionals.py
candidate_kappa_suppression_functionals_v2.py
```

**Experiment type:** Reduced-sector symbolic development tests  
**Status:** Exploratory / pedagogical, not formal theory  
**Related prior experiments:**

```text
candidate_log_scale_modes_test.py
candidate_log_scale_modes_test_v2.py
log_scale_modes_lab_report.md
log_scale_modes_v2_lab_report.md
```

## Purpose

The purpose of these experiments was to investigate toy mechanisms that suppress the conformal/uncompensated log-scale mode \(\kappa\) while allowing the compensated/shear mode \(s\) to remain active.

The experiments follow from the log-scale exterior-mode decomposition:

$$a=\ln A,$$

$$b=\ln B,$$

$$\kappa=\frac{a+b}{2},$$

and

$$s=\frac{a-b}{2}.$$

This gives:

$$A=e^{\kappa+s},$$

$$B=e^{\kappa-s},$$

and therefore:

$$AB=e^{2\kappa}.$$

So reciprocal exterior scaling,

$$AB=1,$$

is equivalent, in this reduced sector, to:

$$\kappa=0.$$

The central question was:

```text
Can a source-free exterior functional suppress kappa while allowing nonzero compensated/shear distortion s?
```

This is a reduced-sector version of the P7-style exterior compensation target.

P7 says that static, source-free exterior curvature is compensated temporal-radial redistribution rather than net exterior substance exchange. In the log-scale toy language, that becomes:

```text
source-free exterior: kappa = 0
active exterior field: s != 0
```

## Core Hypothesis

The kappa-suppression studies tested the following hypothesis:

```text
The static source-free exterior should contain a restoring/no-source structure for kappa,
while source/interface physics may seed the compensated/shear mode s.
```

If true, the exterior can carry gravitational distortion in \(s\) while maintaining:

$$\kappa=0,$$

and therefore:

$$AB=1.$$

The failure control is direct \(\kappa\)-sourcing. If either the bulk exterior or the interface directly sources \(\kappa\), then reciprocal scaling should fail generically:

$$\kappa\neq0,$$

so:

$$AB=e^{2\kappa}\neq1.$$

## Experiment 1: Finite-Dimensional Kappa-Suppression Functionals

The first script tested algebraic finite-dimensional toy functionals.

### Case 0: Algebraic Spine

The script confirmed:

$$AB=e^{2\kappa}.$$

Therefore:

$$\kappa=0\Rightarrow AB=1.$$

This establishes \(\kappa\) as the reduced reciprocal-scaling control mode.

### Case 1: Local Potential Suppresses Kappa and Allows Shear

The tested energy was:

$$E=M_\kappa^2\kappa^2+M_s^2(s-S_b)^2.$$

The stationary equations were:

$$2M_\kappa^2\kappa=0,$$

and:

$$2M_s^2(s-S_b)=0.$$

The solution was:

$$\kappa=0,$$

and:

$$s=S_b.$$

Therefore:

$$AB=1.$$

This showed that a local toy potential can suppress \(\kappa\) while allowing an active shear amplitude.

### Case 2: Kappa-Sourced Control

The control energy was:

$$E=M_\kappa^2\kappa^2-J_k\kappa+M_s^2(s-S_b)^2.$$

The stationary equations gave:

$$\kappa=\frac{J_k}{2M_\kappa^2},$$

and:

$$s=S_b.$$

Therefore:

$$AB=e^{J_k/M_\kappa^2}.$$

This fails reciprocal scaling generically.

This control confirms the danger: if \(\kappa\) is directly sourced, reciprocal exterior scaling is not automatic.

### Case 3: Two-Shell Exterior Relaxation

The two-shell toy used two exterior \(\kappa\) variables and two exterior shear variables:

$$\kappa_1,\kappa_2,s_1,s_2.$$

The energy contained \(\kappa\)-suppression terms, \(\kappa\)-gradient/stiffness terms, shear-gradient terms, and a boundary/interface shear seed.

The solution was:

$$\kappa_1=0,$$

$$\kappa_2=0,$$

with nonzero shear values:

$$s_1=\frac{S_b(K_s+M_s^2)}{2K_s+M_s^2},$$

$$s_2=\frac{K_sS_b}{2K_s+M_s^2}.$$

Thus:

$$AB_1=1,$$

and:

$$AB_2=1.$$

This demonstrated that a multi-shell exterior can suppress \(\kappa\) everywhere while allowing shear to propagate outward.

### Case 4: Two-Shell Kappa Boundary-Source Control

The failure control directly seeded \(\kappa\) at the interface.

The solution was:

$$\kappa_1=\frac{K_b(K_k+M_k^2)}{2K_k+M_k^2},$$

and:

$$\kappa_2=\frac{K_bK_k}{2K_k+M_k^2}.$$

Therefore:

$$AB_1=\exp\left(\frac{2K_b(K_k+M_k^2)}{2K_k+M_k^2}\right),$$

and:

$$AB_2=\exp\left(\frac{2K_bK_k}{2K_k+M_k^2}\right).$$

Both fail reciprocal scaling generically.

This case showed that if the interface directly injects \(\kappa\) into the exterior, the exterior no longer satisfies \(AB=1\) unless some additional constraint removes that \(\kappa\) component.

### Case 5: Interface Shear Source with Exterior Kappa Source Absent

This was the strongest finite-shell toy.

The energy was arranged so that \(\kappa\) had suppression and smoothing, \(\kappa\) had no exterior source, shear was seeded by an interface/boundary amplitude, and shear propagated through the exterior.

The solution was:

$$\kappa_1=0,$$

$$\kappa_2=0,$$

and:

$$s_1=\frac{2S_b}{3},$$

$$s_2=\frac{S_b}{3}.$$

Therefore:

$$AB_1=1,$$

and:

$$AB_2=1.$$

This is the clean finite-shell version of the P7-style toy:

```text
source/interface seeds s,
source-free exterior suppresses kappa,
reciprocal scaling holds.
```

## Experiment 2: Continuum Kappa-Suppression Functionals

The second script extended the finite-shell toys toward a continuum-limit picture using symbolic Euler-Lagrange equations.

### Case 0: Algebraic Spine

The continuum script again confirmed:

$$AB=e^{2\kappa},$$

so:

$$\kappa=0\Rightarrow AB=1.$$

### Case 1: Finite Shell Recap

The script repeated the strongest finite-shell result:

$$\kappa_1=0,$$

$$\kappa_2=0,$$

$$s_1=\frac{2S_b}{3},$$

and:

$$s_2=\frac{S_b}{3}.$$

This preserved the result that reciprocal scaling holds while shear remains active.

### Case 2: Finite Shell Kappa-Source Control

The script repeated the interface-\(\kappa\)-source failure control.

Directly seeding \(\kappa\) at the interface produced nonzero \(\kappa_1\) and \(\kappa_2\), causing:

$$AB_1\neq1,$$

and:

$$AB_2\neq1.$$

### Case 3: Continuum Source-Free Exterior

The continuum source-free exterior density was:

$$L=K_\kappa(\kappa')^2+M_\kappa^2\kappa^2+K_s(s')^2+M_s^2s^2.$$

The Euler-Lagrange equations were:

$$-2K_\kappa\kappa''+2M_\kappa^2\kappa=0,$$

and:

$$-2K_s s''+2M_s^2s=0.$$

Substituting:

$$\kappa=0$$

gave:

$$0=0.$$

So \(\kappa=0\) solves the source-free exterior \(\kappa\) equation.

The interpretation is that, with positive \(M_\kappa^2\) and no \(\kappa\) source, the source-free exterior has \(\kappa=0\) as its relaxed solution under zero \(\kappa\) boundary data.

### Case 4: Continuum Kappa-Source Control

The continuum \(\kappa\)-sourced control used:

$$L=-J_k\kappa+K_\kappa(\kappa')^2+M_\kappa^2\kappa^2.$$

The Euler-Lagrange equation was:

$$-J_k-2K_\kappa\kappa''+2M_\kappa^2\kappa=0.$$

For a constant equilibrium, this gives:

$$\kappa=\frac{J_k}{2M_\kappa^2}.$$

Therefore:

$$AB=e^{J_k/M_\kappa^2}.$$

So a bulk \(\kappa\)-source breaks reciprocal scaling generically.

### Case 5: Continuum Boundary-Seeded Shear with Kappa Boundary Zero

This was the strongest continuum toy.

The bulk density was:

$$L_{\rm bulk}=K_\kappa(\kappa')^2+M_\kappa^2\kappa^2+K_s(s')^2.$$

The Euler-Lagrange equations were:

$$-2K_\kappa\kappa''+2M_\kappa^2\kappa=0,$$

and:

$$-2K_s s''=0.$$

The boundary conditions were:

$$\kappa(0)=0,$$

$$\kappa(R)=0,$$

$$s(0)=S_0,$$

and:

$$s(R)=0.$$

The trial solution was:

$$\kappa(r)=0,$$

and:

$$s(r)=S_0\left(1-\frac{r}{R}\right).$$

This satisfied both bulk equations:

$$EL_\kappa=0,$$

and:

$$EL_s=0.$$

Since:

$$\kappa(r)=0,$$

we get:

$$AB=1$$

throughout the exterior.

This is the clean continuum version of the P7-style toy:

```text
interface seeds s,
exterior kappa is unsourced and relaxes to zero,
reciprocal scaling holds throughout the exterior.
```

### Case 6: Continuum Boundary Kappa-Source Control

The failure control seeded \(\kappa\) at the boundary:

$$\kappa(r)=K_0\left(1-\frac{r}{R}\right).$$

Then:

$$AB(r)=\exp\left(\frac{2K_0(R-r)}{R}\right).$$

This fails reciprocal scaling generically.

The lesson is the same as in the finite-shell control: if the interface seeds exterior \(\kappa\), reciprocal scaling is lost unless an additional condition suppresses \(\kappa\).

## Combined Interpretation

The two experiments converge on the same reduced-sector conclusion.

The useful P7-style mechanism is not:

```text
all exchange is trace-free everywhere.
```

That framing caused problems in the previous version of the theory.

The better reduced-sector mechanism is:

```text
source/interface physics may seed compensated shear s,
while the static source-free exterior suppresses or does not source kappa.
```

In equation form:

$$\kappa_{\rm exterior}=0,$$

while:

$$s_{\rm exterior}\neq0.$$

This gives:

$$AB=1$$

with a nontrivial exterior distortion.

The failure mode is also clear:

```text
if the exterior has a bulk or boundary source for kappa,
then reciprocal scaling fails generically.
```

Mathematically:

$$\kappa\neq0\Rightarrow AB=e^{2\kappa}\neq1.$$

## Relationship to P7

P7 says that, in a static source-free exterior vacuum configuration, curvature is compensated directional redistribution rather than net vacuum substance exchange.

The kappa-suppression toy translates this into:

$$\kappa=0.$$

The shear mode \(s\) carries the compensated exterior distortion.

The experiments therefore suggest a possible future route for deriving P7:

```text
Find a covariant configuration-energy functional whose static source-free
exterior reduction contains a kappa-suppression/no-source equation while
allowing boundary-seeded shear.
```

In that future theory, P7 would no longer need to be primitive; exterior compensation would arise from the variational structure; and reciprocal scaling would follow from the exterior solution.

The experiments do not accomplish that derivation. They identify the reduced-sector structure that such a derivation must reproduce.

## Relationship to the Source Law

These experiments do not derive the source law:

$$U=\frac{GM}{r}.$$

The shear mode \(s\) is allowed to be nonzero, but the experiments do not yet derive the correct radial profile for \(s(r)\).

In the continuum Case 5 toy, the massless shear equation:

$$s''=0$$

on a finite interval gave a simple linear interpolation:

$$s(r)=S_0\left(1-\frac{r}{R}\right).$$

That is useful as a boundary-seeded shear toy, but it is not the gravitational source law.

A real exterior field equation must produce the weak-field profile:

$$s(r)\sim -\frac{2GM}{rc^2},$$

or the appropriate coordinate/gauge equivalent.

Therefore the next major research target remains:

```text
derive the exterior shear profile from a mass/interface constraint.
```

## What Was Established

The studies established the following reduced-sector results:

1. \(\kappa\) controls reciprocal scaling because \(AB=e^{2\kappa}\).
2. \(\kappa=0\) gives \(AB=1\).
3. Source-free exterior toy functionals can suppress \(\kappa\).
4. Shear \(s\) can remain active while \(\kappa=0\).
5. Boundary/interface data can seed shear without seeding exterior \(\kappa\).
6. Direct bulk \(\kappa\)-sourcing breaks reciprocal scaling.
7. Direct boundary/interface \(\kappa\)-seeding breaks reciprocal scaling.
8. The finite-shell and continuum toys agree on the same qualitative mechanism.

## What Was Not Established

The studies did not establish a covariant field equation, a covariant parent of \(\kappa\) and \(s\), a derivation of P7 from P1-P6, a source law for \(s(r)\), the Newtonian profile \(U=GM/r\), strong-field behavior, rotating-source behavior, gravitational waves, cosmology, or the full configuration/substance energy bookkeeping.

The experiments remain reduced-sector toy studies.

## Are the Kappa-Suppression Studies Done?

The reduced-sector kappa-suppression phase is basically complete.

The studies have answered the question they were designed to answer:

```text
Can a toy exterior functional suppress kappa while allowing shear?
```

Yes.

They have also answered the failure-control question:

```text
Does kappa sourcing break reciprocal scaling?
```

Yes.

They have identified the cleanest reduced P7-style structure:

```text
source/interface seeds s,
source-free exterior suppresses kappa,
AB=1 follows.
```

So the current kappa-suppression toy program has reached a natural stopping point.

However, the larger research program is not done.

The next phase should not keep adding more \(\kappa\)-suppression toys unless a specific new question appears. The next phase should move up one level and ask:

```text
What is the covariant parent of kappa and s?
```

and:

```text
What source/interface rule produces the exterior shear profile?
```

In other words, the next research stage is no longer simply “can \(\kappa\) be suppressed?” It is:

```text
derive the exterior mode equations and source law from a covariant configuration-energy functional.
```

## Recommended Next Step

The next useful development document or script should focus on the shear/source-law problem.

Possible document:

```text
candidate_exterior_shear_source_law.md
```

or script:

```text
candidate_shear_profile_source_law.py
```

Core question:

```text
Given kappa=0 in the source-free exterior, what equation for s(r) gives
the weak-field exterior profile needed for U=GM/r?
```

Possible toy targets:

1. Treat \(s\) as a harmonic exterior mode.
2. Test whether a radial Laplace equation gives \(s\propto1/r\).
3. Connect the coefficient to a boundary/interface mass parameter.
4. Check that \(s=-2U/c^2\), or the correct convention-compatible equivalent, is recovered.
5. Confirm that \(\kappa=0\) remains intact.

A possible reduced exterior equation is:

$$\nabla^2 s=0$$

outside the source, with spherical solution:

$$s(r)=\frac{C}{r}.$$

Then the source/interface problem becomes:

```text
What fixes C in terms of GM/c^2?
```

This is the next goblin tunnel.
