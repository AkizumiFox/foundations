"""exr-models-c1 (Section 4.11): 'injective implies surjective' holds for every function on a
domain of 1 to 5 elements; successor on N is injective and misses 0 (window)."""
import itertools

QUOTED = {"missed value": 0}
for n in range(1, 6):
    D = range(n)
    for f in itertools.product(D, repeat=n):
        inj = len(set(f)) == n
        surj = set(f) == set(D)
        assert (not inj) or surj
N = range(0, 2000)
succ = [d + 1 for d in N]
assert len(set(succ)) == len(succ)
assert QUOTED["missed value"] not in succ and min(succ) == 1
print("exr-models-c1: all quoted values check")
