"""Helper for the Chapter 3 sidecars of Sections 3.1-3.2: formulas as token strings.

A formula is a tuple of tokens: atoms ('p', 'q', 'r', 's', 'p_1', ...), 'bot', 'neg',
the binary connectives 'and', 'or', 'imp', 'iff', and the parentheses '(' and ')'.
`is_formula` decides membership by the grammar of def-formula directly (trying every
split), independently of the book's lemmas, so the sidecars can test those lemmas.
"""
from functools import lru_cache
from itertools import product

BINARY = ("and", "or", "imp", "iff")
LATEX = {
    r"\wedge": "and", r"\vee": "or", r"\to": "imp", r"\leftrightarrow": "iff",
    r"\neg": "neg", r"\bot": "bot",
}


def tok(src):
    """Tokenize a LaTeX-ish formula string such as r'(\\neg p \\vee q)'."""
    out, i = [], 0
    while i < len(src):
        c = src[i]
        if c.isspace():
            i += 1
        elif c in "()":
            out.append(c)
            i += 1
        elif c == "\\":
            j = i + 1
            while j < len(src) and src[j].isalpha():
                j += 1
            out.append(LATEX[src[i:j]])
            i = j
        elif c.isalpha():
            j = i + 1
            if src[j:j + 1] == "_":
                j += 2
            out.append(src[i:j])
            i = j
        else:
            raise ValueError(src)
    return tuple(out)


def is_atom(t):
    return t not in BINARY and t not in ("neg", "bot", "(", ")")


@lru_cache(maxsize=None)
def splits(s):
    """All ways s is built by its last clause: list of ('atom',), ('neg', phi), (op, phi, psi)."""
    res = []
    if len(s) == 1 and (s[0] == "bot" or is_atom(s[0])):
        res.append(("base",))
    if len(s) >= 2 and s[0] == "neg" and is_formula(s[1:]):
        res.append(("neg", s[1:]))
    if len(s) >= 5 and s[0] == "(" and s[-1] == ")":
        for k in range(2, len(s) - 2):
            if s[k] in BINARY and is_formula(s[1:k]) and is_formula(s[k + 1:-1]):
                res.append((s[k], s[1:k], s[k + 1:-1]))
    return tuple(res)


@lru_cache(maxsize=None)
def is_formula(s):
    return len(splits(s)) > 0


def parse(s):
    sp = splits(s)
    assert len(sp) == 1, (s, sp)
    return sp[0]


def height(s):
    sp = parse(s)
    if sp[0] == "base":
        return 1
    if sp[0] == "neg":
        return 1 + height(sp[1])
    return 1 + max(height(sp[1]), height(sp[2]))


def nodes(s):
    sp = parse(s)
    if sp[0] == "base":
        return 1
    if sp[0] == "neg":
        return 1 + nodes(sp[1])
    return 1 + nodes(sp[1]) + nodes(sp[2])


def subformulas(s):
    sp = parse(s)
    out = {s}
    for part in sp[1:]:
        out |= subformulas(part)
    return out


def atoms(s):
    return {t for t in s if is_atom(t)}


def connectives(s):
    return sum(1 for t in s if t in BINARY or t == "neg")


def excess(s):
    return s.count("(") - s.count(")")


def all_formulas(max_len, atom_list=("p", "q"), ops=BINARY):
    """Every formula of length <= max_len over the given atoms, bot and connectives."""
    by_len = {1: [(a,) for a in atom_list] + [("bot",)]}
    for n in range(2, max_len + 1):
        cur = [("neg",) + f for f in by_len.get(n - 1, [])]
        for a in range(1, n - 3):
            b = n - 3 - a
            for f, g in product(by_len.get(a, []), by_len.get(b, [])):
                for op in ops:
                    cur.append(("(",) + f + (op,) + g + (")",))
        by_len[n] = cur
    return [f for n in sorted(by_len) for f in by_len[n]]
