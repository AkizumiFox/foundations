"""exm-universal-elimination-derivations (Ch 4, Section 4.3), part (d): the arithmetic reading
f(n) = n + 2, P = even, c = 0 gives f(f(0)) = 4, and evens are closed under f."""
QUOTED = {"c": 0, "f(f(c))": 4}

f = lambda n: n + 2
even = lambda n: n % 2 == 0
assert all(even(f(n)) for n in range(0, 2000, 2))      # premise: P(x) -> P(f(x)) on evens
assert all(even(n) <= even(f(n)) for n in range(0, 2000))
assert even(QUOTED["c"])
assert f(f(QUOTED["c"])) == QUOTED["f(f(c))"] and even(QUOTED["f(f(c))"])
print("exm-universal-elimination-derivations: all quoted values check")
