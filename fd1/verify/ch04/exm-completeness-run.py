"""exm-completeness-run (Section 3.6): (p->q) or (q->p) is a tautology; the method's derivation
has 20 lines with correct row citations; three splittings; the search derivation of
exr-finding-derivations-c2 has 13 lines."""
from pathlib import Path
from _s0607_lib import S06, ROOT, block, tautology, check_rows_in, count_lines, derivations

QUOTED = {"lines": 20, "chapter 2 lines": 13, "splittings": "Three uses"}
t = block(S06, "exm-completeness-run")
assert tautology("(p \\to q) \\vee (q \\to p)")
assert count_lines(t) == 20
assert check_rows_in(t) == 4
assert t.count("\\lem{}") == 3  # one split on p, two on q
c2 = block(ROOT / "src/ch03-finding-derivations/01-finding-derivations.md",
           "exr-finding-derivations-c2", stop="{#exr-finding-derivations-c3")
assert count_lines(c2) == 13
# the case-split tree (Section 4.8): its boxes are the derivation's, and each leaf's tag is
# the row citation inside that box
import sys
sys.path.insert(0, "verify/ch04")
import _s0708_lib as H
assert H.tree_boxes(t) == H.boxes(t), (H.tree_boxes(t), H.boxes(t))
_, lines = derivations(t)[0]
leaves = {("4", "6"): "({\\to}2)", ("7", "9"): "({\\to}1)", ("13", "15"): "({\\to}1)", ("16", "18"): "({\\to}1)"}
for (a, b), tag in leaves.items():
    inside = [lines[str(n)][1] for n in range(int(a), int(b) + 1)]
    assert any(tag in j for j in inside) and any("\\oi" in j for j in inside), (a, b)
assert "\\oe{1,2-10,11-19}" in lines["20"][1]
print("exm-completeness-run: all quoted values check")
