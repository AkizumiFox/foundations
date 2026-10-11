"""exr-derivations-c2 (Section 1.2): the student's list fails only because line 5 cites
line 6; the reordered list is a derivation; the two-line loop consists of Tr instances."""
import pathlib
import sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _toyrules import check_line, is_derivation, tr_instance

QUOTED = {"failing line": 5, "cited later line": 6, "repaired is a derivation": True}
prem = [("0 < 1", None, ()), ("1 < 2", None, ()), ("2 < 3", None, ()), ("3 < 4", None, ())]
student = prem + [("0 < 3", "Tr", (6, 3)), ("0 < 2", "Tr", (1, 2)), ("0 < 4", "Tr", (5, 4))]
assert not is_derivation(student, ("Tr",))
bad = [k for k in range(5, 8) if not all(check_line(student, k, ("Tr",)))]
assert bad == [QUOTED["failing line"]]
assert check_line(student, 5, ("Tr",)) == (True, True, False)
assert QUOTED["cited later line"] in student[4][2]
repaired = prem + [("0 < 2", "Tr", (1, 2)), ("0 < 3", "Tr", (5, 3)), ("0 < 4", "Tr", (6, 4))]
assert is_derivation(repaired, ("Tr",)) == QUOTED["repaired is a derivation"]
assert tr_instance("0 < 0", "0 < 0", "0 < 0")
loop = [("0 < 0", "Tr", (2, 2)), ("0 < 0", "Tr", (1, 1))]
assert check_line(loop, 1, ("Tr",)) == (True, True, False)
assert check_line(loop, 2, ("Tr",)) == (True, True, True)
print("exr-derivations-c2: all checks pass")
