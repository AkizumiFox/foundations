"""exm-refuting-row-search-open: the tree for p->(q v r), q->s |= p->s, its open finished branch
and the row p, r true, q, s false (the Quick check after it)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import _logic as L  # noqa: E402
from _s06_trees import N, check  # noqa: E402

QUOTED = {"row": {"p": True, "q": False, "r": True, "s": False}}

root = [r"p \to (q \vee r)", r"q \to s", r"\neg(p \to s)"]
tree = N(root, r"\neg(p \to s)", [
    N(["p", r"\neg s"], r"p \to (q \vee r)", [
        N(r"\neg p", end="x"),
        N(r"q \vee r", r"q \vee r", [
            N("q", r"q \to s", [N(r"\neg q", end="x"), N("s", end="x")]),
            N("r", r"q \to s", [N(r"\neg q", end="o"), N("s", end="x")])])])])
ok, rows = check(tree, "open example")
assert not ok and rows == [QUOTED["row"]]
ref = L.entails(root[:2], r"p \to s")
assert QUOTED["row"] in ref
print("exm-refuting-row-search-open: all quoted values check")
