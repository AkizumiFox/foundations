"""prp-copy-of-naturals-absorbs: the hotel map h of proof (a) for X = R, s(n) = n (Quick check),
checked on a finite window of rationals; and the gluing of proof (b) on a toy instance."""
from fractions import Fraction as Fr

QUOTED = {3: 4, -3: -3, Fr(1, 2): Fr(1, 2)}


def is_nat(x):
    return x == int(x) and x >= 0


def h(x):
    return x + 1 if is_nat(x) else x


for x, v in QUOTED.items():
    assert h(x) == v
window = [Fr(p, q) for p in range(-40, 41) for q in range(1, 7)]
window = sorted(set(window))
vals = [h(x) for x in window]
assert 0 not in vals                       # no point is sent to 0
assert len(set(vals)) == len(vals)         # injective on the window
for m in range(1, 30):                     # every m in N \ {0} is h(m - 1)
    assert h(m - 1) == m

# (b), toy instance: X = N with s(n) = 2n (copy S = evens), C = {-1, -2, -3} disjoint from X.
# psi: S u C -> S, enumerate S u C as -1, -2, -3, 0, 2, 4, ... and send the k-th to 2k.
C = [-1, -2, -3]
def psi(y):
    return 2 * C.index(y) if y in C else y + 2 * len(C)
def H(x):
    return x if (x >= 0 and x % 2 == 1) else psi(x)
dom = C + list(range(0, 400))
img = [H(x) for x in dom]
assert len(set(img)) == len(img)
assert set(range(0, 400)) <= set(H(x) for x in C + list(range(0, 400 + 2 * len(C))))
print("ok")
