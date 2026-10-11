"""exr-normal-forms-c1 (Section 3.7): NAND and NOR identities, checked on truth values."""
from itertools import product
QUOTED = {}
nand = lambda a, b: not (a and b)
nor = lambda a, b: not (a or b)
for a, b in product([True, False], repeat=2):
    assert nand(a, a) == (not a) and nand(nand(a, b), nand(a, b)) == (a and b)
    assert nor(a, a) == (not a) and nor(nor(a, b), nor(a, b)) == (a or b)
print("exr-normal-forms-c1: all quoted values check")
