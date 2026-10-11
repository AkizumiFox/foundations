"""exr-gcd-and-bezout-c2: gcd(ka, kb) = k gcd(a, b) (sampled), the instance gcd(12, 42) = 6 gcd(2, 7) = 6
with 2*(-3) + 7*1 = 1, and the counterexample in the marking scheme (1 | 6, 1 | 9, 1 not a multiple of 3)."""
import math
for k in range(1, 12):
    for a in range(-20, 21):
        for b in range(-20, 21):
            assert math.gcd(k * a, k * b) == k * math.gcd(a, b)
QUOTED = {"instance": 6, "coprime": (-3, 1)}
assert math.gcd(12, 42) == 6 * math.gcd(2, 7) == QUOTED["instance"]
assert 2 * QUOTED["coprime"][0] + 7 * QUOTED["coprime"][1] == 1
assert 6 % 1 == 0 and 9 % 1 == 0 and 1 % 3 != 0
print("ok")
