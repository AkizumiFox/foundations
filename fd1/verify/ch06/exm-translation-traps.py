"""exm-translation-traps (Section 6.1): each trap's separating reading."""
from fractions import Fraction as F

QUOTED = {"(a) witness": F(1, 2), "(b) A": {1}, "(b) B": {-1}, "(c) n": 2, "(d) n": 1, "(e) A": set()}

N = range(0, 201)
lo, hi = F(1, 3), F(2, 3)
# (a) no natural number in (1/3, 2/3): the sentence and the right formula are false
assert not any(lo < n < hi for n in N)
assert 0 < lo and hi < 1
# the wrong formula (n ranging over the reals) is true at 1/2
assert lo < QUOTED["(a) witness"] < hi

# (b) A = {1}, B = {-1}
A, B = QUOTED["(b) A"], QUOTED["(b) B"]
grid = [F(k, 4) for k in range(-40, 41)]
sentence_b = all(x > 0 for x in A | B)
wrong_b = all(x > 0 for x in grid if (x in A and x in B))
right_b = all(x > 0 for x in grid if (x in A or x in B))
assert sentence_b is False and right_b is False and wrong_b is True
assert not (A & B)

# (c) over N: right true, wrong false at 2
even = lambda n: n % 2 == 0
assert all(even(n) for n in N if n % 4 == 0)
assert even(2) and 2 % 4 != 0
assert QUOTED["(c) n"] == 2

# (d) right formula true; wrong formula at n = 1: hypothesis true (6 | 6), conclusion false
assert all(even(n) for n in N if n % 6 == 0)
assert any(n % 6 == 0 for n in N) and 6 % 6 == 0
assert not even(QUOTED["(d) n"])

# (e) A empty: right formula has false hypothesis (true); wrong: hypothesis true, conclusion false
A = QUOTED["(e) A"]
right_hyp = any(x < 0 for x in A)
wrong_hyp = all(x < 0 for x in A)
concl = not all(0 <= x for x in A)
assert (not right_hyp or concl) is True
assert wrong_hyp is True and concl is False
print("exm-translation-traps: all quoted values check")
