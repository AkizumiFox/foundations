"""exr-unique-factorization-a1 (b): the step run on (2, 2, 3, 5)."""
QUOTED = {"p": (2, 2, 3, 5), "cancelled": 12, "short": (2, 2, 3)}
from math import prod
assert prod(QUOTED["p"]) == 60
assert 60 // 5 == QUOTED["cancelled"] == prod(QUOTED["short"])
# any q_l dividing 60 that is prime lies in {2, 3, 5}
assert [d for d in range(2, 61) if 60 % d == 0 and all(d % e for e in range(2, d))] == [2, 3, 5]
print("exr-unique-factorization-a1: ok")
