# Prime-Factor Dynamics

Discrete dynamical systems on natural numbers induced by prime-factor transformations.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19783160.svg)](https://doi.org/10.5281/zenodo.19783160)
**Author:** Massimiliano Brighindi  
**Project:** MB-X.01

---

## Overview

This repository studies a simple experimental question:

> Do numerical structures belong only to numbers themselves, or can they emerge from the transformations applied to them?

The focus is on transformations defined through prime factorization and on the dynamics produced by iterating those transformations.

This is an experimental mathematical repository.

It provides:

- definitions
- reproducible scripts
- empirical results
- attraction basin analysis
- preliminary regime classification

It does not yet claim a complete theory or formal proof.

---

## Core Idea

Every integer `n >= 2` has a prime factorization.

Example:

```text
12 = 2 × 2 × 3

From this factorization we define transformations such as:

T(n) = sum of prime factors of n

Then we iterate:

n → T(n) → T(T(n)) → ...

The resulting trajectory may reach a fixed point, a cycle, or diverge depending on the transformation.


---

Primary Transformation

The main transformation studied here is:

T(n) = sum of prime factors of n, counted with multiplicity

Examples:

12 = 2 × 2 × 3  →  2 + 2 + 3 = 7
18 = 2 × 3 × 3  →  2 + 3 + 3 = 8
20 = 2 × 2 × 5  →  2 + 2 + 5 = 9

A trajectory example:

20 → 9 → 6 → 5

because:

20 = 2 × 2 × 5  → 9
9  = 3 × 3      → 6
6  = 2 × 3      → 5
5  = prime      → 5


---

Definitions

Prime factors

Let PF(n) be the multiset of prime factors of n.

Example:

PF(12) = {2, 2, 3}


---

Factor-sum transformation

T(n) = sum(PF(n))


---

Trajectory

A trajectory is the sequence produced by repeated application of T:

n, T(n), T(T(n)), ...


---

Attractor

An attractor is a fixed point or cycle reached by iteration.

In the main factor-sum dynamics, primes are fixed points:

5 → 5
7 → 7
11 → 11


---

Basin of attraction

The basin of an attractor a is the set of numbers that eventually reach a.

Example:

8  → 6 → 5
9  → 6 → 5
14 → 9 → 6 → 5
15 → 8 → 6 → 5

These numbers belong to the basin of 5.


---

Reproducible Result

For:

N = 1000
T(n) = sum of prime factors with multiplicity

the dominant attraction basins observed were:

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

The main observed hierarchy is:

5 > 7 >> 11 ≈ 13


---

Basin Distribution



For N = 1000, the dominant terminal attractor is 5, followed by 7, 11, and 13.


---

Why 5 Dominates

The attractor 5 dominates because many low-complexity composite structures flow through a compact channel:

8 → 6 → 5
9 → 6 → 5

with secondary branches:

14 → 9 → 6 → 5
15 → 8 → 6 → 5
16 → 8 → 6 → 5
18 → 8 → 6 → 5
20 → 9 → 6 → 5
24 → 9 → 6 → 5

Core channel:

{8, 9} → 6 → 5

So 5 is not merely a small prime.

Under this transformation, it acts as a dominant terminal attractor.


---

Role of Multiplicity

A key test compares two transformations.

With multiplicity

T(n) = sum of all prime factors, counted with multiplicity

Example:

8 = 2 × 2 × 2  →  2 + 2 + 2 = 6

Without multiplicity

T'(n) = sum of distinct prime factors

Example:

8 = 2 × 2 × 2  →  2

Empirical result for N = 1000:

With multiplicity:
5 → 297
7 → 173

Distinct only:
5 → 193
7 → 176
2 → 168
3 → 103

Conclusion:

5 remains a strong attractor,
but its dominance is amplified by prime-factor multiplicity.

Multiplicity redirects mass away from 2 and 3 toward composite sums that eventually converge to 5.


---

Multiplicity Gain

Comparing the two transformations shows how much each attractor gains or loses from multiplicity.

Observed for N = 1000:

Top gains:
5  → +104
11 → +66
17 → +26
23 → +18

Top losses:
2 → -167
3 → -102

Interpretation:

Prime-factor multiplicity redistributes mass from small primes (2, 3)
into composite sums that converge toward higher attractors, especially 5.


---

Alternative Transformations

The project also tests related transformations.


---

Distinct prime factor sum

T'(n) = sum of distinct prime factors

This weakens the dominance of 5 and increases the role of 2 and 3.


---

Exponent-weighted factor sum

T_k(n) = sum(p^k for p in PF(n))

For:

k = 2, 3

the system becomes expansive.

Empirical behavior:

k = 1 → stable attractors
k = 2 → mostly escape
k = 3 → escape

Interpretation:

Linear prime-factor summation creates terminal attractors.
Exponent-weighted factor summation turns the system expansive.


---

Alternative linear transformation

Another tested transformation:

T_alt(n) = sum(distinct prime factors) + number of prime factors

For N = 300, observed attractors were:

8 → 120
5 → 119
6 → 35
7 → 22
4 → 3

Conclusion:

Linear arithmetic dynamics can generate stable attraction hierarchies,
but the dominant attractor depends on the transformation.

So 5 is not universal.

The existence of a hierarchy is more general than the identity of the dominant attractor.


---

Regime Classification

The experiments suggest three broad regimes.


---

1. Dissipative transformations

These collapse information too aggressively.

Examples:

digit_sum
digit_product

They often converge toward trivial states such as:

1
0
small fixed points


---

2. Compressive linear transformations

These reduce complexity while preserving enough structure to form meaningful attractors.

Example:

T(n) = sum of prime factors

This regime generates stable attraction basins and prime-based hierarchies.


---

3. Expansive nonlinear transformations

These amplify values and tend toward escape or divergence.

Example:

T_k(n) = sum(p^k), k >= 2


---

Main Insight

The central insight is:

Structure is not only in the numbers.
Structure emerges from the transformations applied to them.

More precisely:

transformation → dynamics → attractors → hierarchy

The observed hierarchy is not simply a static property of individual numbers.

It is induced by the rule used to transform them.


---

Current Status

This project currently provides:

experimental definitions

reproducible scripts

observed attraction basins

comparison between related transformations

preliminary regime classification


It does not yet provide:

formal proofs

asymptotic bounds

complete classification of all transformations

universal theorems



---

Quick Start

Run:

python run_basins.py

Expected output includes the basin distribution for:

N = 1000
T(n) = sum of prime factors with multiplicity

Typical dominant basins:

5  → 297
7  → 173
11 → 68
13 → 67

To generate the basin distribution plot:

python plot_basins.py


---

Minimal Script

The core experiment is:

from collections import Counter

N = 1000
MAX_STEPS = 40

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors

def T(n):
    if n <= 1:
        return n
    return sum(prime_factors(n))

def iterate(n):
    seen = set()
    for _ in range(MAX_STEPS):
        if n in seen:
            break
        seen.add(n)
        n = T(n)
    return n

basins = Counter()

for n in range(2, N + 1):
    basins[iterate(n)] += 1

for k, v in basins.most_common():
    print(f"{k}: {v}")


---

Working Hypotheses

H1 — Prime Attractor Hierarchy

Under linear prime-factor-sum dynamics, prime numbers form a hierarchy of terminal attractors.


---

H2 — Multiplicity Amplification

Prime-factor multiplicity amplifies the dominance of 5 by redirecting mass from powers of 2 and 3 into composite channels such as:

8 → 6 → 5
9 → 6 → 5


---

H3 — Transformation Dependence

The dominant attractor is not universal.

It depends on the chosen transformation.


---

H4 — Regime Separation

Arithmetic transformations can be classified by their dynamical regime:

dissipative
compressive
expansive


---

Future Work

Planned directions:

prove convergence properties for the linear factor-sum map

study basin growth as N → ∞

compare attraction hierarchy across transformation families

classify transformations into dissipative, compressive, and expansive regimes

visualize basin graphs

search for other nontrivial arithmetic dynamics

formalize transformation-induced structure as a general framework



---

License

MIT License.

