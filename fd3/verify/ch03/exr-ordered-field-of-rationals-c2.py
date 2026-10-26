"""exr-ordered-field-of-rationals-c2: ps < rq is independent of representatives in Z x Z_{>0}."""
from itertools import product
pairs = [(p, q) for p in range(-5, 6) for q in range(1, 6)]
eq = lambda a, b: a[0] * b[1] == b[0] * a[1]
cls = {}
for a in pairs:
    cls.setdefault(next(b for b in pairs if eq(a, b)), []).append(a)
for A, B in product(cls.values(), cls.values()):
    verdicts = {p * s < r * q for (p, q) in A for (r, s) in B}
    assert len(verdicts) == 1
print("ok")
