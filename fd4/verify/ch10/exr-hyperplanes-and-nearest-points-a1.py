"""A1 and A2: hyperplane 2x1 - x2 + 2x3 = 6."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from _hyperplanes_rn import Fr, vec, dot, sub, mul, nsq

QUOTED = {"norm_a_sq": 9, "dist": 2, "nearest": (Fr(4, 3), Fr(-2, 3), Fr(4, 3)),
          "a2_values": (0, 8), "t1": Fr(3, 4), "cross": (Fr(9, 4), 0, Fr(3, 4))}
a, c = vec(2, -1, 2), Fr(6)
assert nsq(a) == QUOTED["norm_a_sq"]
assert abs(dot(a, vec(0, 0, 0)) - c) / 3 == QUOTED["dist"]
xs = sub(vec(0, 0, 0), mul((0 - c) / nsq(a), a))
assert xs == QUOTED["nearest"] and dot(a, xs) == c and nsq(xs) == 4
q = vec(3, 0, 1)
assert (dot(a, vec(0, 0, 0)), dot(a, q)) == QUOTED["a2_values"]
t1 = (c - 0) / (dot(a, q) - 0)
assert t1 == QUOTED["t1"]
pt = mul(t1, q)
assert pt == QUOTED["cross"] and dot(a, pt) == c
print("ok")
