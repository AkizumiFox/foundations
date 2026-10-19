"""exr-entailment-and-equivalence-a1 (Section 4.5), with the deepening's additions: the twelve
parts of the A2 drill (exr-entailment-and-equivalence-a2), the Quick check on p and q |= p or r
and its converse, and the three-operations Quick check (the substituted formula is a
tautology; q -> r is not equivalent to p)."""
import sys
sys.path.insert(0, "verify/ch04")
import _logic as L

QUOTED = {"tautologies in (a)": 2, "contradictions in (a)": 2}


def kind(s):
    f = L.parse(s)
    vals = [L.val(f, r) for r in L.rows(sorted(L.atoms(f)))]
    return "taut" if all(vals) else "contra" if not any(vals) else "sat"


ks = [kind(s) for s in [r"p \to (q \to p)", r"p \wedge \neg(p \vee q)", r"(p \to q) \wedge (q \to p)",
                        r"\neg(p \to p)", r"(p \wedge q) \to (p \vee r)"]]
assert ks == ["taut", "contra", "sat", "contra", "taut"]
assert ks.count("taut") == QUOTED["tautologies in (a)"] and ks.count("contra") == QUOTED["contradictions in (a)"]
assert not L.entails([r"p \wedge q"], r"p \leftrightarrow q")
assert [L.tv(r, "p", "q") for r in L.entails([r"p \leftrightarrow q"], r"p \wedge q")] == [(False, False)]
assert not L.entails([r"\neg p \to p"], "p")
assert [L.tv(r, "p", "q") for r in L.entails([r"p \vee q"], "p")] == [(False, True)]
assert [L.tv(r, "p", "q") for r in L.entails([r"p \vee q"], "q")] == [(True, False)]

# A2 drill
assert kind(r"(p \to q) \vee p") == "taut"                                   # (a)
assert kind(r"(p \vee q) \wedge \neg p \wedge \neg q") == "contra"        # (b)
assert kind(r"(p \wedge q) \to \neg p") == "sat"                            # (c)
f = L.parse(r"(p \wedge q) \to \neg p")
assert not L.val(f, {"p": True, "q": True}) and all(L.val(f, {"p": False, "q": q}) for q in (True, False))
gam = [r"p \vee q", r"\neg p", r"\neg q"]
assert not [r for r in L.rows("pq") if all(L.val(L.parse(g), r) for g in gam)]  # (d)
assert not L.entails([r"p \to q"], r"\neg p \vee q")                       # (e)
assert (True, False) in [L.tv(r, "p", "q") for r in L.entails([r"p \vee q"], r"p \wedge q")]  # (f)
assert not L.entails([r"\bot"], "p") and not L.entails(["p"], r"q \to p")  # (g), (h)
assert L.equivalent(r"\neg(p \to q)", r"p \wedge \neg q")                 # (i)
assert [L.tv(r, "p", "q") for r in L.rows("pq") if L.val(L.parse(r"p \wedge \neg q"), r)] == [(True, False)]


def rel(a, b, names="pq"):
    A, B = L.parse(a), L.parse(b)
    both_t = any(L.val(A, r) and L.val(B, r) for r in L.rows(names))
    both_f = any(not L.val(A, r) and not L.val(B, r) for r in L.rows(names))
    if not both_t and not both_f: return "contradictory"
    if not both_t: return "contrary"
    if not both_f: return "subcontrary"
    return "none"


assert rel(r"p \wedge q", r"\neg p \vee \neg q") == "contradictory"        # (j)
assert rel(r"p \wedge \neg q", "q") == "contrary"                            # (k)
assert not L.val(L.parse(r"p \wedge \neg q"), {"p": False, "q": False})
assert kind(r"\neg((p \to q) \leftrightarrow (\neg q \to \neg p))") == "contra"   # (l)
# Quick checks
assert not L.entails([r"p \wedge q"], r"p \vee r")
ref = [L.tv(r, "p", "q", "r") for r in L.entails([r"p \vee r"], r"p \wedge q")]
assert (False, True, True) in ref and (False, False, True) in ref
assert kind(r"(q \to r) \vee \neg(q \to r)") == "taut" and not L.equivalent(r"q \to r", "p")
print("exr-entailment-and-equivalence-a1: all quoted values check")
