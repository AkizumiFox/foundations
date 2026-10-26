"""exm-limit-alternating-numerator: a_n = (2n + (-1)^n)/(n+1); a_n - 2 = ((-1)^n - 2)/(n+1);
|(-1)^n - 2| in {1, 3}; |a_n - 2| <= 3/(n+1); distances 1, 3/2, 1/3, 3/4, 1/5 for n = 0..4.
Quick check (eps = 1/10): least N with 1/m < eps/3 for all m >= N is 31; the least N valid in the
definition is 30 (at n = 29 the distance is exactly 1/10).
Method box instance: N = max(N', n0) with C = 3, n0 = 0."""
from fractions import Fraction as Q

QUOTED = {
    "distances": [Q(1), Q(3, 2), Q(1, 3), Q(3, 4), Q(1, 5)],
    "step3_N": 31,
    "least_N": 30,
    "dist_29": Q(1, 10),
}


def a(n):
    return Q(2 * n + (-1) ** n, n + 1)


for n in range(0, 5000):
    assert a(n) - 2 == Q((-1) ** n - 2, n + 1)
    assert abs((-1) ** n - 2) in (1, 3)
    assert abs(a(n) - 2) <= Q(3, n + 1)
assert [abs(a(n) - 2) for n in range(5)] == QUOTED["distances"]

eps = Q(1, 10)
# step (3): least N with 1/m < eps/3 for every m >= N (1/m decreases, so test m = N)
N = 1
while not Q(1, N) < eps / 3:
    N += 1
assert N == QUOTED["step3_N"]
assert all(Q(1, m) < eps / 3 for m in range(N, N + 2000))
assert not Q(1, 30) < eps / 3


# least N in the definition: all n >= N have distance < eps (checked on a long range; beyond
# n = 30 the bound 3/(n+1) <= 3/31 < 1/10 covers every n)
def works(N):
    return all(abs(a(n) - 2) < eps for n in range(N, 3000))


assert Q(3, 31) < eps
least = next(N for N in range(0, 3000) if works(N))
assert least == QUOTED["least_N"]
assert abs(a(29) - 2) == QUOTED["dist_29"]

# method box with C = 3, n0 = 0: N = max(N', 0) gives a valid threshold for sample eps
for e in [Q(1, 2), Q(1, 7), Q(3, 100)]:
    Np = 1
    while not Q(1, Np) < e / 3:
        Np += 1
    Nn = max(Np, 0)
    assert all(abs(a(n) - 2) <= Q(3, n + 1) < e for n in range(Nn, Nn + 1000))
print("ok")
