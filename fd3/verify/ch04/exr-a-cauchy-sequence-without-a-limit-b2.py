"""exr-a-cauchy-sequence-without-a-limit-b2: H_{2^k} >= 1 + k/2 (k <= 11); H_1 = 1; 2^{k+1} = 2^k + 2^k."""
from fractions import Fraction as F
QUOTED = {"H1": 1, "gain": F(1, 2)}
H = [F(0)]
for n in range(2**11):
    H.append(H[-1] + F(1, n + 1))
assert H[1] == 1
for k in range(12):
    assert H[2**k] >= 1 + F(k, 2)
    assert 2**(k + 1) == 2**k + 2**k and 2**k >= 1
assert H[1] == QUOTED["H1"] and all(H[2**(k+1)] - H[2**k] >= QUOTED["gain"] for k in range(11))
print("ok")
