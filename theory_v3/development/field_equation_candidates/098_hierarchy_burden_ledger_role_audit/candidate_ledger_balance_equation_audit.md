# candidate_ledger_balance_equation_audit — Analysis Note

## Result

`candidate_ledger_balance_equation_audit.py` writes the burden ledger as:

```text
E_burden = E_exchange + E_interface + E_other + J_curv
```

It also writes the parent correction balance target as:

```text
divergence(H_curv + H_exch) = 0.
```

In symbolic form:

```text
D_total = D_curv + D_exch.
```

If the total correction must be divergence-safe and `D_curv` is nonzero, the required partner is:

```text
D_exch = -D_curv.
```

The classification is:

```text
H_curv alone is safe only if D_curv = 0 independently.

If D_curv != 0, an exchange/source-balance partner is required.

H_exch cannot be inserted by naming the missing partner;
it needs independent definition/source/divergence proof.
```

## Interpretation

This is the most important equation-balance result in Group 98.

It formalizes the intuition that configuration-only accounting may not balance the field equations. If the curvature correction sector is not divergence-safe by itself, then an exchange or source-balance partner is required.

But the script also blocks the dangerous shortcut:

```text
just define H_exch to cancel H_curv.
```

That is not a theory. It is bookkeeping paint unless the exchange term has independent physical definition and source law.

## What Changed

The need for a possible exchange/substance ledger is now stated as a conditional consistency requirement:

```text
if ∇H_curv != 0,
then a real exchange/source partner is required.
```

## What Did Not Change

No exchange term is derived.

No correction tensor is inserted.

No parent equation is written.

## Carry-forward status

```text
BURDEN_LEDGER_REQUIRES_MULTIPLE_CANDIDATE_TERMS
CONFIGURATION_ONLY_BALANCE_DEFERRED
H_CURV_ONLY_SAFE_ONLY_IF_DIVERGENCE_SAFE
EXCHANGE_PARTNER_REQUIRED_IF_CURVATURE_DIVERGENCE_NONZERO
H_EXCH_INSERTABILITY_OPEN
BIANCHI_SAFETY_NOT_DECLARED
```
