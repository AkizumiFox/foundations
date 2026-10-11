"""exr-induction-in-practice-b3 (Ch 7, 02): 17 = 5*3 + 2; -17 = 5*(-4) + 3; odd squares are 8t + 1;
2 | n and 3 | n imply 6 | n; 2 = 3*0 + 2, 4 = 3*1 + 1."""
QUOTED = {(17, 5): (3, 2), (-17, 5): (-4, 3)}
for (a, n), (q, r) in QUOTED.items():
    assert a == q * n + r and 0 <= r < n and divmod(a, n) == (q, r)
for k in range(-200, 200):
    x = 2 * k + 1
    assert x * x == 4 * k * (k + 1) + 1 and (k * (k + 1)) % 2 == 0 and x * x % 8 == 1
for n in range(-600, 600):
    if n % 2 == 0 and n % 3 == 0:
        assert n % 6 == 0
assert divmod(2, 3) == (0, 2) and divmod(4, 3) == (1, 1)
print("exr-induction-in-practice-b3: all quoted values check")
