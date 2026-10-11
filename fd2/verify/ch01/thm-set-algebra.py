"""thm-set-algebra (Section 6.2): the eight laws on all triples of subsets of a 3-element set,
the truth table for (d), and the absorption quick check."""
from itertools import combinations, product
QUOTED = {}
U = [1, 2, 3]
subs = [frozenset(c) for k in range(4) for c in combinations(U, k)]
for A, B, C in product(subs, repeat=3):
    assert A | B == B | A and A & B == B & A
    assert (A | B) | C == A | (B | C) and (A & B) & C == A & (B & C)
    assert A & (B | C) == (A & B) | (A & C) and A | (B & C) == (A | B) & (A | C)
    assert A - (B | C) == (A - B) & (A - C) and A - (B & C) == (A - B) | (A - C)
    assert A & (A | B) == A
# the printed table (rows T before F, last atom fastest)
cols = []
for p, q, r in product([True, False], repeat=3):
    c4 = p and not (q or r)
    c5 = (p and not q) and (p and not r)
    c6 = p and not (q and r)
    c7 = (p and not q) or (p and not r)
    assert c4 == c5 and c6 == c7
    cols.append((c4, c6))
assert cols == [(False, False), (False, True), (False, True), (True, True),
                (False, False), (False, False), (False, False), (False, False)]
# section examples: {1,2,3} and {2,4}; [0,2], [1,3] checked by sampling
A, B = {1, 2, 3}, {2, 4}
assert A | B == {1, 2, 3, 4} and A & B == {2} and A - B == {1, 3} and B - A == {4}
assert (A | B) - (A & B) == {1, 3, 4}
X, A2, B2 = {1, 2, 3, 4, 5, 6}, {1, 2, 3}, {2, 4, 6}
assert X - (A2 | B2) == {5} == (X - A2) & (X - B2) and X - A2 == {4, 5, 6} and X - B2 == {1, 3, 5}
from fractions import Fraction as F
for n in range(-40, 120):
    x = F(n, 32)
    inA, inB = 0 <= x <= 2, 1 <= x <= 3
    assert (inA or inB) == (0 <= x <= 3) and (inA and inB) == (1 <= x <= 2)
    assert (inA and not inB) == (0 <= x < 1)
# integers divisible by 2 and 3 are the multiples of 6
assert all((n % 2 == 0 and n % 3 == 0) == (n % 6 == 0) for n in range(-200, 201))
# warning: {1} minus {2} vs {2} minus {1}
assert {1} - {2} == {1} and {2} - {1} == {2}
print("thm-set-algebra: all quoted values check")
