"""exr-division-with-remainder-r3: (3q+1)^2 = 3(3q^2+2q)+1, (3q+2)^2 = 3(3q^2+4q+1)+1;
hence 3 | a^2 implies 3 | a."""
QUOTED = {1: ((9, 6, 1), (3, 2, 0)), 2: ((9, 12, 4), (3, 4, 1))}
for q in range(-80, 81):
    for r, ((a, b, c), (u, v, w)) in QUOTED.items():
        x = (3 * q + r) ** 2
        assert x == a * q * q + b * q + c == 3 * (u * q * q + v * q + w) + 1
for a in range(-500, 501):
    if (a * a) % 3 == 0:
        assert a % 3 == 0
print("ok")
