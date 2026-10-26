"""exm-limit-from-definition: (n^2+1)/(2n^2+3) - 1/2 = -1/(2(2n^2+3)); 2(2n^2+3) - (n+1) = 4n^2 - n + 5,
which is >= 3n + 5 for n >= 1 and = 5 at n = 0; hence 1/(2(2n^2+3)) <= 1/(n+1) for every n.
Also: the table's rows chain (bound <= 1/(n+1) < eps once n + 1 >= N) for sample eps."""
from fractions import Fraction as Q

QUOTED = {"at_0": 5}
assert 2 * (2 * 0 + 3) - (0 + 1) == QUOTED["at_0"]
for k in range(0, 3000):
    d = Q(k * k + 1, 2 * k * k + 3) - Q(1, 2)
    assert d == Q(-1, 2 * (2 * k * k + 3))
    assert 2 * (2 * k * k + 3) - (k + 1) == 4 * k * k - k + 5 > 0
    if k >= 1:
        assert k * k >= k
        assert 4 * k * k - k + 5 >= 3 * k + 5
    assert abs(d) <= Q(1, k + 1)

# forward proof on samples: least N with 1/m < eps for m >= N, then every n >= N works
for eps in [Q(1, 3), Q(1, 10), Q(2, 7), Q(1, 1000)]:
    N = 1
    while not Q(1, N) < eps:
        N += 1
    for n in range(N, N + 500):
        assert abs(Q(n * n + 1, 2 * n * n + 3) - Q(1, 2)) <= Q(1, n + 1) < eps
print("ok")
