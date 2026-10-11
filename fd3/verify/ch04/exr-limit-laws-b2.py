"""exr-limit-laws-b2: distractor eps = a - b gives only a_n > b and b_n < a, which
a_n = b_n = (a + b)/2 satisfies together with a_n <= b_n; the right eps = (a - b)/2 separates."""
from fractions import Fraction as Q

QUOTED = {}
for A in [Q(p, 3) for p in range(-6, 7)]:
    for B in [Q(p, 5) for p in range(-6, 7)]:
        if B < A:
            m = (A + B) / 2
            e = A - B
            assert abs(m - A) < e and abs(m - B) < e and m <= m   # no contradiction
            e2 = (A - B) / 2
            assert not (abs(m - A) < e2)                          # midpoint excluded
print("ok")
