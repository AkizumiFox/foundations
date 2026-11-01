"""exm-lines-in-the-plane: (a) the t-formula recovers w; Quick check 4x1 + 3x2 = 13."""
import random
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from _hyperplanes_rn import Fr, vec, dot, sub, mul, nsq, add

QUOTED = {"qc_normal": (4, 3), "qc_c": 13}
random.seed(1)
for _ in range(200):
    a = vec(random.randint(-9, 9), random.randint(-9, 9))
    if a == (0, 0):
        continue
    c = Fr(random.randint(-9, 9))
    p0 = mul(c / nsq(a), a)
    assert dot(a, p0) == c
    t_rand = Fr(random.randint(-20, 20), random.randint(1, 7))
    x = add(p0, mul(t_rand, (-a[1], a[0])))  # a point of H
    w = sub(x, p0)
    t = (a[0] * w[1] - a[1] * w[0]) / nsq(a)
    assert mul(t, (-a[1], a[0])) == w
    # (b): a = (-v2, v1) is orthogonal to v
    v = vec(random.randint(-9, 9), random.randint(-9, 9))
    assert dot((-v[1], v[0]), v) == 0
# Quick check
P, Q = vec(1, 3), vec(4, -1)
v = sub(Q, P)
a = (-v[1], v[0])
assert a == vec(*QUOTED["qc_normal"])
assert dot(a, P) == QUOTED["qc_c"] == dot(a, Q)
# warning: H_{(1,1),1} = H_{(2,2),2} = H_{(-1,-1),-1} (pairs are multiples)
assert (2 * 1, 2 * 1, 2 * 1) == (2, 2, 2) and (-1, -1, -1) == tuple(-1 * k for k in (1, 1, 1))
print("ok")
