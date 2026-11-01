"""lem-difference-of-powers: z^n - w^n = (z - w) sum_{k<n} z^k w^{n-1-k}, termwise (z - w) z^k w^{n-1-k} = b_{k+1} - b_k with b_k = z^k w^{n-k}, on random integers (a commutative ring) and in Z/6, including n = 1."""
import random
random.seed(6)
for mod in (None, 6):
    for _ in range(1000):
        z, w, n = random.randint(-9, 9), random.randint(-9, 9), random.randint(1, 8)
        r = (lambda x: x % mod) if mod else (lambda x: x)
        b = lambda k: z ** k * w ** (n - k)
        for k in range(n):
            assert r((z - w) * z ** k * w ** (n - 1 - k)) == r(b(k + 1) - b(k))
        assert r(z ** n - w ** n) == r((z - w) * sum(z ** k * w ** (n - 1 - k) for k in range(n)))
print("ok")
