"""prp-sum-reindex: reversal and splitting on random lists, including m = -1, m = n, n = 0; second Quick check: the split of sum_{k=0}^{5} at m = 2 is (a0+a1+a2) + (a3+a4+a5)."""
import random

QUOTED = {"qc_m2": ([0, 1, 2], [3, 4, 5]), "qc_m_minus1": ([], [0, 1, 2, 3, 4, 5])}


def S(a, lo, hi):
    return sum(a[k] for k in range(lo, hi + 1))


assert (list(range(0, 3)), list(range(3, 6))) == QUOTED["qc_m2"]
assert (list(range(0, 0)), list(range(0, 6))) == QUOTED["qc_m_minus1"]
random.seed(2)
for _ in range(500):
    n = random.randint(0, 9)
    a = [random.randint(-20, 20) for _ in range(n + 1)]
    assert S(a, 0, n) == sum(a[n - k] for k in range(n + 1))
    for m in range(-1, n + 1):
        assert S(a, 0, n) == S(a, 0, m) + S(a, m + 1, n)
print("ok")
