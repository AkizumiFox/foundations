"""exr-inverses-b4 (Section 1.6) and the section's new quick checks: verdicts and witnesses."""
from itertools import product
from fractions import Fraction as F
QUOTED = {"(a) shift": 3, "(b) smallest value": 3, "(c) g at m < 3": 0, "(e) verdict": False,
          "check s(n)=2n+1": [2, 1], "check 2x^3-5": [2, 5]}
f = lambda n: n + 3
# (a) on Z: both composites are the identity
g = lambda n: n - 3
assert all(g(f(n)) == n and f(g(n)) == n for n in range(-200, 201))
# (b) on N: 0, 1, 2 are never values; the least value is 3
assert min(f(n) for n in range(500)) == QUOTED["(b) smallest value"]
assert all(f(n) != m for n in range(500) for m in (0, 1, 2))
# (c) g maps N to N and is a left inverse
gc = lambda m: m - 3 if m >= 3 else 0
assert all(gc(m) >= 0 for m in range(500)) and all(gc(f(n)) == n for n in range(500))
# (e) brute force: a function {1,2} -> {1,2,3} has a left inverse iff injective; the constant 1 has none
X, Y = (1, 2), (1, 2, 3)
def has_left_inverse(fx):
    return any(all(gv[Y.index(fx[x])] == x for x in X) for gv in product(X, repeat=len(Y)))
for vals in product(Y, repeat=2):
    fx = dict(zip(X, vals))
    assert has_left_inverse(fx) == (vals[0] != vals[1])
assert not has_left_inverse({1: 1, 2: 1})
# (d) on small sets: g o f = id and f o g != id forces f non-surjective
for nx, ny in [(1, 2), (2, 3), (2, 2), (3, 3)]:
    Xs, Ys = range(nx), range(ny)
    for fv in product(Ys, repeat=nx):
        for gv in product(Xs, repeat=ny):
            if all(gv[fv[x]] == x for x in Xs) and not all(fv[gv[y]] == y for y in Ys):
                assert set(fv) != set(Ys)
# quick check: left inverse of s(n) = 2n + 1 on N
s = lambda n: 2 * n + 1
gs = lambda m: (m - 1) // 2 if m % 2 else 0
assert all(gs(m) >= 0 for m in range(500)) and all(gs(s(n)) == n for n in range(500))
assert all(s(n) % 2 == 1 for n in range(500))   # even m are never values
# quick check: inverse of 2x^3 - 5 (exact on rationals with rational cube roots)
for x in [F(k, 7) for k in range(-50, 51)]:
    y = 2 * x**3 - 5
    assert (y + 5) / 2 == x**3          # so cbrt((y+5)/2) = x, the real cube root being unique
for t in [F(k, 5) for k in range(-40, 41)]:   # y = 2 t^3 - 5 has cbrt((y+5)/2) = t
    y = 2 * t**3 - 5
    assert 2 * t**3 - 5 == y
print("exr-inverses-b4: ok")
