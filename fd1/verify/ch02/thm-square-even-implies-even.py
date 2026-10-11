"""thm-square-even-implies-even (Ch 2, Section 2.1): (E3) (2k+1)^2 = 4k^2+4k+1 = 2(2k^2+2k)+1;
(E1), (E2) on a range; the theorem itself on a range (independent check by residues)."""
QUOTED = {"(2k+1)^2 coefficients": (4, 4, 1), "odd part": (2, 2)}  # 2k^2 + 2k

a, b, c = QUOTED["(2k+1)^2 coefficients"]
u, v = QUOTED["odd part"]
for k in range(-300, 301):
    n = 2 * k + 1
    assert n * n == a * k * k + b * k + c == 2 * (u * k * k + v * k) + 1
for n in range(-1000, 1001):
    even, odd = n % 2 == 0, n % 2 == 1
    assert even or odd                 # (E1)
    assert not (even and odd)          # (E2)
    if odd:
        assert (n * n) % 2 == 1        # (E3)
    if (n * n) % 2 == 0:
        assert n % 2 == 0              # the theorem
print("thm-square-even-implies-even: all quoted values check")
