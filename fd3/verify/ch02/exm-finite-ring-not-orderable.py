"""exm-finite-ring-not-orderable (Section 10.3): the two-element tables satisfy (F1)-(F9)
(all eight triples), the case descriptions used in the solution, and 2.1 = 0."""
from itertools import product


def check_field(R, add, mul, zero, one):
    for a, b, c in product(R, repeat=3):
        assert add(a, b) == add(b, a)                                   # F1
        assert add(add(a, b), c) == add(a, add(b, c))                   # F2
        assert mul(mul(a, b), c) == mul(a, mul(b, c))                   # F5
        assert mul(a, b) == mul(b, a)                                   # F6
        assert mul(a, add(b, c)) == add(mul(a, b), mul(a, c))           # F9
    for a in R:
        assert add(a, zero) == a                                        # F3
        assert any(add(a, x) == zero for x in R)                        # F4
        assert mul(a, one) == a                                         # F7
        if a != zero:
            assert any(mul(a, x) == one for x in R)                     # F8
    assert one != zero


def mult(n, x, add, zero):
    r = zero
    for _ in range(n):
        r = add(r, x)
    return r


ADD2 = {(0, 0): 0, (0, 1): 1, (1, 0): 1, (1, 1): 0}
MUL2 = {(0, 0): 0, (0, 1): 0, (1, 0): 0, (1, 1): 1}
add2 = lambda x, y: ADD2[(x, y)]
mul2 = lambda x, y: MUL2[(x, y)]
check_field([0, 1], add2, mul2, 0, 1)
QUOTED = {"two_dot_one": 0, "neg": {0: 0, 1: 1}}
assert mult(2, 1, add2, 0) == QUOTED["two_dot_one"]
assert all(add2(x, QUOTED["neg"][x]) == 0 for x in (0, 1))
# the case descriptions used in the text: x + 1 is the other element; 1.x = x; 0.x = 0
assert all(add2(x, 1) == 1 - x and mul2(1, x) == x and mul2(0, x) == 0 for x in (0, 1))

print("exm-finite-ring-not-orderable: all quoted values check")
