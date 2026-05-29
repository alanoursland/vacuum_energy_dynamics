# Projection Variable Identification — Proof Chain Plan

## Purpose

The previous GR boundary-reduction measurement group showed that weak-field GR fixes the physical scalar boundary ledger

```text
Poisson equation -> finite Gauss flux -> 1/r exterior
```

but does not, by itself, fix the compactified projection contact index `R` used in the original moment-kernel ladder.

This folder asks the next narrower question:

```text
What exactly can the original projection variable be identified with in a weak-field scalar/GR reduction?
```

The intended answer is conservative:

```text
The original y-variable and C_R moment ladder define a projection chart/test-pairing on a compactified scalar boundary problem. If GR is embedded into that same chart, the observed ladder is the R=0 chart. But the physical GR scalar field alone does not uniquely choose that chart.
```

## Strategy

The proof scripts separate four layers:

1. physical radial scalar data (`r`, exterior `1/r`, finite flux);
2. compactification variables (`q=1/r`, `x`, `y=x^2`);
3. moment/test pairing weight (`(1-y)^(R+1)y^(-1/2)`);
4. field/test rescaling choices that can shift apparent contact order.

The group should close the following result:

```text
The projection variable is identified as a compactified moment/test variable, not as an invariant physical scalar field by itself.
```

## Success Criteria

Closed by this group:

- the beta factor `y^(-1/2)` follows from `y=x^2`;
- the `R=0` moment functional gives the observed `r_k` ratio;
- multiplying the endpoint weight by extra `(1-y)^R` shifts the ladder ratio;
- field/test rescalings can change apparent compactified contact power without changing exterior finite flux;
- therefore `R_GR` is a property of a chosen projection embedding, not of the raw weak-field scalar ledger alone.

Still imported after this group:

- the physical reason to choose the original projection chart;
- the parent ontology that makes that chart natural;
- the tensor/Weyl sector;
- matter action origin;
- nonlinear constraint closure.
