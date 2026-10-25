"""exr-countable-unions-and-choice-a1 (c): A_n = {n, n+1}, lists c(n)(m) = n for odd m,
n + 1 for even m; J = N (all A_n non-empty); F(3, 2) = c(3)(2) = 4; each c(n) is onto A_n."""

QUOTED = {"F(3,2)": 4}


def c(n, m):
    return n if m % 2 == 1 else n + 1


assert c(3, 2) == QUOTED["F(3,2)"]
for n in range(50):
    A = {n, n + 1}
    assert {c(n, m) for m in range(10)} == A      # onto A_n (m = 0 and m = 1 suffice)
    assert c(n, 1) == n and c(n, 0) == n + 1
print("exr-countable-unions-and-choice-a1: all quoted values check")
