"""Helpers for the Section 3.6 and 3.7 sidecars (not run on its own: the name starts with _).

Formulas are parsed with tools/check_fitch.py's parser after mapping the book's lowercase
atoms p, q, r, s, e, a, b and the metavariables alpha, beta to capital letters. Row
citations \\by{$(tag)$}{refs} in derivations are checked against the sequents of
lem-connective-rows by matching the cited lines and the line itself to the schema.
"""
import itertools
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import check_fitch as cf  # noqa: E402

S06 = ROOT / "src/ch03-semantics-soundness-completeness/06-completeness.md"
S07 = ROOT / "src/ch03-semantics-soundness-completeness/07-normal-forms.md"


def upper(text):
    text = text.replace(r"\alpha", "A").replace(r"\beta", "B")
    return re.sub(r"(?<![A-Za-z\\])([pqrsabe])(?![A-Za-z])", lambda m: m.group(1).upper(), text)


def parse(text):
    return cf.parse_formula(upper(text))


def atoms(f, acc=None):
    acc = set() if acc is None else acc
    if f[0] == "var":
        acc.add(f[1])
    elif f[0] != "bot":
        for g in f[1:]:
            atoms(g, acc)
    return acc


def value(f, env):
    return cf.evaluate(f, env)


def rows(letters):
    for vals in itertools.product([True, False], repeat=len(letters)):
        yield dict(zip(letters, vals))


def entails(premises, concl):
    fs = [parse(x) if isinstance(x, str) else x for x in premises]
    c = parse(concl) if isinstance(concl, str) else concl
    letters = sorted(set().union(*(atoms(g) for g in fs + [c])))
    return all(value(c, env) for env in rows(letters) if all(value(g, env) for g in fs))


def equivalent(x, y):
    return entails([x], y) and entails([y], x)


def tautology(x):
    return entails([], x)


def truth_rows(x, letters):
    f = parse(x)
    return [value(f, env) for env in rows(letters)]


# The sequents of lem-connective-rows, with A, B for alpha, beta.
ROWS = {
    "(\\neg 1)": (["A"], "\\neg\\neg A"),
    "(\\bot 1)": ([], "\\neg\\bot"),
    "(\\wedge 1)": (["A", "B"], "A \\wedge B"),
    "(\\wedge 2)": (["\\neg A"], "\\neg(A \\wedge B)"),
    "(\\wedge 3)": (["\\neg B"], "\\neg(A \\wedge B)"),
    "(\\vee 1)": (["A"], "A \\vee B"),
    "(\\vee 2)": (["B"], "A \\vee B"),
    "(\\vee 3)": (["\\neg A", "\\neg B"], "\\neg(A \\vee B)"),
    "({\\to}1)": (["\\neg A"], "A \\to B"),
    "({\\to}2)": (["B"], "A \\to B"),
    "({\\to}3)": (["A", "\\neg B"], "\\neg(A \\to B)"),
    "({\\leftrightarrow}1)": (["A", "B"], "A \\leftrightarrow B"),
    "({\\leftrightarrow}2)": (["\\neg A", "\\neg B"], "A \\leftrightarrow B"),
    "({\\leftrightarrow}3)": (["A", "\\neg B"], "\\neg(A \\leftrightarrow B)"),
    "({\\leftrightarrow}4)": (["\\neg A", "B"], "\\neg(A \\leftrightarrow B)"),
}


def match(pat, f, sub):
    """Match formula tree f against pattern tree pat with metavariables A, B."""
    if pat[0] == "var" and pat[1] in "AB":
        if pat[1] in sub:
            return sub[pat[1]] == f
        sub[pat[1]] = f
        return True
    if pat[0] != f[0] or len(pat) != len(f):
        return False
    if pat[0] in ("var",):
        return pat == f
    return all(match(p, g, sub) for p, g in zip(pat[1:], f[1:]))


def check_row_instance(tag, cited, concl):
    prem, c = ROWS[tag]
    prem = [cf.parse_formula(x) for x in prem]
    c = cf.parse_formula(c)
    if len(prem) != len(cited):
        return False
    sub = {}
    if not match(c, concl, sub):
        return False
    return all(match(p, g, sub) for p, g in zip(prem, cited))


ND = re.compile(r"\\begin\{nd\}(.*?)\\end\{nd\}", re.S)
LINE = re.compile(r"\\(hypo|have)\s*\{([^}]*)\}\s*\{(.*?)\}\s*(\\by\{(.*?)\}\{([^}]*)\}|\\[a-z]+\{[^}]*\})?\s*$")


def block(path, label, stop=None):
    """Text from the {#label} block to the next labelled block (or to `stop`)."""
    s = Path(path).read_text()
    i = s.index("{#" + label)
    j = s.find("::: {#", i + 5)
    if stop:
        j = s.index(stop, i)
    return s[i:j if j > 0 else len(s)]


def derivations(text):
    out = []
    for m in ND.finditer(text):
        lines = {}
        order = []
        for raw in m.group(1).split("\n"):
            raw = raw.strip()
            if not raw.startswith("\\hypo") and not raw.startswith("\\have"):
                continue
            # split: \have {n} {formula} justification
            g = re.match(r"\\(hypo|have)\s*\{([^}]*)\}\s*\{", raw)
            k = g.end()
            depth = 1
            while depth:
                depth += {"{": 1, "}": -1}.get(raw[k], 0)
                k += 1
            formula = raw[g.end():k - 1]
            just = raw[k:].strip()
            lines[g.group(2)] = (formula, just)
            order.append(g.group(2))
        out.append((order, lines))
    return out


def check_rows_in(text):
    """Every \\by{$(tag)$}{refs} line in the derivations of `text` is an instance of its row."""
    n = 0
    for order, lines in derivations(text):
        for lab in order:
            formula, just = lines[lab]
            m = re.match(r"\\by\{\$(.*?)\$\}\{([^}]*)\}", just)
            if not m or m.group(1) not in ROWS:
                continue
            cited = [parse(lines[r.strip()][0]) for r in m.group(2).split(",") if r.strip()]
            assert check_row_instance(m.group(1), cited, parse(formula)), (lab, formula, just)
            n += 1
    return n


def count_lines(text, k=0):
    return len(derivations(text)[k][0])
