# candidate_amplitude_origin_sieve — Result Note

## Result

The script audits possible origins for the source-independent amplitude `p_free`.

It rejects direct source coupling:

```text
p0 = p_free + lambda*rho_M
d(p0)/d(rho_M) = lambda
```

It rejects diagnostic repair choices:

```text
p_free = T_target/k_trace
p_free = M_target/k_mass
```

It also rejects zero response:

```text
p_free = 0
```

because zeroing the amplitude kills the candidate rather than licensing it.

## Main Findings

The source-independent amplitude remains underived.

The result is important because `p_free` cannot be used as a magic knob. It cannot be:

```text
coupled to ordinary matter density;
chosen to cancel trace burden;
chosen to cancel mass burden;
set to zero and called survival.
```

The only acceptable future path is to derive `p_free` from an actual stress/energy/geometry/variational principle, or leave the transition response audit-only.

## Boundary

No amplitude principle is derived here.

## Steering Consequence

The classifier should report that stress-energy accounting is not closed and that the candidate remains audit-only, with diagnostic-only downgrade possible if no principle appears.
