"""Shared helper for the Chapter 3 sidecars: a small propositional evaluator, written
independently of tools/check_fitch.py.

Formulas are parsed from the book's LaTeX: atoms are lowercase letters (p, q, r, s, t, u,
p_1, ...), metavariables \\varphi, \\psi, \\chi are treated as atoms; connectives \\neg,
\\wedge, \\vee, \\to, \\leftrightarrow, \\bot. Precedence: not > and > or > to > iff, with
-> grouped to the right (Chapter 1's conventions)."""
import itertools
import re
from fractions import Fraction

MAC = {r"\neg": "~", r"\wedge": "&", r"\vee": "|", r"\to": ">", r"\leftrightarrow": "=",
       r"\bot": "0", r"\varphi": "PHI", r"\psi": "PSI", r"\chi": "CHI"}


def tokens(s):
    s = re.sub(r"\\[,;:! ]|\\(?:left|right|bigl|bigr|Bigl|Bigr)(?![A-Za-z])", " ", s)
    out, i = [], 0
    while i < len(s):
        c = s[i]
        if c.isspace():
            i += 1
        elif c == "\\":
            m = re.match(r"\\[A-Za-z]+", s[i:])
            out.append(MAC[m.group(0)])
            i += len(m.group(0))
        elif c in "()":
            out.append(c)
            i += 1
        elif c.islower():
            m = re.match(r"[a-z](_\{?\d+\}?)?", s[i:])
            out.append(("atom", m.group(0).replace("{", "").replace("}", "")))
            i += len(m.group(0))
        else:
            raise ValueError(f"unexpected {c!r} in {s!r}")
    return [("atom", t) if t in ("PHI", "PSI", "CHI") else t for t in out]


PREC = {"=": (1, True), ">": (2, True), "|": (3, False), "&": (4, False)}


def parse(s):
    toks = tokens(s)
    pos = 0

    def unary():
        nonlocal pos
        t = toks[pos]
        if t == "~":
            pos += 1
            return ("not", unary())
        if t == "0":
            pos += 1
            return ("bot",)
        if isinstance(t, tuple):
            pos += 1
            return t
        if t == "(":
            pos += 1
            f = binary(0)
            assert toks[pos] == ")"
            pos += 1
            return f
        raise ValueError(f"bad token {t!r} in {s!r}")

    def binary(mp):
        nonlocal pos
        left = unary()
        while pos < len(toks) and toks[pos] in PREC and PREC[toks[pos]][0] >= mp:
            op = toks[pos]
            prec, right = PREC[op]
            pos += 1
            left = (op, left, binary(prec if right else prec + 1))
        return left

    f = binary(0)
    assert pos == len(toks), s
    return f


def atoms(f):
    if f[0] == "atom":
        return {f[1]}
    if f[0] == "bot":
        return set()
    return set().union(*(atoms(g) for g in f[1:]))


def val(f, v):
    """Two-valued: v maps atom names to True/False."""
    k = f[0]
    if k == "atom":
        return v[f[1]]
    if k == "bot":
        return False
    if k == "not":
        return not val(f[1], v)
    a, b = val(f[1], v), val(f[2], v)
    return {"&": a and b, "|": a or b, ">": (not a) or b, "=": a == b}[k]


def rows(names):
    """All rows over names, T first, the last atom alternating fastest."""
    for bits in itertools.product([True, False], repeat=len(names)):
        yield dict(zip(names, bits))


def entails(premises, concl):
    """Return the list of refuting rows (empty iff the entailment holds)."""
    fs = [parse(p) for p in premises]
    g = parse(concl)
    names = sorted(set().union(atoms(g), *(atoms(f) for f in fs)))
    return [r for r in rows(names) if all(val(f, r) for f in fs) and not val(g, r)]


def false_rows(formula):
    return entails([], formula)


def equivalent(a, b):
    return not entails([a], b) and not entails([b], a)


def tv(r, *names):
    return tuple(r[n] for n in names)


HALF = Fraction(1, 2)
THREE = (Fraction(0), HALF, Fraction(1))


def imp3(a, b):
    return Fraction(1) if a <= b else b


def val3(f, u):
    k = f[0]
    if k == "atom":
        return u[f[1]]
    if k == "bot":
        return Fraction(0)
    if k == "not":
        return imp3(val3(f[1], u), Fraction(0))
    a, b = val3(f[1], u), val3(f[2], u)
    return {"&": min(a, b), "|": max(a, b), ">": imp3(a, b),
            "=": min(imp3(a, b), imp3(b, a))}[k]


# ---- truth tables printed in a section file -------------------------------------------

TV = re.compile(r"^\\mathrm\{([TF])\}$")


def tables_in(path):
    """Yield (header formulas, rows of booleans) for every T/F array in the file."""
    text = open(path, encoding="utf-8").read()
    for m in re.finditer(r"\\begin\{array\}\{[^}]*\}(.*?)\\end\{array\}", text, re.S):
        body = m.group(1)
        if "\\hline" not in body:
            continue
        head, rest = body.split("\\hline", 1)
        header = [h.strip() for h in head.strip().rstrip("\\").split("&")]
        data = []
        for r in re.split(r"\\\\", rest):
            r = r.strip()
            if not r:
                continue
            cells = [c.strip() for c in r.split("&")]
            data.append([TV.match(c).group(1) == "T" for c in cells])
        yield header, data


def check_tables(path, expected_count=None):
    """Evaluate every printed table; the first columns that parse as single atoms are the
    inputs. Returns the number of tables checked; raises AssertionError on a wrong entry."""
    n = 0
    for header, data in tables_in(path):
        fs = [parse(h) for h in header]
        inputs = [i for i, f in enumerate(fs) if f[0] == "atom"]
        # inputs must be a prefix of the columns
        assert inputs == list(range(len(inputs))), header
        names = [fs[i][1] for i in inputs]
        # every combination listed exactly once, in the book's order
        assert [tuple(r[:len(names)]) for r in data] == \
            [tuple(x.values()) for x in rows(names)], (header, "row order")
        for r in data:
            assert len(r) == len(header), header
            env = dict(zip(names, r))
            for i, f in enumerate(fs):
                assert val(f, env) == r[i], (path, header[i], env)
        n += 1
    if expected_count is not None:
        assert n == expected_count, (path, n)
    return n
