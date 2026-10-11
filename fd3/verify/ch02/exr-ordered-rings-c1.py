"""exr-ordered-rings-c1 (Section 10.3), part (c): the tables mod 3 satisfy (F1)-(F9), and
1.1 = 1, 2.1 = 2, 3.1 = 0."""
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


QUOTED = {"three_dot_one_mod3": 0, "mod3_multiples": {1: 1, 2: 2, 3: 0}}
ADD3 = [[0, 1, 2], [1, 2, 0], [2, 0, 1]]
MUL3 = [[0, 0, 0], [0, 1, 2], [0, 2, 1]]
add3 = lambda x, y: ADD3[x][y]
mul3 = lambda x, y: MUL3[x][y]
assert all(ADD3[x][y] == (x + y) % 3 and MUL3[x][y] == (x * y) % 3 for x in range(3) for y in range(3))
check_field([0, 1, 2], add3, mul3, 0, 1)
for n, v in QUOTED["mod3_multiples"].items():
    assert mult(n, 1, add3, 0) == v
assert mult(3, 1, add3, 0) == QUOTED["three_dot_one_mod3"]
print("exr-ordered-rings-c1: all quoted values check")
