"""exr-derived-rules-b4 (Ch 2, Section 2.3): (a)-(c) valid by truth table, the MPT look-alike
broken at x = 0; (d) the premises (multiples of 4 are even, multiples of 9 are multiples
of 3) and the conclusion on a range of integers, and the instance n = 7."""
from fractions import Fraction
# helpers: formulas as nested tuples, classical truth tables, a grid of rationals
from fractions import Fraction
from itertools import product


def V(n): return ("var", n)
def Not(a): return ("not", a)
def And(a, b): return ("and", a, b)
def Or(a, b): return ("or", a, b)
def Imp(a, b): return ("imp", a, b)


def letters(f, acc=None):
    acc = set() if acc is None else acc
    if f[0] == "var":
        acc.add(f[1])
    for x in f[1:]:
        if isinstance(x, tuple):
            letters(x, acc)
    return acc


def tv(f, v):
    op = f[0]
    if op == "var":
        return v[f[1]]
    if op == "not":
        return not tv(f[1], v)
    a, b = tv(f[1], v), tv(f[2], v)
    return {"and": a and b, "or": a or b, "imp": (not a) or b}[op]


def classically_valid(prem, concl):
    ls = set()
    for f in prem + [concl]:
        letters(f, ls)
    ls = sorted(ls)
    for vals in product([False, True], repeat=len(ls)):
        v = dict(zip(ls, vals))
        if all(tv(p, v) for p in prem) and not tv(concl, v):
            return False
    return True


def grid(lo=-20, hi=20, den=8):
    return [Fraction(k, den) for k in range(lo * den, hi * den + 1)]


def counterexample_set_true(prem, concl, v):
    return all(tv(p, v) for p in prem) and not tv(concl, v)

P, Q, R, S = V("P"), V("Q"), V("R"), V("S")
QUOTED = {"look-alike x": 0, "instance n": 7}
assert classically_valid([And(Imp(P, R), Imp(Q, R)), Or(P, Q)], R)                      # (a)
assert classically_valid([And(Imp(P, R), Imp(Q, S)), Or(Not(R), Not(S))], Or(Not(P), Not(Q)))  # (b)
assert classically_valid([Not(And(P, Q))], Imp(P, Not(Q)))                             # (c)
assert not classically_valid([Not(And(P, Q)), Not(P)], Q)                              # look-alike
x = Fraction(QUOTED["look-alike x"])
assert counterexample_set_true([Not(And(P, Q)), Not(P)], Q, {"P": x > 5, "Q": x > 3})
for n in range(-500, 501):
    F, E, N, T = n % 4 == 0, n % 2 == 0, n % 9 == 0, n % 3 == 0
    assert (not F or E) and (not N or T)
    if (not E) or (not T):
        assert (not F) or (not N)
n = QUOTED["instance n"]
assert n % 2 == 1 and n % 4 != 0
print("exr-derived-rules-b4: all verdicts and witnesses check")
