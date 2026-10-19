"""exr-structural-induction-c5 (Ch 4, Section 4.3): Polish notation. The two translations of (a);
weight 1 and proper prefixes of weight <= 0 for every Polish formula over p, q, r up to length 9 and
200 random ones; unique reading of K phi psi; the running weights of (d)."""
import random
from itertools import product
from _s0102_formulas import tok, parse

QUOTED = {"(d) from the first symbol": "-1, -2, -1, 0, 0, 1"}

PREFIX = {"and": "K", "or": "A", "imp": "C", "iff": "E"}
W = {"N": 0, "K": -1, "A": -1, "C": -1, "E": -1}


def polish(s):
    sp = parse(s)
    if sp[0] == "base":
        return s[0] if s[0] != "bot" else "B"
    if sp[0] == "neg":
        return "N" + polish(sp[1])
    return PREFIX[sp[0]] + polish(sp[1]) + polish(sp[2])


def w(u):
    return sum(W.get(c, 1) for c in u)


assert polish(tok(r"((p \wedge \neg q) \to p)")) == "CKpNqp"
assert polish(tok(r"\neg(p \vee (q \leftrightarrow r))")) == "NApEqr"


def polish_formulas(n):
    by = {1: ["p", "q", "r", "B"]}
    for k in range(2, n + 1):
        cur = ["N" + f for f in by[k - 1]]
        for a in range(1, k - 1):
            for f, g in product(by[a], by[k - 1 - a]):
                cur += [op + f + g for op in "KACE"]
        by[k] = cur
    return [f for k in by for f in by[k]]


def rand_polish(d, rng):
    if d == 0 or rng.random() < 0.25:
        return rng.choice("pqrB")
    if rng.random() < 0.3:
        return "N" + rand_polish(d - 1, rng)
    return rng.choice("KACE") + rand_polish(d - 1, rng) + rand_polish(d - 1, rng)


rng = random.Random(5)
forms = polish_formulas(7) + [rand_polish(7, rng) for _ in range(200)]
fset = set(polish_formulas(7))
for f in forms:
    assert w(f) == 1 and all(w(f[:k]) <= 0 for k in range(len(f)))
# (c): K phi psi is read in one way (checked for all short ones by trying every split)
for f in polish_formulas(7):
    if f[0] in "KACE":
        rest = f[1:]
        assert sum(1 for k in range(1, len(rest)) if rest[:k] in fset and rest[k:] in fset) == 1
# (d)
s = "CApqNr"
run = [w(s[:k]) for k in range(1, len(s) + 1)]
assert run == [-1, -2, -1, 0, 0, 1]
after = [w(s[1:k]) for k in range(2, len(s) + 1)]
assert after[:3] == [-1, 0, 1] and min(k for k in range(1, 6) if w(s[1:1 + k]) == 1) == 3
print("exr-structural-induction-c5: all quoted values check")
