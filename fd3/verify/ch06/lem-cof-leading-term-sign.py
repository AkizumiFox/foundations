"""lem-cof-leading-term-sign: T = 1 + sum_{i<d} |a_i|/|a_d|; for t > T, p(t) != 0 with the sign of a_d.
Quick check: p(t) = t^2 - 100t, list (0, -100, 1): T = 101, p(102) = 204 > 0, and p(t) > 0 for t > 100.
The lemma itself is tested on random integer lists at many t > T (exact arithmetic)."""
from fractions import Fraction as F
import random
QUOTED = {"T": F(101), "p(102)": F(204)}
def ev(a, t):
    return sum(c * t ** i for i, c in enumerate(a))
def thr(a):
    d = len(a) - 1
    return 1 + sum(F(abs(c), abs(a[d])) for c in a[:d])
a = [0, -100, 1]
assert thr(a) == QUOTED["T"]
assert ev(a, 102) == QUOTED["p(102)"]
for t in [F(100) + F(1, k) for k in range(1, 50)] + [F(101), F(150)]:
    assert ev(a, t) > 0
random.seed(1)
for _ in range(3000):
    d = random.randint(0, 6)
    a = [random.randint(-50, 50) for _ in range(d)] + [random.choice([i for i in range(-9, 10) if i])]
    T = thr(a)
    for k in range(1, 8):
        t = T + F(1, k * k)
        v = ev(a, t)
        assert v != 0 and (v > 0) == (a[-1] > 0)
print("ok")
