"""exr-structures-and-satisfaction-b3 (Section 7.1): the failing values of the descriptions that are
not structures, and the repairs."""
import math
from fractions import Fraction as F

# (i) x -> 1/x for x != 0, f(0) = 0: total on Q, values rational
for x in [F(k, 7) for k in range(-50, 51)]:
    v = F(0) if x == 0 else 1 / x
    assert isinstance(v, F)
# (ii) x -> x - 1 on N: f(0) = -1 not in N; repair f(0) := 0 stays in N
assert 0 - 1 == -1 and -1 < 0
assert all((x - 1 if x > 0 else 0) >= 0 for x in range(0, 1000))
# (iv) 1/2 not an integer
assert F(1, 2).denominator != 1
# (v) a set of pairs is fine; (vi) sqrt(-1) is not real; repairs total
try:
    math.sqrt(-1)
    raise AssertionError("sqrt(-1) should fail over the reals")
except ValueError:
    pass
assert all(math.sqrt(x) >= 0 for x in [k / 4 for k in range(0, 400)])
g = lambda x: math.sqrt(x) if x >= 0 else 0.0
assert all(isinstance(g(x), float) for x in [k / 4 for k in range(-400, 400)])
print("exr-structures-and-satisfaction-b3: all quoted values check")
