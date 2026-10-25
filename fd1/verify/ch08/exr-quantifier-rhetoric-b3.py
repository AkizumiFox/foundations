"""exr-quantifier-rhetoric-b3 (Ch 8, Section 8.2): {n : 6 | n} = {n : 2 | n and 3 | n};
n = 6k gives n = 2(3k) = 3(2k); 2a = 3b gives b = 2(a - b) and n = 6(a - b)."""
RANGE = 600  # test range, not quoted in the text

R = RANGE
for n in range(-R, R + 1):
    inA = n % 6 == 0
    inB = n % 2 == 0 and n % 3 == 0
    assert inA == inB
    if inA:
        k = n // 6
        assert n == 2 * (3 * k) == 3 * (2 * k)
    if inB:
        a, b = n // 2, n // 3
        assert n == 2 * a == 3 * b
        assert b == 3 * b - 2 * b == n - 2 * b == 2 * a - 2 * b == 2 * (a - b)
        assert n == 3 * b == 6 * (a - b)
print("exr-quantifier-rhetoric-b3: all quoted values check")
