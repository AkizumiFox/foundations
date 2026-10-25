"""exr-definability-and-isomorphism-b2 (Section 7.5): (ii) cubes in Z, (iii) {0} in (N; *),
(iv) all pairs x != y in (Z; +), (v) empty in Q (midpoint) and all of Z (y = x + 1)."""
from fractions import Fraction as F

Z = range(-20, 21)
assert [x for x in Z if any(x == y ** 3 for y in Z)] == [-8, -1, 0, 1, 8]
assert [x for x in range(0, 30) if all(y * x == x for y in range(0, 30))] == [0]
for x in Z:
    for y in Z:
        assert any(z + z != z and x + z == y for z in range(-41, 42)) == (x != y)
for x, y in [(F(0), F(1)), (F(-2, 3), F(-1, 2))]:
    m = (x + y) / 2; assert x < m < y
for x in Z:
    assert not any(x < z < x + 1 for z in range(-25, 26))
print("exr-definability-and-isomorphism-b2: all quoted values check")
