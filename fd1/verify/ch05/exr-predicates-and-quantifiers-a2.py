"""exr-predicates-and-quantifiers-a2 (Section 5.1) and the finite worlds of Section 5.1:
world W (Figure W: six readings, its Quick check, the long "and"/"or" and its Quick check),
the building of Figure K (two verdicts, its Quick check), drill parts (a)-(l)."""
from _fo_models import structure, sat, P, ALL, EX, NOT, AND, OR, IMP

QUOTED = {
    "W readings": [True, False, False, True, True, False],
    "W counterexamples to forall P": ["c", "d"], "W witness for exists P": "a",
    "W Quick check": [True, True], "W Quick check witness": "d",
    "long-and false conjunct": "a",
    "K fifth, sixth": [True, False], "K Quick check": True,
    "drill (a)-(d)": [True, True, False, True], "drill (d) true disjunct": "c",
    "drill (i)": False,
}

W = structure("abcd", const={"c": "c"},
              pred={"P": {("a",), ("b",)}, "Q": {("b",), ("c",)},
                    "R": {("a", "b"), ("b", "c"), ("c", "c"), ("d", "a")}})
x, y = "x", "y"
readings = [EX(x, P("P", x)), ALL(x, P("P", x)), ALL(x, OR(P("P", x), P("Q", x))),
            EX(x, AND(P("P", x), P("Q", x))), ALL(x, EX(y, P("R", x, y))),
            EX(y, ALL(x, P("R", x, y)))]
assert [sat(f, W, {}) for f in readings] == QUOTED["W readings"]
assert [d for d in W["D"] if not sat(P("P", x), W, {x: d})] == QUOTED["W counterexamples to forall P"]
assert sat(P("P", x), W, {x: QUOTED["W witness for exists P"]})
# exists y forall x R(x, y) fails: c receives from b and c only
assert {u for u in W["D"] if ("%s" % u, "c") in {(a, b) for a, b in W["pred"]["R"]}} == {"b", "c"}
qc = [ALL(x, IMP(P("Q", x), P("R", x, ("c", "c")))), EX(x, ALL(y, NOT(P("R", y, x))))]
assert [sat(f, W, {}) for f in qc] == QUOTED["W Quick check"]
assert sat(ALL(y, NOT(P("R", y, x))), W, {x: "d"})
assert [d for d in W["D"] if sat(ALL(y, NOT(P("R", y, x))), W, {x: d})] == ["d"]
# long "and": forall x P(x) <-> P(a) & ... & P(d); exists <-> disjunction; De Morgan
conj = all(sat(P("P", x), W, {x: d}) for d in "abcd")
disj = any(sat(P("P", x), W, {x: d}) for d in "abcd")
assert conj == sat(ALL(x, P("P", x)), W, {}) and disj == sat(EX(x, P("P", x)), W, {})
assert (not conj) == any(not sat(P("P", x), W, {x: d}) for d in "abcd")
# second Quick check: P(d) -> Q(d) conjuncts; only the one at a is false
false_conj = [d for d in "abcd" if not sat(IMP(P("P", x), P("Q", x)), W, {x: d})]
assert false_conj == [QUOTED["long-and false conjunct"]]
# drill (a)-(d)
drill = [ALL(x, IMP(P("P", x), EX(y, P("R", x, y)))), EX(x, AND(P("Q", x), NOT(P("P", x)))),
         ALL(x, EX(y, P("R", y, x))), EX(x, P("R", x, x))]
assert [sat(f, W, {}) for f in drill] == QUOTED["drill (a)-(d)"]
assert [d for d in "abcd" if sat(P("R", x, x), W, {x: d})] == [QUOTED["drill (d) true disjunct"]]
assert [d for d in "abcd" if sat(AND(P("Q", x), NOT(P("P", x))), W, {x: d})] == ["c"]

# Figure K
K = structure(["k1", "k2", "l1", "l2"],
              pred={"Key": {("k1",), ("k2",)}, "Lock": {("l1",), ("l2",)},
                    "Opens": {("k1", "l1"), ("k2", "l2")}})
fifth = ALL(y, IMP(P("Lock", y), EX(x, AND(P("Key", x), P("Opens", x, y)))))
sixth = EX(x, AND(P("Key", x), ALL(y, IMP(P("Lock", y), P("Opens", x, y)))))
assert [sat(fifth, K, {}), sat(sixth, K, {})] == QUOTED["K fifth, sixth"]
assert sat(NOT(sixth), K, {}) == QUOTED["K Quick check"]
alt = ALL(x, IMP(P("Key", x), NOT(ALL(y, IMP(P("Lock", y), P("Opens", x, y))))))
assert sat(alt, K, {}) == QUOTED["K Quick check"]
h = EX(y, AND(P("Lock", y), ALL(x, IMP(P("Key", x), P("Opens", x, y)))))
assert sat(h, K, {}) == QUOTED["drill (i)"]
# the slip: exists x (Key(x) -> Opens(x, f)) is true when f is a lock that is no key
Kf = dict(K, const={"f": "l1"})
assert sat(EX(x, IMP(P("Key", x), P("Opens", x, ("c", "f")))), Kf, {})
# sixth implies fifth in every building on up to 3 objects (sanity check)
import itertools
for n in range(1, 4):
    D = list(range(n))
    for keys in itertools.product([0, 1], repeat=n):
        for locks in itertools.product([0, 1], repeat=n):
            pairs = [(a, b) for a in D for b in D]
            for bits in itertools.product([0, 1], repeat=len(pairs)):
                M = structure(D, pred={"Key": {(d,) for d in D if keys[d]},
                                       "Lock": {(d,) for d in D if locks[d]},
                                       "Opens": {p for p, b in zip(pairs, bits) if b}})
                assert (not sat(sixth, M, {})) or sat(fifth, M, {})
# (j)-(l): x + 1 > x; x = y defeats y > x; y = x defeats x < y
for v in range(-50, 51):
    assert v + 1 > v and not (v > v)
print("exr-predicates-and-quantifiers-a2: all quoted values check")
