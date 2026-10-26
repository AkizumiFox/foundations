"""exr-cuts-c1: q' = (q^2 + 2)/(2q): q - q' = (q^2 - 2)/(2q), q'^2 - 2 = (q^2 - 2)^2/(4q^2)."""
from fractions import Fraction as F
QUOTED = {"q_prime_numerator_constant": 2, "q_prime_denominator_factor": 2}

for q in [F(n, 37) for n in range(1, 400)]:
    qp = (q * q + QUOTED["q_prime_numerator_constant"]) / (QUOTED["q_prime_denominator_factor"] * q)
    assert q - qp == (q * q - 2) / (2 * q)
    assert qp * qp - 2 == (q * q - 2) ** 2 / (4 * q * q)
    if q * q > 2:
        assert 0 < qp < q and qp * qp > 2
print("ok")
