"""exr-biconditional-and-definitions-b5 (Ch 2, Section 2.4): (iii) <=> (iv) on all integer triples
|a|, |b|, |x| <= 20; the triples quoted in (a) and (c); (v) agrees with (i) everywhere."""
import itertools

QUOTED = {"narrow": (5, 2, 3), "broad": (2, 5, 100), "order test": (2, 5, 3)}

def between(a, b, x):           # the intended meaning
    return min(a, b) < x < max(a, b)
c1 = lambda a, b, x: a < x and x < b
c2 = lambda a, b, x: a < x or x < b
c3 = lambda a, b, x: (a < x and x < b) or (b < x and x < a)
c4 = lambda a, b, x: (x - a) * (x - b) < 0
c5 = lambda a, b, x: (not x <= a) and (not b <= x)

R = range(-20, 21)
for a, b, x in itertools.product(R, R, R):
    assert c3(a, b, x) == c4(a, b, x) == between(a, b, x)
    assert c5(a, b, x) == c1(a, b, x)
    assert (not c1(a, b, x)) or between(a, b, x)       # (i) is not too broad
a, b, x = QUOTED["narrow"]
assert between(a, b, x) and not c1(a, b, x) and not c2(a, b, x) and not c5(a, b, x)
assert not (5 < 3) and not (3 < 2)
a, b, x = QUOTED["broad"]
assert c2(a, b, x) and not between(a, b, x)
a, b, x = QUOTED["order test"]
for c in (c1, c2, c5):
    assert c(a, b, x) and not c(b, a, x)
for c in (c3, c4):
    assert c(a, b, x) and c(b, a, x)
print("exr-biconditional-and-definitions-b5: all quoted values check")
