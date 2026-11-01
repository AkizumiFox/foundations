"""def-norm-rn and the blocks after it in Section 9.4: ||(3,4)|| = 5; the Quick check ||(1,2,2)|| = 3 and (3/5, 0, 4/5) a unit vector;
(3,4)/5 = (3/5, 4/5); the warning ||(1,1)|| = sqrt 2 != 2; d((1,2),(4,6)) = 5. Roots are identified by uniqueness: s >= 0 and s^2 = t."""
from fractions import Fraction as Fr

def dot(x, y): return sum(Fr(a) * Fr(b) for a, b in zip(x, y))
def is_root(s, t): return s >= 0 and s * s == t

def tup(t): return tuple(Fr(v) for v in t.strip("()").split(", "))
QUOTED = {"norm34": 5, "norm122": 3, "unit": "(3/5, 0, 4/5)", "dir34": "(3/5, 4/5)", "d": 5}
assert is_root(QUOTED["norm34"], dot((3, 4), (3, 4))) and dot((3, 4), (3, 4)) == 25
assert is_root(QUOTED["norm122"], dot((1, 2, 2), (1, 2, 2)))
assert dot(tup(QUOTED["unit"]), tup(QUOTED["unit"])) == 1 and is_root(1, 1)
assert tuple(Fr(c, 5) for c in (3, 4)) == tup(QUOTED["dir34"]) and dot(tup(QUOTED["dir34"]), tup(QUOTED["dir34"])) == 1
assert dot((1, 1), (1, 1)) == 2 and not is_root(2, 2)  # ||(1,1)||^2 = 2, and 2 is not sqrt 2 since 2^2 = 4 != 2
diff = (1 - 4, 2 - 6)
assert diff == (-3, -4) and is_root(QUOTED["d"], dot(diff, diff))
assert is_root(0, 0) and is_root(1, 1) and is_root(7, 49) and is_root(3, 9)
# Pythagoras instance: (3,0) . (0,4) = 0, ||(3,4)||^2 = 25 = 9 + 16
assert dot((3, 0), (0, 4)) == 0 and dot((3, 4), (3, 4)) == 25 == 9 + 16
# parallelogram instance: x = (2,0), y = (1,1); diagonals (3,1), (1,-1)
assert dot((3, 1), (3, 1)) == 10 and dot((1, -1), (1, -1)) == 2 and 10 + 2 == 12 == 2 * dot((2, 0), (2, 0)) + 2 * dot((1, 1), (1, 1))
print("ok")
