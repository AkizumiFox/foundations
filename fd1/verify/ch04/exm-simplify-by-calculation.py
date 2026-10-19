"""exm-simplify-by-calculation (Section 4.9): each step of the chain is an equivalence, and
each cited law holds for the step (checked by truth table)."""
from _logic import equivalent
CHAIN = ["(p \\to q) \\wedge (p \\to \\neg q)", "(\\neg p \\vee q) \\wedge (\\neg p \\vee \\neg q)",
         "\\neg p \\vee (q \\wedge \\neg q)", "\\neg p \\vee \\bot", "\\neg p"]
for a, b in zip(CHAIN, CHAIN[1:]):
    assert equivalent(a, b), (a, b)
# step 2 is (g), second form, right to left, with phi = not p, psi = q, chi = not q
assert equivalent("\\neg p \\vee (q \\wedge \\neg q)", "(\\neg p \\vee q) \\wedge (\\neg p \\vee \\neg q)")
assert equivalent("q \\wedge \\neg q", "\\bot")          # (c) of prp-more-equivalences
assert equivalent("\\neg p \\vee \\bot", "\\neg p")      # (a)
print("exm-simplify-by-calculation: all quoted values check")
