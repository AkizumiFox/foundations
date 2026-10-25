"""def-levels-of-proof (Section 8.3, the opening "One short proof, four texts"):
(2k + 1)^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1, so the square of an odd integer is odd with
witness 2k^2 + 2k; the skeleton has 7 lines and the full derivation 8; in the skeleton the
lines without words in the plain prose are the three closings 5, 6, 7."""
import re
from pathlib import Path

QUOTED = {"skeleton lines": 7, "full lines": 8, "closings": [5, 6, 7]}
for k in range(-200, 201):
    n = 2 * k + 1
    assert n * n == 4 * k * k + 4 * k + 1 == 2 * (2 * k * k + 2 * k) + 1
    assert (n * n) % 2 == 1
ROOT = Path(__file__).resolve().parents[2]
SEC = (ROOT / "src/ch08-from-derivations-to-prose/03-levels-of-abbreviation.md").read_text()
head = SEC[:SEC.index("{#def-levels-of-proof}")]
sk, full = re.findall(r"\\begin\{nd\}(.*?)\\end\{nd\}", head, re.S)[:2]
num = lambda b: [int(m) for m in re.findall(r"\\(?:hypo|have)\s*\{(\d+)\}", b)]
assert num(sk) == list(range(1, QUOTED["skeleton lines"] + 1))
assert num(full) == list(range(1, QUOTED["full lines"] + 1))
closing = [int(m.group(1)) for m in re.finditer(r"\\have\s*\{(\d+)\}[^\n]*\\(?:Ee|ii|Ai)\{", sk)]
assert closing == QUOTED["closings"], closing
print("def-levels-of-proof: all quoted values check")
