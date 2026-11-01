"""B4: (c) witness (0, y) equidistant from (+-1, 0); (e) a = (2,0), c = 2 gives distance 1."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from _hyperplanes_rn import Fr, vec, dot, sub, mul, nsq

QUOTED = {"e_dist": 1}
p, q = vec(-1, 0), vec(1, 0)
for y in range(-10, 11):
    x = vec(0, y)
    assert nsq(sub(x, p)) == nsq(sub(x, q))
assert sub(q, p) == (2, 0) and (nsq(q) - nsq(p)) / 2 == 0
a, c = vec(2, 0), Fr(2)
# distance = |<a,0> - c| / ||a||, ||a|| = 2
assert abs(0 - c) / 2 == QUOTED["e_dist"] != abs(c)
print("ok")
