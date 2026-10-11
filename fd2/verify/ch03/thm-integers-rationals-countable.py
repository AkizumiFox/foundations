"""thm-integers-rationals-countable: z(2k) = k, z(2k+1) = -(k+1); first values 0, -1, 1, -2, 2;
z is a bijection from {0..2N} onto {-N..N}; the rational list repeats 1 as 1/1, 2/2, 3/3."""
from fractions import Fraction as Fr
QUOTED = {"first_values": [0, -1, 1, -2, 2]}
def z(n):
    k, r = divmod(n, 2)
    return k if r == 0 else -(k + 1)
assert [z(n) for n in range(5)] == QUOTED["first_values"]
N = 3000
vals = [z(n) for n in range(2 * N + 1)]
assert sorted(vals) == list(range(-N, N + 1))
assert all(z(2 * m) == m for m in range(N))
assert all(z(2 * (n - 1) + 1) == -n for n in range(1, N))
assert Fr(1, 1) == Fr(2, 2) == Fr(3, 3) == 1
print("ok")
