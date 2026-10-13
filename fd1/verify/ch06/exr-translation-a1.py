"""exr-translation-a1 (Ch 4, Section 4.8): the counterexamples and witnesses of (a)(v) and (b)."""

QUOTED = {"(b)(ii) x outside A": 7, "(a)(v) d": 1}

W = range(-50, 51)
A, B = {0}, {5}
# (b)(ii): the sentence in words is false (0 > 5 fails), but x = 7 is not in A
assert not any(all(x > y for y in B) for x in A)
assert 7 not in A
# (b)(iii) over N: y + 1 > y, but no natural number exceeds every natural number
N = range(0, 200)
assert all(y + 1 > y and y + 1 >= 0 for y in N)
assert not any(all(x > y for y in N) for x in N)
# (a)(v): d = 1 divides every n, with k = n
assert all(n == 1 * n for n in W)
print("exr-translation-a1: all quoted values check")
