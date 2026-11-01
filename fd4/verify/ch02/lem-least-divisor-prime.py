"""lem-least-divisor-prime and the remark after it (least divisor e has e*e <= p; the case 11)."""

def is_prime(p):
    return p >= 2 and all(p % d for d in range(2, p))

QUOTED = {"p": 11, "checks": [2, 3], "four_sq": 16}
assert 4 * 4 == QUOTED["four_sq"] > QUOTED["p"]
for d in QUOTED["checks"]:
    assert d * d <= QUOTED["p"] and QUOTED["p"] % d != 0
assert is_prime(QUOTED["p"])
for n in range(2, 3000):
    e = min(d for d in range(2, n + 1) if n % d == 0)
    assert is_prime(e)
    if not is_prime(n):
        assert e * e <= n
print("lem-least-divisor-prime: ok")
