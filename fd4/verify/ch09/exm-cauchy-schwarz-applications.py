"""exm-cauchy-schwarz-applications: (a) (a+b+c)^2 <= 3(a^2+b^2+c^2), equality iff a = b = c;
(b) p = (2,3,-1), ||p||^2 = 14, max of <p,x> over unit x is sqrt 14 at p/sqrt 14 (checked on squares)."""
import random, sys, os, math
sys.path.insert(0, os.path.dirname(__file__))
from _common_ch09_05 import *
QUOTED = {"p": (2, 3, -1), "p_norm2": 14}
random.seed(2)
for _ in range(5000):
    a, b, c = (random.randint(-5, 5) for _ in range(3))
    l, r = (a + b + c) ** 2, 3 * (a*a + b*b + c*c)
    assert l <= r and ((l == r) == (a == b == c))
p = QUOTED["p"]
assert n2(p) == QUOTED["p_norm2"]
s = math.sqrt(14)
assert abs(14 / s - s) < 1e-12                      # 14/sqrt14 = sqrt14
x0 = tuple(t / s for t in p)
assert abs(sum(t * t for t in x0) - 1) < 1e-12 and abs(sum(a * b for a, b in zip(p, x0)) - s) < 1e-12
for _ in range(20000):                               # random unit vectors never exceed sqrt 14
    v = [random.gauss(0, 1) for _ in range(3)]; nv = math.sqrt(sum(t * t for t in v)); v = [t / nv for t in v]
    assert sum(a * b for a, b in zip(p, v)) <= s + 1e-12
print("ok")
