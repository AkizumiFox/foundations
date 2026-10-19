"""exr-formulas-and-parse-trees-a2 (Ch 4, Section 4.1): the twelve-part drill, the length 5 of
(p -> q) in "Two languages", and the two derivations of "Letters, metavariables and substitution"
(the printed substitution instance and drill (l)), each checked by tools/check_fitch.py on a copy
transcribed to capital letters (the checker reads capitals only)."""
import re
import subprocess
import sys
import tempfile
from itertools import combinations
from pathlib import Path

from _s0102_formulas import tok, is_formula, parse, subformulas, BINARY

HERE = Path(__file__).resolve().parent
FD1 = HERE.parent.parent
SECTION = FD1 / "src/ch04-semantics-soundness-completeness/01-formulas-and-parse-trees.md"

QUOTED = {
    "two languages: length of (p -> q)": 5,
    "(c) symbols": 10,
    "(f) subformulas among the four": [r"(p \wedge q)", "r"],
    "(g) answer": r"(p \wedge \neg q)",
    "(h) deletions": 4, "(h) answer": r"\neg p",
    "(i) answers": [r"((p \vee q) \vee r)", r"(p \vee (q \vee r))"],
    "(j) answer": r"((\neg p \vee q) \to r)",
    "(k) leaves": ["p", "q", "p"],
    "(l) lines": [r"q \to q", r"q \to p", "q", "q", "p", r"q \to p"],
}

assert len(tok(r"(p \to q)")) == QUOTED["two languages: length of (p -> q)"]
# (a), (b)
assert is_formula(tok(r"\neg\neg\neg p"))
assert not is_formula(tok(r"(p \wedge (q))")) and len(tok("(q)")) == 3
# (c)
assert len(tok(r"((p \to q) \vee \neg r)")) == QUOTED["(c) symbols"]
# (e)
assert parse(tok(r"(\neg(p \wedge q) \to r)"))[0] == "imp"
# (f)
big = tok(r"((p \wedge q) \to r)")
cands = [r"(p \wedge q)", r"(q \to r)", "r"]
assert [c for c in cands if tok(c) in subformulas(big)] == QUOTED["(f) subformulas among the four"]
assert is_formula(tok(r"(q \to r)")) and not is_formula(tok(r"q) \to r"))
# (g): the only one-symbol insertion giving a formula
SYMS = ["p", "q", "r", "bot", "neg", "(", ")"] + list(BINARY)
s = tok(r"(p \wedge \neg q")
found = {s[:i] + (x,) + s[i:] for i in range(len(s) + 1) for x in SYMS if is_formula(s[:i] + (x,) + s[i:])}
assert found == {tok(QUOTED["(g) answer"])}, found
# (h): fewest deletions
s = tok(r"((\neg p))")
best = None
for k in range(len(s) + 1):
    keep = {tuple(s[i] for i in idx) for idx in combinations(range(len(s)), len(s) - k)}
    good = [t for t in keep if is_formula(t)]
    if good:
        best = (k, set(good))
        break
assert best == (QUOTED["(h) deletions"], {tok(QUOTED["(h) answer"])}), best
# (i): inserting one pair of parentheses; exactly the two groupings arise
s = tok(r"(p \vee q \vee r)")
res = set()
for i in range(len(s) + 1):
    for j in range(i, len(s) + 1):
        t = s[:i] + ("(",) + s[i:j] + (")",) + s[j:]
        if is_formula(t):
            res.add(t)
assert res == {tok(x) for x in QUOTED["(i) answers"]}, res
# (j)
assert is_formula(tok(QUOTED["(j) answer"]))
assert parse(tok(QUOTED["(j) answer"]))[0] == "imp"
# (k): leaves of (p -> (q -> p)), left to right
k = tok(r"(p \to (q \to p))")
assert [t for t in k if t in ("p", "q", "r")] == QUOTED["(k) leaves"]

# the derivations: read the nd blocks printed in the section
text = SECTION.read_text()
blocks = re.findall(r"\\begin\{nd\}(.*?)\\end\{nd\}", text, re.S)
assert len(blocks) == 2, len(blocks)
orig, inst = blocks


def subst(block, mapping):
    alts = "|".join(sorted(map(re.escape, mapping), key=len, reverse=True))
    pat = re.compile(r"(?<![\\A-Za-z])(?:" + alts + r")(?![A-Za-z_])")
    return pat.sub(lambda m: mapping[m.group(0)], block)


def fitch_ok(block):
    with tempfile.TemporaryDirectory() as d:
        f = Path(d) / "check.md"
        f.write_text("```{=latex}\n$\\begin{nd}" + block + "\\end{nd}$\n```\n")
        r = subprocess.run([sys.executable, str(FD1.parent / "tools/check_fitch.py"), str(f)],
                           cwd=FD1, capture_output=True, text=True)
        out = r.stdout + r.stderr
        m = re.search(r"(\d+) derivation\(s\).*?(\d+) error\(s\)", out, re.S)
        return r.returncode == 0 and m and m.group(1) == "1" and m.group(2) == "0", out


# the printed instance: p_1, p_2 -> P, Q; it must be exactly the original with the substitution
ok, out = fitch_ok(subst(inst, {"p_1": "P", "p_2": "Q"}))
assert ok, out
expected_inst = subst(orig, {"P": r"(p_1 \wedge p_2)", "Q": r"\neg p_1", "R": r"(p_2 \vee p_1)"})
norm = lambda b: re.sub(r"\s+", "", b)
# the printed instance drops the outer parentheses of a whole line (shorthand rule 1)
for a, b in zip(inst.strip().splitlines(), expected_inst.strip().splitlines()):
    a, b = norm(a), norm(b)
    if a != b:
        # allowed difference: one outer pair around a whole line
        assert a.replace("{(p_1\\wedgep_2)}", "{p_1\\wedgep_2}").replace("{(p_2\\veep_1)}", "{p_2\\veep_1}") == b.replace("{(p_1\\wedgep_2)}", "{p_1\\wedgep_2}").replace("{(p_2\\veep_1)}", "{p_2\\veep_1}"), (a, b)

# drill (l): q for P, q for Q, p for R; lines as quoted; checked in capitals (q -> Q, p -> P)
lower = subst(orig, {"P": "q", "Q": "q", "R": "p"})
got = re.findall(r"\\(?:hypo|have)\s*\{\d+\}\s*\{([^}]*)\}", lower)
assert [norm(x) for x in got] == [norm(x) for x in QUOTED["(l) lines"]], got
ok, out = fitch_ok(subst(lower, {"q": "Q", "p": "P"}))
assert ok, out
print("exr-formulas-and-parse-trees-a2: all quoted values check")
