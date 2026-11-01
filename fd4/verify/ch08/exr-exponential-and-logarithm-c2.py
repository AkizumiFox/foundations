"""exr-exponential-and-logarithm-c2: (a) X = (4/eps)^4 = 256/eps^4 gives log x < 4 x^(1/4) < eps sqrt x;
(b) delta = 2 eps/m, Y = 256/delta^4 = 16 m^4/eps^4, X = Y^(m/2) gives log x < eps x^(1/m);
the alternative route of the scheme, X = (2m/eps)^(2m), also works."""
from math import log, sqrt, isclose
for eps in [5, 1, 0.5, 0.1]:
    Xa = 256 / eps ** 4
    assert isclose(Xa, (4 / eps) ** 4)
    for f in [1.0001, 2, 50]:
        x = Xa * f
        assert x ** 0.25 > 4 / eps
        assert log(x) < 4 * x ** 0.25 < eps * sqrt(x)
    for m in range(1, 4):
        delta = 2 * eps / m
        Y = 256 / delta ** 4
        assert isclose(Y, 16 * m ** 4 / eps ** 4)
        X = Y ** (m / 2)
        for f in [1.0001, 2, 50]:
            x = X * f
            y = x ** (2 / m)
            assert y > Y and isclose(sqrt(y), x ** (1 / m))
            assert log(y) < delta * sqrt(y)
            assert log(x) < eps * x ** (1 / m)
        X2 = (2 * m / eps) ** (2 * m)
        for f in [1.0001, 2, 50]:
            x = X2 * f
            assert log(x) < eps * x ** (1 / m)
print("ok")
