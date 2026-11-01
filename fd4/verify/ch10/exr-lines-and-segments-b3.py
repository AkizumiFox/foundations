"""exr-lines-and-segments-b3: R(1,0,0) and (0,1,0)+R(0,0,1) are skew: second coordinates 0 != 1; directions not multiples."""
from fractions import Fraction as Fr

for s in range(-5, 6):
    for t in range(-5, 6):
        assert (s, 0, 0) != (0, 1, t)
assert (0, 0, 0)[1] == 0 != 1
# (1,0,0) = L(0,0,1) needs 1 = 0 in coordinate 1; (0,0,1) = L(1,0,0) needs 1 = 0 in coordinate 3
assert all(L * 0 != 1 for L in map(Fr, range(-5, 6)))
print("ok")
