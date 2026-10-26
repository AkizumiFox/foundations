"""exr-division-with-remainder-c2 (C1: remainders of squares mod 4)."""
QUOTED = {"even": (4, 0), "odd": ((1, 1), 1), "sums": {0, 1, 2}}  # a^2 = q^2*4+0; (q^2+q)*4+1


def rem(a, n):
    rs = [a - q * n for q in range(-abs(a) - 1, abs(a) + 2) if 0 <= a - q * n < n]
    assert len(rs) == 1
    return rs[0]


for q in range(-60, 61):
    assert (2 * q) ** 2 == q * q * 4 + QUOTED["even"][1] == 4 * q * q
    (u, v), r1 = QUOTED["odd"]
    assert (2 * q + 1) ** 2 == 4 * q * q + 4 * q + 1 == (u * q * q + v * q) * 4 + r1
assert 4 == 2 * 2
assert {rem(a * a, 4) for a in range(-120, 121)} == {0, 1}
assert {s + t for s in (0, 1) for t in (0, 1)} == QUOTED["sums"] and 3 not in QUOTED["sums"]
assert all(rem(x * x + y * y, 4) != 3 for x in range(-40, 41) for y in range(-40, 41))
print("ok")
