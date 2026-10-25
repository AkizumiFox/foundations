"""exr-relations-b2: the chosen relation, the failing variant, and the number of all answers."""
from itertools import product, chain, combinations

X = [1, 2, 3]
pairs = list(product(X, X))


def props(R):
    return (all((x, x) in R for x in X),
            all((y, x) in R for (x, y) in R),
            all(x == y for (x, y) in R if (y, x) in R),
            all((x, z) in R for (x, y) in R for (y2, z) in R if y == y2))


R = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1), (1, 3), (2, 3)}
assert props(R) == (True, False, False, True)
bad = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1), (3, 1)}
assert props(bad)[3] is False and (3, 2) not in bad
answers = [set(c) for c in chain.from_iterable(combinations(pairs, r) for r in range(10))
           if props(set(c)) == (True, False, False, True)]
# every answer contains the diagonal, a two-way pair, a one-way pair
for A in answers:
    assert all((x, x) in A for x in X)
    assert any(x != y and (y, x) in A for (x, y) in A)
    assert any((y, x) not in A for (x, y) in A)
QUOTED = {"number_of_answers": len(answers)}
assert QUOTED["number_of_answers"] == 6, len(answers)
# structure: a two-way pair {a, b}, and the third element c entirely above or entirely below it
for A in answers:
    off = {p for p in A if p[0] != p[1]}
    two = [frozenset(p) for p in off if (p[1], p[0]) in off]
    assert len(set(two)) == 1
    a, b = sorted(two[0]); c = ({1, 2, 3} - {a, b}).pop()
    assert off - {(a, b), (b, a)} in ({(a, c), (b, c)}, {(c, a), (c, b)})
# sufficiency: the reverse of each answer is an answer (c below the pair from c above)
for A in answers:
    assert {(y, x) for (x, y) in A} in answers
assert {(y, x) for (x, y) in R} in answers
print("ok")
