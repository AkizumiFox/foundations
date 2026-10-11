"""exr-a-cauchy-sequence-without-a-limit-r2: 2^n >= n + 1; 2(n + 1) = 2n + 2 >= n + 2, strict for n >= 1."""
QUOTED = {"base": (1, 1)}
for n in range(200):
    assert 2**n >= n + 1
    assert 2*(n + 1) == 2*n + 2 >= n + 2
    assert (n + 2 < 2*n + 2) == (n >= 1)
assert (2**0, 0 + 1) == QUOTED["base"]
print("ok")
