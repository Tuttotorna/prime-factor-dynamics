# prime-factor-dynamics — basin computation

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

print("Attraction basins:")
for k, v in basins.most_common():
    print(f"{k}: {v}")