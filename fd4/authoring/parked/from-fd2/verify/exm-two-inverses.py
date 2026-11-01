"""exm-two-inverses: X = {e, a, b}; e identity, a*a = a*b = b*a = b*b = e.
Commutative with identity e; a has inverses a and b; (a*a)*b = b, a*(a*b) = a.
Also the chain of prp-operation-inverse-unique breaks only at the associativity step."""
from itertools import product

X = ["e", "a", "b"]
T = {}
for u in X:
    T[("e", u)] = u
    T[(u, "e")] = u
for u, v in product(["a", "b"], repeat=2):
    T[(u, v)] = "e"
op = lambda u, v: T[(u, v)]

QUOTED = {"(a*a)*b": "b", "a*(a*b)": "a", "inverses_of_a": {"a", "b"}}

assert len(T) == 9 and all(T[p] in X for p in T)
assert all(op(u, v) == op(v, u) for u in X for v in X)
assert all(op("e", u) == u == op(u, "e") for u in X)
assert {y for y in X if op("a", y) == "e" == op(y, "a")} == QUOTED["inverses_of_a"]
assert op(op("a", "a"), "b") == QUOTED["(a*a)*b"]
assert op("a", op("a", "b")) == QUOTED["a*(a*b)"]
bad = [(x, y, z) for x, y, z in product(X, repeat=3) if op(op(x, y), z) != op(x, op(y, z))]
assert len(bad) > 0 and ("a", "a", "b") in bad
# C2: cancellation fails: a*a = a*b with a != b
assert op("a", "a") == op("a", "b")
print(f"exm-two-inverses: all quoted values check ({27 - len(bad)} of 27 triples associate)")
