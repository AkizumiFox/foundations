"""1.5 B4 (Prove or disprove): (a) n^2 + n sends 0 and -1 to 0; (b) x^3 + 2x is injective,
via (x - y)(x^2 + xy + y^2 + 2) and the completed square; (c) (-k, k) -> k under 2m + 3n;
(d) 2m + 4n is always even, so 1 is missed; (e) x^2 + 4x = (x + 2)^2 - 4 maps [-2, oo) onto
[-4, oo), injectively, with preimage -2 + sqrt(y + 4)."""
from fractions import Fraction as F
import itertools, math

QUOTED = {"a_witnesses": (0, -1), "c_preimage": "(-k, k)", "d_witness": 1}

# (a)
u, v = QUOTED["a_witnesses"]
assert u != v and u * u + u == v * v + v == 0
# (b) identity and positivity, exactly on a grid
pts = [F(k, 4) for k in range(-40, 41)]
for x, y in itertools.product(pts, repeat=2):
    assert (x**3 + 2 * x) - (y**3 + 2 * y) == (x - y) * (x * x + x * y + y * y + 2)
    assert x * x + x * y + y * y + 2 == (x + y / 2) ** 2 + F(3, 4) * y * y + 2 >= 2
# strictly increasing on the grid, so injective there
assert all(a**3 + 2 * a < b**3 + 2 * b for a, b in zip(pts, pts[1:]))
# (c)
for k in range(-500, 501):
    m, n = -k, k
    assert 2 * m + 3 * n == k
# (d)
assert all((2 * m + 4 * n) % 2 == 0 for m in range(-30, 31) for n in range(-30, 31))
assert QUOTED["d_witness"] % 2 == 1
# (e)
for x in [F(k, 8) for k in range(-16, 200)]:
    assert x * x + 4 * x == (x + 2) ** 2 - 4 >= -4
for k in range(0, 400):
    y = F(k, 7) - 4                      # y >= -4
    r = math.sqrt(y + 4)
    x = -2 + r
    assert x >= -2 and abs(x * x + 4 * x - float(y)) < 1e-9
for s in range(0, 50):                    # exact check on perfect squares y + 4 = s^2
    y = s * s - 4
    x = -2 + s
    assert x >= -2 and x * x + 4 * x == y
# injective on [-2, oo): equal values force equal points (exact grid)
grid = [F(k, 6) for k in range(-12, 120)]
seen = {}
for x in grid:
    val = x * x + 4 * x
    assert val not in seen
    seen[val] = x
print("exr-functions-b4: all quoted values check")
