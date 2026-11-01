"""prp-staircase-squeeze, exm-strange-staircase, exr-strange-functions-b3: the staircase s(x) = 1/floor(1/x)."""
from fractions import Fraction as Fr
from math import floor

QUOTED = {
    "s(0.4)": Fr(1, 2),
    "s(0.4) - 0.4": Fr(1, 10),
    "2*0.4^2": Fr(32, 100),
}

def s(x: Fr) -> Fr:
    return Fr(0) if x == 0 else Fr(1, floor(1 / x))

x = Fr(2, 5)
assert floor(1 / x) == 2
assert s(x) == QUOTED["s(0.4)"]
assert s(x) - x == QUOTED["s(0.4) - 0.4"]
assert 2 * x * x == QUOTED["2*0.4^2"]
assert 0 <= s(x) - x < 2 * x * x

# step description: s = 1/n on (1/(n+1), 1/n]
for n in range(1, 200):
    for k in range(1, 20):
        y = Fr(1, n + 1) + (Fr(1, n) - Fr(1, n + 1)) * Fr(k, 19)
        assert s(y) == Fr(1, n)
    # the chain 1/(n(n+1)) <= 2/(n+1)^2
    assert Fr(1, n * (n + 1)) <= Fr(2, (n + 1) ** 2)

# squeeze and monotonicity on a grid of rationals in (0,1]
grid = sorted({Fr(p, q) for q in range(1, 120) for p in range(1, q + 1)})
for y in grid:
    assert 0 <= s(y) - y < 2 * y * y
prev = s(Fr(0))
for y in grid:
    assert s(y) >= prev
    prev = s(y)
print("prp-staircase-squeeze: all checks passed")
