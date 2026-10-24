"""exr-translation-b3 (Section 6.1): the twenty formulas against their sentences over N.

Universal quantifiers range over 0..U, existential ones over 0..W (W > U),
so that witnesses for the cut-off universal cases exist.  Each formula is
evaluated literally, quantifier by quantifier; each sentence is computed
independently by trial division.
"""


def isprime(n):
    return n >= 2 and all(n % d for d in range(2, int(n ** 0.5) + 1))


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def primefactors(n):
    return [d for d in divisors(n) if isprime(d)]


QUOTED = {"19": True, "20": False, "16 counterexample": (0, 1),
          "20 counterexamples": [2, 4, 8, 16, 32]}

U, W = 60, 200
UA, WE = range(0, U + 1), range(0, W + 1)
P = isprime
E = lambda x: x % 2 == 0
dv = lambda x, y: any(y == x * k for k in range(0, y + 1)) if y > 0 else True  # x | y
imp = lambda a, b: (not a) or b
A = lambda f: all(f(x) for x in UA)
X = lambda f: any(f(x) for x in WE)

formula = {
    1: E(2) and P(2),
    2: X(lambda x: P(x) and dv(x, 9)),
    3: A(lambda x: imp(P(x) and 2 < x, not E(x))),
    4: not X(lambda x: P(x) and x < 2),
    5: A(lambda x: imp(E(x), dv(2, x))),
    6: A(lambda x: imp(dv(x, 9), not E(x))),
    7: A(lambda x: dv(1, x)),
    8: X(lambda x: A(lambda y: dv(x, y))),
    9: A(lambda y: X(lambda x: dv(x, y))),
    10: A(lambda x: imp(P(x), X(lambda y: P(y) and x < y))),
    11: A(lambda x: X(lambda y: x < y and P(y))),
    12: A(lambda x: imp(1 < x, X(lambda y: P(y) and dv(y, x)))),
    13: A(lambda x: imp(P(x), A(lambda y: imp(dv(y, x), y == 1 or y == x)))),
    14: A(lambda x: imp(dv(x, 2), x == 1 or x == 2)),
    15: not A(lambda x: imp(not E(x), P(x))),
    16: A(lambda x: A(lambda y: imp(x < y, X(lambda z: x < z and z < y)))),
    17: X(lambda x: P(x) and A(lambda y: imp(E(y), dv(x, y)))),
    18: A(lambda x: imp(dv(x, 1), x == 1)),
    19: A(lambda x: A(lambda y: imp(dv(x, y) and dv(y, x), x == y))),
    20: A(lambda x: imp(E(x), X(lambda y: P(y) and dv(y, x) and not (y == 2)))),
}

# the sentences, computed independently (divisors of 0: every number)
divs = lambda n: set(range(0, W + 1)) if n == 0 else set(divisors(n))
sentence = {
    1: 2 % 2 == 0 and isprime(2),
    2: any(isprime(d) for d in divs(9)),
    3: all(x % 2 == 1 for x in UA if isprime(x) and x > 2),
    4: not any(isprime(x) for x in (0, 1)),
    5: all(x % 2 == 0 for x in UA if x % 2 == 0),
    6: all(d % 2 == 1 for d in divs(9)),
    7: all(x % 1 == 0 for x in UA),
    8: True,   # 1 divides every number
    9: True,   # every number divides itself (0 | 0)
    10: True,  # Euclid
    11: True,  # Euclid
    12: all(len(primefactors(x)) > 0 for x in UA if x > 1),
    13: all(divs(x) == {1, x} for x in UA if isprime(x)),
    14: divs(2) == {1, 2},
    15: any(x % 2 == 1 and not isprime(x) for x in UA),  # 1, 9, ...
    16: False,  # nothing strictly between 0 and 1
    17: True,   # 2 divides every even number
    18: divs(1) == {1},
}
for k, v in sentence.items():
    assert formula[k] == v, (k, formula[k], v)
assert formula[19] is QUOTED["19"] and formula[20] is QUOTED["20"]
# 19: if y = xk and x = yl then x = 0 = y or k = l = 1
for x in range(0, 40):
    for y in range(0, 40):
        if dv(x, y) and dv(y, x):
            assert x == y
# 20 fails at every power of 2 (only prime divisor 2)
for x in QUOTED["20 counterexamples"]:
    assert primefactors(x) == [2]
# 16 fails at (0, 1); 10 and 11 both true
x, y = QUOTED["16 counterexample"]
assert x < y and not any(x < z < y for z in WE)
assert formula[10] and formula[11]
print("exr-translation-b3: all quoted values check")
