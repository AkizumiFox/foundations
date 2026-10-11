"""exm-image-two-witnesses (Ch 6, Section 6.6): squaring, A = {-1}, B = {1}."""
QUOTED = {"f(A) and f(B)": [1], "A": -1}
f = lambda x: x * x
A, B = {-1}, {1}
img = lambda S: {f(s) for s in S}
assert img(A) & img(B) == {1} and img(A & B) == set()
print("exm-image-two-witnesses: all quoted values check")
