"""exm-substitution-in-one-row (Section 4.5): sigma puts q and r for p and p for q;
v(p) = F, v(q) = T, v(r) = T; v(sigma(chi)) = F; w = (T, F, T); w(chi) = F."""
import sys
sys.path.insert(0, "verify/ch04")
import _logic as L

QUOTED = {"v(sigma chi)": False, "w": {"p": True, "q": False, "r": True}, "w(chi)": False}
v = {"p": False, "q": True, "r": True}
sigma = {"p": r"q \wedge r", "q": "p"}
schi = L.parse(r"((q \wedge r) \to p) \vee \neg(q \wedge r)")
assert L.val(schi, v) is QUOTED["v(sigma chi)"]
w = {a: L.val(L.parse(sigma.get(a, a)), v) for a in "pqr"}
assert w == QUOTED["w"]
chi = L.parse(r"(p \to q) \vee \neg p")
assert L.val(chi, w) is QUOTED["w(chi)"]
# the claim of lem-substitution on this chi, every valuation
for r in L.rows("pqr"):
    ww = {a: L.val(L.parse(sigma.get(a, a)), r) for a in "pqr"}
    assert L.val(schi, r) == L.val(chi, ww)
print("exm-substitution-in-one-row: all quoted values check")
