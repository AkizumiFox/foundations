"""exm-modus-tollens-instance (Ch 2, Section 2.3): x > 2 gives x^2 = x*x > 2x > 4;
x^2 <= 4 forces x <= 2. The fold "Modus tollens and testing a claim": 2^p - 1 is prime
for p = 2, 3, 5, 7 (3, 7, 31, 127) and 2^11 - 1 = 2047 = 23 * 89."""
from fractions import Fraction as F

QUOTED = {
    "threshold": 2,
    "square threshold": 4,
    "confirming": {2: 3, 3: 7, 5: 31, 7: 127},
    "refuting p": 11,
    "refuting value": 2047,
    "factors": (23, 89),
}


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, int(n ** 0.5) + 1))


pts = [F(k, 16) for k in range(-160, 161)] + [F(2) + F(1, 10**6), F(2) - F(1, 10**6)]
for x in pts:
    if x > 2:
        assert x * x > 2 * x > 4
    if x * x <= QUOTED["square threshold"]:
        assert x <= QUOTED["threshold"]

for p, m in QUOTED["confirming"].items():
    assert is_prime(p) and 2 ** p - 1 == m and is_prime(m), p
p = QUOTED["refuting p"]
a, b = QUOTED["factors"]
assert is_prime(p) and 2 ** p - 1 == QUOTED["refuting value"] == a * b
assert not is_prime(QUOTED["refuting value"]) and is_prime(a) and is_prime(b)
print("exm-modus-tollens-instance: all quoted values check")
