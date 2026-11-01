"""exr-bounds-and-suprema-a1: x^2 on [-1, 2); part (f) formerly A2 (c)."""
from fractions import Fraction as Fr

QUOTED = {"sup": 4, "inf": 0, "spread": 4}
pts = [Fr(k, 100) for k in range(-100, 200)]   # [-1, 2) sampled
vals = [x * x for x in pts]
assert min(vals) == QUOTED["inf"] and max(vals) < QUOTED["sup"]
assert max(vals) > QUOTED["sup"] - Fr(1, 20)
assert QUOTED["sup"] - QUOTED["inf"] == QUOTED["spread"]
assert max(abs(a - b) for a in vals for b in vals[::7]) < QUOTED["spread"]
assert 2 not in pts and -2 not in pts
# part (f): sup |f| = max(|sup f|, |inf f|) on sample functions (attained cases)
pts = [Fr(k, 50) for k in range(-100, 101)]
funcs = [lambda x: x, lambda x: x - 3, lambda x: x + 5, lambda x: x * x - 1, lambda x: -x * x - 2, lambda x: 3 * x - x**3]
for f in funcs:
    v = [f(x) for x in pts]
    S, I = max(v), min(v)
    assert max(abs(t) for t in v) == max(abs(S), abs(I))
print("ok")
