"""prp-nearest-point-on-hyperplane: Pythagoras identity, invariance under (la, lc); Quick check (1,2,3)."""
import random
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from _hyperplanes_rn import Fr, vec, dot, sub, mul, nsq

QUOTED = {"qc_point": (-1, 0, 1), "qc_dist_sq": 12}


def star(x, a, c):
    return sub(x, mul((dot(a, x) - c) / nsq(a), a))


random.seed(3)
for _ in range(200):
    n = random.randint(1, 4)
    a = vec(*[random.randint(-5, 5) for _ in range(n)])
    if nsq(a) == 0:
        continue
    c = Fr(random.randint(-9, 9))
    x = vec(*[random.randint(-9, 9) for _ in range(n)])
    xs = star(x, a, c)
    assert dot(a, xs) == c
    # random point y of H: xs + w with w orthogonal to a
    z = vec(*[random.randint(-9, 9) for _ in range(n)])
    w = sub(z, mul(dot(z, a) / nsq(a), a))
    y = tuple(u + v for u, v in zip(xs, w))
    assert dot(a, y) == c
    assert nsq(sub(x, y)) == nsq(sub(x, xs)) + nsq(sub(xs, y))
    # distance squared formula
    assert nsq(sub(x, xs)) == (dot(a, x) - c) ** 2 / nsq(a)
    lam = Fr(random.choice([-3, -1, 2, 5]), random.choice([1, 2, 7]))
    assert star(x, mul(lam, a), lam * c) == xs
x, a, c = vec(1, 2, 3), vec(1, 1, 1), 0
xs = star(x, a, c)
assert xs == vec(*QUOTED["qc_point"])
assert nsq(sub(x, xs)) == QUOTED["qc_dist_sq"] == Fr(36, 3)  # (2 sqrt 3)^2 = 12 = 6^2/3
print("ok")
