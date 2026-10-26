"""exr-addition-a1 (a): alpha = D_1, s = -1/2, a = 0: eps = 1/4, n = 3, p = 3/4, t = -5/4, margin 1/4."""
from fractions import Fraction as Fr

QUOTED = {"eps": "1/4", "n": 3, "p": "3/4", "t": "-5/4"}
s = Fr(-1, 2)
eps = -s / 2
assert eps == Fr(QUOTED["eps"])
D1 = lambda x: x < 1
n = 0
while D1(0 + (n + 1) * eps):
    n += 1
assert n == QUOTED["n"]
p = 0 + n * eps
assert p == Fr(QUOTED["p"]) and D1(p) and not D1(p + eps)
t = s - p
assert t == Fr(QUOTED["t"]) and not D1(-t - eps) and -t - eps == 1 and p + t == s
# another start may give another pair: a = 1/8 gives p = 7/8; a = -1/4 gives p = 3/4 again
def walk(a):
    k = 0
    while D1(a + (k + 1) * eps):
        k += 1
    return a + k * eps
assert walk(Fr(1, 8)) == Fr(7, 8)
assert walk(Fr(-1, 4)) == Fr(3, 4)
# any p with 3/4 <= p < 1 works with t = -1/2 - p
for k in range(750, 1000):
    pp = Fr(k, 1000)
    assert D1(pp) and not D1(-(s - pp) - eps)
print("ok")
