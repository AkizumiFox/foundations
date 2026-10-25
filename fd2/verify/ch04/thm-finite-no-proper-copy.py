"""Warning after exm-hilbert-hotel: x -> x/(1+x) sends 1/n to 1/(n+1), inverse y -> y/(1-y);
1/n <= 1/2 for n >= 2; also exm-hilbert-hotel: 2n != 1 and n -> 2n injective."""
from fractions import Fraction as Fr
F = Fr
QUOTED = {"bound": F(1, 2)}
for n in range(1, 2000):
    x = Fr(1, n)
    y = x / (1 + x)
    assert y == Fr(1, n + 1)
    assert y / (1 - y) == x
    if n >= 2:
        assert x <= QUOTED["bound"]
assert all(2 * n != 1 for n in range(1000))
assert len({2 * n for n in range(1000)}) == 1000
print("ok")
