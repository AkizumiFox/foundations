"""exr-derivations-b2 (Section 1.2): which candidate lines 4 are justified."""
import pathlib
import sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _toyrules import check_line

QUOTED = {"(a)": True, "(b)": True, "(c)": False, "(d)": True, "(e)": False, "(f)": True}
prem = [("0 < x", None, ()), ("x < 3", None, ()), ("3 < y", None, ())]
cands = {
    "(a)": ("0 < 3", "Tr", (1, 2)),
    "(b)": ("x < y", "Tr", (2, 3)),
    "(c)": ("0 < y", "Tr", (1, 3)),
    "(d)": ("0 + 2 < x + 2", "Sh", (1,)),
    "(e)": ("x + 1 < 3 + 2", "Sh", (2,)),
    "(f)": ("x + y < 3 + y", "Sh", (2,)),
}
for key, line in cands.items():
    assert all(check_line(prem + [line], 4)) == QUOTED[key], key
# (c) is derivable in two steps: 0 < 3 by Tr 1, 2, then 0 < y by Tr with line 3
two = prem + [("0 < 3", "Tr", (1, 2)), ("0 < y", "Tr", (4, 3))]
assert all(check_line(two, 5))
print("exr-derivations-b2: all checks pass")
