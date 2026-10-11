"""thm-reals-uncountable-decimal, aftermath: list x_1 = 1/2, x_n = 0 (n >= 2), expansions
not ending in 9s: 0.5000..., 0.000...; naive rule e_n = 9 - d_nn gives 4, 9, 9, ... (= 1/2);
the 4/5 rule gives 4, 5, 5, ... = 41/90; and 0.4 <= y <= 0.6 for any 4/5 digit sequence."""
from fractions import Fraction as Fr

QUOTED = {"naive": (4, 9, 9, 9), "rule45": (4, 5, 5, 5), "y_num": 41, "y_den": 90}


def diag(n):  # d_{n,n} for the list
    return 5 if n == 1 else 0


naive = tuple(9 - diag(n) for n in range(1, 5))
rule = tuple(5 if diag(n) != 5 else 4 for n in range(1, 5))
assert naive == QUOTED["naive"] and rule == QUOTED["rule45"]


def t(d, n):
    return sum(Fr(d(k), 10**k) for k in range(1, n + 1))


naive_d = lambda k: 4 if k == 1 else 9
rule_d = lambda k: 4 if k == 1 else 5
y = Fr(QUOTED["y_num"], QUOTED["y_den"])
for n in range(1, 40):
    assert t(naive_d, n) <= Fr(1, 2) <= t(naive_d, n) + Fr(1, 10**n)   # naive number is x_1
    assert t(rule_d, n) <= y <= t(rule_d, n) + Fr(1, 10**n)             # 0.4555... = 41/90
assert y != Fr(1, 2) and y != 0
# any digit sequence with digits in {4,5}: t_1 in {0.4, 0.5}, so 0.4 <= y <= t_1 + 0.1 <= 0.6
for e1 in (4, 5):
    assert Fr(4, 10) <= Fr(e1, 10) and Fr(e1, 10) + Fr(1, 10) <= Fr(6, 10)
print("thm-reals-uncountable-decimal: all quoted values check")
