"""exr-induction-b5 (Ch 4, Section 4.2): a_0 = 2, a_1 = 3, a_(n+2) = 3a_(n+1) - 2a_n gives a_n = 2^n + 1."""
QUOTED = {"a_0": 2, "a_1": 3, "a_2": 5}

a = [2, 3]
for n in range(0, 300):
    a.append(3 * a[n + 1] - 2 * a[n])
assert all(a[n] == 2 ** n + 1 for n in range(len(a)))
assert a[2] == 3 * 3 - 2 * 2 == 5
for n in range(2, 300):
    assert 3 * (2 ** (n - 1) + 1) - 2 * (2 ** (n - 2) + 1) == 3 * 2 ** (n - 1) - 2 ** (n - 1) + 1 == 2 ** n + 1
print("exr-induction-b5: all quoted values check")
