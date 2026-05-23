# `m = 2` Selector Tests

## Purpose

This note keeps the projection-origin probe small.

The prior notes established:

```text
psi_k:
  derived from an integration-by-parts primitive

L[f]:
  derived as a weighted-divergence pullback

primitive family:
  G_(k,m)(x) = x^(2k - 1)(1 - x^2)^m
```

The family test exposed the main danger:

```text
Every m gives an IBP construction.
Boundary cleanliness alone does not select m = 2.
```

This note asks only one question:

```text
Can m = 2 be selected independently of already observing
r_k = (2k - 1)/(2k + 3)?
```

The goal is containment. This is not a physical-interpretation note.

## Definitions

Let:

```text
a = 1 - x^2
```

and keep the projection weight:

```text
w = a^4.
```

The primitive-power family is:

```text
G_(k,m)(x) = x^(2k - 1)a^m.
```

The corresponding pullback operator is:

```text
L_m[f] = a f' - 2(5 - m)xf.
```

The observed operator is:

```text
L_2[f] = a f' - 6xf.
```

## Selector 1: Weighted-Adjoint Closure

Under the projection weight:

```text
w = a^4,
```

integration by parts gives:

```text
<L_m f, g>_w
=
[a^5 f g]_0^1
+
<f, L_m^* g>_w
```

where:

```text
L_m^*[g] = -a g' + 2m xg.
```

Compare this with:

```text
L_(5-m)[g] = a g' - 2m xg.
```

Therefore:

```text
L_m^* = -L_(5-m).
```

This is a real structural result.

But it does not select `m = 2`.

Instead, it pairs the family members:

```text
m = 1 <-> m = 4
m = 2 <-> m = 3
m = 3 <-> m = 2
m = 4 <-> m = 1
```

The fixed skew-adjoint value would be:

```text
m = 5/2,
```

which is not an integer primitive power.

So adjoint closure does not independently select the observed case.

Result:

```text
adjoint selector for m = 2:
  failed

adjoint structure:
  real, but family-wide

best it gives:
  the adjacent pair {2,3}, not m = 2 alone
```

## Selector 2: Exponent Ladder

For general `m`, the exponent roles are:

```text
primitive factor:       a^m
operator flux factor:   a^(5 - m)
projection weight:      a^4
IBP boundary factor:    a^5
```

For `m = 2`, this becomes:

```text
primitive factor:       a^2
operator flux factor:   a^3
projection weight:      a^4
IBP boundary factor:    a^5
```

or:

```text
a^2 -> a^3 -> a^4 -> a^5.
```

If one requires the ordered adjacent ladder:

```text
primitive -> flux -> weight -> boundary
```

to climb by one exponent at each step, then:

```text
m = 2
```

is selected.

This is suggestive.

But it is not yet an independent derivation unless the ordering principle itself is justified.

The adjoint-pair symmetry naturally gives the pair:

```text
{2, 3}
```

because:

```text
m <-> 5 - m.
```

Choosing the lower member `m = 2` requires an additional orientation:

```text
primitive before flux,
or lower endpoint order before higher flux order,
or a directed integration-by-parts interpretation.
```

That orientation may be reasonable, but it is not yet forced.

Result:

```text
exponent-ladder selector:
  suggestive

strict ordered ladder:
  selects m = 2

independent derivation:
  not yet
```

## Selector 3: Compactified Radial Measure

A possible independent selector would be a compactified radial measure.

Test a generic compactification family:

```text
r = x / a^c,    c > 0.
```

Then:

```text
dr/dx = a^(-c - 1)[1 + (2c - 1)x^2].
```

An `n`-dimensional radial measure gives:

```text
r^(n - 1) dr
=
x^(n - 1)[1 + (2c - 1)x^2] a^(-cn - 1) dx.
```

The important part is the power of `a`:

```text
a^(-cn - 1).
```

For:

```text
c > 0
n > 0
```

this is a negative power.

It cannot equal the positive projection weight:

```text
a^4.
```

The standard compactification:

```text
r = x / sqrt(1 - x^2)
```

has:

```text
c = 1/2
```

and gives measure exponent:

```text
-(n + 2)/2.
```

To equal `+4`, it would formally require:

```text
n = -10,
```

which is not a positive dimension.

Therefore:

```text
compactified radial measure alone:
  does not produce w = a^4
```

A compactified measure could still contribute if multiplied by an additional envelope, decay factor, density, or variational weight. But then `m = 2` is not selected by compactification alone.

Result:

```text
compactification-alone selector:
  failed

compactification plus extra envelope:
  possible, but would be a new assumption
```

## Combined Result

The three selector tests give:

```text
m = 2 from observed projection ratio:
  yes

m = 2 from adjoint closure:
  no

m = 2 from ordered exponent ladder:
  suggestive only

m = 2 from compactified radial measure alone:
  no

m = 2 independent derivation:
  not achieved
```

This is not a total failure.

It means the projection hierarchy remains:

```text
formal but structured
```

rather than:

```text
independently derived from operator/domain geometry.
```

## Updated Status

```text
psi_k origin:
  derived

L operator:
  derived

primitive family artifact risk:
  confirmed

m = 2 selector:
  observed-ratio selection only

adjoint structure:
  family pairing m <-> 5 - m

exponent ladder:
  strongest remaining clue

compactified measure:
  does not select m = 2 alone

physical interpretation:
  still closed
```

## Stop Rule

Do not keep adding selector tests unless a concrete new object appears.

Concrete objects could include:

```text
specific measure
specific boundary condition
specific variational functional
specific compactification with required envelope
specific source-signature theorem
specific self-adjoint domain
```

Labels do not count.

Without a new object, stop here and record:

```text
m = 2 is selected by the observed projection hierarchy,
not independently derived.
```

That is a valid result.

## Recommended Next Move

Do not start physical interpretation yet.

Do not start parent-equation construction.

Do not start broad source-signature mining.

The safest next action is to update the branch README/status to say:

```text
The projection hierarchy has a real IBP/operator structure,
but m = 2 has not been independently selected.
The branch remains formal but structured.
```

Then pause.

Only continue if the next step begins from a concrete object, not a new possible meaning.

## Validation Summary

The generating script validated:

```text
- weighted adjoint identity grid M=1..5: passed
- adjoint pairing L_m^* = -L_(5-m): passed
- no integer m is skew-adjoint under w=a^4: passed
- ordered adjacent exponent ladder selects m=2: passed
- adjoint-pair adjacency gives pair {2,3}, not m=2 alone: passed
- compactified radial derivative validated for c=1/2,1,2: passed
- standard compactified radial measure cannot yield a^4 for positive dimension: passed
- generic c>0 compactified radial measure cannot yield a^4 alone: passed
```

## Bottom Line

The best current answer is:

```text
m = 2 is real within the observed projection hierarchy,
but not yet forced independently.
```

The hierarchy has survived the first origin tests, but it has not crossed the physical interpretation gate.

This branch should now be contained.
