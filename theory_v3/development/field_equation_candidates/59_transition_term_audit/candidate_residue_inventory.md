# candidate_residue_inventory — Result Note

## Result

The script inventories the main transition-term ingredients from Groups 57 and 58.

The blend residues are:

```text
R1 = (F_out - F_in)*s'
R2 = (F_out - F_in)*s'' + 2*(F_out' - F_in')*s'
```

The weighted-neutral layer shape is:

```text
eta(y)=w(y)*(y-c*)
```

with:

```text
w(y)=(1-y^2)^2
c*=2Rell/(7R^2+ell^2)
```

The stress-like basis is:

```text
eta^2
```

## Main Findings

This inventory is useful because it separates three different kinds of objects:

```text
R1/R2:
  transition residues, candidate clues from blending;

eta:
  weighted-neutral scalar layer shape;

eta^2:
  positive stress-like layer basis requiring filters.
```

The residues are not inserted terms. `eta` is not ordinary source. `eta^2` is not automatically a stress tensor.

That distinction is the main value of this script. It creates a candidate surface without upgrading it.

## Boundary

This is inventory only. It does not prove locality, neutrality, source safety, divergence safety, or covariant lift.

## Steering Consequence

The next filter should be locality. Candidate transition terms must be layer-localized and must not leak as constant/background terms.
