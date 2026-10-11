"""exr-induction-b3 (Ch 3, Section 3.2): nodes <= 2^height - 1, with equality example."""
from _s0102_formulas import tok, nodes, height, all_formulas

QUOTED = {"equality example nodes": 7, "height": 3}

for f in all_formulas(12):
    assert nodes(f) <= 2 ** height(f) - 1
w = tok(r"((p \wedge q) \wedge (r \wedge p))")
assert nodes(w) == 7 == 2 ** 3 - 1 and height(w) == 3
print("exr-induction-b3: all quoted values check")
