"""exr-unique-factorization-b3: factorizations of 1001 and 2^10 - 1, primality checks, the gcd."""
from math import gcd, prod

QUOTED = {
    "f1001": (7, 11, 13), "m143": 143,
    "f1023": (3, 11, 31), "m341": 341, "pow": 1024,
    "div11": [(5, 2, 1), (3, 3, 2)], "div13": [(6, 2, 1), (4, 3, 1)],
    "div31": [(15, 2, 1), (10, 3, 1), (7, 4, 3), (6, 5, 1)],
    "sq": {4: 16, 6: 36},
    "q91": 91, "q93": 93, "div91_by_2": (45, 1),
    "bez": (46, 45, 4186, 4185),
    "euclid": [(1023, 1, 1001, 22), (1001, 45, 22, 11), (22, 2, 11, 0)],
    "gcd": 11,
}
assert 2 ** 10 == QUOTED["pow"] and QUOTED["pow"] - 1 == 1023
assert 1001 == 7 * QUOTED["m143"] and QUOTED["m143"] == 11 * 13 and prod(QUOTED["f1001"]) == 1001
assert 1023 == 3 * QUOTED["m341"] and QUOTED["m341"] == 11 * 31 and prod(QUOTED["f1023"]) == 1023
for p, key in [(11, "div11"), (13, "div13"), (31, "div31")]:
    for q, d, r in QUOTED[key]:
        assert p == q * d + r and 0 < r < d
    ds = [d for _, d, _ in QUOTED[key]]
    assert ds == [d for d in range(2, p) if d * d <= p]
for d, v in QUOTED["sq"].items():
    assert d * d == v
assert 4 * 4 > 13 and 6 * 6 > 31
assert 1001 == 11 * QUOTED["q91"] and 1023 == 11 * QUOTED["q93"]
assert QUOTED["q91"] == 7 * 13 and QUOTED["q93"] == 3 * 31 and QUOTED["q93"] - QUOTED["q91"] == 2
q, r = QUOTED["div91_by_2"]
assert 91 == q * 2 + r and r == 1
x, y, a, b = QUOTED["bez"]
assert 91 * x == a and 93 * y == b and a - b == 1
assert 1001 * x - 1023 * y == 11
for (a_, q_, b_, r_) in QUOTED["euclid"]:
    assert a_ == q_ * b_ + r_ and 0 <= r_ < b_
assert gcd(1001, 1023) == QUOTED["gcd"]
print("exr-unique-factorization-b3: ok")
