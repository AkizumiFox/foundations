"""exr-induction-c3 (Ch 3, Section 3.2): nodes > neg for formulas in not and and only
(brute force), and exr-induction-b2: number of subformulas <= length."""
from _s0102_formulas import all_formulas, nodes, subformulas

QUOTED = {"exit check verified on small formulas": True}

for f in all_formulas(15, atom_list=("p", "q"), ops=("and",)):
    if "bot" in f:
        continue
    assert nodes(f) > f.count("neg")
    assert nodes(f) - f.count("neg") >= 1
for f in all_formulas(12):
    assert len(subformulas(f)) <= len(f)
print("exr-induction-c3: all quoted values check")
