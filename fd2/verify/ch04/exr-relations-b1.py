"""exr-relations-b1: sample checks of the five relations."""
from itertools import product
from fractions import Fraction as Fr

QUOTED = {}


def props(X, rel):
    X = list(X)
    return (all(rel(x, x) for x in X),
            all(rel(y, x) for x, y in product(X, X) if rel(x, y)),
            all(x == y for x, y in product(X, X) if rel(x, y) and rel(y, x)),
            all(rel(x, z) for x, y, z in product(X, X, X) if rel(x, y) and rel(y, z)))


NN = list(product(range(5), range(5)))
assert props(NN, lambda u, v: u[0] + v[1] == u[1] + v[0]) == (True, True, False, True)
reals = [Fr(n, 2) for n in range(-6, 7)]
assert props(reals, lambda x, y: x * x == y * y) == (True, True, False, True)
# functions on a finite sample of points, values in a small set (pointwise order)
pts = [-1, 0, 1]
funcs = list(product([-1, 0, 1], repeat=len(pts)))
assert props(funcs, lambda f, g: all(a <= b for a, b in zip(f, g))) == (True, False, True, True)
f, zero = (-1, 0, 1), (0, 0, 0)  # f(x) = x and the constant 0
assert not all(a <= b for a, b in zip(f, zero)) and not all(a <= b for a, b in zip(zero, f))
assert props(reals, lambda x, y: x * y > 0) == (False, True, False, True)
nonzero = [x for x in reals if x != 0]
assert props(nonzero, lambda x, y: x * y > 0) == (True, True, False, True)
assert props(range(-10, 11), lambda x, y: y == x + 1) == (False, False, True, False)
print("ok")
