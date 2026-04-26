# structural_metrics.py

from collections import Counter
from statistics import mean

N = 300
MAX_STEPS = 40

# -----------------------------
# PRIME FACTORIZATION
# -----------------------------
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

# multiset representation as Counter
def S(n):
    return Counter(prime_factors(n))

# -----------------------------
# STRUCTURAL DELTA
# -----------------------------
def delta(A, B):
    keys = set(A.keys()) | set(B.keys())
    return sum(abs(A.get(p, 0) - B.get(p, 0)) for p in keys)

# -----------------------------
# TRANSFORMATION
# -----------------------------
def T(n):
    if n <= 1:
        return n
    return sum(prime_factors(n))

# -----------------------------
# TRAJECTORY + METRICS
# -----------------------------
def trajectory(n):
    seq = [n]
    seen = set()

    for _ in range(MAX_STEPS):
        if n in seen:
            break
        seen.add(n)
        n = T(n)
        seq.append(n)
        if seq[-1] == seq[-2]:
            break

    return seq

def structural_deltas(seq):
    deltas = []
    for i in range(len(seq) - 1):
        A = S(seq[i])
        B = S(seq[i+1])
        deltas.append(delta(A, B))
    return deltas

def coherence(deltas):
    if not deltas:
        return 1.0
    return 1 / (1 + mean(deltas))

# -----------------------------
# RUN
# -----------------------------
print("=" * 80)
print("STRUCTURAL METRICS ANALYSIS")
print("=" * 80)

results = []

for n in range(2, N + 1):
    seq = trajectory(n)
    deltas = structural_deltas(seq)
    C = coherence(deltas)

    results.append((n, C, len(seq), deltas[:5]))

# sort by coherence
results.sort(key=lambda x: x[1], reverse=True)

print("\nTOP COHERENCE (most stable trajectories):")
for n, C, L, d in results[:10]:
    print(f"n={n}, C={C:.4f}, len={L}, deltas={d}")

print("\nLOWEST COHERENCE (most disruptive):")
for n, C, L, d in results[-10:]:
    print(f"n={n}, C={C:.4f}, len={L}, deltas={d}")