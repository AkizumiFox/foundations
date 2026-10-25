"""exm-independence-rst (Section 7.4): each structure has exactly the two named properties;
the first two are 5.4 B5 (d), (f) with a, b for 0, 1."""
import sys
sys.path.insert(0, "verify/ch07")
from _rel_props import refl, sym, trans

QUOTED = {
    "not_refl": ("ab", {("a", "a")}),
    "not_sym": ("ab", {("a", "a"), ("b", "b"), ("a", "b")}),
    "not_trans": ("a,b,c", {("a", "a"), ("b", "b"), ("c", "c"),
                          ("a", "b"), ("b", "a"), ("b", "c"), ("c", "b")}),
}
D, R = QUOTED["not_refl"]
assert not refl(D, R) and sym(D, R) and trans(D, R) and ("b", "b") not in R
D, R = QUOTED["not_sym"]
assert refl(D, R) and not sym(D, R) and trans(D, R) and ("b", "a") not in R
D, R = QUOTED["not_trans"]; D = D.split(",")
assert refl(D, R) and sym(D, R) and not trans(D, R) and ("a", "c") not in R
ren = {"a": 0, "b": 1}
assert {(ren[x], ren[y]) for x, y in QUOTED["not_refl"][1]} == {(0, 0)}
assert {(ren[x], ren[y]) for x, y in QUOTED["not_sym"][1]} == {(0, 0), (1, 1), (0, 1)}
print("exm-independence-rst: all quoted values check")
