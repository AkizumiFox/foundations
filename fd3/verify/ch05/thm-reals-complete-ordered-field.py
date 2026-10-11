"""Quick check after thm-reals-complete-ordered-field (Section 5.6): bisection of A = {q in Q : q^2 < 2}
with a_0 = 1, M = 2: (l_k, u_k) = (0, 2), (1, 2), (1, 3/2), (5/4, 3/2); D = 2, u_3 - l_3 = 1/4 = D/2^3;
7/5 in A (49/25 < 2); midpoints 1, 3/2, 5/4."""
from fractions import Fraction as F
QUOTED = {"pairs": [(F(0), F(2)), (F(1), F(2)), (F(1), F(3, 2)), (F(5, 4), F(3, 2))],
          "mid": [F(1), F(3, 2), F(5, 4)], "width3": F(1, 4), "D": 2}
def is_upper_bound(c):
    # for c > 0: c is an upper bound of A iff c^2 >= 2 (no rational has square 2)
    return c > 0 and c * c >= 2
assert F(7, 5) ** 2 == F(49, 25) < 2
l, u = F(0), F(2)
pairs = [(l, u)]
mids = []
for k in range(3):
    c = (l + u) / 2
    mids.append(c)
    if is_upper_bound(c):
        u = c
    else:
        assert F(7, 5) > c   # the witness used in the text
        l = c
    pairs.append((l, u))
assert pairs == QUOTED["pairs"] and mids == QUOTED["mid"]
D = pairs[0][1] - pairs[0][0]
assert D == QUOTED["D"] and pairs[3][1] - pairs[3][0] == QUOTED["width3"] == D / 2 ** 3
print("ok")
