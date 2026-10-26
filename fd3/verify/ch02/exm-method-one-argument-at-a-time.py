"""exm-method-one-argument-at-a-time (quick check): (0,0) ~ (1,1) (0+1 = 0+1),
outputs of [(a,b)] -> [(a+a, b)] are (0,0), (2,1), not related: 0+1 != 0+2.
Also the box's example [(a+d, b+c)] is not symmetric in the two pairs."""
import itertools
QUOTED = {"outputs": ((0, 0), (2, 1)), "cross": (1, 2)}
rel = lambda p, q: p[0] + q[1] == p[1] + q[0]
f = lambda p: (p[0] + p[0], p[1])
assert rel((0, 0), (1, 1)) and 0 + 1 == 0 + 1
assert (f((0, 0)), f((1, 1))) == QUOTED["outputs"]
assert (0 + 1, 0 + 2) == QUOTED["cross"] and not rel(*QUOTED["outputs"])
ga = lambda p, q: (p[0] + q[1], p[1] + q[0])
assert ga((1, 0), (0, 0)) != ga((0, 0), (1, 0))
print("exm-method-one-argument-at-a-time: OK")
