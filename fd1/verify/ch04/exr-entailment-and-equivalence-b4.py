"""exr-entailment-and-equivalence-b4 (Section 4.5): the six classifications and the witness
rows quoted in the solution."""
import sys
sys.path.insert(0, "verify/ch04")
import _logic as L

QUOTED = {"a": "contradictory", "b": "contrary", "c": "subcontrary", "d": "subcontrary",
          "e": "contrary", "f": "none"}
PAIRS = {"a": ("p \\to q", "p \\wedge \\neg q"), "b": ("p \\wedge q", "\\neg p \\wedge q"),
         "c": ("p \\vee q", "\\neg p \\vee q"), "d": ("p \\to q", "q \\to p"),
         "e": ("p \\leftrightarrow q", "p \\wedge \\neg q"), "f": ("p", "p \\vee q")}


def rel(a, b):
    A, B = L.parse(a), L.parse(b)
    both_t = any(L.val(A, r) and L.val(B, r) for r in L.rows("pq"))
    both_f = any(not L.val(A, r) and not L.val(B, r) for r in L.rows("pq"))
    if not both_t and not both_f: return "contradictory"
    if not both_t: return "contrary"
    if not both_f: return "subcontrary"
    return "none"


for k, (a, b) in PAIRS.items():
    assert rel(a, b) == QUOTED[k], k


def both(a, b, row, val):
    return L.val(L.parse(a), row) == val and L.val(L.parse(b), row) == val


T, F = True, False
assert all(both(*PAIRS["b"], {"p": p, "q": F}, F) for p in (T, F))
assert both(*PAIRS["c"], {"p": F, "q": T}, T)
assert both(*PAIRS["d"], {"p": T, "q": T}, T)
assert [L.tv(r, "p", "q") for r in L.false_rows("q \\to p")] == [(F, T)]
assert both(*PAIRS["e"], {"p": F, "q": T}, F)
assert both(*PAIRS["f"], {"p": T, "q": T}, T) and both(*PAIRS["f"], {"p": F, "q": F}, F)
assert not L.entails(["p"], "p \\vee q")
print("exr-entailment-and-equivalence-b4: all quoted values check")
