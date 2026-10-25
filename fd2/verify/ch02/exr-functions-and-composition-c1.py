"""exr-functions-and-composition-c1 (Section 2.1): idempotents; |.| idempotent, negation not; three idempotents on {1, 2}; plus the C2 counterexample."""
from itertools import product
from fractions import Fraction as F

QUOTED = {"idempotents on {1,2}": 3, "functions on {1,2}": 4, "C2 composite": "x + 3", "C2 f(0), g(0)": (1, 2)}

X = (1, 2)
funcs = [dict(zip(X, vals)) for vals in product(X, repeat=len(X))]
assert len(funcs) == QUOTED["functions on {1,2}"]
idem = [f for f in funcs if all(f[f[x]] == f[x] for x in X)]
assert len(idem) == QUOTED["idempotents on {1,2}"]
assert {2: 1, 1: 2} not in idem  # the swap
# (a) on all maps of a 3-element set: idempotent => f fixes its range
Y = (0, 1, 2)
for vals in product(Y, repeat=3):
    f = dict(zip(Y, vals))
    if all(f[f[x]] == f[x] for x in Y):
        assert all(f[y] == y for y in set(f.values()))
# (b)
xs = [F(k, 3) for k in range(-30, 31)]
assert all(abs(abs(x)) == abs(x) for x in xs)
m = lambda x: -x
assert m(m(1)) == 1 != m(1)
# C2 counterexample: f(x) = x + 1, g(x) = x + 2 commute and differ at 0
fx = lambda x: x + 1
gx = lambda x: x + 2
assert all(gx(fx(x)) == fx(gx(x)) == x + 3 for x in xs)
assert (fx(0), gx(0)) == QUOTED["C2 f(0), g(0)"]
print("exr-functions-and-composition-c1: ok")
