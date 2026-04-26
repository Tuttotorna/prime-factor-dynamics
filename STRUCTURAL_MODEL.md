# Structural Model

This document defines the structural layer used in Prime-Factor Dynamics.

The goal is to move from descriptive iteration to measurable structural change.

---

## 1. Structural State

For every integer n >= 2, define its structural state as the multiset of prime factors:

S(n) = PF(n)

Example:

12 = 2 × 2 × 3  
S(12) = {2, 2, 3}

Equivalently, using exponent form:

n = p1^a1 × p2^a2 × ... × pk^ak

we define:

S(n) = {(p1, a1), (p2, a2), ..., (pk, ak)}

This representation makes the structure explicit and comparable.

---

## 2. Transformation

The main transformation is:

T(n) = sum of prime factors of n, counted with multiplicity

Example:

20 = 2 × 2 × 5  
T(20) = 2 + 2 + 5 = 9

This transformation maps multiplicative structure into additive structure.

---

## 3. Trajectory

A trajectory is the sequence:

n0 → n1 → n2 → ...

where:

n_{i+1} = T(n_i)

Each step induces a structural trajectory:

S(n0) → S(n1) → S(n2) → ...

---

## 4. Structural Delta

Define the structural delta between two consecutive states as a distance between their prime-factor multisets.

Let A and B be multisets of prime factors with multiplicities.

Define:

Δ(A, B) = sum over all primes p of |a_p - b_p|

where a_p and b_p are the multiplicities of p in A and B.

This is equivalent to the L1 distance on exponent vectors.

Example:

S(20) = {2,2,5}  → (2:2, 5:1)  
S(9)  = {3,3}    → (3:2)

Δ = |2-0| + |0-2| + |1-0| = 5

Properties:

- Δ(A, B) >= 0  
- Δ(A, B) = 0 iff A = B  
- symmetric: Δ(A, B) = Δ(B, A)

---

## 5. Structural Compression

The map T acts as a compression operator on multiplicative structure.

It transforms:

multiplicative decomposition → additive collapse

This process:

- reduces factorization depth  
- removes prime identity structure  
- preserves only aggregate magnitude  

This compression pushes trajectories toward low-complexity stable states.

---

## 6. Attractors

An attractor is a value reached by iteration.

In the main factor-sum dynamics, primes are fixed points:

T(p) = p

Example:

20 → 9 → 6 → 5

Structural trajectory:

{2,2,5} → {3,3} → {2,3} → {5}

---

## 7. Basin

The basin of an attractor a is:

B(a) = { n | T^k(n) = a for some k >= 0 }

Example (basin of 5):

8, 9, 14, 15, 16, 18, 20, 24

---

## 8. Structural Coherence

For a trajectory of length L, define:

Δ_i = Δ(S(n_i), S(n_{i+1}))

and:

C = 1 / (1 + mean(Δ_i))

Interpretation:

- high C → smooth structural evolution  
- low C → abrupt structural change  

---

## 9. Saturation

A trajectory is saturated when it reaches a fixed point or a cycle.

For prime attractors:

T(p) = p

At saturation:

Δ_i = 0

or the structural sequence becomes periodic.

---

## 10. Interpretation

The basin hierarchy is not only a property of individual numbers.

It is induced by the transformation:

transformation → structural trajectory → attractor → basin hierarchy

Empirical result:

5 is the dominant terminal attractor for N = 1000

Structural interpretation:

T compresses many low-complexity multiplicative structures through numerical channels such as:

8 → 6 → 5  
9 → 6 → 5

---

## 11. Status

This model is preliminary.

It provides:

- structural states  
- structural trajectories  
- structural delta  
- compression interpretation  
- coherence measure  

It does not yet provide:

- formal convergence proofs  
- asymptotic basin estimates  
- uniqueness of dominant attractors  
- full classification of transformations