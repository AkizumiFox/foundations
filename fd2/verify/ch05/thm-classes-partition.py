"""Quick check in Section 7.5 (after def-equivalence-class): "same last digit" on {1, ..., 30}
has ten classes of three elements, e.g. [1] = [11] = [21] = {1, 11, 21}; and the partition
facts of thm-classes-partition on that example."""

QUOTED = {"classes": 10, "size": 3, "class_of_1": {1, 11, 21}, "last": {10, 20, 30}}

X = range(1, 31)
rel = lambda x, y: x % 10 == y % 10
cls = {a: frozenset(x for x in X if rel(x, a)) for a in X}
quotient = set(cls.values())
assert len(quotient) == QUOTED["classes"]
assert all(len(c) == QUOTED["size"] for c in quotient)
assert cls[1] == cls[11] == cls[21] == QUOTED["class_of_1"]
assert cls[10] == QUOTED["last"]
# partition: non-empty, pairwise disjoint, covering; [a] = [b] iff a ~ b
assert all(c for c in quotient)
assert all(c == d or not (c & d) for c in quotient for d in quotient)
assert set().union(*quotient) == set(X)
assert all((cls[a] == cls[b]) == rel(a, b) for a in X for b in X)
print("thm-classes-partition: all quoted values check")
