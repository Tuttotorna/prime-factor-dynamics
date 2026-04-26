# Structural Metrics Results

This file records the first structural-metric analysis for Prime-Factor Dynamics.

Parameters:

```text
N = 300
MAX_STEPS = 40

Structural state:

S(n) = multiset of prime factors of n

Structural delta:

Δ(A, B) = sum over all primes p of |a_p - b_p|

Coherence:

C = 1 / (1 + mean(Δ_i))


---

Top Coherence

The highest-coherence trajectories are fixed points.

n=2,  C=1.0000, trajectory=[2, 2]
n=3,  C=1.0000, trajectory=[3, 3]
n=4,  C=1.0000, trajectory=[4, 4]
n=5,  C=1.0000, trajectory=[5, 5]
n=7,  C=1.0000, trajectory=[7, 7]
n=11, C=1.0000, trajectory=[11, 11]
n=13, C=1.0000, trajectory=[13, 13]
n=17, C=1.0000, trajectory=[17, 17]
n=19, C=1.0000, trajectory=[19, 19]
n=23, C=1.0000, trajectory=[23, 23]

Note: 4 is also fixed because:

4 = 2 × 2
T(4) = 2 + 2 = 4


---

Lowest Coherence

These trajectories show the strongest structural disruption.

n=215, C=0.1875, attractor=11, deltas=[7, 6, 0], trajectory=[215, 48, 11, 11]
n=287, C=0.1875, attractor=11, deltas=[7, 6, 0], trajectory=[287, 48, 11, 11]
n=183, C=0.1905, attractor=7,  deltas=[8, 5, 4, 0], trajectory=[183, 64, 12, 7, 7]
n=295, C=0.1905, attractor=7,  deltas=[8, 5, 4, 0], trajectory=[295, 64, 12, 7, 7]
n=87,  C=0.2105, attractor=7,  deltas=[7, 5, 3, 0], trajectory=[87, 32, 10, 7, 7]
n=158, C=0.2105, attractor=7,  deltas=[6, 5, 4, 0], trajectory=[158, 81, 12, 7, 7]
n=218, C=0.2105, attractor=11, deltas=[4, 6, 5, 0], trajectory=[218, 111, 40, 11, 11]
n=232, C=0.2105, attractor=7,  deltas=[6, 5, 4, 0], trajectory=[232, 35, 12, 7, 7]
n=247, C=0.2105, attractor=7,  deltas=[7, 5, 3, 0], trajectory=[247, 32, 10, 7, 7]
n=111, C=0.2143, attractor=11, deltas=[6, 5, 0], trajectory=[111, 40, 11, 11]


---

Interpretation

The top-coherence set is dominated by fixed points.

The lowest-coherence trajectories are not random: they pass through large structural changes before reaching a stable attractor.

Examples:

215 → 48 → 11
287 → 48 → 11
183 → 64 → 12 → 7
295 → 64 → 12 → 7

This shows that the transformation does not merely assign final attractors.

It induces measurable structural disruption along the path.


---

Preliminary Observation

The first structural metric separates two regimes:

high coherence  → fixed or near-fixed structural behavior
low coherence   → abrupt compression before attraction

This supports the interpretation of T as a structural compression operator on multiplicative structure.

