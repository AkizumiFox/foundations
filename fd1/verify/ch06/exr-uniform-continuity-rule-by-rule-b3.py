"""exr-uniform-continuity-rule-by-rule-b3: sqrt on [0, inf), delta = eps^2; the school
inequality |sqrt x - sqrt y| <= sqrt|x - y| on samples, and |x - y| < eps^2 gives
|sqrt x - sqrt y| < eps."""
import math

QUOTED = {"delta = eps^k, k": 2}
for eps in [1.0, 0.5, 0.01, 3.0]:
    delta = eps ** QUOTED["delta = eps^k, k"]
    for x in [0.0, 1e-6, 0.3, 2.0, 50.0, 1e4]:
        for frac in [0.0, 0.2, 0.5, 0.99]:
            for y in (x + frac * delta, max(0.0, x - frac * delta)):
                assert abs(math.sqrt(x) - math.sqrt(y)) <= math.sqrt(abs(x - y)) + 1e-12
                if abs(x - y) < delta:
                    assert abs(math.sqrt(x) - math.sqrt(y)) < eps
print("exr-uniform-continuity-rule-by-rule-b3: all quoted values check")
