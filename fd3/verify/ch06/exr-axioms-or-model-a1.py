"""exr-axioms-or-model-a1 (a)(i): sqrt2 + sqrt3 > 3 via (b + c)^2 = 5 + 2 bc with b^2 = 2,
c^2 = 3, (bc)^2 = 6; 5 + 2 bc > 9 iff bc > 2 iff 6 > 4 (bc >= 0). Exact integer checks,
plus a decimal sanity check."""
from decimal import Decimal, getcontext
QUOTED = {"square": "5 + 2bc", "compare": (6, 4, 9)}
# (b + c)^2 = b^2 + 2bc + c^2 = 2 + 3 + 2bc
assert 2 + 3 == 5
assert 2 * 3 == 6            # (bc)^2 = b^2 c^2
assert 9 - 5 == 2 * 2        # 5 + 2 bc > 9 iff bc > 2
assert 6 > 2 ** 2
getcontext().prec = 40
s = Decimal(2).sqrt() + Decimal(3).sqrt()
assert s > 3 and abs(s * s - (5 + 2 * Decimal(6).sqrt())) < Decimal("1e-30")
print("ok")
