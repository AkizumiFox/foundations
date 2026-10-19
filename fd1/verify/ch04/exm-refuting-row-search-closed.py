"""exm-refuting-row-search-closed: the closed tree for p->(q v r), q->s, r->s |= p->s, its five
closed branches, the reordering Quick check, and the fold 'A tree is a table with rows merged'
(four candidate rows after p, not-s; all sixteen struck out)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import _logic as L  # noqa: E402
from _s06_trees import N, check  # noqa: E402

QUOTED = {"closed branches": 5, "rows": 16, "candidates after p, not s": 4}

root = [r"p \to (q \vee r)", r"q \to s", r"r \to s", r"\neg(p \to s)"]
tree = N(root, r"\neg(p \to s)", [
    N(["p", r"\neg s"], r"p \to (q \vee r)", [
        N(r"\neg p", end="x"),
        N(r"q \vee r", r"q \vee r", [
            N("q", r"q \to s", [N(r"\neg q", end="x"), N("s", end="x")]),
            N("r", r"r \to s", [N(r"\neg r", end="x"), N("s", end="x")])])])])
ok, rows = check(tree, "closed example")
assert ok and not rows
assert not L.entails(root[:3], r"p \to s")


def count_leaves(t):
    return 1 if not t.get("kids") else sum(count_leaves(k) for k in t["kids"])


assert count_leaves(tree) == QUOTED["closed branches"]
assert 2 ** 4 == QUOTED["rows"]

# reordering Quick check: p -> (q v r) first; the node p, not-s under each open side
re = N(root, r"p \to (q \vee r)", [
    N(r"\neg p", r"\neg(p \to s)", [N(["p", r"\neg s"], end="x")]),
    N(r"q \vee r", r"\neg(p \to s)", [
        N(["p", r"\neg s"], r"q \vee r", [
            N("q", r"q \to s", [N(r"\neg q", end="x"), N("s", end="x")]),
            N("r", r"r \to s", [N(r"\neg r", end="x"), N("s", end="x")])])])])
ok2, _ = check(re, "reordered")
assert ok2

# fold: rows with p T and s F number four; the branch q strikes out those with q T, r strikes the rest
cand = [r for r in L.rows(["p", "q", "r", "s"]) if r["p"] and not r["s"]]
assert len(cand) == QUOTED["candidates after p, not s"]
assert len([r for r in cand if r["q"]]) == 2
# every candidate violates a root formula (so is struck out)
for r in cand:
    assert not all(L.val(L.parse(f), r) for f in root)
print("exm-refuting-row-search-closed: all quoted values check")
