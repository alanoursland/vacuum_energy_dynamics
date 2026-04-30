# Lab Report: Candidate Log-Scale Exterior Modes v2

## Experiment

**Script:** `candidate_log_scale_modes_test_v2.py`  
**Experiment type:** VacuumForge reduced-sector development test  
**Status:** Exploratory / pedagogical, not formal theory  
**Related note:** `candidate_log_scale_exterior_modes.md`  
**Related prior report:** `log_scale_modes_lab_report.md`

## Purpose

The purpose of the v2 experiment was to improve the original log-scale mode test by making the derivation pipeline explicit.

The original experiment confirmed the algebraic usefulness of the log-scale variables, but the requirement validator initially failed to recognize derived reciprocal-scaling results because derived consequences were recorded in the assumptions store and the leak detector did not respect the `status="derived"` field.

After fixing the leak detector so that derived records are not treated as raw premises, this v2 run tests whether the forge can distinguish:

1. a direct tautological assumption,
2. a structural trace-kernel derivation,
3. a generic \(\kappa\)-sourced failure case,
4. and an interface/source-to-exterior separation toy that matches the current P7-style exterior framing.

The central reduced-sector question remains:

```text
Can the static source-free exterior suppress the conformal/uncompensated mode kappa while allowing the compensated/shear mode s?
```

## Mode Definitions

The static exterior metric factors are written as:

$$a=\ln A,$$

and

$$b=\ln B.$$

The log-scale modes are:

$$\kappa=\frac{a+b}{2},$$

and

$$s=\frac{a-b}{2}.$$

Equivalently,

$$a=\kappa+s,$$

and

$$b=\kappa-s.$$

Therefore,

$$A=e^{\kappa+s},$$

and

$$B=e^{\kappa-s}.$$

Multiplying the metric factors gives:

$$AB=e^{2\kappa}.$$

Thus:

$$\kappa=0 \quad \Rightarrow \quad AB=1.$$

This makes \(\kappa\) the reduced-sector variable that measures failure of reciprocal exterior scaling.

The shear or compensated mode \(s\) remains active when \(\kappa=0\). In this reduced language, static exterior gravity should live in \(s\), not in \(\kappa\).

## Hypothesis

The v2 experiment tested the following claims.

First, the algebraic spine should hold:

$$\kappa=0 \Rightarrow AB=1.$$

Second, under the weak-field gamma ansatz,

$$A=e^{\Phi/c^2},$$

$$B=e^{-\gamma_v\Phi/c^2},$$

reciprocal scaling should imply:

$$\gamma_v=1.$$

Third, direct insertion of \(\delta\kappa=0\) should be flagged as tautological.

Fourth, a pre-mode trace-kernel source rule should be able to derive \(J_\kappa=0\) non-tautologically.

Fifth, a toy quadratic exterior energy should produce:

$$\kappa_{\rm eq}=0$$

when

$$J_\kappa=0,$$

but should produce:

$$\kappa_{\rm eq}\neq0$$

when

$$J_\kappa\neq0.$$

Sixth, the source/interface-to-exterior separation toy should allow an exterior shear mode \(s\neq0\) while still suppressing \(\kappa\) in the source-free exterior.

## Leak Detector Fix

The earlier v2 run revealed a tooling issue.

The script recorded derived results such as:

$$\kappa=0,$$

and

$$AB=1$$

with `status="derived"`.

However, the leak detector iterated over all active assumption records without checking the status field. It therefore treated derived bookkeeping entries as if they were raw assumptions. This made derived \(\kappa=0\) and derived \(AB=1\) look like leaked targets.

The fix was to make the leak detector respect provenance: derived records should not be treated as premise leaks.

After this fix, the same v2 experiment correctly distinguished derived-and-recorded results from smuggled assumptions.

## Results

### Section 1: Algebraic Spine

The script computed:

$$A=e^{\kappa+s},$$

$$B=e^{\kappa-s},$$

and:

$$AB=e^{2\kappa}.$$

With \(\kappa=0\), it found:

$$AB=1.$$

This passed.

The weak-field ansatz test used:

$$A=e^{\Phi/c^2},$$

and:

$$B=e^{-\Phi\gamma_v/c^2}.$$

The product was:

$$AB=e^{\Phi(1-\gamma_v)/c^2}.$$

Taking the logarithm gave:

$$\ln(AB)=\frac{\Phi(1-\gamma_v)}{c^2}.$$

Solving \(AB=1\) gave:

$$\gamma_v=1.$$

This passed.

### Case A: Direct Mode Assumption

Case A directly defined the exchange operator with:

$$\delta\kappa=0.$$

The analyzer classified this case as **tautological**.

It found:

$$J_a=S,$$

$$J_b=-S,$$

$$J_\kappa=0,$$

and:

$$J_s=2S.$$

VacuumForge correctly emitted a leak warning that the exchange operator explicitly zeroed all trace-contributing variables.

This is the desired result. Directly inserting \(\delta\kappa=0\) is not a derivation of trace-free exchange. It is a control case showing what a smuggled conclusion looks like.

### Case B: Structural Trace-Kernel Exterior

Case B used a physical 3+1 pre-mode projection:

$$a=q_t,$$

$$b=\frac{q_x+q_y+q_z}{3}.$$

The trace vector is:

$$\left[1,\frac13,\frac13,\frac13\right].$$

The exchange direction was:

$$(-S,S,S,S).$$

This satisfies the trace-kernel condition:

$$-1+\frac{1+1+1}{3}=0.$$

VacuumForge found:

$$J_a=-S,$$

$$J_b=S,$$

$$J_\kappa=0,$$

and:

$$J_s=-2S.$$

It classified this as **derived**, not tautological.

The toy exterior energy equilibrium then gave the stationary equations:

$$2C_\kappa\kappa=0,$$

and:

$$2C_\sigma s-J_s=0.$$

The solution was:

$$\kappa_{\rm eq}=0,$$

and:

$$s_{\rm eq}=\frac{J_s}{2C_\sigma}.$$

The script then recorded the reciprocal chain:

$$\kappa=0 \Rightarrow AB=1 \Rightarrow \gamma_v=1.$$

After the leak-detector fix, requirement validation passed:

- reciprocal scaling passed,
- \(\gamma_v=1\) passed,
- positive energy passed,
- leak detection was clean.

This is the cleanest positive result of the experiment.

### Case C: Generic Kappa-Sourced Exchange

Case C used a generic exchange source with:

$$J_\kappa=J_k,$$

and:

$$J_s=J_s.$$

The stationary equations were:

$$2C_\kappa\kappa-J_k=0,$$

and:

$$2C_\sigma s-J_s=0.$$

The solution was:

$$\kappa_{\rm eq}=\frac{J_k}{2C_\kappa},$$

and:

$$s_{\rm eq}=\frac{J_s}{2C_\sigma}.$$

Therefore:

$$AB=e^{2\kappa_{\rm eq}}=e^{J_k/C_\kappa}.$$

So reciprocal scaling does not follow generically.

Requirement validation correctly failed reciprocal scaling and \(\gamma_v=1\). Trace-free exchange also failed, as expected, because the exchange source had nonzero \(J_\kappa\).

This is the necessary failure control.

### Case D: Interface/Source-to-Exterior Separation Toy

Case D modeled the current framework’s distinction between source/interface behavior and static source-free exterior behavior.

The toy interpretation was:

```text
Source/interface physics may seed a boundary shear amplitude.
The exterior region itself is source-free and has J_kappa_ext = 0.
```

The stationary equations were:

$$2C_\kappa\kappa=0,$$

and:

$$2C_\sigma s-S_{\rm boundary}=0.$$

The solution was:

$$\kappa_{\rm eq}=0,$$

and:

$$s_{\rm eq}=\frac{S_{\rm boundary}}{2C_\sigma}.$$

Thus the exterior suppresses the conformal/uncompensated mode while retaining an active compensated/shear mode.

The script recorded:

$$\kappa=0 \Rightarrow AB=1 \Rightarrow \gamma_v=1.$$

After the leak-detector fix, requirement validation passed:

- reciprocal scaling passed,
- \(\gamma_v=1\) passed,
- positive energy passed,
- leak detection was clean.

This case is the best reduced-sector analogue of the current P7-style exterior-compensation picture.

## Interpretation

The v2 experiment confirms that the log-scale mode decomposition is a useful reduced-sector laboratory for the static exterior problem.

The key identity is:

$$AB=e^{2\kappa}.$$

Therefore, the P7 reciprocal-scaling target becomes:

$$\kappa=0.$$

The experiment also clarifies what must be avoided.

If \(\kappa=0\) is inserted directly as a mode-basis assumption, the result is tautological.

If \(\kappa\) is generically sourced, reciprocal scaling fails:

$$AB=e^{J_k/C_\kappa}.$$

The interesting middle path is structural or dynamical \(\kappa\)-suppression:

```text
derive or dynamically enforce J_kappa = 0 in the static source-free exterior,
while allowing the compensated/shear mode s to remain active.
```

Case B shows one reduced algebraic route: a pre-mode exchange direction can lie in the trace kernel and thereby produce \(J_\kappa=0\).

Case D shows the framework-relevant route: source/interface behavior may seed exterior shear, while the source-free exterior suppresses \(\kappa\).

## Relationship to P7

P7 states that in a static, source-free exterior vacuum configuration, temporal and radial distortions compensate:

$$A(r)B(r)=1.$$

The log-scale experiment rewrites this as:

$$\kappa=0.$$

Case D gives a toy version of how this could coexist with source/interface physics:

- the source or interface supplies a boundary shear amplitude,
- the exterior carries compensated distortion \(s\),
- the exterior has no \(\kappa\) source,
- exterior equilibrium gives \(\kappa=0\).

This does not derive P7. It gives a reduced algebraic laboratory for the type of deeper field-equation mechanism that would derive P7.

## What Was Actually Established

This experiment established:

1. \(\kappa\) is the correct reduced mode for reciprocal scaling.
2. \(\kappa=0\) implies \(AB=1\).
3. \(AB=1\) implies \(\gamma_v=1\) under the weak-field ansatz used in the test.
4. Direct \(\delta\kappa=0\) insertion is tautological.
5. A 3+1 pre-mode trace-kernel exchange can derive \(J_\kappa=0\) non-tautologically.
6. A toy quadratic energy with \(J_\kappa=0\) gives \(\kappa_{\rm eq}=0\).
7. A toy quadratic energy with \(J_\kappa\neq0\) gives \(\kappa_{\rm eq}\neq0\) and breaks reciprocal scaling.
8. A source/interface-to-exterior separation toy can keep \(s\neq0\) while suppressing exterior \(\kappa\).

## What Was Not Established

This experiment did not establish a full field equation.

It did not derive P7 from P1–P6.

It did not derive the source law:

$$U=\frac{GM}{r}.$$

It did not derive the strong-field metric.

It did not address rotating sources, frame dragging, gravitational waves, cosmology, or nonspherical configurations.

It did not prove that the physical vacuum must choose the trace-kernel exchange direction.

It did not prove that source-free exterior \(\kappa\)-suppression follows from a covariant action.

The experiment is a reduced algebraic and energy-equilibrium sanity test.

## Conclusion

The v2 experiment strengthens the case for using log-scale exterior modes as a development tool.

The useful reduced-sector dictionary is:

$$\kappa=\frac{\ln A+\ln B}{2},$$

and:

$$s=\frac{\ln A-\ln B}{2}.$$

In this language:

$$AB=e^{2\kappa}.$$

Therefore, P7-style exterior compensation is equivalent to:

$$\kappa=0.$$

The forge confirms that if a source-free exterior law suppresses \(\kappa\) while allowing \(s\), then reciprocal scaling and \(\gamma_v=1\) follow cleanly in the reduced weak-field setting.

The forge also confirms that if \(\kappa\) is generically sourced, reciprocal scaling fails.

Thus the sharpened research target is:

```text
Find a covariant source law, boundary/interface rule, or configuration-energy
functional that suppresses kappa in static source-free exterior configurations
while allowing compensated shear s.
```

## Next Experiment

The next useful experiment should go beyond algebraic source-coupled energy and test candidate exterior functionals for \(\kappa\)-suppression.

Possible next script:

```text
candidate_kappa_suppression_functionals.py
```

Suggested tests:

1. A mass-like exterior penalty:

$$E_\kappa=\int M_\kappa^2\kappa^2\,dr.$$

2. A gradient stiffness penalty:

$$E_\kappa=\int K_\kappa(\kappa')^2\,dr.$$

3. A combined exterior functional:

$$E_{\rm ext}=\int dr\,w(r)\left[K_\kappa(\kappa')^2+M_\kappa^2\kappa^2+K_s(s')^2+V_s(s)\right].$$

4. Boundary conditions where source/interface physics sets \(s\) but not exterior \(\kappa\).

5. A check that the exterior solution suppresses \(\kappa\) without forcing \(s=0\).

6. A check that the result is not equivalent to assuming \(AB=1\) directly.

The key next question is:

```text
Can kappa suppression be made a consequence of exterior variational dynamics,
rather than an imposed exterior condition?
```
