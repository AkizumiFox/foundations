"""exr-counting-and-descriptions-r1 (Section 5.8, R1): in every term over the variables x, y,
the constant 0 and the two-place +, of height at most 2 (all of them) and a sample of
heights 3 and 4, the number of occurrences of + is one
less than the number of occurrences of variables and constants; (x + 0) + (y + x) has 4 and 3."""

QUOTED = {"atoms": 4, "plus": 3}


def terms(h):
    if h == 0:
        return ["x", "y", "0"]
    smaller = terms(h - 1)
    return smaller + [("+", s, t) for s in smaller for t in smaller]


def a(t):
    return 1 if isinstance(t, str) else a(t[1]) + a(t[2])


def p(t):
    return 0 if isinstance(t, str) else p(t[1]) + p(t[2]) + 1


level = ["x", "y", "0"]
for h in range(1, 4):
    level = level + [("+", s, t) for s in level for t in level][:20000]
for t in level:
    assert p(t) == a(t) - 1
# height 4, sampled along the left and right spines
for t in level[:200]:
    for u in level[:200]:
        assert p(("+", t, u)) == a(("+", t, u)) - 1
ex = ("+", ("+", "x", "0"), ("+", "y", "x"))
assert a(ex) == QUOTED["atoms"] and p(ex) == QUOTED["plus"]
print("exr-counting-and-descriptions-r1: all quoted values check")
