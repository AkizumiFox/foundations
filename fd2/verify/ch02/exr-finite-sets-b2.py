"""exr-finite-sets-b2: (a) 6 integers, two equal remainders mod 5; (b) 5 of {1..8}, two sum to 9;
{1,2,3,4} shows 5 is least; largest sum there is 7."""
from itertools import combinations
QUOTED = {"a_size": 6, "mod": 5, "b_size": 5, "witness": (1, 2, 3, 4), "max_sum": 7}
for s in combinations(range(-6, 9), QUOTED["a_size"]):
    assert len({x % QUOTED["mod"] for x in s}) < len(s)
for s in combinations(range(1, 9), QUOTED["b_size"]):
    assert any(x + y == 9 for x, y in combinations(s, 2))
    assert all(1 <= min(x, 9 - x) <= 4 for x in s)
w = QUOTED["witness"]
assert all(x + y != 9 for x, y in combinations(w, 2))
assert max(x + y for x, y in combinations(w, 2)) == QUOTED["max_sum"]
print("ok")
