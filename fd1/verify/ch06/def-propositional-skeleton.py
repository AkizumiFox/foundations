"""def-propositional-skeleton and the TAUT verdicts of Section 6.3 (main line and A1),
by explicit truth tables over the skeletons quoted in the text."""
from _tt import entails, satisfiable, imp
# the example skeleton p -> (q or not p) (not asked to be a tautology; check it is not one)
assert not entails("pq", [], lambda v: imp(v["p"], v["q"] or not v["p"]))
# TAUT examples
assert entails("pq", [lambda v: not (v["p"] and v["q"]), lambda v: v["q"]], lambda v: not v["p"])
assert entails("pr", [lambda v: imp(v["p"], v["r"]), lambda v: not v["r"]], lambda v: not v["p"])
# non-examples: p |/= q; x = x is one atom, not a tautology
assert not entails("pq", [lambda v: v["p"]], lambda v: v["q"])
assert not entails("p", [], lambda v: v["p"])
# Quick check: (a) yes; (b) two atoms, no; (c) not p |/= q
assert entails("pq", [lambda v: v["p"] and v["q"]], lambda v: v["q"] and v["p"])
assert not entails("pq", [lambda v: v["p"]], lambda v: v["q"])
assert not entails("pq", [lambda v: not v["p"]], lambda v: v["q"])
# Not allowed: s = t, P(s) to P(t): p, q |/= r
assert not entails("pqr", [lambda v: v["p"], lambda v: v["q"]], lambda v: v["r"])
# A1 (a): not p or (q and p) is not a tautology; refuted at p true, q false
f = lambda v: (not v["p"]) or (v["q"] and v["p"])
assert not entails("pq", [], f) and not f({"p": True, "q": False})
# A1 (b): p and not q is satisfiable, so no TAUT step to bot
assert satisfiable("pq", [lambda v: v["p"] and not v["q"]])
# A1 (c): (i) yes, (ii) no, (iii) yes
assert entails("pq", [lambda v: v["p"], lambda v: imp(v["p"], v["q"])], lambda v: v["q"])
assert not entails("pqr", [lambda v: v["p"], lambda v: v["q"]], lambda v: v["r"])
assert entails("p", [lambda v: not (not v["p"])], lambda v: v["p"])
print("def-propositional-skeleton: all quoted verdicts check")
