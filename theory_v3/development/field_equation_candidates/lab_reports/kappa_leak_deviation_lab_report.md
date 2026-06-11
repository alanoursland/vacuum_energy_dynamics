# Lab Report: Kappa-Leak Deviation Study

## Experiment

**Script:** `candidate_kappa_leak_deviation.py`  
**Experiment type:** Reduced weak-field deviation probe  
**Status:** Exploratory / pedagogical, not formal theory  
**Development unit:** Reduced exterior deviations / mixed-regime behavior

## Purpose

The purpose of this experiment was to study the first clean deviation channel identified by the reduced exterior mode program:

```text
What happens if the static exterior is mostly compensated shear,
but contains a small nonzero kappa component?
```

The reduced exterior program established:

$$\kappa=\frac{\ln A+\ln B}{2},$$

and:

$$s=\frac{\ln A-\ln B}{2}.$$

Therefore:

$$A=e^{\kappa+s},$$

and:

$$B=e^{\kappa-s}.$$

Multiplying gives:

$$AB=e^{2\kappa}.$$

The baseline compensated exterior has:

$$\kappa=0,$$

and:

$$s=-2\epsilon,$$

where:

$$\epsilon=\frac{GM}{rc^2}.$$

This gives:

$$A=e^{-2\epsilon}\approx1-2\epsilon,$$

and:

$$B=e^{2\epsilon}\approx1+2\epsilon,$$

with:

$$AB=1.$$

The current experiment introduced a small nonzero \(\kappa\)-leak:

$$\kappa=\lambda_k\epsilon,$$

while keeping the baseline shear:

$$s=-2\epsilon.$$

The goal was to identify how this leak changes \(A\), \(B\), \(AB\), and a gamma-like weak-field response proxy.

---

## Background

The exchange / creation distinction study showed:

```text
exchange:
  J_kappa = 0
  shear active
  AB = 1

creation/destruction:
  J_kappa != 0
  traceful
  AB != 1 generically

mixed:
  J_kappa != 0 and J_s != 0
  shear plus traceful leakage
```

This suggests that a small \(\kappa\)-leak may arise from a mixed regime:

```text
mostly exchange-like shear,
plus small traceful creation/destruction component.
```

The present study asks what the weak-field metric consequences would be in the reduced areal-gauge model.

---

## Case 0: Baseline Compensated Exterior

The baseline model was:

$$\kappa=0,$$

and:

$$s=-2\epsilon.$$

Therefore:

$$A=e^{\kappa+s}=e^{-2\epsilon},$$

and:

$$B=e^{\kappa-s}=e^{2\epsilon}.$$

The product is:

$$AB=1.$$

The series expansions were:

$$A=1-2\epsilon+2\epsilon^2+\cdots,$$

and:

$$B=1+2\epsilon+2\epsilon^2+\cdots.$$

The script confirmed:

```text
A first order is 1 - 2 eps
B first order is 1 + 2 eps
AB = 1 exactly
```

This reproduces the baseline compensated exterior result.

---

## Case 1: Constant Fractional Kappa Leak

The first deviation model was:

$$\kappa=\lambda_k\epsilon,$$

and:

$$s=-2\epsilon.$$

Then:

$$A=e^{\kappa+s}=e^{(\lambda_k-2)\epsilon},$$

and:

$$B=e^{\kappa-s}=e^{(\lambda_k+2)\epsilon}.$$

The product is:

$$AB=e^{2\lambda_k\epsilon}.$$

Expanding to first order:

$$A\approx1+(\lambda_k-2)\epsilon,$$

$$B\approx1+(\lambda_k+2)\epsilon,$$

and:

$$AB\approx1+2\lambda_k\epsilon.$$

The script confirmed all three first-order coefficients.

This makes \(\lambda_k\) a clean reduced deviation parameter.

When:

$$\lambda_k=0,$$

the model returns to the compensated exterior.

When:

$$\lambda_k\neq0,$$

reciprocal scaling is broken:

$$AB\neq1.$$

---

## Case 2: Gamma-Like Proxy

The script derived a gamma-like weak-field proxy.

Start with:

$$A\approx1+(\lambda_k-2)\epsilon.$$

Define the observed Newtonian potential coefficient \(\epsilon_N\) by matching:

$$A\approx1-2\epsilon_N.$$

Then:

$$\epsilon_N=\frac{2-\lambda_k}{2}\epsilon.$$

The spatial coefficient is:

$$B\approx1+(\lambda_k+2)\epsilon.$$

Match this to:

$$B\approx1+2\gamma_{\rm eff}\epsilon_N.$$

Then:

$$2\gamma_{\rm eff}\epsilon_N=(\lambda_k+2)\epsilon.$$

Substitute \(\epsilon_N\):

$$2\gamma_{\rm eff}\left(\frac{2-\lambda_k}{2}\epsilon\right) =
(\lambda_k+2)\epsilon.$$

Therefore:

$$\gamma_{\rm eff} =
\frac{2+\lambda_k}{2-\lambda_k}.$$

The script output the equivalent symbolic form:

$$\gamma_{\rm eff}=\frac{-\lambda_k-2}{\lambda_k-2},$$

which simplifies to:

$$\gamma_{\rm eff}=\frac{2+\lambda_k}{2-\lambda_k}.$$

The deviation is:

$$\gamma_{\rm eff}-1 =
\frac{2\lambda_k}{2-\lambda_k}.$$

For small \(\lambda_k\):

$$\gamma_{\rm eff} =
1+\lambda_k+\frac{\lambda_k^2}{2}+\cdots.$$

So:

$$\gamma_{\rm eff}-1\approx\lambda_k.$$

This is the main observational-pressure result.

A small \(\kappa\)-leak maps directly to a gamma-like weak-field deviation at leading order.

---

## Case 3: Newtonian Temporal Normalization Pressure

The script then tested a stronger condition.

If:

$$\epsilon=\frac{GM}{rc^2}$$

is already fixed by observed Newtonian acceleration, then the temporal coefficient must be:

$$A\approx1-2\epsilon.$$

But with constant fractional \(\kappa\)-leak:

$$A\approx1+(\lambda_k-2)\epsilon.$$

Matching the Newtonian temporal coefficient requires:

$$\lambda_k-2=-2.$$

Therefore:

$$\lambda_k=0.$$

The script confirmed this.

This is a significant constraint on the simplest leak model.

A constant proportional \(\kappa\)-leak cannot simply be added to ordinary static gravity while keeping the same Newtonian mass normalization. It either changes the observed temporal potential coefficient or must be absorbed into a redefinition of source strength.

This means ordinary weak-field static \(\kappa\)-leak is likely highly constrained.

---

## Case 4: Decaying Kappa-Leak Profile

The script tested a decaying leak profile:

$$\kappa(r)=\eta\epsilon e^{-r/L},$$

where:

$$\epsilon=\frac{GM}{rc^2}.$$

The baseline shear remained:

$$s(r)=-2\epsilon.$$

Then:

$$A=e^{\eta\epsilon e^{-r/L}-2\epsilon},$$

and:

$$B=e^{\eta\epsilon e^{-r/L}+2\epsilon}.$$

The product is:

$$AB=e^{2\eta\epsilon e^{-r/L}}.$$

The leak ratio is:

$$\frac{\kappa}{\epsilon}=\eta e^{-r/L}.$$

Thus the gamma-like deviation proxy is approximately:

$$\gamma_{\rm eff}-1\approx\eta e^{-r/L}$$

for small leak.

This profile vanishes at large radius and may be more observationally plausible than a constant fractional leak.

The script confirmed that the decaying leak vanishes asymptotically.

---

## Case 5: Power-Law Kappa-Leak Profile

The script also tested a power-law leak profile:

$$\kappa(r)=\eta\epsilon\left(\frac{R_0}{r}\right)^n.$$

Again:

$$s(r)=-2\epsilon.$$

The product is:

$$AB=e^{2\kappa(r)}.$$

The leak ratio is:

$$\frac{\kappa}{\epsilon}=\eta\left(\frac{R_0}{r}\right)^n.$$

For:

$$n>0,$$

the leak becomes smaller at large radius.

For:

$$n=0,$$

the profile reduces to the constant fractional leak case.

The script confirmed this profile as a tunable deviation model.

---

## Case 6: Mixed Exchange + Creation Source as Kappa-Leak Origin

The script connected \(\kappa\)-leak to the exchange/creation regime classification.

A mixed source was modeled by:

$$J_\kappa=C,$$

and:

$$J_s=S.$$

The reduced equilibrium energy was:

$$E=C_\kappa\kappa^2+C_s s^2-C\kappa-Ss.$$

Stationarity gave:

$$\kappa_{\rm eq}=\frac{C}{2C_\kappa},$$

and:

$$s_{\rm eq}=\frac{S}{2C_s}.$$

The metric product becomes:

$$AB=e^{2\kappa_{\rm eq}}=e^{C/C_\kappa}.$$

The script confirmed:

```text
mixed source produces nonzero kappa leak
mixed source preserves shear channel
mixed source breaks reciprocal scaling generically
```

This gives a possible reduced origin for \(\kappa\)-leak:

```text
ordinary exchange supplies compensated shear,
while a small traceful creation/destruction component leaks into kappa.
```

---

## Case 7: Observational Pressure Summary

The script summarized the observational pressure:

For:

$$\kappa=\lambda_k\epsilon,$$

and:

$$s=-2\epsilon,$$

the weak-field coefficients are:

$$A\approx1+(\lambda_k-2)\epsilon,$$

and:

$$B\approx1+(\lambda_k+2)\epsilon.$$

The gamma-like proxy is:

$$\gamma_{\rm eff}=\frac{2+\lambda_k}{2-\lambda_k}.$$

For small leak:

$$\gamma_{\rm eff}-1\approx\lambda_k.$$

Therefore, ordinary static exterior \(\kappa\)-leak should be very small or hidden in regimes where weak-field constraints do not apply.

The script did not apply real observational bounds. It identified the reduced deviation proxy.

---

## Main Result

The experiment established \(\kappa\)-leak as the first clean reduced deviation channel.

The key relation is:

$$\gamma_{\rm eff} =
\frac{2+\lambda_k}{2-\lambda_k}.$$

For small leak:

$$\gamma_{\rm eff}-1\approx\lambda_k.$$

So a small nonzero \(\kappa\) in an otherwise compensated exterior would appear as a gamma-like weak-field deviation.

This suggests that static weak-field observations tightly constrain ordinary \(\kappa\)-leak.

---

## Interpretation

The baseline exterior is:

```text
pure exchange / relaxation endpoint
```

with:

$$\kappa=0,$$

and:

$$s=-2\epsilon.$$

A mixed regime introduces:

```text
exchange-like shear plus traceful creation/destruction leakage
```

which gives:

$$\kappa\neq0.$$

This changes both temporal and radial weak-field coefficients and breaks:

$$AB=1.$$

The simplest constant leak model is under strong pressure because it changes the Newtonian temporal coefficient unless \(\lambda_k=0\).

More plausible leak models would need to be:

```text
short-range,
environment-dependent,
source-interface-dependent,
confined to strong-field regions,
or dynamically suppressed in ordinary weak-field exteriors.
```

---

## What Was Established

This study established:

1. The baseline compensated exterior gives \(A\approx1-2\epsilon\), \(B\approx1+2\epsilon\), and \(AB=1\).
2. A constant fractional \(\kappa\)-leak gives \(A\approx1+(\lambda_k-2)\epsilon\).
3. The same leak gives \(B\approx1+(\lambda_k+2)\epsilon\).
4. The product becomes \(AB\approx1+2\lambda_k\epsilon\).
5. A gamma-like proxy is:
   $$\gamma_{\rm eff}=(2+\lambda_k)/(2-\lambda_k).$$
6. For small leak:
   $$\gamma_{\rm eff}-1\approx\lambda_k.$$
7. Newtonian temporal normalization forces \(\lambda_k=0\) in the simplest constant-leak model if \(\epsilon=GM/(rc^2)\) is already fixed.
8. Decaying and power-law leak profiles can represent localized or suppressed deviations.
9. Mixed exchange+creation sources naturally generate \(\kappa\)-leak in the reduced model.
10. \(\kappa\)-leak is a promising but highly constrained deviation channel.

---

## What Was Not Established

This study did not perform a full PPN derivation.

It did not apply real observational bounds.

It did not prove that \(\lambda_k\) is identical to a formal PPN parameter.

It did not derive \(\kappa\)-leak from a covariant field equation.

It did not show that \(\kappa\)-leak exists physically.

It did not determine whether decaying or power-law leak profiles are allowed by the full theory.

It did not address strong fields, time dependence, gravitational waves, or cosmology.

This is a reduced areal-gauge weak-field toy.

---

## Relationship to the Reduced Exterior Program

This study fits naturally after the reduced exterior mode program.

The stable branch established:

$$\kappa=0,\qquad s\neq0$$

as the static source-free exterior compensated sector.

The current study asks what happens when:

$$\kappa\neq0$$

slightly.

The result is that \(\kappa\) directly controls deviation from reciprocal scaling:

$$AB=e^{2\kappa}.$$

It also controls a gamma-like response proxy.

Therefore \(\kappa\)-leak is the natural first deviation channel for the theory.

---

## Relationship to Regime Classification

The exchange/creation distinction test showed:

```text
exchange -> J_kappa = 0
creation/destruction -> J_kappa != 0
mixed -> J_kappa != 0 and J_s != 0
```

The present study shows that mixed regimes can produce weak-field deviations through \(\kappa\)-leak.

Thus the regime map becomes:

```text
static exterior exchange / relaxation:
  kappa = 0
  GR-like weak-field recovery

mixed exchange + creation/destruction:
  kappa != 0
  possible deviation channel

creation / traceful growth:
  likely not ordinary static exterior gravity
  possibly cosmological or boundary regime
```

---

## Next Development Targets

### 1. Observational Constraint Note

A useful next document would be:

```text
candidate_kappa_leak_observational_constraints.md
```

Purpose:

```text
Map the gamma-like proxy to known weak-field constraints carefully.
```

This should be done cautiously because the current \(\gamma_{\rm eff}\) is only a reduced proxy, not yet a full PPN parameter.

### 2. Kappa-Leak Profile Study

A possible next script:

```text
candidate_kappa_leak_profiles.py
```

Purpose:

```text
Explore decaying, power-law, source-radius, and environment-dependent leak profiles.
```

### 3. Covariant Parent Work

A deeper next target remains:

```text
candidate_orbit_space_modes.py
```

Purpose:

```text
Find a gauge-aware or covariant parent for kappa and s.
```

This is necessary before making strong observational claims.

---

## Conclusion

The kappa-leak deviation study passed.

It identifies the first clear reduced deviation parameter:

$$\lambda_k.$$

For:

$$\kappa=\lambda_k\epsilon,$$

and:

$$s=-2\epsilon,$$

the weak-field metric factors become:

$$A\approx1+(\lambda_k-2)\epsilon,$$

and:

$$B\approx1+(\lambda_k+2)\epsilon.$$

The gamma-like proxy is:

$$\gamma_{\rm eff} =
\frac{2+\lambda_k}{2-\lambda_k}.$$

For small leak:

$$\gamma_{\rm eff}-1\approx\lambda_k.$$

Thus ordinary static exterior \(\kappa\)-leak should be tightly constrained. This makes \(\kappa\)-leak a useful deviation channel, but also a dangerous one for the theory.

The next step is to connect this reduced proxy to observational constraints carefully, without overclaiming a full PPN derivation.
