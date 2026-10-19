"""exr-valuations-and-truth-tables-b5 (Section 4.4): the four claims p -> not q, q or r,
r -> p, not (p and r) are all true in exactly one row, p = F, q = T, r = F; n = 3, 9, 21
satisfy them; the witnesses 30, 6, 10, 2, 15, 3, 5, 1 realize the eight rows in the book's
order."""
import sys
sys.path.insert(0, "verify/ch04")
import _logic as L

QUOTED = {"examples": [3, 9, 21], "witnesses": [30, 6, 10, 2, 15, 3, 5, 1]}
fs = [L.parse(s) for s in [r"p \to \neg q", r"q \vee r", r"r \to p", r"\neg(p \wedge r)"]]
good = [L.tv(r, "p", "q", "r") for r in L.rows("pqr") if all(L.val(f, r) for f in fs)]
assert good == [(False, True, False)]


def row(n):
    return (n % 2 == 0, n % 3 == 0, n % 5 == 0)


for n in QUOTED["examples"]:
    assert row(n) == (False, True, False)
assert [row(n) for n in QUOTED["witnesses"]] == [L.tv(r, "p", "q", "r") for r in L.rows("pqr")]
print("exr-valuations-and-truth-tables-b5: all quoted values check")
