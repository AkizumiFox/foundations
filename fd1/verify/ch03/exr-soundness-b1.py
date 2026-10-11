"""exr-soundness-b1 (Section 3.5): refuting rows for (a)-(c); (d) has no refuting row, and
its conclusion is false only at p = T, q = r = F, where the premise is false."""
import sys
sys.path.insert(0, "verify/ch03")
import _logic as L

QUOTED = {"non-derivable": 3}
a = [L.tv(r, "p", "q", "r") for r in L.entails([r"(p \wedge q) \to r"], r"p \to r")]
b = [L.tv(r, "p", "q") for r in L.entails([r"\neg(p \wedge q)"], r"\neg p")]
c = [L.tv(r, "p", "q", "r") for r in L.entails([r"p \leftrightarrow q", r"q \vee r"], "p")]
assert (True, False, False) in a and (True, False) in b and (False, False, True) in c
assert not L.entails([r"p \to (q \vee r)"], r"(p \to q) \vee (p \to r)")
assert [L.tv(r, "p", "q", "r") for r in L.false_rows(r"(p \to q) \vee (p \to r)")] == [(True, False, False)]
assert sum(bool(x) for x in (a, b, c)) == QUOTED["non-derivable"]
print("exr-soundness-b1: all quoted values check")
