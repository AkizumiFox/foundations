"""Search-tree checker for Section 4.6 (def-search-tree, prp-search-decides).

A tree is given as nested dicts:
    {"f": [formulas on this node], "use": formula whose rule makes the children,
     "kids": [child nodes], "end": "x" (closed) | "o" (open, finished) | "u" (left unfollowed)}
Formulas are the book's LaTeX strings (parsed by _logic.parse) or tuples built with
the helpers below (the tuple ("nand", a, b) is the connective | of 4.5 C1 and 4.6 C1, C3).
The drawings stack a one-way node under its parent; here it is a node of its own.

check(tree) verifies: each "use" formula is on the branch, is not a literal, and is not yet
used on that branch; the children carry exactly the formulas of its rule (one way or two
ways); nothing is added below a closed branch; every leaf marked "x" holds a clash; every
leaf marked "o" is open and finished and its row v_B (atoms on B true, all others false)
makes every formula on the branch, the root's included, true. It returns
(all_closed, [rows of open finished branches]), and it cross-checks the verdict against a
truth table of the root list.
"""
import itertools
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _logic as L  # noqa: E402


def P(f):
    return L.parse(f) if isinstance(f, str) else f


def neg(a):
    return ("not", a)


def nand(a, b):
    return ("nand", P(a), P(b))


def val(f, v):
    if f[0] == "nand":
        return not (val(f[1], v) and val(f[2], v))
    if f[0] == "not":
        return not val(f[1], v)
    if f[0] in ("&", "|", ">", "="):
        a, b = val(f[1], v), val(f[2], v)
        return {"&": a and b, "|": a or b, ">": (not a) or b, "=": a == b}[f[0]]
    return L.val(f, v)


def atoms(f):
    if f[0] == "atom":
        return {f[1]}
    if f[0] == "bot":
        return set()
    return set().union(*(atoms(g) for g in f[1:]))


def literal(f):
    if f[0] in ("atom", "bot"):
        return True
    return f[0] == "not" and f[1][0] in ("atom", "bot")


def rule(f):
    """The ways of f, as a list of lists (one list: one way; two lists: a split)."""
    k = f[0]
    if k == "&":
        return [[f[1], f[2]]]
    if k == "|":
        return [[f[1]], [f[2]]]
    if k == ">":
        return [[neg(f[1])], [f[2]]]
    if k == "=":
        return [[f[1], f[2]], [neg(f[1]), neg(f[2])]]
    if k == "nand":
        return [[neg(f[1])], [neg(f[2])]]
    assert k == "not", f
    g = f[1]
    if g[0] == "not":
        return [[g[1]]]
    if g[0] == "|":
        return [[neg(g[1]), neg(g[2])]]
    if g[0] == ">":
        return [[g[1], neg(g[2])]]
    if g[0] == "&":
        return [[neg(g[1])], [neg(g[2])]]
    if g[0] == "=":
        return [[g[1], neg(g[2])], [neg(g[1]), g[2]]]
    if g[0] == "nand":
        return [[g[1], g[2]]]
    raise ValueError(f)


def closed(branch):
    return ("bot",) in branch or any(neg(f) in branch for f in branch)


def check(tree, name=""):
    root = [P(f) for f in tree["f"]]
    names = sorted(set().union(*(atoms(f) for f in root)))
    open_rows, leaves = [], []

    def walk(node, branch, used):
        branch = branch | {P(f) for f in node["f"]}
        kids = node.get("kids", [])
        if closed(branch):
            assert not kids and node.get("end") == "x", (name, "closed branch not ended", node["f"])
            leaves.append("x")
            return
        if not kids:
            end = node.get("end")
            assert end in ("o", "u"), (name, "open leaf must be marked o or u", node["f"])
            leaves.append(end)
            if end == "o":
                for f in branch:
                    assert literal(f) or f in used, (name, "unfinished branch marked o", f)
                v = {a: (("atom", a) in branch) for a in
                     sorted(set(names) | set().union(*(atoms(f) for f in branch)))}
                for f in branch:
                    assert val(f, v), (name, "row fails on branch formula", f)
                open_rows.append({a: v[a] for a in names})
            return
        u = P(node["use"])
        assert u in branch and not literal(u) and u not in used, (name, "bad use", node["use"])
        ways = rule(u)
        assert len(kids) == len(ways), (name, "wrong number of children for", node["use"])
        for kid, way in zip(kids, ways):
            assert {P(f) for f in kid["f"]} == set(way), (name, "child is not the rule's output", node["use"])
            walk(kid, branch, used | {u})

    walk(tree, frozenset(), frozenset())
    all_closed = all(x == "x" for x in leaves)
    sat = [r for r in L.rows(names) if all(val(f, r) for f in root)]
    if all_closed:
        assert not sat, (name, "tree closed but the list is satisfiable")
    if "o" in leaves:
        assert sat, (name, "open finished branch but the list is unsatisfiable")
    return all_closed, open_rows


def N(f, use=None, kids=None, end=None):
    d = {"f": f if isinstance(f, list) else [f]}
    if use is not None:
        d["use"] = use
    if kids:
        d["kids"] = kids
    if end:
        d["end"] = end
    return d


def text():
    return (Path(__file__).resolve().parents[2] /
            "src/ch04-semantics-soundness-completeness/06-refuting-row-search.md").read_text()


def all_sat_rows(fs, names):
    fs = [P(f) for f in fs]
    return [tuple(r[n] for n in names) for r in L.rows(names) if all(val(f, r) for f in fs)]


if __name__ == "__main__":
    # self-test: a tree that must be rejected (a branch marked open that holds a clash)
    bad = N([r"p \vee q", r"\neg p"], r"p \vee q", [N("p", end="o"), N("q", end="o")])
    try:
        check(bad, "self-test")
    except AssertionError:
        print("_s06_trees: checker rejects a wrongly marked tree; ok")
    else:
        raise SystemExit("checker accepted a bad tree")
