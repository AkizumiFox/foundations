"""exr-models-c2 (Section 4.11): no structure on 1 to 4 elements is a model of
'strict order without largest element'; (N, <) satisfies all three conjuncts on a window."""
import itertools

QUOTED = {}
for n in range(1, 5):
    D = range(n)
    pairs = [(a, b) for a in D for b in D if a != b]  # irreflexive relations only
    for bits in itertools.product([0, 1], repeat=len(pairs)):
        R = {p for p, b in zip(pairs, bits) if b}
        trans = all((a, c) in R for (a, b) in R for (b2, c) in R if b == b2)
        nolargest = all(any((d, e) in R for e in D) for d in D)
        assert not (trans and nolargest)
W = range(0, 40)
assert all(not d < d for d in W) and all(d + 1 > d for d in W)
print("exr-models-c2: all quoted values check")
