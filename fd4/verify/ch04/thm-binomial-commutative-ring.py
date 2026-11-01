"""thm-binomial-commutative-ring: (x + y)^n = sum C(n, k).(x^k y^(n-k)) for n <= 8 in Z/7Z and
Z/12Z on all pairs, the multiple C.z computed as repeated addition."""
from math import comb
QUOTED = {"n_max": 8, "moduli": (7, 12)}


def mult(n, a, mod):
    s = 0
    for _ in range(n):
        s = (s + a) % mod
    return s


for mod in QUOTED["moduli"]:
    for n in range(QUOTED["n_max"] + 1):
        for x in range(mod):
            for y in range(mod):
                lhs = pow(x + y, n, mod)
                rhs = 0
                for k in range(n + 1):
                    rhs = (rhs + mult(comb(n, k), (pow(x, k, mod) * pow(y, n - k, mod)) % mod, mod)) % mod
                assert lhs == rhs
print("ok")
