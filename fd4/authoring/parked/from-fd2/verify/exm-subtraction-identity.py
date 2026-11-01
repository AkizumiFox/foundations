"""exm-subtraction-identity and the quick checks after it; hook values of the section."""
from fractions import Fraction as F
from itertools import product

QUOTED = {"(2-3)-4": -5, "2-(3-4)": 3, "2^(3^2)": 512, "(2^3)^2": 64,
          "avg_left": 2, "avg_right": 1}
assert (2 - 3) - 4 == QUOTED["(2-3)-4"] and 2 - (3 - 4) == QUOTED["2-(3-4)"]
assert 2 ** (3 ** 2) == QUOTED["2^(3^2)"] and (2 ** 3) ** 2 == QUOTED["(2^3)^2"]
assert 0 - 1 == -1 != 1
# left identity: e - 0 = 0 -> e = 0; e - 1 = 1 -> e = 2
assert [e for e in range(-10, 11) if e - 0 == 0] == [0]
assert [e for e in range(-10, 11) if e - 1 == 1] == [2]
avg = lambda x, y: F(x + y, 2)
assert avg(avg(0, 0), 4) == QUOTED["avg_left"] and avg(0, avg(0, 4)) == QUOTED["avg_right"]
# max: associative and commutative on a sample; identity 0 on N; none on Z
R = range(-6, 7)
assert all(max(max(x, y), z) == max(x, max(y, z)) for x, y, z in product(R, repeat=3))
assert all(max(0, x) == x for x in range(0, 20))
assert all(max(e, e - 1) == e != e - 1 for e in R)
print("exm-subtraction-identity: all quoted values check")
