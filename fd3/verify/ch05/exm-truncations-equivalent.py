"""exm-truncations-equivalent and the hook of Section 5.1: the truncations d_k = m_k/10^k,
the Newton sequence, and the bounds used in Steps 1-4."""
from fractions import Fraction as F

QUOTED = {
    "m": [1, 14, 141, 1414, 14142, 141421, 1414213],
    "d_0_to_3": [F(1), F(7, 5), F(141, 100), F(707, 500)],
    "newton_0_to_3": [F(2), F(3, 2), F(17, 12), F(577, 408)],
    "diff_1_to_3": [F(1, 10), F(1, 150), F(11, 51000)],
    "m1_test": (196, 200, 225),
    "bound_at_1": F(3, 4),
}


def m_of(k):
    """largest natural m with m^2 <= 2 (10^k)^2, by search (independent of isqrt)."""
    t = 2 * (10 ** k) ** 2
    lo, hi = 0, 2 * 10 ** k
    assert hi * hi > t
    while hi - lo > 1:          # invariant: lo^2 <= t < hi^2
        mid = (lo + hi) // 2
        if mid * mid <= t:
            lo = mid
        else:
            hi = mid
    return lo


m = [m_of(k) for k in range(12)]
assert m[:7] == QUOTED["m"]
d = [F(m[k], 10 ** k) for k in range(12)]
assert d[:4] == QUOTED["d_0_to_3"]
assert (14 ** 2, 2 * 10 ** 2, 15 ** 2) == QUOTED["m1_test"]

x = [F(2)]
for _ in range(11):
    x.append((x[-1] ** 2 + 2) / (2 * x[-1]))
assert x[:4] == QUOTED["newton_0_to_3"]
assert [x[k] - d[k] for k in (1, 2, 3)] == QUOTED["diff_1_to_3"]

for k in range(12):
    p = F(10 ** k)
    assert p >= k + 1                                   # 10^k >= k + 1
    assert x[k] ** 2 > 2 >= d[k] ** 2                   # never equal
    assert (m[k] + 1) ** 2 > 2 * p * p                  # maximality
    assert 0 <= 2 - d[k] ** 2 < 5 / p                   # Step 3
    assert 1 <= d[k] < 2
    if k + 1 < 12:
        assert 10 * m[k] <= m[k + 1] and d[k] <= d[k + 1]   # Step 1
    for j in range(k, 12):
        assert 0 <= d[j] - d[k] < 1 / p <= F(1, k + 1)       # Step 2
    if k >= 1:
        e = x[k] ** 2 - 2
        assert 0 < e <= F(1, 4 * k)
        assert F(1, 4 * k) <= F(1, k + 1)
        assert abs(x[k] - d[k]) <= F(1, 4 * k) + 5 / p <= F(1, k + 1) + 5 / p
assert F(1, 4) + F(5, 10) == QUOTED["bound_at_1"]
print("ok")
