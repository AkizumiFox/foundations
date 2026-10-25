"""exr-counter-models-c4 (Section 7.2): least sizes 3, 3, 2 by exhaustive search over sizes 1-3,
and the stated counter-models."""
import sys
sys.path.insert(0, "verify/ch07")
from _fo_models import (structure, is_counter_model, all_relations, all_subsets,
                        P, ALL, EX, NOT, AND, OR)
X = lambda n: P(n, "x")
a_G = [EX("x", X("P")), EX("x", X("Q")), EX("x", X("R"))]
a_c = OR(OR(EX("x", AND(X("P"), X("Q"))), EX("x", AND(X("Q"), X("R")))), EX("x", AND(X("P"), X("R"))))
b_G = [ALL("x", EX("y", P("R", "x", "y"))), ALL("x", NOT(P("R", "x", "x")))]
b_c = EX("x", EX("y", AND(P("R", "x", "y"), P("R", "y", "x"))))
c_G = [EX("x", X("P")), EX("x", NOT(X("P"))), EX("x", X("Q")), EX("x", NOT(X("Q")))]
c_c = OR(EX("x", AND(X("P"), X("Q"))), EX("x", AND(NOT(X("P")), NOT(X("Q")))))
def least(G, c, gen):
    for n in (1, 2, 3):
        if any(is_counter_model(G, c, M) for M in gen(list(range(n)))):
            return n
def unary3(D):
    for Ps in all_subsets(D):
        for Qs in all_subsets(D):
            for Rs in all_subsets(D):
                yield structure(D, pred={"P": Ps, "Q": Qs, "R": Rs})
def binary(D):
    for R in all_relations(D, 2):
        yield structure(D, pred={"R": R})
def unary2(D):
    for Ps in all_subsets(D):
        for Qs in all_subsets(D):
            yield structure(D, pred={"P": Ps, "Q": Qs})
assert least(a_G, a_c, unary3) == 3
assert least(b_G, b_c, binary) == 3
assert least(c_G, c_c, unary2) == 2
assert is_counter_model(a_G, a_c, structure("abc", pred={"P": {("a",)}, "Q": {("b",)}, "R": {("c",)}}))
assert is_counter_model(b_G, b_c, structure("abc", pred={"R": {("a", "b"), ("b", "c"), ("c", "a")}}))
assert is_counter_model(c_G, c_c, structure("ab", pred={"P": {("a",)}, "Q": {("b",)}}))
print("exr-counter-models-c4: all quoted values check")
