"""exm-small-products and the quick check after it (Ch 6 Section 6.3)."""
from itertools import product

QUOTED = {"size of {1,2} x {a,b,c}": 6, "size of {0,1} x {0,1,2}": 6}

p = set(product([1, 2], "abc"))
q = set(product("abc", [1, 2]))
assert len(p) == QUOTED["size of {1,2} x {a,b,c}"] and p.isdisjoint(q)
assert set(product([0, 1], [0, 1, 2])) == {(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)}
assert len(set(product([0, 1], [0, 1, 2]))) == QUOTED["size of {0,1} x {0,1,2}"]
assert set(product([1, 2], [])) == set() and (1, 1) not in set(product([1], []))
print("exm-small-products: all quoted values check")
