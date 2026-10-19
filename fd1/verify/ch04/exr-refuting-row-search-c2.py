"""exr-refuting-row-search-c2: (a) closes, (b) open with the row p T, q F, r T."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import _logic as L  # noqa: E402
from _s06_trees import N, check  # noqa: E402

QUOTED = {"(b) row": {"p": True, "q": False, "r": True}}
ta = N([r"p \to (q \vee r)", r"\neg r", r"\neg(p \to q)"], r"\neg(p \to q)", [
    N(["p", r"\neg q"], r"p \to (q \vee r)", [
        N(r"\neg p", end="x"),
        N(r"q \vee r", r"q \vee r", [N("q", end="x"), N("r", end="x")])])])
assert check(ta, "(a)")[0] and not L.entails([r"p \to (q \vee r)", r"\neg r"], r"p \to q")
tb = N([r"p \vee q", r"p \to r", r"\neg(q \vee \neg r)"], r"\neg(q \vee \neg r)", [
    N([r"\neg q", r"\neg\neg r"], r"\neg\neg r", [
        N("r", r"p \vee q", [
            N("p", r"p \to r", [N(r"\neg p", end="x"), N("r", end="o")]),
            N("q", end="x")])])])
ok, rows = check(tb, "(b)")
assert rows == [QUOTED["(b) row"]] and QUOTED["(b) row"] in L.entails([r"p \vee q", r"p \to r"], r"q \vee \neg r")
print("exr-refuting-row-search-c2: all quoted values check")
