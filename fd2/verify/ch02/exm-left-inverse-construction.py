"""exm-left-inverse-construction (Ch 6, Section 6.5): f: {1,2} -> {a,b,c}, 1->a, 2->c."""
from itertools import product
QUOTED = {"number of left inverses": 2, "x_0 = 1 gives g(b)": 1, "x_0 = 2 gives g'(b)": 2}
X, Y = [1, 2], ["a", "b", "c"]
f = {1: "a", 2: "c"}
lefts = [dict(zip(Y, vals)) for vals in product(X, repeat=len(Y))
         if all(dict(zip(Y, vals))[f[x]] == x for x in X)]
assert len(lefts) == QUOTED["number of left inverses"]
# the construction of thm-left-inverse-iff-injective (b)
def construct(x0):
    rng = set(f.values())
    return {y: (next(x for x in X if f[x] == y) if y in rng else x0) for y in Y}
assert construct(1)["b"] == 1 and construct(2)["b"] == 2
assert construct(1) in lefts and construct(2) in lefts and construct(1) != construct(2)
print("exm-left-inverse-construction: all quoted values check")
