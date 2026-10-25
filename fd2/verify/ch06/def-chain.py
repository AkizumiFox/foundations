"""Section 6.1, def-chain examples and Quick check: {2^n} is a chain in (N, |), {2, 3} is not;
{{1}, {1, 2}, {3}} is not a chain under inclusion; {0, 1, 5, 25} and {3, 6, 0} are chains in (N, |)."""
from itertools import combinations

QUOTED = {"pow2_chain": True, "two_three": False, "sets_a": False, "b": True, "c": True}


def divides(a, b):
    # a | b iff b = k a for some integer k
    if a == 0:
        return b == 0
    return b % a == 0


def is_chain(xs, le):
    return all(le(x, y) or le(y, x) for x, y in combinations(xs, 2))


assert is_chain([2 ** n for n in range(12)], divides) == QUOTED["pow2_chain"]
assert is_chain([2, 3], divides) == QUOTED["two_three"]
sub = lambda a, b: a <= b
assert is_chain([frozenset({1}), frozenset({1, 2}), frozenset({3})], sub) == QUOTED["sets_a"]
assert is_chain([0, 1, 5, 25], divides) == QUOTED["b"]
assert is_chain([3, 6, 0], divides) == QUOTED["c"]
assert is_chain([frozenset(), frozenset({2}), frozenset({2, 3})], sub)
print("def-chain: all quoted values check")
