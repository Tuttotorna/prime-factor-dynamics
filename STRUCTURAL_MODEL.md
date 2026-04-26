# Structural Model

This document defines the structural layer used in Prime-Factor Dynamics.

The goal is to move from descriptive iteration to measurable structural change.

---

## 1. Structural State

For every integer `n >= 2`, define its structural state as the multiset of prime factors:

```text
S(n) = PF(n)

Example:

12 = 2 × 2 × 3

S(12) = {2, 2, 3}

Equivalently, using exponent form:

n = p1^a1 × p2^a2 × ... × pk^ak

we define:

S(n) = {(p1, a1), (p2, a2), ..., (pk, ak)}


---

2. Transformation

The main transformation is:

T(n) = sum of prime factors of n, counted with multiplicity

Example:

20 = 2 × 2 × 5

T(20) = 2 + 2 + 5 = 9

This maps multiplicative structure into additive structure.


---

3. Trajectory

A trajectory is the sequence:

n0 → n1 → n2 → ...

where:

n_{i+1} = T(n_i)

Each step also produces a structural trajectory:

S(n0) → S(n1) → S(n2) → ...


---

4. Structural Delta

Define the structural delta between two consecutive states as a distance between their prime-factor structures:

Δ_i = Δ(S(n_i), S(n_{i+1}))

A simple first version is the multiset symmetric difference:

Δ(A, B) = |A △ B|

where repeated prime factors are counted with multiplicity.

Example:

S(20) = {2, 2, 5}
S(9)  = {3, 3}

Δ(S(20), S(9)) = 5

because the two multisets share no common elements.


---

5. Structural Compression

The map T acts as a compression operator on multiplicative structure.

It transforms:

multiplicative decomposition
→ additive collapse

This often reduces structural complexity and pushes trajectories toward prime fixed points.

Primes are fixed points because:

T(p) = p


---

6. Attractors

An attractor is a value reached by iteration.

In the main factor-sum dynamics, terminal attractors are usually primes.

Example:

20 → 9 → 6 → 5

The corresponding structural trajectory is:

{2,2,5} → {3,3} → {2,3} → {5}


---

7. Basin

The basin of an attractor a is:

B(a) = { n | T^k(n) = a for some k >= 0 }

For example, numbers such as:

8, 9, 14, 15, 16, 18, 20, 24

belong to the basin of 5.


---

8. Structural Coherence

For a trajectory of length L, define a simple coherence score:

C = 1 / (1 + mean(Δ_i))

where:

Δ_i = Δ(S(n_i), S(n_{i+1}))

Higher C means the trajectory changes structure more smoothly.

Lower C means stronger structural disruption.


---

9. Saturation

A trajectory is saturated when it reaches a fixed point or cycle.

For the main transformation, prime fixed points satisfy:

T(p) = p

At saturation:

Δ_i = 0

or the structural pattern repeats.


---

10. Interpretation

The observed basin hierarchy is not only a property of individual numbers.

It emerges from the transformation:

transformation → structural trajectory → attractor → basin hierarchy

The main empirical result:

5 is the dominant terminal attractor for N = 1000

can be structurally interpreted as:

T compresses many low-complexity multiplicative structures
through the channel {8, 9} → 6 → 5.


---

11. Status

This model is preliminary.

It provides:

structural states

structural trajectories

structural delta

compression interpretation

coherence measure


It does not yet provide:

formal convergence proof

asymptotic basin estimates

uniqueness of the dominant attractor

complete classification of transformations


