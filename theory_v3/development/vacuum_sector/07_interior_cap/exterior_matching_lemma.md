# Exterior Matching Lemma

## Claim

If the exterior field equations and exterior charges are preserved, an interior
modification does not by itself change the exterior proxy. Changing exterior
mass, Lambda, or residual terms leaves the interior-cap ledger and returns to
the appropriate source, Lambda, or residual gate.

## Scope

This is a contract-level exterior-preservation lemma, not a full uniqueness
theorem and not a derivation of a finite interior cap.

## Symbolic Proxy

Use the exterior proxy:

```text
f_ext(r) = 1 - 2GM_ext/(c^2 r) - Lambda_ext r^2/3
```

With fixed exterior data:

```text
d f_ext / d R_cap = 0
```

so the cap radius does not enter the exterior proxy by itself.

Changing the exterior mass gives:

```text
Delta f_ext = -2G delta_M/(c^2 r)
```

Changing the exterior Lambda baseline gives:

```text
Delta f_ext = -delta_Lambda r^2/3
```

Those are not silent interior modifications; they reroute to source/matching
bookkeeping or the Lambda selector ledger.

## Route Classification

```text
fixed exterior equations plus fixed exterior charges:
    exterior proxy preserved at lemma level

surface-layer charge shift:
    deferred pending junction/source bookkeeping

Lambda baseline shift:
    rejected here; return to Lambda selector ledger

exterior residual leak:
    rejected here; return to epsilon residual gates
```

## Current Classification

The VacuumForge lemma records:

```text
derivation: exterior_matching_lemma_026
obligation satisfied: exterior_matching_lemma_required_025
new obligation: finite_strain_admissibility_probe_required_026
```

Current conclusion:

```text
Exterior preservation is licensed only at the fixed-charge contract level.
```

This does not license an interior cap. It only clears the path to ask whether
a finite-strain admissibility rule can derive a cap scale.
