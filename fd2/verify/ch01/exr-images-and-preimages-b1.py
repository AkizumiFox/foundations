"""exr-images-and-preimages-b1 (Ch 6, Section 6.6): m - n, the indicator of [0,1], x^2 - 2x."""
from fractions import Fraction as F
import math
QUOTED = {"g([0,3])": [-1, 3], "g^{-1}({0})": [0, 2], "g^{-1}([-1,0])": [0, 2]}
# (a)
N = range(0, 40)  # N = {0, 1, ...}; the image is Z_{>0}
assert {m - n for m in N for n in N if m > n} == set(range(1, 40))
assert all(k - 0 == k and k > 0 for k in range(1, 100))
# (c)
g = lambda x: x * x - 2 * x
xs = [F(k, 200) for k in range(0, 601)]
vals = [g(x) for x in xs]
assert min(vals) == -1 and max(vals) == 3
assert all(abs(g(1 + math.sqrt(y + 1)) - y) < 1e-12 and 1 <= 1 + math.sqrt(y + 1) <= 3
           for y in [float(F(k, 50)) for k in range(-50, 151)])
ys = [F(k, 100) for k in range(-500, 501)]
assert [x for x in ys if g(x) == 0] == [0, 2]
assert all((-1 <= g(x) <= 0) == (0 <= x <= 2) for x in ys)
print("exr-images-and-preimages-b1: all quoted values check")
