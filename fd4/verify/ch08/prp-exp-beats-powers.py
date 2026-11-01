"""prp-exp-beats-powers: (a) exp x > (x/(k+1))^(k+1) and exp x > M x^k past M (k+1)^(k+1);
(b) log x < m x^(1/m) and log x < eps x past 4/eps^2; quoted thresholds 27,000 and 40,000."""
from math import exp, log
QUOTED = {"exp_thr": 27000, "log_thr": 40000}
assert 1000 * 3 ** 3 == QUOTED["exp_thr"] and 4 / (1 / 100) ** 2 == QUOTED["log_thr"]
for k in range(0, 6):
    for x in [0.01, 0.5, 1, 2, 5, 20, 60]:
        assert exp(x) > (x / (k + 1)) ** (k + 1)
    for M in [0.5, 1, 3]:
        x0 = M * (k + 1) ** (k + 1)
        for f in [1.0001, 1.5, 3]:
            x = x0 * f
            if x < 700:
                assert exp(x) > M * x ** k
# exp x > 1000 x^2 for x > 27000: compare logs
for x in [27000.01, 30000, 1e5]:
    assert x > log(1000) + 2 * log(x)
for m in range(1, 6):
    for x in [1e-3, 0.5, 1, 2, 10, 1e3, 1e6]:
        assert log(x) < m * x ** (1 / m)
for eps in [2, 1, 0.1, 0.01]:
    for f in [1.0001, 2, 10]:
        x = 4 / eps ** 2 * f
        assert log(x) < 2 * x ** 0.5 <= eps * x * (1 + 1e-12)
print("ok")
