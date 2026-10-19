"""exm-satisfiability-search: e v t, e -> f, not(f & t); the open finished branch e, f, not-t;
exactly two satisfying rows (TTF and FFT on e, f, t), realized by 4 and 3; the row e = F,
f = T is no integer's; the satisfiability Quick check (3.2 B4 (a)) closes."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s06_trees import N, check, all_sat_rows  # noqa: E402

QUOTED = {"n for e f not-t": 4, "n for not-e not-f t": 3}

lst = [r"e \vee t", r"e \to f", r"\neg(f \wedge t)"]
tree = N(lst, r"e \vee t", [
    N("e", r"e \to f", [N(r"\neg e", end="x"),
                        N("f", r"\neg(f \wedge t)", [N(r"\neg f", end="x"), N(r"\neg t", end="o")])]),
    N("t", end="u")])
ok, rows = check(tree, "satisfiability")
assert rows == [{"e": True, "f": True, "t": False}]
# the branch t followed to the end
full_t = N("t", r"e \to f", [
    N(r"\neg e", r"\neg(f \wedge t)", [N(r"\neg f", end="o"), N(r"\neg t", end="x")]),
    N("f", r"\neg(f \wedge t)", [N(r"\neg f", end="x"), N(r"\neg t", end="x")])])
tree2 = N(lst, r"e \vee t", [tree["kids"][0], full_t])
ok2, rows2 = check(tree2, "satisfiability, t followed")
assert {tuple(r[a] for a in "eft") for r in rows2} == {(True, True, False), (False, False, True)}
assert set(all_sat_rows(lst, ["e", "f", "t"])) == {(True, True, False), (False, False, True)}


def row(n):
    return (n % 2 == 0, n % 4 == 0, n % 3 == 0)


assert row(QUOTED["n for e f not-t"]) == (True, True, False)
assert row(QUOTED["n for not-e not-f t"]) == (False, False, True)
assert not any(row(n)[0] is False and row(n)[1] for n in range(-200, 201))

# Quick check: p -> q, q -> not p, p is unsatisfiable
qc = N([r"p \to q", r"q \to \neg p", "p"], r"p \to q", [
    N(r"\neg p", end="x"),
    N("q", r"q \to \neg p", [N(r"\neg q", end="x"), N(r"\neg p", end="x")])])
ok3, _ = check(qc, "B4 (a)")
assert ok3
print("exm-satisfiability-search: all quoted values check")
