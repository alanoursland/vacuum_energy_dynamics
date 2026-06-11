# Lab Report: Candidate Exchange / Creation Distinction Test

## Experiment

**Script:** `candidate_exchange_creation_distinction_test.py`  
**Experiment type:** Reduced-sector operator classification test  
**Status:** Exploratory / pedagogical, not formal theory  
**Development unit:** Exchange / creation / relaxation regime classification

## Purpose

The purpose of this experiment was to test whether the proposed distinction between exchange, creation/destruction, and relaxation is algebraically consistent with the reduced \(\kappa/s\) exterior mode program.

The motivating issue came from the P3 volume-preservation study. That study showed that P1 and P3 identify vacuum energy with vacuum volume:

$$E_{\rm vac}=\rho_v V_{\rm vac}.$$

Therefore, if a local process preserves vacuum energy, it also preserves vacuum volume:

$$\delta E_{\rm vac}=0
\quad\Longleftrightarrow\quad
\delta V_{\rm vac}=0.$$

However, P1 and P3 do not decide whether a local vacuum process is conservative exchange or net creation/destruction. That classification must be supplied or derived separately.

This experiment therefore tested the candidate classification:

```text
exchange:
  conservative local redistribution
  expected J_kappa = 0

creation:
  positive local vacuum amount change
  expected J_kappa > 0

destruction:
  negative local vacuum amount change
  expected J_kappa < 0

relaxation:
  energy-descent / fill-in response
  expected to drive kappa toward zero when unsourced
```

The goal was not to prove that nature uses these regimes. The goal was to check whether the classification behaves correctly inside the reduced mode algebra.

---

## Reduced Mode Setup

The reduced exterior variables are:

$$a=\ln A,$$

and:

$$b=\ln B.$$

The mode decomposition is:

$$\kappa=\frac{a+b}{2},$$

and:

$$s=\frac{a-b}{2}.$$

The source projections are:

$$J_\kappa=\frac{J_a+J_b}{2},$$

and:

$$J_s=\frac{J_a-J_b}{2}.$$

The product of metric factors is:

$$AB=e^{2\kappa}.$$

Therefore:

$$\kappa=0 \quad \Longleftrightarrow \quad AB=1.$$

The reduced equilibrium toy used:

$$E(\kappa,s) =
C_\kappa\kappa^2
+
C_s s^2
-
J_\kappa\kappa
-
J_s s.$$

Stationarity gives:

$$\kappa_{\rm eq}=\frac{J_\kappa}{2C_\kappa},$$

and:

$$s_{\rm eq}=\frac{J_s}{2C_s}.$$

Thus any operator with:

$$J_\kappa=0$$

does not source the reciprocal-scaling control mode, while any operator with:

$$J_\kappa\neq0$$

generically breaks reciprocal scaling.

---

## Case 0: P1 + P3 Bookkeeping Identity

The script first checked the bookkeeping identity.

P1 says vacuum is energy. P3 says local vacuum energy density is constant. Therefore:

$$E_{\rm vac}=\rho_v V_{\rm vac}.$$

The variation is:

$$\delta E_{\rm vac}=\rho_v\delta V_{\rm vac}.$$

Since \(\rho_v\) is nonzero and constant:

$$\delta E_{\rm vac}=0
\quad\Longleftrightarrow\quad
\delta V_{\rm vac}=0.$$

This passed.

The important interpretation is that energy preservation and volume preservation are equivalent under P1 and P3. But this does not decide whether a process is exchange or creation/destruction. That distinction must be supplied or derived separately.

---

## Case 1: Reduced Operator Classification

The script tested four reduced operator types.

### Exchange

The exchange operator was:

$$J_a=S,$$

and:

$$J_b=-S.$$

Then:

$$J_\kappa=\frac{S-S}{2}=0,$$

and:

$$J_s=\frac{S-(-S)}{2}=S.$$

The reduced volume / trace source is proportional to:

$$J_a+J_b=0.$$

So the exchange operator is trace-kernel, volume-preserving, and shear-active.

This passed.

### Creation

The creation operator was:

$$J_a=C,$$

and:

$$J_b=C.$$

Then:

$$J_\kappa=C,$$

and:

$$J_s=0.$$

The reduced volume / trace source is:

$$J_a+J_b=2C.$$

So creation is traceful and not volume-preserving.

This passed.

### Destruction

The destruction operator was:

$$J_a=-C,$$

and:

$$J_b=-C.$$

Then:

$$J_\kappa=-C,$$

and:

$$J_s=0.$$

The reduced volume / trace source is:

$$J_a+J_b=-2C.$$

So destruction is traceful and not volume-preserving.

This passed.

### Mixed Exchange Plus Creation

The mixed operator was:

$$J_a=S+C,$$

and:

$$J_b=-S+C.$$

Then:

$$J_\kappa=C,$$

and:

$$J_s=S.$$

So the mixed operator contains both compensated shear and traceful creation.

This passed.

---

## Case 2: Equilibrium Consequences

The script then computed reduced equilibrium consequences for each operator.

### Exchange Equilibrium

For exchange:

$$J_\kappa=0,$$

and:

$$J_s=S.$$

The energy was:

$$E=C_\kappa\kappa^2+C_s s^2-Ss.$$

Stationarity gave:

$$\kappa_{\rm eq}=0,$$

and:

$$s_{\rm eq}=\frac{S}{2C_s}.$$

Therefore:

$$AB=1.$$

This confirms that exchange supports active shear while preserving reciprocal scaling.

### Creation Equilibrium

For creation:

$$J_\kappa=C,$$

and:

$$J_s=0.$$

The energy was:

$$E=C_\kappa\kappa^2+C_s s^2-C\kappa.$$

Stationarity gave:

$$\kappa_{\rm eq}=\frac{C}{2C_\kappa},$$

and:

$$s_{\rm eq}=0.$$

Therefore:

$$AB=e^{C/C_\kappa}.$$

This breaks reciprocal scaling generically.

### Destruction Equilibrium

For destruction:

$$J_\kappa=-C,$$

and:

$$J_s=0.$$

The energy was:

$$E=C_\kappa\kappa^2+C_s s^2+C\kappa.$$

Stationarity gave:

$$\kappa_{\rm eq}=-\frac{C}{2C_\kappa},$$

and:

$$s_{\rm eq}=0.$$

Therefore:

$$AB=e^{-C/C_\kappa}.$$

This also breaks reciprocal scaling generically.

### Mixed Equilibrium

For mixed exchange plus creation:

$$J_\kappa=C,$$

and:

$$J_s=S.$$

The energy was:

$$E=C_\kappa\kappa^2+C_s s^2-C\kappa-Ss.$$

Stationarity gave:

$$\kappa_{\rm eq}=\frac{C}{2C_\kappa},$$

and:

$$s_{\rm eq}=\frac{S}{2C_s}.$$

Therefore:

$$AB=e^{C/C_\kappa}.$$

The mixed operator has both active shear and traceful \(\kappa\)-sourcing. This is a useful possible deviation channel: gravity-like shear plus traceful leakage.

---

## Case 3: Relaxation as Energy Descent

The script tested an unsourced relaxation energy:

$$E=C_\kappa\kappa^2+C_s s^2.$$

The gradients were:

$$\frac{\partial E}{\partial\kappa}=2C_\kappa\kappa,$$

and:

$$\frac{\partial E}{\partial s}=2C_s s.$$

A gradient descent flow gives:

$$\frac{d\kappa}{d\tau}=-2C_\kappa\kappa,$$

and:

$$\frac{ds}{d\tau}=-2C_s s.$$

The energy decreases as:

$$\frac{dE}{d\tau} =
-4C_\kappa^2\kappa^2
-
4C_s^2s^2.$$

This is negative away from equilibrium.

The unsourced relaxation endpoint is:

$$\kappa=0,$$

and:

$$s=0.$$

The interpretation is that relaxation drives \(\kappa\) toward zero, but exterior gravity requires \(s\) to remain nonzero through boundary/source data or a shear source law.

This passed.

---

## Case 4: Relaxation with Boundary-Maintained Shear

The script then tested relaxation with boundary-maintained shear:

$$E=C_\kappa\kappa^2+C_s(s-S_b)^2.$$

Stationarity gave:

$$\kappa_{\rm eq}=0,$$

and:

$$s_{\rm eq}=S_b.$$

Therefore:

$$AB=1.$$

This confirms that relaxation can suppress \(\kappa\) while preserving nonzero shear when shear is maintained by boundary/interface data.

This is the relaxation endpoint most relevant to static exterior gravity.

---

## Case 5: Classification Consistency Matrix

The resulting classification was:

| Regime | Local energy / volume | \(J_\kappa\) | \(\kappa_{\rm eq}\) | \(AB\) | Interpretation |
|---|---:|---:|---:|---:|---|
| Exchange | \(0\) | \(0\) | \(0\) | \(1\) | conservative shear redistribution |
| Creation | \(>0\) | \(>0\) | \(>0\) | \(\neq1\) | traceful vacuum amount increase |
| Destruction | \(<0\) | \(<0\) | \(<0\) | \(\neq1\) | traceful vacuum amount decrease |
| Mixed | \(\neq0\) | \(\neq0\) | \(\neq0\) | \(\neq1\) | shear plus creation/destruction |
| Relaxation endpoint | response-dependent | \(\to0\) if unsourced | \(0\) | \(1\) | balanced static exterior |

The matrix separates exchange from creation/destruction cleanly.

---

## Case 6: Impact on the P3 Volume-Preservation Question

The earlier question was:

```text
Does P3 force exchange to preserve volume?
```

The reformulated answer is:

```text
P1 + P3 make energy preservation equivalent to volume preservation.
But P1 + P3 do not decide whether a process is exchange or creation.
```

This script therefore treated exchange, creation, destruction, and relaxation as operator classes and checked their reduced consequences.

The result is:

```text
If exchange is defined as conservative redistribution, then it is trace-kernel
and gives J_kappa = 0 in the reduced model.

Creation/destruction are traceful and may source kappa.
```

The open question remains:

```text
Can the exchange/creation distinction be derived from the postulates,
or must it be added as a structural principle?
```

---

## Main Result

The experiment supports the proposed regime classification.

Exchange behaves as the static exterior gravity channel:

$$J_\kappa=0,$$

$$s_{\rm eq}\neq0,$$

$$\kappa_{\rm eq}=0,$$

and:

$$AB=1.$$

Creation/destruction behave as traceful vacuum-amount changes:

$$J_\kappa\neq0,$$

$$\kappa_{\rm eq}\neq0,$$

and:

$$AB\neq1$$

generically.

Relaxation behaves as a balancing or fill-in response:

$$\kappa\to0$$

when unsourced, while nonzero \(s\) can remain if maintained by boundary/source data.

This is algebraically consistent with the reduced exterior mode program.

---

## Interpretation

The experiment gives a clean structure:

```text
exchange supplies compensated shear;
relaxation suppresses imbalance;
creation/destruction are traceful regimes.
```

This allows the theory to keep static exterior gravity in the compensated regime:

$$\kappa=0,\qquad s\neq0,$$

without forbidding vacuum creation/destruction in other regimes.

That matters because cosmological expansion or boundary growth may require vacuum amount change. The theory should not outlaw that possibility simply to make static gravity easier.

Instead, the theory can classify regimes:

```text
static exterior gravity:
  exchange / relaxation endpoint

cosmic expansion:
  possible creation / traceful growth

non-equilibrium events:
  possible mixed or transition regimes
```

This is more flexible than treating all vacuum dynamics as conservative exchange.

---

## What Was Established

This study established:

1. Under P1+P3, energy preservation and volume preservation are equivalent.
2. P1+P3 do not classify whether a process is exchange or creation.
3. Exchange, if defined as conservative redistribution, is trace-kernel in the reduced model.
4. Exchange gives \(J_\kappa=0\), \(\kappa_{\rm eq}=0\), and \(AB=1\).
5. Exchange can support active shear \(s\).
6. Creation and destruction are traceful in the reduced model.
7. Creation/destruction source \(\kappa\) and break reciprocal scaling generically.
8. Mixed operators contain both shear and traceful \(\kappa\)-sourcing.
9. Relaxation decreases reduced configuration energy.
10. Relaxation can suppress \(\kappa\) while boundary/source data maintain \(s\).

---

## What Was Not Established

This study did not prove that nature uses the proposed regimes.

It did not derive the exchange/creation distinction from existing postulates.

It did not prove that static exterior gravity is purely exchange.

It did not prove that cosmological expansion is vacuum creation.

It did not derive a field equation for creation/destruction.

It did not connect traceful regimes to observational cosmology.

It did not prove that mixed \(\kappa\)-leak regimes occur physically.

It only showed that the proposed classification is algebraically consistent with the reduced mode model.

---

## Relationship to Previous Work

This lab report connects several prior threads.

The P3 volume-preservation test showed that P1+P3 identify energy and volume but do not define exchange.

The reduced exterior mode program showed that \(\kappa=0\) gives reciprocal scaling and that \(s\) can carry the exterior gravitational distortion.

The reduced action toy showed that \(\kappa\)-suppression and shear sourcing can coexist in one variational structure.

The current experiment classifies the process types that can feed those modes:

```text
exchange -> shear without kappa
creation/destruction -> kappa
relaxation -> kappa suppression / fill-in
```

This helps prevent a premature assumption that all vacuum dynamics are conservative exchange.

---

## Next Development Targets

There are two natural next targets.

### 1. Observational Regime Map

A useful next document would be:

```text
candidate_regime_map_observations.md
```

Its purpose would be to map the candidate regimes to observational domains:

```text
static exterior gravity -> exchange / relaxation
cosmological expansion -> creation / traceful growth
gravitational waves -> exchange-like vacuum propagation?
black holes / collapse -> destruction, compression, or boundary regime?
laboratory tests -> constraints on kappa-leak / traceful deviations
```

This would help determine where the theory could be tested or contradicted.

### 2. Kappa-Leak Deviation Study

A useful future script would be:

```text
candidate_kappa_leak_deviation.py
```

Its purpose would be to test what happens when a mixed operator produces small but nonzero \(\kappa\):

$$\kappa=\varepsilon_\kappa(r).$$

Then:

$$AB=e^{2\varepsilon_\kappa}.$$

This could produce deviations from GR-like reciprocal scaling.

This may become important for novel predictions.

---

## Conclusion

The candidate exchange / creation distinction test passed.

It supports the regime classification:

```text
exchange:
  conservative redistribution
  trace-kernel
  kappa_eq = 0
  AB = 1
  shear active

creation/destruction:
  net vacuum amount change
  traceful
  kappa_eq != 0
  AB != 1 generically

relaxation:
  energy descent / fill-in
  can drive kappa -> 0
  can coexist with boundary-maintained shear
```

The result does not prove the ontology, but it gives a coherent reduced algebraic structure.

The main unresolved question is now sharp:

```text
Is the exchange/creation distinction derived from the existing postulates,
or must it become a separate structural principle?
```

The next useful step is to map the regimes to observational domains.
