"""exr-countable-unions-and-choice-b4: (e) c(n) = phi(min{j : phi(j) in A_n}) lies in A_n and repeats on
families of non-empty subsets of a finite U; the repeated value lies in A_m cap A_n. (c) g(y) = min f^{-1}(y)
is a right inverse for a surjection N -> Y on a finite window. Quick check (3.2): (n + 1)^2 > n."""
import random
random.seed(3)
for _ in range(2000):
    k = random.randint(1, 6)
    U = list(range(k))
    phi = random.sample(U, k)  # bijection {1..k} -> U, phi[j-1]
    L = k + 1 + random.randint(0, 5)  # more indices than elements of U
    fam = [set(random.sample(U, random.randint(1, k))) for _ in range(L)]
    c = [phi[min(j for j in range(k) if phi[j] in A)] for A in fam]
    assert all(c[n] in fam[n] for n in range(L))
    pairs = [(m, n) for m in range(L) for n in range(m + 1, L) if c[m] == c[n]]
    assert pairs
    m, n = pairs[0]
    assert c[m] in fam[m] & fam[n]
for _ in range(500):
    Y = list(range(random.randint(1, 8)))
    f = [random.choice(Y) for _ in range(40)] + Y  # onto Y
    g = {y: min(i for i in range(len(f)) if f[i] == y) for y in Y}
    assert all(f[g[y]] == y for y in Y)
assert all((n + 1) ** 2 > n for n in range(10000))
print("ok")
