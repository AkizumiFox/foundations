"""thm-division-algorithm (Ch 7, 02): existence and uniqueness on a range; the witnesses q = 0 (a >= 0)
and q = a (a < 0) put a - qn in R; -7 = 3 * (-3) + 2; parity and the n = 3 classes; 4k + 1, 4k + 3 odd;
no integer m has 2m = 1."""
QUOTED = {"ex": (-7, 3, -3, 2)}
for a in range(-200, 201):
    for n in range(1, 25):
        q0 = 0 if a >= 0 else a
        assert a - q0 * n >= 0
        R = [a - q * n for q in range(-300, 301) if a - q * n >= 0]
        r = min(R)
        q = (a - r) // n
        assert a == q * n + r and 0 <= r < n
        sols = [(qq, rr) for qq in range(-300, 301) for rr in [a - qq * n] if 0 <= rr < n]
        assert sols == [(q, r)]
a, n, q, r = QUOTED["ex"]
assert a == q * n + r and 0 <= r < n
for a in range(-100, 101):
    assert (a % 2) in (0, 1) and (a % 3) in (0, 1, 2)
for k in range(-50, 51):
    assert (4 * k + 1) % 2 == 1 and (4 * k + 3) % 2 == 1
    assert 4 * k + 1 == 2 * (2 * k) + 1 and 4 * k + 3 == 2 * (2 * k + 1) + 1
assert all(2 * m != 1 for m in range(-100, 101))
print("thm-division-algorithm: all quoted values check")
