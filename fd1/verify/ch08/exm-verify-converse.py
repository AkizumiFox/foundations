"""exm-verify-converse (Proof B, Ch 5, Section 5.6): n = 2k gives n^2 = 4k^2 = 2(2k^2); the row
P false, Q true makes P -> Q true and Q -> P false; 'if x > 1 then x^2 > 1' is true and its
converse fails at x = -2; the claim (n^2 even => n even) holds."""
from fractions import Fraction as F
QUOTED = {"row": (False, True), "x": -2}
imp = lambda a, b: (not a) or b
P, Q = QUOTED["row"]
assert imp(P, Q) and not imp(Q, P)
for k in range(-500, 501):
    n = 2 * k
    assert n * n == 4 * k * k == 2 * (2 * k * k)
for n in range(-1000, 1001):
    if (n * n) % 2 == 0:
        assert n % 2 == 0
for t in range(-300, 301):
    x = F(t, 17)
    if x > 1:
        assert x * x > 1
x = QUOTED["x"]
assert x * x > 1 and not x > 1
print("exm-verify-converse: all quoted values check")
