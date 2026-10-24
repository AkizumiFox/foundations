"""exr-counting-and-descriptions-b1 (Section 5.8): over N, x*x < 3 iff x in {0, 1}
(checked for 0 <= x <= 100; for x >= 2, x*x >= 4); any three such numbers have two equal."""
import itertools

QUOTED = {"solutions": {0, 1}}

sols = {x for x in range(0, 101) if x * x < 3}
assert sols == QUOTED["solutions"]
assert all(x * x >= 4 for x in range(2, 101))
for u, v, w in itertools.product(sorted(sols), repeat=3):
    assert u == v or u == w or v == w
print("exr-counting-and-descriptions-b1: all quoted values check")
