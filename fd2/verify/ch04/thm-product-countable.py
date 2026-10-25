"""thm-product-countable: p(m, n) = 2^m 3^n is injective; 3^k is odd; 2^(m-m') 3^n even for m > m'."""
QUOTED = {}
N = 60
seen = {}
for m in range(N):
    for n in range(N):
        v = 2**m * 3**n
        assert v not in seen
        seen[v] = (m, n)
assert all(3**k % 2 == 1 for k in range(200))
assert all((2**d * 3**n) % 2 == 0 for d in range(1, 40) for n in range(40))
assert all(3**k * 3 == 2 * ((3**k - 1) // 2 * 3 + 1) + 1 for k in range(100))
print("ok")
