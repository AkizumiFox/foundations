"""cor-well-ordering-integers (Ch 7, 01): the paragraph after it replaces the real bound -7/2
by the integer -4 below it; and the shift s -> s - b sends a bounded-below set of integers into N."""
from fractions import Fraction as F
import math, random

QUOTED = {"real_bound": F(-7, 2), "integer_below": -4}
assert math.floor(QUOTED["real_bound"]) == QUOTED["integer_below"]
assert QUOTED["integer_below"] <= QUOTED["real_bound"]
random.seed(1)
for _ in range(500):
    b = random.randint(-30, 30)
    S = {random.randint(b, b + 40) for _ in range(random.randint(1, 8))}
    T = {s - b for s in S}
    assert all(t >= 0 for t in T)
    assert min(T) + b == min(S)
    assert -min({-s for s in S}) == max(S)
print("cor-well-ordering-integers: all quoted values check")
