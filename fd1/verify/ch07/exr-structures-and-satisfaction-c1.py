"""exr-structures-and-satisfaction-c1 (Section 7.1): the three entailments hold on every structure
with one-place P, Q (and a constant c in (c)) on 1-3 elements."""
import sys
sys.path.insert(0, "verify/ch07")
from _fo_models import structure, sat, is_counter_model, all_subsets, P, ALL, EX, AND, OR, IMP

c = ("c", "c")
cases = [
    ([ALL("x", AND(P("P", "x"), P("Q", "x")))], AND(ALL("x", P("P", "x")), ALL("x", P("Q", "x")))),
    ([ALL("x", OR(P("P", "x"), P("Q", "x")))], OR(ALL("x", P("P", "x")), EX("x", P("Q", "x")))),
    ([EX("x", IMP(P("P", "x"), P("Q", c)))], IMP(ALL("x", P("P", "x")), P("Q", c))),
]
count = 0
for n in range(1, 4):
    D = list(range(n))
    for Ps in all_subsets(D):
        for Qs in all_subsets(D):
            for cv in D:
                M = structure(D, const={"c": cv}, pred={"P": Ps, "Q": Qs})
                for prem, concl in cases:
                    assert not is_counter_model(prem, concl, M)
                    count += 1
assert count > 0
print("exr-structures-and-satisfaction-c1: all quoted values check")
