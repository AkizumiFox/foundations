"""exr-levels-of-abbreviation-c2 (exit check): for c != 0 and eps > 0, eps/|c| > 0, and
|a - L| < eps/|c| gives |c a - c L| = |c| |a - L| < eps; for c = 0 every N works. The
level-0 derivation has 17 lines. Exact rational arithmetic on a grid."""
import re
from fractions import Fraction as Fr
from pathlib import Path

QUOTED = {"derivation lines": 17, "N for c = 0": 0}
grid = [Fr(a, b) for a in range(-7, 8) for b in (1, 2, 3, 5)]
for c in grid:
    for eps in [Fr(1, 100), Fr(1, 3), Fr(2), Fr(7, 2)]:
        if c != 0:
            assert eps / abs(c) > 0
            for d in [Fr(0), eps / abs(c) / 2, eps / abs(c) * Fr(99, 100), -eps / abs(c) / 3]:
                a, L = Fr(5) + d, Fr(5)                     # |a - L| = |d| < eps/|c|
                assert abs(a - L) < eps / abs(c)
                assert abs(c * a - c * L) == abs(c) * abs(a - L) < eps
        else:
            for a in grid:
                assert abs(c * a - c * Fr(3)) == 0 < eps
ROOT = Path(__file__).resolve().parents[2]
SEC = (ROOT / "src/ch05-from-derivations-to-prose/03-levels-of-abbreviation.md").read_text()
part = SEC[SEC.index("{#exr-levels-of-abbreviation-c2}"):]
blk = re.findall(r"\\begin\{nd\}(.*?)\\end\{nd\}", part, re.S)[0]
assert len(re.findall(r"\\(?:hypo|have)\s*\{(\d+)\}", blk)) == QUOTED["derivation lines"]
print("exr-levels-of-abbreviation-c2: all quoted values check")
