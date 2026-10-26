"""exr-where-n-comes-from-b1 (and the section's first Quick check, A1 (a), (b)):
von Neumann numerals as frozensets. S(4) = 5; |n| = n for n <= 5; 2 u 3 = 3, 2 n 3 = 2;
{1} subset of 3; {1} is none of 0..5; 3 written with braces; 1 subset of 3; 3 not in 1;
S(3) = {0, 1, 2, 3} = 4; 2 in 3 and 2 subset of 3."""
E0 = frozenset()
def S(x): return x | frozenset([x])
def num(k):
    x = E0
    for _ in range(k): x = S(x)
    return x
QUOTED = {"S(4)": 5, "sizes": {n: n for n in range(6)}, "union": 3, "inter": 2}
N = [num(k) for k in range(7)]
assert S(N[4]) == frozenset(N[:5]) == N[QUOTED["S(4)"]]
for n, size in QUOTED["sizes"].items():
    assert len(N[n]) == size and N[n] == frozenset(N[:n])
assert N[2] | N[3] == N[QUOTED["union"]] and N[2] & N[3] == N[QUOTED["inter"]]
one_set = frozenset([N[1]])
assert one_set <= N[3]
assert all(one_set != N[k] for k in range(6))
assert N[1] == frozenset([E0]) and one_set != N[1]
# Quick check: 3 with braces; 1 subset of 3; 3 not in 1
three = frozenset([E0, frozenset([E0]), frozenset([E0, frozenset([E0])])])
assert three == N[3] and N[1] <= N[3] and N[3] not in N[1]
# A1 (a), (b)
assert S(N[3]) == frozenset(N[:4]) == N[4]
assert N[2] in N[3] and N[2] <= N[3]
print("ok")
