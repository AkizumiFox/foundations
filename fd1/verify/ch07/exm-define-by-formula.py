"""exm-define-by-formula (Section 7.5): maximal and greatest elements in divisibility orders
on {1,2,3}, {1,2,3,6} and (Quick check) {1,2,3,4,6}; the warning's set (greatest defines empty
on {1,2,3}); sup [0,1) = 1 with the witness max(0, (z+1)/2)."""
from fractions import Fraction as F

def le(d, e):
    return e % d == 0
def maximal(S):
    return sorted(x for x in S if all((not le(x, y)) or y == x for y in S))
def greatest(S):
    return sorted(x for x in S if all(le(y, x) for y in S))
QUOTED = {"123": ([2, 3], []), "1236": ([6], [6]), "12346": ([4, 6], [])}
assert (maximal({1, 2, 3}), greatest({1, 2, 3})) == QUOTED["123"]
assert (maximal({1, 2, 3, 6}), greatest({1, 2, 3, 6})) == QUOTED["1236"]
assert (maximal({1, 2, 3, 4, 6}), greatest({1, 2, 3, 4, 6})) == QUOTED["12346"]
for z in [F(-5), F(0), F(1, 3), F(9, 10), F(999, 1000)]:
    w = max(F(0), (z + 1) / 2)
    assert 0 <= w < 1 and w > z
print("exm-define-by-formula: all quoted values check")
