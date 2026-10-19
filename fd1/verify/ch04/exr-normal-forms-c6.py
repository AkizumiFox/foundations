"""exr-normal-forms-c6 (Section 4.9, displayed C5): #phi counts, monotonicity under |=,
inclusion-exclusion, minterm facts and the full-DNF count, on random formulas over three
atoms; the converse counterexample; the thm-dnf boundary remark."""
import random
from _logic import val, rows
N = ["p", "q", "r"]
ROWS = list(rows(N))
def count(f):
    return sum(1 for v in ROWS if val(f, v))
random.seed(6)
def rand(d):
    if d == 0 or random.random() < 0.3:
        return ("atom", random.choice(N))
    k = random.choice(["not", "&", "|", ">", "="])
    return ("not", rand(d - 1)) if k == "not" else (k, rand(d - 1), rand(d - 1))
for _ in range(2000):
    f, g = rand(3), rand(3)
    if all(val(g, v) for v in ROWS if val(f, v)):
        assert count(f) <= count(g)
    assert count(("|", f, g)) == count(f) + count(g) - count(("&", f, g))
def minterm(v):
    lits = [("atom", n) if v[n] else ("not", ("atom", n)) for n in N]
    m = lits[-1]
    for l in reversed(lits[:-1]):
        m = ("&", l, m)
    return m
for v in ROWS:
    for w in ROWS:
        if v != w:
            assert not any(val(minterm(v), u) and val(minterm(w), u) for u in ROWS)
assert all(any(val(minterm(v), u) for v in ROWS) for u in ROWS)
# converse fails: p and q on p, q
P, Q = ("atom", "p"), ("atom", "q")
assert count(P) == count(Q) and not all(val(Q, v) for v in ROWS if val(P, v))
# thm-dnf over phi's own atoms: phi = p over p, q, r has # = 4 and 4 / 2^2 = 1 minterm there
assert count(P) == 4
print("exr-normal-forms-c6: all quoted values check")
