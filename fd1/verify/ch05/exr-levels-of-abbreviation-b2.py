"""exr-levels-of-abbreviation-b2: if n = 2k + 1 then n^2 - 1 = 4k(k + 1); k(k + 1) is
2 j(2j + 1) for k = 2j and 2 (2j + 1)(j + 1) for k = 2j + 1; 4 (2i) = 8i; the skeleton has
22 lines. Polynomial identities of degree <= 2 are checked at 61 points each."""
import re
from pathlib import Path

QUOTED = {"modulus": 8, "skeleton lines": 22}
R = range(-30, 31)
for k in R:
    n = 2 * k + 1
    assert n * n - 1 == 4 * k * (k + 1)
    assert (n * n - 1) % QUOTED["modulus"] == 0
for j in R:
    k = 2 * j
    assert k * (k + 1) == 2 * (j * (2 * j + 1))
    k = 2 * j + 1
    assert k * (k + 1) == 2 * ((2 * j + 1) * (j + 1))
for i in R:
    assert 4 * (2 * i) == 8 * i
ROOT = Path(__file__).resolve().parents[2]
SEC = (ROOT / "src/ch05-from-derivations-to-prose/03-levels-of-abbreviation.md").read_text()
part = SEC[SEC.index("{#exr-levels-of-abbreviation-b2}"):]
blk = re.findall(r"\\begin\{nd\}(.*?)\\end\{nd\}", part, re.S)[0]
assert len(re.findall(r"\\(?:hypo|have)\s*\{(\d+)\}", blk)) == QUOTED["skeleton lines"]
print("exr-levels-of-abbreviation-b2: all quoted values check")
