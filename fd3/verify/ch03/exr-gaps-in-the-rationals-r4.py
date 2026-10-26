"""exr-gaps-in-the-rationals-r4: (2m+1)^3 = 2(4m^3 + 6m^2 + 3m) + 1; (2q - p)^3 - 2(p - q)^3 =
-3p^3 + 12p^2 q - 18pq^2 + 10q^3, not a constant multiple of p^3 - 2q^3; parity: every integer is 2m or 2m + 1, not both;
no p, q <= 300 with p^3 = 2q^3."""
from fractions import Fraction as F
import math
QUOTED = {"coeffs": (-3, 12, -18, 10)}
for m in range(-20, 21):
    assert (2*m + 1)**3 == 2*(4*m**3 + 6*m*m + 3*m) + 1
a3, a2, a1, a0 = QUOTED["coeffs"]
for p in range(-5, 6):
    for q in range(-5, 6):
        assert (2*q - p)**3 - 2*(p - q)**3 == a3*p**3 + a2*p*p*q + a1*p*q*q + a0*q**3
# not c * (p^3 - 2q^3): the p^2 q coefficient is 12 != 0
assert a2 != 0
for a in range(-40, 41):
    m, r = divmod(a, 2)
    assert r in (0, 1) and a == 2*m + r
    assert not any(a == 2*k for k in range(-40, 41)) or not any(a == 2*k + 1 for k in range(-40, 41))
assert not any(p**3 == 2*q**3 for p in range(1, 400) for q in range(1, 300))
print("ok")
