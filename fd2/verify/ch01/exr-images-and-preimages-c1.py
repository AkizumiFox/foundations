"""exr-images-and-preimages-c1 (b) (Ch 6, Section 6.6): squaring, A = {-1,1}, B = {1}."""
QUOTED = {"A": [-1, 1], "f(A \\ B)": [1]}
f = lambda x: x * x
A, B = {-1, 1}, {1}
img = lambda S: {f(s) for s in S}
assert img(A - B) == {1} and img(A) - img(B) == set()
print("exr-images-and-preimages-c1: all quoted values check")
