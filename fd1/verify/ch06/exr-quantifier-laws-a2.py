"""exr-quantifier-laws-a2 (Section 6.2): (i) over N, "every multiple of 3 is odd" is false at 6;
(j) over {a, b}, the expansions of exists x (P and Q) and (exists x P) and (exists x Q), with the
quoted values making the second true and the first false; (l) over Z, P = multiple of 4,
Q = even: the premise is true on a test range and the line fails at 2."""
from itertools import product
# (i)
assert 6 % 3 == 0 and 6 % 2 == 0
assert not all(n % 2 == 1 for n in range(0, 101) if n % 3 == 0)
# (j)
first = lambda Pa, Pb, Qa, Qb: (Pa and Qa) or (Pb and Qb)
second = lambda Pa, Pb, Qa, Qb: (Pa or Pb) and (Qa or Qb)
v = dict(Pa=True, Qb=True, Pb=False, Qa=False)
assert second(**v) and not first(**v)
# the expansion of the one-way law: first entails second in every row
for Pa, Pb, Qa, Qb in product([True, False], repeat=4):
    assert (not first(Pa, Pb, Qa, Qb)) or second(Pa, Pb, Qa, Qb)
# (l)
Z = range(-50, 51)
P = lambda n: n % 4 == 0
Q = lambda n: n % 2 == 0
assert all((not P(n)) or Q(n) for n in Z)
assert not ((not (not P(2))) or (not Q(2)))   # not P(2) -> not Q(2) is false
print("exr-quantifier-laws-a2: ok")
