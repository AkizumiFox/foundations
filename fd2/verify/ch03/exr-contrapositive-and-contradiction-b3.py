"""exr-contrapositive-and-contradiction-b3 (F2.2 §04): n < 2^n for n >= 1; 1 < 2; m - 1 < 2^(m-1) gives m <= 2^(m-1) < 2^m."""
assert 1 < 2 ** 1
for m in range(2, 500):
    assert m - 1 < 2 ** (m - 1) and m <= 2 ** (m - 1) < 2 ** m
for n in range(1, 2000):
    assert n < 2 ** n
print("exr-contrapositive-and-contradiction-b3: all quoted values check")
