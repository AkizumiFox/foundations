"""exr-structural-induction-b3 (Ch 4, Section 4.3): the mirror m is an involution and keeps the height
(on 500 random formulas and on every formula up to length 11); part (a); part (d)."""
import random
from _s0102_formulas import tok, parse, height, is_formula, all_formulas, BINARY

QUOTED = {"(a)": "((\\neg r \\wedge q) \\to p)"}


def m(s):
    sp = parse(s)
    if sp[0] == "base":
        return s
    if sp[0] == "neg":
        return ("neg",) + m(sp[1])
    return ("(",) + m(sp[2]) + (sp[0],) + m(sp[1]) + (")",)


def rand_formula(depth, rng):
    if depth == 0 or rng.random() < 0.2:
        return (rng.choice(["p", "q", "r", "bot"]),)
    if rng.random() < 0.3:
        return ("neg",) + rand_formula(depth - 1, rng)
    return ("(",) + rand_formula(depth - 1, rng) + (rng.choice(BINARY),) + rand_formula(depth - 1, rng) + (")",)


rng = random.Random(4)
sample = [rand_formula(6, rng) for _ in range(500)] + all_formulas(11, atom_list=("p", "q"))
for s in sample:
    assert is_formula(s) and is_formula(m(s))
    assert m(m(s)) == s and height(m(s)) == height(s)
assert m(tok(r"(p \to (q \wedge \neg r))")) == tok(r"((\neg r \wedge q) \to p)")
assert m(tok(r"(p \wedge p)")) == tok(r"(p \wedge p)") and m(tok(r"\neg(q \vee q)")) == tok(r"\neg(q \vee q)")
print("exr-structural-induction-b3: all quoted values check")
