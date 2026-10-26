"""lem-integer-multiples: (a)-(d) checked in Z/nZ for n = 1..12 and integers m, k in [-15, 15],
with the multiple defined by the recursion and n.a := -((-n).a) for n < 0 (independent of ring
multiplication). Quick check: (-3).[2] = [4] in Z/5Z."""
QUOTED = {"check": (5, -3, 2, 4)}  # in Z/5Z, (-3).[2] = [4]


def mult(n, a, mod):
    """n.a in Z/modZ by the recursion of F3.2 and the negative-multiple definition."""
    if n < 0:
        return (-mult(-n, a, mod)) % mod
    s = 0
    for _ in range(n):
        s = (s + a) % mod
    return s


R = range(-15, 16)
for mod in range(1, 13):
    one = 1 % mod
    for m in R:
        for k in R:
            assert (mult(m, one, mod) + mult(k, one, mod)) % mod == mult(m + k, one, mod)
            assert (mult(m, one, mod) * mult(k, one, mod)) % mod == mult(m * k, one, mod)
            for a in range(mod):
                assert (mult(m, one, mod) * a) % mod == mult(m, a, mod)
                assert mult(m + k, a, mod) == (mult(m, a, mod) + mult(k, a, mod)) % mod
                assert mult(-m, a, mod) == (-mult(m, a, mod)) % mod
                assert mult(m * k, a, mod) == mult(m, mult(k, a, mod), mod)
                for b in range(mod):
                    assert mult(m, (a + b) % mod, mod) == (mult(m, a, mod) + mult(m, b, mod)) % mod
                    assert (mult(m, a, mod) * b) % mod == mult(m, (a * b) % mod, mod)
mod, n, a, val = QUOTED["check"]
assert mult(n, a, mod) == val
assert (mult(n, 1, mod) * a) % mod == val
assert (-6 - 4) % 5 == 0
print("ok")
