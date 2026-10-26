"""exr-where-n-comes-from-b2 (and the section's second Quick check): Kuratowski pairs of
von Neumann numerals. (0,1) = {1, 2}; (1,0) = {{1}, 2}; (1,1) = {{1}}; (0,1) != (1,0) via
1 in (0,1), 1 not in (1,0); 2 elements if a != b, 1 if a = b; (0,1) is not a numeral;
{{0}} = (0,0) = {1}."""
E0 = frozenset()
def S(x): return x | frozenset([x])
def num(k):
    x = E0
    for _ in range(k): x = S(x)
    return x
def fs(*a): return frozenset(a)
def pair(a, b): return fs(fs(a), fs(a, b))
N = [num(k) for k in range(8)]
QUOTED = {"(0,1)": fs(N[1], N[2]), "(1,0)": fs(fs(N[1]), N[2]), "(1,1)": fs(fs(N[1]))}
assert pair(N[0], N[1]) == QUOTED["(0,1)"]
assert pair(N[1], N[0]) == QUOTED["(1,0)"]
assert pair(N[1], N[1]) == QUOTED["(1,1)"]
assert N[1] in pair(N[0], N[1]) and N[1] not in pair(N[1], N[0])
assert N[1] != fs(N[1]) and N[0] in N[1] and N[1] not in N[1] and N[1] in N[2]
assert pair(N[0], N[1]) != pair(N[1], N[0])
for a in range(5):
    for b in range(5):
        assert len(pair(N[a], N[b])) == (2 if a != b else 1)
        # characteristic property on small numerals
        for c in range(5):
            for d in range(5):
                assert (pair(N[a], N[b]) == pair(N[c], N[d])) == (a == c and b == d)
assert N[0] not in pair(N[0], N[1]) and all(pair(N[0], N[1]) != n for n in N)
# Quick check: {{0}} = (0,0) = {1}
assert fs(fs(N[0])) == pair(N[0], N[0]) == fs(N[1])
print("ok")
