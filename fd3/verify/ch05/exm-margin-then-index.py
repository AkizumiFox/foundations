"""exm-margin-then-index: a_n = (2n + 1)/(n + 3); 2n + 1 = 2(n + 3) - 5, a_n - 1 = (n - 2)/(n + 3) = 1 - 5/(n + 3);
margin 1/2, threshold 7 (least for this margin, a_6 - 1 = 4/9); margin 1 fails; a_n - 1 > 0 from n = 3."""
from fractions import Fraction as F

QUOTED = {"delta": F(1, 2), "N": 7, "a6m1": F(4, 9), "bad_delta": 1, "pos_from": 3}

# identities of rational functions, checked exactly at many points (degree <= 2, so 50 points suffice)
for k in range(0, 50):
    k = F(k)
    a = (2 * k + 1) / (k + 3)
    assert 2 * (k + 3) - 5 == 2 * k + 1
    assert a == 2 - 5 / (k + 3)
    assert a - 1 == (k - 2) / (k + 3) == 1 - 5 / (k + 3)
    # (n-2)/(n+3) >= 1/2  <=>  2(n-2) >= n+3  <=>  n >= 7
    assert 2 * (k - 2) - (k + 3) == k - 7

t = lambda k: F(2 * k + 1, k + 3) - 1
for k in range(0, 2000):
    assert (t(k) >= QUOTED["delta"]) == (k >= QUOTED["N"])
    assert t(k) < QUOTED["bad_delta"]
    assert (t(k) > 0) == (k >= QUOTED["pos_from"])
assert t(6) == QUOTED["a6m1"] < QUOTED["delta"]
print("ok")
