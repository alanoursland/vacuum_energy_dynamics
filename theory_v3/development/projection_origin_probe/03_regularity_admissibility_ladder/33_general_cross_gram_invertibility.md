# Regularity Ladder Proof 33: General Cross-Gram Invertibility

## Purpose

This report tests the cross-Gram invertibility mechanism for the generalized
endpoint-contact row family.

## Objects

Rows:

```text
chi_(R,k)(y)
  = y^k - ((2k-1)/(2k+2R+3))y^(k-1).
```

Balanced source coordinates:

```text
B_(R,q)(y) = y^q - c_(R,q).
```

Pairing weight:

```text
(1-y)^(R+4)y^(-1/2).
```

## Validated Checks

- general-R chi/balanced cross Gram determinants nonzero for R=0..4 N=1..5: passed

## Determinant Data

Small exact determinants:

```text
R=0, N=1: det=512*(beta(1/2, 2) + 39*beta(3/2, 2))/(225225*beta(1/2, 2))
R=0, N=2: det=4194304*(-12*beta(3/2, 2) + beta(1/2, 2) + 51*beta(5/2, 2))/(1207285954875*beta(1/2, 2))
R=0, N=3: det=137438953472*(-969*beta(5/2, 2) + beta(1/2, 2) + 153*beta(3/2, 2) + 1615*beta(7/2, 2))/(17020920328542903898125*beta(1/2, 2))
R=0, N=4: det=36028797018963968*(-166060*beta(7/2, 2) - 4332*beta(3/2, 2) + 131*beta(1/2, 2) + 51186*beta(5/2, 2) + 163875*beta(9/2, 2))/(136900210194117395471418441203109375*beta(1/2, 2))
R=1, N=1: det=1024*(beta(1/2, 3) + 15*beta(3/2, 3))/(315315*beta(1/2, 3))
R=1, N=2: det=33554432*(-51*beta(3/2, 3) + 8*beta(1/2, 3) + 323*beta(5/2, 3))/(233972018054775*beta(1/2, 3))
R=1, N=3: det=2199023255552*(-1083*beta(5/2, 3) + 7*beta(1/2, 3) + 171*beta(3/2, 3) + 2185*beta(7/2, 3))/(3272782560772229561531475*beta(1/2, 3))
R=1, N=4: det=9223372036854775808*(-23000*beta(7/2, 3) - 432*beta(3/2, 3) + 31*beta(1/2, 3) + 25875*beta(9/2, 3) + 6486*beta(5/2, 3))/(122799488544123303737862341759189109375*beta(1/2, 3))
R=2, N=1: det=4096*(5*beta(1/2, 4) + 51*beta(3/2, 4))/(6891885*beta(1/2, 4))
R=2, N=2: det=268435456*(-114*beta(3/2, 4) + 1197*beta(5/2, 4) + 37*beta(1/2, 4))/(20957207902906275*beta(1/2, 4))
R=2, N=3: det=281474976710656*(-1173*beta(5/2, 4) + 17*beta(1/2, 4) + 201*beta(3/2, 4) + 2875*beta(7/2, 4))/(3494864234538916567492539375*beta(1/2, 4))
R=2, N=4: det=2361183241434822606848*(-23460*beta(7/2, 4) - 276*beta(3/2, 4) + 55*beta(1/2, 4) + 30015*beta(9/2, 4) + 6210*beta(5/2, 4))/(526546664093122994527419741128865873984375*beta(1/2, 4))
R=3, N=1: det=8192*(57*beta(3/2, 5) + 7*beta(1/2, 5))/(22863555*beta(1/2, 5))
R=3, N=2: det=8589934592*(-7*beta(3/2, 5) + 161*beta(5/2, 5) + 6*beta(1/2, 5))/(232081672702554675*beta(1/2, 5))
R=3, N=3: det=18014398509481984*(-115*beta(5/2, 5) + 23*beta(3/2, 5) + 345*beta(7/2, 5) + 3*beta(1/2, 5))/(133969795657325135087214009375*beta(1/2, 5))
R=3, N=4: det=604462909807314587353088*(-27840*beta(7/2, 5) - 120*beta(3/2, 5) + 107*beta(1/2, 5) + 40455*beta(9/2, 5) + 7110*beta(5/2, 5))/(1916003016032190172705370453255346940976953125*beta(1/2, 5))
R=4, N=1: det=131072*(7*beta(3/2, 6) + beta(1/2, 6))/(63047985*beta(1/2, 6))
R=4, N=2: det=274877906944*(23*beta(5/2, 6) + beta(1/2, 6))/(2426308396435798875*beta(1/2, 6))
R=4, N=3: det=2305843009213693952*(-117*beta(5/2, 6) + 435*beta(7/2, 6) + 29*beta(3/2, 6) + 5*beta(1/2, 6))/(90064239898719943088177054484375*beta(1/2, 6))
R=4, N=4: det=154742504910672534362390528*(-269700*beta(7/2, 6) + 1116*beta(3/2, 6) + 445005*beta(9/2, 6) + 68382*beta(5/2, 6) + 1597*beta(1/2, 6))/(44628064795698873190882408243710792407491822265625*beta(1/2, 6))
```

## Interpretation

For each tested `R,N`, the generalized rows and balanced source coordinates
produce an invertible cross-Gram matrix.

Together with the kernel theorem, this supports the general picture:

```text
endpoint-contact level R
  -> adapted row family chi_(R,k)
  -> balanced source basis y^q-c_(R,q)
  -> nondegenerate finite coordinate pairing.
```
