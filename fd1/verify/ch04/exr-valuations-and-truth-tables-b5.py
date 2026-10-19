"""exr-valuations-and-truth-tables-b5 (Section 4.4): the four claims a -> not b, b or c,
c -> a, not (a and c) are all true in exactly one row, a = F, b = T, c = F; n = 3, 9, 21
satisfy them; the witnesses 30, 6, 10, 2, 15, 3, 5, 1 realize the eight rows in the book's
order."""
import sys
sys.path.insert(0, "verify/ch04")
import _logic as L

QUOTED = {"examples": [3, 9, 21], "witnesses": [30, 6, 10, 2, 15, 3, 5, 1]}
fs = [L.parse(s) for s in [r"a \to \neg b", r"b \vee c", r"c \to a", r"\neg(a \wedge c)"]]
good = [L.tv(r, "a", "b", "c") for r in L.rows("abc") if all(L.val(f, r) for f in fs)]
assert good == [(False, True, False)]


def row(n):
    return (n % 2 == 0, n % 3 == 0, n % 5 == 0)


for n in QUOTED["examples"]:
    assert row(n) == (False, True, False)
assert [row(n) for n in QUOTED["witnesses"]] == [L.tv(r, "a", "b", "c") for r in L.rows("abc")]
print("exr-valuations-and-truth-tables-b5: all quoted values check")
