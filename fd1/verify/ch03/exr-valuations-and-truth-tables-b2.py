"""exr-valuations-and-truth-tables-b2 (Section 3.3): occ = bin + 1 for binary-built formulas,
on every binary-built formula with up to 4 binary connectives over atoms p, q, r; and the
worked instance (p -> q) and (p or r): 4 atom occurrences, 3 binary connectives."""
import itertools
import sys
sys.path.insert(0, "verify/ch03")
import _logic as L

QUOTED = {"occurrences": 4, "binary connectives": 3}


def occ(f):
    return 1 if f[0] == "atom" else occ(f[1]) + occ(f[2])


def nbin(f):
    return 0 if f[0] == "atom" else nbin(f[1]) + nbin(f[2]) + 1


def build(k):
    if k == 0:
        return [("atom", a) for a in "pqr"]
    out = []
    for i in range(k):
        for a in build(i):
            for b in build(k - 1 - i):
                for op in "&|>=":
                    out.append((op, a, b))
    return out


for k in range(4):
    for f in build(k):
        assert occ(f) == nbin(f) + 1
f = L.parse(r"(p \to q) \wedge (p \vee r)")
assert (occ(f), nbin(f)) == (QUOTED["occurrences"], QUOTED["binary connectives"])
print("exr-valuations-and-truth-tables-b2: all quoted values check")
