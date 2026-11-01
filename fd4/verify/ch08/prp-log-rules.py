"""prp-log-rules (c): (1 + t/2)^2 = 1 + t + t^2/4; exp t > 1 + t for t != 0; 1/2 < log 2 < 1;
QC: 2^sqrt2 > 2, sqrt2^sqrt2 < 2."""
from fractions import Fraction as Fr
from math import exp, log, sqrt
for k in range(-50, 51):
    t = Fr(k, 7)
    assert (1 + t / 2) ** 2 == 1 + t + t * t / 4
    if t != 0:
        assert exp(float(t)) > 1 + float(t)
assert 0.5 < log(2) < 1
assert 2 ** sqrt(2) > 2 and sqrt(2) ** sqrt(2) < 2
print("ok")
