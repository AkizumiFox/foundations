"""B1: nearest point of (1,0,0) + R(1,1,1) to (0,3,0)."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from _hyperplanes_rn import Fr, vec, dot, sub, mul, nsq, add

QUOTED = {"t0": Fr(2, 3), "m": (Fr(5, 3), Fr(2, 3), Fr(2, 3)), "dist_sq": Fr(26, 3)}
p, v, x = vec(1, 0, 0), vec(1, 1, 1), vec(0, 3, 0)
t0 = dot(sub(x, p), v) / nsq(v)
assert t0 == QUOTED["t0"]
m = add(p, mul(t0, v))
assert m == QUOTED["m"]
assert dot(sub(x, m), v) == 0
assert nsq(sub(x, m)) == QUOTED["dist_sq"] == Fr(25 + 49 + 4, 9)
# brute check: no rational t on a grid beats it
for k in range(-300, 301):
    t = Fr(k, 50)
    assert nsq(sub(x, add(p, mul(t, v)))) >= QUOTED["dist_sq"]
print("ok")
