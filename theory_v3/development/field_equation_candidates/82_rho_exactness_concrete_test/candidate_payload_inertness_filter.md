# candidate_payload_inertness_filter — Analysis Note

## Result

`candidate_payload_inertness_filter.py` factors possible physical payload carried by local nonzero `rho`:

```text
payload = rho*(D_parent*i_div + M_A*i_mass + S_M*i_src + T_zeta*i_trace)
```

Safe no-payload route:

```text
0
```

Dangerous active channels:

```text
source payload = S_M*rho
trace payload = T_zeta*rho
mass payload = M_A*rho
divergence payload = D_parent*rho
```

## Interpretation

This script explains why local nonzero `rho` remains dangerous even after flat or weighted neutrality.

If `rho` carries source, trace, mass, or divergence payload locally, then integrated cancellation may not be enough. The theory would need to show that the local remainder is physically inert, gauge-exact, boundary-only, or otherwise non-carrying.

This is not just a governance check. It is a physical interpretation filter. It asks whether the exact remainder is merely a mathematical redistribution or a local physical load.

## Conceptual Consequence

The exactness route has two independent unresolved burdens after Group 82:

```text
weighted geometric neutrality;
local payload inertness.
```

Solving one does not solve the other.

For example:

```text
weighted charge = 0
```

does not imply:

```text
source payload = 0
trace payload = 0
mass payload = 0
divergence payload = 0
```

So even if Group 83 derives the skew geometrically, a later inertness/payload theorem is still needed.

## Boundary

The script does not prove payload inertness. It defines what would have to vanish or be absent.

## Steering Consequence

A good follow-up after weighted-skew derivation would be:

```text
local_rho_inertness_test
```

or a more covariant version of the payload filter.
