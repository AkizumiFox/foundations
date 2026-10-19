"""exr-structural-induction-a2 (Ch 4, Section 4.3): the drill's counts."""
from _s0102_formulas import tok, excess, height, subformulas, parse, is_formula, all_formulas, BINARY

QUOTED = {"(c) excess": 3, "(e),(g) height": 4, "(h) value": 2, "(j) length": 6}

f = tok(r"((p \wedge (q \vee r)) \to p)")
seg = tok(r"((p \wedge (q")
assert f[:len(seg)] == seg and excess(seg) == 3                                   # (c)
g = tok(r"((p \to q) \wedge (r \vee p))")
assert [t for i, t in enumerate(g) if t in BINARY and excess(g[:i]) == 1] == ["and"]   # (d)
assert height(tok(r"((p \wedge q) \vee \neg\neg r)")) == 4                      # (e)
h = tok(r"\neg(p \vee \neg p)")
assert height(h) == 4 and height(tok(r"(p \vee \neg p)")) == 3 and height(tok(r"\neg p")) == 2   # (g)
assert subformulas(h) == {h, tok(r"(p \vee \neg p)"), tok("p"), tok(r"\neg p")}


def b(s):
    sp = parse(s)
    if sp[0] == "base":
        return 1 if s == ("bot",) else 0
    return sum(b(part) for part in sp[1:])


assert b(tok(r"(\bot \to \neg\bot)")) == 2                                      # (h)
for s in all_formulas(11, atom_list=("p", "q")):
    assert b(s) == s.count("bot")
    for part in [x for x in subformulas(s) if x != s]:
        assert height(part) < height(s)                                             # (f)
    if "neg" not in s and "bot" not in s:
        assert len(s) % 2 == 1                                                      # (l)
w = tok(r"(p \wedge \neg q)")
assert is_formula(w) and len(w) == 6 and w[0] == "("                                # (j)
print("exr-structural-induction-a2: all quoted values check")
