"""exr-valuations-and-truth-tables-c2 (Section 3.3): every formula in and, or, -> over
p, q, r with up to 3 connectives is true under the all-T valuation; the stated reason
"u(phi) = F" is false for p -> q under all-T."""
import sys
sys.path.insert(0, "verify/ch03")
import _logic as L

QUOTED = {"claim true": True}


def build(k):
    if k == 0:
        return [("atom", a) for a in "pqr"]
    return [(op, a, b) for i in range(k) for a in build(i) for b in build(k - 1 - i) for op in "&|>"]


u = {a: True for a in "pqr"}
assert all(L.val(f, u) for k in range(4) for f in build(k)) is QUOTED["claim true"]
assert u["p"] is True and L.val(L.parse(r"p \to q"), u) is True
print("exr-valuations-and-truth-tables-c2: all quoted values check")
