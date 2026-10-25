"""exr-kripke-models-b2 and exr-kripke-models-c1 (Section 8.8): every claim of B2 and
C1 (b) is classically valid (truth tables), so a TAUT line would "derive" each; the
printed derivations of B2 (a), (b), (d), (f) and C1 (a) have 16, 13, 9, 9 and 12 lines
and contain no RAA, not-not-E, LEM or TAUT line. (Their shapes are checked by
tools/check_fitch.py; the countermodels of (c), (e), (g) and C1 (b) by kripke.py.)"""
import itertools
import pathlib
import re

QUOTED = {"b2_lines": [16, 13, 9, 9], "c1_lines": [12]}

imp = lambda a, b: (not a) or b
claims = {
    "a": (lambda p, q: [not (not (p and q))], lambda p, q: (not (not p)) and (not (not q))),
    "b": (lambda p, q: [(not (not p)) and (not (not q))], lambda p, q: not (not (p and q))),
    "c": (lambda p, q: [not (not (p or q))], lambda p, q: (not (not p)) or (not (not q))),
    "d": (lambda p, q: [imp(imp(p, q), p)], lambda p, q: not (not p)),
    "e": (lambda p, q: [imp(not p, p)], lambda p, q: p),
    "f": (lambda p, q: [(p or q) and (not p)], lambda p, q: q),
    "g": (lambda p, q: [imp(p, q) and imp(not p, q)], lambda p, q: q),
    "c1a": (lambda p, q: [p or not p], lambda p, q: imp(imp(imp(p, q), p), p)),
    "c1b": (lambda p, q: [], lambda p, q: imp(imp(imp(imp(p, q), p), p), p or not p)),
}
for name, (prem, concl) in claims.items():
    for p, q in itertools.product([True, False], repeat=2):
        if all(prem(p, q)):
            assert concl(p, q), name

src = pathlib.Path("src/ch08-from-derivations-to-prose/08-kripke-models.md").read_text()
def blocks(start, end):
    part = src.split(start)[1].split(end)[0]
    return [b.split("\\end{nd}")[0] for b in part.split("\\begin{nd}")[1:]]
for blks, lens in [(blocks("{#exr-kripke-models-b2}", "{#exr-kripke-models-c1}"), QUOTED["b2_lines"]),
                   (blocks("{#exr-kripke-models-c1}", "{#exr-kripke-models-c2}"), QUOTED["c1_lines"])]:
    assert len(blks) == len(lens)
    for blk, n in zip(blks, lens):
        nums = [int(x) for x in re.findall(r"\\(?:hypo|have)\s*\{(\d+)\}", blk)]
        assert nums == list(range(1, n + 1)), nums
        assert not re.search(r"\\(raa|nne|lem|taut)\b|\\by\{", blk)
print("exr-kripke-models-b2: all quoted values check")
