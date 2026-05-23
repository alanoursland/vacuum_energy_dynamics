# candidate_shape_origin_problem — Analysis Note

## Result

`candidate_shape_origin_problem.py` opens Group 86 as a structural-origin test for the Group 85 profile:

```text
P(y) = 1 - 12y^2 + 51y^4
```

The imported Group 85 status is correct:

```text
even quartic suppression profile found;
M0..M5 vanish;
W0..W3 vanish;
local rho remains nonzero;
M6/W4 remain nonzero;
shape origin remains open;
parent divergence identity unproven;
recombination blocked.
```

## Interpretation

This opener targets exactly the right weak point. Group 85 made the quartic profile look effective, but not yet principled. It was found by moment constraints. Group 86 asks whether that moment-designed shape has an internal origin in the reduced model.

The important distinction is:

```text
moment-derived profile:
  found because it kills chosen moments

reduced structural origin:
  forced by minimal degree and a payload-action criterion

full physical/geometric origin:
  derived from the actual geometry, variational physics, or covariant structure
```

Group 86 aims for the second, not the third.

## What Changed

The status question becomes sharper. The project is no longer asking whether `P` works. Group 85 answered that. Group 86 asks why this `P` appears inside the reduced model.

## What Did Not Change

The opener correctly preserves the cautions:

```text
M6/W4 remain;
local rho remains nonzero;
reduced origin is not full geometry;
parent equation remains blocked.
```

## Steering Consequence

The group should be judged by whether it proves an origin inside the reduced model, such as minimal degree, quartic uniqueness, and payload-action minimization. The results show that it does.
