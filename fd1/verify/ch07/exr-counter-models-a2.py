"""exr-counter-models-a2 (Section 7.2): all twelve parts."""
import sys, itertools
sys.path.insert(0, "verify/ch07")
from _fo_models import (structure, sat, is_counter_model, all_relations, all_subsets,
                        P, ALL, EX, NOT, AND, OR, IMP)
Px, Qx = P("P", "x"), P("Q", "x")
ab = ["a", "b"]
# (a)
assert is_counter_model([EX("x", NOT(Px))], NOT(EX("x", Px)), structure(ab, pred={"P": {("a",)}}))
# (b) not a counter-model; none on sizes 1..3
assert not is_counter_model([ALL("x", Px)], EX("x", Px), structure(["a"], pred={"P": {("a",)}}))
for n in (1, 2, 3):
    for Ps in all_subsets(range(n)):
        assert not is_counter_model([ALL("x", Px)], EX("x", Px), structure(range(n), pred={"P": Ps}))
# (c) and (l): D = {a}, P empty, Q = {a}
Mc = structure(["a"], pred={"P": set(), "Q": {("a",)}})
assert is_counter_model([ALL("x", IMP(Px, Qx))], ALL("x", IMP(Qx, Px)), Mc)
assert is_counter_model([ALL("x", IMP(Px, Qx)), EX("x", Qx)], EX("x", Px), Mc)
# (d) Z with <, N with > (windows): premise witnesses y - 1, y + 1; no element related to itself
W, N = range(-100, 101), range(0, 200)
assert all((y - 1) < y for y in W) and all(not (x < x) for x in W)
assert all((y + 1) > y for y in N) and all(not (x > x) for x in N)
# (e) only Q = {b} works
good = [Qs for Qs in all_subsets(ab)
        if is_counter_model([ALL("x", OR(Px, Qx))], ALL("x", Qx), structure(ab, pred={"P": {("a",)}, "Q": Qs}))]
assert good == [{("b",)}]
# (f) supersets of {(a, b)}: only {(a, b), (b, a)}
pr = ALL("x", EX("y", P("R", "x", "y"))); cn = EX("y", ALL("x", P("R", "x", "y")))
good = [R for R in all_relations(ab, 2) if ("a", "b") in R and is_counter_model([pr], cn, structure(ab, pred={"R": R}))]
assert good == [{("a", "b"), ("b", "a")}]
# (g), (h) expansions agree with the sentences on every structure on {a, b}
for R in all_relations(ab, 2):
    for Ps in all_subsets(ab):
        M = structure(ab, pred={"R": R, "P": Ps})
        r = lambda x, y: (x, y) in R; p = lambda x: (x,) in Ps
        assert sat(ALL("x", EX("y", P("R", "y", "x"))), M, {}) == ((r("a", "a") or r("b", "a")) and (r("a", "b") or r("b", "b")))
        assert sat(EX("x", AND(Px, ALL("y", P("R", "x", "y")))), M, {}) == \
            ((p("a") and r("a", "a") and r("a", "b")) or (p("b") and r("b", "a") and r("b", "b")))
# (i) skeleton p -> p tautology; (j) skeleton p -> q not
assert all((not p) or p for p in (False, True))
assert not all((not p) or q for p, q in itertools.product((False, True), repeat=2))
# (j) valid on all structures of size <= 2 (0 and + only)
zero = ("c", "0"); plus = lambda s, t: ("f", "+", s, t)
f_j = IMP(ALL("x", ("eq", plus(zero, "x"), "x")), ("eq", plus(zero, zero), zero))
for n in (1, 2):
    D = list(range(n))
    for tab in itertools.product(D, repeat=n * n):
        for z in D:
            M = structure(D, const={"0": z}, func={"+": lambda x, y, tab=tab, n=n: tab[x * n + y]})
            assert sat(f_j, M, {})
# (k) true in N (window); false on {a, b} with x + y read as x
assert all(x + y == y + x for x in range(30) for y in range(30))
Mk = structure(ab, func={"+": lambda x, y: x})
assert not sat(ALL("x", ALL("y", ("eq", plus("x", "y"), plus("y", "x")))), Mk, {})
print("exr-counter-models-a2: all quoted values check")
