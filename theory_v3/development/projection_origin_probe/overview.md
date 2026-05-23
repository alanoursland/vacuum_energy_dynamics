# Projection Origin Probe

## Purpose

This directory holds a focused investigation into the formal projection hierarchy that survived the previous theory-search process.

The goal is not to derive full gravitational field equations here.

The goal is narrower:

> Determine whether the projection hierarchy has a natural operator, source, boundary, or geometric origin, or whether it is only a formal artifact.

This work exists because most prior branches either became diagnostic-only, remained compatibility scaffolding, or required unearned axioms. The projection hierarchy is the one compact mathematical object that survived with enough structure to test directly.

## Core Object

The central projection form is:

```text
A[k,j] = 2 ∫₀¹ ψ_k(x) φ_j(x) (1 - x²)^4 dx
```

with:

```text
φ_j(x) = x^(2j)

ψ_k(x) = x^(2k) - ((2k - 1)/(2k + 3)) x^(2k - 2)
```

and weight:

```text
w(x) = (1 - x²)^4
```

The row-test functions may also be written:

```text
ψ_k(x) = x^(2k - 2)(x² - r_k)

r_k = (2k - 1)/(2k + 3)
```

Each `ψ_k` is sign-changing on `[0,1]`, with root:

```text
x_k = sqrt((2k - 1)/(2k + 3))
```

This prevents a naive positive-Gram or Hessian interpretation.

## Current Status

The hierarchy currently has this status:

```text
formal weighted projection: derived
source-vector map: formally derived
physical residual: not derived
physical source: not identified
boundary/domain meaning: not derived
physical ledger assignment: deferred
parent equation: not ready
```

The hierarchy should currently be treated as an auxiliary admissibility candidate, not as:

```text
curvature energy
exchange energy
interface energy
total burden
source law
field equation
merger prediction
```

## Formal Source Map

A minimal formal residual family is:

```text
R_S[f](x) = f(x) - S(x)
```

For a finite profile:

```text
f_N(x) = Σ_j c_j x^(2j)
```

the projected condition gives:

```text
A c = b(S)
```

where:

```text
b_k(S) = 2 ∫₀¹ ψ_k(x) S(x) (1 - x²)^4 dx
```

This is a formal source-vector map. It is not yet a physical source law.

## Main Questions

This directory is organized around five killable questions.

### 1. Where does `ψ_k` come from?

Determine whether the row-test functions can be derived from:

```text
integration by parts
weighted orthogonality
a Sturm-Liouville-like operator
a boundary condition
a moment-cancellation condition
a projection residual
```

The key target is the ratio:

```text
r_k = (2k - 1)/(2k + 3)
```

This ratio must be derived, not merely observed.

### 2. What is `x`?

The variable `x` currently has no physical interpretation.

Possible interpretations to test:

```text
normalized radial coordinate
compactified boundary-layer coordinate
dimensionless vacuum-response coordinate
moment/projection parameter
pure formal integration variable
```

No physical meaning should be assumed.

### 3. What is `f(x)`?

The profile `f` may represent an admissibility profile, response profile, correction profile, or nothing physical.

The work should determine whether `f` can be linked to a vacuum-response variable without smuggling in unearned field content.

### 4. What is `S(x)`?

The formal source `S(x)` is only a target profile in the projection equation.

It must not be called ordinary matter, mass, curvature, burden, exchange, or boundary data unless independently derived.

### 5. Is there a natural residual/operator problem?

The main constructive target is to find an operator or residual equation such that projection against `ψ_k` is natural.

A successful result would look like:

```text
Given a natural residual R[f],
the condition <ψ_k, R[f]>_w = 0
produces A c = b
with the observed ψ_k and weight w.
```

## Working Rules

This directory should avoid the failure modes of the previous broad search.

Do not create new route ledgers unless they close or kill a specific question.

Do not introduce active `O`, hidden projectors, repair currents, or boundary terms by name.

Do not call a compatibility identity a theorem.

Do not call finite-N evidence an all-order proof.

Do not assign physical meaning to formal variables without derivation.

Do not use GR recovery, weak-field success, or downstream convenience to select structures.

## Near-Term Work Plan

### Step 1: Ratio Origin Test

Test whether:

```text
r_k = (2k - 1)/(2k + 3)
```

comes from a weighted moment ratio, orthogonality condition, or integration-by-parts identity.

Record the result as one of:

```text
derived
not derived
derived only under artificial condition
compatibility-only
failed
```

### Step 2: Operator Pullback Test

Look for an operator `L` such that:

```text
∫ ψ_k f w dx
```

can be rewritten as:

```text
∫ basis_k L[f] dx + boundary terms
```

All boundary terms must be explicit.

### Step 3: Boundary Term Test

Determine whether the ratio `r_k` is forced by eliminating a boundary term or endpoint contribution.

### Step 4: Source Signature Test

Study formal source families:

```text
S_pq(x) = x^(2q)(1 - x²)^p
```

but only as formal sources.

The goal is to understand which endpoint/domain assumptions produce all-negative, leading-positive, or mixed source-vector signatures.

### Step 5: Physical Interpretation Gate

Only after a natural residual/operator origin is found, test whether `x`, `f`, and `S` can be interpreted physically.

Until then, the projection hierarchy remains formal.

## Success Criteria

This investigation succeeds if it produces one of the following:

```text
A natural operator/residual origin for ψ_k and w.
A clear proof that ψ_k is only an artifact of the earlier construction.
A boundary/domain derivation of the source-vector structure.
A clean reason to discard the hierarchy as physically irrelevant.
```

A negative result is acceptable.

The point is to make the projection hierarchy killable.

## Current Best Label

The current best label for this branch is:

```text
formal weighted projection / admissibility hierarchy
```

Not:

```text
gravity field equation
curvature energy
vacuum burden
source law
parent equation
```

## One-Line Summary

This directory tests whether the surviving projection hierarchy has a real operator/source/boundary origin, or whether it should be discarded as a formal artifact.

```
