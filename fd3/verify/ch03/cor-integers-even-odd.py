"""cor-integers-even-odd (b): (2q + 1)^2 = 4q^2 + 4q + 1 = 2(2q^2 + 2q) + 1.
Both sides are polynomials of degree 2 in q, so agreement at more than 2 points is an identity."""
QUOTED = {"expanded": (4, 4, 1), "outer": (2, 2)}  # 4q^2 + 4q + 1; 2(2q^2 + 2q) + 1
a, b, c = QUOTED["expanded"]
s, t = QUOTED["outer"]
for q in range(-50, 51):
    lhs = (2 * q + 1) ** 2
    assert lhs == a * q * q + b * q + c == 2 * (s * q * q + t * q) + 1
    assert lhs % 2 == 1
print("ok")
