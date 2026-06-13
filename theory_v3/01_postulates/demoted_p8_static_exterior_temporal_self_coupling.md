# Demoted P8: Static Exterior Temporal Self-Coupling

> **STATUS: RETIRED AS A POSTULATE; RETAINED AS A THEOREM RECORD.**
> The former P8 statement is no longer a live input. Its content is a
> derived static-sector theorem under **P9 + the C2 bootstrap**.

## Derived Statement

In a static, source-free exterior vacuum configuration, the temporal
mapping composes multiplicatively. Equivalently, for the temporal scale
factor

$$\alpha(r)=\sqrt{-g_{tt}(r)},$$

the weak-field exterior relation is

$$d\ln\alpha=-\frac{dU}{c^2}+O(c^{-6}),$$

with no independent quadratic term in $\ln\alpha$ through one
post-Newtonian order.

This is the content formerly carried by P8.

## Why It Is Derived

P9 says that configuration energy gravitates at the universal coupling
and is counted exactly once. In the static spherical bookkeeping sector,
Trial C2 applies that count-once requirement to the one-parameter family
of candidate distortion variables. The unique P9-compatible member is
the one for which

$$\mathcal A=e^s=A,$$

and the vacuum shear obeys

$$\Delta_{\text{areal}}s=-(s')^2.$$

The exponential structure $A=e^s$ is exactly the multiplicative
composition statement: each exterior shell acts on the already-distorted
temporal rate inherited from the interior shells. Thus the former P8
rule is not an independent structural assumption. It is the theorem
selected by P9's self-energy bookkeeping.

Solving the resulting exterior law gives

$$A(r)=1-\frac{2GM}{c^2r},$$

with the constant fixed by the Newton anchor. Expanding this result in
the weak-field exterior gives the T4 temporal coefficient

$$-g_{tt}=1-\frac{2U}{c^2}+2\frac{U^2}{c^4}+O(c^{-6}),$$

so

$$\beta=1.$$

## What Changed

The former P8 file described a localized recovery postulate. That status
is obsolete. The live postulate set contains P1-P6, P7', and P9; P8 is
not among the inputs.

The historical statement was not killed because it was false. It was
demoted because Trial C2 proved its content from the later-adopted P9
bookkeeping rule. Downstream references should therefore be read as:

$$\text{former P8 content} = \text{P9 + C2 theorem}.$$

## Relation to T4

T4 is now a corollary of the static-sector theorem above. Its direct
dependency is no longer a postulate called P8. The chain is:

```text
P9 + C2 bootstrap
  -> A = e^s
  -> multiplicative temporal composition
  -> d ln alpha = -dU/c^2 + O(c^-6)
  -> beta = 1
```

## Provenance

- `p9_configuration_energy_gravitates.md`: live postulate supplying
  count-once configuration self-gravitation.
- `development/field_equation_trials/002_trial_C_burden_ledger/`:
  static self-coupling bootstrap and selector.
- `04_field_equations/proof.md` section 2.3: direct proof placement in
  the closed field-equation derivation.
- `02_foundations/t4_second_order_temporal_self_coupling.md`: weak-field
  corollary extracting the one-post-Newtonian temporal coefficient.
