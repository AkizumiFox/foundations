"""exr-theories-and-models-b2 (Section 7.4): each sentence true in the first structure and
false in the second (windows of Z, N, Q for (a), (b))."""
import sys
from fractions import Fraction as F
sys.path.insert(0, "verify/ch07")
from _fo_models import structure, sat, P, ALL, EX, AND, NOT

# (a) every element has an additive inverse
assert all(-x in range(-20, 21) for x in range(-20, 21))
assert not any(1 + y == 0 for y in range(0, 100))
# (b) every nonzero element has a reciprocal
Q = [F(p, q) for p in range(-7, 8) for q in range(1, 6)]
assert all(x == 0 or (1 / x) * x == 1 for x in Q)
assert not any(2 * y == 1 for y in range(-100, 101))
# (c), (d)
R = lambda s, t: P("R", s, t)
path = EX("x", EX("y", EX("z", AND(R("x", "y"), R("y", "z")))))
fork = EX("x", EX("y", EX("z", AND(AND(R("x", "y"), R("x", "z")), NOT(("eq", "y", "z"))))))
M1 = structure("abc", pred={"R": {("a", "b"), ("b", "c")}})
M2 = structure("abc", pred={"R": {("a", "b"), ("a", "c")}})
assert sat(path, M1, {}) and not sat(path, M2, {})
assert sat(fork, M2, {}) and not sat(fork, M1, {})
print("exr-theories-and-models-b2: all quoted values check")
