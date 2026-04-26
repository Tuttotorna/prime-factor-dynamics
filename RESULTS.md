Results

This file contains raw empirical results used in the repository.

---

Basin Distribution — T(n) = sum of prime factors (with multiplicity)

Parameters:

- N = 1000
- MAX_STEPS = 40

Observed attractors:

5  → 297
7  → 173
11 → 68
13 → 67
19 → 43
17 → 32
23 → 29
29 → 18
31 → 17
37 → 10

---

Distinct Factor-Sum Dynamics

Transformation:

T'(n) = sum of distinct prime factors

Observed:

5  → 193
7  → 176
2  → 168
3  → 103
13 → 56
19 → 34

---

Multiplicity Gain

Difference between T and T':

Top gains:
5  → +104
11 → +66
17 → +26
23 → +18

Top losses:
2 → -167
3 → -102

---

Alternative Linear Dynamics

Transformation:

T_alt(n) = sum(distinct primes) + number of prime factors

Observed (N = 300):

8 → 120
5 → 119
6 → 35
7 → 22
4 → 3

---

Exponent-Weighted Dynamics

Transformation:

T_k(n) = sum(p^k for p in PF(n))

Observed:

k = 1 → stable attractors
k = 2 → escape
k = 3 → escape

---

Notes

- Results are empirical
- No formal proofs provided
- Range limited to tested N