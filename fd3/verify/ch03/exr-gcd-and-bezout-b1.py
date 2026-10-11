"""exr-gcd-and-bezout-b1: Euclid on (1001, 357) and 7 = 5*1001 - 14*357."""
import math
QUOTED = {"rows": [(1001, 2, 357, 287), (357, 1, 287, 70), (287, 4, 70, 7), (70, 10, 7, 0)],
          "gcd": 7, "x": 5, "y": -14}
for x, q, y, r in QUOTED["rows"]:
    assert x == q * y + r and 0 <= r < y
assert math.gcd(1001, 357) == QUOTED["gcd"]
assert 287 - 4 * 70 == 7 and 5 * 287 - 4 * 357 == 7 and 5 * (1001 - 2 * 357) - 4 * 357 == 7
assert 1001 * QUOTED["x"] + 357 * QUOTED["y"] == 7
assert 5 * 1001 == 5005 and 14 * 357 == 4998 and 5005 - 4998 == 7
print("ok")
