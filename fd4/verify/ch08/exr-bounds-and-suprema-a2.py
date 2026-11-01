"""exr-bounds-and-suprema-a2 (c): sup |f| = max(|sup f|, |inf f|) on sample functions (attained cases)."""
from fractions import Fraction as Fr

pts = [Fr(k, 50) for k in range(-100, 101)]
funcs = [lambda x: x, lambda x: x - 3, lambda x: x + 5, lambda x: x * x - 1, lambda x: -x * x - 2, lambda x: 3 * x - x**3]
for f in funcs:
    v = [f(x) for x in pts]
    S, I = max(v), min(v)
    assert max(abs(t) for t in v) == max(abs(S), abs(I))
print("ok")
