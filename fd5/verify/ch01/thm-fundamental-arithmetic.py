"""thm-fundamental-arithmetic: the warning on H = {4k + 1}; plus a brute-force uniqueness check."""
from math import prod

H = lambda h: h >= 1 and h % 4 == 1

def h_prime(h):
    """h in H, h > 1, not a product of two elements of H both > 1."""
    if not (H(h) and h > 1):
        return False
    return not any(H(a) and a > 1 and h % a == 0 and H(h // a) and h // a > 1 for a in range(2, h))

QUOTED = {"h_primes": [9, 21, 49], "n": 441, "f1": (9, 49), "f2": (21, 21)}
K_VALUES = {9: 2, 21: 5, 49: 12, 441: 110}  # membership in H, not quoted
for h, k in K_VALUES.items():
    assert h == 4 * k + 1
for h in QUOTED["h_primes"]:
    assert h_prime(h)
assert prod(QUOTED["f1"]) == QUOTED["n"] == prod(QUOTED["f2"])
assert sorted(QUOTED["f1"]) != sorted(QUOTED["f2"])
# 9 divides 21*21 inside H (quotient 49 in H), but 9 does not divide 21
assert (21 * 21) % 9 == 0 and H(21 * 21 // 9) and 21 % 9 != 0
# closure: (4k+1)(4l+1) = 4(4kl+k+l)+1
for k in range(30):
    for l in range(30):
        assert (4 * k + 1) * (4 * l + 1) == 4 * (4 * k * l + k + l) + 1
# existence of H-factorizations (warning's claim) for small h
def has_h_fact(h):
    return h == 1 or h_prime(h) or any(H(a) and a > 1 and h % a == 0 and H(h // a) and h // a > 1
                                       and has_h_fact(a) and has_h_fact(h // a) for a in range(2, h))
assert all(has_h_fact(h) for h in range(1, 800) if H(h))
print("thm-fundamental-arithmetic: ok")
