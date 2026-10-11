"""exm-injective-surjective-first (Ch 6 Section 6.4)."""
from fractions import Fraction as F

QUOTED = {"preimage formula check": True, "witness for 3n": 1}

f = lambda x: 3 * x - 5
assert all(f((y + 5) / F(3)) == y for y in [F(k, 5) for k in range(-50, 51)])
assert all(3 * n != QUOTED["witness for 3n"] for n in range(-1000, 1001))
h = {1: "a", 2: "b", 3: "a"}
assert h[1] == h[3] and set(h.values()) == {"a", "b"}
k = {1: "a", 2: "c"}
assert len(set(k.values())) == 2 and "b" not in k.values()
print("exm-injective-surjective-first: all quoted values check")
