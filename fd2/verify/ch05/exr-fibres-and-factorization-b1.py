"""exr-fibres-and-factorization-b1.
(a) fibers of x^2 - 1 over 3, -1, -2: {-2, 2}, {0}, empty.
(b) f: a,c -> 1; b,d -> 3: classes {a,c},{b,d}; image {1,3}.
(c) mod-4 classes: [a]_2 yes, [a]_8 no (0 vs 4), [a^2]_8 yes; (a+4k)^2 - a^2 = 8(ak + 2k^2)."""
from fractions import Fraction
import math

QUOTED = {"a": {3: {-2, 2}, -1: {0}, -2: set()},
          "b_classes": {frozenset("ac"), frozenset("bd")}, "b_image": {1, 3},
          "c": (True, False, True)}

# real solutions of x^2 = y + 1: none if y + 1 < 0, else +-sqrt(y + 1)
for y, fib in QUOTED["a"].items():
    t = y + 1
    sols = set() if t < 0 else {math.isqrt(t), -math.isqrt(t)}
    assert t < 0 or math.isqrt(t) ** 2 == t
    assert sols == fib, (y, sols)

f = {"a": 1, "b": 3, "c": 1, "d": 3}
cl = {frozenset(u for u in f if f[u] == f[v]) for v in f}
assert cl == QUOTED["b_classes"] and set(f.values()) == QUOTED["b_image"]

R = range(-100, 101)
def const(g):
    return all(g(a) == g(b) for a in R for b in R if (a - b) % 4 == 0)
res = (const(lambda a: a % 2), const(lambda a: a % 8), const(lambda a: a * a % 8))
assert res == QUOTED["c"]
assert 0 % 8 != 4 % 8
assert all((a + 4 * k) ** 2 - a**2 == 8 * (a * k + 2 * k**2)
           for a in range(-30, 31) for k in range(-30, 31))  # degree-2 identity, 61x61 points
print("exr-fibres-and-factorization-b1: all quoted values check")
