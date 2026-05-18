# candidate_energy_sign_sieve — Result Note

## Result

The script compares simple energy-density closures:

```text
u=0
u=P
u=-P
```

It finds:

```text
u=0:
  trace diagnostic = P
  active diagnostic = P

u=P:
  trace diagnostic = 0
  active diagnostic = 2P

u=-P:
  trace diagnostic = 2P
  active diagnostic = 0
```

It also exposes sign/positivity burden for `u=±P` through interior values such as:

```text
u(0) for u=P =
-4R^2*p0*(7R^2-2ell^2)/(7R^2+ell^2)^2

u(0) for u=-P =
+4R^2*p0*(7R^2-2ell^2)/(7R^2+ell^2)^2
```

## Main Findings

No simple closure solves the accounting problem.

The zero-energy closure is rejected because it leaves both diagnostics open.

The trace-free closure:

```text
u=P
```

closes trace but leaves active-mass burden.

The active-mass-neutral closure:

```text
u=-P
```

closes active mass but leaves trace burden.

The sign behavior is also not automatically admissible. Depending on parameter regime and location, the proposed `u` choices can change sign or demand a sign convention that has not been derived.

## Boundary

This is not a full energy-condition theorem. It is a reduced sign/accounting warning.

## Steering Consequence

The next check should test amplitude origin. Even if the closure form were acceptable, the coefficient `p_free` still needs a non-repair, non-source-coupled origin.
