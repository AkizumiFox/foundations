"""exm-cancel-parity-map and the Quick check after it (F2.6 §02)."""
QUOTED = {"h(1)": 2, "g(1)": 1}

odd = lambda n: n % 2 == 1
g = lambda n: n
h = lambda n: n + (1 if odd(n) else 0)
R = range(-300, 301)
# (b): agree on all even numbers 2q, differ at 1, differ exactly at the odd numbers
assert all(g(2 * q) == h(2 * q) for q in R)
assert h(1) == QUOTED["h(1)"] and g(1) == QUOTED["g(1)"]
assert all((g(n) != h(n)) == odd(n) for n in R)
# psi(q) = 2q misses 1
assert all(2 * q != 1 for q in R)
# (a): phi(q, r) = 2q + r reaches every integer in the window exactly once
vals = [2 * q + r for q in range(-200, 201) for r in (0, 1)]
assert len(vals) == len(set(vals))
assert set(range(-399, 400)) <= set(vals)
# Quick check: u(t) = 2t + 1 injective on a grid of rationals; squaring not (1, -1)
from fractions import Fraction as F
ts = [F(k, 7) for k in range(-100, 101)]
assert len({2 * t + 1 for t in ts}) == len(ts)
assert 1 ** 2 == (-1) ** 2
print("exm-cancel-parity-map: all quoted values check")
