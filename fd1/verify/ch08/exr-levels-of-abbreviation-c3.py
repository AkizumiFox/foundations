"""exr-levels-of-abbreviation-c3 (Section 8.3): (2k)^2 = 4k^2; (2k + 1)^2 - 1 = 4k^2 + 4k =
4(k^2 + k); so 4 | n^2 or 4 | n^2 - 1 for every integer n (checked on |n| <= 500); the
solution's skeleton has 15 lines."""
import re
from pathlib import Path

QUOTED = {"skeleton lines": 15}
for k in range(-300, 301):
    assert (2 * k) ** 2 == 4 * k * k
    assert (2 * k + 1) ** 2 - 1 == 4 * k * k + 4 * k == 4 * (k * k + k)
for n in range(-500, 501):
    assert (n * n) % 4 == 0 or (n * n - 1) % 4 == 0
ROOT = Path(__file__).resolve().parents[2]
SEC = (ROOT / "src/ch08-from-derivations-to-prose/03-levels-of-abbreviation.md").read_text()
part = SEC[SEC.index("{#exr-levels-of-abbreviation-c3}"):]
blk = re.findall(r"\\begin\{nd\}(.*?)\\end\{nd\}", part, re.S)[0]
assert len(re.findall(r"\\(?:hypo|have)\s*\{(\d+)\}", blk)) == QUOTED["skeleton lines"]
print("exr-levels-of-abbreviation-c3: all quoted values check")
