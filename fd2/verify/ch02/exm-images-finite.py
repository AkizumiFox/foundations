"""exm-images-finite (Ch 6, Section 6.6): f on {1,2,3,4} -> {0,1,2,5}."""
QUOTED = {"f({1,4})": [1], "f({2,3})": [0, 2], "f(X)": [0, 1, 2],
          "f^{-1}({1})": [1, 4], "f^{-1}({0,2})": [2, 3]}
f = {1: 1, 2: 2, 3: 0, 4: 1}
X, Y = set(f), {0, 1, 2, 5}
img = lambda A: {f[a] for a in A}
pre = lambda B: {x for x in X if f[x] in B}
assert img({1, 4}) == {1} and img({2, 3}) == {0, 2} and img(X) == {0, 1, 2} and img(set()) == set()
assert pre({1}) == {1, 4} and pre({0, 2}) == {2, 3} and pre({5}) == set()
assert pre(set()) == set() and pre(Y) == X
print("exm-images-finite: all quoted values check")
