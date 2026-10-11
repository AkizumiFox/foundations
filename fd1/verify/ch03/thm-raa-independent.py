"""thm-raa-independent (Section 3.5, optional): exhaustive check, over all values in
{0, 1/2, 1}, that every primitive rule except RAA preserves the three-valued relation
(m = the least value of the context), in exactly the form the proof uses; that RAA fails
(m = 1, u(phi) = 1/2); the values quoted at u(p) = 1/2 and for Peirce at (1/2, 0); and
that De Morgan (d) and (p -> q) or (q -> p) are NOT refuted by these values."""
import itertools
import sys
from fractions import Fraction
sys.path.insert(0, "verify/ch03")
import _logic as L

H = Fraction(1, 2)
QUOTED = {"u(p)": Fraction(1, 2), "value of not not p": 1, "value of p or not p": Fraction(1, 2), "Peirce value": Fraction(1, 2)}
V = L.THREE
imp, neg = L.imp3, (lambda a: L.imp3(a, Fraction(0)))
iff = lambda a, b: min(imp(a, b), imp(b, a))
for m, x, y, z in itertools.product(V, repeat=4):
    # premises and assumptions, R: phi in Gamma_k gives m <= u(phi); here trivial
    # and-I, and-E, or-I
    if m <= x and m <= y:
        assert m <= min(x, y)
    if m <= min(x, y):
        assert m <= x and m <= y
    if m <= x:
        assert m <= max(x, y) and m <= max(y, x)
    # ->E and <->E (both forms)
    if m <= imp(x, y) and m <= x:
        assert m <= y
    if m <= iff(x, y) and m <= x:
        assert m <= y
    if m <= iff(x, y) and m <= y:
        assert m <= x
    # not-E and bot-E
    if m <= x and m <= neg(x):
        assert m <= 0
    if m <= 0:
        assert m <= z
    # ->I, not-I, <->I
    if min(m, x) <= y:
        assert m <= imp(x, y)
    if min(m, x) <= 0:
        assert m <= neg(x)
    if min(m, x) <= y and min(m, y) <= x:
        assert m <= iff(x, y)
    # or-E
    if m <= max(x, y) and min(m, x) <= z and min(m, y) <= z:
        assert m <= z
# RAA fails
m, x = Fraction(1), H
assert min(m, neg(x)) <= 0 and not m <= x
# the refutations
u = {"p": QUOTED["u(p)"], "q": Fraction(0)}
assert L.val3(L.parse(r"\neg p"), u) == 0
assert L.val3(L.parse(r"\neg\neg p"), u) == QUOTED["value of not not p"]
assert L.val3(L.parse(r"p \vee \neg p"), u) == QUOTED["value of p or not p"]
assert L.val3(L.parse(r"\neg\neg p \to p"), u) == H
assert L.val3(L.parse(r"p \to q"), u) == 0
assert L.val3(L.parse(r"(p \to q) \to p"), u) == 1
assert L.val3(L.parse(r"((p \to q) \to p) \to p"), u) == QUOTED["Peirce value"]
# not refuted: De Morgan (d) and prelinearity
for a, b in itertools.product(V, repeat=2):
    w = {"p": a, "q": b}
    assert L.val3(L.parse(r"\neg(p \wedge q)"), w) <= L.val3(L.parse(r"\neg p \vee \neg q"), w)
    assert L.val3(L.parse(r"(p \to q) \vee (q \to p)"), w) == 1
# on {0, 1} the three-valued clauses are the two-valued tables
for a, b in itertools.product((Fraction(0), Fraction(1)), repeat=2):
    A, B = a == 1, b == 1
    assert (min(a, b) == 1) == (A and B) and (max(a, b) == 1) == (A or B)
    assert (imp(a, b) == 1) == ((not A) or B) and (iff(a, b) == 1) == (A == B) and (neg(a) == 1) == (not A)
print("thm-raa-independent: all quoted values check")
