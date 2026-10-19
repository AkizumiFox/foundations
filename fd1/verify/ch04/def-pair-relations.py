"""def-pair-relations (Section 4.5): the three pairs of the table (contradictory, contrary,
subcontrary) with their witness rows; the Quick check (p <-> q, p <-> not q contradictory);
contradictory iff phi == not psi on these pairs."""
import sys
sys.path.insert(0, "verify/ch04")
import _logic as L

QUOTED = {"pairs": [("p \\to q", "p \\wedge \\neg q", "contradictory"),
                    ("p \\wedge q", "\\neg p", "contrary"),
                    ("p \\vee q", "\\neg p \\vee q", "subcontrary"),
                    ("p \\leftrightarrow q", "p \\leftrightarrow \\neg q", "contradictory")]}


def rel(a, b):
    A, B = L.parse(a), L.parse(b)
    both_t = any(L.val(A, r) and L.val(B, r) for r in L.rows("pq"))
    both_f = any(not L.val(A, r) and not L.val(B, r) for r in L.rows("pq"))
    if not both_t and not both_f: return "contradictory"
    if not both_t: return "contrary"
    if not both_f: return "subcontrary"
    return "none"


for a, b, k in QUOTED["pairs"]:
    assert rel(a, b) == k, (a, b)
    assert (k == "contradictory") == L.equivalent(a, "\\neg(" + b + ")")
# witnesses
assert [L.tv(r, "p", "q") for r in L.rows("pq") if L.val(L.parse("p \\wedge \\neg q"), r)] == [(True, False)]
assert L.false_rows("p \\to q") and [L.tv(r, "p", "q") for r in L.false_rows("p \\to q")] == [(True, False)]
w = {"p": True, "q": False}
assert not L.val(L.parse("p \\wedge q"), w) and not L.val(L.parse("\\neg p"), w)
w = {"p": False, "q": True}
assert L.val(L.parse("p \\vee q"), w) and L.val(L.parse("\\neg p \\vee q"), w)
print("def-pair-relations: all quoted values check")
