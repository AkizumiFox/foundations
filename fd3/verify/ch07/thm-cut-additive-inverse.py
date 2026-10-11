"""thm-cut-additive-inverse (Section 7.3): with eps = -s/2, t = s - p: -t - eps = p + eps and p + t = s;
the construction run on rational cuts and on sigma; and the prompt's answer: with eps = -s on D_1,
s = -1, a = 0 the walk stops at p = 0 and 1 - r lies in D_1 for every r > 0."""
from fractions import Fraction as Fr
import random

QUOTED = {"prompt_p": 0}

random.seed(1)
for _ in range(3000):
    s = -Fr(random.randint(1, 10**5), random.randint(1, 10**3))
    p = Fr(random.randint(-10**5, 10**5), random.randint(1, 10**3))
    eps = -s / 2
    t = s - p
    assert -t - eps == p + eps and p + t == s and s == -2 * eps


def walk(member, a, e):
    n = 0
    while member(a + (n + 1) * e):
        n += 1
    return a + n * e  # in alpha, next step out


def sigma(x):
    return x <= 0 or x * x < 2


cuts = [lambda x, c=c: x < c for c in [Fr(1), Fr(-3), Fr(7, 2)]] + [sigma]
starts = [Fr(0), Fr(-5), Fr(1), Fr(-1)]
random.seed(5)
for member, a in zip(cuts, starts):
    assert member(a)
    for _ in range(300):
        sv = -Fr(random.randint(1, 4000), random.randint(1, 400))
        e = -sv / 2
        pv = walk(member, a, e)
        tv = sv - pv
        assert member(pv) and not member(pv + e)
        assert not member(-tv - e) and pv + tv == sv
# prompt: D_1, s = -1, a = 0, eps = 1
D1 = lambda x: x < 1
pv = walk(D1, Fr(0), Fr(1))
assert pv == QUOTED["prompt_p"]
for r in [Fr(1, k) for k in range(1, 100)]:
    assert D1(pv - (-1) - r)
print("ok")
