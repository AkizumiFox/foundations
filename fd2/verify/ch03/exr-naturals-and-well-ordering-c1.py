"""exr-naturals-and-well-ordering-c1 (Ch 7, 01): for non-empty S in N bounded by M, the least
upper bound of S in N lies in S and is its greatest element (random finite tests)."""
import random
random.seed(7)
for _ in range(2000):
    M = random.randint(0, 40)
    S = {random.randint(0, M) for _ in range(random.randint(1, 10))}
    U = [u for u in range(0, M + 1) if all(s <= u for s in S)]
    assert M in U
    u = min(U)
    assert u in S and u == max(S)
    # the alternative route: least element of {M - s}
    assert M - min(M - s for s in S) == max(S)
print("exr-naturals-and-well-ordering-c1: all quoted values check")
