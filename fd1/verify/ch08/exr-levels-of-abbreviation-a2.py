"""exr-levels-of-abbreviation-a2 (Section 8.3 drill): (i) P and Q |= P (TAUT, and-E);
(j) P |= Q fails in the row P true, Q false (two letters on the skeleton);
(k) 2^(n+1) = 2^n + 2^n, and for n >= 1 with 2^n > n: 2^n >= 1 and
2^n + 2^n > n + 2^n >= n + 1, so 2^(n+1) > n + 1."""
from itertools import product

for P, Q in product([True, False], repeat=2):
    if P and Q:
        assert P                          # (i): every row making P and Q true makes P true
assert any(P and not Q for P, Q in product([True, False], repeat=2))   # (j): a refuting row
for n in range(1, 200):
    assert 2 ** (n + 1) == 2 * 2 ** n == 2 ** n + 2 ** n
    assert 2 ** n > n and 2 ** n >= 1
    assert 2 ** n + 2 ** n > n + 2 ** n >= n + 1
    assert 2 ** (n + 1) > n + 1
print("exr-levels-of-abbreviation-a2: all quoted values check")
