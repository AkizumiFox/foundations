"""exm-rhetoric-conjunction (Ch 5, Section 5.1): A = (0, 2); 2 is an upper bound and no t < 2 is;
the witness a = (max{t, 0} + 2)/2 lies in A and exceeds t."""
from fractions import Fraction as Fr

QUOTED = {"bound": 2, "witness (max(t,0)+2)/2 checked below": True, "a_range": (1, 2)}

# exact checks on many t < 2, including negative, zero, and close to 2
ts = [Fr(-1000), Fr(-3), Fr(-1, 2), Fr(0), Fr(1, 3), Fr(1), Fr(3, 2), Fr(199, 100), Fr(1999999, 1000000)]
for tv in ts:
    mv = max(tv, Fr(0))
    av = (mv + 2) / 2
    assert 0 <= mv < 2 and mv >= tv
    assert QUOTED["a_range"][0] <= av < QUOTED["a_range"][1]
    assert 0 < av < QUOTED["bound"]          # a in A
    assert av - mv == (2 - mv) / 2 > 0
    assert av > tv                            # a > t, so t is not an upper bound
# every element of A is <= 2
for x in [Fr(1, 10**6), Fr(1), Fr(19, 10), Fr(1999999, 10**6)]:
    assert 0 < x < 2 and x <= QUOTED["bound"]
print("exm-rhetoric-conjunction: all quoted values check")
