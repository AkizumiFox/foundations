"""exr-quantifier-laws-b5 (Section 6.2): over Z with P even, Q positive and c read as 0, the
premise exists x (P(x) and Q(x)) is true (witness 2) and the line P(c) and Q(c) is false."""
Z = range(-50, 51)
P = lambda n: n % 2 == 0
Q = lambda n: n > 0
assert P(2) and Q(2)
assert any(P(n) and Q(n) for n in Z)
c = 0
assert not (P(c) and Q(c))
print("exr-quantifier-laws-b5: ok")
