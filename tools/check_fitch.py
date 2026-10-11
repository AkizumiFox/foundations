#!/usr/bin/env python3
"""Check every Fitch derivation and every truth table in the book's source.

Part 0 prints derivations as fitch.sty `nd` environments inside raw LaTeX blocks
(syntax in `latex/fitch-book.sty`, conventions in `authoring/NOTATION.md`):

    \\hypo {1} {P \\to Q}
    \\open
    \\hypo {2} {P}
    \\have {3} {Q}  \\ie{1,2}
    \\close
    \\have {4} {P \\to Q} \\ii{2-3}

A derivation is mechanical, so it is checked mechanically. For each `nd` block:

* **labels** are unique and number the lines 1, 2, 3, ... in order;
* **boxes** balance, and each box begins with an assumption (`\\hypo`), except a
  flagged box (`\\open[x_0]`, the eigenvariable box of forall-I, which has none);
  an assumption in the middle of a box is an error;
* **cited lines exist and are available**: earlier, and not inside a box that has
  closed (NOTATION.md: "a line may cite any earlier line not inside a closed box");
* **cited ranges** (`i-j`, for ->I, not-I, RAA, or-E, iff-I) are exactly a closed
  box, first line its assumption and last line its last line, whose enclosing box
  is still open;
* **rule shapes** for the propositional rules (and-I/E, ->I/E, or-I/E, not-I/E,
  bot-E, RAA, iff-I/E, R), at the level of formulas, with a small parser for
  letters (any capital), `\\neg \\wedge \\vee \\to \\leftrightarrow \\bot` and
  parentheses;
* **quantifier and equality rules** (`\\Ae \\Ai \\Ei \\Ee \\eqi \\eqe`), shape and side
  conditions, with a small first-order parser (predicates P(x, y), function symbols
  f(x), + - \\cdot ^, names x, x_0, c, 0, \\varepsilon_0, relations = < \\le \\in ...,
  `\\forall x` / `\\exists x`, binding like \\neg, and bounded `\\forall x \\in A`):
  - forall-E: phi[t/x] from forall x phi, t free for x (no capture);
  - forall-I: a flagged box [x_0] with no assumption ending in phi[x_0/x] gives
    forall x phi; x_0 not in forall x phi, a premise or an open assumption;
  - exists-I: exists x phi from phi[t/x], t free for x;
  - exists-E: from exists x phi (line h) and a flagged box [x_0] assuming phi[x_0/x]
    and ending in chi (a line of the box itself), chi; x_0 not in chi, in
    exists x phi, in a premise or in an open assumption;
  - =I: t = t; =E: from t = s and phi[t/x], phi[s/x] (some occurrences of t
    replaced by s, none under a quantifier on a variable of t or s).
  Bounded forms (Chapter 4 §08) reuse the tags: forall-E and exists-I then cite the
  bound's instance as a second line, and the forall-I / exists-E box assumes it.

fitch.sty's optional arguments are read (fitchdoc.pdf, section 3.6):
`\\have[n][k]{label}{...}` prints the line as n+k (then n+k+1, ...); `\\have[n]` is
`[n][0]`; `\\have[][7]` jumps the count to 7; `\\have[\\ ][0]{}{\\vdots}` prints no
number (a gap row). A guard `\\open[x_0]` (or `\\hypo{l}[x_0]{...}`, `\\guard{x_0}`)
flags the box with the name x_0.
`\\begin{nd}[schema]` (latex/fitch-book.sty's key) prints each label as given. Lines
are cited by their {label}; the numbering check reads the printed numbers, which
must run 1, 2, 3, ..., jumping forward only across a gap row (an unlabelled row or
a `\\vdots` row). A row that would print a stray "+n" (a blank base left by a gap
row, e.g. `\\have[\\ ][0]` followed by a plain `\\have`) is an error.

Skipped, with a note (shown by `--notes`): a `\\vdots` or unlabelled row and a
justification-free line after it, a `\\by{text}{refs}` justification (its refs are
still checked for availability), and any line whose formula (or a cited one)
neither parser can read (a metavariable such as `\\varphi`: shape not checked).

**Markers**, on a line of the raw LaTeX block before `\\begin{nd}` (or on the line
just before the block; with several `nd`s in one block, between the previous
`\\end{nd}` and this one; the nearest marker wins):

* `% expect-invalid` -- a deliberately flawed derivation (a non-example, a "find
  the error" exercise). Its errors are expected: they are not reported, and the
  block is an error only if it checks *clean*.
* `% schema` -- a rule schema or a partial derivation with gap rows, whose lines
  may carry letters (i, j, k) for numbers. Only what is checkable is checked: box
  structure, that cited lines exist and are available, cited ranges, and the rule
  shape of every line whose own formula and cited formulas parse. Lines without a
  justification (given lines, the far end of a gap) and justifications citing
  nothing (a gap still to fill, `\\oe{}`) are notes, not errors. Errors in a
  schema block are reported as usual. `\\begin{nd}[schema]` implies `% schema`.

A block with non-numeric labels and neither marker is an error (mark it).

**Truth tables.** A display `array` whose header row is statement letters and
formulas, and whose rows below `\\hline` are T/F (`\\mathrm{T}`, `\\text{F}`, `T`),
is evaluated: every formula column must agree with the letter columns in every
row. Columns the parser cannot read are skipped with a note.

    python3 tools/check_fitch.py                        # all of src/
    python3 tools/check_fitch.py src/ch01-logic-connectives
    python3 tools/check_fitch.py --notes                # also list what was skipped

Exits 1 on any error. Importable:

    from tools.check_fitch import find_violations, report
    errors, notes = find_violations(Path("src"))
"""
import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import series  # noqa: E402

# ---------------------------------------------------------------------------
# Formulas
# ---------------------------------------------------------------------------

BOT = ("bot",)
OPS = {  # token -> (precedence, right-associative); chains of ∧ and ∨ group to the right (Ch 3 §04)
    "iff": (1, True), "imp": (2, True), "or": (3, True), "and": (4, True),
}
MACROS = {
    r"\neg": "not", r"\lnot": "not", r"\wedge": "and", r"\land": "and",
    r"\vee": "or", r"\lor": "or", r"\to": "imp", r"\rightarrow": "imp",
    r"\leftrightarrow": "iff", r"\iff": "iff", r"\bot": "bot",
}
SPACING = re.compile(r"\\[,;:! ]|\\q?quad(?![A-Za-z])|\\(?:left|right|mathrm|mathit)(?![A-Za-z])")


class ParseError(ValueError):
    pass


def tokenize(text: str) -> list:
    s = SPACING.sub(" ", text)
    s = re.sub(r"\{(\\[A-Za-z]+)\}", r" \1 ", s)   # {\to} -> \to
    tokens = []
    i = 0
    while i < len(s):
        c = s[i]
        if c.isspace():
            i += 1
        elif c in "({":
            tokens.append("(")
            i += 1
        elif c in ")}":
            tokens.append(")")
            i += 1
        elif c == "\\":
            m = re.match(r"\\[A-Za-z]+", s[i:])
            if not m or m.group(0) not in MACROS:
                raise ParseError(f"unknown command {m.group(0) if m else s[i:i+2]}")
            tokens.append(MACROS[m.group(0)])
            i += len(m.group(0))
        elif c.isupper() and c.isalpha():
            if i + 1 < len(s) and (s[i + 1].isalnum() or s[i + 1] in "_^'"):
                raise ParseError(f"not a statement letter near {s[i:i+3]!r}")
            tokens.append(("var", c))
            i += 1
        else:
            raise ParseError(f"unexpected {c!r}")
    return tokens


def parse_formula(text: str):
    """Parse a propositional formula into a tuple tree; raise ParseError."""
    tokens = tokenize(text)
    if not tokens:
        raise ParseError("empty formula")
    pos = 0

    def peek():
        return tokens[pos] if pos < len(tokens) else None

    def unary():
        nonlocal pos
        t = peek()
        if t == "not":
            pos += 1
            return ("not", unary())
        if t == "bot":
            pos += 1
            return BOT
        if isinstance(t, tuple):
            pos += 1
            return t
        if t == "(":
            pos += 1
            inner = binary(0)
            if peek() != ")":
                raise ParseError("unbalanced parentheses")
            pos += 1
            return inner
        raise ParseError(f"unexpected {t!r}")

    def binary(min_prec):
        nonlocal pos
        left = unary()
        while isinstance(peek(), str) and peek() in OPS and OPS[peek()][0] >= min_prec:
            op = peek()
            prec, right_assoc = OPS[op]
            pos += 1
            right = binary(prec if right_assoc else prec + 1)
            left = (op, left, right)
        return left

    tree = binary(0)
    if pos != len(tokens):
        raise ParseError(f"trailing {tokens[pos]!r}")
    return tree


def evaluate(f, env: dict) -> bool:
    k = f[0]
    if k == "var":
        return env[f[1]]
    if k == "bot":
        return False
    if k == "not":
        return not evaluate(f[1], env)
    a, b = evaluate(f[1], env), evaluate(f[2], env)
    return {"and": a and b, "or": a or b, "imp": (not a) or b, "iff": a == b}[k]


def show(f) -> str:
    k = f[0]
    if k == "var":
        return f[1]
    if k == "bot":
        return "⊥"
    if k == "top":
        return "⊤"
    if k == "pred":
        return f"{f[1]}({', '.join(show_term(a) for a in f[2])})"
    if k == "rel":
        return f"{show_term(f[2])} {REL_SYM.get(f[1], f[1])} {show_term(f[3])}"
    if k in ("forall", "exists"):
        q = "∀" if k == "forall" else "∃"
        if f[3] is not None:
            b = f[3]
            if b[0] == "rel" and b[2] == ("v", f[1]):
                return f"{q}{f[1]} {REL_SYM.get(b[1], b[1])} {show_term(b[3])} {show(f[2])}"
            return f"{q}{f[1]} [{show(b)}] {show(f[2])}"
        return f"{q}{f[1]} {show(f[2])}"
    if k == "not":
        return "¬" + (f"({show(f[1])})" if f[1][0] == "rel" else show(f[1]))
    sym = {"and": "∧", "or": "∨", "imp": "→", "iff": "↔"}[k]
    return f"({show(f[1])} {sym} {show(f[2])})"


# ---------------------------------------------------------------------------
# First-order formulas (Chapter 4): terms, predicates, =, quantifiers
# ---------------------------------------------------------------------------
#
# Terms:    ("v", name)                a variable or constant (x, x_0, c, 0, \varepsilon_0)
#           ("app", head, (args...))   f(x), x + y (head "+"), a_n (head "_"), \abs{t}
# Formulas: the propositional trees above, plus
#           ("var", P)                 a statement letter (a 0-ary predicate)
#           ("pred", P, (terms...))    P(x), R(x, y)
#           ("rel", op, s, t)          s = t, s < t, x \in A (op "=", "<", "le", "in", ...)
#           ("forall" | "exists", x, body, bound)
#                                      bound is None, or the formula of a bounded
#                                      quantifier (\forall x \in A, \exists n \ge N)
# `s \ne t` reads as \neg(s = t) and `x \notin A` as \neg(x \in A).

FO_MACROS = {
    r"\neg": ("op", "not"), r"\lnot": ("op", "not"), r"\wedge": ("op", "and"),
    r"\land": ("op", "and"), r"\vee": ("op", "or"), r"\lor": ("op", "or"),
    r"\to": ("op", "imp"), r"\rightarrow": ("op", "imp"), r"\leftrightarrow": ("op", "iff"),
    r"\iff": ("op", "iff"), r"\bot": ("op", "bot"), r"\top": ("op", "top"),
    r"\forall": ("q", "forall"), r"\exists": ("q", "exists"),
    r"\le": ("rel", "le"), r"\leq": ("rel", "le"), r"\leqslant": ("rel", "le"),
    r"\ge": ("rel", "ge"), r"\geq": ("rel", "ge"), r"\geqslant": ("rel", "ge"),
    r"\lt": ("rel", "<"), r"\gt": ("rel", ">"), r"\ne": ("rel", "ne"), r"\neq": ("rel", "ne"),
    r"\in": ("rel", "in"), r"\notin": ("rel", "notin"), r"\subseteq": ("rel", "subseteq"),
    r"\subset": ("rel", "subset"), r"\mid": ("rel", "mid"),
    r"\cdot": ("aop", "*"), r"\times": ("aop", "*"),
    r"\lvert": ("bar",), r"\rvert": ("bar",), r"\vert": ("bar",),
    r"\abs": ("fn", "abs", 1), r"\frac": ("fn", "/", 2), r"\sqrt": ("fn", "sqrt", 1),
}
GREEK = {"alpha", "beta", "gamma", "delta", "epsilon", "varepsilon", "zeta", "eta",
         "iota", "kappa", "lambda", "mu", "nu", "xi", "pi", "rho", "sigma", "tau",
         "omega"}  # not \varphi, \psi, \chi, \theta: formula metavariables
REL_SYM = {"=": "=", "<": "<", ">": ">", "le": "≤", "ge": "≥", "in": "∈",
           "subseteq": "⊆", "subset": "⊂", "mid": "∣"}


def fo_tokenize(text: str) -> list:
    """Tokens of a first-order formula. Never fails: what it cannot read becomes an
    ("unknown", ...) token, which the parser rejects (so names can still be listed)."""
    s = SPACING.sub(" ", text)
    s = re.sub(r"\{(\\[A-Za-z]+)\}", r" \1 ", s)
    s = re.sub(r"\\mathbb\s*\{\s*([A-Z])\s*\}", r"\\n\1", s)
    tokens = []
    i = 0

    def subscript(j):
        """Digits after '_' at j (x_0, x_{12}) -> (suffix, end), else (None, j)."""
        m = re.match(r"_(?:(\d)|\{\s*(\d+)\s*\})", s[j:])
        if m:
            return "_" + (m.group(1) or m.group(2)), j + len(m.group(0))
        return None, j

    while i < len(s):
        c = s[i]
        if c.isspace() or c == ".":
            i += 1
        elif c in "({[":
            tokens.append("(" if c != "[" else ("unknown", "["))
            i += 1
        elif c in ")}":
            tokens.append(")")
            i += 1
        elif c == ",":
            tokens.append(",")
            i += 1
        elif c == "|":
            tokens.append(("bar",))
            i += 1
        elif c in "=<>":
            tokens.append(("rel", c))
            i += 1
        elif c in "+-*/^_":
            tokens.append(("aop", c))
            i += 1
        elif c.isdigit():
            m = re.match(r"\d+", s[i:])
            tokens.append(("name", m.group(0), False))
            i += len(m.group(0))
            if i < len(s) and s[i].isalpha():          # 2a: implicit product
                tokens.append(("aop", "*"))
        elif c == "\\":
            m = re.match(r"\\[A-Za-z]+", s[i:])
            if not m:
                tokens.append(("unknown", s[i:i + 2]))
                i += 2
                continue
            mac = m.group(0)
            i += len(mac)
            if mac in FO_MACROS:
                tokens.append(FO_MACROS[mac])
            elif mac[1:] in GREEK or re.fullmatch(r"\\n[A-Z]z?", mac):
                suf, i = subscript(i)
                while i < len(s) and s[i] == "'":
                    suf, i = (suf or "") + "'", i + 1
                tokens.append(("name", mac + (suf or ""), False))
            else:
                tokens.append(("unknown", mac))
        elif c.isalpha() and c.isascii():
            i += 1
            suf, i = subscript(i)
            while i < len(s) and s[i] == "'":
                suf, i = (suf or "") + "'", i + 1
            tokens.append(("name", c + (suf or ""), c.isupper()))
        else:
            tokens.append(("unknown", c))
            i += 1
    return tokens


def parse_fo(text: str):
    """Parse a first-order formula into a tuple tree; raise ParseError."""
    tokens = fo_tokenize(text)
    if not tokens:
        raise ParseError("empty formula")
    pos = 0

    def peek(k=0):
        return tokens[pos + k] if pos + k < len(tokens) else None

    def kind(t):
        return t[0] if isinstance(t, tuple) else t

    def expect(tok):
        nonlocal pos
        if peek() != tok:
            raise ParseError(f"expected {tok!r}, got {peek()!r}")
        pos += 1

    def binary(min_prec):
        nonlocal pos
        left = unary()
        while kind(peek()) == "op" and peek()[1] in OPS and OPS[peek()[1]][0] >= min_prec:
            op = peek()[1]
            prec, right_assoc = OPS[op]
            pos += 1
            right = binary(prec if right_assoc else prec + 1)
            left = (op, left, right)
        return left

    def unary():
        nonlocal pos
        t = peek()
        if t == ("op", "not"):
            pos += 1
            return ("not", unary())
        if t in (("op", "bot"), ("op", "top")):
            pos += 1
            return (t[1],)
        if kind(t) == "q":
            pos += 1
            v = peek()
            if kind(v) != "name" or v[1][0].isdigit():
                raise ParseError(f"{t[1]} needs a variable, got {v!r}")
            pos += 1
            bound = None
            if kind(peek()) == "rel":
                op = peek()[1]
                pos += 1
                bound = make_rel(op, ("v", v[1]), term())
            return (t[1], v[1], unary(), bound)
        if t == "(":
            save = pos
            try:
                pos += 1
                inner = binary(0)
                expect(")")
                if kind(peek()) not in ("rel", "aop"):
                    return inner
            except ParseError:
                pass
            pos = save
        return atom()

    def atom():
        nonlocal pos
        t = peek()
        if kind(t) == "name" and t[2]:                   # a capital: predicate or letter
            nxt = peek(1)
            if nxt == "(":
                pos += 2
                args = [term()]
                while peek() == ",":
                    pos += 1
                    args.append(term())
                expect(")")
                return ("pred", t[1], tuple(args))
            if kind(nxt) not in ("rel", "aop"):
                pos += 1
                return ("var", t[1])
        left = term()
        if kind(peek()) != "rel":
            raise ParseError(f"expected a relation after a term, got {peek()!r}")
        op = peek()[1]
        pos += 1
        right = term()
        if kind(peek()) == "rel":
            raise ParseError("chained relations")
        return make_rel(op, left, right)

    def make_rel(op, a, b):
        if op == "ne":
            return ("not", ("rel", "=", a, b))
        if op == "notin":
            return ("not", ("rel", "in", a, b))
        return ("rel", op, a, b)

    def term():
        nonlocal pos
        left = product()
        while peek() in (("aop", "+"), ("aop", "-")):
            op = peek()[1]
            pos += 1
            left = ("app", op, (left, product()))
        return left

    def product():
        nonlocal pos
        left = signed()
        while peek() in (("aop", "*"), ("aop", "/")):
            op = peek()[1]
            pos += 1
            left = ("app", op, (left, signed()))
        return left

    def signed():
        nonlocal pos
        if peek() == ("aop", "-"):
            pos += 1
            return ("app", "neg", (signed(),))
        return power()

    def power():
        nonlocal pos
        base = primary()
        if peek() in (("aop", "^"), ("aop", "_")):
            op = peek()[1]
            pos += 1
            return ("app", op, (base, signed() if peek() != "(" else primary()))
        return base

    def primary():
        nonlocal pos
        t = peek()
        if kind(t) == "name":
            pos += 1
            if peek() == "(" and not t[2] and not t[1][0].isdigit():   # f(x), g(x, y)
                pos += 1
                args = [term()]
                while peek() == ",":
                    pos += 1
                    args.append(term())
                expect(")")
                return ("app", t[1], tuple(args))
            return ("v", t[1])
        if t == "(":
            pos += 1
            inner = term()
            expect(")")
            return inner
        if kind(t) == "bar":
            pos += 1
            inner = term()
            if kind(peek()) != "bar":
                raise ParseError("unclosed |")
            pos += 1
            return ("app", "abs", (inner,))
        if kind(t) == "fn":
            pos += 1
            args = []
            for _ in range(t[2]):
                expect("(")
                args.append(term())
                expect(")")
            return ("app", t[1], tuple(args))
        raise ParseError(f"unexpected {t!r}")

    tree = binary(0)
    if pos != len(tokens):
        raise ParseError(f"trailing {tokens[pos]!r}")
    return tree


def read_formula(text: str):
    """A line's formula: propositional if it parses as such, else first-order."""
    try:
        return parse_formula(text)
    except ParseError:
        return parse_fo(text)


QUANT = ("forall", "exists")
CONNECTIVES = ("not", "and", "or", "imp", "iff")


def term_names(t) -> set:
    if t[0] == "v":
        return {t[1]}
    return set().union(*(term_names(a) for a in t[2]))


def names(f, free_only=False) -> set:
    """Names occurring in formula f (with free_only, only free occurrences)."""
    k = f[0]
    if k in ("var", "bot", "top"):
        return set()
    if k == "pred":
        return set().union(*(term_names(a) for a in f[2]))
    if k == "rel":
        return term_names(f[2]) | term_names(f[3])
    if k in CONNECTIVES:
        return set().union(*(names(a, free_only) for a in f[1:]))
    x, body, bound = f[1], f[2], f[3]
    inner = names(body, free_only) | (names(bound, free_only) if bound else set())
    return inner - {x} if free_only else inner | {x}


def subst_term(t, x, s):
    if t[0] == "v":
        return s if t[1] == x else t
    return ("app", t[1], tuple(subst_term(a, x, s) for a in t[2]))


def subst(f, x, s):
    """f[s/x]: replace the free occurrences of the name x by the term s (no capture check)."""
    k = f[0]
    if k in ("var", "bot", "top"):
        return f
    if k == "pred":
        return ("pred", f[1], tuple(subst_term(a, x, s) for a in f[2]))
    if k == "rel":
        return ("rel", f[1], subst_term(f[2], x, s), subst_term(f[3], x, s))
    if k in CONNECTIVES:
        return (k,) + tuple(subst(a, x, s) for a in f[1:])
    if f[1] == x:
        return f
    return (k, f[1], subst(f[2], x, s), subst(f[3], x, s) if f[3] else None)


def free_for(s, x, f, bound=frozenset()) -> bool:
    """s is free for x in f: no free x of f lies under a quantifier on a name of s."""
    k = f[0]
    if k in ("var", "bot", "top"):
        return True
    if k in ("pred", "rel"):
        if x in names(f) and x not in bound:
            return not (term_names(s) & bound)
        return True
    if k in CONNECTIVES:
        return all(free_for(s, x, a, bound) for a in f[1:])
    if f[1] == x:
        return True
    inner = bound | {f[1]}
    return free_for(s, x, f[2], inner) and (f[3] is None or free_for(s, x, f[3], inner))


def instance_term(pattern, x, target):
    """A term t with pattern[t/x] == target: ("ok", t) (t None if x is not free in
    pattern, so any term works), or None if target is no instance of pattern."""
    found = []

    def mt(p, q, bound):
        if p[0] == "v" and p[1] == x and x not in bound:
            if found and found[0] != q:
                return False
            if not found:
                found.append(q)
            return True
        if p[0] != q[0]:
            return False
        if p[0] == "v":
            return p == q
        return p[1] == q[1] and len(p[2]) == len(q[2]) and all(
            mt(a, b, bound) for a, b in zip(p[2], q[2]))

    def mf(p, q, bound):
        if p[0] != q[0]:
            return False
        k = p[0]
        if k in ("var", "bot", "top"):
            return p == q
        if k == "pred":
            return p[1] == q[1] and len(p[2]) == len(q[2]) and all(
                mt(a, b, bound) for a, b in zip(p[2], q[2]))
        if k == "rel":
            return p[1] == q[1] and mt(p[2], q[2], bound) and mt(p[3], q[3], bound)
        if k in CONNECTIVES:
            return all(mf(a, b, bound) for a, b in zip(p[1:], q[1:]))
        if p[1] != q[1] or (p[3] is None) != (q[3] is None):
            return False
        inner = bound | {p[1]}
        return mf(p[2], q[2], inner) and (p[3] is None or mf(p[3], q[3], inner))

    if not mf(pattern, target, frozenset()):
        return None
    t = found[0] if found else None
    if (subst(pattern, x, t) if t else pattern) != target:
        return None
    return ("ok", t)


def replaces(a, b, t, s):
    """b arises from a by replacing some free occurrences of the term t by s, none of
    them under a quantifier on a name of t or s: a = φ[t/x], b = φ[s/x] for some φ.
    Returns "" or what is wrong ("no" for a shape mismatch, "capture" for a binder)."""
    risky = term_names(t) | term_names(s)
    problem = []

    def rt(p, q, bound):
        if p == q:
            return True
        if p == t and q == s:
            if risky & bound:
                problem.append("capture")
                return False
            return True
        if p[0] == "app" and q[0] == "app" and p[1] == q[1] and len(p[2]) == len(q[2]):
            return all(rt(x, y, bound) for x, y in zip(p[2], q[2]))
        return False

    def rf(p, q, bound):
        if p[0] != q[0]:
            return False
        k = p[0]
        if k in ("var", "bot", "top"):
            return p == q
        if k == "pred":
            return p[1] == q[1] and len(p[2]) == len(q[2]) and all(
                rt(x, y, bound) for x, y in zip(p[2], q[2]))
        if k == "rel":
            return p[1] == q[1] and rt(p[2], q[2], bound) and rt(p[3], q[3], bound)
        if k in CONNECTIVES:
            return all(rf(x, y, bound) for x, y in zip(p[1:], q[1:]))
        if p[1] != q[1] or (p[3] is None) != (q[3] is None):
            return False
        inner = bound | {p[1]}
        return rf(p[2], q[2], inner) and (p[3] is None or rf(p[3], q[3], inner))

    ok = rf(a, b, frozenset())
    return "" if ok else (problem[0] if problem else "no")


def show_term(t) -> str:
    if t[0] == "v":
        return t[1]
    head, args = t[1], t[2]
    if head in ("+", "-", "*", "/") and len(args) == 2:
        sym = {"*": "·"}.get(head, head)
        return f"({show_term(args[0])} {sym} {show_term(args[1])})"
    if head in ("^", "_"):
        return f"{show_term(args[0])}{head}{show_term(args[1])}"
    if head == "neg":
        return "-" + show_term(args[0])
    if head == "abs":
        return f"|{show_term(args[0])}|"
    return f"{head}({', '.join(show_term(a) for a in args)})"


def matrix(f):
    """The body of a quantifier, with a bound unfolded: ∀x∈A φ is ∀x (x∈A → φ),
    ∃x∈A φ is ∃x (x∈A ∧ φ)."""
    if f[3] is None:
        return f[2]
    return ("imp" if f[0] == "forall" else "and", f[3], f[2])


# ---------------------------------------------------------------------------
# Derivations
# ---------------------------------------------------------------------------

RULES = {  # macro -> (display name, citation shape: L = line, B = box)
    "ai": ("∧I", "LL"), "ae": ("∧E", "L"), "ii": ("→I", "B"), "ie": ("→E", "LL"),
    "oi": ("∨I", "L"), "oe": ("∨E", "LBB"), "ni": ("¬I", "B"), "ne": ("¬E", "LL"),
    "be": ("⊥E", "L"), "raa": ("RAA", "B"), "bi": ("↔I", "BB"), "bie": ("↔E", "LL"),
    "r": ("R", "L"),
    # derived rules (Chapter 1 proves each once; latex/fitch-book.sty has their macros)
    "nni": ("¬¬I", "L"), "nne": ("¬¬E", "L"), "mt": ("MT", "LL"), "ctp": ("CP", "L"),
    "ds": ("DS", "LL"), "dm": ("DM", "L"), "lem": ("LEM", ""),
    # quantifier and equality rules (Chapter 4); "|" separates the citation shapes
    # of the unbounded and the bounded form (\forall x \in A: the bound is a line)
    "Ae": ("∀E", "L|LL"), "Ai": ("∀I", "B"), "Ei": ("∃I", "L|LL"), "Ee": ("∃E", "LB"),
    "eqi": ("=I", ""), "eqe": ("=E", "LL"),
}
QUANT_RULES = {"Ae", "Ai", "Ei", "Ee", "eqi", "eqe"}


@dataclass
class Line:
    label: str
    text: str
    hypo: bool
    rule: str = ""          # macro name, "by", or ""
    by_text: str = ""
    refs: str = ""
    lineno: int = 0         # line in the source file
    boxes: tuple = ()       # ids of the boxes containing this line, outermost first
    formula: object = None
    parse_error: str = ""
    display: str = ""       # the number fitch.sty prints for the line
    gap: bool = False       # an unlabelled row or a \vdots row


@dataclass
class Box:
    id: int
    parent: int | None
    lines: list = field(default_factory=list)   # indices into the line list
    closed_at: int = -1                          # index of the first line after it
    guard: list = field(default_factory=list)   # flagged names, from \open[x_0]


def read_group(s: str, i: int):
    """Read a balanced {...} group starting at or after i; return (content, end)."""
    while i < len(s) and s[i].isspace():
        i += 1
    if i >= len(s) or s[i] != "{":
        return None, i
    depth, j = 0, i
    while j < len(s):
        if s[j] == "{":
            depth += 1
        elif s[j] == "}":
            depth -= 1
            if depth == 0:
                return s[i + 1:j], j + 1
        j += 1
    raise ParseError("unbalanced braces")


def read_opt(s: str, i: int):
    """Read an optional [...] argument at or after i; return (content or None, end)."""
    j = i
    while j < len(s) and s[j].isspace():
        j += 1
    if j >= len(s) or s[j] != "[":
        return None, i
    depth, k = 0, j + 1
    while k < len(s):
        c = s[k]
        if c == "\\":
            k += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
        elif c == "]" and depth == 0:
            return s[j + 1:k], k + 1
        k += 1
    raise ParseError("unbalanced [ in an optional argument")


def blank_base(base: str) -> bool:
    """A base that prints nothing, such as the \\  of \\have[\\ ][0]."""
    return re.sub(r"\\[ ,;:!]|~|\s", "", base) == ""


def render_number(base: str, ctr: int) -> str:
    """fitch.sty's \\nd@render: the counter alone, or the base followed by +k / -k."""
    if base == "":
        return str(ctr)
    return base + ("" if ctr == 0 else f"+{ctr}" if ctr > 0 else str(ctr))


COMMAND = re.compile(r"\\(hypo|have|open|close|guard)\b")


def guard_names(text: str) -> list:
    """The names of a guard [x_0] or [x_0, y_0]."""
    toks = [t for t in fo_tokenize(text) if t != ","]
    if toks and all(isinstance(t, tuple) and t[0] == "name" for t in toks):
        return [t[1] for t in toks]
    return [text.strip()] if text.strip() else []


def parse_nd(body: str, first_lineno: int, schema_key: bool = False):
    """Turn an nd body into (lines, boxes, structural errors).

    Reads fitch.sty's optional arguments \\have[base][offset]{label}[guard]{formula}
    and sets each line's printed number (`display`); with `schema_key`
    (\\begin{nd}[schema]) a line prints its own label.
    """
    lines, boxes, errors = [], [], []
    stack = []
    pos = 0
    base, ctr = "", 1
    while True:
        m = COMMAND.search(body, pos)
        if not m:
            break
        lineno = first_lineno + body.count("\n", 0, m.start())
        cmd = m.group(1)
        pos = m.end()
        if cmd == "open":
            g, pos = read_opt(body, pos)          # guard: the flagged name
            box = Box(id=len(boxes), parent=stack[-1] if stack else None)
            box.guard = guard_names(g) if g else []
            boxes.append(box)
            stack.append(box.id)
            continue
        if cmd == "guard":                        # \guard[n]{x}: the n-th innermost box
            n, pos = read_opt(body, pos)
            g, pos = read_group(body, pos)
            try:
                depth = int(n) if n and n.strip() else 1
            except ValueError:
                depth = 1
            if g is not None and 0 < depth <= len(stack):
                boxes[stack[-depth]].guard += guard_names(g)
            continue
        if cmd == "close":
            if not stack:
                errors.append((lineno, "\\close without a matching \\open"))
                continue
            box = boxes[stack.pop()]
            box.closed_at = len(lines)
            if not box.lines:
                errors.append((lineno, "empty box"))
            continue
        opt1, pos = read_opt(body, pos)
        opt2 = None
        if opt1 is not None:
            opt2, pos = read_opt(body, pos)
        label, pos = read_group(body, pos)
        g, pos = read_opt(body, pos)              # guard (\hypo{i}[x_0]{...}): innermost box
        if g and stack:
            boxes[stack[-1]].guard += guard_names(g)
        text, pos = read_group(body, pos)
        if label is None or text is None:
            errors.append((lineno, f"\\{cmd} needs {{label}} {{formula}}"))
            continue
        line = Line(label=label.strip(), text=text.strip(), hypo=(cmd == "hypo"),
                    lineno=lineno, boxes=tuple(stack))
        line.gap = not line.label or "\\vdots" in line.text
        if opt1 is not None:                      # fitch.sty: [n] means [n][0]
            base = opt1
            ctr = 0
        if opt2 is not None and opt2.strip():
            try:
                ctr = int(opt2.strip())
            except ValueError:
                errors.append((lineno, f"\\{cmd}[{opt1}][{opt2}]: the offset is not a number"))
        if schema_key:
            line.display = line.label
        else:
            line.display = render_number(base, ctr)
            if base and blank_base(base) and ctr != 0:
                errors.append((lineno, f"line {line.label or '(unlabelled)'} prints a stray "
                                       f"number {ctr:+d}: an earlier row left the base blank; "
                                       f"give this line its own [base][offset] or [][n]"))
            ctr += 1
        # justification: the rest up to the next command
        nxt = COMMAND.search(body, pos)
        rest = body[pos:nxt.start() if nxt else len(body)]
        jm = re.match(r"\s*\\([A-Za-z]+)", rest)
        if jm:
            name = jm.group(1)
            j = len(jm.group(0))
            if name == "by":
                by_text, j = read_group(rest, j)
                refs, j = read_group(rest, j)
                line.rule, line.by_text, line.refs = "by", by_text or "", refs or ""
            else:
                refs, j = read_group(rest, j)
                line.rule, line.refs = name, refs or ""
        for b in stack:
            boxes[b].lines.append(len(lines))
        lines.append(line)
    for b in stack:
        errors.append((first_lineno, "box opened but never closed"))
        boxes[b].closed_at = len(lines)
    return lines, boxes, errors


def parse_refs(refs: str):
    """'1,3-5' -> [('L', '1'), ('B', ('3', '5'))]."""
    out = []
    for part in [p.strip() for p in refs.split(",") if p.strip()]:
        if "-" in part:
            a, b = [x.strip() for x in part.split("-", 1)]
            out.append(("B", (a, b)))
        else:
            out.append(("L", part))
    return out


def check_numbering(lines):
    """Printed numbers run 1, 2, 3, ..., jumping forward only across a gap row."""
    errors = []
    shown, prev, gap_since, bad = [], None, False, False
    for ln in lines:
        if ln.gap:
            gap_since = True
            continue
        if not re.fullmatch(r"-?\d+", ln.display):
            prev, gap_since = None, False          # symbolic (n, n+1): not checked
            continue
        d = int(ln.display)
        if re.fullmatch(r"\d+", ln.label) and int(ln.label) != d:
            errors.append((ln.lineno, f"line label {ln.label} prints as {d}"))
        shown.append(d)
        if prev is None:
            ok = d == 1 or gap_since or len(shown) > 1   # after a symbolic run: free
        else:
            ok = d > prev if gap_since else d == prev + 1
        bad |= not ok
        prev, gap_since = d, False
    if bad:
        errors.append((lines[0].lineno, f"lines are not numbered 1, 2, 3, ...: {shown}"))
    return errors


def check_derivation(lines, boxes, schema=False):
    """Return (errors, notes) for one parsed derivation: lists of (lineno, message).

    With `schema` (a rule schema or a partial derivation), unjustified lines and
    justifications citing nothing are notes instead of errors.
    """
    errors, notes = [], []
    if not schema and any(not re.fullmatch(r"\d+", ln.label) for ln in lines if ln.label):
        errors.append((lines[0].lineno if lines else 0,
                       "non-numeric line labels: mark a rule schema or partial derivation "
                       "'% schema', a deliberately flawed one '% expect-invalid'"))
        return errors, notes

    index = {}
    for k, ln in enumerate(lines):
        if not ln.label:
            continue
        if ln.label in index:
            errors.append((ln.lineno, f"line label {ln.label} used twice"))
        else:
            index[ln.label] = k
    if len(index) == sum(1 for ln in lines if ln.label):
        errors += check_numbering(lines)

    # boxes begin with their assumption; no assumption in mid-box
    for box in boxes:                  # a flagged box (\open[x_0], for ∀I) may have none
        if box.lines and not lines[box.lines[0]].hypo and not box.guard:
            errors.append((lines[box.lines[0]].lineno,
                           f"box starting at line {lines[box.lines[0]].label} "
                           f"does not begin with an assumption"))
    for k, ln in enumerate(lines):
        if ln.hypo and ln.boxes:
            box = boxes[ln.boxes[-1]]
            run = box.lines[:next((n for n, i in enumerate(box.lines)
                                   if not lines[i].hypo), len(box.lines))]
            if k not in run:
                errors.append((ln.lineno, f"assumption {ln.label} in the middle of a box"))

    def available(j, k):
        """Line index j may be cited at line index k."""
        return j < k and set(lines[j].boxes) <= set(lines[k].boxes)

    def box_for(a, b, k):
        """The closed box a-b citable at line index k, or an error message."""
        if a not in index or b not in index:
            return None, f"cites {a}-{b}, but line {a if a not in index else b} does not exist"
        ia, ib = index[a], index[b]
        for box in boxes:
            if box.lines and box.lines[0] == ia and box.lines[-1] == ib:
                if box.closed_at > k:
                    return None, f"cites box {a}-{b}, which is still open"
                parent_ok = box.parent is None or box.parent in lines[k].boxes
                if not parent_ok:
                    return None, f"cites box {a}-{b}, which sits inside a box that has closed"
                return box, ""
        if any(box.lines and box.lines[0] == ia and k in box.lines for box in boxes):
            return None, f"cites box {a}-{b}, which is still open"
        return None, f"cites {a}-{b}, which is not a box (a box runs from its assumption to its last line)"

    after_vdots = False
    for k, ln in enumerate(lines):
        if ln.gap:
            after_vdots = True
            notes.append((ln.lineno, "\\vdots or unlabelled row: skipped"))
            continue
        try:
            ln.formula = read_formula(ln.text)
        except ParseError as e:
            ln.parse_error = str(e)
        if ln.hypo:
            if ln.rule and ln.rule != "by":
                errors.append((ln.lineno, f"assumption {ln.label} carries a rule"))
            continue
        if not ln.rule:
            if after_vdots:
                notes.append((ln.lineno, f"line {ln.label} follows \\vdots, unjustified: skipped"))
            elif schema:
                notes.append((ln.lineno, f"line {ln.label} unjustified (a given line of the schema): skipped"))
            else:
                errors.append((ln.lineno, f"line {ln.label} has no justification"))
            continue
        after_vdots = False

        cites = parse_refs(ln.refs)
        if schema and not cites and ln.rule in RULES and RULES[ln.rule][1]:
            notes.append((ln.lineno, f"line {ln.label} cites nothing yet (a gap in the schema): skipped"))
            continue
        cited_ok = True
        resolved = []
        for shape, ref in cites:
            if shape == "L":
                if ref not in index:
                    errors.append((ln.lineno, f"line {ln.label} cites line {ref}, which does not exist"))
                    cited_ok = False
                elif not available(index[ref], k):
                    why = "a later line" if index[ref] >= k else "inside a box that has closed"
                    errors.append((ln.lineno, f"line {ln.label} cites line {ref}, {why}"))
                    cited_ok = False
                resolved.append(("L", index.get(ref)))
            else:
                box, err = box_for(ref[0], ref[1], k)
                if err:
                    errors.append((ln.lineno, f"line {ln.label} {err}"))
                    cited_ok = False
                resolved.append(("B", box))

        if ln.rule == "by":
            notes.append((ln.lineno, f"line {ln.label} justified by text "
                                     f"({ln.by_text.strip() or 'empty'}): shape not checked"))
            continue
        if ln.rule not in RULES:
            errors.append((ln.lineno, f"line {ln.label}: unknown rule macro \\{ln.rule}"))
            continue
        name, want = RULES[ln.rule]
        got = "".join(s for s, _ in cites)
        if got not in want.split("|"):
            errors.append((ln.lineno, f"line {ln.label}: {name} cites "
                                      f"{_shape_words(want)}, got {ln.refs or 'nothing'}"))
            continue
        if not cited_ok:
            continue
        quant = ln.rule in QUANT_RULES
        involved = [ln] + [lines[i] for s, i in resolved if s == "L"]
        for s, box in resolved:
            if s == "B" and quant:          # a ∀I box may open with a gap row, not an assumption
                involved += own_assumptions(box, lines) + [lines[box.lines[-1]]]
            elif s == "B":
                involved += [lines[box.lines[0]], lines[box.lines[-1]]]
        bad = [x for x in involved if x.formula is None]
        if bad:
            notes.append((ln.lineno, f"line {ln.label}: formula of line {bad[0].label} "
                                     f"not propositional or first-order "
                                     f"({bad[0].parse_error or 'a gap row'}): shape not checked"))
            continue
        if quant:
            problem = check_quant(ln.rule, k, resolved, lines)
            if problem is None:
                notes.append((ln.lineno, f"line {ln.label}: {name} box not readable: shape not checked"))
                continue
        else:
            problem = check_shape(ln.rule, ln.formula, resolved, lines)
        if problem:
            errors.append((ln.lineno, f"line {ln.label}: {name} {problem}"))
    return errors, notes


def _shape_words(want: str) -> str:
    words = {"L": "a line", "B": "a box i-j"}
    return " or ".join(", ".join(words[c] for c in alt) or "nothing" for alt in want.split("|"))


def check_shape(rule, f, resolved, lines):
    """Return '' if the line is a correct instance of the rule, else what is wrong."""
    L = [lines[i].formula for s, i in resolved if s == "L"]
    B = [(lines[b.lines[0]].formula, lines[b.lines[-1]].formula) for s, b in resolved if s == "B"]
    s = show
    if rule == "ai":
        if f[0] == "and" and {(f[1], f[2]), (f[2], f[1])} & {(L[0], L[1])}:
            return ""
        return f"needs {s(f)} to be the conjunction of the cited lines {s(L[0])}, {s(L[1])}"
    if rule == "ae":
        if L[0][0] == "and" and f in (L[0][1], L[0][2]):
            return ""
        return f"needs the cited line to be a conjunction with {s(f)} as one side (got {s(L[0])})"
    if rule == "ii":
        (a, b), = B
        if f == ("imp", a, b):
            return ""
        return f"needs {s(a)} → {s(b)} from its box, not {s(f)}"
    if rule == "ie":
        for imp, ant in ((L[0], L[1]), (L[1], L[0])):
            if imp[0] == "imp" and imp[1] == ant and imp[2] == f:
                return ""
        return f"needs an implication and its antecedent giving {s(f)} (got {s(L[0])}, {s(L[1])})"
    if rule == "oi":
        if f[0] == "or" and L[0] in (f[1], f[2]):
            return ""
        return f"needs {s(f)} to be a disjunction with {s(L[0])} as one side"
    if rule == "oe":
        d = L[0]
        (a1, c1), (a2, c2) = B
        if d[0] != "or":
            return f"cites {s(d)}, which is not a disjunction"
        if (a1, a2) != (d[1], d[2]):
            return f"boxes must assume {s(d[1])} and {s(d[2])} (got {s(a1)}, {s(a2)})"
        if c1 != f or c2 != f:
            return f"both boxes must end in {s(f)} (got {s(c1)}, {s(c2)})"
        return ""
    if rule == "ni":
        (a, b), = B
        if b != BOT:
            return f"box must end in ⊥ (ends in {s(b)})"
        if f != ("not", a):
            return f"concludes {s(f)}, but the box assumed {s(a)}"
        return ""
    if rule == "ne":
        if f != BOT:
            return f"concludes ⊥, not {s(f)}"
        if L[1] == ("not", L[0]) or L[0] == ("not", L[1]):
            return ""
        return f"needs a statement and its negation (got {s(L[0])}, {s(L[1])})"
    if rule == "be":
        return "" if L[0] == BOT else f"cites {s(L[0])}, not ⊥"
    if rule == "raa":
        (a, b), = B
        if b != BOT:
            return f"box must end in ⊥ (ends in {s(b)})"
        if a != ("not", f):
            return f"concludes {s(f)}, but the box assumed {s(a)}, not ¬{s(f)}"
        return ""
    if rule == "bi":
        (a1, c1), (a2, c2) = B
        if f[0] == "iff" and (a1, c1, a2, c2) == (f[1], f[2], f[2], f[1]):
            return ""
        return f"needs boxes {s(f[1]) if f[0] == 'iff' else 'A'} … {s(f[2]) if f[0] == 'iff' else 'B'} and back, concluding a biconditional"
    if rule == "bie":
        for bic, side in ((L[0], L[1]), (L[1], L[0])):
            if bic[0] == "iff" and ((bic[1] == side and bic[2] == f) or (bic[2] == side and bic[1] == f)):
                return ""
        return f"needs a biconditional and one side giving the other (got {s(L[0])}, {s(L[1])}, {s(f)})"
    if rule == "r":
        return "" if L[0] == f else f"repeats {s(L[0])} as {s(f)}"
    if rule == "nni":
        return "" if f == ("not", ("not", L[0])) else f"needs ¬¬{s(L[0])}, not {s(f)}"
    if rule == "nne":
        return "" if L[0] == ("not", ("not", f)) else f"needs the cited line to be ¬¬{s(f)} (got {s(L[0])})"
    if rule == "mt":
        for imp, neg in ((L[0], L[1]), (L[1], L[0])):
            if imp[0] == "imp" and neg == ("not", imp[2]) and f == ("not", imp[1]):
                return ""
        return f"needs A → B and ¬B giving ¬A (got {s(L[0])}, {s(L[1])}, {s(f)})"
    if rule == "ctp":
        a = L[0]
        if a[0] == "imp" and f == ("imp", ("not", a[2]), ("not", a[1])):
            return ""
        if (a[0] == "imp" and a[1][0] == "not" and a[2][0] == "not"
                and f == ("imp", a[2][1], a[1][1])):
            return ""          # the converse direction, ¬B → ¬A to A → B
        return f"needs the contrapositive of {s(a)}, not {s(f)}"
    if rule == "ds":
        for d, n in ((L[0], L[1]), (L[1], L[0])):
            if d[0] == "or" and ((n == ("not", d[1]) and f == d[2]) or (n == ("not", d[2]) and f == d[1])):
                return ""
        return f"needs A ∨ B and ¬A giving B (got {s(L[0])}, {s(L[1])}, {s(f)})"
    if rule == "dm":
        a = L[0]
        def dual(x):
            if x[0] == "not" and x[1][0] in ("and", "or"):
                op = "or" if x[1][0] == "and" else "and"
                return (op, ("not", x[1][1]), ("not", x[1][2]))
            return None
        if dual(a) == f or dual(f) == a:
            return ""
        return f"is not a De Morgan law between {s(a)} and {s(f)}"
    if rule == "lem":
        if f[0] == "or" and f[2] == ("not", f[1]):
            return ""
        return f"needs A ∨ ¬A, not {s(f)}"
    return "unknown rule"


# ---------------------------------------------------------------------------
# Quantifier and equality rules
# ---------------------------------------------------------------------------

def occurs(name: str, ln) -> bool:
    """The name occurs in line ln (read from its tokens when the formula did not parse)."""
    if ln.formula is not None:
        return name in names(ln.formula)
    return any(t[0] == "name" and t[1] == name
               for t in fo_tokenize(ln.text) if isinstance(t, tuple))


def own_assumptions(box, lines):
    """The assumption lines of the box itself (not of a box inside it)."""
    return [lines[i] for i in box.lines if lines[i].hypo and lines[i].boxes[-1] == box.id]


def check_quant(rule, k, resolved, lines):
    """Return '' if line k is a correct instance of a quantifier or equality rule,
    else what is wrong. All formulas involved have parsed."""
    ln = lines[k]
    f = ln.formula
    L = [lines[i].formula for s, i in resolved if s == "L"]
    boxes_cited = [b for s, b in resolved if s == "B"]
    s = show

    def instance(pattern, x, target, what):
        """'' or the problem with target = pattern[t/x], t free for x."""
        r = instance_term(pattern, x, target)
        if r is None:
            return f"needs {what}"
        t = r[1]
        if t is not None and not free_for(t, x, pattern):
            return (f"substitutes {show_term(t)} for {x}, but {show_term(t)} is not free for "
                    f"{x} in {s(pattern)} (a variable of it would be captured)")
        return ""

    def fresh(x0, extra):
        """The first side-condition clause x0 violates, or ''."""
        for what, g in extra:
            if x0 in names(g):
                return f"the flagged name {x0} occurs in {what} {s(g)}"
        for j in range(k):
            h = lines[j]
            if h.hypo and set(h.boxes) <= set(ln.boxes) and occurs(x0, h):
                kind = "premise" if not h.boxes else "open assumption"
                return f"the flagged name {x0} occurs in the {kind} {h.label} ({h.text.strip()})"
        return ""

    if rule == "eqi":
        if f[0] == "rel" and f[1] == "=" and f[2] == f[3]:
            return ""
        return f"concludes t = t, not {s(f)}"

    if rule == "eqe":
        errs = []
        for eq, a in ((L[0], L[1]), (L[1], L[0])):
            if not (eq[0] == "rel" and eq[1] == "="):
                continue
            r = replaces(a, f, eq[2], eq[3])
            if r == "":
                return ""
            errs.append(r)
        if not errs:
            return f"cites no equation (got {s(L[0])}, {s(L[1])})"
        if "capture" in errs:
            return ("replaces a term under a quantifier that binds one of its variables "
                    "(not free for x)")
        return (f"needs an equation t = s and a line φ[t/x] giving φ[s/x] "
                f"(got {s(L[0])}, {s(L[1])}, {s(f)})")

    if rule == "Ae":
        quants = [(n, q) for n, q in enumerate(L) if q[0] == "forall"]
        if not quants:
            return f"cites no ∀ line (got {', '.join(s(q) for q in L)})"
        problem = ""
        for n, q in quants:
            x = q[1]
            if len(L) == 1:
                problem = instance(matrix(q), x, f, f"{s(f)} to be an instance of {s(q)}")
            elif q[3] is None:
                problem = f"cites two lines, but {s(q)} has no bound"
            else:
                other = L[1 - n]
                problem = instance(("and", q[3], q[2]), x, ("and", other, f),
                                   f"{s(other)} and {s(f)} to be the bound and the body of "
                                   f"{s(q)} at one term")
            if not problem:
                return ""
        return problem

    if rule == "Ei":
        if f[0] != "exists":
            return f"concludes {s(f)}, which is not an ∃ formula"
        x = f[1]
        if len(L) == 1:
            return instance(matrix(f), x, L[0], f"{s(L[0])} to be an instance of {s(f)}")
        if f[3] is None:
            return f"cites two lines, but {s(f)} has no bound"
        problem = ""
        for a, b in ((L[0], L[1]), (L[1], L[0])):
            problem = instance(("and", f[3], f[2]), x, ("and", a, b),
                               f"the cited lines to be the bound and the body of {s(f)} "
                               f"at one term")
            if not problem:
                return ""
        return problem

    box, = boxes_cited
    if not box.guard:
        return "needs a flagged box (\\open[x_0])"
    first, last = lines[box.lines[0]], lines[box.lines[-1]]
    if last.boxes[-1] != box.id:
        return f"the box's last line {last.label} must be a line of the box itself"
    if last.formula is None:
        return None
    hyps = own_assumptions(box, lines)
    if any(h.formula is None for h in hyps):
        return None

    if rule == "Ai":
        if f[0] != "forall":
            return f"concludes {s(f)}, which is not a ∀ formula"
        x = f[1]
        problem = ""
        for x0 in box.guard:
            v = ("v", x0)
            if not hyps:
                ok = last.formula == subst(matrix(f), x, v)
                want = f"a box with no assumption ending in {s(subst(matrix(f), x, v))}"
            elif len(hyps) == 1 and f[3] is not None:
                ok = (hyps[0].formula == subst(f[3], x, v)
                      and last.formula == subst(f[2], x, v))
                want = (f"a box assuming {s(subst(f[3], x, v))} and ending in "
                        f"{s(subst(f[2], x, v))}")
            else:
                ok = False
                want = "a flagged box with no assumption (a ∀I box has none)"
            if not ok:
                problem = f"needs {want}"
                continue
            return fresh(x0, [("the conclusion", f)])
        return problem

    if rule == "Ee":
        e = L[0]
        if e[0] != "exists":
            return f"cites {s(e)}, which is not an ∃ formula"
        x = e[1]
        if last.formula != f:
            return f"the box must end in the conclusion {s(f)} (ends in {s(last.formula)})"
        problem = ""
        for x0 in box.guard:
            v = ("v", x0)
            got = [h.formula for h in hyps]
            wants = [[subst(matrix(e), x, v)]]
            if e[3] is not None:
                b, m = subst(e[3], x, v), subst(e[2], x, v)
                wants += [[b, m], [m, b]]
            if got not in wants:
                problem = (f"the box must assume {' and '.join(s(w) for w in wants[-1])} "
                           f"(assumes {', '.join(s(g) for g in got) or 'nothing'})")
                continue
            return fresh(x0, [("the conclusion", f), ("the ∃ line", e)])
        return problem
    return "unknown rule"


# ---------------------------------------------------------------------------
# Truth tables
# ---------------------------------------------------------------------------

TV = re.compile(r"^(?:\\mathrm\{([TF])\}|\\text\{([TF])\}|\\textsf\{([TF])\}|([TF]))$")


def check_truth_table(body: str, first_lineno: int):
    errors, notes = [], []
    rows = [r.strip() for r in re.split(r"\\\\", body)]
    if not any("\\hline" in r for r in rows):
        return None
    header_raw, *rest = re.split(r"\\hline", body, maxsplit=1)
    if not rest:
        return None
    header = [c.strip() for c in header_raw.strip().rstrip("\\").split("&")]
    data = []
    for r in re.split(r"\\\\", rest[0]):
        r = r.replace("\\hline", "").strip()
        if not r:
            continue
        cells = [c.strip() for c in r.split("&")]
        vals = []
        for c in cells:
            m = TV.match(c)
            if not m:
                return None            # not a T/F table
            vals.append(next(g for g in m.groups() if g) == "T")
        data.append(vals)
    if not data:
        return None
    columns = []
    for h in header:
        try:
            columns.append(parse_formula(h))
        except ParseError as e:
            columns.append(None)
            notes.append((first_lineno, f"truth table column {h!r} not propositional ({e}): skipped"))
    letters = {c[1]: n for n, c in enumerate(columns) if c is not None and c[0] == "var"}
    for r, vals in enumerate(data, 1):
        if len(vals) != len(header):
            errors.append((first_lineno, f"truth table row {r} has {len(vals)} cells, header {len(header)}"))
            continue
        env = {x: vals[n] for x, n in letters.items()}
        for n, col in enumerate(columns):
            if col is None or col[0] == "var":
                continue
            try:
                want = evaluate(col, env)
            except KeyError as e:
                notes.append((first_lineno, f"truth table column {header[n]!r} uses letter "
                                            f"{e.args[0]} with no column: skipped"))
                columns[n] = None
                continue
            if want != vals[n]:
                row = ", ".join(f"{x}={'T' if env[x] else 'F'}" for x in sorted(env))
                errors.append((first_lineno, f"truth table: {header[n]} is "
                                             f"{'T' if want else 'F'} in row {r} ({row}), "
                                             f"table says {'T' if vals[n] else 'F'}"))
    return errors, notes


# ---------------------------------------------------------------------------
# Files
# ---------------------------------------------------------------------------

ND = re.compile(r"\\begin\{nd\}(.*?)\\end\{nd\}", re.S)
ARRAY = re.compile(r"\\begin\{array\}\{[^}]*\}(.*?)\\end\{array\}", re.S)
MARKER = re.compile(r"%\s*(expect-invalid|schema)\b")
ND_OPTIONS = re.compile(r"\A\s*\[([^\]]*)\]")


def block_marker(text: str, start: int):
    """The marker for the nd starting at `start`: 'expect-invalid', 'schema' or None.

    Looks back from \\begin{nd} to the fence that opens the raw block (plus the
    line before it), or to the previous \\end{nd} in the same block; the nearest
    marker wins.
    """
    lines = text[:start].split("\n")
    for n, ln in enumerate(reversed(lines[-15:])):
        if n and "\\end{nd}" in ln:
            return None
        m = MARKER.search(ln)
        if m:
            return m.group(1)
        if ln.strip().startswith("```"):
            idx = len(lines) - n - 2
            m = MARKER.search(lines[idx]) if idx >= 0 else None
            return m.group(1) if m else None
    return None


def expects_invalid(text: str, start: int) -> bool:
    return block_marker(text, start) == "expect-invalid"


def nd_options(body: str):
    """(set of keys in \\begin{nd}[...], body without the options)."""
    m = ND_OPTIONS.match(body)
    if not m:
        return set(), body
    keys = {kv.split("=")[0].strip() for kv in m.group(1).split(",")}
    for kv in m.group(1).split(","):
        if kv.split("=")[0].strip() == "schema" and "=" in kv and kv.split("=", 1)[1].strip() == "false":
            keys.discard("schema")
    return keys, " " * m.end() + body[m.end():]


def check_text(text: str):
    """(errors, notes, counts) for one file: errors/notes are (lineno, message)."""
    errors, notes = [], []
    counts = {"derivations": 0, "expected_invalid": 0, "schema": 0, "tables": 0}
    for m in ND.finditer(text):
        lineno = text.count("\n", 0, m.start(1)) + 1
        counts["derivations"] += 1
        marker = block_marker(text, m.start())
        keys, body = nd_options(m.group(1))
        schema = marker == "schema" or "schema" in keys
        if schema and marker != "expect-invalid":
            counts["schema"] += 1
        try:
            lines, boxes, struct = parse_nd(body, lineno, schema_key="schema" in keys)
            errs, nts = check_derivation(lines, boxes, schema=schema) if lines else ([], [])
            errs = struct + errs
        except ParseError as e:
            errs, nts = [(lineno, f"cannot read derivation: {e}")], []
        if marker == "expect-invalid":
            counts["expected_invalid"] += 1
            if errs:
                nts = nts + [(lineno, f"expected invalid, and is: {errs[0][1]}"
                                      + (f" (+{len(errs) - 1} more)" if len(errs) > 1 else ""))]
                errs = []
            else:
                errs = [(lineno, "marked % expect-invalid but checks clean")]
        errors += errs
        notes += nts
    for m in ARRAY.finditer(text):
        lineno = text.count("\n", 0, m.start()) + 1
        res = check_truth_table(m.group(1), lineno)
        if res is None:
            continue
        counts["tables"] += 1
        errors += res[0]
        notes += res[1]
    return errors, notes, counts


def find_violations(root: Path):
    """Check every .md under `root` (a file or directory).

    Returns (errors, notes, counts); errors and notes are (path, lineno, message).
    """
    root = Path(root)
    files = [root] if root.is_file() else sorted(root.rglob("*.md"))
    errors, notes = [], []
    total = {"derivations": 0, "expected_invalid": 0, "schema": 0, "tables": 0}
    for f in files:
        e, n, c = check_text(f.read_text(encoding="utf-8"))
        errors += [(f, ln, msg) for ln, msg in e]
        notes += [(f, ln, msg) for ln, msg in n]
        for k in total:
            total[k] += c[k]
    return errors, notes, total


def report(items) -> str:
    return "\n".join(f"{p}:{ln}: {msg}" for p, ln, msg in items)


def main(argv=None) -> int:
    argv = series.enter_book(argv)
    ap = argparse.ArgumentParser(
        description="Check Fitch derivations (nd blocks) and truth tables in the book's source.",
        epilog="Mark a deliberately flawed derivation with '% expect-invalid' before \\begin{nd}, "
               "a rule schema or partial derivation with '% schema'.")
    ap.add_argument("paths", nargs="*", default=["src"], help="files or directories (default: src)")
    ap.add_argument("--notes", action="store_true", help="also list what was skipped and why")
    series.add_book_arg(ap)
    args = ap.parse_args(argv)
    errors, notes, total = [], [], {"derivations": 0, "expected_invalid": 0, "schema": 0, "tables": 0}
    for p in args.paths:
        e, n, c = find_violations(Path(p))
        errors += e
        notes += n
        for k in total:
            total[k] += c[k]
    if args.notes and notes:
        print(report(notes))
        print()
    if errors:
        print(report(errors))
    print(f"\n{total['derivations']} derivation(s) ({total['expected_invalid']} marked "
          f"expect-invalid, {total['schema']} schema), {total['tables']} truth table(s): {len(errors)} error(s), "
          f"{len(notes)} note(s){'' if args.notes else ' (--notes to list)'}.")
    return 1 if errors else 0


def run(book, labels):
    """The engine's check plugin protocol (build/plugins.py): (errors, warnings). Every invalid
    derivation or truth table is an error, as `./build.py check` had it before the plugin hook."""
    errors, _, _ = find_violations(book.src_dir)
    root = Path(book.root).resolve()
    return report([(Path(p).resolve().relative_to(root), n, m) for p, n, m in errors]).splitlines(), []

if __name__ == "__main__":
    sys.exit(main())
