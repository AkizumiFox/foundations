"""exm-search-with-witnesses (Section 6.3): the reading over Z.
P(x): x > 0; R(x, y): y = 2x + 1; Q(y): y odd. All three premises and the conclusion true
(checked on a window of integers, where every needed witness lies)."""
W = range(-200, 201)
P = lambda x: x > 0
R = lambda x, y: y == 2 * x + 1
Q = lambda y: y % 2 == 1
# premise 1: every positive x has some y with R(x, y): y = 2x + 1
assert all((not P(x)) or R(x, 2 * x + 1) for x in W)
# premise 2: R(x, y) -> Q(y)
assert all((not R(x, y)) or Q(y) for x in W for y in range(-401, 402))
# premise 3: some integer is positive
assert any(P(x) for x in W)
# conclusion: some integer is odd
assert any(Q(y) for y in W)
print("exm-search-with-witnesses: all quoted values check")
