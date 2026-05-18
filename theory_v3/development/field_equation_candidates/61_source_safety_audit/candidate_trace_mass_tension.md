# candidate_trace_mass_tension — Result Note

## Result

The script exposes a reduced tension between trace-free closure and active-mass-neutral closure.

It compares two conditions using an energy density `u`:

```text
trace-free:
  -u + p_r + 2p_t = 0
  therefore u = p_r + 2p_t

active-mass-neutral:
  u + p_r + 2p_t = 0
  therefore u = -(p_r + 2p_t)
```

Both can hold only if:

```text
p_r + 2p_t = 0
```

The script finds this is not generic for the closure-supported layer.

## Main Findings

This is one of the sharpest Group 61 results.

The stress-only transition response cannot simply choose one convenient energy density and claim both trace neutrality and active mass neutrality. The two requirements point in opposite directions unless the pressure sum vanishes.

That means the layer stress closure now has a real stress-accounting burden. It needs a derived relation among `u`, `p_r`, `p_t`, mass coupling, and trace role.

## Boundary

This is reduced closure accounting, not a covariant stress theorem.

## Steering Consequence

The next check should test conservation/exchange. Reduced `D=0` may show internal balance, but it cannot by itself prove source safety or conservation.
