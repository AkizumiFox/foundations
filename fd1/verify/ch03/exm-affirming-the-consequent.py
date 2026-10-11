"""exm-affirming-the-consequent (Section 3.4): the only refuting row of p -> q, q |= p is
p = F, q = T; the n = 2 face: 2 is even and not divisible by 4; the Quick check's
denying-the-hypothesis row."""
import sys
sys.path.insert(0, "verify/ch03")
import _logic as L

QUOTED = {"n": 2}
ref = L.entails([r"p \to q", "q"], "p")
assert [L.tv(r, "p", "q") for r in ref] == [(False, True)]
n = QUOTED["n"]
assert n % 2 == 0 and n % 4 != 0
assert not L.entails(["p", r"\neg p"], "q")
assert [L.tv(r, "p", "q") for r in L.entails([r"p \to q", r"\neg p"], r"\neg q")] == [(False, True)]
print("exm-affirming-the-consequent: all quoted values check")
