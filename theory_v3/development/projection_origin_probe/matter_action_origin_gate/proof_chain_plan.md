# Matter Action Origin Gate — Proof Chain Plan

## Purpose

This folder tests the next exposed source-side gate:

```text
Does shared interval dependence force universal metric stress coupling,
or is matter coupling still imported?
```

The target is deliberately conditional.  The folder does **not** derive the
microscopic existence of matter species.  It proves a narrower bridge:

```text
If matter actions use the same metric interval and volume structure, then
metric variation routes their source through the stress tensor.
```

That result is important because it separates three layers:

1. **Metric interval ownership** — matter uses the same quadratic interval
   structure as the vacuum geometry.
2. **Stress coupling** — variation with respect to that interval structure
   produces a symmetric stress tensor source.
3. **Matter ontology** — the existence and microscopic form of the matter
   action remain external unless a later proof chain derives them.

## Strategy

The proof chain is split into six batches.

### Batch A — Shared metric interval variation

Show that if proper time / local interval length depends on `g_ab`, variation
of the interval produces a bilinear metric source term.  This includes the
volume factor and inverse metric variation identities used in standard matter
stress definitions.

### Batch B — Stress tensor normalization

Verify the metric variation convention

```text
δS_m = 1/2 ∫ sqrt(|g|) T^{ab} δg_ab
```

or the equivalent inverse-metric convention.  The scripts explicitly track the
sign/convention dependence so that the gate does not pretend a convention is a
physical derivation.

### Batch C — Examples and trace limitations

Use scalar-field, point-particle, conformal, and null-radiation witnesses to
show what metric coupling sees and what trace-only coupling misses.  In
particular, conformal/scalar-only response couples only to the trace and cannot
carry general shear/traceless stress.

### Batch D — Universality and routing gates

Check that species-dependent metric factors or independent nonmetric channels
introduce observable coupling differences or double-counting ledgers unless
explicitly routed as additional fields.

### Batch E — Conservation consistency

Show that diffeomorphism-type variation of a metric matter action gives the
usual conservation route.  This is a compatibility gate, not a microscopic
origin theorem.

### Batch F — Status and remaining frontier

Close with the exact conditional status:

```text
shared metric interval dependence -> universal stress coupling;
microscopic matter action origin remains open.
```

## Expected conclusion

The folder should prove that universal stress coupling is not an additional
force law once matter actions are committed to the same metric interval.  But
it should also record that the commitment itself is the remaining ontology
question.
