"""exm-refute-product-of-divisors (F2.1 §01): a = b = c = 2 refutes "a | c, b | c => ab | c";
the pairs (2, 3) and (2, 5) resist (checked on a range of c); 4 does not divide 2."""
QUOTED = {"counter": (2, 2, 2), "resist": ((2, 3), (2, 5))}

def div(a, b):
    return b == 0 if a == 0 else b % a == 0

a, b, c = QUOTED["counter"]
assert div(a, c) and div(b, c) and not div(a * b, c)
assert all(4 * k != 2 for k in range(-100, 101))
for a, b in QUOTED["resist"]:
    cs = [c for c in range(-600, 601) if div(a, c) and div(b, c)]
    assert all(div(a * b, c) for c in cs)
    assert cs[:3] == [-600, -600 + a * b, -600 + 2 * a * b]  # c runs over the multiples of ab
# the search is exhaustive over small cases: every counterexample with 1 <= a, b <= 6 has a common factor > 1
from math import gcd
for a in range(1, 7):
    for b in range(1, 7):
        bad = any(div(a, c) and div(b, c) and not div(a * b, c) for c in range(-200, 201))
        assert bad == (gcd(a, b) > 1)
print("exm-refute-product-of-divisors: all quoted values check")
