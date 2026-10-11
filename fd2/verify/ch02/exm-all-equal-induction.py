"""exm-all-equal-induction (Ch 7, 02): the lists x_1..x_n and x_2..x_{n+1} share an entry iff n >= 2;
the counterexample x_1 = 0, x_2 = 1."""
QUOTED = {"smallest_n": 2}
share = [n for n in range(1, 50) if set(range(1, n + 1)) & set(range(2, n + 2))]
assert min(share) == QUOTED["smallest_n"] and share == list(range(2, 50))
x = [0, 1]
assert x[0] != x[1]
print("exm-all-equal-induction: all quoted values check")
