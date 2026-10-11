"""exm-sets-of-numbers-as-images (Ch 6, Section 6.6): sums of small sets."""
QUOTED = {"{1,2}+{10,20}": [11, 21, 12, 22], "size": 4, "{1,2}+{1,2}": [2, 3, 4], "size2": 3}
s = lambda A, B: {a + b for a in A for b in B}
assert s({1, 2}, {10, 20}) == {11, 12, 21, 22} and len(s({1, 2}, {10, 20})) == 4
assert s({1, 2}, {1, 2}) == {2, 3, 4} and len(s({1, 2}, {1, 2})) == 3
print("exm-sets-of-numbers-as-images: all quoted values check")
