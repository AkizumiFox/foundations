"""Gate 0, P4: a0 = 0, a1 = 1, a_{n+2} = 3 a_{n+1} - 2 a_n; and the variant a1 = 2."""
QUOTED = {"variant": {"a2": 6, "a3": 14}, "formula_values": {2: 3, 3: 7},
          "points": [1, 2, 3, 1, 1, 2]}
assert sum(QUOTED["points"]) == 10


def seq(a0, a1, n):
    a = [a0, a1]
    while len(a) < n:
        a.append(3 * a[-1] - 2 * a[-2])
    return a


a = seq(0, 1, 80)
assert all(a[n] == 2**n - 1 for n in range(80))
# the step's algebra
assert all(3 * (2**(n + 1) - 1) - 2 * (2**n - 1) == 3 * 2**(n + 1) - 2**(n + 1) - 1
           == 2 * 2**(n + 1) - 1 == 2**(n + 2) - 1 for n in range(80))
b = seq(0, 2, 80)
assert b[2] == QUOTED["variant"]["a2"] and b[3] == QUOTED["variant"]["a3"]
assert 3 * 2 - 2 * 0 == 6 and 3 * 6 - 2 * 2 == 14
for k, v in QUOTED["formula_values"].items():
    assert 2**k - 1 == v
assert all(b[n] == 2**(n + 1) - 2 for n in range(80))
print("ok")
