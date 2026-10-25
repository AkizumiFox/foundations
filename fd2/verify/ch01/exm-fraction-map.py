"""1.5 exm-fraction-map: f(x) = x/(1 + |x|) maps R into (-1, 1), keeps the sign of x, is
injective, and x = y/(1 - |y|) solves f(x) = y with 1 + |x| = 1/(1 - |y|), for both signs of y;
the backwards formulas y/(1 - y) (y >= 0) and y/(1 + y) (y < 0) agree with it.
Also the Quick checks of the section that quote values: n -> 5n - 2 on Z misses 0 and is
injective on a window; the indicator of {1, 4} in {1,...,5} is 10010, the value of 01100 at 2
is 1, and there are 32 strings of length 5 (the five-string game)."""
from fractions import Fraction as F
import itertools

QUOTED = {"qc_witness": 0, "indicator_14": "10010", "value_01100_at_2": 1, "strings": 32}

f = lambda x: x / (1 + abs(x))
xs = [F(k, 7) for k in range(-200, 201)] + [F(10**6), F(-10**6)]
for x in xs:
    assert 1 + abs(x) >= 1 > 0
    assert abs(f(x)) < 1
    assert (f(x) > 0) == (x > 0) and (f(x) < 0) == (x < 0) and (f(x) == 0) == (x == 0)
# injective on the sample (exact arithmetic)
vals = [f(x) for x in xs]
assert len(set(vals)) == len(set(xs))
# the two cases of the injectivity proof: cleared denominators
for x1, x2 in itertools.product([F(k, 5) for k in range(0, 30)], repeat=2):
    assert (x1 * (1 + x2) == x2 * (1 + x1)) == (x1 == x2)
for x1, x2 in itertools.product([F(-k, 5) for k in range(1, 30)], repeat=2):
    assert (x1 * (1 - x2) == x2 * (1 - x1)) == (x1 == x2)
# surjectivity, both signs of y
ys = [F(k, 97) for k in range(-96, 97)]
for y in ys:
    x = y / (1 - abs(y))
    assert 1 + abs(x) == 1 / (1 - abs(y))
    assert f(x) == y
    assert x * (1 - abs(y)) == y
    if y >= 0:
        assert x == y / (1 - y) and x >= 0
    else:
        assert x == y / (1 + y) and x < 0

# Quick check: n -> 5n - 2
g = lambda n: 5 * n - 2
window = range(-1000, 1001)
assert len({g(n) for n in window}) == len(window)
assert all(g(n) != QUOTED["qc_witness"] for n in window)
assert F(2, 5).denominator != 1   # 5n = 2 only at n = 2/5
# Quick check after the game, and the game's count
ind = "".join("1" if k in (1, 4) else "0" for k in range(1, 6))
assert ind == QUOTED["indicator_14"]
assert int("01100"[2 - 1]) == QUOTED["value_01100_at_2"]
assert len(list(itertools.product("01", repeat=5))) == QUOTED["strings"]
assert ind not in ("01001", "10110")   # not the game's diagonal or its flip
lst = ["00000", "11111", "01010", "10101", "00111"]
diag = "".join(lst[k][k] for k in range(5))
assert diag == "01001" and "".join("1" if c == "0" else "0" for c in diag) == "10110"
print("exm-fraction-map: all quoted values check")
