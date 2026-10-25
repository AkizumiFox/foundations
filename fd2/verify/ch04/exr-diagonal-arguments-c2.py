"""exr-diagonal-arguments-c2: pi_b swaps 2q, 2q+1 iff b(q) = 1; pi_b o pi_b = id; the
diagonal b(n) = 1 iff f_n(2n) = 2n gives pi(2n) != f_n(2n); b -> pi_b is injective
(checked on finite windows and sample lists)."""
import random

QUOTED = {}


def pi(b, m):
    q, r = divmod(m, 2)
    return m if b(q) == 0 else 2 * q + 1 - r


random.seed(1)
for _ in range(200):
    bits = [random.randint(0, 1) for _ in range(40)]
    b = lambda q, bits=bits: bits[q]
    vals = [pi(b, m) for m in range(80)]
    assert sorted(vals) == list(range(80))                 # bijection on the window
    assert all(pi(b, pi(b, m)) == m for m in range(80))     # involution
# diagonal against a sample list of permutations of the window
lists = []
for _ in range(30):
    bits = [random.randint(0, 1) for _ in range(40)]
    lists.append(lambda m, bits=bits: pi(lambda q: bits[q], m))
lists.append(lambda m: m)                                    # identity
bdiag = [1 if lists[n](2 * n) == 2 * n else 0 for n in range(len(lists))]
for n, fn in enumerate(lists):
    assert pi(lambda q: bdiag[q], 2 * n) != fn(2 * n)
# injectivity of b -> pi_b: pi_b(2q) is 2q + b(q)
for _ in range(50):
    bits = [random.randint(0, 1) for _ in range(20)]
    assert [pi(lambda q: bits[q], 2 * q) - 2 * q for q in range(20)] == bits
print("exr-diagonal-arguments-c2: all quoted values check")
