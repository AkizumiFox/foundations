"""def-characteristic first examples: char F2 = 2, char F3 = 3, Z/6Z has characteristic 6,
the zero ring (Z/1Z) has characteristic 1."""
QUOTED = {"F2": 2, "F3": 3, "Z6": 6, "zero_ring": 1}


def char(mod):
    one = 1 % mod
    s = 0
    for n in range(1, 10 * mod + 2):
        s = (s + one) % mod
        if s == 0:
            return n
    return 0


assert char(2) == QUOTED["F2"]
assert char(3) == QUOTED["F3"]
assert char(6) == QUOTED["Z6"]
assert char(1) == QUOTED["zero_ring"]
# Z/6Z: k.[1] != [0] for k = 1..5
assert all(k % 6 != 0 for k in range(1, 6))
print("ok")
