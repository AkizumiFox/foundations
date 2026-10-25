"""exr-definability-and-isomorphism-b3 (Section 7.5): all 24 permutations of {1,2,3,4};
exactly the identity and the swap of 1, 2 are automorphisms; the four formulas define
{3}, {4}, {1,2}, {3,4}; the other two-element sets and {1}, {2} are moved by the swap."""
import itertools

D = [1, 2, 3, 4]
R = {(1, 1), (1, 2), (2, 1), (2, 2), (3, 3)}
A = []
for p in itertools.permutations(D):
    h = dict(zip(D, p))
    if all(((x, y) in R) == ((h[x], h[y]) in R) for x in D for y in D):
        A.append(h)
QUOTED = {"autos": 2}
assert len(A) == QUOTED["autos"]
swap = {1: 2, 2: 1, 3: 3, 4: 4}
assert swap in A and {d: d for d in D} in A
assert [x for x in D if (x, x) in R and all((x, y) not in R or y == x for y in D)] == [3]
assert [x for x in D if (x, x) not in R] == [4]
other = lambda x: any((x, y) in R and y != x for y in D)
assert [x for x in D if other(x)] == [1, 2]
assert [x for x in D if not other(x)] == [3, 4]
for S in [{1}, {2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}]:
    assert {swap[s] for s in S} != S
print("exr-definability-and-isomorphism-b3: all quoted values check")
