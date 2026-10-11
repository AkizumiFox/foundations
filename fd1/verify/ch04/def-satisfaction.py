"""def-satisfaction and the text around it (Section 4.11): term values in the arithmetic
structure on R; the trace of forall x exists y (x < y) in N and in {1, 2, 3}; forall y (x <= y)
in N under l(x) = 0 and l(x) = 1; the one-element structure; the Quick check on
forall x exists y (y * y = x) in R, [0, oo), C."""
import cmath
import itertools
import sys
sys.path.insert(0, "verify/ch04")
from _fo_models import structure, sat, P, ALL, EX, NOT

QUOTED = {"x*x + y at x = 2, y = -3": 1, "at y = 1": 5, "at x = 0": -3, "1 + 1": 2,
          "failing element in {1,2,3}": 3}


def term(x, y):
    return x * x + y


assert term(2, -3) == QUOTED["x*x + y at x = 2, y = -3"]
assert term(2, 1) == QUOTED["at y = 1"]
assert term(0, -3) == QUOTED["at x = 0"]
assert 1 + 1 == QUOTED["1 + 1"]

lt = lambda D: {(a, b) for a in D for b in D if a < b}
le = lambda D: {(a, b) for a in D for b in D if a <= b}
phi = ALL("x", EX("y", P("<", "x", "y")))

# {1, 2, 3}: false, and the failing element is 3 (the only d with no witness)
D3 = [1, 2, 3]
M3 = structure(D3, pred={"<": lt(D3)})
assert not sat(phi, M3, {})
fails = [d for d in D3 if not sat(EX("y", P("<", "x", "y")), M3, {"x": d})]
assert fails == [QUOTED["failing element in {1,2,3}"]]

# N: the witness d + 1 is in N and larger, checked for d = 0..10000
assert all(d + 1 >= 0 and d < d + 1 for d in range(0, 10001))

# forall y (x <= y) in N: with l(x) = 0 true (0 <= e for all e >= 0); with l(x) = 1 false at e = 0
assert all(0 <= e for e in range(0, 10001))
assert not (1 <= 0)

# one-element structure: forall and exists agree, x = y always satisfied
for Pset in [set(), {("a",)}]:
    M = structure(["a"], pred={"P": Pset})
    assert sat(ALL("x", P("P", "x")), M, {}) == sat(EX("x", P("P", "x")), M, {})
    assert sat(("eq", "x", "y"), M, {"x": "a", "y": "a"})

# forall x (x = x) always; exists x not(x = x) never (finite samples)
for n in range(1, 5):
    M = structure(range(n))
    assert sat(ALL("x", ("eq", "x", "x")), M, {})
    assert not sat(EX("x", NOT(("eq", "x", "x"))), M, {})

# Quick check: R false at -1; [0, oo) true via sqrt; C true via principal sqrt
assert all(e * e != -1 for e in [x / 7 for x in range(-700, 701)])
for d in [0, 0.25, 2, 9, 1e6]:
    assert abs(d ** 0.5 * d ** 0.5 - d) < 1e-6 * max(1, d)
for z in [complex(a, b) for a, b in itertools.product(range(-3, 4), repeat=2)]:
    w = cmath.sqrt(z)
    assert abs(w * w - z) < 1e-9
print("def-satisfaction: all quoted values check")
