# Synthesis Proof 16: Regular Source Basis

## Purpose

This report constructs signed source profiles satisfying the first
regularity/admissibility condition:

```text
integral_0^1 aS dx = 0.
```

It then compares their `psi_k` projection signatures with positive source
probes.

## Validated Checks

- positive even monomial probes fail first admissibility: passed
- balanced monomial-minus-constant basis satisfies first admissibility: passed
- balanced coefficient c_q=3/((2q+1)(2q+3)): passed
- balanced source basis independent over tested truncation: passed
- balanced source projection signatures retain full tested rank: passed
- signed admissible example recovered as B_1: passed

## Positive Source Probes

Positive even monomials:

```text
S_q = x^(2q)
```

fail the first admissibility condition:

```text
integral_0^1 aS_q dx > 0.
```

Exact checked values and projection signatures:

```text
S=x^0: int aS=2/3, psi signature=[-256/5775, -256/35035, -256/135135, -256/401115, -768/3002285]
S=x^2: int aS=2/15, psi signature=[256/225225, -256/315315, -256/626535, -256/1344915, -5888/63047985]
S=x^4: int aS=2/35, psi signature=[256/225225, -256/5360355, -1792/18706545, -256/4103715, -256/6938295]
S=x^6: int aS=2/63, psi signature=[256/425425, 256/4849845, -256/14549535, -768/37182145, -256/16900975]
S=x^8: int aS=2/99, psi signature=[256/799425, 256/4849845, 256/91265265, -256/42902475, -2816/456326325]
S=x^10: int aS=2/143, psi signature=[256/1426425, 2816/70984095, 256/35102025, -256/386122275, -256/111205575]
S=x^12: int aS=2/195, psi signature=[256/2414425, 256/9100525, 256/35102025, 256/219559725, -256/423361575]
```

## Balanced Signed Basis

Define:

```text
B_q(x) = x^(2q) - c_q
```

with:

```text
c_q = integral a x^(2q) dx / integral a dx.
```

SymPy verifies the closed form:

```text
c_q = 3 / ((2q+1)(2q+3)).
```

Therefore:

```text
integral_0^1 a B_q dx = 0.
```

Exact balanced sources and their projection signatures:

```text
B_1=x^2-1/5: (5*x**2 - 1)/5, psi signature=[1024/102375, 1024/1576575, -1024/34459425, -7168/114317775, -1024/24249225, -1024/40028625]
B_2=x^4-3/35: (35*x**4 - 3)/35, psi signature=[38912/7882875, 108544/187612425, 305152/4583103525, -2048/266741475, -108544/7250518275, -63488/5323807125]
B_3=x^6-1/21: (21*x**6 - 1)/21, psi signature=[72704/26801775, 31744/79214135, 1024/14101857, 1024/105172353, -1024/345262775, -74752/15971421375]
B_4=x^8-1/33: (33*x**8 - 1)/33, psi signature=[4096/2462229, 20480/74687613, 1994752/33129291195, 2707456/202456779525, 1134592/717801309225, -413696/311931637875]
B_5=x^10-3/143: (143*x**10 - 3)/143, psi signature=[17408/15690675, 21545984/111657981435, 33762304/717801309225, 100484096/7895814401475, 118469632/38658727653975, 145470464/879959150445375]
B_6=x^12-1/65: (65*x**12 - 1)/65, psi signature=[2197504/2788660875, 2377728/16917875975, 88064/2416839425, 76220416/6938745989175, 846718976/254210421239775, 76859392/97773238938375]
B_7=x^14-1/85: (85*x**14 - 1)/85, psi signature=[41984/71504125, 195584/1849322475, 7457792/262022575815, 11643904/1268959792815, 89406464/28493915347755, 10015744/10006224453225]
```

The first member is:

```text
B_1 = x^2 - 1/5,
```

which matches the signed admissible example from the regularity theorem:

```text
F = a(x^2 - 1/5).
```

## Matrix Observation

The tested balanced source basis is linearly independent, and its `psi_k`
projection signature matrix retains full tested rank.

So imposing the first admissibility condition does not collapse the projection
signatures. It removes the purely positive monomial probes and leaves a signed
balanced source space that the projection hierarchy still resolves.
