"""exm-subsets-of-the-plane: one point in and one out for each set; the x1*x2 >= 0 comparison."""

from fractions import Fraction as Fr

QUOTED = {
    "A": ((5, 0), (0, 5)),
    "Q": ((0, 3), (-1, 2)),
    "Q_lookalike": (-1, -1),
    "D": ((-2, -2), (1, 2)),
    "G": ((3, 9), (9, 3)),
    "E": ((Fr(3, 5), Fr(4, 5)), (1, 1)),
}

conds = {
    "A": lambda x: x[1] == 0,
    "Q": lambda x: x[0] >= 0 and x[1] >= 0,
    "D": lambda x: x[0] == x[1],
    "G": lambda x: x[1] == x[0] ** 2,
    "E": lambda x: x[0] ** 2 + x[1] ** 2 <= 1,
}
for name, (pin, pout) in ((k, v) for k, v in QUOTED.items() if k in conds):
    assert conds[name](pin), name
    assert not conds[name](pout), name

p = QUOTED["Q_lookalike"]
assert p[0] * p[1] == 1 >= 0 and not conds["Q"](p)
assert 9 ** 2 == 81 and 3 != 81
assert Fr(3, 5) ** 2 == Fr(9, 25) and Fr(4, 5) ** 2 == Fr(16, 25) and Fr(9, 25) + Fr(16, 25) == 1
assert 1 + 1 == 2 > 1
# the graph G = {(t, t^2)} equals {x : x2 = x1^2} on a sample
for tt in [Fr(k, 3) for k in range(-9, 10)]:
    assert conds["G"]((tt, tt ** 2))
print("exm-subsets-of-the-plane: OK")
