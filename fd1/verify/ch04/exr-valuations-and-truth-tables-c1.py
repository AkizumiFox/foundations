"""exr-valuations-and-truth-tables-c1 (Section 4.4): an <->-built formula is true under v
exactly when the number f_v of false atom occurrences is even, checked on random <->-built
formulas over four atoms under every valuation; (b) (p <-> q) <-> p has the value of q in
all four rows, with p occurring twice and q once."""
import itertools
import random
import sys
sys.path.insert(0, "verify/ch04")
import _logic as L

QUOTED = {"occurrences of p in (b)": 2, "occurrences of q in (b)": 1}
random.seed(4)
ATOMS = "pqrs"


def build(depth):
    if depth == 0 or random.random() < 0.3:
        return ("atom", random.choice(ATOMS))
    return ("=", build(depth - 1), build(depth - 1))


def occ(f):
    return [f[1]] if f[0] == "atom" else occ(f[1]) + occ(f[2])


for _ in range(400):
    f = build(5)
    for bits in itertools.product([True, False], repeat=4):
        v = dict(zip(ATOMS, bits))
        fv = sum(1 for a in occ(f) if not v[a])
        assert L.val(f, v) == (fv % 2 == 0)
g = L.parse(r"(p \leftrightarrow q) \leftrightarrow p")
assert occ(g).count("p") == QUOTED["occurrences of p in (b)"]
assert occ(g).count("q") == QUOTED["occurrences of q in (b)"]
for r in L.rows("pq"):
    assert L.val(g, r) == r["q"]
print("exr-valuations-and-truth-tables-c1: all quoted values check")
