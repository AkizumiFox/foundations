"""exm-cubes-plus-five-n (F2.1 §01): both case expansions of n^3 + 5n.
Each identity is between polynomials in k of degree <= 3, so agreement at 41 points proves it."""
QUOTED = {"even": "2(4k^3 + 5k)", "odd": "2(4k^3 + 6k^2 + 8k + 3)", "odd_sum": "8k^3 + 12k^2 + 16k + 6"}
K = range(-20, 21)
for k in K:
    n = 2 * k
    assert n**3 + 5 * n == 8 * k**3 + 10 * k == 2 * (4 * k**3 + 5 * k)
    n = 2 * k + 1
    assert n**3 == 8 * k**3 + 12 * k**2 + 6 * k + 1 and 5 * n == 10 * k + 5
    assert n**3 + 5 * n == 8 * k**3 + 12 * k**2 + 16 * k + 6 == 2 * (4 * k**3 + 6 * k**2 + 8 * k + 3)
assert all((m**3 + 5 * m) % 2 == 0 for m in range(-50, 51))
print("exm-cubes-plus-five-n: all quoted values check")
