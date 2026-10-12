"""exr-disjunction-and-cases-b3 (Ch 1, Section 1.6, recast): the sequent P or Q, P -> R,
Q -> (S and T) |- R or T is valid; (2k)^2 = 4k^2; (2k+1)^2 = 4k(k+1) + 1 = 8m + 1 with
k(k+1) = 2m; n^2 mod 8 is 0, 1 or 4, the even case 0 mod 4 and the odd case 1 mod 8;
36 = 4 * 9, 49 = 8 * 6 + 1."""
from _s06s07_logic import V, And, Or, Imp, classically_valid

QUOTED = {"6^2": (36, 4, 9, 0), "7^2": (49, 8, 6, 1)}
P, Q, R, S, T = V("P"), V("Q"), V("R"), V("S"), V("T")
assert classically_valid([Or(P, Q), Imp(P, R), Imp(Q, And(S, T))], Or(R, T))
for k in range(-200, 201):
    assert (2 * k) ** 2 == 4 * k * k
    assert (2 * k + 1) ** 2 == 4 * k * (k + 1) + 1
    assert k * (k + 1) % 2 == 0
    m = k * (k + 1) // 2
    assert (2 * k + 1) ** 2 == 8 * m + 1
for n in range(-100, 101):
    assert n * n % 8 in (0, 1, 4)
    if n % 2 == 0:
        assert n * n % 4 == 0
    else:
        assert n * n % 8 == 1 and n * n % 2 == 1
for base, (sq, d, q, r) in ((6, QUOTED["6^2"]), (7, QUOTED["7^2"])):
    assert base ** 2 == sq == d * q + r
print("exr-disjunction-and-cases-b3: all quoted values check")
