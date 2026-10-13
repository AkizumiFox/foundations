"""exr-predicates-and-quantifiers-c1 (Ch 4, Section 4.1): least elements of N, Z, [0,1], (0,1]."""
from fractions import Fraction as Fr

QUOTED = {"witness over N": 0, "witness over [0,1]": 0}

N = range(0, 500)
assert all(0 <= y for y in N)
assert all((x - 1) < x for x in range(-100, 100))
pts = sorted({Fr(p, q) for q in range(1, 30) for p in range(0, q + 1)})   # sample of [0,1]
assert all(0 <= y for y in pts) and 0 in pts
half_open = [x for x in pts if x > 0]
for x in half_open:
    y = x / 2
    assert 0 < y < x <= 1          # y lies in (0,1] and defeats x
print("exr-predicates-and-quantifiers-c1: all quoted values check")
