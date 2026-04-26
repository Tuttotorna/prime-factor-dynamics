# Theorems

This file contains formally established properties of the prime-factor-sum dynamics.

---

## Definition

Let:

```text
T(n) = sum of prime factors of n, counted with multiplicity

Examples:

12 = 2 × 2 × 3  →  T(12) = 7
20 = 2 × 2 × 5  →  T(20) = 9


---

Theorem 1 — Monotonicity

For every integer n ≥ 2:

T(n) ≤ n

Moreover:

T(n) = n  ⇔  n is prime or n = 4

Proof

Let:

n = p1 × p2 × ... × pk

where each pi ≥ 2.

Then:

T(n) = p1 + p2 + ... + pk

For integers a, b ≥ 2:

a + b ≤ a * b

with equality only when:

a = b = 2

Applying this inequality iteratively:

p1 + p2 + ... + pk ≤ p1 × p2 × ... × pk = n

Equality holds only in the following cases:

k = 1 → n is prime

k = 2 and p1 = p2 = 2 → n = 4



---

Theorem 2 — Convergence

For every integer n ≥ 2, the sequence:

n, T(n), T²(n), T³(n), ...

eventually reaches a fixed point.

Proof

From Theorem 1:

T(n) ≤ n

and for all non-fixed points:

T(n) < n

Therefore, the sequence is non-increasing and strictly decreasing until it reaches a fixed point.

A strictly decreasing sequence of positive integers must terminate.

Thus, every trajectory reaches some m such that:

T(m) = m


---

Fixed Points

The fixed points of T are exactly:

all prime numbers and 4


---

Corollary

For every n ≥ 2, the trajectory under T converges to:

a prime number or 4


---

Interpretation

The transformation T is a dissipative map on ℕ:

it never increases n and strictly decreases it outside fixed points

This explains:

the absence of divergence

the absence of non-trivial cycles

the existence of terminal attractors



---

Status

These results are elementary but fundamental.

They provide:

a formal basis for convergence

a justification for empirical basin observations

a link between multiplicative structure and additive collapse

