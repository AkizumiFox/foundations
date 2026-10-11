"""exm-chaining-derivation (Section 1.2): the three Tr derivations, the alternative in (c),
and the Quick checks after the example (citation order; the sequent of (c))."""
import pathlib
import sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _toyrules import is_derivation, tr_instance

QUOTED = {
    "(a) is a derivation with Tr": True,
    "(b) is a derivation with Tr": True,
    "(c) is a derivation with Tr": True,
    "(c) alternative is a derivation with Tr": True,
    "lines": 5,
}

a = [("0 < x", None, ()), ("x < y", None, ()), ("y < 1", None, ()),
     ("0 < y", "Tr", (1, 2)), ("0 < 1", "Tr", (4, 3))]
b = [("y < 1", None, ()), ("0 < x", None, ()), ("x < y", None, ()),
     ("0 < y", "Tr", (2, 3)), ("0 < 1", "Tr", (4, 1))]
c = [("u < v", None, ()), ("w < z", None, ()), ("v < w", None, ()),
     ("v < z", "Tr", (3, 2)), ("u < z", "Tr", (1, 4))]
c_alt = [("u < v", None, ()), ("w < z", None, ()), ("v < w", None, ()),
         ("u < w", "Tr", (1, 3)), ("u < z", "Tr", (4, 2))]
for name, d in (("(a)", a), ("(b)", b), ("(c)", c), ("(c) alternative", c_alt)):
    assert is_derivation(d, rules=("Tr",)) == QUOTED[f"{name} is a derivation with Tr"], name
    assert len(d) == QUOTED["lines"]
# (b): "Tr 1, 4" for line 5 would be wrong
assert not tr_instance(b[0][0], b[3][0], "0 < 1")
# Quick check: line 1 is 0 < x, line 3 is x < 1
assert tr_instance("0 < x", "x < 1", "0 < 1")
assert not tr_instance("x < 1", "0 < x", "0 < 1")
# the instance and non-instances after def-rule-schema, and the warning
assert tr_instance("0 < 1/2", "1/2 < 1", "0 < 1")
assert not tr_instance("0 < 1/2", "1/3 < 1", "0 < 1")
assert not tr_instance("0 < 2/4", "1/2 < 1", "0 < 1")
# the false-premise warning: 1 < 0, 0 < -1 give 1 < -1 by Tr
assert tr_instance("1 < 0", "0 < -1", "1 < -1")
print("exm-chaining-derivation: all checks pass")
