"""ax-induction's warning (Ch 3, Section 3.2): the flawed induction for 2^n >= n^2."""
QUOTED = {"2^3": 8, "3^2": 9, "step valid from": "holds only for \\( n \\ge 3 \\)"}

# 2 n^2 >= (n+1)^2 exactly when n >= 3 (among n in N, which starts at 0)
assert [n for n in range(0, 50) if 2 * n * n < (n + 1) ** 2] == [0, 1, 2]
# the claim: true at 0, 1, 2 (base case 2^0 = 1 >= 0), false at 3, true again from 4 on
assert 2 ** 0 == 1 >= 0 and 2 ** 1 == 2 >= 1
assert [n for n in range(0, 200) if 2 ** n < n * n] == [3]
assert 2 ** 3 == 8 and 3 ** 2 == 9 and 2 ** 4 == 16 == 4 ** 2
print("ax-induction: all quoted values check")
