"""exr-refuting-row-search-c1 (and C3): rules for the not-both connective read off (V7); (b) valid;
(c) p | (p | p) a tautology; the new cases of C3 checked on all rows."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s06_trees import N, check, nand, neg, P, val, rule  # noqa: E402

QUOTED = {"(b)": "valid", "(c)": "tautology"}
p, q = P("p"), P("q")
# (a): the rules agree with (V7) on all four rows: phi|psi true iff not-phi or not-psi true;
# not(phi|psi) true iff phi and psi true
for a in (True, False):
    for b in (True, False):
        v = {"p": a, "q": b}
        assert val(nand(p, q), v) == any(all(val(f, v) for f in w) for w in rule(nand(p, q)))
        assert val(neg(nand(p, q)), v) == any(all(val(f, v) for f in w) for w in rule(neg(nand(p, q))))
assert len(rule(neg(nand(p, q)))) == 1 and len(rule(nand(p, q))) == 2
tb = N([nand(p, q), p, P(r"\neg\neg q")], r"\neg\neg q", [
    N(q, nand(p, q), [N(P(r"\neg p"), end="x"), N(P(r"\neg q"), end="x")])])
assert check(tb, "C1 (b)")[0]
f = nand(p, nand(p, p))
tc = N([neg(f)], neg(f), [N([p, nand(p, p)], nand(p, p), [N(P(r"\neg p"), end="x"), N(P(r"\neg p"), end="x")])])
assert check(tc, "C1 (c)")[0]
assert all(val(f, {"p": a}) for a in (True, False))
assert all(val(nand(p, p), {"p": a}) == (not a) for a in (True, False))
print("exr-refuting-row-search-c1: all quoted values check")
