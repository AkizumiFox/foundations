"""exr-from-argument-to-derivation-b1 (Ch 3 s03): the facts of (a)-(c) on grids; the three sequents valid."""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s05s06_logic import *  # noqa: E402,F401,F403

QUOTED = {"lines": {"a": 6, "b": 3, "c": 10}}
grid = [Fr(k, 8) for k in range(-80, 81)]
for x in grid:
    if x > 1:
        assert x * x > x                      # (a) A -> C
    if x < 0:
        assert x * x > 0 > x                  # (a) B -> C
    if x * x <= x:                            # the paragraph's conclusion holds
        assert 0 <= x <= 1
for k in range(-200, 201):
    assert (2 * k) ** 2 == 2 * (2 * k * k)    # (b)
    if (k * k) % 2 == 1:
        assert k % 2 == 1
for a in grid:
    for b in grid[::7]:
        if a * b == 0 and a != 0:
            assert b == (1 / a) * (a * b) == 0  # (c)
A, B, C, E, S, Z = V("A"), V("B"), V("C"), V("E"), V("S"), V("Z")
assert classically_valid([Imp(A, C), Imp(B, C), Not(C)], And(Not(B), Not(A)))
assert classically_valid([Imp(E, S), Not(S)], Not(E))
assert not classically_valid([Imp(Not(E), Not(S)), Not(S)], Not(E))   # the wrong supply gives nothing
assert classically_valid([Imp(And(Z, Not(A)), B), Z], Or(A, B))
print("exr-from-argument-to-derivation-b1: ok")
