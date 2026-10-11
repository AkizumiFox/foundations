"""thm-completeness (Section 3.6, the warning after exm-completeness-run): n atoms give 2^n row
derivations and 2^n - 1 splittings; for n = 10, 1024 and 1023. The splitting count follows the
proof: splitting on p_j is done once for each assignment to p_1, ..., p_{j-1}."""
QUOTED = {"rows n=10": 1024, "splittings n=10": 1023}
for n in range(0, 12):
    assert sum(2 ** (j - 1) for j in range(1, n + 1)) == 2 ** n - 1
assert 2 ** 10 == 1024 and 2 ** 10 - 1 == 1023
print("thm-completeness: all quoted values check")
