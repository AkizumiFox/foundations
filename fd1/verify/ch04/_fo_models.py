"""Shared helper for the Section 4.11 and 4.12 sidecars: a small evaluator of first-order
formulas in FINITE structures, written independently of tools/check_fitch.py.

Formulas are nested tuples:
    ("P", "R", t1, ..., tn)   predicate R applied to terms
    ("eq", t1, t2)            equation
    ("bot",)
    ("not", f), ("and", f, g), ("or", f, g), ("imp", f, g), ("iff", f, g)
    ("all", "x", f), ("ex", "x", f)
Terms: a string is a variable; ("c", name) a constant; ("f", name, t1, ..., tn).
A structure is a dict with keys D (list), const (dict), func (dict name -> callable),
pred (dict name -> set of tuples)."""
import itertools


def val(t, M, l):
    if isinstance(t, str):
        return l[t]
    if t[0] == "c":
        return M["const"][t[1]]
    if t[0] == "f":
        return M["func"][t[1]](*[val(s, M, l) for s in t[2:]])
    raise ValueError(t)


def sat(f, M, l):
    op = f[0]
    if op == "P":
        return tuple(val(t, M, l) for t in f[2:]) in M["pred"][f[1]]
    if op == "eq":
        return val(f[1], M, l) == val(f[2], M, l)
    if op == "bot":
        return False
    if op == "not":
        return not sat(f[1], M, l)
    if op == "and":
        return sat(f[1], M, l) and sat(f[2], M, l)
    if op == "or":
        return sat(f[1], M, l) or sat(f[2], M, l)
    if op == "imp":
        return (not sat(f[1], M, l)) or sat(f[2], M, l)
    if op == "iff":
        return sat(f[1], M, l) == sat(f[2], M, l)
    if op in ("all", "ex"):
        x, body = f[1], f[2]
        vals = (sat(body, M, {**l, x: d}) for d in M["D"])
        return all(vals) if op == "all" else any(vals)
    raise ValueError(f)


def structure(D, const=None, func=None, pred=None):
    return {"D": list(D), "const": const or {}, "func": func or {}, "pred": pred or {}}


def is_counter_model(prem, concl, M, l=None):
    l = l or {}
    return all(sat(p, M, l) for p in prem) and not sat(concl, M, l)


def all_relations(D, arity):
    tuples = list(itertools.product(D, repeat=arity))
    for bits in itertools.product([False, True], repeat=len(tuples)):
        yield {t for t, b in zip(tuples, bits) if b}


def all_subsets(D):
    D = list(D)
    for bits in itertools.product([False, True], repeat=len(D)):
        yield {(d,) for d, b in zip(D, bits) if b}


# shorthands
def P(name, *ts):
    return ("P", name) + ts


def ALL(x, f):
    return ("all", x, f)


def EX(x, f):
    return ("ex", x, f)


def NOT(f):
    return ("not", f)


def AND(f, g):
    return ("and", f, g)


def OR(f, g):
    return ("or", f, g)


def IMP(f, g):
    return ("imp", f, g)
