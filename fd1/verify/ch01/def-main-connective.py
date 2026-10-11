"""Values quoted in Section 1.1 between def-main-connective's neighbours on the main line:
the connective table, the promise table and its Quick check, the "only if" passage,
the try-to-break Quick check and Argument B, the good-form/bad-form table, and the fold
"Valid, or only convincing?" (Chapter 1, Section 1.1)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _grid import grid, implies_on_grid

QUOTED = {
    "promise table rows": {3: (True, True), -3: (False, True), 0: (False, False)},
    "promise quick check breakers among (3, -3, 1)": [-3],
    "only-if reverse broken at": -3,
    "form witness n": 2,
    "6-argument": 6,
    "n = 3 instance": (3, 9),
    "euler polynomial prime for n in": (0, 39),
    "n = 40 value": 1681,
    "41^2": 41,
}

# connective table: each example true for every real x (exact rational grid)
assert all(x**2 >= 0 and x**2 + 1 > 0 for x in grid())
assert all(x >= 0 or x < 0 for x in grid())
assert implies_on_grid(lambda x: x > 1, lambda x: x**2 > 1)
assert all((x**2 == 0) == (x == 0) for x in grid())
assert all(not (x**2 < 0) for x in grid())

# promise table: rows of P: x > 1, Q: x^2 > 1
for x, (p, q) in QUOTED["promise table rows"].items():
    assert (x > 1, x**2 > 1) == (p, q)
# no x with x > 1 and x^2 <= 1; and x > 1 gives x^2 > x > 1
assert not any(x > 1 and x**2 <= 1 for x in grid())
assert all(x**2 > x > 1 for x in grid() if x > 1)

# promise Quick check: "if x^2 > 4 then x > 2" broken among 3, -3, 1
broken = [x for x in (3, -3, 1) if x**2 > 4 and not x > 2]
assert broken == QUOTED["promise quick check breakers among (3, -3, 1)"]

# "only if" passage: x > 2 -> x^2 > 2x > 4; reverse broken at -3
assert all(x**2 > 2 * x > 4 for x in grid() if x > 2)
r = QUOTED["only-if reverse broken at"]
assert r**2 > 4 and not r > 2

# try to break it (i), and Argument B's converse step: P: 4 | n, Q: n even
n = QUOTED["form witness n"]
assert all((m % 4 != 0) or (m % 2 == 0) for m in range(-1000, 1001))   # P -> Q for every integer
assert n % 2 == 0 and n % 4 != 0                                       # Q true, P false at n = 2
# B's own content: n^2 even -> n even for every integer (no counterexample with B's content)
assert all((m * m) % 2 != 0 or m % 2 == 0 for m in range(-1000, 1001))

# good-form table: 6 even and not prime; 3 and 9 odd
def is_prime(k):
    return k >= 2 and all(k % d for d in range(2, int(k**0.5) + 1))
six = QUOTED["6-argument"]
assert six % 2 == 0 and not is_prime(six)
a, b = QUOTED["n = 3 instance"]
assert a**2 == b and a % 2 == 1 and b % 2 == 1

# fold: n^2 + n + 41
lo, hi = QUOTED["euler polynomial prime for n in"]
assert all(is_prime(k * k + k + 41) for k in range(lo, hi + 1))
assert 40**2 + 40 + 41 == 1600 + 40 + 41 == QUOTED["n = 40 value"] == QUOTED["41^2"] ** 2
assert not is_prime(QUOTED["n = 40 value"])
print("def-main-connective: all quoted values check")
