# candidate_lift_cleanliness_requirements — Result Note

## Result

`candidate_lift_cleanliness_requirements.py` states the legal closure routes for lift cleanliness.

The residual after boundary anti-match is:

```text
R_lift = L_bulk + L_gauge
```

Two legal closure routes are visible:

```text
independent neutrality:
  L_bulk = 0
  L_gauge = 0

lawful shared identity:
  L_bulk + L_gauge = 0
  derived from lift/gauge structure
```

Both reduce the residual to zero algebraically.

## Main Findings

The script correctly distinguishes compatibility from theorem. Independent neutrality and shared identity are legal forms, but neither is proven by the algebra alone.

The rejected closures are the key governance result:

```text
drop L_bulk/L_gauge by prose;
choose L_bulk=-L_gauge as repair;
hide a repair current;
use active O by label.
```

## Boundary

The script states requirements. It does not derive independent neutrality or a shared lift identity.

## Steering Consequence

Proceed to bulk neutrality. The next script should test whether `L_bulk = 0` can be derived or remains only a compatibility condition.
