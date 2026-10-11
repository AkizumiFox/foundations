"""exr-a-cauchy-sequence-without-a-limit-r2: r_0 = 1, r_{n+1} = r_n/2 + 1 in Q;
r_1 = 3/2, r_2 = 7/4; 1 <= r_n < 2, r_n < r_{n+1}, r_{n+1} - r_n = 1 - r_n/2."""
from fractions import Fraction as Q

QUOTED = {"r1": Q(3, 2), "r2": Q(7, 4)}
r = [Q(1)]
for n in range(200):
    r.append(r[n] / 2 + 1)
for n in range(200):
    assert 1 <= r[n] < 2
    assert r[n] < r[n + 1]
    assert r[n + 1] - r[n] == 1 - r[n] / 2 > 0
    assert r[n] == r[n] / 2 + r[n] / 2
assert Q(2) / 2 == 1 < 2
assert r[1] == QUOTED["r1"] and r[2] == QUOTED["r2"]
print("ok")
