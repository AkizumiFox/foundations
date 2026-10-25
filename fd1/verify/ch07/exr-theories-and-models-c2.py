"""exr-theories-and-models-c2 (Section 7.4): three structures, each satisfying exactly two
of (Refl), (Antisym), (Trans); and (N, <=) satisfying all three (window)."""
import sys
sys.path.insert(0, "verify/ch07")
from _rel_props import refl, antisym, trans

QUOTED = {
    "not_refl": ("ab", {("a", "b")}),
    "not_antisym": ("ab", {("a", "a"), ("a", "b"), ("b", "a"), ("b", "b")}),
    "not_trans": ("a,b,c", {("a", "a"), ("b", "b"), ("c", "c"), ("a", "b"), ("b", "c")}),
}
D, R = QUOTED["not_refl"]
assert not refl(D, R) and antisym(D, R) and trans(D, R)
D, R = QUOTED["not_antisym"]
assert refl(D, R) and not antisym(D, R) and trans(D, R)
D, R = QUOTED["not_trans"]; D = D.split(",")
assert refl(D, R) and antisym(D, R) and not trans(D, R) and ("a", "c") not in R
N = range(12)
le = {(x, y) for x in N for y in N if x <= y}
assert refl(N, le) and antisym(N, le) and trans(N, le)
print("exr-theories-and-models-c2: all quoted values check")
