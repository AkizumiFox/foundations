"""exr-models-r1 (Section 4.11): (p -> q) -> r |/= p -> r with the unique refuting row
p = T, q = F, r = F; (p -> q) -> r |= q -> r; the printed derivation has 7 lines."""
import re
import sys
sys.path.insert(0, "verify/ch03")
import _logic as L

QUOTED = {"lines": 7}
rows = [L.tv(r, "p", "q", "r") for r in L.entails([r"(p \to q) \to r"], r"p \to r")]
assert rows == [(True, False, False)]
assert not L.entails([r"(p \to q) \to r"], r"q \to r")
src = open("src/ch04-predicate-logic/11-models.md").read()
blk = src.split("{#exr-models-r1}")[1].split("{#exr-models-r2}")[0]
nd = blk.split(r"\begin{nd}")[1].split(r"\end{nd}")[0]
assert len(re.findall(r"\\(hypo|have)\s*\{", nd)) == QUOTED["lines"]
print("exr-models-r1: all quoted values check")
