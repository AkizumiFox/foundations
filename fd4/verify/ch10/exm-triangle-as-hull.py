"""exm-triangle-as-hull: (1, 1) = (1/3)(p1 + p2 + p3); (2, 2) forces lambda2 = lambda3 = 2/3, lambda1 = -1/3 < 0;
hull = {x1 >= 0, x2 >= 0, x1 + x2 <= 3}. Also A2 (a) and the hull-of-the-sides midpoint in the Idea."""
from fractions import Fraction as F
import random
QUOTED = {"w11": (F(1, 3),) * 3, "l23_for_22": F(2, 3), "sum23": F(4, 3), "a2a": (0, F(1, 3), F(2, 3))}
p = [(0, 0), (3, 0), (0, 3)]
def comb(w, pts): return tuple(sum(wi * q[k] for wi, q in zip(w, pts)) for k in range(2))
assert comb(QUOTED["w11"], p) == (1, 1)
# (2,2): weights solve 3 l2 = 2, 3 l3 = 2 uniquely
l2 = l3 = F(2, 3); assert 3 * l2 == 2 and l2 == QUOTED["l23_for_22"] and l2 + l3 == QUOTED["sum23"] and 1 - (l2 + l3) < 0
# A2 (a)
assert comb(QUOTED["a2a"], p) == (1, 2) and sum(QUOTED["a2a"]) == 1
# hull description: random weights land in the triangle, and the triangle's points have non-negative weights
random.seed(1)
for _ in range(2000):
    a, b = sorted([F(random.randint(0, 100), 100), F(random.randint(0, 100), 100)])
    w = (a, b - a, 1 - b); x = comb(w, p)
    assert x[0] >= 0 and x[1] >= 0 and x[0] + x[1] <= 3
    y = (F(random.randint(-10, 40), 10), F(random.randint(-10, 40), 10))
    inside = y[0] >= 0 and y[1] >= 0 and y[0] + y[1] <= 3
    ww = (1 - (y[0] + y[1]) / 3, y[0] / 3, y[1] / 3)
    assert comb(ww, p) == y and (min(ww) >= 0) == inside
assert (2 + 2) > 3
# Idea: (1,0) in [p,q], (0,1) in [r,p] for p=(0,0), q=(2,0), r=(0,2); midpoint (1/2,1/2) on no side
m = (F(1, 2), F(1, 2)); on_pq = m[1] == 0; on_rp = m[0] == 0; on_qr = m[0] + m[1] == 2
assert not (on_pq or on_rp or on_qr)
print("ok")
