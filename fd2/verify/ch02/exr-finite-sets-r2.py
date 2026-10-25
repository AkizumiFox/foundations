"""exr-finite-sets-r2 (F2.2 §05): (S1) exists x forall y R(x, y), (S2) forall y exists x R(x, y)
for R = divides on {1..6} (both true) and {2..6} (S1 false, S2 true); (S1) => (S2) on all
relations on a 3-element set; x + y = 0 on Z: (S2) by x = -y, (S1) fails by y = 1 - x."""
QUOTED = {"first_set_top": 6, "second_set_bottom": 2, "witness_y_for_x2": 3}
from itertools import product
def S1(X, R): return any(all(R(x, y) for y in X) for x in X)
def S2(X, R): return all(any(R(x, y) for x in X) for y in X)
div = lambda x, y: y % x == 0
assert S1(range(1, 7), div) and S2(range(1, 7), div)
assert not S1(range(2, 7), div) and S2(range(2, 7), div)
assert all(not div(2, 3) and all(not div(x, 2) for x in range(3, 7)) for _ in [0])
X = range(3)
for bits in product([False, True], repeat=9):
    R = lambda x, y, b=bits: b[3 * x + y]
    assert (not S1(X, R)) or S2(X, R)
opp = lambda x, y: x + y == 0
Z = range(-100, 101)
assert all(opp(-y, y) for y in Z)
assert all(not opp(x, 1 - x) and x + (1 - x) == 1 for x in Z)
print("exr-finite-sets-r2: all quoted values check")
