"""exm-not-a-derivation (Section 1.2): each change fails exactly one of the three questions."""
import pathlib
import sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _toyrules import check_line, is_derivation

QUOTED = {"(a) is a derivation": False, "(b) is a derivation": False}

prem = [("0 < x", None, ()), ("x < y", None, ()), ("y < 1", None, ())]
swapped = prem + [("0 < 1", "Tr", (5, 3)), ("0 < y", "Tr", (1, 2))]
roles = prem + [("0 < y", "Tr", (1, 2)), ("0 < 1", "Tr", (3, 4))]
assert is_derivation(swapped, ("Tr",)) == QUOTED["(a) is a derivation"]
assert is_derivation(roles, ("Tr",)) == QUOTED["(b) is a derivation"]
# (a): line 4 passes rule and instance, fails 'earlier'; line 5 passes all three
assert check_line(swapped, 4, ("Tr",)) == (True, True, False)
assert check_line(swapped, 5, ("Tr",)) == (True, True, True)
# (b): line 5 passes rule and 'earlier', fails instance
assert check_line(roles, 5, ("Tr",)) == (True, False, True)
assert check_line(roles, 4, ("Tr",)) == (True, True, True)
print("exm-not-a-derivation: all checks pass")
