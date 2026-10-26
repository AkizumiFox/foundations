"""exr-well-defined-operations-b3: (a) [(a+d, b+c)] respects ~ in each argument
(not symmetric); it equals x + (-y). (b) (0,0) ~ (1,1) give (0,0), (1,2): 0+2 != 0+1.
(c) (1,0) ~ (2,1), second argument (0,1): outputs (1,0), (2,0): 1+0 != 0+2.
(d) (a*a + b*b, a*b + b*a) is g_mul(x, x) and respects ~."""
import itertools
QUOTED = {
    "b_outputs": ((0, 0), (1, 2)), "b_cross": (2, 1),
    "c_outputs": ((1, 0), (2, 0)), "c_cross": (1, 2),
}
rel = lambda p, q: p[0] + q[1] == p[1] + q[0]
add = lambda p, q: (p[0] + q[0], p[1] + q[1])
mul = lambda p, q: (p[0] * q[0] + p[1] * q[1], p[0] * q[1] + p[1] * q[0])
neg = lambda p: (p[1], p[0])
ga = lambda p, q: (p[0] + q[1], p[1] + q[0])
gc = lambda p, q: (p[0] * q[1], p[1] * q[0])
gd = lambda p: (p[0] * p[0] + p[1] * p[1], p[0] * p[1] + p[1] * p[0])
P = [(a, b) for a in range(7) for b in range(7)]
# (a) both arguments, independently; not symmetric; equals x + (-y)
for x, x2, y in itertools.product(P, repeat=3):
    if rel(x, x2):
        assert rel(ga(x, y), ga(x2, y))
        assert rel(ga(y, x), ga(y, x2))
assert any(ga(x, y) != ga(y, x) for x, y in itertools.product(P, repeat=2))
for x, y in itertools.product(P, repeat=2):
    assert ga(x, y) == add(x, neg(y))
# (b)
f = lambda p: (p[1], p[0] + p[1])
assert rel((0, 0), (1, 1))
assert (f((0, 0)), f((1, 1))) == QUOTED["b_outputs"]
assert (0 + 2, 0 + 1) == QUOTED["b_cross"] and not rel(*QUOTED["b_outputs"])
# (c)
assert rel((1, 0), (2, 1)) and 1 + 1 == 0 + 2
assert (gc((1, 0), (0, 1)), gc((2, 1), (0, 1))) == QUOTED["c_outputs"]
assert (1 + 0, 0 + 2) == QUOTED["c_cross"] and not rel(*QUOTED["c_outputs"])
# (d)
for x, x2 in itertools.product(P, repeat=2):
    assert gd(x) == mul(x, x)
    if rel(x, x2):
        assert rel(gd(x), gd(x2))
print("exr-well-defined-operations-b3: OK")
