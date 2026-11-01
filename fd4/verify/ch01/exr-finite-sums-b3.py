"""exr-finite-sums-b3: 1/k^2 - 1/(k+1)^2 = (2k+1)/(k^2(k+1)^2); sum_{k=1}^{n} = 1 - 1/(n+1)^2, also n = 0."""
from fractions import Fraction as Fr
for k in range(1, 300):
    assert Fr(1, k * k) - Fr(1, (k + 1) ** 2) == Fr(2 * k + 1, k * k * (k + 1) ** 2)
    assert (k + 1) ** 2 - k * k == 2 * k + 1
for n in range(0, 150):
    assert sum(Fr(2 * k + 1, k * k * (k + 1) ** 2) for k in range(1, n + 1)) == 1 - Fr(1, (n + 1) ** 2)
print("ok")
