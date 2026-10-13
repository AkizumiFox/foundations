"""thm-cnf (Section 3.7, the warning after exm-normal-forms-two-routes): distributing
(p1 and q1) or (p2 and q2) or (p3 and q3) gives 8 clauses (2^n for n conjuncts), and their
conjunction is equivalent to it."""
import itertools
from _s0607_lib import equivalent
QUOTED = {"clauses": 8}
clauses = ["(" + " \\vee ".join(c) + ")" for c in itertools.product("PA", "QB", "RE")]
assert len(clauses) == 8
assert equivalent("(P \\wedge A) \\vee (Q \\wedge B) \\vee (R \\wedge E)", " \\wedge ".join(clauses))
print("thm-cnf: all quoted values check")
