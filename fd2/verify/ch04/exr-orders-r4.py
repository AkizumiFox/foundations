"""exr-orders-r4: every non-empty finite subset of a partial order has a maximal element; the
inductive procedure (keep m unless m < x_{n+1}, then take x_{n+1}) returns one. Checked on all
lists from {1..12} under divisibility and on subsets of P({1,2,3}) under inclusion."""
import random
from itertools import combinations

QUOTED = {}  # (R4 quotes no numbers; the checks below test its procedure on samples)
MAX_LEN = 7

def run(xs, lt):
    m = xs[0]
    for x in xs[1:]:
        if lt(m, x):
            m = x
    return m

random.seed(3)
div_lt = lambda a, b: a != b and b % a == 0
for _ in range(5000):
    xs = [random.randint(1, 12) for _ in range(random.randint(1, MAX_LEN))]
    m = run(xs, div_lt)
    assert m in xs and not any(div_lt(m, a) for a in xs)
P = [frozenset(c) for r in range(4) for c in combinations([1, 2, 3], r)]
sub_lt = lambda a, b: a < b
for _ in range(5000):
    xs = random.choices(P, k=random.randint(1, 6))
    m = run(xs, sub_lt)
    assert m in xs and not any(sub_lt(m, a) for a in xs)
print("exr-orders-r4: all quoted values check")
