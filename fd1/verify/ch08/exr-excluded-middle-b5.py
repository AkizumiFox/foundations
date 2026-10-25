"""exr-excluded-middle-b5 (Section 8.7): the three sequents are classically valid (truth
tables), and the printed derivations have 13, 10 and 10 lines, use no RAA, not-not-E, LEM
or TAUT line and cite no result. (Each derivation is also checked by tools/check_fitch.py.)"""
import itertools
import pathlib
import re

QUOTED = {"lines": [13, 10, 10]}

imp = lambda a, b: (not a) or b
seqs = [
    (lambda P, Q: [not (P and Q)], lambda P, Q: not (not ((not P) or (not Q)))),
    (lambda P, Q: [imp(P, Q)], lambda P, Q: not (not ((not P) or Q))),
    (lambda P, Q: [], lambda P, Q: imp(P or not P, imp(not (not P), P))),
]
for prem, concl in seqs:
    for P, Q in itertools.product([True, False], repeat=2):
        if all(prem(P, Q)):
            assert concl(P, Q)

src = pathlib.Path("src/ch08-from-derivations-to-prose/07-excluded-middle.md").read_text()
part = src.split("{#exr-excluded-middle-b5}")[1].split("{#exr-excluded-middle-c1}")[0]
blocks = [b.split("\\end{nd}")[0] for b in part.split("\\begin{nd}")[1:]]
assert len(blocks) == 3
for blk, n in zip(blocks, QUOTED["lines"]):
    nums = [int(x) for x in re.findall(r"\\(?:hypo|have)\s*\{(\d+)\}", blk)]
    assert nums == list(range(1, n + 1)), nums
    assert not re.search(r"\\(raa|nne|lem|taut)\b|\\by\{", blk)
print("exr-excluded-middle-b5: all quoted values check")
