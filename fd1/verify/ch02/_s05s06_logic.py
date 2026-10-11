"""Shared helpers for the Chapter 2, sections 05-06 sidecars (not a sidecar itself).

Formulas are nested tuples: ("var", "P"), ("not", A), ("and", A, B), ("or", A, B),
("imp", A, B), ("iff", A, B), ("bot",). Three semantics:
  * classical truth tables (two values);
  * Goedel's three-valued logic G3 (values 0, 1/2, 1), sound for every primitive rule
    of the book except RAA;
  * Kripke models (finite rooted partial orders, monotone valuations), sound for every
    primitive rule except RAA.
A sequent refuted by G3 or by a Kripke model has no derivation without RAA.
"""
from fractions import Fraction
from itertools import product, combinations


def V(n):
    return ("var", n)


def Not(a):
    return ("not", a)


def And(a, b):
    return ("and", a, b)


def Or(a, b):
    return ("or", a, b)


def Imp(a, b):
    return ("imp", a, b)


def Iff(a, b):
    return ("iff", a, b)


BOT = ("bot",)


def letters(f, acc=None):
    acc = set() if acc is None else acc
    if f[0] == "var":
        acc.add(f[1])
    for x in f[1:]:
        if isinstance(x, tuple):
            letters(x, acc)
    return acc


def tv(f, v):
    """Classical truth value of f under the assignment v (dict letter -> bool)."""
    k = f[0]
    if k == "var":
        return v[f[1]]
    if k == "bot":
        return False
    if k == "not":
        return not tv(f[1], v)
    a, b = tv(f[1], v), tv(f[2], v)
    return {"and": a and b, "or": a or b, "imp": (not a) or b, "iff": a == b}[k]


def classically_valid(prem, concl):
    ls = sorted(set().union(*(letters(f) for f in prem + [concl])))
    for vals in product([False, True], repeat=len(ls)):
        v = dict(zip(ls, vals))
        if all(tv(p, v) for p in prem) and not tv(concl, v):
            return False
    return True


HALF = Fraction(1, 2)


def g3(f, v):
    k = f[0]
    if k == "var":
        return v[f[1]]
    if k == "bot":
        return Fraction(0)
    if k == "not":
        return g3(("imp", f[1], BOT), v)
    a, b = g3(f[1], v), g3(f[2], v)
    if k == "and":
        return min(a, b)
    if k == "or":
        return max(a, b)
    if k == "imp":
        return Fraction(1) if a <= b else b
    if k == "iff":
        return min(Fraction(1) if a <= b else b, Fraction(1) if b <= a else a)


def g3_refutation(prem, concl):
    ls = sorted(set().union(*(letters(f) for f in prem + [concl])))
    for vals in product([Fraction(0), HALF, Fraction(1)], repeat=len(ls)):
        v = dict(zip(ls, vals))
        lo = min([g3(p, v) for p in prem], default=Fraction(1))
        if not lo <= g3(concl, v):
            return v
    return None


def posets(n):
    """Rooted partial orders on {0..n-1} with root 0, as sets of pairs (a, b) meaning a <= b."""
    pairs = [(a, b) for a in range(n) for b in range(n) if a != b and b != 0]
    for k in range(len(pairs) + 1):
        for extra in combinations(pairs, k):
            le = {(a, a) for a in range(n)} | {(0, b) for b in range(n)} | set(extra)
            if any((b, a) in le for (a, b) in le if a != b):
                continue
            if any((a, c) not in le for (a, b) in le for (b2, c) in le if b == b2):
                continue
            yield le


def kripke_refutation(prem, concl, max_worlds=3):
    ls = sorted(set().union(*(letters(f) for f in prem + [concl])))
    for n in range(1, max_worlds + 1):
        for le in posets(n):
            up = {w: [u for u in range(n) if (w, u) in le] for w in range(n)}
            upsets = [frozenset(S) for k in range(n + 1) for S in combinations(range(n), k)
                      if all(u in S for w in S for u in up[w])]
            for choice in product(upsets, repeat=len(ls)):
                val = dict(zip(ls, choice))

                def forces(w, f):
                    k = f[0]
                    if k == "var":
                        return w in val[f[1]]
                    if k == "bot":
                        return False
                    if k == "not":
                        return all(not forces(u, f[1]) for u in up[w])
                    if k == "and":
                        return forces(w, f[1]) and forces(w, f[2])
                    if k == "or":
                        return forces(w, f[1]) or forces(w, f[2])
                    if k == "imp":
                        return all((not forces(u, f[1])) or forces(u, f[2]) for u in up[w])
                    if k == "iff":
                        return all(forces(u, f[1]) == forces(u, f[2]) for u in up[w])

                if all(forces(0, p) for p in prem) and not forces(0, concl):
                    return (n, sorted(le), {x: sorted(s) for x, s in val.items()})
    return None


# ---------------------------------------------------------------------------
# Derivations: an independent check of the line counts the text quotes. The
# derivation is written out here (not read from the book) and passed through the
# book's own checker, tools/check_fitch.py.
# ---------------------------------------------------------------------------
import re as _re
import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parents[2] / "tools"))
from check_fitch import check_text as _check_text  # noqa: E402


def check_derivation(body):
    """Check an nd body with tools/check_fitch.py; return (errors, number of lines)."""
    text = ("```{=latex}\n\\begin{center}\n$\\begin{nd}\n" + body
            + "\n\\end{nd}$\n\\end{center}\n```\n")
    errors, notes, counts = _check_text(text)
    n = len(_re.findall(r"\\(?:hypo|have)\s*\{\d+\}", body))
    return errors, n
