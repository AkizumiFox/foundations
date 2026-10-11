"""exr-entailment-and-equivalence-a1 (Section 3.4)."""
import sys
sys.path.insert(0, "verify/ch03")
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
print("exr-entailment-and-equivalence-a1: all quoted values check")
