# Vacuum Action Origin: Status After Proofs 7-11

## What This Batch Adds

Proofs `7` through `11` extend the action-origin chain from static local
ingredients to propagation, gradient strain, torsion gating, boundary
completion, and the first candidate action audit.

## Proof 7: Lorentzian Propagation Gate

Proof `7` validates:

```text
Lorentzian principal symbol:
  -omega^2 + c^2 k^2 = 0 -> omega^2 = c^2 k^2

Euclidean principal symbol:
  omega^2 + c^2 k^2 = 0 -> omega^2 = -c^2 k^2
```

So real finite-speed propagation selects a hyperbolic/Lorentzian principal
structure. The same Lorentzian wave Lagrangian has positive Hamiltonian energy.

## Proof 8: Local Additivity to Gradient Strain

Proof `8` validates:

```text
E = K/(2h) sum (q_(i+1)-q_i)^2
```

has interior variation:

```text
partial E / partial q_i = -K h Delta_discrete q_i.
```

In the continuum limit, the edge energy becomes:

```text
(K/2)(q')^2.
```

This is the bridge from finite-cell local response to continuum gradient
strain.

## Proof 9: Torsion Defect Gate

Proof `9` validates:

```text
T^a_bc T_a^bc = 24 tau^2.
```

With positive torsion stiffness and no torsion source:

```text
tau = 0.
```

With a defect source:

```text
tau = J/(24 mu).
```

So torsion-free is a real physical branch condition, not automatic.

## Proof 10: Boundary Completion and Flux Sources

Proof `10` validates:

```text
-(1/2)q q'' + (1/2)d(q q')/dx = (1/2)(q')^2.
```

The boundary completion cancels derivative-of-variation boundary data, while
boundary source terms still impose flux conditions:

```text
q'(R)=Q_R
q'(L)=Q_L.
```

## Proof 11: First Action Candidate Audit

Proof `11` validates the scalar candidate:

```text
S[q] = integral [(1/2)q_t^2 - (1/2)c^2 q_x^2 - (1/2)m^2 q^2]
```

gives:

```text
q_tt - c^2 q_xx + m^2 q = 0.
```

It passes locality, propagation, gradient-strain, and boundary-flux gates. It
does not pass the final gravitational variable gate because a scalar has one
degree of freedom, while a four-dimensional massless metric field has two.

## Current Impact

The vacuum-action chain now has a minimal action prototype:

```text
reciprocal response
  -> metric candidate
  -> Lorentzian propagation signature
  -> local additive edge strain
  -> second-order wave action
  -> boundary-flux sources.
```

This is real progress, but it is not yet gravity.

The scalar prototype proves that the action-origin assumptions cohere. The next
step is to lift the response variable:

```text
q
  -> metric g_ab
  -> Levi-Civita connection strain
  -> EH/GHY action.
```

## Remaining Gap

The hard remaining question is now precise:

```text
why does the vacuum response variable become the metric itself,
rather than an additional scalar field living on a metric?
```

The next proofs should focus on metric self-reference:

```text
13. interval field self-coupling: the response variable changes its own
    measurement metric;
14. universal coupling: why every energy form perturbs the same interval;
15. spin-2 bootstrap gate: self-coupling of the linear metric field;
16. boundary flux to metric boundary term: stronger GHY analogy;
17. status after metric self-coupling gates.
```
