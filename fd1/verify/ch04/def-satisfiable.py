"""def-satisfiable (Section 3.4): p, not p is unsatisfiable; p -> q, q -> r, r -> not p is
satisfiable, by p = F, q = r = T, and p is F in every row making all three true; and the
tautology/contradiction examples after def-tautology. Rows as regions (Section 4.5): p and q
is true only at TT (the lens), p or q at TT, TF, FT (both circles), not p at FT, FF; and
p and q |= p or q; the contingent example p -> q."""
import sys
sys.path.insert(0, "verify/ch04")
import _logic as L

QUOTED = {"satisfiable": True}
gamma = [r"p \to q", r"q \to r", r"r \to \neg p"]
sat = [r for r in L.rows("pqr") if all(L.val(L.parse(g), r) for g in gamma)]
assert (len(sat) > 0) is QUOTED["satisfiable"]
assert {"p": False, "q": True, "r": True} in sat and all(not r["p"] for r in sat)
assert not [r for r in L.rows("p") if L.val(L.parse("p"), r) and L.val(L.parse(r"\neg p"), r)]
for t in [r"p \to p", r"p \vee \neg p", r"\neg\bot"]:
    assert not L.false_rows(t)
for c in [r"p \wedge \neg p", r"p \leftrightarrow \neg p", r"\bot"]:
    assert all(not L.val(L.parse(c), r) for r in L.rows(sorted(L.atoms(L.parse(c)))))
assert L.false_rows(r"p \to q") and L.entails([], r"p \to q")
reg = lambda s: [L.tv(r, "p", "q") for r in L.rows("pq") if L.val(L.parse(s), r)]
T, F = True, False
assert reg(r"p \wedge q") == [(T, T)]
assert reg(r"p \vee q") == [(T, T), (T, F), (F, T)]
assert reg(r"\neg p") == [(F, T), (F, F)]
assert set(reg(r"p \wedge q")) <= set(reg(r"p \vee q")) and not L.entails([r"p \wedge q"], r"p \vee q")
assert reg(r"p \to q") and L.false_rows(r"p \to q")
print("def-satisfiable: all quoted values check")
