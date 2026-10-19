"""exr-soundness-c3 (Section 4.7, A changed table): with (V4) replaced by exclusive or, the
or-E case still holds for every value combination (a true disjunction has a true side),
the or-I case fails at p = q = T, and p |- p or q is not valid for the new table."""
import itertools

xor = lambda a, b: a != b
B = (True, False)
# or-E case, in the form the proof uses: m (the context) true, x or y true, each box
# (context and its side true gives z) -> z true
for m, x, y, z in itertools.product(B, repeat=4):
    if m and xor(x, y) and (not (m and x) or z) and (not (m and y) or z):
        assert z
# or-I case fails
fails = [(x, y) for x, y in itertools.product(B, repeat=2) if x and not xor(x, y)]
assert fails == [(True, True)]
print("exr-soundness-c3: all quoted values check")
