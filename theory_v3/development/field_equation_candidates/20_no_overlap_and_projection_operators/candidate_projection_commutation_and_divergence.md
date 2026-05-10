# Candidate Projection Commutation And Divergence

## Canonical Filename

```text
candidate_projection_commutation_and_divergence.md
```

This document summarizes the output of:

```text
candidate_projection_commutation_and_divergence.py
```

## What This Document Is

This document is a Group 20 no-overlap / projection-operator artifact.

It is not a proof that \(O\) commutes with derivatives, not a Bianchi-compatibility theorem, not a conservation law, and not a correction-tensor insertability result.

Its purpose is to test whether no-overlap projectors can preserve divergence safety without becoming a repair mechanism.

The locked-door question was:

```text
Does O commute with derivatives/divergence in a way that preserves constraints?
```

The result is:

```text
Divergence-compatible projection is not solved.

Constant algebraic projectors are toy-safe only.
Variable or boundary-sensitive projectors create commutator and surface terms.
No parent correction tensor becomes insertable from O alone.

Best next script:
  candidate_projection_boundary_and_exterior_neutrality.py
```

## Core Result

Allowed status:

```text
constant algebraic projectors are toy-safe only,
diagnostic-only sector labels remain safe,
constraint/Hodge-like projectors remain candidate classes,
covariantly constant and boundary-neutral projectors remain theorem targets.
```

Rejected:

```text
commutation by declaration,
Bianchi compatibility by name,
nonlocal repair projection,
recovery-chosen divergence projector.
```

Missing before divergence-compatible \(O\) can be real:

```text
commutator identity,
connection-compatible sector basis,
projected divergence law,
boundary flux neutrality,
source, mass, and scalar trace leakage controls.
```

## Compact Commutation Ledger

| Entry | Candidate | Status | Consequence |
|---|---|---|---|
| D1: divergence-compatible projection target | \(O\) commutes with derivative/divergence strongly enough to preserve constraints | THEOREM_TARGET | divergence-compatible projection remains theorem target |
| D2: algebraic constant projector | constant matrix projector with \(D(O)=0\) | SAFE_IF | can commute algebraically in toy basis only |
| D3: variable local projector | position-dependent \(O(x)\) | RISK | derivative leakage appears as \((\nabla O)\) field |
| D4: covariantly constant projector | \(\nabla_\mu O=0\) on the relevant domain | THEOREM_TARGET | promising but not currently derived |
| D5: constraint projector | \(O\) projects onto constraint-satisfying sector | CANDIDATE | candidate route only |
| D6: Hodge-like projector | longitudinal/transverse or exact/coexact/harmonic split | CANDIDATE | useful analogy, not a derived \(O\) |
| D7: nonlocal elliptic projector | solve auxiliary elliptic equation to project divergence-free part | RISK | cannot be inserted without stronger structure |
| D8: boundary-sensitive projector | \(O\) carries boundary terms explicitly | THEOREM_TARGET | handoff to boundary/exterior neutrality script |
| D9: diagnostic-only projector | \(O\) labels sectors after a derivation but does not alter equations | SAFE_IF | safe bookkeeping while active \(O\) remains deferred |
| D10: commutes by declaration | declare \([\nabla,O]=0\) without deriving it | REJECTED | projected divergence cannot be asserted |
| D11: Bianchi compatibility by name | \(O\) is compatible with Bianchi identity because it is called a projection | REJECTED | no correction tensor becomes insertable from \(O\) alone |
| D12: divergence decision | divergence-compatible \(O\) remains deferred until commutator and boundary terms are derived | RECOMMENDED | next script should test boundary and exterior neutrality |

## Status Counts

The run counted:

```text
CANDIDATE:      2
RECOMMENDED:    1
REJECTED:       2
RISK:           2
SAFE_IF:        2
THEOREM_TARGET: 3
```

Interpretation:

```text
Constant toy projectors may commute only in a fixed algebraic basis.
Variable or boundary-sensitive projectors create commutator and surface terms.
Divergence-compatible projection remains a theorem target.
```

## Local Commutator Check

The script tested:

\[
O(x)=
\begin{pmatrix}
p(x)&0\\
0&q(x)
\end{pmatrix},
\qquad
v(x)=
\begin{pmatrix}
a(x)\\
b(x)
\end{pmatrix}.
\]

The commutator is:

\[
\frac{d}{dx}(Ov)-O\frac{dv}{dx} =
\begin{pmatrix}
a(x)p'(x)\\
b(x)q'(x)
\end{pmatrix}.
\]

Equivalently:

\[
\frac{d}{dx}(Ov)-O\frac{dv}{dx} =
\frac{dO}{dx}v.
\]

If \(dO/dx=0\), the commutator vanishes in the toy basis:

```text
Matrix([[0], [0]])
```

Interpretation:

```text
A variable projector does not commute with derivatives.
The leakage term is not optional; it must be assigned, canceled by theorem, or rejected.
```

## Projected Divergence Requirement

The formal requirement is:

\[
\nabla_\mu(OX)^\mu =
O\nabla_\mu X^\mu
+
(\nabla_\mu O)X^\mu.
\]

Therefore projected conservation requires one of:

1. \(\nabla_\mu O=0\) on the relevant sector.
2. \((\nabla_\mu O)X^\mu\) is a derived neutral term.
3. Boundary/source terms cancel by an explicit theorem.
4. \(O\) is diagnostic-only and does not alter the field equation.

It is not enough to say:

```text
O preserves Bianchi identity,
O preserves conservation,
O prevents overlap.
```

The commutator and boundary accounting must be explicit.

## Rejected Divergence Branches

Rejected:

```text
commutes by declaration,
Bianchi compatibility by name,
nonlocal repair projection.
```

These rejections preserve the Group 19 correction-tensor result:

```text
H_curv/H_exch do not become insertable just because O is named.
```

They also preserve the Group 20 discipline:

```text
projection cannot be a hidden source,
projection cannot be a boundary repair,
projection cannot be chosen by recovery.
```

## Failure Controls

Projection commutation fails if:

1. \([\nabla,O]\) is set to zero by declaration.
2. Bianchi compatibility is claimed by name.
3. Boundary terms are dropped.
4. Nonlocal projection repairs divergence failure.
5. Source leakage is relabeled as \(\Sigma/R\).
6. Scalar trace leakage is hidden by projection.
7. \(M_{\rm ext}\) shifts through the projected sector.
8. Recovery chooses \(O\) after the fact.

## What This Study Established

This study established that divergence-compatible projection remains theorem-targeted.

The local symbolic check shows the core obstruction: a variable projector introduces a commutator leakage term. A constant projector can commute in a toy algebraic basis, but that does not supply a covariant sector basis, a boundary law, or source neutrality.

## What This Study Did Not Establish

This study did not define a divergence-compatible \(O\).

It did not prove \([\nabla,O]=0\).

It did not derive a connection-compatible sector basis.

It did not derive projected conservation.

It did not neutralize boundary flux.

It did not make \(H_{\rm curv}\), \(H_{\rm exch}\), or any parent correction tensor insertable.

## Next Development Target

The next script should be:

```text
candidate_projection_boundary_and_exterior_neutrality.py
```

Purpose:

```text
Test whether projection can preserve boundary neutrality, M_ext,
and exterior scalar silence without becoming a counterterm, shell source,
far-zone patch, or recovery-tuned filter.
```
