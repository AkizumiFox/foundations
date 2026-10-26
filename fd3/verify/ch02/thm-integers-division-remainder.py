"""thm-integers-division-remainder and its aftermath in 05-division-with-remainder:
the Quick check (-23 by 4, with the tempting non-remainder -3), the warning (-17 by 5),
and the divisibility-test instance (12 by 5)."""
QUOTED = {
    "check": (-23, 4, -6, 1),           # a, n, q, r
    "check_false": (-23, 4, -5, -3),    # a true equation, but -3 is not a remainder
    "test": (12, 5, 2, 2),
    "warning_false": (-17, 5, -3, -2),
    "warning_true": (-17, 5, -4, 3),
}


def pairs(a, n, lo=-200, hi=200):
    """All (q, r) with a = q n + r and 0 <= r < n, by search (independent of divmod)."""
    return [(q, a - q * n) for q in range(lo, hi) if 0 <= a - q * n < n]


for key in ("check", "test", "warning_true"):
    a, n, q, r = QUOTED[key]
    assert a == q * n + r and 0 <= r < n
    assert pairs(a, n) == [(q, r)]
for key in ("check_false", "warning_false"):
    a, n, q, r = QUOTED[key]
    assert a == q * n + r and not (0 <= r < n)
assert (-6) * 4 == -24 and -24 + 1 == -23
assert all(5 * k != 12 for k in range(-50, 51))
print("ok")
