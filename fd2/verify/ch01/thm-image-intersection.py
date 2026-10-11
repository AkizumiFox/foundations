"""The opening question of Ch 6, Section 6.6 (the witness for thm-image-intersection):
squaring, A = [-1,0], B = [0,1]; preimages of C = [0,1], D = [1,4]."""
from fractions import Fraction as F
QUOTED = {"A": [-1, 0], "B": [0, 1], "D": [1, 4]}
def grid(lo, hi, n=1000):
    lo, hi = F(lo), F(hi)
    return [lo + (hi - lo) * k / n for k in range(n + 1)]
sq = lambda x: x * x
# f(A) and f(B) are [0,1]: squares land there, and every y in [0,1] is hit (by -r and r, r = sqrt y)
assert all(0 <= sq(a) <= 1 for a in grid(-1, 0)) and all(0 <= sq(b) <= 1 for b in grid(0, 1))
# preimages: [0,1] -> [-1,1]; [1,4] -> [-2,-1] u [1,2]; common points -1, 1; {1} -> {-1, 1}
xs = grid(-3, 3, 3000)
both = [x for x in xs if 0 <= sq(x) <= 1 and 1 <= sq(x) <= 4]
assert both == [-1, 1] and [x for x in xs if sq(x) == 1] == [-1, 1]
print("thm-image-intersection: all quoted values check")
