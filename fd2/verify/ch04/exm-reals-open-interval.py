"""exm-reals-open-interval: s(x) = x/(1+|x|), t(y) = y/(1-|y|), and the quoted values."""
from fractions import Fraction as F

QUOTED = {"s(1)": F(1, 2), "s(-3)": F(-3, 4)}


def s(x):
    return x / (1 + abs(x))


def t(y):
    return y / (1 - abs(y))


assert s(F(1)) == QUOTED["s(1)"] and s(F(-3)) == QUOTED["s(-3)"]
# the two identities used in the text, 1 - |s(x)| = 1/(1+|x|) and 1 + |t(y)| = 1/(1-|y|)
for k in range(-300, 301):
    x = F(k, 11)
    assert 1 - abs(s(x)) == 1 / (1 + abs(x))
for k in range(-99, 100):
    y = F(k, 100)
    assert 1 + abs(t(y)) == 1 / (1 - abs(y))
# exact checks on a grid
for k in range(-200, 201):
    x = F(k, 7)
    assert abs(s(x)) < 1 and t(s(x)) == x
for k in range(-99, 100):
    y = F(k, 100)
    assert s(t(y)) == y
# affine maps
c, d = F(-2), F(5)
for k in range(1, 50):
    u = F(k, 50)
    v = c + (d - c) * u
    assert c < v < d and (v - c) / (d - c) == u
print("ok")
