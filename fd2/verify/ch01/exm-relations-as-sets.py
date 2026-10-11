"""exm-relations-as-sets and the quick check after it (Ch 6 Section 6.3)."""
from fractions import Fraction as F

QUOTED = {
    "elements of L": 3,
    "size of D": 14,
    "row sizes": (6, 3, 2, 1, 1, 1),
}

U = [1, 2, 3]
L = {(a, b) for a in U for b in U if a < b}
assert L == {(1, 2), (1, 3), (2, 3)} and len(L) == QUOTED["elements of L"]
assert len(U) ** 2 == 9  # the size of {1,2,3}^2; the text does not print it
assert {a for a, _ in L} == {1, 2} and {b for _, b in L} == {2, 3}
assert {(b, a) for a, b in L} == {(2, 1), (3, 1), (3, 2)} == {(a, b) for a in U for b in U if a > b}

V = range(1, 7)
D = {(a, b) for a in V for b in V if b % a == 0}
rows = tuple(sum(1 for b in V if b % a == 0) for a in V)
assert rows == QUOTED["row sizes"] and len(D) == QUOTED["size of D"] == sum(rows)
assert {a for a, _ in D} == set(V) == {b for _, b in D}

# circle: points with x in [-1, 1] have y = sqrt(1 - x^2); x = 2 gives y^2 = -3
assert 1 - 2 ** 2 == -3
for x in [F(k, 10) for k in range(-10, 11)]:
    assert 1 - x * x >= 0
for x in [F(k, 10) for k in list(range(-30, -10)) + list(range(11, 30))]:
    assert 1 - x * x < 0
print("exm-relations-as-sets: all quoted values check")
