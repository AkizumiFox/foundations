"""exr-finite-sets-b4: (a) 0..11 pairwise differences not multiples of 12; (b) 3 integers, two
have even sum; (c) five of the eight {0,1}^3 points, no lattice midpoint; (d) k -> floor((k+1)/2)
on {1..8} takes 1..4 each exactly twice; (e) |P({1,2,3})| = 8 > 7; (f) injections of {1..n} to
itself are surjective (n <= 6). Also the Quick checks: 11 integers mod 10; {3..7} via k -> k+2;
{0..4} etc. Verdicts: (b), (e), (f) true; (a), (c), (d) false."""
from itertools import combinations, product, permutations
s = range(12)
assert all((x - y) % 12 != 0 for x, y in combinations(s, 2))
assert all(1 <= abs(x - y) <= 11 for x, y in combinations(s, 2))
for t in combinations(range(-8, 9), 13):
    assert any((x - y) % 12 == 0 for x, y in combinations(t, 2))
for t in combinations(range(-6, 7), 3):
    assert any((x + y) % 2 == 0 for x, y in combinations(t, 2))
cube = list(product((0, 1), repeat=3))
five = cube[:5]
assert len(set(five)) == 5
assert not any(all((p[i] + q[i]) % 2 == 0 for i in range(3)) for p, q in combinations(five, 2))
vals = [(k + 1) // 2 for k in range(1, 9)]
assert vals == [1, 1, 2, 2, 3, 3, 4, 4]
assert all(vals.count(v) == 2 for v in (1, 2, 3, 4))
assert 2 ** 3 == 8 > 7
subsets = [c for r in range(4) for c in combinations((1, 2, 3), r)]
assert len(subsets) == 8
for n in range(0, 7):
    dom = range(1, n + 1)
    for f in product(dom, repeat=n):
        if len(set(f)) == n:
            assert set(f) == set(dom)
# Quick checks
for t in combinations(range(-6, 10), 11):
    assert any((x - y) % 10 == 0 for x, y in combinations(t, 2))
assert [k + 2 for k in range(1, 6)] == [3, 4, 5, 6, 7]
print("ok")
