"""exr-refuting-row-search-b2: the five-claim list is unsatisfiable (closed tree); dropping (4)
gives the branch s, f, t and n = 12; dropping (1) gives s, not-f, t and n = 6."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s06_trees import N, check, all_sat_rows  # noqa: E402

QUOTED = {"drop 4": 12, "drop 1": 6}
c = {1: r"s \to f", 2: r"s \vee o", 3: r"\neg o", 4: r"f \to \neg t", 5: r"s \to t"}
lst = [c[i] for i in range(1, 6)]
t = N(lst, r"s \vee o", [
    N("s", r"s \to f", [N(r"\neg s", end="x"),
                        N("f", r"f \to \neg t", [N(r"\neg f", end="x"),
                                                 N(r"\neg t", r"s \to t", [N(r"\neg s", end="x"), N("t", end="x")])])]),
    N("o", end="x")])
assert check(t, "(a)")[0]
t4 = N([c[1], c[2], c[3], c[5]], r"s \vee o", [
    N("s", r"s \to f", [N(r"\neg s", end="x"),
                        N("f", r"s \to t", [N(r"\neg s", end="x"), N("t", end="o")])]),
    N("o", end="x")])
assert check(t4, "drop 4")[1] == [{"s": True, "f": True, "o": False, "t": True}]
t1 = N([c[2], c[3], c[4], c[5]], r"s \vee o", [
    N("s", r"f \to \neg t", [N(r"\neg f", r"s \to t", [N(r"\neg s", end="x"), N("t", end="o")]),
                             N(r"\neg t", end="u")]),
    N("o", end="x")])
assert check(t1, "drop 1")[1] == [{"s": True, "f": False, "o": False, "t": True}]


def row(n):
    return {"s": n % 6 == 0, "f": n % 4 == 0, "o": n % 2 == 1, "t": n % 3 == 0}


def holds(n, keys):
    from _s06_trees import val, P
    return all(val(P(c[k]), row(n)) for k in keys)


assert holds(QUOTED["drop 4"], [1, 2, 3, 5]) and holds(QUOTED["drop 1"], [2, 3, 4, 5])
assert not any(holds(n, [1, 2, 3, 4, 5]) for n in range(-500, 501))
assert all_sat_rows(lst, ["s", "f", "o", "t"]) == []
print("exr-refuting-row-search-b2: all quoted values check")
