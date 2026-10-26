"""exr-division-with-remainder-a1 (a): quotient and remainder by 6 of 47, -47, 0."""
QUOTED = {47: (7, 5), -47: (-8, 1), 0: (0, 0)}
for a, (q, r) in QUOTED.items():
    assert a == q * 6 + r and 0 <= r < 6
    assert divmod(a, 6) == (q, r)  # Python's divmod uses the floor convention
assert -8 * 6 == -48 and -48 + 1 == -47
assert -47 == -7 * 6 - 5  # the look-alike pair (-7, -5) is not a division with remainder
print("ok")
