"""exm-odd-sum-reversal: sum_{k=0}^{n}(2k+1) = (n+1)^2; the paired terms sum to 2n+2; 2S = (n+1)(2n+2) = 2(n+1)^2; check n = 2: 1 + 3 + 5 = 9; constant sum = (n+1)c."""
QUOTED = {"check_n": 2, "check_terms": [1, 3, 5], "check_value": 9}
for n in range(0, 60):
    S = sum(2 * k + 1 for k in range(n + 1))
    assert S == (n + 1) ** 2
    assert all((2 * k + 1) + (2 * (n - k) + 1) == 2 * n + 2 for k in range(n + 1))
    assert 2 * S == (n + 1) * (2 * n + 2) == 2 * (n + 1) ** 2
    for c in (-3, 0, 5):
        assert sum(c for _ in range(n + 1)) == (n + 1) * c
n = QUOTED["check_n"]
assert [2 * k + 1 for k in range(n + 1)] == QUOTED["check_terms"]
assert sum(QUOTED["check_terms"]) == QUOTED["check_value"] == 3 ** 2
print("ok")
