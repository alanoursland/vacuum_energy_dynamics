# Scalaron Screening Appeal Note

## Purpose

This directory holds the bounded follow-up for the scalaron screening
obligation recorded in `04_field_equations/05_open_obligations.md`.

Current status: completed. See `scalaron_screening_note.md` and the
forge script
`vacuum_forge/src/field_equation_trials/013_scalaron_screening/scalaron_screening_p7prime_obstruction.py`.

The admitted equations already set

$$a=0$$

at four-derivative order. This note does not reopen that result. Its job
is narrower: close the predictable objection that scalaron screening
might rescue

$$a \neq 0$$

from the E3 contradiction with P7'.

## Current Status

The closed theory chain is:

```text
G20:
  at <= 4 derivatives, ghost safety leaves only a R^2 + Gauss-Bonnet

E3:
  any a != 0 gives mandatory scalaron hair around static sources
  scalaron hair gives AB != 1 / preferred static t-r frame
  P7' forbids that static vacuum structure
  therefore a = 0
```

The screening note is an appeal-file supplement to E3. It should explain
why "screened" scalar hair still does not pass P7' unless P7' itself is
re-scoped by theory-owner decision.

## What Was Done

1. **Objection stated cleanly.**

   Screening might make the scalaron profile short-ranged, small,
   environment-dependent, or hard to observe. Does that allow
   \(a \neq 0\) while keeping the admitted theory?

2. **Observational screening separated from structural compatibility.**

   G20 screening language concerns detectability and bench-top bounds.
   P7' is an exact static-frame-indifference condition. A small
   violation is still a violation unless P7' is explicitly weakened.

3. **Local P7' obstruction proved for a general screened scalar
   profile.**

   In the scalaron weak-field exterior, write the scalar contribution as
   \(q(r)\):

   $$\phi=\phi_{\rm GR}-q(r), \qquad \psi=\phi_{\rm GR}+q(r).$$

   In areal gauge E3 gives

   $$AB-1=\frac{2}{c^2}\left(\phi+r\psi'\right).$$

   The GR part cancels:

   $$\phi_{\rm GR}+r\phi_{\rm GR}'=0.$$

   Therefore the scalar contribution is

   $$\phi+r\psi'=r q'(r)-q(r).$$

   Exact P7' requires

   $$r q'(r)-q(r)=0.$$

   The solution is

   $$q(r)=C r.$$

   Asymptotic flatness forces \(C=0\), hence

   $$q(r)\equiv0.$$

   So any nonzero screened scalar profile still violates P7'. Screening
   changes the size or support of the violation; it does not convert it
   into an allowed static vacuum configuration.

4. **Connected to E3 mandatory hair.**

   E3 already proves that for \(a\neq0\), static sourced bodies leak
   scalaron hair. Combining that with the general obstruction above:

   ```text
   a != 0 -> mandatory q != 0 somewhere
   q != 0 somewhere -> P7' violation
   therefore P7' -> a = 0
   ```

5. **Only escape stated.**

   The theory owner may appeal by re-scoping P7' to exclude the
   scalaron layer, to apply only beyond some range, or to apply only to
   the two-derivative sector. That is not a screening rescue inside the
   admitted theory; it is a postulate revision. It needs independent
   grounding, otherwise it is recovery-shaped.

6. **Obligations ledger updated.**

   The scalaron screening note was moved from active rigor debts to
   retired rigor debts in `04_field_equations/05_open_obligations.md`,
   with this directory and the forge script as discharge pointers.

## Forge Proof

The prose appeal note uses existing validated inputs:

- G20 validates the scalaron class, \(\alpha=1/3\), and its ghost safety.
- E3 validates mandatory hair and the P7' contradiction.

Because item 3 is proof-bearing, it is machine-checked in vacuum forge
with SymPy.

The forge script lives under:

```text
vacuum_forge/src/field_equation_trials/013_scalaron_screening/
```

Script:

```text
scalaron_screening_p7prime_obstruction.py
```

Archive dependencies:

- `009_trial_E_boundary_admissibility__trial_E3_p7prime_vs_scalaron`
  - `shadow_violation_e3`
  - `mandatory_hair_e3`
  - `p7prime_forces_a_zero_e3`
- `010_gate_G20_beta_health__gate_G20_beta_health`
  - `scalaron_health_g20`
  - `alpha_one_third_g20`

SymPy checks:

1. For arbitrary \(q(r)\), verify

   $$\phi+r\psi'=r q'-q$$

   after substituting

   $$\phi=-GM/r-q,\qquad\psi=-GM/r+q.$$

2. Solve the exact P7' condition

   $$r q'-q=0$$

   and record that asymptotic flatness kills the only solution
   \(q=C r\), leaving \(q=0\).

3. Verify that the G20 Yukawa profile

   $$q(r)=\frac{GM}{3r}e^{-r/\ell_*}$$

   gives a nonzero P7' shadow:

   $$r q'-q \neq 0.$$

4. Records the governance result:

   ```text
   screening_does_not_rescue_scalaron_under_P7prime
   ```

   with status `DERIVED` when the symbolic checks pass.

## Acceptance Criteria

The scalaron screening obligation is retired. The note states:

- screening suppresses detectability, not the exact P7' obstruction;
- any nonzero screened scalar profile gives \(AB\neq1\) somewhere under
  the static scalaron form;
- E3 already proves nonzero hair is mandatory for \(a\neq0\);
- therefore screening cannot rescue \(a\neq0\) unless P7' is re-scoped;
- re-scoping P7' is the existing theory-owner appeal, not an admitted
  result.

The general-profile lemma is proof-bearing, so the forge script was
added before the obligation was retired.
