"""thm-integers-mod-n-ring: the Quick check in Z/12Z and Z/1Z; (b) and (d) on small n."""
QUOTED = {"sum": (15, 1, 3), "prod": (56, 4, 8), "size_Z1": 1}
s, q, r = QUOTED["sum"]
assert 7 + 8 == s == q * 12 + r and 0 <= r < 12
p, q, r = QUOTED["prod"]
assert 7 * 8 == p == q * 12 + r and 0 <= r < 12
assert len({a % 1 for a in range(-20, 21)}) == QUOTED["size_Z1"]
for n in range(1, 30):
    classes = {a % n for a in range(-200, 201)}
    assert classes == set(range(n)) and len(classes) == n
    # k . [1] = [k] by the recursion
    m = 0
    for k in range(0, 3 * n):
        assert m == k % n
        m = (m + 1) % n
    assert (n % n == 0)
print("thm-integers-mod-n-ring: ok")
