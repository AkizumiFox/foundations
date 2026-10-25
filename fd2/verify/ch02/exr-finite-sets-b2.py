"""exr-finite-sets-b2: (a) 6 integers, two equal remainders mod 5; (b) every 7-subset of the
3 x 3 grid {1,2,3}^2 has three points in one row (same first coordinate); a row count of at most
2 each gives at most 6 points; six points, two per row, have no row of three."""
from itertools import combinations, product
QUOTED = {"a_size": 6, "mod": 5, "b_size": 7, "row_cap": 2, "rows": 3, "six": 6}
for s in combinations(range(-6, 9), QUOTED["a_size"]):
    assert len({x % QUOTED["mod"] for x in s}) < len(s)
grid = list(product((1, 2, 3), repeat=2))
for s in combinations(grid, QUOTED["b_size"]):
    counts = [sum(1 for (x, _) in s if x == i) for i in (1, 2, 3)]
    assert sum(counts) == len(s)
    assert max(counts) >= 3
assert QUOTED["rows"] * QUOTED["row_cap"] == QUOTED["six"] < QUOTED["b_size"]
six = [(i, j) for i in (1, 2, 3) for j in (1, 2)]
assert len(six) == 6 and all(sum(1 for (x, _) in six if x == i) == 2 for i in (1, 2, 3))
print("ok")
