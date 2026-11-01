"""exr-frobenius-and-fermat-r3: in the four-element field of exr-finite-fields-from-modular-arithmetic-c1,
1 + 1 = (1 + 1) + (0 + 0)alpha = 0 (coefficients in F_2), so 2.1 = 0; i^2 = -1 in Q(i) subset C."""
QUOTED = {"one": (1, 0)}


def add(u, v):
    return ((u[0] + v[0]) % 2, (u[1] + v[1]) % 2)


one = QUOTED["one"]
assert add(one, one) == (0, 0)
assert complex(0, 1) ** 2 == -1
print("ok")
