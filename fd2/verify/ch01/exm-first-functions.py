"""exm-first-functions and the quick check after exm-not-a-function (Ch 6 Section 6.4):
the listed graphs satisfy (Fn1)/(Fn2) or fail the named clause; indicator ranges."""
import sys
sys.path.insert(0, "verify/ch06")
from _sets import is_function, subsets

QUOTED = {"clauses checked": True}

X = {1, 2, 3}
assert is_function({(1, "a"), (2, "b"), (3, "a")}, X, {"a", "b"})
# quick check: constant 2 is a function; {(1,1),(2,2)} fails F1 at 3; the third fails F2 at 2
assert is_function({(1, 2), (2, 2), (3, 2)}, X, X)
r2 = {(1, 1), (2, 2)}
assert not any(a == 3 for a, _ in r2)
r3 = {(1, 3), (2, 1), (3, 2), (2, 3)}
assert sorted(b for a, b in r3 if a == 2) == [1, 3]
# indicator ranges
for A in subsets(X):
    rng = {1 if x in A else 0 for x in X}
    if A and set(X) - A:
        assert rng == {0, 1}
    elif not A:
        assert rng == {0}
    else:
        assert rng == {1}
print("exm-first-functions: all quoted values check")
