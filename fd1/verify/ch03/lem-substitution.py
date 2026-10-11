"""lem-substitution (Section 3.4): the worked substitution and the warning's rows, and a
brute-force check of the lemma: for every tautology chi over p, q with up to 2 connectives
and every substitution of formulas over q, r with up to 1 connective, sigma(chi) is a
tautology."""
import itertools
import sys
sys.path.insert(0, "verify/ch03")
import _logic as L

QUOTED = {"lemma holds on the sample": True}


def subst(f, s):
    if f[0] == "atom":
        return s.get(f[1], f)
    if f[0] == "bot":
        return f
    return (f[0],) + tuple(subst(g, s) for g in f[1:])


def build(k, names):
    if k == 0:
        return [("atom", a) for a in names] + [("bot",)]
    out = [("not", g) for g in build(k - 1, names)]
    for i in range(k):
        for a in build(i, names):
            for b in build(k - 1 - i, names):
                out += [(op, a, b) for op in "&|>="]
    return out


def taut(f):
    return all(L.val(f, r) for r in L.rows(sorted(L.atoms(f))))


chis = [f for k in range(3) for f in build(k, "pq") if taut(f)]
phis = [f for k in range(2) for f in build(k, "qr")]
ok = True
for chi in chis:
    for a, b in itertools.product(phis, repeat=2):
        ok &= taut(subst(chi, {"p": a, "q": b}))
assert ok is QUOTED["lemma holds on the sample"]
# worked example: sigma(p) = q and r, sigma(q) = p
got = subst(L.parse(r"(p \to q) \vee \neg p"), {"p": L.parse(r"q \wedge r"), "q": ("atom", "p")})
assert got == L.parse(r"((q \wedge r) \to p) \vee \neg(q \wedge r)")
assert taut(L.parse(r"(q \to r) \vee \neg(q \to r)"))
# warning: q -> p is not a tautology (q = T, p = F); p or q is not, p or not p is
assert [L.tv(r, "p", "q") for r in L.false_rows(r"q \to p")] == [(False, True)]
assert L.false_rows(r"p \vee q") and not L.false_rows(r"p \vee \neg p")
print("lem-substitution: all quoted values check")
