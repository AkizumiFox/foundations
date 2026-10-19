"""lem-parenthesis-count (Ch 3, Section 3.2): parts (a)-(c) by brute force on small formulas,
the depth-one remark, the example ex("(p and (q") = 2, and the S2 counterexample showing
the strict clause of (b) alone is not inductive."""
from _s0102_formulas import tok, excess, all_formulas, BINARY

QUOTED = {"example excess": "= 2", "depth 2 label": "depth 2", "main connective label": "main connective,"}

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


def depths(f):
    out, d = [], 0
    for t in f:
        out.append(d)
        d += {"(": 1, ")": -1}.get(t, 0)
    return out, d


# the depth-profile figure: ((p and q) or r)
d, end = depths(tok(r"((p \wedge q) \vee r)"))
assert d == [0, 1, 2, 2, 2, 2, 1, 1, 1] and end == 0
# the Quick check: (p and (q or r)); the and is the only binary connective at depth 1
f = tok(r"(p \wedge (q \vee r))")
d, end = depths(f)
assert d == [0, 1, 1, 1, 2, 2, 2, 2, 1] and end == 0
assert [t for t, x in zip(f, d) if t in BINARY and x == 1] == ["and"]
# drill (b) of exr-structural-induction-a2: neg(p -> neg q)
f = tok(r"\neg(p \to \neg q)")
d, end = depths(f)
assert d == [0, 0, 1, 1, 1, 1, 1] and end == 0
assert [t for t, x in zip(f, d) if t in BINARY and x == 1] == ["imp"]
# depth of a symbol = excess of the initial segment before it
for g in all_formulas(11, atom_list=("p", "q")):
    dd, _ = depths(g)
    assert all(dd[i] == excess(g[:i]) for i in range(len(g)))
# the hook: p and q or r, read both ways, at p = q = F, r = T
p_, q_, r_ = False, False, True
assert ((p_ and q_) or r_) is True and (p_ and (q_ or r_)) is False
print("lem-parenthesis-count: all quoted values check")
