"""exr-images-and-preimages-c3 (b) (Ch 6, Section 6.6): constant map {1,2} -> {0}."""
QUOTED = {"A": [1], "B": [2], "value": 0}
f = {1: 0, 2: 0}
img = lambda S: {f[s] for s in S}
A, B = {1}, {2}
assert img(A & B) == set() and img(A) & img(B) == {0}
print("exr-images-and-preimages-c3: all quoted values check")
