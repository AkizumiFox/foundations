"""exr-using-an-implication-b5 (Section 1.3): (a)-(c) the added premises make the sequents
valid (truth tables); (d)(i)-(iii) true for -50 <= n <= 50, (iv) false at n = 2."""
import itertools

QUOTED = {"counterexample (iv)": 2}
RANGE = (-50, 50)     # integers checked; not quoted in the text
imp = lambda a, b: (not a) or b
for P, Q, R in itertools.product((False, True), repeat=3):
    # (a) P -> Q, Q -> R with P, or with Q, or with P and Q, give R
    if imp(P, Q) and imp(Q, R) and (P or Q):
        assert R
    # (b) P, (P and Q) -> R with Q gives R
    if P and imp(P and Q, R) and Q:
        assert R
    # (c) P, Q with P -> R, Q -> R, (P and Q) -> R or R gives R and P
    for extra in (imp(P, R), imp(Q, R), imp(P and Q, R), R):
        if P and Q and extra:
            assert R and P
d = lambda a, b: b % a == 0
lo, hi = RANGE
for n in range(lo, hi + 1):
    assert imp(d(4, n), d(2, n))                  # (i)
    assert imp(d(2, n), d(4, n * n))              # (ii)
    assert imp(d(2, n * n), d(2, n))              # (iii)
assert not all(imp(d(4, n * n), d(4, n)) for n in range(lo, hi + 1))
n = QUOTED["counterexample (iv)"]
assert d(4, n * n) and not d(4, n)
print("exr-using-an-implication-b5: checks")
