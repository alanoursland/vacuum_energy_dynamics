# Vacuum Dimension Selector 27: Dimension Selector Dependency Table

## Purpose

This report makes the dependencies explicit so that the folder cannot be read
as deriving four-dimensional spacetime from the scalar projection hierarchy
alone.

## Validated Arithmetic

- `n=3` plus one clock gives `D=4`: passed
- `D=4` gives two massless spin-2 degrees of freedom: passed
- `D=4` gives a three-dimensional spacetime boundary hypersurface: passed

## Dependency Table

| Selector | Required Assumption | Result | Remaining Dependency |
|---|---|---|---|
| Conserved scalar flux | radial flux model in n-space | n=3 for inverse-square | does not derive spacetime |
| One clock channel | exactly one time direction | D=n+1=4 | clock channel imported |
| Massless spin-2 | standard weak-field GR lift | two polarizations at D=4 | metric lift imported |
| Lovelock action | local metric, diffeomorphism invariance, second-order equations | EH curvature term singled out in D=4 | assumptions imported |
| Boundary hypersurface | spacetime boundary data | D=4 gives three-boundary induced metric | scalar sector incomplete |

## Interpretation

The current proof chain is a selector intersection, not a complete ontological
derivation. Its value is that it isolates which assumptions must be supplied by
the parent vacuum theory.
