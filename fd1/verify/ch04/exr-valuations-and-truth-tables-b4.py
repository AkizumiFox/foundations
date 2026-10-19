"""exr-valuations-and-truth-tables-b4 (Section 4.4): the three statements e, e -> f,
f or not e; the count of true ones in each row (three, one, two, two); only the row
e = T, f = F has exactly one; n = 2, 6, -10 are even and not divisible by 4 and make exactly
one statement true; (B) and (C) agree in every row."""
import sys
sys.path.insert(0, "verify/ch04")
import _logic as L

QUOTED = {"counts": [3, 1, 2, 2], "examples": [2, 6, -10]}
fs = [L.parse(s) for s in ["e", r"e \to f", r"f \vee \neg e"]]
counts = [sum(L.val(f, r) for f in fs) for r in L.rows("ef")]
assert counts == QUOTED["counts"]
assert [L.tv(r, "e", "f") for r in L.rows("ef") if sum(L.val(f, r) for f in fs) == 1] == [(True, False)]
for n in QUOTED["examples"]:
    row = {"e": n % 2 == 0, "f": n % 4 == 0}
    assert row == {"e": True, "f": False}
    stmts = [n % 2 == 0, (n % 2 != 0) or (n % 4 == 0), (n % 4 == 0) or (n % 2 != 0)]
    assert sum(stmts) == 1
assert all(L.val(fs[1], r) == L.val(fs[2], r) for r in L.rows("ef"))
# FT impossible for integers: divisible by 4 implies even
assert all(n % 2 == 0 for n in range(-100, 101) if n % 4 == 0)
print("exr-valuations-and-truth-tables-b4: all quoted values check")
