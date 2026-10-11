"""exr-models-r2 (Section 4.11): not(P -> not Q) |= notnot P and notnot Q; the printed
derivation has 15 lines and uses neither RAA nor notnot-E."""
import re
import sys
sys.path.insert(0, "verify/ch03")
import _logic as L

QUOTED = {"lines": 15}
assert not L.entails([r"\neg (p \to \neg q)"], r"\neg\neg p \wedge \neg\neg q")
src = open("src/ch04-predicate-logic/11-models.md").read()
blk = src.split("{#exr-models-r2}")[1].split("{#exr-models-r3}")[0]
nd = blk.split(r"\begin{nd}")[1].split(r"\end{nd}")[0]
assert len(re.findall(r"\\(hypo|have)\s*\{", nd)) == QUOTED["lines"]
assert r"\raa" not in nd and r"\nne" not in nd
print("exr-models-r2: all quoted values check")
