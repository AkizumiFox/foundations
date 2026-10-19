"""exr-biconditional-and-definitions-b6 (Ch 2, Section 2.4): for |n| <= 500 the four conditions
(n odd; n + 1 even; 8 | n^2 - 1; n^2 odd) agree; n + 1 = 2j gives n^2 - 1 = 4j(j - 1);
k(k - 1) is even."""

QUOTED = {"divisor": 8}

N = 500  # search range, not quoted in the text
for n in range(-N, N + 1):
    conds = [n % 2 == 1, (n + 1) % 2 == 0, (n * n - 1) % QUOTED["divisor"] == 0, (n * n) % 2 == 1]
    assert len(set(conds)) == 1, n
    if (n + 1) % 2 == 0:
        j = (n + 1) // 2
        assert n - 1 == 2 * (j - 1) and n * n - 1 == (n - 1) * (n + 1) == 4 * j * (j - 1)
for k in range(-N, N + 1):
    assert (k * (k - 1)) % 2 == 0
print("exr-biconditional-and-definitions-b6: all quoted values check")
