"""thm-rationals-embed-ordered-field: in F = Q the formula (p.1)(q.1)^{-1} is independent of the fraction,
additive, multiplicative and strictly increasing on samples (iota_Q is the identity)."""
from fractions import Fraction as Fr
import itertools

QUOTED = {"iota_one": 1}

def mult_int(m):
    n = abs(m)
    y = Fr(0)
    for _ in range(n):
        y += 1
    return y if m >= 0 else -y

def iota(p, q):
    return mult_int(p) / mult_int(q)

assert iota(1, 1) == QUOTED["iota_one"]
for m, mp in itertools.product(range(-6, 7), repeat=2):
    assert mult_int(m + mp) == mult_int(m) + mult_int(mp)
    assert mult_int(m * mp) == mult_int(m) * mult_int(mp)
    assert mult_int(-m) == -mult_int(m)
fracs = [(p, q) for p in range(-5, 6) for q in range(1, 5)]
for (p, q), (r, s) in itertools.product(fracs, repeat=2):
    if p * s == r * q:
        assert iota(p, q) == iota(r, s)
    x, y = Fr(p, q), Fr(r, s)
    assert iota(p, q) == x
    assert iota(p * s + r * q, q * s) == iota(p, q) + iota(r, s)
    assert iota(p * r, q * s) == iota(p, q) * iota(r, s)
    if x < y:
        assert iota(p, q) < iota(r, s)
print("ok")
