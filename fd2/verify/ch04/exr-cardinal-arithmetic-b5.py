"""exr-cardinal-arithmetic-b5 (c): s(n) = 0 before place n, 1 from place n on.
On prefixes of length L: s(n) is not eventually zero (its tail is all 1s), and s(m), s(n)
differ at place min(m, n) when m != n."""
L = 40


def s(n):
    return [0 if k < n else 1 for k in range(L)]


for n in range(L // 2):
    assert all(s(n)[k] == 1 for k in range(n, L))
    for m in range(L // 2):
        if m != n:
            j = min(m, n)
            assert s(m)[j] != s(n)[j]
            assert s(m)[:j] == s(n)[:j]
# (b): s(n) = n + 2 lands in R \ {0, 1} and is injective on a range
assert all(n + 2 not in (0, 1) for n in range(1000))
print("ok")
