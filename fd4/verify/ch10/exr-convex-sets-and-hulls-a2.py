"""exr-convex-sets-and-hulls-a2 (a): 0*(0,0) + (1/3)(3,0) + (2/3)(0,3) = (1,2), weights >= 0 adding to 1."""
from fractions import Fraction as F
p = [(0, 0), (3, 0), (0, 3)]
w = (F(0), F(1, 3), F(2, 3))
assert all(x >= 0 for x in w) and sum(w) == 1
assert tuple(sum(wi * q[k] for wi, q in zip(w, p)) for k in range(2)) == (1, 2)
print("ok")
