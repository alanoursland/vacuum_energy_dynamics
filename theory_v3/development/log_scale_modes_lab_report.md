# Lab Report: Candidate Log-Scale Exterior Modes Experiment

## Experiment

**Script:** `candidate_log_scale_modes_test.py`  
**Experiment type:** VacuumForge reduced-sector development test  
**Status:** Pedagogical / exploratory, not formal theory  
**Related note:** `candidate_log_scale_exterior_modes.md`

## Purpose

The purpose of this experiment was to test the algebraic core of the candidate log-scale exterior mode language.

The candidate introduces logarithmic variables for the static exterior metric factors:

$$a=\ln A,$$

$$b=\ln B,$$

and defines the modes

$$\kappa=\frac{a+b}{2},$$

$$s=\frac{a-b}{2}.$$

Here, \(\kappa\) is interpreted as the conformal, uncompensated, or measure-changing mode, while \(s\) is interpreted as the shear, compensated, or reciprocal mode.

The target claim was:

$$\kappa=0 \quad \Rightarrow \quad A B = 1.$$

Since \(A(r)B(r)=1\) is the reciprocal exterior scaling condition used in P7/T3, the experiment asked whether \(\kappa\) is the right reduced variable for studying exterior compensation.

The secondary goal was to distinguish three cases:

1. Directly assuming \(\delta\kappa=0\), which should be classified as tautological.
2. Deriving \(J_\kappa=0\) from a pre-mode trace-kernel structure, which should count as a structural derivation.
3. Comparing a \(\kappa\)-suppressed toy energy fork against a \(\kappa\)-sourced toy energy fork.

## Hypothesis

The log-scale mode language should make reciprocal scaling algebraically transparent.

Specifically:

$$A=e^{\kappa+s},$$

$$B=e^{\kappa-s},$$

so

$$AB=e^{2\kappa}.$$

Therefore, if a future exterior field equation or source law can show

$$\kappa=0,$$

then reciprocal exterior scaling follows immediately:

$$AB=1.$$

With the weak-field ansatz

$$A=e^{\Phi/c^2},$$

$$B=e^{-\gamma_v\Phi/c^2},$$

the condition \(AB=1\) should imply

$$\gamma_v=1.$$

The experiment was expected to show that the log-scale variables are useful, but that the real physics problem remains open: deriving why static source-free exterior configurations suppress \(\kappa\) without simply assuming it.

## Setup

The script tested five sections:

1. Pure algebra of the log-scale variables.
2. Leak control in the direct \((\kappa,s)\) mode basis.
3. Structural trace-kernel exchange in a physical 3+1 pre-mode projection.
4. Toy energy fork comparison: trace-conserving versus \(\kappa\)-sourced exchange.
5. Interpretive verdict.

The physical 3+1 pre-mode projection used:

$$a=q_t,$$

$$b=\frac{q_x+q_y+q_z}{3}.$$

The trace vector was therefore:

$$\left[1,\frac13,\frac13,\frac13\right].$$

A trace-free exchange direction was chosen as:

$$(-S,S,S,S),$$

which satisfies:

$$-1+\frac{1+1+1}{3}=0.$$

## Results

### 1. Algebraic identity

The script found:

$$A=e^{\kappa+s},$$

$$B=e^{\kappa-s},$$

and therefore:

$$AB=e^{2\kappa}.$$

Setting \(\kappa=0\) gave:

$$AB=1.$$

This passed.

The weak-field ansatz test produced:

$$A=e^{\Phi/c^2},$$

$$B=e^{-\Phi\gamma_v/c^2},$$

so:

$$AB=e^{\Phi(1-\gamma_v)/c^2}.$$

Taking the logarithm gave:

$$\ln(AB)=\frac{\Phi(1-\gamma_v)}{c^2}.$$

Solving \(AB=1\) gave:

$$\gamma_v=1.$$

This also passed.

### 2. Leak control

The direct mode-basis test defined exchange by directly setting:

$$\delta\kappa=0.$$

VacuumForge classified this as **tautological**, not derived.

The exchange produced:

$$J_a=S,$$

$$J_b=-S,$$

$$J_\kappa=0,$$

$$J_s=2S.$$

The tool emitted a leak warning because the exchange operator explicitly zeroed all trace-contributing variables. This is the desired behavior. Directly defining exchange as \(\delta\kappa=0\) is not an explanation of trace-free exchange; it is an assumption inserted into the operator.

### 3. Structural trace-kernel exchange in 3+1

The physical 3+1 projection test used:

$$a=q_t,$$

$$b=\frac{q_x+q_y+q_z}{3}.$$

The trace vector was:

$$\left[1,\frac13,\frac13,\frac13\right].$$

For the exchange direction

$$\delta(q_t,q_x,q_y,q_z)=(-S,S,S,S),$$

VacuumForge found:

$$J_a=-S,$$

$$J_b=S,$$

$$J_\kappa=0,$$

$$J_s=-2S.$$

This was classified as **derived**, not tautological.

Creation was also checked. Symmetric creation produced:

$$J_a=C,$$

$$J_b=C,$$

$$J_\kappa=2C,$$

$$J_s=0.$$

This was classified as pure trace.

This result is important because it shows that \(J_\kappa=0\) can arise structurally from a pre-mode exchange direction lying in the kernel of the trace projection.

### 4. Toy energy fork comparison

The toy energy functional had the source-coupled quadratic structure:

$$E\sim C_\kappa\kappa^2+C_s s^2-J_\kappa\kappa-J_s s.$$

The trace-conserving fork used:

$$J_\kappa=0.$$

The stationary equations were:

$$2C_\kappa\kappa=0,$$

$$2C_s s-J_s=0.$$

The solution was:

$$\kappa=0,$$

$$s=\frac{J_s}{2C_s}.$$

This is the desired exterior-compensation behavior: the conformal/uncompensated mode is suppressed, while the shear/compensated mode remains active.

The \(\kappa\)-sourced fork used:

$$J_\kappa=J_k.$$

The stationary equations were:

$$2C_\kappa\kappa-J_k=0,$$

$$2C_s s-J_s=0.$$

The solution was:

$$\kappa=\frac{J_k}{2C_\kappa},$$

$$s=\frac{J_s}{2C_s}.$$

This gives:

$$AB=e^{2\kappa}=e^{J_k/C_\kappa}.$$

Therefore, reciprocal scaling does not follow generically in the \(\kappa\)-sourced fork.

### 5. Validation bookkeeping issue

The requirement validation comparison reported failures for reciprocal scaling and \(\gamma_v=1\) even in the trace-conserving fork.

This was not a failure of the algebraic result. It was a context bookkeeping issue in the script.

The trace-conserving fork found:

$$\kappa_{\rm eq}=0.$$

The script correctly printed the consequence:

$$\kappa=0\Rightarrow AB=1\Rightarrow\gamma_v=1.$$

However, it did not insert the derived assumption \(\gamma_v=1\) back into the VacuumForge context before running the general requirement validator. Therefore, the validator still saw the free-\(\gamma_v\) ansatz:

$$AB=e^{-\Phi\gamma_v/c^2+\Phi/c^2},$$

and correctly reported that reciprocal scaling had not yet been registered inside the context.

This is a script-pipeline issue, not a theoretical contradiction.

## Interpretation

The experiment supports the usefulness of the log-scale exterior mode language.

The strongest result is:

$$AB=e^{2\kappa}.$$

This means \(\kappa\) is exactly the reduced-sector mode that measures failure of reciprocal scaling.

In the static spherical exterior sector:

- \(\kappa=0\) means reciprocal compensation.
- \(s\neq0\) carries the allowed compensated exterior gravitational distortion.
- P7 can be written as the reduced-sector statement \(\kappa=0\).

The experiment also confirms the old warning from the previous theory-development scripts: reciprocal scaling does not follow from a generic source-coupled energy unless the \(\kappa\) mode is unsourced or otherwise suppressed. If exchange sources \(\kappa\), then:

$$\kappa_{\rm eq}\neq0,$$

and:

$$AB\neq1.$$

So the central future task remains unchanged:

**Find a non-tautological source law, constraint rule, or configuration-energy functional that suppresses \(\kappa\) in static source-free exterior configurations while allowing \(s\neq0\).**

## Pedagogical Value

This experiment is useful because it cleanly separates three levels:

### Algebraic identity

$$\kappa=0\Rightarrow AB=1.$$

This is confirmed.

### Structural trace-kernel derivation

A pre-mode exchange direction can yield \(J_\kappa=0\) without directly defining \(\delta\kappa=0\). This is confirmed in the 3+1 isotropic time-vs-space exchange example.

### Physical theory

The framework still needs a reason why the static source-free exterior should select the trace-kernel / \(\kappa\)-suppressed behavior. This remains open.

The experiment therefore sharpens the research target rather than solving it.

## Conclusion

The candidate log-scale exterior mode language survives its first VacuumForge sanity test.

The main confirmed result is:

$$\kappa=\frac{\ln A+\ln B}{2}$$

is the correct reduced variable for tracking reciprocal exterior scaling, because:

$$AB=e^{2\kappa}.$$

The candidate is not a field equation and does not derive P7. It provides a useful mode language in which the P7 target becomes:

$$\kappa=0.$$

The experiment also confirms that directly imposing \(\delta\kappa=0\) is tautological, while deriving \(J_\kappa=0\) from a pre-mode trace-kernel structure is non-tautological in the reduced algebraic setting.

The next experiment should patch the validation context so that, after \(\kappa_{\rm eq}=0\) is derived, the script records:

$$AB=1,$$

and:

$$\gamma_v=1,$$

then reruns requirement validation. After that, the next substantive experiment should test candidate exterior energy functionals that suppress \(\kappa\) dynamically or by constraint, rather than by direct assumption.

## Next Experiment

Suggested next script:

```text
candidate_log_scale_modes_test_v2.py
```

Recommended changes:

1. After the trace-conserving fork derives \(\kappa_{\rm eq}=0\), add the derived result \(AB=1\) to the context.
2. Derive \(\gamma_v=1\) from \(AB=1\) and add it as a derived context result.
3. Rerun requirement validation after recording those derived consequences.
4. Add a non-tautological toy penalty test, such as:

$$E_\kappa\sim M_\kappa^2\kappa^2,$$

with no direct \(\kappa\) source, to test whether exterior relaxation suppresses \(\kappa\).
5. Add a source/interior comparison where \(\kappa\) is allowed inside or at the interface but relaxes to zero outside.

The most important future question is:

```text
Can kappa be sourced in substance-regime or interface regions,
while still being suppressed in the static source-free exterior?
```

That question connects the log-scale mode experiment to the current formal framework’s distinction between substance-regime exchange and configuration-regime exterior compensation.
