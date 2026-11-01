"""prp-perpendicular-bisector: identity ||x-p||^2 - ||x-q||^2 = 2<q-p,x> - 2c; Quick check x1 + 2x2 = 5."""
import random
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from _hyperplanes_rn import Fr, vec, dot, sub, mul, nsq, add

QUOTED = {"qc_c": 10, "qc_reduced": (1, 2, 5), "qc_midpoint": (1, 2)}
random.seed(2)
for _ in range(200):
    n = random.randint(1, 4)
    p = vec(*[random.randint(-9, 9) for _ in range(n)])
    q = vec(*[random.randint(-9, 9) for _ in range(n)])
    x = vec(*[Fr(random.randint(-30, 30), random.randint(1, 5)) for _ in range(n)])
    c = (nsq(q) - nsq(p)) / 2
    assert nsq(sub(x, p)) - nsq(sub(x, q)) == 2 * dot(sub(q, p), x) - 2 * c
    assert dot(sub(q, p), mul(Fr(1, 2), add(p, q))) == c
    # strict side contains p when p != q
    if p != q:
        assert dot(sub(q, p), p) < c
p, q = vec(0, 0), vec(2, 4)
c = (nsq(q) - nsq(p)) / 2
assert c == QUOTED["qc_c"]
a1, a2, cc = QUOTED["qc_reduced"]
assert (Fr(1, 2) * 2, Fr(1, 2) * 4, Fr(1, 2) * c) == (a1, a2, cc)
m = QUOTED["qc_midpoint"]
assert m[0] + 2 * m[1] == 5
print("ok")
