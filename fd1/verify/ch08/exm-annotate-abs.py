"""exm-annotate-abs (Ch 5, Section 5.5): for real x, |x - 1| < 1 implies x > 0; the case facts
used in the table; the remark that -|u| <= u gives -1 < x - 1 in one step."""
from fractions import Fraction as F

QUOTED = {}

pts = [F(k, 97) for k in range(-500, 501)]
for x in pts:
    assert x >= 1 or x < 1                      # sentence (2)
    if abs(x - 1) < 1:
        assert x > 0                            # the claim
        assert -1 < x - 1                       # the one-step route
        if x < 1:
            assert abs(x - 1) == 1 - x          # sentence (6)
            assert 1 - x < 1                    # sentence (7)
    assert -abs(x - 1) <= x - 1                 # -|u| <= u
print("exm-annotate-abs: all quoted values check")
