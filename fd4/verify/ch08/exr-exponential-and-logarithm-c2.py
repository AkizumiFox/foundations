"""exr-exponential-and-logarithm-c2: X = 4/eps^2 for (a); Y = 4 m^2/eps^2, X = Y^m for (b)."""
from math import log
for eps in [1, 0.5, 0.1]:
    for m in range(1, 4):
        Y = 4 * m * m / eps ** 2
        X = Y ** m
        for f in [1.0001, 2, 50]:
            x = X * f
            assert log(x) < eps * x ** (1 / m)
        for f in [1.0001, 2]:
            x = 4 / eps ** 2 * f
            assert log(x) < eps * x
print("ok")
