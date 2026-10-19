"""exr-refuting-row-search-b1: verdicts (a), (c) valid; (b), (d) refuted with the stated rows;
each tree through the checker."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import _logic as L  # noqa: E402
from _s06_trees import N, check  # noqa: E402

QUOTED = {"b": {"p": False, "q": True, "r": False, "s": False},
          "d": {"p": False, "q": False, "r": True}}

ta = N([r"p \to q", r"r \to s", r"p \vee r", r"\neg(q \vee s)"], r"\neg(q \vee s)", [
    N([r"\neg q", r"\neg s"], r"p \vee r", [
        N("p", r"p \to q", [N(r"\neg p", end="x"), N("q", end="x")]),
        N("r", r"r \to s", [N(r"\neg r", end="x"), N("s", end="x")])])])
assert check(ta, "(a)")[0] and not L.entails([r"p \to q", r"r \to s", r"p \vee r"], r"q \vee s")

tb = N([r"p \to q", r"r \to s", r"q \vee s", r"\neg(p \vee r)"], r"\neg(p \vee r)", [
    N([r"\neg p", r"\neg r"], r"q \vee s", [
        N("q", r"p \to q", [
            N(r"\neg p", r"r \to s", [N(r"\neg r", end="o"), N("s", end="u")]),
            N("q", end="u")]),
        N("s", end="u")])])
ok, rows = check(tb, "(b)")
assert rows == [QUOTED["b"]] and QUOTED["b"] in L.entails([r"p \to q", r"r \to s", r"q \vee s"], r"p \vee r")

tc = N([r"(p \wedge q) \to r", r"\neg((p \to r) \vee (q \to r))"], r"\neg((p \to r) \vee (q \to r))", [
    N([r"\neg(p \to r)", r"\neg(q \to r)"], r"\neg(p \to r)", [
        N(["p", r"\neg r"], r"\neg(q \to r)", [
            N(["q", r"\neg r"], r"(p \wedge q) \to r", [
                N(r"\neg(p \wedge q)", r"\neg(p \wedge q)", [N(r"\neg p", end="x"), N(r"\neg q", end="x")]),
                N("r", end="x")])])])])
assert check(tc, "(c)")[0] and not L.entails([r"(p \wedge q) \to r"], r"(p \to r) \vee (q \to r)")

td = N([r"p \leftrightarrow q", r"q \vee r", r"\neg(p \vee \neg r)"], r"\neg(p \vee \neg r)", [
    N([r"\neg p", r"\neg\neg r"], r"\neg\neg r", [
        N("r", r"p \leftrightarrow q", [
            N(["p", "q"], end="x"),
            N([r"\neg p", r"\neg q"], r"q \vee r", [N("q", end="x"), N("r", end="o")])])])])
ok, rows = check(td, "(d)")
assert rows == [QUOTED["d"]] and QUOTED["d"] in L.entails([r"p \leftrightarrow q", r"q \vee r"], r"p \vee \neg r")
print("exr-refuting-row-search-b1: all quoted values check")
