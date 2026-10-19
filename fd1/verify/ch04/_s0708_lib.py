"""Helpers for the Section 4.7 and 4.8 sidecars (not run on its own: the name starts with _).

tools/check_fitch.py tokenizes only capital statement letters, so a derivation printed
with Chapter 4's lowercase atoms is checked here on a copy in which p, q, r, s become
P, Q, R, S inside every nd environment and nothing else changes (so the copy and the
printed block differ in the letters only, by construction). check() fails if a copied
derivation has an error, or if any of its lines was skipped as unreadable (which would
mean the copy was not really checked).
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / ".." / "tools"))
import check_fitch as cf  # noqa: E402

DIR = ROOT / "src/ch04-semantics-soundness-completeness"
S07 = DIR / "07-soundness.md"
S08 = DIR / "08-completeness.md"
ND = re.compile(r"\\begin\{nd\}.*?\\end\{nd\}", re.S)


def block(path, label):
    """From the {#label} block to the next labelled block (the solution included)."""
    s = Path(path).read_text()
    i = s.index("{#" + label)
    j = s.find("::: {#", i + 5)
    k = s.find("<!-- dependency ledger", i)
    ends = [x for x in (j, k) if x > 0]
    return s[i:min(ends) if ends else len(s)]


def between(path, start, stop):
    s = Path(path).read_text()
    i = s.index(start)
    return s[i:s.index(stop, i)]


def upper(text):
    def cap(m):
        return re.sub(r"(?<![A-Za-z\\])([pqrs])(?![A-Za-z])", lambda n: n.group(1).upper(), m.group(0))
    return ND.sub(cap, text)


def check(text, derivations=None, invalid=0):
    """Check every nd in `text` on a capital copy; return the check_text counts."""
    errors, notes, counts = cf.check_text(upper(text))
    assert not errors, errors
    bad = [n for n in notes if "not propositional" in n[1] or "cannot read" in n[1]]
    assert not bad, bad
    if derivations is not None:
        assert counts["derivations"] == derivations, counts
    assert counts["expected_invalid"] == invalid, counts
    return counts


def invalid_lines(text):
    """For each nd marked expect-invalid in `text`: the line labels its errors name."""
    out = []
    t = upper(text)
    for m in ND.finditer(t):
        if cf.block_marker(t, m.start()) != "expect-invalid":
            continue
        body = cf.nd_options(m.group(0)[len("\\begin{nd}"):-len("\\end{nd}")])[1]
        lines, boxes, struct = cf.parse_nd(body, 1)
        errs, _ = cf.check_derivation(lines, boxes)
        out.append(sorted({re.match(r"line (\S+):", e[1]).group(1) for e in struct + errs
                           if re.match(r"line (\S+):", e[1])}))
    return out


def boxes(text, k=0):
    """The boxes (first, last) of the k-th nd in `text`, by line label."""
    body = ND.findall(text)[k]
    out, stack, last = [], [], None
    for raw in body.split("\n"):
        raw = raw.strip()
        if raw.startswith("\\open"):
            stack.append(None)
        elif raw.startswith("\\close"):
            out.append((stack.pop(), last))
        else:
            m = re.match(r"\\(hypo|have)(?:\[[^\]]*\])*\s*\{([^}]*)\}", raw)
            if m and m.group(2):
                last = m.group(2)
                if stack and stack[-1] is None:
                    stack[-1] = last
    return sorted(out, key=lambda b: int(b[0]))


def tree_boxes(text):
    """The 'box a--b' ranges named in the tikzpicture trees of `text`."""
    return sorted({(a, b) for a, b in re.findall(r"box (\d+)--(\d+)", text)}, key=lambda b: int(b[0]))
