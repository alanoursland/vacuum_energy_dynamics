# Radiative TT Averaging

## Purpose

This directory holds the first targeted covariant-lift rigor upgrade:
Isaacson-style averaging for the radiative transverse-traceless sector.

Current status: completed at the local inertial short-wave level. See
`radiative_tt_averaging_note.md` and the forge script:

```text
vacuum_forge/src/field_equation_trials/015_isaacson_averaging/isaacson_tt_averaging.py
```

## Scope

The 008 radiative bootstrap derives the TT normalization and verifies
positivity/null transport directly on explicit waves. Its remaining
radiative rigor debt included averaging assumptions: secular terms,
total derivatives, and scale separation.

This note closes only the averaging part. It does not claim the separate
gauge-invariance lift of averaged \(<t_{ab}>\); that remains the next
radiative subpiece.

## Assumptions

The averaging theorem is stated in a local inertial patch with:

- short wavelength \(\lambda\);
- background/envelope scale \(L\);
- averaging window \(\ell_{\rm avg}\) satisfying
  \(\lambda \ll \ell_{\rm avg} \ll L\);
- TT perturbations \(h^{TT}_{ij}\);
- periodic fast phase \(\theta\), with slow amplitudes treated as
  constant across one averaging cell up to \(O(\lambda/L)\).

Under these assumptions, fast total derivatives and mixed fast/slow
cross terms average away, and the leading averaged stress takes the
standard local form:

$$
<t_{ab}> =
{c^4\over 32\pi G}
<\partial_a h^{TT}_{ij}\partial_b h^{TT}_{ij}>
$$

up to corrections suppressed by powers of \(\lambda/L\).

## Forge Proof

The forge script validates:

1. periodic averages:
   \(<\sin\theta>=<\cos\theta>=<\sin\theta\cos\theta>=0\),
   \(<\sin^2\theta>=<\cos^2\theta>=1/2\);
2. fast total derivative averages vanish over a full cell;
3. for \(h=A(U)\cos\theta\), the averaged derivative product splits
   into a leading fast piece plus a slow-envelope correction, with the
   cross term exactly zero;
4. for a retarded TT wave, the averaged derivative products are positive
   and null-transported.

Archive result:

```text
isaacson_tt_averaging_015
```

The corresponding obligation record is:

```text
isaacson_averaging_rigor_015
```

