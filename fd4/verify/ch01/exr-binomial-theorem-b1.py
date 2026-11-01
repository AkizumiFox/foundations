"""exr-binomial-theorem-b1: (2x - 1)^5 = sum C(5,k) 2^k (-1)^(5-k) x^k, six terms 32x^5 - 80x^4 + 80x^3 - 40x^2 + 10x - 1, x^3 coefficient 80;
sum C(n,k) 3^k = 4^n (n < 40), check n = 2: 1 + 6 + 9 = 16."""
from math import comb
QUOTED = {"six": (-1, 10, -40, 80, -80, 32), "x3": 80, "n2": (1, 6, 9, 16)}


def polypow(p, n):
    r = [1]
    for _ in range(n):
        q = [0] * (len(r) + len(p) - 1)
        for i, a in enumerate(r):
            for j, b in enumerate(p):
                q[i + j] += a * b
        r = q
    return r


P = polypow([-1, 2], 5)
assert P == [comb(5, k) * 2 ** k * (-1) ** (5 - k) for k in range(6)]
assert tuple(P) == QUOTED["six"]
assert P[3] == QUOTED["x3"] == comb(5, 3) * 8
assert len(P) == 6 and all(P)
for n in range(40):
    assert sum(comb(n, k) * 3 ** k for k in range(n + 1)) == 4 ** n
a, b, c, d = QUOTED["n2"]
assert [comb(2, k) * 3 ** k for k in range(3)] == [a, b, c] and a + b + c == d == 4 ** 2
print("ok")
