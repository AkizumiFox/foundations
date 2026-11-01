"""exr-...-a1 (03): (c) a = (1, 4): A1 = 1, A2 = 5/2, x = 3/2, chain 4 <= 4 <= 25/4, Bernoulli 1 + 2x = 4;
(d) (-1,-1,1): abc = 1 > -1/27."""
from fractions import Fraction as Fr
QUOTED = {"A1": Fr(1), "A2": Fr(5, 2), "x": Fr(3, 2), "chain": (4, 4, Fr(25, 4))}
a1, a2 = Fr(1), Fr(4)
A1, A2 = a1, (a1 + a2) / 2
x = A2 / A1 - 1
assert (A1, A2, x) == (QUOTED["A1"], QUOTED["A2"], QUOTED["x"])
assert (a1 * a2, A1 * a2, A2 ** 2) == QUOTED["chain"]
assert 1 + 2 * x == a2 / A1 == 4 and (1 + x) ** 2 == Fr(25, 4)
assert (-1) * (-1) * 1 == 1 and Fr(-1, 3) ** 3 == Fr(-1, 27) < 1
print("ok")
