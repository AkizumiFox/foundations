"""exr-quantifier-laws-b4 (Section 6.2): the readings of (b), (d), (f) over Z, cut to [-50, 50].
(b) P even, Q odd: premise true, conclusion false at 0. (d) P even, Q positive: premise true
(witnesses 2 and 1), conclusion false at 0. (f) P even, Q(x): x = 0: premise true (witness 0),
conclusion false at 1."""
Z = range(-50, 51)
ALL = lambda p: all(p(n) for n in Z)
EX = lambda p: any(p(n) for n in Z)
even = lambda n: n % 2 == 0
odd = lambda n: n % 2 == 1
pos = lambda n: n > 0
zero = lambda n: n == 0
# (b)
prem = ALL(even) == ALL(odd)
concl = ALL(lambda n: even(n) == odd(n))
assert prem and not concl and even(0) != odd(0)
# (d)
assert even(2) and pos(1)
prem = (not EX(even)) or EX(pos)
concl = ALL(lambda n: (not even(n)) or pos(n))
assert prem and not concl and even(0) and not pos(0)
# (f)
assert zero(0)
prem = ALL(even) or EX(zero)
concl = ALL(lambda n: even(n) or zero(n))
assert prem and not concl and not even(1) and not zero(1)
print("exr-quantifier-laws-b4: ok")
