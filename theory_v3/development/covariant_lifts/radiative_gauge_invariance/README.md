# Radiative Gauge Invariance

## Purpose

This directory holds Phase 2 of the targeted covariant-lift program:
gauge invariance of the averaged radiative stress.

Current status: completed at leading local inertial short-wave order.
See `radiative_gauge_invariance_note.md` and the forge script:

```text
vacuum_forge/src/field_equation_trials/016_radiative_gauge_invariance/radiative_gauge_invariance.py
```

## Scope

The 015 averaging lift established the Isaacson averaging rules and the
leading local form

$$
<t_{ab}> =
{c^4\over 32\pi G}
<\partial_a h^{TT}_{ij}\partial_b h^{TT}_{ij}> .
$$

This phase proves that the leading averaged stress is invariant under
admissible high-frequency relabeling gauge transformations:

$$
h_{ab}\mapsto h_{ab}+\partial_a\xi_b+\partial_b\xi_a .
$$

The proof is made at the radiative TT level. The leading fast gauge
piece is longitudinal with respect to the propagation direction and is
killed by the TT projector. Slow-envelope pieces remain in the same
suppressed \(O(\lambda/L)\) class already recorded in 015.

## Forge Proof

The forge script validates:

1. for arbitrary unit propagation direction \(n_i\), the TT projection of
   \(n_i v_j+n_j v_i\) vanishes;
2. for a \(z\)-propagating wave, adding the explicit pure-gauge spatial
   tensor leaves the TT-projected field unchanged;
3. the derivative contraction entering
   \(<t_{ab}>\) is unchanged after TT projection;
4. an explicit averaged plus/cross wave with an added longitudinal gauge
   piece has the same averaged stress as the original wave.

Archive result:

```text
radiative_gauge_invariance_016
```

This closes the radiative gauge-invariance subpiece of the covariant
lift debt. It does not address the vector-sector time-dependent lift or
nonlinear stability.

