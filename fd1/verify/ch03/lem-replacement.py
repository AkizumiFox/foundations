"""lem-replacement (Section 3.4): the chain p -> not(q and not r) == p -> (not q or not not r)
== p -> (not q or r) == not p or (not q or r); the warning's row p = T, q = F."""
import sys
sys.path.insert(0, "verify/ch03")
import _logic as L

QUOTED = {"chain holds": True}
chain = [r"p \to \neg(q \wedge \neg r)", r"p \to (\neg q \vee \neg\neg r)",
         r"p \to (\neg q \vee r)", r"\neg p \vee (\neg q \vee r)"]
assert all(L.equivalent(a, b) for a, b in zip(chain, chain[1:])) is QUOTED["chain holds"]
x = {"p": True, "q": False}
assert L.val(L.parse(r"\neg(p \wedge q)"), x) and not L.val(L.parse(r"\neg p"), x)
assert not L.entails([r"p \wedge q"], "p")
print("lem-replacement: all quoted values check")
