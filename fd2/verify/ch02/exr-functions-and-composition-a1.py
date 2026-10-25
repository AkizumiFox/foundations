"""exr-functions-and-composition-a1 (Section 2.1)."""
from itertools import product

QUOTED = {"graph": {(1, 2), (2, 3), (3, 3)}, "f o f": {1: 3, 2: 3, 3: 3}, "f o f o f": {1: 3, 2: 3, 3: 3},
          "sqrt(x-1) fails at": 0, "1/(x^2-1) fails at": [-1, 1],
          "|{0}^{1,2,3}|": 1, "|empty^{1}|": 0}

f = {1: 2, 2: 3, 3: 3}
assert set(f.items()) == QUOTED["graph"]
ff = {x: f[f[x]] for x in f}
fff = {x: f[ff[x]] for x in f}
assert ff == QUOTED["f o f"] and fff == QUOTED["f o f o f"]
# (b) x^2 + 1 >= 1 on a grid; x - 1 < 0 at the quoted point; roots of x^2 - 1 among integers
assert all(x * x + 1 >= 1 for x in [k / 10 for k in range(-100, 101)])
assert QUOTED["sqrt(x-1) fails at"] - 1 < 0
assert [x for x in range(-50, 51) if x * x - 1 == 0] == QUOTED["1/(x^2-1) fails at"]
# (c)
assert all(n * n - n == n * (n - 1) for n in range(-1000, 1001))
assert all(x * x == x for x in (0, 1))
# (d) count functions by listing value tuples
def count(dom, cod):
    return sum(1 for _ in product(cod, repeat=len(dom)))
assert count([1, 2, 3], [0]) == QUOTED["|{0}^{1,2,3}|"]
assert count([1], []) == QUOTED["|empty^{1}|"]
print("exr-functions-and-composition-a1: ok")
