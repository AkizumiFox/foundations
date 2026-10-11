"""exr-derivations-a1 (Section 1.2): the justifications of (b) are forced; (c) fails only at
line 3 ('earlier'); (e) Tr and Sh preserve truth (sampled on exact rationals)."""
import itertools
import pathlib
import sys
from fractions import Fraction
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _toyrules import check_line, is_derivation, sh_instance, tr_instance

QUOTED = {"(b) line 6 adds": 2, "(c) failing line": 3, "(e) true": True}

prem = [("1 < x", None, ()), ("x < y", None, ()), ("y < 5", None, ())]
b = prem + [("x < 5", "Tr", (2, 3)), ("1 < 5", "Tr", (1, 4)),
            ("1 + 2 < 5 + 2", "Sh", (5,))]
assert is_derivation(b)
# uniqueness: no other citation of Tr/Sh justifies lines 4, 5, 6
for k in (4, 5, 6):
    stmt = b[k - 1][0]
    ok = []
    for i, j in itertools.product(range(1, k), repeat=2):
        if tr_instance(b[i - 1][0], b[j - 1][0], stmt):
            ok.append(("Tr", (i, j)))
    for i in range(1, k):
        if sh_instance(b[i - 1][0], stmt):
            ok.append(("Sh", (i,)))
    assert ok == [(b[k - 1][1], b[k - 1][2])], (k, ok)
c = [("0 < x", None, ()), ("x < 1", None, ()), ("0 + 1 < 1 + 1", "Sh", (4,)),
     ("0 < 1", "Tr", (1, 2))]
assert not is_derivation(c)
assert check_line(c, QUOTED["(c) failing line"]) == (True, True, False)
assert check_line(c, 4) == (True, True, True)
# (e): the rules lead from true to true, on a grid of exact rationals
pts = [Fraction(n, 4) for n in range(-12, 13)]
for a, bb, cc in itertools.product(pts, repeat=3):
    if a < bb and bb < cc:
        assert a < cc
    if a < bb:
        assert a + cc < bb + cc
print("exr-derivations-a1: all checks pass")
