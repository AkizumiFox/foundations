"""ax-induction (Ch 4, Section 4.2): the warning's flawed induction for 2^n >= n^2; the Quick check on 5^n - 1."""
QUOTED = {"2^3": 8, "3^2": 9, "step valid from": "holds only for \\( n \\ge 3 \\)"}

# 2 n^2 >= (n+1)^2 exactly when n >= 3 (among n in N, which starts at 0)
assert [n for n in range(0, 50) if 2 * n * n < (n + 1) ** 2] == [0, 1, 2]
# the claim: true at 0, 1, 2 (base case 2^0 = 1 >= 0), false at 3, true again from 4 on
assert 2 ** 0 == 1 >= 0 and 2 ** 1 == 2 >= 1
assert [n for n in range(0, 200) if 2 ** n < n * n] == [3]
assert 2 ** 3 == 8 and 3 ** 2 == 9 and 2 ** 4 == 16 == 4 ** 2
# the Quick check after exm-power-inequality: 4 | 5^n - 1, with step identity
for n in range(0, 200):
    assert (5 ** n - 1) % 4 == 0 and 5 ** (n + 1) - 1 == 5 * (5 ** n - 1) + 4
assert 5 ** 0 - 1 == 0
print("ax-induction: all quoted values check")
