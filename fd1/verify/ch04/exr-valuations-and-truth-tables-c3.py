"""exr-valuations-and-truth-tables-c3 (Section 4.4): Ver and Fal, defined by the table of the
item, agree with v(phi) = T and v(phi) = F on random formulas built by not, and, or over
three atoms, under every valuation; and the game itself (a minimax search over the players'
choices) gives the same winner."""
import itertools
import random
import sys
sys.path.insert(0, "verify/ch04")
import _logic as L

QUOTED = {"atoms": 3}
random.seed(43)
ATOMS = "pqr"


def build(d):
    if d == 0 or random.random() < 0.25:
        return ("atom", random.choice(ATOMS))
    k = random.choice(["not", "&", "|"])
    return ("not", build(d - 1)) if k == "not" else (k, build(d - 1), build(d - 1))


def ver(f, v):
    k = f[0]
    if k == "atom": return v[f[1]]
    if k == "not": return fal(f[1], v)
    if k == "&": return ver(f[1], v) and ver(f[2], v)
    return ver(f[1], v) or ver(f[2], v)


def fal(f, v):
    k = f[0]
    if k == "atom": return not v[f[1]]
    if k == "not": return ver(f[1], v)
    if k == "&": return fal(f[1], v) or fal(f[2], v)
    return fal(f[1], v) and fal(f[2], v)


def play(f, v, verifier_is_A):
    """True iff player A (the original verifier) wins with best play."""
    k = f[0]
    if k == "atom":
        return v[f[1]] == verifier_is_A
    if k == "not":
        return play(f[1], v, not verifier_is_A)
    outcomes = [play(f[1], v, verifier_is_A), play(f[2], v, verifier_is_A)]
    chooser_is_A = (k == "|") == verifier_is_A   # verifier chooses at or, falsifier at and
    return any(outcomes) if chooser_is_A else all(outcomes)


assert len(ATOMS) == QUOTED["atoms"]
for _ in range(500):
    f = build(5)
    for bits in itertools.product([True, False], repeat=3):
        v = dict(zip(ATOMS, bits))
        t = L.val(f, v)
        assert ver(f, v) == t and fal(f, v) == (not t)
        assert play(f, v, True) == t
print("exr-valuations-and-truth-tables-c3: all quoted values check")
