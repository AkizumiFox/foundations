"""prp-norm-coordinate-bounds and cor-balls-and-boxes-rn: M <= ||x|| <= sqrt(n) M on random vectors (checked on squares, exactly);
sharpness: e1 gives M = ||x|| = 1, (1,...,1) gives ||x|| = sqrt n = sqrt n * M; the corner (r/sqrt2, r/sqrt2) of the inner square has norm r;
the corollary (b) on random points."""
QUOTED = {"bound": "\\sqrt n \\, M", "inner": "r / \\sqrt 2"}
from fractions import Fraction as Fr
import random

def sq(x): return sum(a * a for a in x)
random.seed(11)
for _ in range(5000):
    n = random.randint(1, 7)
    x = [Fr(random.randint(-20, 20), random.randint(1, 6)) for _ in range(n)]
    M = max(abs(a) for a in x)
    assert all(a * a <= sq(x) for a in x) and M * M <= sq(x) <= n * M * M
for n in range(1, 10):
    e1 = [1] + [0] * (n - 1); assert sq(e1) == 1 and max(map(abs, e1)) == 1
    ones = [1] * n; assert sq(ones) == n  # ||(1,..,1)|| = sqrt n, M = 1
# corner (r/sqrt2, r/sqrt2): squared norm 2 * (r^2/2) = r^2
for r2 in (Fr(1), Fr(9, 4), Fr(7)):
    assert 2 * (r2 / 2) == r2
# (b): coordinates within r/sqrt n give distance < r (checked on squares: sum d_k^2 < n (r^2/n) = r^2)
for _ in range(3000):
    n = random.randint(1, 6); r2 = Fr(random.randint(1, 50), random.randint(1, 5))
    d = [Fr(random.randint(-100, 100), 101) for _ in range(n)]
    if all(dk * dk < r2 / n for dk in d):
        assert sq(d) < r2
# instance: x = (1,-2,2): M = 2, ||x||^2 = 9 = 3^2, and 3 <= 2 sqrt 3 since 9 <= 12 = (2 sqrt 3)^2 = 4 * 3
x0 = (1, -2, 2); assert max(abs(a) for a in x0) == 2 and sq(x0) == 9 == 3 * 3 and 9 <= 4 * 3
print("ok")
