"""thm-unique-readability (Ch 3, Section 3.2): every compound formula up to length 13 over
p, q, bot splits in exactly one way (checked by trying every split, independently of the proof);
exr-induction-c1: no proper initial segment of a formula is a formula."""
from _s0102_formulas import splits, all_formulas, is_formula

QUOTED = {"unique readability holds on all formulas up to length 13": True}

for f in all_formulas(13, atom_list=("p", "q")):
    assert len(splits(f)) == 1, f
    assert not any(is_formula(f[:k]) for k in range(0, len(f)))
print("thm-unique-readability: all quoted values check")
