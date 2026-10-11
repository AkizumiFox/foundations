"""exr-contradiction-and-vacuous-truth-b2 (Ch 2, Section 2.1): n = 2k gives n + 1 = 2k + 1 (odd);
the claim "n + 1 even => n odd" on a range."""
QUOTED = {"n + 1 for n = 2k": (2, 1)}  # 2k + 1

s, t = QUOTED["n + 1 for n = 2k"]
for k in range(-500, 501):
    n = 2 * k
    assert n + 1 == s * k + t and (n + 1) % 2 == 1
for n in range(-1000, 1001):
    if (n + 1) % 2 == 0:
        assert n % 2 == 1
print("exr-contradiction-and-vacuous-truth-b2: all quoted values check")
