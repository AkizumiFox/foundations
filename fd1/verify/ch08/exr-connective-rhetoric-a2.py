"""exr-connective-rhetoric-a2 (Ch 8, Section 8.1): (j) x <= -1 gives -x >= 1 and x^2 >= 1;
(k) (2k)^2 = 2(2k^2); (l) a cycle on four conditions needs 4 implications, every ordered pair 12;
the Not-allowed block's x = 1/2 (x^3 < x)."""
from fractions import Fraction as Fr
from itertools import permutations
from itertools import product


def identity(f, nvars):
    """A polynomial identity of low degree, checked on a grid of integer points."""
    return all(f(*v) == 0 for v in product(range(-7, 8), repeat=nvars))

QUOTED = {"cycle_4": 4, "ordered_pairs_4": 12, "biconditionals_4": 6, "x_half_cube": Fr(1, 8)}

# (j)
for x in [Fr(-1), Fr(-3, 2), Fr(-10), Fr(-1001, 1000)]:
    assert -x >= 1 and x * x == (-x) * (-x) >= 1
# (k)
assert identity(lambda k: (2 * k) ** 2 - 2 * (2 * k ** 2), 1)
# (l)
assert len(list(permutations(range(4), 2))) == QUOTED["ordered_pairs_4"]
assert QUOTED["ordered_pairs_4"] // 2 == QUOTED["biconditionals_4"]
cycle = [(0, 1), (1, 2), (2, 3), (3, 0)]
assert len(cycle) == QUOTED["cycle_4"]
# reachability: the cycle makes every condition reach every other
reach = {i: {i} for i in range(4)}
for _ in range(4):
    for a, b in cycle:
        for i in range(4):
            if a in reach[i]:
                reach[i].add(b)
assert all(reach[i] == set(range(4)) for i in range(4))
# the cycle check: (i)=>(ii), (ii)=>(iii), (iii)=>(iv), (iv)=>(ii) leaves (i) unreachable
bad = [(0, 1), (1, 2), (2, 3), (3, 1)]
reach = {i: {i} for i in range(4)}
for _ in range(4):
    for a, b in bad:
        for i in range(4):
            if a in reach[i]:
                reach[i].add(b)
assert 0 not in reach[1] and 0 not in reach[2] and 0 not in reach[3]
# Not allowed: x^3 >= x fails at 1/2
x = Fr(1, 2)
assert x ** 3 == QUOTED["x_half_cube"] and x ** 3 < x
print("exr-connective-rhetoric-a2: all quoted values check")
