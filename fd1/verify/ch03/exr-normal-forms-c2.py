"""exr-normal-forms-c2 (Section 3.7): majority is self-dual, so every {not, M} formula takes
opposite values on flipped rows (checked on all formulas of depth <= 2 over 2 atoms); p and q is F
on (T, F) and (F, T); {and, or, ->, <->} formulas are T under all-T (depth <= 2)."""
import itertools
QUOTED = {}
M = lambda a, b, c: a + b + c >= 2
for a, b, c in itertools.product([True, False], repeat=3):
    assert M(not a, not b, not c) == (not M(a, b, c))
# functions of two inputs as tuples over rows TT, TF, FT, FF
R = list(itertools.product([True, False], repeat=2))
fs = {tuple(r[0] for r in R), tuple(r[1] for r in R)}
for _ in range(2):
    new = set(fs)
    for f in fs:
        new.add(tuple(not x for x in f))
    for f, g, h in itertools.product(fs, repeat=3):
        new.add(tuple(M(x, y, z) for x, y, z in zip(f, g, h)))
    fs = new
flip = {0: 3, 1: 2, 2: 1, 3: 0}
for f in fs:
    assert all(f[i] != f[flip[i]] for i in range(4))
assert (True, False, False, False) not in fs
imp = lambda a, b: (not a) or b
gs = {(True,) * 4}
base = {tuple(r[0] for r in R), tuple(r[1] for r in R)}
fs2 = set(base)
for _ in range(2):
    new = set(fs2)
    for f, g in itertools.product(fs2, repeat=2):
        for op in (lambda a, b: a and b, lambda a, b: a or b, imp, lambda a, b: a == b):
            new.add(tuple(op(x, y) for x, y in zip(f, g)))
    fs2 = new
assert all(f[0] for f in fs2)
print("exr-normal-forms-c2: all quoted values check")
