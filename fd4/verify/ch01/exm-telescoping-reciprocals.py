"""exm-telescoping-reciprocals: 1/((j+1)(j+2)) = b_{j+1} - b_j with b_j = -1/(j+1); sum = b_n - b_0 = 1 - 1/(n+1) = n/(n+1); the hook's values 1/2, 2/3, 3/4; scratch-work check 1/k - 1/(k+1) = 1/(k(k+1))."""
from fractions import Fraction as Fr
QUOTED = {"partial": [Fr(1, 2), Fr(2, 3), Fr(3, 4)]}
b = lambda j: -Fr(1, j + 1)
for k in range(1, 200):
    assert Fr(1, k) - Fr(1, k + 1) == Fr(1, k * (k + 1))
for j in range(0, 200):
    assert Fr(1, (j + 1) * (j + 2)) == b(j + 1) - b(j)
for n in range(1, 200):
    S = sum(Fr(1, k * (k + 1)) for k in range(1, n + 1))
    assert S == b(n) - b(0) == 1 - Fr(1, n + 1) == Fr(n, n + 1)
assert [sum(Fr(1, k * (k + 1)) for k in range(1, n + 1)) for n in (1, 2, 3)] == QUOTED["partial"]
print("ok")
