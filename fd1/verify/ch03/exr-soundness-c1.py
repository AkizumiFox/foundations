"""exr-soundness-c1 (Section 3.5): rule X (and -> or) preserves truth in all four rows;
rule Y (or -> and) fails at p = T, q = F; p |= q fails there."""
import itertools

QUOTED = {"failing rows of Y": 2}
for a, b in itertools.product((True, False), repeat=2):
    assert (not (a and b)) or (a or b)
bad = [(a, b) for a, b in itertools.product((True, False), repeat=2) if (a or b) and not (a and b)]
assert bad == [(True, False), (False, True)] and len(bad) == QUOTED["failing rows of Y"]
p, q = True, False
assert p and not q
print("exr-soundness-c1: all quoted values check")
