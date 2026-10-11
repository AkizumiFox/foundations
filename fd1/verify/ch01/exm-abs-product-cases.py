"""exm-abs-product-cases (Ch 1, Section 1.7): |xy| = |x||y| in each of the four sign cases,
and the remark |a| = -a for a <= 0 (the x = 0, y < 0 hole)."""
from fractions import Fraction as F

QUOTED = {
    "case x>=0, y>=0: |xy| = xy": True,
    "case x>=0, y<0: xy <= 0 and |xy| = -xy = x(-y)": True,
    "case x<0, y>=0: xy <= 0 and |xy| = -xy = (-x)y": True,
    "case x<0, y<0: xy > 0 and |xy| = xy = (-x)(-y)": True,
    "x = 0, y < 0 gives xy = 0 (not negative)": 0,
}

pts = sorted({F(k, 4) for k in range(-40, 41)} | {F(0)})
for x in pts:
    for y in pts:
        p = x * y
        assert abs(p) == abs(x) * abs(y)
        if x >= 0 and y >= 0:
            assert p >= 0 and abs(p) == p
        elif x >= 0 and y < 0:
            assert p <= 0 and abs(p) == -p == x * (-y)
        elif x < 0 and y >= 0:
            assert p <= 0 and abs(p) == -p == (-x) * y
        else:
            assert p > 0 and abs(p) == p == (-x) * (-y)
for a in pts:
    if a <= 0:
        assert abs(a) == -a
assert F(0) * F(-3) == QUOTED["x = 0, y < 0 gives xy = 0 (not negative)"]
print("exm-abs-product-cases: all quoted values check")
