"""exr-theories-and-models-a2 (Section 7.4 drill): parts (b), (d), (e), (f), (g), (i), (l)."""
import itertools
import sys
from fractions import Fraction as F
sys.path.insert(0, "verify/ch07")
from _rel_props import refl, irrefl, sym, antisym, trans, all_relations
from _fo_models import structure, sat, P, ALL

# (b) < on Z is not reflexive (window)
W = range(-5, 6)
assert not refl(W, {(x, y) for x in W for y in W if x < y})
# (d)
D, R = "ab", {("a", "b"), ("b", "a")}
assert sym(D, R) and not refl(D, R) and not trans(D, R)
# (e) nonzero rationals under multiplication: sample
S = [F(p, q) for p in range(-6, 7) for q in range(1, 6) if p != 0]
for u, v, w in itertools.product(S[:12], repeat=3):
    assert (u * v) * w == u * (v * w)
assert all(u * 1 == u == 1 * u and u * (1 / u) == 1 and (1 / u) != 0 for u in S)
# (f) one element
assert irrefl("a", set()) and trans("a", set())
assert refl("a", {("a", "a")}) and antisym("a", {("a", "a")}) and trans("a", {("a", "a")})
assert not irrefl("a", {("a", "a")}) and not refl("a", set())
# (g) fewest pairs added to {(a,b)} for an equivalence relation on {a,b}
best = min((R for R in all_relations("ab") if ("a", "b") in R and refl("ab", R)
            and sym("ab", R) and trans("ab", R)), key=len)
assert best - {("a", "b")} == {("a", "a"), ("b", "b"), ("b", "a")}
# (i) T = {forall x R(x,x)}: sigma false in a structure with empty R
sigma = ALL("x", P("R", "x", "x"))
assert not sat(sigma, structure(["a"], pred={"R": set()}), {})
# (l)
D = "abc"
R = {("a", "a"), ("b", "b"), ("c", "c"), ("a", "b")}
assert refl(D, R) and antisym(D, R) and trans(D, R)
assert sum(1 for x in D for y in D if x < y and ((x, y) in R or (y, x) in R)) == 1
print("exr-theories-and-models-a2: all quoted values check")
