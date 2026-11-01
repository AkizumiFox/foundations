"""exr-binomial-theorem-a1 (c): the step n = 1 -> 2 of the binomial proof, monomials x^i y^j as
pairs (i, j) with natural coefficients: u = (0, xy, x^2), w = (y^2, xy, 0), sum y^2 + 2xy + x^2.
(b): for non-commuting 2x2 matrices, (x+y)^2 != x^2 + 2xy + y^2."""
from math import comb
QUOTED = {"u": [{}, {(1, 1): 1}, {(2, 0): 1}], "w": [{(0, 2): 1}, {(1, 1): 1}, {}],
          "sum": {(0, 2): 1, (1, 1): 2, (2, 0): 1}}
n = 1
z = [(k, n + 1 - k) for k in range(n + 2)]
u = [{}] + [{z[k]: comb(n, k - 1)} for k in range(1, n + 2)]
w = [({z[k]: comb(n, k)} if comb(n, k) else {}) for k in range(n + 2)]
assert u == QUOTED["u"] and w == QUOTED["w"]
tot = {}
for d in u + w:
    for m, c in d.items():
        tot[m] = tot.get(m, 0) + c
assert tot == QUOTED["sum"]


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def ad(*ms):
    return [[sum(m[i][j] for m in ms) for j in range(2)] for i in range(2)]


X = [[0, 1], [0, 0]]
Y = [[0, 0], [1, 0]]
S = ad(X, Y)
assert mm(S, S) == ad(mm(X, X), mm(X, Y), mm(Y, X), mm(Y, Y))
assert mm(S, S) != ad(mm(X, X), mm(X, Y), mm(X, Y), mm(Y, Y))
print("ok")
