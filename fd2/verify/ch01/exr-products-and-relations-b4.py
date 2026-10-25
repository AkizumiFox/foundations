"""1.4 B4 (Prove or disprove): (a) (3x - y, x + 2y) = (a, b) has the unique solution
x = (2a + b)/7, y = (3b - a)/7; (b) (1, 0), (-1, 0) both solve (x^2, y) = (1, 0);
(c) {} x {1} = {} x {2} although {1} != {2}; (d) on small finite sets, A x B = A x C with A
nonempty forces B = C; (e) E x E = {} only for E = {}; and the Quick checks after the box:
(x^2, x^3) = (4, -8) only for x = -2, (x^2, x) = (4, 3) never."""
import itertools
from fractions import Fraction as F

QUOTED = {"x": "(2a + b)/7", "y": "(3b - a)/7", "b_witnesses": ((1, 0), (-1, 0)),
          "qc1": -2, "qc2_forced": 3}

# uniqueness: the coefficient matrix [[3, -1], [1, 2]] has determinant 7 != 0, and Cramer's
# rule gives the solution independently of the elimination in the text
det = 3 * 2 - (-1) * 1
assert det == 7
cramer = lambda A_, B_: (F(A_ * 2 - (-1) * B_, det), F(3 * B_ - 1 * A_, det))
# the existence check by exact arithmetic on a grid
for A_, B_ in itertools.product(range(-5, 6), repeat=2):
    X, Y = F(2 * A_ + B_, 7), F(3 * B_ - A_, 7)
    assert (X, Y) == cramer(A_, B_)
    assert (3 * X - Y, X + 2 * Y) == (A_, B_)
    assert 3 * F(2 * A_ + B_, 7) - F(3 * B_ - A_, 7) == F(7 * A_, 7)

# (b)
for (u, v) in QUOTED["b_witnesses"]:
    assert (u * u, v) == (1, 0)
assert QUOTED["b_witnesses"][0] != QUOTED["b_witnesses"][1]

def prod(S, T):
    return {(s, t) for s in S for t in T}

# (c)
assert prod(set(), {1}) == prod(set(), {2}) == set() and {1} != {2}

# (d) and (e): exhaustive over subsets of a 3-element universe
U = [0, 1, 2]
subsets = [set(c) for r in range(4) for c in itertools.combinations(U, r)]
for A_, B_, C_ in itertools.product(subsets, repeat=3):
    if A_ and prod(A_, B_) == prod(A_, C_):
        assert B_ == C_
assert [E for E in subsets if prod(E, E) == set()] == [set()]

# Quick check after exm-method-uniqueness
# x^3 is strictly increasing, so x^3 = -8 has at most one real solution; -2 is one
pts = [F(k, 50) for k in range(-500, 501)]
assert all(u**3 < v**3 for u, v in zip(pts, pts[1:]))
q = QUOTED["qc1"]
assert q**3 == -8 and q**2 == 4
assert [t for t in pts if t**3 == -8] == [q]
assert QUOTED["qc2_forced"] ** 2 == 9 != 4
print("exr-products-and-relations-b4: all quoted values check")
