"""exm-subset-first-examples (Section 6.1): 6k = 3(2k); 3 witnesses S != T; 4 refutes 4Z in 6Z."""
QUOTED = {"proper-subset witness": 3, "non-example witness": 4}
assert all(6 * k == 3 * (2 * k) for k in range(-100, 101))
assert 3 % 3 == 0 and 3 % 6 != 0
assert 4 % 4 == 0 and 4 % 6 != 0
# [1,2] inside [0,3] on a grid
from fractions import Fraction as F
assert all(0 <= x <= 3 for x in (1 + F(k, 50) for k in range(51)))
# warning (N1): 0, 12, 24, -12 are multiples of 4 and 3, yet 4 is not a multiple of 3
assert all(n % 4 == 0 and n % 3 == 0 for n in (0, 12, 24, -12)) and 4 % 3 != 0
print("exm-subset-first-examples: all quoted values check")
