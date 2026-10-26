"""exr-units-and-crt-r1: (a + b) - (a' + b') = (a + b' - a' - b) + 2(b - b'), and
(a + b) - (a - b) = 2b; the map agrees with the parity of a - b on pairs in a window."""
from itertools import product
for a, b, a2, b2 in product(range(-3, 4), repeat=4):
    assert (a + b) - (a2 + b2) == (a + b2 - a2 - b) + 2*(b - b2)
    assert (a + b) - (a - b) == 2*b
for A in range(20):
    for B in range(20):
        assert (A + B) % 2 == (A - B) % 2
print("ok")
