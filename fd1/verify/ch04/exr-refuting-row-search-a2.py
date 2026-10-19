"""exr-refuting-row-search-a2 (and A1 (a), (b)): the rules (a)-(d), the branches (e)-(g), the
searches (h)-(j), and A1's split formulas and row."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import _logic as L  # noqa: E402
from _s06_trees import N, check, rule, P, closed  # noqa: E402

QUOTED = {"h row": {"p": False, "q": True}, "g row": {"p": True, "q": False}}

S = lambda ways: [set(w) for w in ways]  # noqa: E731
assert S(rule(P(r"\neg(p \vee q)"))) == [{P(r"\neg p"), P(r"\neg q")}]
assert S(rule(P(r"p \to (q \wedge r)"))) == [{P(r"\neg p")}, {P(r"q \wedge r")}]
assert S(rule(P(r"\neg(p \leftrightarrow q)"))) == [{P("p"), P(r"\neg q")}, {P(r"\neg p"), P("q")}]
assert S(rule(P(r"\neg\neg(p \wedge q)"))) == [{P(r"p \wedge q")}]
assert closed({P(f) for f in [r"p \vee q", r"\neg p", r"\neg q", "q"]})
assert not closed({P(f) for f in [r"p \to q", r"\neg q", "p"]})
tf = N([r"p \to q", r"\neg q", "p"], r"p \to q", [N(r"\neg p", end="x"), N("q", end="x")])
assert check(tf, "(f)")[0]
tg = N([r"\neg(p \wedge q)", "p", r"\neg q"], r"\neg(p \wedge q)", [N(r"\neg p", end="x"), N(r"\neg q", end="o")])
assert check(tg, "(g)")[1] == [QUOTED["g row"]]
th = N([r"p \vee q", r"\neg p"], r"p \vee q", [N("p", end="x"), N("q", end="o")])
assert check(th, "(h)")[1] == [QUOTED["h row"]] and QUOTED["h row"] in L.entails([r"p \vee q"], "p")
ti = N([r"p \wedge q", r"\neg(p \vee r)"], r"p \wedge q", [
    N(["p", "q"], r"\neg(p \vee r)", [N([r"\neg p", r"\neg r"], end="x")])])
assert check(ti, "(i)")[0] and not L.entails([r"p \wedge q"], r"p \vee r")
tj = N([r"p \leftrightarrow q", r"q \leftrightarrow \neg p"], r"p \leftrightarrow q", [
    N(["p", "q"], r"q \leftrightarrow \neg p", [N(["q", r"\neg p"], end="x"),
                                               N([r"\neg q", r"\neg\neg p"], end="x")]),
    N([r"\neg p", r"\neg q"], r"q \leftrightarrow \neg p", [
        N(["q", r"\neg p"], end="x"),
        N([r"\neg q", r"\neg\neg p"], end="x")])])
assert check(tj, "(j)")[0]
# (k): not(r -> s) is one way, p v q is two
assert len(rule(P(r"\neg(r \to s)"))) == 1 and len(rule(P(r"p \vee q"))) == 2
# A1 (a): which split
splits = [f for f in [r"p \wedge q", r"\neg(p \wedge q)", r"\neg(p \to q)", r"p \leftrightarrow q", r"\neg\neg p"]
          if len(rule(P(f))) == 2]
assert splits == [r"\neg(p \wedge q)", r"p \leftrightarrow q"]
# A1 (b): branch p -> q (used), not q, not p, r: row p F, q F, r T, and it makes p -> q true
v = {"p": False, "q": False, "r": True}
assert L.val(P(r"p \to q"), v)
print("exr-refuting-row-search-a2: all quoted values check")
