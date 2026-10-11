"""exr-limits-b1: distances 1/(n+1) and 1/(2(2n^2+3)); 2(2n^2+3) - (n+1) = 4n^2 - n + 5 >= 3n + 5
for n >= 1 and = 5 at n = 0; hence 1/(2(2n^2+3)) <= 1/(n+1)."""
from fractions import Fraction as Q

QUOTED = {"at_0": 5}
assert 2 * (2 * 0 + 3) - (0 + 1) == QUOTED["at_0"]
for k in range(0, 3000):
    assert Q(k * k + 1, 2 * k * k + 3) - Q(1, 2) == Q(-1, 2 * (2 * k * k + 3))
    assert 2 * (2 * k * k + 3) - (k + 1) == 4 * k * k - k + 5
    if k >= 1:
        assert 4 * k * k - k + 5 >= 3 * k + 5
    assert Q(1, 2 * (2 * k * k + 3)) <= Q(1, k + 1)
    assert abs(Q(2 * k + 1, k + 1) - 2) == Q(1, k + 1)
print("ok")
