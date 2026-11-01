"""B2: R(1,2,2) meets S((3,0,0), 3) at t = 0, 2/3; via prp-line-meets-sphere t0 = 1/3, d^2 = 8."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from _hyperplanes_rn import Fr, vec, dot, sub, mul, nsq

QUOTED = {"ts": (0, Fr(2, 3)), "point": (Fr(2, 3), Fr(4, 3), Fr(4, 3)), "t0": Fr(1, 3),
          "m": (Fr(1, 3), Fr(2, 3), Fr(2, 3)), "d_sq": 8}
v, c, r = vec(1, 2, 2), vec(3, 0, 0), 3
# polynomial 9t^2 - 6t + 9
for t in [Fr(k, 7) for k in range(-30, 30)]:
    assert nsq(sub(mul(t, v), c)) == 9 * t * t - 6 * t + 9
for t in QUOTED["ts"]:
    assert nsq(sub(mul(t, v), c)) == r * r
assert mul(QUOTED["ts"][1], v) == QUOTED["point"]
t0 = dot(c, v) / nsq(v)
assert t0 == QUOTED["t0"] and mul(t0, v) == QUOTED["m"]
d_sq = nsq(sub(c, mul(t0, v)))
assert d_sq == QUOTED["d_sq"]
# sqrt(9 - 8)/||v|| = 1/3
assert (t0 - Fr(1, 3), t0 + Fr(1, 3)) == QUOTED["ts"]
print("ok")
