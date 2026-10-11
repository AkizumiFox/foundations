"""def-sequence-limit-ordered-field (Section 4.3): the hook distances for (n+1)/(n+2),
the non-example (distance to 2 exceeds 1), the warning sequence (1 + (-1)^n)/(n + 1),
and the "eventually" examples of def-sequence-ordered-field."""
from fractions import Fraction as Q

QUOTED = {"warning_terms": [Q(2), Q(0), Q(2, 3), Q(0), Q(2, 5)], "eventually_from": 10}
for k in range(0, 500):
    t = Q(k + 1, k + 2)
    assert 1 - t == Q(1, k + 2)                       # 1 - a_n = 1/(n+2)
    assert 2 - t == Q(k + 3, k + 2) == 1 + Q(1, k + 2)  # 2 - a_n
    assert 2 - t > 1                                  # non-example: never within 1 of 2
    assert (1 - t) > (1 - Q(k + 2, k + 3))            # distances shrink
    assert (2 - t) > (2 - Q(k + 2, k + 3))
w = [Q(1 + (-1) ** k, k + 1) for k in range(400)]
assert w[:5] == QUOTED["warning_terms"]
for k in range(400):
    assert 0 <= w[k] <= Q(2, k + 1)
    if k % 2 == 1:
        assert w[k] == 0
assert w[1] < w[2]                                     # not monotone
for e in [Q(1, 7), Q(1, 100), Q(3, 1000)]:             # |w_n| < eps once 1/(n+1) < eps/2
    for k in range(3000):
        if Q(1, k + 1) < e / 2:
            assert abs(Q(1 + (-1) ** k, k + 1)) <= Q(2, k + 1) < e
good = [k for k in range(200) if Q(1, k + 1) < Q(1, 10)]
assert min(good) == QUOTED["eventually_from"] and good == list(range(10, 200))
for k in range(50):
    assert (-1) ** (k + 2) == (-1) ** k and (-1) ** (k + 1) == -((-1) ** k)
print("ok")
