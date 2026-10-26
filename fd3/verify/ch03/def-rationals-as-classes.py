"""def-rationals-as-classes (Section 10.4): the example classes, checked on a window of
Z x Z_{>0}: [(1, 2)] = {(k, 2k)}, [(-2, 1)] = {(-2s, s)}, [(0, 1)] = {(0, s)}; (4, 6), (6, 9)
lie in [(2, 3)]; the elements of [(1, 2)] with denominator <= 6."""
rel = lambda x, y: x[0] * y[1] == y[0] * x[1]
W = [(a, b) for a in range(-40, 41) for b in range(1, 21)]
cls = lambda x: {y for y in W if rel(x, y)}
QUOTED = {"half_small": [(1, 2), (2, 4), (3, 6)], "two_thirds": [(4, 6), (6, 9)]}
assert cls((1, 2)) == {(k, 2 * k) for k in range(1, 11)}
assert cls((-2, 1)) == {(-2 * s, s) for s in range(1, 21)}
assert cls((0, 1)) == {(0, s) for s in range(1, 21)}
assert sorted(y for y in cls((1, 2)) if y[1] <= 6) == QUOTED["half_small"]
assert all(rel((2, 3), y) for y in QUOTED["two_thirds"])
assert 2 * 6 == 4 * 3 and 2 * 9 == 6 * 3
print("def-rationals-as-classes: all quoted values check")
