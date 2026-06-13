# In-House Spin-2 Closure Uniqueness Plan

## Exact Claim Needed By VED

VED already supplies the physical reasons for the spin-2 setup:

- K1: the vacuum configuration is metric-like, so perturbations are
  symmetric tensor fields;
- K2: coupling to matter is universal because matter reads the vacuum
  mappings directly;
- K3: gauge freedom is relabeling of vacuum elements;
- P9: configuration energy gravitates at the universal coupling, counted
  once.

The remaining mathematical claim is not that "GR is true." It is:

```text
massless spin-2 + relabeling gauge symmetry + universal coupling
+ self-energy coupling + locality/two-derivative/no-extra-field
consistency => Einstein-Hilbert nonlinear closure
```

The current proof cites Deser 1970 for that claim. This directory is the
program to replace the citation.

## First Rung Completed

The first forge script verifies the obstruction that starts the
self-coupling chain:

1. The Fierz-Pauli/linearized Einstein operator is identically conserved:

   ```text
   partial^mu G^(1)_{mu nu} = 0
   ```

2. Therefore the linear equation requires a conserved source.

3. The gauge variation of the matter coupling

   ```text
   (1/2) int h_{mu nu} T^{mu nu}
   ```

   reduces, after integration by parts, to a term proportional to
   `partial_mu T^{mu nu}`.

4. Once matter exchanges energy-momentum with the spin-2 field,
   `partial_mu T_matter^{mu nu}` is not zero. A compensating field stress
   with the opposite divergence is forced.

This proves the first consistency step only. It does not yet prove the
full Deser closure.

## Next Rungs

The next useful script should compute the first explicit self-coupling
term or move to a first-order/Palatini presentation where the closure can
be shown without an infinite uncontrolled tower.

