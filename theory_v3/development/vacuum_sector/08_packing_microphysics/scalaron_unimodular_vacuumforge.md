# VacuumForge: The Scalaron vs the Unimodular Constraint (O-P10-3)

## Purpose

Attacks the P7' tension: the packing's f'' term is R^2-class, carrying
a scalaron that P7' (as adopted) forbids. Tests the proposed
resolution -- that the unimodular constraint (P3's seat) projects the
scalaron out -- and records the actual resolution.

## Verified Results

```text
1. THE PROPOSED MECHANISM IS REFUTED (in-house). The f(R) EL tensor is
   identically conserved (verified on FRW for f = R + alpha R^2, no
   field equations imposed), so the divergence of the traceless
   (unimodular) equations reconstructs the trace equation up to an
   integration constant:

       f'R - 2f + 3 box f' = kappa T + const
       =>  (6 alpha box - 1) R = kappa T + const.

   The scalaron propagates with m^2 = 1/(6 alpha), exactly as in
   full-diff f(R). The same Bianchi mechanism that made Lambda an
   integration constant (033) resurrects the scalaron here.
   Unimodular f(R) = f(R) + free Lambda -- no more, no less.

2. THE RANGE NUMBERS. The packing coefficient alpha ~ |f''/2f'| a^2
   gives scalaron range l* = sqrt(6 alpha) ~ a: for Planck packing,
   ~4e-35 m vs the 54-micron laboratory frontier -- margin ~1e30.
   Every observable is exactly as P7'-exact predicts.

3. THE INFLECTION ALTERNATIVE. Strict all-orders P7' exactness is
   equivalent to f''(Delta_0) = 0 (verified: the R^2-class coefficient
   is exactly f''/2), an inflection of the wedge energy at the
   frustrated ground state -- with the recorded recovery-shaped cost.
```

## The Resolution (reduced to a scoping ruling)

O-P10-3 is now fully understood; what remains is a one-line
theory-owner ruling between:

```text
(i)  P7'-SCOPED (recommended): P7' exact in the a -> 0 idealization,
     with the Planck-range scalaron as a controlled O(a^2) correction
     WITHIN the postulate -- the exact precedent of the F1 expansion
     leak, which P7' already carries ("a correction within the
     postulate, not a violation of it"). Observable face unchanged;
     E3/G20 kills stand; the null-test falsifier is untouched.

(ii) STRICT EXACTNESS: adopt f''(Delta_0) = 0 as a wedge-energy
     constraint (inflection at the ground state). Kills the R^2 class
     exactly; costs an unmotivated constraint on f (recovery-shaped
     unless a reason emerges -- e.g., a microphysical symmetry of the
     wedge potential).

The ruling is a scoping clarification of adopted P7', not a new
adoption. Recommendation on record: route (i), by precedent and
economy.
```

## Ledger Effect

```text
O-P10-3: attacked; the candidate cancellation mechanism refuted
in-house; the tension reduced to a pre-analyzed scoping ruling
(p7prime_scoping_ruling_047, theory owner). No coefficient moves under
either route; no observable changes under either route.
```

## Verification

```text
vacuum_forge/src/vacuum_sector/047_scalaron_unimodular/scalaron_unimodular.py
```

Archive record: `scalaron_unimodular_047`.
