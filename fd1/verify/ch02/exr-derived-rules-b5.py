"""exr-derived-rules-b5 (Ch 2, Section 2.3): derive or break. Each verdict by truth table
(derive: valid; break: invalid), and each break at its stated value of x makes the
counterexample set true; for (g) and (h) the premises said to hold for every x hold on a grid."""
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
CLAIMS = {
    "a": ([Or(P, Q), Q], Not(P), "break"),
    "b": ([Imp(Or(P, R), Not(Q)), Q], Not(R), "derive"),
    "c": ([Imp(Not(P), Q)], Imp(Not(Q), Not(P)), "break"),
    "d": ([Or(P, And(Q, R)), Not(P)], R, "derive"),
    "e": ([Imp(And(P, Q), R), Not(R), P], Not(Q), "derive"),
    "f": ([Imp(P, Or(Q, R)), Not(Q)], Imp(P, R), "derive"),
    "g": ([Imp(P, Or(Q, R)), Not(Q)], R, "break"),
    "h": ([And(Imp(P, Q), Imp(R, S)), Or(Not(Q), Not(S))], And(Not(P), Not(R)), "break"),
}
QUOTED = {"a": 2, "c": 1, "g": 0, "h": 1}
STATEMENTS = {
    "a": {"P": lambda x: x > 0, "Q": lambda x: x > 1},
    "c": {"P": lambda x: x > 0, "Q": lambda x: x > 5},
    "g": {"P": lambda x: x > 5, "Q": lambda x: x > 3, "R": lambda x: x > 4},
    "h": {"P": lambda x: x > 5, "Q": lambda x: x > 9, "R": lambda x: x > 0, "S": lambda x: x > -1},
}
for k, (prem, concl, verdict) in CLAIMS.items():
    assert classically_valid(prem, concl) == (verdict == "derive"), k
for k, x in QUOTED.items():
    prem, concl, _ = CLAIMS[k]
    v = {n: f(Fraction(x)) for n, f in STATEMENTS[k].items()}
    assert counterexample_set_true(prem, concl, v), k
imp = lambda a, b: (not a) or b
assert all(imp(t > 5, t > 3 or t > 4) for t in grid())          # (g) premise for every x
assert all(imp(t > 0, t > -1) for t in grid())                  # (h) R -> S for every x
print("exr-derived-rules-b5: all verdicts and witnesses check")
