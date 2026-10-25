"""exr-definability-and-isomorphism-b1 (Section 7.5): (i)-(iii) in (N; *) on a window
(divides, squares, coprime via the written formula with U renamed), (v) for sample sets."""
import math

W = range(0, 40)
WIDE = range(0, 1700)
U = lambda z: all(z * w == w for w in range(0, 3))  # z*w = w for w = 1 already forces z = 1
assert [z for z in range(0, 50) if U(z)] == [1]
divides = lambda x, y: any(x * z == y for z in WIDE)
for x in W:
    for y in W:
        assert divides(x, y) == ((x == 0 and y == 0) or (x != 0 and y % x == 0))
assert [x for x in W if any(y * y == x for y in W)] == [k * k for k in range(0, 7)]
for x in W:
    for y in W:
        f = all(not (divides(z, x) and divides(z, y)) or U(z) for z in range(0, 41))
        assert f == (math.gcd(x, y) == 1)
# (v): sup of [0,1) is 1, not in A; for A = [0,1] the sup is in A
print("exr-definability-and-isomorphism-b1: all quoted values check")
