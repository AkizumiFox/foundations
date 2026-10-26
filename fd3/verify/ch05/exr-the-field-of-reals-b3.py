"""exr-the-field-of-reals-b3: a = (1, 0, 0, ...), b = (0, 1, 1, ...) are eventually
constant, neither is the zero sequence, and a_n b_n = 0 for every n; a is eventually 0
(class 0_R), b is eventually 1 (class 1_R)."""
from fractions import Fraction as F

QUOTED = {"a": (1, 0, 0), "b": (0, 1, 1), "product": 0, "a_tail": 0, "b_tail": 1, "from_index": 1}


def a(n):
    return F(1) if n == 0 else F(0)


def b(n):
    return F(0) if n == 0 else F(1)


N = 500
assert tuple(a(n) for n in range(3)) == QUOTED["a"]
assert tuple(b(n) for n in range(3)) == QUOTED["b"]
assert any(a(n) != 0 for n in range(N)) and any(b(n) != 0 for n in range(N))
assert all(a(n) * b(n) == QUOTED["product"] for n in range(N))
k = QUOTED["from_index"]
assert all(a(n) == QUOTED["a_tail"] for n in range(k, N))
assert all(b(n) == QUOTED["b_tail"] for n in range(k, N))
# eventually constant, so Cauchy with threshold k at every tolerance
assert all(abs(a(m) - a(n)) == 0 and abs(b(m) - b(n)) == 0 for m in range(k, 60) for n in range(k, 60))
print("ok")
