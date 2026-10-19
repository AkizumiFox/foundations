"""Section 4.6 'The withheld verdicts': the four searches of 3.2 B3 (a), (d), (f), (g) through
the tree checker; each row refutes its claim and is the row of 3.2's break at the stated x."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import _logic as L  # noqa: E402
from _s06_trees import N, check  # noqa: E402

QUOTED = {
    "a": {"p": False, "q": True},
    "d": {"p": False, "q": True, "r": False},
    "f": {"p": True, "q": False, "r": False},
    "g": {"p": True, "q": True},
}

ta = N([r"\neg p \vee \neg q", r"\neg\neg(p \vee q)"], r"\neg\neg(p \vee q)", [
    N(r"p \vee q", r"\neg p \vee \neg q", [
        N(r"\neg p", r"p \vee q", [N("p", end="x"), N("q", end="o")]),
        N(r"\neg q", end="u")])])
td = N([r"p \to q", r"\neg p \to (r \vee q)", r"\neg r", r"\neg p"], r"p \to q", [
    N(r"\neg p", r"\neg p \to (r \vee q)", [
        N(r"\neg\neg p", end="x"),
        N(r"r \vee q", r"r \vee q", [N("r", end="x"), N("q", end="o")])]),
    N("q", end="u")])
tf = N([r"(p \to q) \to r", r"\neg r", r"\neg q"], r"(p \to q) \to r", [
    N(r"\neg(p \to q)", r"\neg(p \to q)", [N(["p", r"\neg q"], end="o")]),
    N("r", end="x")])
tg = N([r"p \vee q", "p", r"\neg\neg q"], r"\neg\neg q", [
    N("q", r"p \vee q", [N("p", end="o"), N("q", end="o")])])

claims = {"a": ([r"\neg p \vee \neg q"], r"\neg(p \vee q)", ta),
          "d": ([r"p \to q", r"\neg p \to (r \vee q)", r"\neg r"], "p", td),
          "f": ([r"(p \to q) \to r", r"\neg r"], "q", tf),
          "g": ([r"p \vee q", "p"], r"\neg q", tg)}
for k, (prem, concl, t) in claims.items():
    ok, rows = check(t, k)
    assert not ok and QUOTED[k] in rows, (k, rows)
    assert QUOTED[k] in L.entails(prem, concl), k

# 3.2 B3's statements about x at the stated value
x_rows = {"a": ({"p": lambda x: x > 2, "q": lambda x: x > 0}, 1),
          "d": ({"p": lambda x: x > 5, "q": lambda x: x > 0, "r": lambda x: x > 10}, 1),
          "f": ({"p": lambda x: x > 0, "q": lambda x: x > 2, "r": lambda x: x > 3}, 1),
          "g": ({"p": lambda x: x > 1, "q": lambda x: x > 2}, 3)}
for k, (st, x) in x_rows.items():
    assert {a: f(x) for a, f in st.items()} == QUOTED[k], k
print("_s06_withheld: all quoted values check")
