"""exm-binomial-expansions: (a+b)^4 coefficients; (x-1)^5 = x^5 - 5x^4 + 10x^3 - 10x^2 + 5x - 1;
11^4 = 10000 + 4000 + 600 + 40 + 1 = 14641. Polynomials as coefficient lists (index = power of x)."""
from math import comb
QUOTED = {"a": [1, 4, 6, 4, 1], "b": [-1, 5, -10, 10, -5, 1], "c_terms": [10000, 4000, 600, 40, 1], "c": 14641}


def polypow(p, n):
    r = [1]
    for _ in range(n):
        q = [0] * (len(r) + len(p) - 1)
        for i, u in enumerate(r):
            for j, v in enumerate(p):
                q[i + j] += u * v
        r = q
    return r


# (a + b)^4 in the variable a with b = 1 gives the coefficients of a^k b^(4-k)
assert polypow([1, 1], 4) == QUOTED["a"]
assert polypow([-1, 1], 5) == QUOTED["b"]
for k in range(6):
    assert QUOTED["b"][k] == comb(5, k) * (-1) ** (5 - k)
assert [comb(4, k) * 10 ** k for k in range(4, -1, -1)] == QUOTED["c_terms"]
assert sum(QUOTED["c_terms"]) == 11 ** 4 == QUOTED["c"]
print("ok")
