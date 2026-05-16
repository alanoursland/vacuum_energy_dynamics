# candidate_divergence_filter — Result Note

## Result

The script applies a reduced divergence filter to weighted-layer stress candidates.

For radial stress built from the weighted-neutral shape:

```text
p_r = p0*eta^2
```

the radial-only candidate:

```text
p_t=0
```

generically gives:

```text
D != 0
```

and is rejected.

The closure-supported candidate uses:

```text
p_t = p_r + r*p_r'/2
```

and gives:

```text
D = p_r' + 2*(p_r-p_t)/r = 0
```

## Main Findings

This script is important because it prevents the weighted layer from being treated as a simple scalar/radial pressure blob.

A radial-only layer stress fails the reduced divergence test. The candidate only survives if it carries a tangential closure.

So the surviving candidate class is narrower:

```text
localized;
weighted-neutral;
source/trace incidence-clean;
closure-supported;
reduced-divergence silent.
```

This is a useful restriction. It turns the route from “any weighted-neutral layer response” into “a closure-supported transition response.”

## Boundary

Reduced `D=0` is not a covariant Bianchi proof. The closure is not an inserted stress tensor and not parent closure.

## Steering Consequence

The classifier should retain only the closure-supported candidate family and reject radial-only or divergence-failing transition terms.
