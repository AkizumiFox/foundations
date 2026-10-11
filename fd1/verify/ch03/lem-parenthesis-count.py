"""lem-parenthesis-count (Ch 3, Section 3.2): parts (a)-(c) by brute force on small formulas,
the depth-one remark, the example ex("(p and (q") = 2, and the S2 counterexample showing
the strict clause of (b) alone is not inductive."""
from _s0102_formulas import tok, excess, all_formulas, BINARY

QUOTED = {"example excess": "= 2"}

assert excess(tok(r"(p \wedge (q")) == 2
for f in all_formulas(13, atom_list=("p", "q")):
    assert excess(f) == 0                                              # (a)
    for k in range(len(f) + 1):
        assert excess(f[:k]) >= 0                                      # (b), first sentence
        if f[0] == "(" and 0 < k < len(f):
            assert excess(f[:k]) >= 1                                  # (b), strict clause
    depth_one = [i for i, t in enumerate(f) if t in BINARY and excess(f[:i]) == 1]
    for i, t in enumerate(f):
        if t in BINARY:
            assert excess(f[:i]) >= 1                                  # (c)
    if f[0] == "(":
        assert len(depth_one) == 1                                     # the main connective only
# the negation formula neg(p and q) has an initial segment "neg (p" of excess 1, not covered
# by the strict clause (it does not begin with a parenthesis): the first sentence of (b) is needed
seg = tok(r"\neg(p")
assert excess(seg) == 1 and seg[0] == "neg"
print("lem-parenthesis-count: all quoted values check")
