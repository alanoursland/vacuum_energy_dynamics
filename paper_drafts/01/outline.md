# Paper 1 Outline: Einstein's Equations from Vacuum Energy Bookkeeping

## Working Title

**Einstein's Equations from Energy Bookkeeping: A Derivation of General
Relativity from Vacuum-Substance Postulates**

Shorter title option:

**General Relativity from Vacuum-Substance Postulates**

## Target Venues

Primary path: arXiv gr-qc preprint, with Zenodo DOI as fallback if arXiv
endorsement blocks submission.

Journal targets:

- Foundations of Physics, if framed as a foundational derivation with
  explicit ontology and scope.
- Classical and Quantum Gravity, if covariant lifts and rigor debts are
  substantially paid before submission.

## Central Claim

Starting from a vacuum-substance ontology and two fenced structural
commitments, the gravitational response is fixed sector by sector and
closes on

```text
G_ab + Lambda g_ab = (8 pi G / c^4) T_ab.
```

The result is not obtained by fitting post-Newtonian coefficients. The
static sector, radiative sector, vector sector, and four-derivative sector
each have independent derivation and kill-condition checks. The theory
therefore contains GR as its closed gravitational response, while differing
from GR in ontology and in open vacuum-sector physics.

## Paper Scope

This paper should be honest about its level of closure.

Claim strongly:

- reduced-sector derivations are machine-verified;
- every coefficient in the gravitational sector is fixed;
- surviving local response is Einstein-Hilbert plus Lambda;
- four-derivative freedom is killed by static frame indifference.

Scope carefully:

- full covariant closure relies on standard spin-2 uniqueness/self-coupling
  theorems;
- in-house covariant lifts and Deser-style uniqueness proof remain rigor
  debts;
- Lambda's value is not derived here.

## Intended Reader

Relativists and foundations readers familiar with:

- emergent or analog gravity;
- thermodynamic derivations of Einstein's equations;
- spin-2 bootstrap derivations;
- modified-gravity no-go or selection arguments.

The paper should not assume the reader accepts VED. It should make the
derivation auditable from stated postulates, theorem labels, and scripts.

## Abstract Skeleton

We present a derivation of the Einstein field equations from a
vacuum-substance ontology. The postulates identify vacuum with energy and
spacetime, impose constant local vacuum density, interpret curvature as a
spatial differential of vacuum amount, assign energy to curvature
configurations, require minimum-energy stability, and treat motion in
gradients as vacuum exchange. Two additional fenced commitments complete
the source ledger: static frame indifference and universal gravitation of
configuration energy counted once. From these inputs, the static spherical
sector yields the Schwarzschild exterior and a negative local field-energy
density; stability forces that negative sector to be constrained; the
radiative bootstrap fixes the transverse-traceless normalization and
quadrupole coefficient; the vector sector fixes the Lense-Thirring
normalization; and static frame indifference eliminates the only healthy
four-derivative scalar freedom. The surviving local gravitational response
is Einstein's equation with a cosmological term. Observational anchors are
used only as post-derivation kill conditions. We state the reduced-sector
proofs, the conditional covariant closure, the falsifier ledger, and the
remaining obligations.

## Section Plan

### 1. Introduction

Purpose:

- State the problem: can GR's field equations be derived from a
  non-geometric vacuum ontology without coefficient fitting?
- Situate against Jacobson, Verlinde, Padmanabhan, Sakharov, and spin-2
  bootstrap routes.
- State what is new: energy-bookkeeping route, local negative field-energy
  density, sector-indefinite stability architecture, and P7-prime
  elimination of scalaron freedom.

Tone:

- restrained;
- precise about scope;
- no triumphal language.

### 2. Inputs and Anti-Circularity Rules

Content:

- SR imports: local Lorentz invariance, Minkowski zero-source state,
  mass-energy bookkeeping.
- Postulates P1-P6, P7-prime, P9, stated compactly.
- Fences on P7-prime and P9.
- What is not imported: Einstein equations, Schwarzschild as a solution,
  GR phenomenology, fitted PPN coefficients.
- One empirical normalization: Newton's `G`.

Table:

- postulate;
- role in derivation;
- where it first does nontrivial work.

### 3. Kinematic Layer: Why the Vacuum Configuration Is a Metric

Goal:

Derive the field variable and gauge structure from vacuum-spacetime
identity.

Claims:

- local vacuum configuration assigns clock and rod mappings;
- perturbations are symmetric tensor fields;
- relabeling vacuum elements gives gauge freedom;
- universal matter response follows from matter reading the same vacuum
  mappings.

Assumed by writing time:

- polished wording that does not overclaim mathematical derivation of the
  metric from ontology.

### 4. Static Bookkeeping and the Exact Exterior

Goal:

Show the first major payoff without using field equations.

Steps:

1. Areal-flux source law:

```text
Delta_areal A = (8 pi G / c^2) rho.
```

2. Static frame indifference:

```text
AB = 1
```

in static source-free exteriors.

3. P9 self-coupling and exponential identity:

```text
Delta_areal(e^s) = e^s [Delta_areal s + (s')^2].
```

4. Negative static field energy:

```text
u_field = -c^4 (s')^2 / (8 pi G).
```

5. Exact Schwarzschild exterior:

```text
A = 1 - 2GM/(c^2 r),    B = A^{-1}.
```

Key point:

Schwarzschild appears as a result of bookkeeping, not as a target metric.

### 5. Sector Architecture and Stability

Goal:

Explain why the negative static sector is not pathological.

Content:

- ghost exclusion: negative scalar/static sector cannot propagate;
- source slavery: source-free flat vacuum is unique;
- TT positivity: propagating modes have positive energy and null flux.

This section can cite Paper 2 if Paper 2 is written first. If Paper 1 is
written first, include the compact proof and move details to an appendix.

Table:

- static scalar/shear: negative, elliptic, source-slaved;
- TT radiation: positive, hyperbolic, radiative;
- vector sector: constraint-sourced by momentum;
- trace/kappa: suppressed in static vacuum.

### 6. Linear Spin-2 Closure and Radiative Bootstrap

Goal:

Move from static bookkeeping to dynamical response.

Steps:

1. Fierz-Pauli uniqueness for massless spin-2 linear operator.
2. Linear theory cannot fix `K_T`.
3. P9 self-coupling fixes response normalization:

```text
N = c^4 / (8 pi G).
```

4. Second-order radiative bootstrap fixes:

```text
K_T = c^4 / (16 pi G)
```

and the standard quadrupole coefficient.

Scope statement:

The closure uses standard self-coupled spin-2 uniqueness. An in-house
closure proof is a rigor debt, not a coefficient freedom.

### 7. Eliminating Four-Derivative Freedom

Goal:

Show why the result is Einstein-Hilbert, not generic higher-curvature
gravity.

Steps:

1. Ghost gate kills Weyl/spin-2 quadratic curvature terms.
2. Gauss-Bonnet is inert in 4D.
3. The only healthy local survivor is `a R^2`, with scalaron range
   `sqrt(6a)`.
4. Static scalaron hair is mandatory for `a != 0`.
5. Scalaron hair violates static frame indifference / `AB = 1`.
6. Therefore:

```text
a = 0.
```

This section may become shorter if Paper 6 is written first; otherwise it
should contain the full theorem chain.

### 8. Result

State:

```text
G_ab + Lambda g_ab = (8 pi G / c^4) T_ab.
```

Also state action form:

```text
S = c^4/(16 pi G) int sqrt(-g) (R - 2 Lambda) d^4x + S_matter
```

plus inert Gauss-Bonnet.

Clarify:

- Lambda is permitted but not valued;
- all local gravitational coefficients are fixed;
- gravitational sector matches GR;
- VED novelty shifts to vacuum-sector physics and ontology.

### 9. Kill Conditions and Empirical Checks

Goal:

Make clear observations are tests after derivation, not fits.

Table:

- Newtonian limit: normalization anchor only;
- binary pulsar / GW energy loss: radiative coefficient;
- GPB/LAGEOS: vector sector;
- short-range Yukawa: P7-prime / scalaron exclusion;
- boundary smoothing: P7-prime;
- kappa leak: derived but unobservably small.

Emphasize:

- zero matched coefficients beyond `G`;
- observational confrontation happened after derivation.

### 10. Where VED Is Not GR

Content:

- metric/vacuum as substance;
- local static field-energy density owned by the theory;
- substance frame, quarantined couplings;
- Lambda as frustration floor candidate;
- dark-sector candidate mechanism;
- Casimir/UFFT sector.

Purpose:

Prevent the reader from saying "if the equations are GR, the theory is
only GR." The response: gravitational equations match; ontology and vacuum
sector do not.

### 11. Open Obligations

Split into two lists.

Rigor debts:

- in-house Deser closure;
- covariant lifts of reduced-sector proofs;
- Isaacson/gauge rigor;
- nonlinear stability;
- tensor-virial identity.

Open physics:

- Lambda value;
- dark-sector abundance;
- measure identity;
- interior cap;
- Casimir/UFFT window.

### 12. Conclusion

Close with:

- the derivation fixed GR rather than a deviation;
- the negative results are part of the result;
- future work belongs in rigor closure and vacuum-sector physics.

## Figures and Tables

### Figure 1: Derivation Flow

Postulates -> static bootstrap -> sector architecture -> spin-2 closure ->
four-derivative kill -> Einstein equations.

### Figure 2: Two Independent Routes to Schwarzschild

Bookkeeping route and spin-2 closure route meet at the same exterior.

### Figure 3: Four-Derivative Elimination

Quadratic terms -> ghost gate -> scalaron survivor -> P7-prime hair
contradiction -> `a = 0`.

### Table 1: Postulates and Roles

Compact postulate ledger.

### Table 2: Coefficients and Kill Conditions

Derived coefficient, derivation source, observation that could have killed
it.

### Table 3: GR vs VED

Same field equations; different ontology/open sectors.

## Appendices

- Appendix A: Areal-flux/static bootstrap details.
- Appendix B: Sector architecture proof, or pointer to Paper 2.
- Appendix C: Radiative bootstrap algebra.
- Appendix D: Scalaron no-hair proof, or pointer to Paper 6.
- Appendix E: Verification script index.

## Claims To Avoid

- Do not claim the full covariant proof is completely self-contained if it
  still cites Deser.
- Do not claim Lambda's value is derived.
- Do not imply observations were used to tune non-Newtonian coefficients.
- Do not hide P7-prime and P9 as if they were derived from P1-P6.

## Claims To Emphasize

- The derivation has negative space: many candidate deviations died.
- P7/P8 are not live recovery postulates.
- P7-prime and P9 were adopted with fences before their strongest
  consequences were known.
- The theory currently predicts no accessible gravitational deviation from
  GR, except as null tests of the commitments.

## Assumed Missing Pieces By Writing Time

1. Clean public repository or archive DOI.
2. Related-work pass on all derivation routes to GR.
3. Citation-ready statement of Fierz-Pauli and Deser results.
4. Clean covariant-scope paragraph.
5. Updated theorem labels and script paths.
6. AI-assistance disclosure language matched to target venue.
