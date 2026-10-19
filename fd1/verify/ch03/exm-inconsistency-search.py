"""exm-inconsistency-search (Ch 3 s02): the four conditions on an integer n,
(1) n even -> 4 | n, (2) n even or 3 | n, (3) 3 | n -> n even, (4) 4 does not divide n.
No n in [-200, 200] meets all four; n = 6, 1, 3, 12 each meets all but (1), (2), (3), (4);
the Quick check: in 1..10 exactly 3 and 9 meet (1), (2), (4), and each breaks (3).
Also: the letter list E -> F, E or T, T -> E, not F is unsatisfiable by truth table."""
from itertools import product

QUOTED = {
    "all_but": {6: 1, 1: 2, 3: 3, 12: 4},
    "qc_meet_124": [3, 9],
}


def conds(n):
    E, F, T = n % 2 == 0, n % 4 == 0, n % 3 == 0
    return {1: (not E) or F, 2: E or T, 3: (not T) or E, 4: not F}


for n in range(-200, 201):
    assert not all(conds(n).values()), n
for n, k in QUOTED["all_but"].items():
    c = conds(n)
    assert not c[k] and all(v for j, v in c.items() if j != k), n
meet = [n for n in range(1, 11) if conds(n)[1] and conds(n)[2] and conds(n)[4]]
assert meet == QUOTED["qc_meet_124"], meet
assert all(not conds(n)[3] for n in meet)
# the letter list, as a list of statements: no assignment makes every member true
for E, F, T in product([False, True], repeat=3):
    assert not (((not E) or F) and (E or T) and ((not T) or E) and (not F))
print("exm-inconsistency-search: ok")
