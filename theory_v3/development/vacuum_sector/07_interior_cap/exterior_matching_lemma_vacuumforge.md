# VacuumForge Exterior Matching Lemma

## Purpose

This report records the contract-level exterior matching lemma for
interior-cap work. It does not prove a full uniqueness theorem and does not
derive an interior cap.

This report depends on:

```text
interior_cap_admissibility_contract_025
```

It satisfies:

```text
exterior_matching_lemma_required_025
```

## Symbolic Checks

Exterior proxy:

```text
f_ext(r) = -2*G*M_ext/(c**2*r) - Lambda_ext*r**2/3 + 1
d f_ext / d R_cap = 0
```

Exterior charge shift:

```text
Delta f_ext from delta_M = -2*G*delta_M/(c**2*r)
```

Exterior Lambda shift:

```text
Delta f_ext from delta_Lambda = -delta_Lambda*r**2/3
```

If exterior equations and exterior charges are fixed, this proxy has no
dependence on the interior cap radius. If a surface layer changes exterior
mass, or if the Lambda baseline changes, the exterior changes and the claim
must be routed through the appropriate ledger.

## Matching Route Ledger

| route | route | exterior data | matching condition | exterior effect | disposition | next obligation |
| --- | --- | --- | --- | --- | --- | --- |
| fixed_charge_exterior | change only interior variables while preserving exterior charges | M_ext and Lambda fixed | junction conditions must conserve exterior charges | exterior proxy unchanged | lemma-level exterior preservation | now test finite-strain admissibility scale |
| surface_layer_charge_shift | surface layer changes exterior mass or pressure ledger | M_ext -> M_ext + delta_M | source ledger required | exterior changes through charge shift | deferred pending source and junction ledger | write surface/source bookkeeping before use |
| lambda_baseline_shift | interior rule changes exterior Lambda baseline | Lambda_ext -> Lambda_ext + delta_Lambda | must return to Lambda selector ledger | exterior asymptotics change | rejected as wrong ledger here | return to Lambda baseline selector if desired |
| exterior_residual_leak | interior rule leaks into exterior field equation | epsilon K_residual outside object | residual gates required | tested exterior is not protected | rejected as residual-gate reroute | return to epsilon residual gates before use |

## Readiness

| route | fixed exterior equations | fixed exterior charges | matching written | exterior preserved |
| --- | --- | --- | --- | --- |
| fixed_charge_exterior | True | True | True | True |
| surface_layer_charge_shift | True | False | False | False |
| lambda_baseline_shift | True | False | False | False |
| exterior_residual_leak | False | False | False | False |

## Current Conclusion

The fixed-charge exterior route preserves the exterior proxy at lemma level.
This licenses only the exterior-preservation contract, not an interior cap.
Surface charge shifts need source and junction bookkeeping. Lambda shifts and
exterior residual leaks are wrong-ledger moves here.

## Classification

```text
result type: exterior matching lemma
scope: exterior preservation for interior modifications
conclusion: fixed exterior equations plus fixed exterior charges preserve the exterior proxy
non-conclusion: no finite-strain cap, no nonsingularity theorem, no full uniqueness theorem
```

The next technical target is:

```text
finite_strain_admissibility_probe_required_026
```
