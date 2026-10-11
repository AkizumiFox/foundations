"""def-dedekind-cut, Quick check (c): E = {p : p^3 < 5}. 0 in E, 2 not (8 > 5).
Cubes: p^3 - q^3 = (p - q)(p^2 + pq + q^2). (C3): d = 5 - p^3, h = d/(3p^2 + 3p + 5) in (0, 1),
(p + h)^3 = p^3 + 3p^2 h + 3p h^2 + h^3 < p^3 + h(3p^2 + 3p + 1) < p^3 + d = 5.
Also (a): {p < 0 or p^2 < 4} = D_2 on samples; (b): 1 in, -2 out (4 > 2)."""
from fractions import Fraction as F

QUOTED = {"two_cubed": 8, "minus_two_sq": 4}
assert 2 ** 3 == QUOTED["two_cubed"] > 5
assert (-2) ** 2 == QUOTED["minus_two_sq"] > 2 and 1 < 2

grid = [F(n, 97) for n in range(-400, 400)]
for p in grid:
    for q in grid[::37]:
        assert p ** 3 - q ** 3 == (p - q) * (p * p + p * q + q * q)
    # (a)
    assert (p < 0 or p * p < 4) == (p < 2)

count = 0
for p in [F(n, 1000) for n in range(1, 1710)]:
    if p ** 3 >= 5:
        continue
    count += 1
    d = 5 - p ** 3
    h = d / (3 * p * p + 3 * p + 5)
    assert 0 < d < 5 < 3 * p * p + 3 * p + 5
    assert 0 < h < 1 and h ** 3 < h ** 2 < h
    assert (p + h) ** 3 == p ** 3 + 3 * p * p * h + 3 * p * h * h + h ** 3
    assert (p + h) ** 3 < p ** 3 + h * (3 * p * p + 3 * p + 1) < p ** 3 + d == 5
assert count > 1500
print("ok")
