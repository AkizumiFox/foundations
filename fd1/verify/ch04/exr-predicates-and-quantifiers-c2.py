"""exr-predicates-and-quantifiers-c2 (Ch 4, Section 4.1): the wrong connective under forall and exists."""
from fractions import Fraction as Fr

QUOTED = {"A for (a), first": {1}, "A for (a), second": {-1}, "counterexample": 0, "witness": 1}

R = sorted({Fr(p, q) for p in range(-20, 21) for q in range(1, 5)})   # finite sample of R


def forall_and(A):          # forall x (x in A and x > 0), on the sample
    return all(x in A and x > 0 for x in R)


def exists_imp(A):          # exists x (x in A -> x > 0), on the sample
    return any((x not in A) or x > 0 for x in R)


# (a) first: every element of {1} is positive; the mistranslation fails at x = 0
A = {Fr(1)}
assert all(a > 0 for a in A) and not forall_and(A) and not (0 in A)
# (a) second: no element of {-1} is positive; the mistranslation holds with witness 0
A = {Fr(-1)}
assert not any(a > 0 for a in A) and Fr(-1) < 0 and exists_imp(A) and (0 not in A)
# (b) x = 0 is a counterexample to the first for every A, x = 1 a witness for the second
assert not (0 > 0) and 1 > 0
samples = [set(), {Fr(1)}, {Fr(-1)}, {Fr(0)}, {Fr(0), Fr(1)}, set(R)]
for A in samples:
    assert not ((0 in A) and 0 > 0)            # 0 fails x in A and x > 0
    assert (1 not in A) or 1 > 0               # 1 satisfies x in A -> x > 0
    assert not forall_and(A) and exists_imp(A)
print("exr-predicates-and-quantifiers-c2: all quoted values check")
