"""exr-predicates-and-quantifiers-b3 (Section 5.1): every and some on D = {0, 1, 2}."""
QUOTED = {"(a) verdict": True, "(a) true disjunct": 0, "(b) true disjunct": 2,
          "(c) A": set(), "(c) verdicts": (True, False)}
D = [0, 1, 2]
disjuncts = [all(x <= y for y in D) for x in D]          # the three conjunctions of (a)
assert any(disjuncts) == QUOTED["(a) verdict"]
assert [x for x in D if disjuncts[x]] == [QUOTED["(a) true disjunct"]]
assert len([(x, y) for x in D for y in D]) == 9            # nine atoms
neg = [not (x < 2) for x in D]                             # (b) after De Morgan
assert (not all(x < 2 for x in D)) == any(neg)
assert [x for x in D if neg[x]] == [QUOTED["(b) true disjunct"]]
A = {x for x in D if x > 2}
assert A == QUOTED["(c) A"]
assert (all(x > 5 for x in D if x in A), any(x in A and x > 5 for x in D)) == QUOTED["(c) verdicts"]
# (d): on every non-empty domain of size 1-4 and every P, forall P implies exists P
import itertools
for n in range(1, 5):
    for bits in itertools.product([False, True], repeat=n):
        assert (not all(bits)) or any(bits)
print("exr-predicates-and-quantifiers-b3: all quoted values check")
