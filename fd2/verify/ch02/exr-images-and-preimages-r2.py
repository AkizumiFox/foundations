"""exr-images-and-preimages-r2 (Ch 6, Section 6.6): A \\ (B \\ C) versus (A \\ B) \\ C."""
from itertools import product
QUOTED = {"differing rows (1-based)": [1, 3], "rows": 8}
rows = list(product([True, False], repeat=3))   # T before F, last atom fastest
left = [p and not (q and not r) for p, q, r in rows]
right = [p and not q and not r for p, q, r in rows]
assert len(rows) == 8
assert [i + 1 for i in range(8) if left[i] != right[i]] == [1, 3]
A = B = C = {1}
assert A - (B - C) == {1} and (A - B) - C == set()
A, B, C = {1}, set(), {1}
assert A - (B - C) == {1} and (A - B) - C == set()
print("exr-images-and-preimages-r2: all quoted values check")
